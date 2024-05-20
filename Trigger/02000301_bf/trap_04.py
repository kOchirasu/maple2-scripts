""" trigger/02000301_bf/trap_04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=208, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=209, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[610])
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1102], auto_target=False)
        self.set_mesh(trigger_ids=[3041,3042,3043,3044,3045,3046], visible=True)
        self.set_mesh(trigger_ids=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414], visible=True)
        self.set_mesh(trigger_ids=[3047,3048], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10401]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10402]):
            return 경보(self.ctx)
        if self.monster_dead(spawn_ids=[1102]):
            return 경보(self.ctx)
        if self.monster_dead(spawn_ids=[1003]):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=208, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=209, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004')
        self.spawn_monster(spawn_ids=[2005], auto_target=False)
        self.show_guide_summary(entity_id=20003002, text_id=20003002)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_dialogue(type=1, spawn_id=1003, script='$02000301_BF__TRAP_04__1$', time=2)
        self.set_mesh(trigger_ids=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414], fade=5.0)
        self.set_mesh(trigger_ids=[3047,3048], fade=5.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2005]):
            self.hide_guide_summary(entity_id=20003002)
            self.set_effect(trigger_ids=[610])
            self.set_actor(trigger_id=208, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=209, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2005]):
            self.set_mesh(trigger_ids=[3041,3042,3043,3044,3045,3046], fade=5.0)
            self.set_mesh(trigger_ids=[4401,4402,4403,4404,4405,4406,4407,4408,4409,4410,4411,4412,4413,4414], fade=5.0)
            return 해제(self.ctx)


initial_state = 시작
