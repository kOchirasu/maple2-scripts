""" trigger/02000486_bf/100_dualkill.xml """
import trigger_api


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return Wait(self.ctx)


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckDualKill', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckDualKill') == 1:
            return CheckDualKill(self.ctx)


class CheckDualKill(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900]):
            return LionBlueDead(self.ctx)
        if self.monster_dead(spawn_ids=[901]):
            return LionRedDead(self.ctx)


class LionBlueDead(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901]):
            self.set_achievement(trigger_id=9900, type='trigger', achieve='ChangeLionDualKill')
            return Quit(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class LionRedDead(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900]):
            self.set_achievement(trigger_id=9900, type='trigger', achieve='ChangeLionDualKill')
            return Quit(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = 룸체크
