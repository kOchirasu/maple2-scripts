""" trigger/02000292_bf/battle05.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[117,118,119,120], fade=2.0)
        self.destroy_monster(spawn_ids=[1020])
        self.destroy_monster(spawn_ids=[1021])
        self.destroy_monster(spawn_ids=[1022])
        self.destroy_monster(spawn_ids=[1023])
        self.destroy_monster(spawn_ids=[1024])
        self.destroy_monster(spawn_ids=[2020])
        self.destroy_monster(spawn_ids=[2021])
        self.destroy_monster(spawn_ids=[2022])
        self.destroy_monster(spawn_ids=[2023])
        self.destroy_monster(spawn_ids=[2024])
        self.set_effect(trigger_ids=[5004]) # Dark_Intro_Chord

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1020], auto_target=False)
        self.spawn_monster(spawn_ids=[1021], auto_target=False)
        self.spawn_monster(spawn_ids=[1022], auto_target=False)
        self.spawn_monster(spawn_ids=[1023], auto_target=False)
        self.spawn_monster(spawn_ids=[1024], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[1020,1021,1022,1023,1024]):
            return MobBattle01(self.ctx)


class MobBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004], visible=True) # Dark_Intro_Chord
        self.change_monster(from_spawn_id=1020, to_spawn_id=2015)
        self.change_monster(from_spawn_id=1021, to_spawn_id=2016)
        self.change_monster(from_spawn_id=1022, to_spawn_id=2017)
        self.change_monster(from_spawn_id=1023, to_spawn_id=2018)
        self.change_monster(from_spawn_id=1024, to_spawn_id=2019)
        self.spawn_monster(spawn_ids=[1025], auto_target=False)
        self.set_mesh(trigger_ids=[117,118,119,120], visible=True, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BlockOn01(self.ctx)


class BlockOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002923, text_id=20002923)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1025]):
            return BlockOff01(self.ctx)


class BlockOff01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002923)
        self.set_mesh(trigger_ids=[117,118,119,120], fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
