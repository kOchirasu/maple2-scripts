""" trigger/02000072_in/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001566], quest_states=[3]):
            # 50001566 완료 이후부터 쓰러진 마노비치만 있는 집. 이후 시나리오 변경 시 이 부분도 내용에 맞게 수정 요망
            return 환자홀로있는집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001566], quest_states=[2]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001566], quest_states=[1]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001565], quest_states=[3]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001565], quest_states=[2]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001565], quest_states=[1]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001564], quest_states=[3]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001564], quest_states=[2]):
            # 50001564 완료가능시 아르마노 가출하고 조디와 대화하는 연출
            return 아르마노가출대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001564], quest_states=[1]):
            return 아르마노가출전(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001563], quest_states=[3]):
            return 아르마노가출전(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001563], quest_states=[2]):
            return 아르마노가출전(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001563], quest_states=[1]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[3]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[2]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001561], quest_states=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001561], quest_states=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001561], quest_states=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001560], quest_states=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001560], quest_states=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001560], quest_states=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001559], quest_states=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001559], quest_states=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001559], quest_states=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001558], quest_states=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001558], quest_states=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001558], quest_states=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001557], quest_states=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001557], quest_states=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001557], quest_states=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001556], quest_states=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001556], quest_states=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001556], quest_states=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001555], quest_states=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001555], quest_states=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001555], quest_states=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001554], quest_states=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001554], quest_states=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001554], quest_states=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001553], quest_states=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001553], quest_states=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001553], quest_states=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[2]):
            # 50001552 완료가능시 오스칼 퇴장하는 연출
            return 오스칼퇴장대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[1]):
            return 침공직후상태(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[3]):
            return 침공직후상태(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[2]):
            return 침공직후상태(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[1]):
            return 빈집(self.ctx)


class 빈집(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 침공직후상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[2]):
            # 50001552 완료가능시 오스칼 퇴장하는 연출
            return 오스칼퇴장연출(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[1]):
            return 침공직후상태01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[3]):
            return 침공직후상태01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[2]):
            return 침공직후상태01(self.ctx)


class 침공직후상태01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[2]):
            # 50001552 완료가능시 오스칼 퇴장하는 연출
            return 오스칼퇴장연출(self.ctx)
        """
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[3]):
            return 침공직후상태02(self.ctx)
        """
        """
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[2]):
            return 침공직후상태02(self.ctx)
        """
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[2]):
            return 침공직후상태02(self.ctx)


class 침공직후상태02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[2]):
            # 50001552 완료가능시 오스칼 퇴장하는 연출
            return 오스칼퇴장연출(self.ctx)
        """
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[1]):
            return 침공직후상태01(self.ctx)
        """
        """
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[3]):
            return 침공직후상태01(self.ctx)
        """
        """
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[2]):
            return 침공직후상태01(self.ctx)
        """
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[2]):
            return 침공직후상태01(self.ctx)


class 오스칼퇴장대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8001], return_view=False)
        self.spawn_monster(spawn_ids=[101,102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[2]):
            return 오스칼퇴장연출(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[2]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 오스칼퇴장연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_Wayout_102_O')
        self.add_balloon_talk(spawn_id=102, msg='$02000072_IN__MAIN__0$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오스칼퇴장연출종료(self.ctx)


class 오스칼퇴장연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.destroy_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        """
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[2]):
            return 퀘스트조건체크(self.ctx)
        """
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001552], quest_states=[2]):
            return 종료(self.ctx)


# 50001552 완료가능시 오스칼 퇴장하는 연출 종료
class 마노비치혼자(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 종료(self.ctx)


class 아르마노가출전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103,104,105,106], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001564], quest_states=[2]):
            return 아르마노가출연출(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001564], quest_states=[2]):
            return 아르마노가출전01(self.ctx)


class 아르마노가출전01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001564], quest_states=[2]):
            return 아르마노가출연출(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001564], quest_states=[2]):
            return 아르마노가출전02(self.ctx)


class 아르마노가출전02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001564], quest_states=[2]):
            return 아르마노가출연출(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001564], quest_states=[2]):
            return 아르마노가출전01(self.ctx)


class 아르마노가출대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[103,104,105,106], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 아르마노가출연출(self.ctx)


class 아르마노가출연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.move_user(map_id=2000072, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 아르마노대사01(self.ctx)


class 아르마노대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8011], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003244, script='$02000072_IN__MAIN__1$', time=4)
        self.set_scene_skip(state=아르마노가출_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아르마노대사02(self.ctx)


"""
class 아르마노대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사02(self.ctx)
"""

class 아르마노대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003244, script='$02000072_IN__MAIN__2$', time=5)
        # self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_Wayout_104_A')
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 오스칼대사01(self.ctx)


"""
class 아르마노대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 오스칼대사01(self.ctx)
"""

class 오스칼대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8013], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003245, script='$02000072_IN__MAIN__3$', time=4)
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 아르마노대사03(self.ctx)


"""
class 오스칼대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사03(self.ctx)
"""

class 아르마노대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8014], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003244, script='$02000072_IN__MAIN__4$', time=5)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 오스칼대사02(self.ctx)


"""
class 아르마노대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 오스칼대사02(self.ctx)
"""

class 오스칼대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8013], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003245, script='$02000072_IN__MAIN__5$', time=8)
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Talk_A', duration=8000.0)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7500):
            return 오스칼대사03(self.ctx)


"""
class 오스칼대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 오스칼대사03(self.ctx)
"""

class 오스칼대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8013], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003245, script='$02000072_IN__MAIN__6$', time=8)
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Talk_A', duration=8000.0)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 오스칼대사04(self.ctx)


"""
class 오스칼대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 오스칼대사04(self.ctx)
"""

class 오스칼대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003245, script='$02000072_IN__MAIN__7$', time=4)
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Talk_A', duration=8000.0)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 아르마노대사04(self.ctx)


"""
class 오스칼대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사04(self.ctx)
"""

class 아르마노대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8014], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003244, script='$02000072_IN__MAIN__8$', time=6)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 아르마노대사05(self.ctx)


"""
class 아르마노대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사05(self.ctx)
"""

class 아르마노대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003244, script='$02000072_IN__MAIN__9$', time=8)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 프레이대사01(self.ctx)


"""
class 아르마노대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 프레이대사01(self.ctx)
"""

class 프레이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8012], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003246, script='$02000072_IN__MAIN__10$', time=7)
        self.set_npc_emotion_loop(spawn_id=106, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 아르마노대사06(self.ctx)


"""
class 프레이대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사06(self.ctx)
"""

class 아르마노대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8014], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003244, script='$02000072_IN__MAIN__11$', time=8)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 프레이대사02(self.ctx)


"""
class 아르마노대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 프레이대사02(self.ctx)
"""

class 프레이대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8012], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003246, script='$02000072_IN__MAIN__12$', time=9)
        self.set_npc_emotion_loop(spawn_id=106, sequence_name='Talk_A', duration=9000.0)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 아르마노대사07(self.ctx)


"""
class 프레이대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사07(self.ctx)
"""

class 아르마노대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8014,8015], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003244, script='$02000072_IN__MAIN__13$', time=3)
        self.spawn_monster(spawn_ids=[107])
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아르마노대사08(self.ctx)


"""
class 아르마노대사07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사08(self.ctx)
"""

class 아르마노대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8015], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003244, script='$02000072_IN__MAIN__14$', time=6)
        # Missing State: 아르마노가출_스킵완료_조디제외
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 아르마노탈주(self.ctx)


"""
class 아르마노대사08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노탈주(self.ctx)
"""

class 아르마노탈주(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8015], return_view=False)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_Wayout_104_A')
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_Walkin_107_J')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC멈칫(self.ctx)


class PC멈칫(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104])
        self.move_user_path(patrol_name='MS2PatrolData_PC_Follow')
        # self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_Walkin_107_J')
        self.set_dialogue(type=1, script='$02000072_IN__MAIN__15$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 조디등장(self.ctx)


class 조디등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8016], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 조디대사01(self.ctx)


class 조디대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8017], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003247, script='$02000072_IN__MAIN__16$', time=3)
        self.set_npc_emotion_loop(spawn_id=107, sequence_name='Talk_A', duration=3000.0)
        # Missing State: 아르마노가출_스킵완료_조디제외
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 조디대사02(self.ctx)


"""
class 조디대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 조디대사02(self.ctx)
"""

class 조디대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003247, script='$02000072_IN__MAIN__17$', time=4)
        self.set_npc_emotion_loop(spawn_id=107, sequence_name='Talk_A', duration=4000.0)
        # Missing State: 아르마노가출_스킵완료_조디제외
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PC안녕(self.ctx)


"""
class 조디대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC안녕(self.ctx)
"""

class PC안녕(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Hello_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 조디대사03(self.ctx)


class 조디대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003247, script='$02000072_IN__MAIN__18$', time=3)
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아르마노가출연출종료(self.ctx)


class 아르마노가출_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        # 중복 스폰 막기 위해 이동하는 조디, 고정된 조디 소멸 처리
        self.destroy_monster(spawn_ids=[107,108])
        self.destroy_monster(spawn_ids=[104]) # 과정상 사라지는 아르마노 소멸
        self.spawn_monster(spawn_ids=[108]) # 퀘스트 완료 npc 조디 스폰
        # PC 조디 앞으로 이동. 안 되면 포탈 위치로 이동시킬 것
        self.move_user_path(patrol_name='MS2PatrolData_PC_Follow')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아르마노가출연출종료(self.ctx)


class 아르마노가출연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 아르마노가출후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103,105,106,108], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001566], quest_states=[3]):
            return 환자홀로있는집(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 환자홀로있는집(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
