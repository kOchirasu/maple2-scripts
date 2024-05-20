""" trigger/81000003_item/trigger_01.xml """
import trigger_api


class 레버(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000223], state=1)
        self.set_interact_object(trigger_ids=[10000214], state=1)
        self.set_mesh(trigger_ids=[307,308,309,310,311,312,313,314,315,316,317,318,319])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000223], state=0):
            return 다리01(self.ctx)


class 다리01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_mesh(trigger_ids=[307,308], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 다리02(self.ctx)


class 다리02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=1)
        self.set_mesh(trigger_ids=[309,310,311], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 다리03(self.ctx)


class 다리03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=1)
        self.set_mesh(trigger_ids=[312,313,314], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 다리04(self.ctx)


class 다리04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=1)
        self.set_mesh(trigger_ids=[315,316,317], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 다리05(self.ctx)


class 다리05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=1)
        self.set_mesh(trigger_ids=[318,319], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 다리06(self.ctx)


class 다리06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 레버(self.ctx)


initial_state = 레버
