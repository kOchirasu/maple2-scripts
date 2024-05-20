""" trigger/02000252_bf/bigdoor_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[165,166,167,168], visible=True)
        self.set_interact_object(trigger_ids=[10000406], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000406], state=0):
            return 열기(self.ctx)


class 열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[9001], trigger_id=998)
        self.set_mesh(trigger_ids=[165,166,167,168])


initial_state = 대기
