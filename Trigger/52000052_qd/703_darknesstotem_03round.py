""" trigger/52000052_qd/703_darknesstotem_03round.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413]) # TotemGround
        self.set_user_value(key='TotemApp', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TotemApp') == 1:
            return TotemApp01(self.ctx)


class TotemApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2003]) # 전투용 준타
        self.spawn_monster(spawn_ids=[2303], auto_target=False) # 날아라 준타
        self.set_mesh(trigger_ids=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413], visible=True, fade=5.0) # TotemGround
        self.spawn_monster(spawn_ids=[921], auto_target=False) # 암흑 토템

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return JuntaReady01(self.ctx)


class JuntaReady01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2303, script='$52000052_QD__702_DARKNESSTOTEM_02ROUND__0$', time=3) # 전투중인 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return JuntaGoUp01(self.ctx)


class JuntaGoUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2303, patrol_name='MS2PatrolData_2303')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return DestoryTotem01(self.ctx)


class DestoryTotem01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2103], auto_target=False) # 토템 옆에 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return JuntaReturn01(self.ctx)


class JuntaReturn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[921]) # 암흑 토템
        self.destroy_monster(spawn_ids=[2303]) # 날아라 준타
        self.destroy_monster(spawn_ids=[2103]) # 토템 옆에 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return JuntaReturn02(self.ctx)


class JuntaReturn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2203], auto_target=False) # Regen_A 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3400,3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413], fade=5.0) # TotemGround


initial_state = Wait
