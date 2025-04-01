""" trigger/02000334_bf/cannonspawn.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CannonSpawn') == 1:
            return CannonSpawn(self.ctx)


class CannonSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=190, script='$02000334_BF__WAVE__12$', time=3, arg5=1) # 보스 대사
        self.set_dialogue(type=1, spawn_id=199, script='$02000334_BF__MAIN__12$', time=3, arg5=3) # 오스칼 대사
        self.set_timer(timer_id='3', seconds=3, display=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return CannonSpawn_start(self.ctx)


class CannonSpawn_start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9999131, key='cannon_01', value=1)
        self.set_user_value(trigger_id=9999132, key='cannon_02', value=1)
        self.set_user_value(trigger_id=9999133, key='cannon_03', value=1)
        self.spawn_monster(spawn_ids=[301,302,303], auto_target=False) # 대포 생성
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=102, text_id=20000020) # 대포를 쏘세요
        self.set_effect(trigger_ids=[90021], visible=True) # 이벤트 UI 에 맞는 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[190]):
            return Clear(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=102) # 대포를 쏘세요


class Clear(trigger_api.Trigger):
    pass


initial_state = Idle
