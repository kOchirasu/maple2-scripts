""" trigger/02000241_bf/trigger_01_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301], visible=True)
        self.set_mesh(trigger_ids=[701,702], visible=True)
        self.set_actor(trigger_id=501, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=502, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=503, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=504, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=505, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=506, visible=True, initial_sequence='Closed')
        self.destroy_monster(spawn_ids=[601,602,603,604,605,606])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[401]):
            return 버튼눌림(self.ctx)


class 버튼눌림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301])
        self.set_actor(trigger_id=501, visible=True, initial_sequence='Opened')
        self.set_actor(trigger_id=502, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[601,602], auto_target=False)
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData_601')
        self.move_npc(spawn_id=602, patrol_name='MS2PatrolData_602')


initial_state = 대기
