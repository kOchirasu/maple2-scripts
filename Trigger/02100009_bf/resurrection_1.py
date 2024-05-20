""" trigger/02100009_bf/resurrection_1.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[100000001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[100000001]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[100000001], skill_id=50000196, level=1, is_skill_set=False)
        self.add_buff(box_ids=[100000001], skill_id=50000200, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 체력조건달성(self.ctx)


class 체력조건달성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=100000001, is_relative=True) <= 5:
            return 몬스터기절_2(self.ctx)

    def on_exit(self) -> None:
        self.add_buff(box_ids=[100000001], skill_id=50000229, level=1, is_skill_set=False)
        self.add_buff(box_ids=[100000001], skill_id=50000207, level=1, is_skill_set=False)
        self.add_buff(box_ids=[100000001], skill_id=50000216, level=1, is_skill_set=False)


class 몬스터기절_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9900, type='trigger', achieve='02100009_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6800):
            return 몬스터부활(self.ctx)


class 몬스터부활(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[100000001], skill_id=50000204, level=1, is_skill_set=False)
        self.add_buff(box_ids=[100000001], skill_id=50000196, level=1, is_skill_set=False)
        self.add_buff(box_ids=[100000001], skill_id=50000200, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 체력조건미달(self.ctx)


class 체력조건미달(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=100000001, is_relative=True) > 5:
            return 몬스터부활_2(self.ctx)

    def on_exit(self) -> None:
        self.add_buff(box_ids=[100000001], skill_id=50000228, level=1, is_skill_set=False)


class 몬스터부활_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='MonsterDown', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 체력조건달성(self.ctx)


initial_state = 유저감지
