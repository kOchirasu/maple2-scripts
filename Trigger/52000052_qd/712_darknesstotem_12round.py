""" trigger/52000052_qd/712_darknesstotem_12round.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813]) # TotemGround
        self.set_user_value(key='TotemApp', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TotemApp') == 1:
            return TotemApp01(self.ctx)


class TotemApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2012]) # 전투용 준타
        self.spawn_monster(spawn_ids=[2312], auto_target=False) # 날아라 준타
        self.set_mesh(trigger_ids=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813], visible=True, fade=5.0) # TotemGround
        self.spawn_monster(spawn_ids=[925], auto_target=False) # 암흑 토템

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return JuntaReady01(self.ctx)


class JuntaReady01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2312, script='$52000052_QD__702_DARKNESSTOTEM_02ROUND__0$', time=3) # 전투중인 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return JuntaGoUp01(self.ctx)


class JuntaGoUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2312, patrol_name='MS2PatrolData_2312')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return DestoryTotem01(self.ctx)


class DestoryTotem01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2112], auto_target=False) # 토템 옆에 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return JuntaReturn01(self.ctx)


class JuntaReturn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[925]) # 암흑 토템
        self.destroy_monster(spawn_ids=[2312]) # 날아라 준타
        self.destroy_monster(spawn_ids=[2112]) # 토템 옆에 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JuntaReturn02(self.ctx)


class JuntaReturn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2212], auto_target=False) # Regen_A 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813], fade=5.0) # TotemGround


initial_state = Wait
