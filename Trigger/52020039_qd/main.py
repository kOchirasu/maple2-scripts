""" trigger/52020039_qd/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000590], quest_states=[3]):
            return NPC소환(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000600], quest_states=[1]):
            return NPC소환(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000600], quest_states=[2]):
            return NPC소환(self.ctx)


class NPC소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.spawn_monster(spawn_ids=[113], auto_target=False)
        self.spawn_monster(spawn_ids=[114], auto_target=False)
        self.spawn_monster(spawn_ids=[115], auto_target=False)
        self.spawn_monster(spawn_ids=[116], auto_target=False)
        self.spawn_monster(spawn_ids=[117], auto_target=False)
        self.spawn_monster(spawn_ids=[118], auto_target=False)
        self.spawn_monster(spawn_ids=[119], auto_target=False)
        self.spawn_monster(spawn_ids=[120], auto_target=False)


initial_state = Ready
