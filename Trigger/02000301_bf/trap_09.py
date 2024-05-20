""" trigger/02000301_bf/trap_09.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=218, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=219, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_interact_object(trigger_ids=[10000516], state=1)
        self.set_effect(trigger_ids=[609])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[610])
        self.set_mesh(trigger_ids=[3091,3092,3093,3094,3095,3096])
        self.set_mesh(trigger_ids=[4901,4902,4903,4904,4905,4906,4907,4908,4909,4910,4911,4912,4913,4914,4915,4916,4917,4918,4919,4920,4921,4922,4923,4924,4925,4926,4927,4928,4929], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[109]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10901]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10902]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10903]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10904]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10905]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10906]):
            return 경보(self.ctx)
        if self.user_detected(box_ids=[10907]):
            return 경보(self.ctx)
        if self.object_interacted(interact_ids=[10000516], state=0):
            return 해제(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=218, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=219, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_interact_object(trigger_ids=[10000516], state=0)
        self.spawn_monster(spawn_ids=[2010], auto_target=False)
        self.set_effect(trigger_ids=[609], visible=True)
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.show_guide_summary(entity_id=20003001, text_id=20003001)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_mesh(trigger_ids=[3091,3092,3093,3094,3095,3096], visible=True)
        self.set_mesh(trigger_ids=[4901,4902,4903,4904,4905,4906,4907,4908,4909,4910,4911,4912,4913,4914,4915,4916,4917,4918,4919,4920,4921,4922,4923,4924,4925,4926,4927,4928,4929])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2010]):
            self.set_effect(trigger_ids=[610])
            self.hide_guide_summary(entity_id=20003001)
            self.set_actor(trigger_id=218, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=219, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2010])
        self.set_mesh(trigger_ids=[3091,3092,3093,3094,3095,3096], fade=5.0)
        self.set_mesh(trigger_ids=[4901,4902,4903,4904,4905,4906,4907,4908,4909,4910,4911,4912,4913,4914,4915,4916,4917,4918,4919,4920,4921,4922,4923,4924,4925,4926,4927,4928,4929], fade=5.0)


initial_state = 시작
