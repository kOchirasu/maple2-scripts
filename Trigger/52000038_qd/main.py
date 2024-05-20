""" trigger/52000038_qd/main.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20020010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002632], quest_states=[3]):
            self.set_actor(trigger_id=3001, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3002, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3003, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3004, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3005, initial_sequence='Dead_A')
            return scene_c_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002632], quest_states=[2]):
            self.set_actor(trigger_id=3001, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3002, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3003, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3004, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3005, initial_sequence='Dead_A')
            self.spawn_monster(spawn_ids=[131,132])
            return scene_c_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002631], quest_states=[3]):
            self.set_actor(trigger_id=3001, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3002, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3003, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3004, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3005, initial_sequence='Dead_A')
            self.spawn_monster(spawn_ids=[131,132])
            return scene_c_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002631], quest_states=[2]):
            self.set_actor(trigger_id=3001, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3002, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3003, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3004, initial_sequence='Dead_A')
            self.set_actor(trigger_id=3005, initial_sequence='Dead_A')
            self.spawn_monster(spawn_ids=[131,132])
            return scene_c_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002631], quest_states=[1]):
            self.spawn_monster(spawn_ids=[121,122])
            return scene_b_02(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002630], quest_states=[3]):
            # 완료
            return scene_b_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002630], quest_states=[2]):
            # 완료가능
            return scene_b_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002630], quest_states=[1]):
            return ready_02(self.ctx)


class ready_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002630], quest_states=[1]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2001')
        self.set_dialogue(type=1, spawn_id=101, script='$52000038_QD__MAIN__0$', time=2)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2002')
        self.set_dialogue(type=1, spawn_id=102, script='$52000038_QD__MAIN__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2003')
        self.set_dialogue(type=1, spawn_id=101, script='$52000038_QD__MAIN__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2004')
        self.set_dialogue(type=1, spawn_id=102, script='$52000038_QD__MAIN__3$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return start_05_b(self.ctx)


class start_05_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3001, initial_sequence='Dead_A')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2005')
        self.set_dialogue(type=1, spawn_id=101, script='$52000038_QD__MAIN__4$', time=2)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2006')
        self.set_dialogue(type=1, spawn_id=102, script='$52000038_QD__MAIN__5$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[204])
        self.spawn_monster(spawn_ids=[205])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3002, initial_sequence='Dead_A')
        self.set_actor(trigger_id=3003, initial_sequence='Dead_A')
        self.set_actor(trigger_id=3004, initial_sequence='Dead_A')
        self.set_actor(trigger_id=3005, initial_sequence='Dead_A')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2007')
        self.set_dialogue(type=1, spawn_id=101, script='$52000038_QD__MAIN__6$', time=2, arg5=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2008')
        self.set_dialogue(type=1, spawn_id=102, script='$52000038_QD__MAIN__7$', time=2, arg5=4)
        self.show_guide_summary(entity_id=40010, text_id=40010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204,205]):
            self.destroy_monster(spawn_ids=[101,102])
            self.hide_guide_summary(entity_id=40010)
            return scene_b_01(self.ctx)


class scene_b_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='beyondroid1')
        self.spawn_monster(spawn_ids=[111,112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002631], quest_states=[1]):
            self.destroy_monster(spawn_ids=[111,112])
            self.spawn_monster(spawn_ids=[121,122])
            return scene_b_02(self.ctx)


class scene_b_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=121, patrol_name='MS2PatrolData_2009')
        self.set_dialogue(type=1, spawn_id=121, script='$52000038_QD__MAIN__8$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return scene_b_03(self.ctx)


class scene_b_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_2010')
        self.set_dialogue(type=1, spawn_id=122, script='$52000038_QD__MAIN__9$', time=2, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return scene_b_04(self.ctx)


class scene_b_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103])
        self.show_guide_summary(entity_id=20020010, text_id=20020010)
        self.set_dialogue(type=1, spawn_id=121, script='$52000038_QD__MAIN__10$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002631], quest_states=[2]):
            self.destroy_monster(spawn_ids=[121,122])
            self.spawn_monster(spawn_ids=[131,132])
            self.hide_guide_summary(entity_id=20020010)
            return scene_c_01(self.ctx)


class scene_c_01(trigger_api.Trigger):
    pass


initial_state = ready
