""" trigger/52000073_qd/main.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import Align


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[60100115], quest_states=[1]):
            return 레논등장(self.ctx)


class 레논등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        """
        연출 3 : 레터박스 
            연출 1 : 플레이어 조작 뺏기
        """
        self.set_onetime_effect(id=1, enable=True, path='BG\\weather\\Eff_monochrome_03.xml')
        self.set_sound(trigger_id=7001, enable=True)
        self.destroy_monster(spawn_ids=[101])
        self.visible_my_pc(is_visible=False)
        self.set_ambient_light(primary=Vector3(0,0,0))
        self.set_ambient_light(primary=Vector3(1,1,1))
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[302]) # 윈 스틸던의 시체
        self.spawn_monster(spawn_ids=[301]) # 레논
        self.select_camera_path(path_ids=[8001,8002], return_view=False)
        self.set_scene_skip(state=다크윈드통로, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 계단이동(self.ctx)


class 계단이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003,8004], return_view=False)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_2001')
        self.set_dialogue(type=1, spawn_id=301, script='$52000073_QD__MAIN__0$', time=3) # 레논 계단 올라가며 하는 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 시체발견(self.ctx)


class 시체발견(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=301, script='$52000073_QD__MAIN__1$', time=2)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_2002')
        self.select_camera_path(path_ids=[8005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 의문(self.ctx)


class 의문(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=301, script='$52000073_QD__MAIN__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 상황파악(self.ctx)


class 상황파악(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7002, enable=True)
        self.select_camera_path(path_ids=[8006], return_view=False) # 카메라 레논 얼굴로
        self.set_dialogue(type=1, spawn_id=301, script='$52000073_QD__MAIN__3$', time=3)
        self.set_npc_emotion_loop(spawn_id=301, sequence_name='Sit_down_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 현장목격(self.ctx)


class 현장목격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007], return_view=False) # 레논 뒤편으로
        self.spawn_monster(spawn_ids=[303]) # 다크윈드 대원 좌
        self.spawn_monster(spawn_ids=[304]) # 다크윈드 대원 우
        self.set_dialogue(type=1, spawn_id=303, script='$52000073_QD__MAIN__4$', time=3)
        self.set_npc_emotion_loop(spawn_id=303, sequence_name='Attack_Idle_A', duration=1500.0) # 다크윈드 대원 좌 모션
        self.set_npc_emotion_loop(spawn_id=304, sequence_name='Attack_Idle_A', duration=1500.0) # 다크윈드 대원 우 모션
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_2005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오해1(self.ctx)


class 오해1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=303, script='$52000073_QD__MAIN__5$', time=3)
        self.set_dialogue(type=1, spawn_id=304, script='$52000073_QD__MAIN__6$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오해2(self.ctx)


class 오해2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=303, script='$52000073_QD__MAIN__7$', time=3)
        self.set_dialogue(type=1, spawn_id=301, script='$52000073_QD__MAIN__8$', time=3, arg5=1)
        self.set_npc_emotion_loop(spawn_id=303, sequence_name='Attack_01_A', duration=2000.0) # 다크윈드 대원 좌 모션
        self.set_npc_emotion_loop(spawn_id=301, sequence_name='Talk_A', duration=3000.0) # 레논 대화 모션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오해3(self.ctx)


class 오해3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=303, script='$52000073_QD__MAIN__9$', time=3)
        self.set_dialogue(type=1, spawn_id=304, script='$52000073_QD__MAIN__10$', time=3, arg5=2)
        self.move_npc(spawn_id=303, patrol_name='MS2PatrolData_2003')
        self.move_npc(spawn_id=304, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오해4(self.ctx)


class 오해4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=303, sequence_name='Attack_Idle_A', duration=5000.0) # 다크윈드 대원 좌 모션
        self.set_dialogue(type=1, spawn_id=303, script='$52000073_QD__MAIN__11$', time=3)
        self.set_npc_emotion_loop(spawn_id=304, sequence_name='Attack_Idle_A', duration=5000.0) # 다크윈드 대원 우 모션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오해5(self.ctx)


class 오해5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=301, script='$52000073_QD__MAIN__12$', time=5)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_2006')
        self.set_npc_emotion_loop(spawn_id=303, sequence_name='Attack_Idle_A', duration=6000.0) # 다크윈드 대원 좌 모션
        self.set_npc_emotion_loop(spawn_id=304, sequence_name='Attack_Idle_A', duration=6000.0) # 다크윈드 대원 우 모션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 쓰러짐(self.ctx)


class 쓰러짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=303, sequence_name='Down_Idle_A', duration=500000.0) # 다크윈드 대원 좌 모션
        self.set_npc_emotion_loop(spawn_id=304, sequence_name='Down_Idle_A', duration=500000.0) # 다크윈드 대원 우 모션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 탈출(self.ctx)


class 탈출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_2007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 레논탈출(self.ctx)


class 레논탈출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[301])
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라시점변경_ready(self.ctx)


class 카메라시점변경_ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라시점변경(self.ctx)


class 카메라시점변경(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8008], return_view=False) # 공중뷰

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카트반등장(self.ctx)


class 카트반등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[305]) # 카트반

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카트반이동(self.ctx)


class 카트반이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=305, patrol_name='MS2PatrolData_2008')
        self.set_dialogue(type=1, spawn_id=305, script='$52000073_QD__MAIN__13$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 의미심장(self.ctx)


class 의미심장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11001024, msg='$52000073_QD__MAIN__14$', duration=3000, align=Align.Center)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 다크윈드통로(self.ctx)


class 다크윈드통로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.spawn_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[301,302,303,304,305])
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=52000138)


initial_state = idle
