""" trigger/02000301_bf/trap_07.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=214, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=215, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[610])
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1103], auto_target=False)
        self.set_mesh(trigger_ids=[3071,3072,3073,3074,3075,3076], visible=True)
        self.set_mesh(trigger_ids=[4701,4702,4703,4704,4705,4706,4707,4708,4709,4710,4711,4712,4713], visible=True)
        self.set_mesh(trigger_ids=[3077,3078], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[107]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10701]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10702]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10703]):
            return 경보(self.ctx)
        if self.monster_dead(spawn_ids=[1103]):
            return 경보(self.ctx)
        if self.monster_dead(spawn_ids=[1005]):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=214, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=215, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.move_npc(spawn_id=1006, patrol_name='MS2PatrolData_1006')
        self.spawn_monster(spawn_ids=[2008], auto_target=False)
        self.show_guide_summary(entity_id=20003002, text_id=20003002)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_dialogue(type=1, spawn_id=1005, script='$02000301_BF__TRAP_07__1$', time=2)
        self.set_mesh(trigger_ids=[4701,4702,4703,4704,4705,4706,4707,4708,4709,4710,4711,4712,4713], fade=5.0)
        self.set_mesh(trigger_ids=[3077,3078], fade=5.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2008]):
            self.hide_guide_summary(entity_id=20003002)
            self.set_effect(trigger_ids=[610])
            self.set_actor(trigger_id=214, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=215, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2008]):
            self.set_mesh(trigger_ids=[3071,3072,3073,3074,3075,3076], fade=5.0)
            self.set_mesh(trigger_ids=[4701,4702,4703,4704,4705,4706,4707,4708,4709,4710,4711,4712,4713], fade=5.0)
            return 해제(self.ctx)


initial_state = 시작
