""" trigger/02000311_bf/ai.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9999993, key='Buff_01', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_02') == 1:
            return Phase_02(self.ctx)


class Phase_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Phase_02_b(self.ctx)


class Phase_02_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=201, script='$02000311_BF__AI__0$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=202, script='$02000311_BF__AI__1$', time=2)
        self.set_skill(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Phase_02_c(self.ctx)


class Phase_02_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003111, text_id=20003111, duration=5000)
        self.set_effect(trigger_ids=[7001], visible=True)
        self.set_effect(trigger_ids=[7002], visible=True)
        self.set_user_value(trigger_id=9999994, key='Buff_01', value=1)
        self.set_user_value(trigger_id=9999995, key='Buff_02', value=1)


initial_state = idle
