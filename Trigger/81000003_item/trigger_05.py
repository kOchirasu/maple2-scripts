""" trigger/81000003_item/trigger_05.xml """
import trigger_api


class 레버(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000214], state=1)
        self.set_mesh(trigger_ids=[551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000214], state=0):
            return 바닥열기(self.ctx)


class 바닥열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=200)
        self.set_mesh(trigger_ids=[551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 레버(self.ctx)


initial_state = 레버
