""" trigger/02000292_bf/battle02.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[501], visible=True, enable=True)
        self.set_ladder(trigger_ids=[502], visible=True, enable=True)
        self.set_ladder(trigger_ids=[503], visible=True, enable=True)
        self.destroy_monster(spawn_ids=[1006])
        self.destroy_monster(spawn_ids=[1007])
        self.destroy_monster(spawn_ids=[1008])
        self.destroy_monster(spawn_ids=[1009])
        self.destroy_monster(spawn_ids=[1010])
        self.destroy_monster(spawn_ids=[2006])
        self.destroy_monster(spawn_ids=[2007])
        self.destroy_monster(spawn_ids=[2008])
        self.destroy_monster(spawn_ids=[2009])
        self.destroy_monster(spawn_ids=[2010])
        self.set_effect(trigger_ids=[5001]) # Dark_Intro_Chord
        self.set_interact_object(trigger_ids=[10001061], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)
        self.spawn_monster(spawn_ids=[1009], auto_target=False)
        self.spawn_monster(spawn_ids=[1010], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[1006,1007,1008,1009,1010]):
            return MobBattle01(self.ctx)


class MobBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # Dark_Intro_Chord
        self.change_monster(from_spawn_id=1006, to_spawn_id=2006)
        self.change_monster(from_spawn_id=1007, to_spawn_id=2007)
        self.change_monster(from_spawn_id=1008, to_spawn_id=2008)
        self.change_monster(from_spawn_id=1009, to_spawn_id=2009)
        self.change_monster(from_spawn_id=1010, to_spawn_id=2010)
        self.set_ladder(trigger_ids=[501])
        self.set_ladder(trigger_ids=[502])
        self.set_ladder(trigger_ids=[503])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LadderOff01(self.ctx)


class LadderOff01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002921, text_id=20002921, duration=5000)
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
