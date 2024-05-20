""" trigger/02000420_bf/barricade.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[99]):
            return None # Missing State: 카운트


initial_state = 대기
