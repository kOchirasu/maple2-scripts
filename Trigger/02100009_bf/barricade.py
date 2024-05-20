""" trigger/02100009_bf/barricade.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[80000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return CheckUser10_GuildRaid(self.ctx)


class CheckUser10_GuildRaid(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30, start_delay=1) # 최대 30초 대기

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=102) >= 10:
            return MaxCount10_Start(self.ctx)
        if self.count_users(box_id=102) < 10:
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=102) >= 10:
            # 10명이면 바로 시작
            return MaxCount10_Start(self.ctx)
        if self.time_expired(timer_id='1'):
            return MaxCount10_Start(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 최대 30초 대기 타이머 초기화
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        return DungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=904)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return ShowCaption01(self.ctx)


# 설명문 출력
class ShowCaption01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_intro(text='$02100009_BF__BARRICADE__0$')
        self.set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return ShowCaption01Skip(self.ctx)


class ShowCaption01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return ShowCaption02(self.ctx)


class ShowCaption02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_intro(text='$02100009_BF__BARRICADE__1$')
        self.set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return ShowCaption02Skip(self.ctx)


class ShowCaption02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CloseCaptionSetting(self.ctx)


class CloseCaptionSetting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.close_cinematic()
        self.select_camera(trigger_id=904, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001])
        self.set_effect(trigger_ids=[7002])
        self.set_effect(trigger_ids=[7003])
        self.set_effect(trigger_ids=[7004])
        self.set_mesh(trigger_ids=[8000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[100000001]) or self.monster_in_combat(spawn_ids=[100000002]):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02100009_BF__BARRICADE__2$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 차단(self.ctx)


class 차단(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8000], visible=True)
        self.set_effect(trigger_ids=[7001], visible=True)
        self.set_effect(trigger_ids=[7002], visible=True)
        self.set_effect(trigger_ids=[7003], visible=True)
        self.set_effect(trigger_ids=[7004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[100000001,100000002]):
            return 차단해제(self.ctx)


class 차단해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8000])
        self.set_effect(trigger_ids=[7001])
        self.set_effect(trigger_ids=[7002])
        self.set_effect(trigger_ids=[7003])
        self.set_effect(trigger_ids=[7004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Wait
