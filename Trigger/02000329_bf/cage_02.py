""" trigger/02000329_bf/cage_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6802])
        self.set_actor(trigger_id=202, visible=True, initial_sequence='Closed')
        self.spawn_monster(spawn_ids=[1002,1102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1102]):
            return 닭생성(self.ctx)


class 닭생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=202, visible=True, initial_sequence='Opened')
        self.set_timer(timer_id='1', seconds=1)
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[6602])
        self.set_effect(trigger_ids=[6802], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            # self.set_dialogue(type=1, spawn_id=1002, script='후, 한결 낫네요', time=2)
            return 닭이동(self.ctx)


class 닭이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002')
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 닭소멸(self.ctx)


class 닭소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1002])


initial_state = 대기
