""" trigger/02000378_bf/708_darknesstotem_08round.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713]) # TotemGround
        self.set_user_value(key='TotemApp', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TotemApp') == 1:
            return TotemApp01(self.ctx)


class TotemApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2008]) # 전투용 준타
        self.spawn_monster(spawn_ids=[2308], auto_target=False) # 날아라 준타
        self.set_mesh(trigger_ids=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713], visible=True, fade=5.0) # TotemGround
        self.spawn_monster(spawn_ids=[924], auto_target=False) # 암흑 토템

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return JuntaReady01(self.ctx)


class JuntaReady01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2308, script='$02000378_BF__708_DARKNESSTOTEM_08ROUND__0$', time=3) # 전투중인 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return JuntaGoUp01(self.ctx)


class JuntaGoUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2308, patrol_name='MS2PatrolData_2308')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return DestoryTotem01(self.ctx)


class DestoryTotem01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2108], auto_target=False) # 토템 옆에 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return JuntaReturn01(self.ctx)


class JuntaReturn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[924]) # 암흑 토템
        self.destroy_monster(spawn_ids=[2308]) # 날아라 준타
        self.destroy_monster(spawn_ids=[2108]) # 토템 옆에 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JuntaReturn02(self.ctx)


class JuntaReturn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2208], auto_target=False) # Regen_A 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713], fade=5.0) # TotemGround


initial_state = Wait
