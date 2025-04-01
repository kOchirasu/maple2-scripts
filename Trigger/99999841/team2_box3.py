""" trigger/99999841/team2_box3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=913, value=0)
        self.set_interact_object(trigger_ids=[10002181], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.user_value(key='Start') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002179], state=1)
        self.set_interact_object(trigger_ids=[10002180], state=1)
        self.set_interact_object(trigger_ids=[10002181], state=1)
        self.set_interact_object(trigger_ids=[10002182], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002181], state=0):
            return 애디셔널_중첩1(self.ctx)


class 애디셔널_중첩1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=913, value=1)
        self.add_buff(box_ids=[9001], skill_id=70002531, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 애디셔널_중첩2(self.ctx)


class 애디셔널_중첩2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9001], skill_id=70002531, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 애디셔널_중첩3(self.ctx)


class 애디셔널_중첩3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9001], skill_id=70002531, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 애디셔널_중첩4(self.ctx)


class 애디셔널_중첩4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9001], skill_id=70002531, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 애디셔널_중첩5(self.ctx)


class 애디셔널_중첩5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9001], skill_id=70002531, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 애디셔널_중첩6(self.ctx)


class 애디셔널_중첩6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9001], skill_id=70002531, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 애디셔널_중첩7(self.ctx)


class 애디셔널_중첩7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9001], skill_id=70002531, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 애디셔널_중첩8(self.ctx)


class 애디셔널_중첩8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9001], skill_id=70002531, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 애디셔널_중첩9(self.ctx)


class 애디셔널_중첩9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9001], skill_id=70002531, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=901) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002181], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BadMob') == 1:
            return 대기(self.ctx)


initial_state = 대기
