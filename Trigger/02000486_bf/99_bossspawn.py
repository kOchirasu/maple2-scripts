""" trigger/02000486_bf/99_bossspawn.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 던전시작(self.ctx)


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 던전시작(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[900,901], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BossBattle01(self.ctx)


class BossBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='CheckDualKill', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900,901]):
            return BossBattle02(self.ctx)


class BossBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[900,901])
        self.set_achievement(trigger_id=9900, type='trigger', achieve='Madracan02')
        self.set_achievement(trigger_id=9900, type='trigger', achieve='Madracan_Q02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class QuestClear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9900, type='trigger', achieve='Madracan_Q02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = Wait
