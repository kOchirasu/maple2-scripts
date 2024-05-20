""" trigger/02000301_bf/trap_05.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=210, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=211, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_interact_object(trigger_ids=[10000513], state=1)
        self.set_effect(trigger_ids=[606])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[610])
        self.set_mesh(trigger_ids=[3051,3052,3053,3054,3055,3056])
        self.set_mesh(trigger_ids=[4501,4502,4503,4504,4505,4506,4507,4508,4509,4510,4511,4512,4513,4514,4515,4516,4517,4518,4519], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10501]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10502]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10503]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10504]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10505]):
            return 경보(self.ctx)
        if self.object_interacted(interact_ids=[10000513], state=0):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=210, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=211, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_interact_object(trigger_ids=[10000513], state=0)
        self.spawn_monster(spawn_ids=[2006], auto_target=False)
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.show_guide_summary(entity_id=20003001, text_id=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(trigger_ids=[3051,3052,3053,3054,3055,3056], visible=True)
        self.set_mesh(trigger_ids=[4501,4502,4503,4504,4505,4506,4507,4508,4509,4510,4511,4512,4513,4514,4515,4516,4517,4518,4519])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2006]):
            self.hide_guide_summary(entity_id=20003001)
            self.set_effect(trigger_ids=[610])
            self.set_actor(trigger_id=210, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=211, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2006])
        self.set_mesh(trigger_ids=[3051,3052,3053,3054,3055,3056], fade=5.0)
        self.set_mesh(trigger_ids=[4501,4502,4503,4504,4505,4506,4507,4508,4509,4510,4511,4512,4513,4514,4515,4516,4517,4518,4519], fade=5.0)


initial_state = 시작
