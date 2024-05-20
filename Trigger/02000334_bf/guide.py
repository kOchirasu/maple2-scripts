""" trigger/02000334_bf/guide.xml """
import trigger_api


# 플레이어 감지
class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90099, spawn_ids=[150]):
            # 더미 몬스터 감지
            return 차타이머1(self.ctx)


class 차타이머1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 가이드_01(self.ctx)


class 가이드_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=1, arg2='$02000334_BF__GUIDE__0$', arg3='3000')
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=101, text_id=20000010) # 폭탄을 던지세요
        self.set_effect(trigger_ids=[90021], visible=True) # 이벤트 UI 에 맞는 사운드
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90001, spawn_ids=[301]):
            # 대포 몬스터 감지
            return 차타이머2(self.ctx)
        if self.time_expired(timer_id='5'):
            return 가이드_01_02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=101) # 폭탄을 던지세요


class 가이드_01_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=90001, spawn_ids=[301]):
            # 대포 몬스터 감지
            return 차타이머2(self.ctx)


class 차타이머2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 가이드_02(self.ctx)


class 가이드_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[90100]):
            return 오스칼_배웅(self.ctx)
        if self.monster_dead(spawn_ids=[190]):
            return 가이드_02_02(self.ctx)


class 가이드_02_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[90100]):
            return 오스칼_배웅(self.ctx)


class 오스칼_배웅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=199, patrol_name='MS2PatrolData_2016') # 오스칼 플레이어를 쳐다봄...


initial_state = 대기시간
