""" trigger/99999841/debuffmob.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=811, value=0)
        self.set_dungeon_variable(var_id=812, value=0)
        self.set_dungeon_variable(var_id=813, value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.user_value(key='Start') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.time_expired(timer_id='2'):
            return 랜덤확률(self.ctx)


class 랜덤확률(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='디버프 몬스터가 생성되었습니다.\\n몬스터를 처치하면 상대팀에 디버프를 겁니다.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.random_condition(weight=33.0):
            return A지역(self.ctx)
        if self.random_condition(weight=34.0):
            return B지역(self.ctx)
        if self.random_condition(weight=33.0):
            return C지역(self.ctx)


class A지역(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[801], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[801]):
            self.set_event_ui_script(type=BannerType.Text, script='상대팀에 이동속도 감소 디버프를 겁니다.', duration=5000)
            self.set_dungeon_variable(var_id=811, value=1)
            return 딜레이(self.ctx)


class B지역(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[802], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[802]):
            self.set_event_ui_script(type=BannerType.Text, script='상대팀에 공격력 감소 디버프를 겁니다.', duration=5000)
            self.set_dungeon_variable(var_id=812, value=1)
            return 딜레이(self.ctx)


class C지역(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[803], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[803]):
            self.set_event_ui_script(type=BannerType.Text, script='상대팀에 체력 감소 디버프를 겁니다.', duration=5000)
            self.set_dungeon_variable(var_id=813, value=1)
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.time_expired(timer_id='1'):
            self.set_dungeon_variable(var_id=811, value=0)
            self.set_dungeon_variable(var_id=812, value=0)
            self.set_dungeon_variable(var_id=813, value=0)
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
