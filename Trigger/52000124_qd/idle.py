""" trigger/52000124_qd/idle.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101]) # 이브 (11000069)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100140,60100141,60100142,60100143,60100144,60100145,60100146,60100147,60100148,60100149,60100150,60100151,60100152,60100153,60100154,60100155], quest_states=[1]):
            return StateDelete(self.ctx)


# delnpc
class StateDelete(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201,202])


initial_state = idle
