""" trigger/81000003_item/trigger_02.xml """
import trigger_api


class 레버(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000225], state=1)
        self.set_mesh(trigger_ids=[530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000225], state=0):
            return 바닥열기(self.ctx)


class 바닥열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='8', seconds=200)
        self.set_mesh(trigger_ids=[530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='8'):
            return 레버(self.ctx)


initial_state = 레버
