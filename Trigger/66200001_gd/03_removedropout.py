""" trigger/66200001_gd/03_removedropout.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return Remove(self.ctx)


class Remove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_to_portal(box_id=9002, user_tag_id=1, portal_id=21) # Tag1=Blue
        self.move_to_portal(box_id=9002, user_tag_id=2, portal_id=22) # Tag2=Red

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return Remove(self.ctx)


initial_state = Wait
