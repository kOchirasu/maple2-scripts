""" trigger/02000441_bf/barricade.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[80000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return CheckUser04_GuildRaid(self.ctx)


class CheckUser04_GuildRaid(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30, start_delay=1) # 최대 30초 대기

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 4:
            return MaxCount04_Start(self.ctx)
        if self.count_users(box_id=701) < 4:
            return MaxCount04_Wait(self.ctx)


class MaxCount04_Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 4:
            # 10명이면 바로 시작
            return MaxCount04_Start(self.ctx)
        if self.time_expired(timer_id='1'):
            return MaxCount04_Start(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return MaxCount04_Wait(self.ctx)


class MaxCount04_Start(trigger_api.Trigger):
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
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2038801, key='start', value=1)
        self.set_effect(trigger_ids=[70001])
        self.set_effect(trigger_ids=[70002])
        self.set_effect(trigger_ids=[70003])
        self.set_mesh(trigger_ids=[80000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706]):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000441_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 차단(self.ctx)


class 차단(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[80000], visible=True)
        self.set_effect(trigger_ids=[70001], visible=True)
        self.set_effect(trigger_ids=[70002], visible=True)
        self.set_effect(trigger_ids=[70003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Wait
