""" trigger/52010027_qd/main_quest10003101.xml """
import trigger_api


"""
바람의 골짜기 : 52010027
중간 보스 빌런과 전투 벌이는 씬
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003101], quest_states=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52010027, portal_id=6005)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 집에서나옴(self.ctx)


class 집에서나옴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3006')
        self.spawn_monster(spawn_ids=[801])
        self.add_balloon_talk(msg='$52010027_QD__MAIN_QUEST10003101__0$', duration=3000, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 집에서나와서대사침(self.ctx)


class 집에서나와서대사침(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Suprise_A'])
        self.add_balloon_talk(msg='$52010027_QD__MAIN_QUEST10003101__1$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 집에나와서대사침01(self.ctx)


class 집에나와서대사침01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=10000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN_QUEST10003101__2$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 집에나와서대사침02(self.ctx)


class 집에나와서대사침02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4012], return_view=False)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN_QUEST10003101__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 집에나와서대사침03(self.ctx)


class 집에나와서대사침03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=10000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN_QUEST10003101__4$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 집에나와서대사침04(self.ctx)


class 집에나와서대사침04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4012], return_view=False)
        self.move_npc(spawn_id=801, patrol_name='MS2PatrolData_3005')
        self.set_effect(trigger_ids=[5005], visible=True)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN_QUEST10003101__5$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN_QUEST10003101__6$', duration=3000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN_QUEST10003101__7$', duration=3000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN_QUEST10003101__8$', duration=4000)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN_QUEST10003101__9$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return 집에나와서대사침05(self.ctx)


class 집에나와서대사침05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=801, sequence_name='Attack_01_G')
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN_QUEST10003101__10$', duration=3000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN_QUEST10003101__11$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 전투시작01(self.ctx)


class 전투시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52010027, portal_id=6006)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투시작01_1(self.ctx)


class 전투시작01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투시작02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52010027, portal_id=6006)
        self.spawn_monster(spawn_ids=[801])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투시작02(self.ctx)


class 전투시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5005])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[801])
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투시작03(self.ctx)


class 전투시작03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[802])
        self.set_event_ui(type=1, arg2='$52010027_QD__MAIN_QUEST10003101__12$', arg3='3000', arg4='0')
        self.add_balloon_talk(spawn_id=802, msg='$52010027_QD__MAIN_QUEST10003101__13$', duration=3000, delay_tick=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[802]):
            return 전투종료01(self.ctx)


class 전투종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52010027, portal_id=6007)
        self.destroy_monster(spawn_ids=[802])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전투종료02(self.ctx)


class 전투종료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN_QUEST10003101__14$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=803, sequence_name='Stun_A', duration=160000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투종료03(self.ctx)


class 전투종료03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: State


initial_state = idle
