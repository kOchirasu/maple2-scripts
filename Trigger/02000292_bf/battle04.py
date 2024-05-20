""" trigger/02000292_bf/battle04.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[521], visible=True, enable=True)
        self.set_ladder(trigger_ids=[522], visible=True, enable=True)
        self.set_ladder(trigger_ids=[523], visible=True, enable=True)
        self.set_ladder(trigger_ids=[524], visible=True, enable=True)
        self.set_ladder(trigger_ids=[525], visible=True, enable=True)
        self.destroy_monster(spawn_ids=[1015])
        self.destroy_monster(spawn_ids=[1016])
        self.destroy_monster(spawn_ids=[1017])
        self.destroy_monster(spawn_ids=[1018])
        self.destroy_monster(spawn_ids=[1019])
        self.destroy_monster(spawn_ids=[2015])
        self.destroy_monster(spawn_ids=[2016])
        self.destroy_monster(spawn_ids=[2017])
        self.destroy_monster(spawn_ids=[2018])
        self.destroy_monster(spawn_ids=[2019])
        self.set_effect(trigger_ids=[5003]) # Dark_Intro_Chord
        self.set_interact_object(trigger_ids=[10001063], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1015], auto_target=False)
        self.spawn_monster(spawn_ids=[1016], auto_target=False)
        self.spawn_monster(spawn_ids=[1017], auto_target=False)
        self.spawn_monster(spawn_ids=[1018], auto_target=False)
        self.spawn_monster(spawn_ids=[1019], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[1015,1016,1017,1018,1019]):
            return MobBattle01(self.ctx)


class MobBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True) # Dark_Intro_Chord
        self.change_monster(from_spawn_id=1015, to_spawn_id=2015)
        self.change_monster(from_spawn_id=1016, to_spawn_id=2016)
        self.change_monster(from_spawn_id=1017, to_spawn_id=2017)
        self.change_monster(from_spawn_id=1018, to_spawn_id=2018)
        self.change_monster(from_spawn_id=1019, to_spawn_id=2019)
        self.set_ladder(trigger_ids=[521])
        self.set_ladder(trigger_ids=[522])
        self.set_ladder(trigger_ids=[523])
        self.set_ladder(trigger_ids=[524])
        self.set_ladder(trigger_ids=[525])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LadderOff01(self.ctx)


class LadderOff01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002921, text_id=20002921, duration=5000)
        self.set_interact_object(trigger_ids=[10001063], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001063], state=0):
            return LadderOn01(self.ctx)


class LadderOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[521], visible=True, enable=True)
        self.set_ladder(trigger_ids=[522], visible=True, enable=True)
        self.set_ladder(trigger_ids=[523], visible=True, enable=True)
        self.set_ladder(trigger_ids=[524], visible=True, enable=True)
        self.set_ladder(trigger_ids=[525], visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
