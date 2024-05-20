""" trigger/02000301_bf/trap_06.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=212, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=213, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_interact_object(trigger_ids=[10000514], state=1)
        self.set_effect(trigger_ids=[607])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[610])
        self.set_mesh(trigger_ids=[3061,3062,3063,3064,3065,3066])
        self.set_mesh(trigger_ids=[4601,4602,4603,4604,4605,4606,4607,4608,4609,4610,4611,4612,4613,4614], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10601]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10602]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10603]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10604]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10605]):
            return 경보(self.ctx)
        if self.object_interacted(interact_ids=[10000514], state=0):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=212, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=213, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_interact_object(trigger_ids=[10000514], state=0)
        self.spawn_monster(spawn_ids=[2007], auto_target=False)
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.show_guide_summary(entity_id=20003001, text_id=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(trigger_ids=[3061,3062,3063,3064,3065,3066], visible=True)
        self.set_mesh(trigger_ids=[4601,4602,4603,4604,4605,4606,4607,4608,4609,4610,4611,4612,4613,4614])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2007]):
            self.hide_guide_summary(entity_id=20003001)
            self.set_effect(trigger_ids=[610])
            self.set_actor(trigger_id=212, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=213, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2007])
        self.set_mesh(trigger_ids=[3061,3062,3063,3064,3065,3066], fade=5.0)
        self.set_mesh(trigger_ids=[4601,4602,4603,4604,4605,4606,4607,4608,4609,4610,4611,4612,4613,4614], fade=5.0)


initial_state = 시작
