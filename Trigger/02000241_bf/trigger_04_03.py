""" trigger/02000241_bf/trigger_04_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[306], visible=True)
        self.set_mesh(trigger_ids=[707,708], visible=True)
        self.set_mesh(trigger_ids=[309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324])
        self.set_actor(trigger_id=507, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=508, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=509, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=510, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=511, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=512, visible=True, initial_sequence='Closed')
        self.destroy_monster(spawn_ids=[607,608,609,610,611,612])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[406]):
            return 버튼눌림(self.ctx)


class 버튼눌림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[306])
        self.set_actor(trigger_id=509, visible=True, initial_sequence='Opened')
        self.set_actor(trigger_id=510, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[609,610], auto_target=False)
        self.move_npc(spawn_id=609, patrol_name='MS2PatrolData_609')
        self.move_npc(spawn_id=610, patrol_name='MS2PatrolData_610')


initial_state = 대기
