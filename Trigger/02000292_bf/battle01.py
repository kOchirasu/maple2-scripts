""" trigger/02000292_bf/battle01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1003])
        self.destroy_monster(spawn_ids=[1004])
        self.destroy_monster(spawn_ids=[1005])
        self.destroy_monster(spawn_ids=[2001])
        self.destroy_monster(spawn_ids=[2002])
        self.destroy_monster(spawn_ids=[2003])
        self.destroy_monster(spawn_ids=[2004])
        self.destroy_monster(spawn_ids=[2005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[1001,1002,1003,1004,1005]):
            return MobBattle01(self.ctx)


class MobBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # Dark_Intro_Chord
        self.change_monster(from_spawn_id=1001, to_spawn_id=2001)
        self.change_monster(from_spawn_id=1002, to_spawn_id=2002)
        self.change_monster(from_spawn_id=1003, to_spawn_id=2003)
        self.change_monster(from_spawn_id=1004, to_spawn_id=2004)
        self.change_monster(from_spawn_id=1005, to_spawn_id=2005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LadderOff01(self.ctx)


class LadderOff01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002925, text_id=20002925, duration=3000)
        self.set_interact_object(trigger_ids=[10001061], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001061], state=0):
            return LadderOn01(self.ctx)


class LadderOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[501], visible=True, enable=True)
        self.set_ladder(trigger_ids=[502], visible=True, enable=True)
        self.set_ladder(trigger_ids=[503], visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
