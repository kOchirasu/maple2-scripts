""" trigger/99999926/main.xml """
import trigger_api


class DungeonStart(trigger_api.Trigger):
    pass


class Battle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[421,422,423,424,425], auto_target=False)
        # self.set_skill(trigger_ids=[501], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[421,422,423,424,425]):
            return Battle02(self.ctx)


class Battle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[411,412,413,414,415], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[411,412,413,414,415]):
            return Battle03Random(self.ctx)


class Battle03Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return Battle03A(self.ctx)
        if self.random_condition(weight=25.0):
            return Battle03B(self.ctx)


class Battle03A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[421,422,423,424,425], auto_target=False)
        self.spawn_monster(spawn_ids=[441], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[421,422,423,424,425]):
            return MevidicCinematic(self.ctx)


class Battle03B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[411,412,413,414,415], auto_target=False)
        self.spawn_monster(spawn_ids=[441], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[411,412,413,414,415]):
            return MevidicCinematic(self.ctx)


class MevidicCinematic(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[451], auto_target=False)
        self.move_npc(spawn_id=451, patrol_name='MS2PatrolData_701')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=402) >= 1:
            return None # Missing State: LoadingStart


initial_state = DungeonStart
