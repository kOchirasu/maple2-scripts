""" trigger/02000292_bf/battle03.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[511], visible=True, enable=True)
        self.set_ladder(trigger_ids=[512], visible=True, enable=True)
        self.set_ladder(trigger_ids=[513], visible=True, enable=True)
        self.set_ladder(trigger_ids=[514], visible=True, enable=True)
        self.set_ladder(trigger_ids=[515], visible=True, enable=True)
        self.destroy_monster(spawn_ids=[1011])
        self.destroy_monster(spawn_ids=[1012])
        self.destroy_monster(spawn_ids=[1013])
        self.destroy_monster(spawn_ids=[1014])
        self.destroy_monster(spawn_ids=[2011])
        self.destroy_monster(spawn_ids=[2012])
        self.destroy_monster(spawn_ids=[2013])
        self.destroy_monster(spawn_ids=[2014])
        self.set_effect(trigger_ids=[5002]) # Dark_Intro_Chord
        self.set_interact_object(trigger_ids=[10001062], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1011], auto_target=False)
        self.spawn_monster(spawn_ids=[1012], auto_target=False)
        self.spawn_monster(spawn_ids=[1013], auto_target=False)
        self.spawn_monster(spawn_ids=[1014], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[1011,1012,1013,1014]):
            return MobBattle01(self.ctx)


class MobBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # Dark_Intro_Chord
        self.change_monster(from_spawn_id=1011, to_spawn_id=2011)
        self.change_monster(from_spawn_id=1012, to_spawn_id=2012)
        self.change_monster(from_spawn_id=1013, to_spawn_id=2013)
        self.change_monster(from_spawn_id=1014, to_spawn_id=2014)
        self.set_ladder(trigger_ids=[511])
        self.set_ladder(trigger_ids=[512])
        self.set_ladder(trigger_ids=[513])
        self.set_ladder(trigger_ids=[514])
        self.set_ladder(trigger_ids=[515])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LadderOff01(self.ctx)


class LadderOff01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002921, text_id=20002921, duration=5000)
        self.set_interact_object(trigger_ids=[10001062], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001062], state=0):
            return LadderOn01(self.ctx)


class LadderOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[511], visible=True, enable=True)
        self.set_ladder(trigger_ids=[512], visible=True, enable=True)
        self.set_ladder(trigger_ids=[513], visible=True, enable=True)
        self.set_ladder(trigger_ids=[514], visible=True, enable=True)
        self.set_ladder(trigger_ids=[515], visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
