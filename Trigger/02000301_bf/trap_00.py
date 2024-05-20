""" trigger/02000301_bf/trap_00.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=200, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_interact_object(trigger_ids=[10000510], state=1)
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[610])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006])
        self.set_mesh(trigger_ids=[4001,4002,4003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 경보(self.ctx)
        if self.object_interacted(interact_ids=[10000510], state=0):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=200, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_interact_object(trigger_ids=[10000510], state=0)
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[605], visible=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.show_guide_summary(entity_id=20003001, text_id=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006], visible=True)
        self.set_mesh(trigger_ids=[4001,4002,4003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            self.hide_guide_summary(entity_id=20003001)
            self.set_effect(trigger_ids=[610])
            self.set_actor(trigger_id=200, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2001])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006], fade=5.0)
        self.set_mesh(trigger_ids=[4001,4002,4003], fade=5.0)


initial_state = 시작
