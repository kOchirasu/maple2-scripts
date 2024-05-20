""" trigger/02000329_bf/cage_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6801])
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Closed')
        self.spawn_monster(spawn_ids=[1001,1101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1101]):
            return 닭생성(self.ctx)


class 닭생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Opened')
        self.set_timer(timer_id='1', seconds=1)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[6601])
        self.set_effect(trigger_ids=[6801], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            # self.set_dialogue(type=1, spawn_id=1001, script='꼬꼬', time=2)
            return 닭이동(self.ctx)


class 닭이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001')
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 닭소멸(self.ctx)


class 닭소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001])


initial_state = 대기
