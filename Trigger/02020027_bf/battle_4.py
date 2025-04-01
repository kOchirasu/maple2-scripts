""" trigger/02020027_bf/battle_4.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 전투시작_2(self.ctx)


class 전투시작_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='summon_2_2') == 1:
            return 몬스터소환(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401,402,403,404,405,406])
        self.set_dialogue(type=1, spawn_id=401, script='$02020027_BF__battle_1__1$', time=3)
        self.set_dialogue(type=1, spawn_id=403, script='$02020027_BF__battle_1__2$', time=3)
        self.set_dialogue(type=1, spawn_id=405, script='$02020027_BF__battle_1__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[401,402,403,404,405,406]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[201], skill_id=62000002, level=1)
        self.add_buff(box_ids=[201], skill_id=51200002, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        pass


initial_state = 전투시작
