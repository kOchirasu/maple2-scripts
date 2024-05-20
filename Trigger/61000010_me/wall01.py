""" trigger/61000010_me/wall01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000042], state=1)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000042], state=0):
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205], visible=True)
            return 쿨타임(self.ctx)


class 쿨타임(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
