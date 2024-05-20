""" trigger/52010001_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000871], state=1)
        self.set_interact_object(trigger_ids=[10000910], state=1)
        self.set_actor(trigger_id=1001, visible=True, initial_sequence='Down_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000871,10000910], state=0):
            return Event_02(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=701, type='trigger', achieve='Firepotoff') # Firepotoff


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=1001, initial_sequence='Down_Idle_A')
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 노인 생성
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1001')
        self.set_dialogue(type=1, spawn_id=101, script='$52010001_QD__MAIN__0$', time=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[101]):
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52010001_QD__MAIN__1$', time=3)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1002')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52010001_QD__MAIN__2$', time=3)
        self.set_interact_object(trigger_ids=[10000871], state=1)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=703, spawn_ids=[101]):
            return Event_04_02(self.ctx)


class Event_04_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1004')
        self.set_dialogue(type=1, spawn_id=101, script='$52010001_QD__MAIN__3$', time=3)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_06(self.ctx)


class Event_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52010001_QD__MAIN__4$', time=3, arg5=3)
        self.set_interact_object(trigger_ids=[10000910], state=1)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1005')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=704, spawn_ids=[101]):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=1001, visible=True, initial_sequence='Down_Idle_A')
        self.destroy_monster(spawn_ids=[101])


initial_state = idle
