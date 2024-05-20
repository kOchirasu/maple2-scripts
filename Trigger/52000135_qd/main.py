""" trigger/52000135_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102])
        self.set_mesh(trigger_ids=[3000,3001]) # 아이노 크리스탈 on/off 컨트롤
        self.set_mesh_animation(trigger_ids=[3000]) # 아이노 크리스탈 on/off 컨트롤
        # self.set_mesh(trigger_ids=[10001175], visible=True)
        self.set_interact_object(trigger_ids=[10001175], state=1) # 아이노 크리스탈
        self.set_effect(trigger_ids=[3010,3011,3012])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001582], quest_states=[1]):
            return 연출이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001581], quest_states=[3]):
            return 연출이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001581], quest_states=[2]):
            return 연출이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001581], quest_states=[1]):
            return 연출대기(self.ctx)


class 연출이후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 연출대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000135, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아노스대사01(self.ctx)


class 아노스대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_01')
        self.add_cinematic_talk(npc_id=11003251, illust_id='Anos_normal', msg='$52000135_QD__MAIN__0$', duration=4000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=8500.0)
        self.set_scene_skip(state=오브젝트조사전_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아노스대사02(self.ctx)


"""
class 아노스대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사02(self.ctx)
"""

class 아노스대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003251, illust_id='Anos_normal', msg='$52000135_QD__MAIN__1$', duration=4000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=6800.0)
        self.set_skip(state=아노스대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아노스대사03(self.ctx)


class 아노스대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사03(self.ctx)


class 아노스대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002])
        self.add_cinematic_talk(npc_id=11003251, illust_id='0', msg='$52000135_QD__MAIN__2$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='ChatUp_A', duration=5400.0)
        self.move_user_path(patrol_name='MS2PatrolData_PC_03')
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오브젝트조사(self.ctx)


class 오브젝트조사전_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52000135, portal_id=10) # 퀘스트 시작 위치로 pc 이동
        # self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 오브젝트조사(self.ctx)


class 오브젝트조사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001175], state=0):
            return 오브젝트반응이후(self.ctx)


class 오브젝트반응이후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003,8004], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_mesh(trigger_ids=[3000], visible=True) # 아이노 크리스탈 on
        self.set_mesh_animation(trigger_ids=[3000], visible=True) # 아이노 크리스탈 on
        self.set_effect(trigger_ids=[3011], visible=True)
        self.set_interact_object(trigger_ids=[10001175], state=2)
        self.move_user_path(patrol_name='MS2PatrolData_PC_0301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아노스대사04(self.ctx)


class 아노스대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003251, illust_id='Anos_normal', msg='$52000135_QD__MAIN__3$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=7000.0)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_0201')
        self.set_scene_skip(state=오브젝트조사후_스킵완료, action='nextState') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사05(self.ctx)


"""
class 아노스대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사05(self.ctx)
"""

class 아노스대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003251, illust_id='Anos_normal', msg='$52000135_QD__MAIN__4$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=8300.0)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_0202')
        self.set_skip(state=아노스대사05_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사06(self.ctx)


class 아노스대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사06(self.ctx)


class 아노스대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003251, illust_id='Anos_normal', msg='$52000135_QD__MAIN__5$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=6500.0)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_0203')
        self.set_skip(state=아노스대사06_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사07(self.ctx)


class 아노스대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사07(self.ctx)


class 아노스대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003251, illust_id='Anos_normal', msg='$52000135_QD__MAIN__6$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Chatup_A', duration=7900.0)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_0204')
        self.set_skip(state=아노스대사07_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크리스탈끄기(self.ctx)


class 아노스대사07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 크리스탈끄기(self.ctx)


class 크리스탈끄기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_0205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 크리스탈꺼짐(self.ctx)


class 크리스탈꺼짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.set_mesh(trigger_ids=[3000]) # 아이노 크리스탈 on-off
        # self.set_mesh_animation(trigger_ids=[3000])
        self.set_mesh(trigger_ids=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_mesh_animation(trigger_ids=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_effect(trigger_ids=[3011])
        self.set_effect(trigger_ids=[3012], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아노스대사08(self.ctx)


class 아노스대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8005], return_view=False)
        self.add_cinematic_talk(npc_id=11003251, illust_id='0', msg='$52000135_QD__MAIN__7$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=11000.0)
        self.set_effect(trigger_ids=[3012])
        self.set_skip(state=아노스대사08_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아시모프대사01(self.ctx)


class 아노스대사08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아시모프대사01(self.ctx)


class 아시모프대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.add_cinematic_talk(npc_id=11003250, illust_id='0', msg='$52000135_QD__MAIN__8$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=5100.0)
        self.set_skip(state=아시모프대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사09(self.ctx)


class 아시모프대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사09(self.ctx)


class 아노스대사09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003251, illust_id='0', msg='$52000135_QD__MAIN__9$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3800.0)
        self.move_user_path(patrol_name='MS2PatrolData_PC_0302')
        self.set_skip(state=아노스대사09_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC크리스탈접근(self.ctx)


class 아노스대사09_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC크리스탈접근(self.ctx)


class PC크리스탈접근(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000135_QD__MAIN__10$', duration=2000, align=Align.Right)
        self.set_pc_emotion_loop(sequence_name='Object_React_H', duration=1500.0)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=2000.0)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=2000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크리스탈켜짐(self.ctx)


class 크리스탈켜짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8011], return_view=False)
        self.set_mesh(trigger_ids=[3001]) # 아이노 크리스탈 off-on
        self.set_mesh_animation(trigger_ids=[3001]) # 아이노 크리스탈 off-on
        self.set_mesh(trigger_ids=[3000], visible=True) # 아이노 크리스탈 off-on
        self.set_mesh_animation(trigger_ids=[3000], visible=True) # 아이노 크리스탈 off-on
        self.set_effect(trigger_ids=[3010], visible=True)
        self.add_balloon_talk(msg='$52000135_QD__MAIN__11$', duration=3000, delay_tick=1000)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Surprise_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마법사들접근(self.ctx)


class 마법사들접근(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8012], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_Asimov_05')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_04')
        self.set_effect(trigger_ids=[3011], visible=True)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Think_A'])
        self.add_balloon_talk(spawn_id=101, msg='$52000135_QD__MAIN__12$', duration=2000, delay_tick=100)
        self.add_balloon_talk(spawn_id=102, msg='$52000135_QD__MAIN__13$', duration=2000, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아노스대사10(self.ctx)


class 아노스대사10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003251, illust_id='0', msg='$52000135_QD__MAIN__14$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3400.0)
        self.set_skip(state=아노스대사10_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC대사(self.ctx)


class 아노스대사10_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC대사(self.ctx)


class PC대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000135_QD__MAIN__15$', duration=3000)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_06')
        self.set_pc_emotion_sequence(sequence_names=['Talk_A'])
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크리스탈다시꺼짐(self.ctx)


class 크리스탈다시꺼짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_mesh(trigger_ids=[3000]) # 아이노 크리스탈 on-off
        self.set_mesh_animation(trigger_ids=[3000]) # 아이노 크리스탈 on-off
        self.set_mesh(trigger_ids=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_mesh_animation(trigger_ids=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_effect(trigger_ids=[3010,3011])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아노스대사11(self.ctx)


class 아노스대사11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003251, illust_id='0', msg='$52000135_QD__MAIN__16$', duration=5000, align=Align.Right)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_07')
        self.set_skip(state=아노스대사11_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 아시모프대사02(self.ctx)


class 아노스대사11_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아시모프대사02(self.ctx)


class 아시모프대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.add_cinematic_talk(npc_id=11003250, illust_id='Asimov_normal', msg='$52000135_QD__MAIN__17$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=8600.0)
        # Missing State: State,  setsceneskip 2 close
        self.set_scene_skip()
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출종료(self.ctx)


class 오브젝트조사후_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_Asimov_05') # 아시모프 이동. 굳이 안 해도 될 것 같음
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_07') # 아노스 이동. 굳이 안 해도 될 것 같음
        self.set_mesh(trigger_ids=[3000]) # 아이노 크리스탈 on-off
        self.set_mesh_animation(trigger_ids=[3000]) # 아이노 크리스탈 on-off
        self.set_mesh(trigger_ids=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_mesh_animation(trigger_ids=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_effect(trigger_ids=[3010,3011])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='Studyindarkness')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
