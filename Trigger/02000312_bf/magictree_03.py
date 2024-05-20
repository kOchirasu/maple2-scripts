""" trigger/02000312_bf/magictree_03.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001027], state=1)
        self.set_mesh(trigger_ids=[1020,1021,1022,1023,1024], visible=True) # 덩굴

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001027], state=0):
            return Remove(self.ctx)


class Remove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001027], state=0)
        self.set_random_mesh(trigger_ids=[1020,1021,1022,1023,1024], start_delay=5, interval=500, fade=100) # 덩굴
        self.set_user_value(trigger_id=10, key='2ndTreeRemove', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
