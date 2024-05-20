""" trigger/99999841/invasion_portal.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990010, key='PCmove', value=0)
        self.set_interact_object(trigger_ids=[10002184], state=2)


class 포탈열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30, start_delay=1)
        self.set_interact_object(trigger_ids=[10002184], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.time_expired(timer_id='1'):
            self.reset_timer(timer_id='1')
            return 포탈닫힘(self.ctx)
        if self.object_interacted(interact_ids=[10002184], state=2):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990010, key='PCmove', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=1000) == 1:
            return 포탈열림(self.ctx)


class 포탈닫힘(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990010, key='PCmove', value=0)
        self.set_timer(timer_id='2', seconds=60, start_delay=1)
        self.set_interact_object(trigger_ids=[10002184], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.time_expired(timer_id='2'):
            self.reset_timer(timer_id='2')
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002184], state=2)


initial_state = 대기
