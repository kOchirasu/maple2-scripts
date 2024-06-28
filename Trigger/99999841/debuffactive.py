""" trigger/99999841/debuffactive.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=801) == 1:
            return 이동속도감소(self.ctx)
        if self.dungeon_variable(var_id=802) == 1:
            return 공격력감소(self.ctx)
        if self.dungeon_variable(var_id=803) == 1:
            return 체력감소(self.ctx)


class 이동속도감소(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=801, value=0)
        self.set_event_ui_script(type=BannerType.Text, script='이동속도 감소 디버프에 걸립니다.', duration=5000)
        self.add_buff(box_ids=[9001], skill_id=70002581, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        return None # Missing State: 종료


class 공격력감소(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=802, value=0)
        self.set_event_ui_script(type=BannerType.Text, script='공격력 감소 디버프에 걸립니다.', duration=5000)
        self.add_buff(box_ids=[9001], skill_id=70002591, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        return None # Missing State: 종료


class 체력감소(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=803, value=0)
        self.set_event_ui_script(type=BannerType.Text, script='체력 감소 디버프에 걸립니다.', duration=5000)
        self.add_buff(box_ids=[9001], skill_id=70002601, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        return None # Missing State: 종료


initial_state = 대기
