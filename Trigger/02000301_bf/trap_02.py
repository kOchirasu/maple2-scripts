""" trigger/02000301_bf/trap_02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=204, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[610])
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1101], auto_target=False)
        self.set_mesh(trigger_ids=[3021,3022,3023,3024,3025,3026], visible=True)
        self.set_mesh(trigger_ids=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212], visible=True)
        self.set_mesh(trigger_ids=[3027,3028], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10201]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10202]):
            return 경보(self.ctx)
        if self.monster_dead(spawn_ids=[1101]):
            return 경보(self.ctx)
        if self.monster_dead(spawn_ids=[1001]):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=204, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[605], visible=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002')
        self.spawn_monster(spawn_ids=[2003], auto_target=False)
        self.show_guide_summary(entity_id=20003002, text_id=20003002)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_dialogue(type=1, spawn_id=1001, script='$02000301_BF__TRAP_02__1$', time=2)
        self.set_mesh(trigger_ids=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212], fade=5.0)
        self.set_mesh(trigger_ids=[3027,3028], fade=5.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2003]):
            self.hide_guide_summary(entity_id=20003002)
            self.set_effect(trigger_ids=[610])
            self.set_actor(trigger_id=204, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=205, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2003]):
            self.set_mesh(trigger_ids=[3021,3022,3023,3024,3025,3026], fade=5.0)
            self.set_mesh(trigger_ids=[4201,4202,4203,4204,4205,4206,4207,4208,4209,4210,4211,4212], fade=5.0)
            return 해제(self.ctx)


initial_state = 시작
