""" trigger/81000003_item/trigger_04.xml """
import trigger_api


class 레버(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[510,511,512,513,514,515,516], visible=True)
        self.set_effect(trigger_ids=[701])
        self.set_effect(trigger_ids=[702])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[401]):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[510,511,512,513,514,515,516])
        self.set_effect(trigger_ids=[701], visible=True)
        self.set_effect(trigger_ids=[702], visible=True)
        self.set_timer(timer_id='11', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 폭죽끄기(self.ctx)


class 폭죽끄기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=120)
        self.set_effect(trigger_ids=[701])
        self.set_effect(trigger_ids=[702])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 레버(self.ctx)


initial_state = 레버
