""" trigger/02000301_bf/trap_08.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=216, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=217, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_interact_object(trigger_ids=[10000515], state=1)
        self.set_effect(trigger_ids=[608])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[610])
        self.set_mesh(trigger_ids=[3081,3082,3083,3084,3085,3086])
        self.set_mesh(trigger_ids=[4801,4802,4803,4804,4805,4806,4807,4808,4809,4810,4811,4812,4813,4814,4815,4816,4817,4818], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[108]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10801]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10802]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10803]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10804]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10805]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10806]):
            return 경보(self.ctx)
        if self.object_interacted(interact_ids=[10000515], state=0):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=216, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=217, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_interact_object(trigger_ids=[10000515], state=0)
        self.spawn_monster(spawn_ids=[2009], auto_target=False)
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.show_guide_summary(entity_id=20003001, text_id=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(trigger_ids=[3081,3082,3083,3084,3085,3086], visible=True)
        self.set_mesh(trigger_ids=[4801,4802,4803,4804,4805,4806,4807,4808,4809,4810,4811,4812,4813,4814,4815,4816,4817,4818])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2009]):
            self.hide_guide_summary(entity_id=20003001)
            self.set_effect(trigger_ids=[610])
            self.set_actor(trigger_id=216, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=217, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2009])
        self.set_mesh(trigger_ids=[3081,3082,3083,3084,3085,3086], fade=5.0)
        self.set_mesh(trigger_ids=[4801,4802,4803,4804,4805,4806,4807,4808,4809,4810,4811,4812,4813,4814,4815,4816,4817,4818], fade=5.0)


initial_state = 시작
