""" trigger/52000133_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,111,112])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001599], quest_states=[3]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001599], quest_states=[2]):
            return 예민한아노스(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001599], quest_states=[1]):
            return 예민한아노스(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001598], quest_states=[3]):
            return 예민한아노스(self.ctx)
        """
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001598], quest_states=[1]):
            return 예민한아노스(self.ctx)
        """
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001598], quest_states=[2]):
            # 엘리넬 마법학원 : 50001598 퀘스트 진행 중인 상태
            return 예민한아노스_연출준비(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001584], quest_states=[2]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001584], quest_states=[1]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001583], quest_states=[3]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001583], quest_states=[2]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001583], quest_states=[1]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001582], quest_states=[3]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001582], quest_states=[2]):
            # 엘리넬 마법학원 : 50001582 퀘스트 진행 중인 상태
            return 케이틀린첫만남_연출시작(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001582], quest_states=[1]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001581], quest_states=[3]):
            return 빈집(self.ctx)


class 케이틀린첫만남(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 케이틀린첫만남_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.spawn_monster(spawn_ids=[101])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000133, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 전경스케치01(self.ctx)


class 전경스케치01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전경스케치02(self.ctx)


class 전경스케치02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8001], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000133_QD__MAIN__0$', duration=2000, align=Align.Left)
        self.set_scene_skip(state=케이틀린첫만남_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전경스케치03(self.ctx)


class 전경스케치03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_PC01')
        # # 전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨
        self.set_skip(state=케이틀린첫만남_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전경스케치04(self.ctx)


class 전경스케치04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.add_cinematic_talk(npc_id=11003254, illust_id='Caitlyn_normal', msg='$52000133_QD__MAIN__1$', duration=3000, align=Align.Center)
        # # 전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨
        self.set_skip(state=케이틀린첫만남_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전경스케치05(self.ctx)


class 전경스케치05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.add_balloon_talk(spawn_id=101, msg='$52000133_QD__MAIN__2$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Bore_A', duration=3000.0)
        # # 전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨
        self.set_skip(state=케이틀린첫만남_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전경스케치06(self.ctx)


class 전경스케치06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_PC02')
        # # 전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨
        self.set_skip(state=케이틀린첫만남_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전경스케치07(self.ctx)


class 전경스케치07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='NameCaption', title='$52000133_QD__MAIN__3$', desc='$52000133_QD__MAIN__4$', align=Align.Center | Align.Right, offset_rate_x=-0.05, offset_rate_y=0.15, duration=10000, scale=2.0)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Bore_B', duration=4000.0)
        # # 전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨
        self.set_skip(state=케이틀린첫만남_스킵완료)
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출종료(self.ctx)


class 케이틀린첫만남_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52000133, portal_id=12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 예민한아노스(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111,113])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 예민한아노스_연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000133, portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 예민한아노스_연출시작(self.ctx)


class 예민한아노스_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8100], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 케이틀린대사01(self.ctx)


class 케이틀린대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8101], return_view=False)
        self.add_cinematic_talk(npc_id=11003258, illust_id='Caitlyn_normal', msg='$52000133_QD__MAIN__5$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Bore_A', duration=4600.0)
        self.move_user_path(patrol_name='2_MS2PatrolData_PC01')
        self.set_scene_skip(state=예민한아노스_스킵완료, action='nextState') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC대사01(self.ctx)


"""
class 케이틀린대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC대사01(self.ctx)
"""

class PC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8120], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000133_QD__MAIN__6$', duration=3000)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=2000.0)
        self.move_user_path(patrol_name='2_MS2PatrolData_PC02')
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 케이틀린대사02(self.ctx)


"""
class PC대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 케이틀린대사02(self.ctx)
"""

class 케이틀린대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003258, illust_id='Caitlyn_normal', msg='$52000133_QD__MAIN__7$', duration=3000, align=Align.Right)
        self.move_npc(spawn_id=111, patrol_name='2_MS2PatrolData_Katelyn01')
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC대사02(self.ctx)


"""
class 케이틀린대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC대사02(self.ctx)
"""

class PC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8110], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000133_QD__MAIN__8$', duration=3000, align=Align.Right)
        self.move_user_path(patrol_name='2_MS2PatrolData_PC03')
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=2000.0)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 케이틀린대사03(self.ctx)


"""
class PC대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 케이틀린대사03(self.ctx)
"""

class 케이틀린대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8110], return_view=False)
        self.spawn_monster(spawn_ids=[112])
        self.add_cinematic_talk(npc_id=11003258, illust_id='Caitlyn_normal', msg='$52000133_QD__MAIN__9$', duration=4000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Talk_A', duration=8200.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아노스걸어나옴(self.ctx)


"""
class 아노스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아노스걸어나옴(self.ctx)
"""

class 아노스걸어나옴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8140], return_view=False)
        self.add_cinematic_talk(npc_id=11003259, illust_id='Anos_normal', msg='$52000133_QD__MAIN__10$', duration=3000, align=Align.Left)
        self.move_npc(spawn_id=112, patrol_name='2_MS2PatrolData_Anos01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사01(self.ctx)


class 아노스대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003259, illust_id='Anos_normal', msg='$52000133_QD__MAIN__11$', duration=3000, align=Align.Left)
        self.move_npc(spawn_id=111, patrol_name='2_MS2PatrolData_Katelyn02')
        self.set_npc_emotion_loop(spawn_id=112, sequence_name='Talk_A', duration=3600.0)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC대사03(self.ctx)


"""
class 아노스대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC대사03(self.ctx)
"""

class PC대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000133_QD__MAIN__12$', align=Align.Center, duration=3000)
        self.set_pc_emotion_loop(sequence_name='Emotion_Hello_A', duration=2000.0)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사02(self.ctx)


"""
class PC대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사02(self.ctx)
"""

class 아노스대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003259, illust_id='Anos_normal', msg='$52000133_QD__MAIN__13$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=112, sequence_name='ChatUp_A', duration=7000.0)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC대사04(self.ctx)


"""
class 아노스대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC대사04(self.ctx)
"""

class PC대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8131], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000133_QD__MAIN__14$', duration=3000, align=Align.Right)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Surprise_A'])
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사03(self.ctx)


"""
class PC대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사03(self.ctx)
"""

class 아노스대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003259, illust_id='Anos_normal', msg='$52000133_QD__MAIN__15$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=112, sequence_name='Bore_A', duration=8100.0)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 케이틀린대사04(self.ctx)


"""
class 아노스대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 케이틀린대사04(self.ctx)
"""

class 케이틀린대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8132], return_view=False)
        self.add_cinematic_talk(npc_id=11003258, illust_id='Caitlyn_normal', msg='$52000133_QD__MAIN__16$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Talk_A', duration=12000.0)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사04(self.ctx)


"""
class 케이틀린대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사04(self.ctx)
"""

class 아노스대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003259, illust_id='Anos_normal', msg='$52000133_QD__MAIN__17$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=112, sequence_name='Bore_B', duration=9500.0)
        # self.set_skip(state=예민한아노스_스킵완료)

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
        self.select_camera_path(path_ids=[8133], return_view=False)
        self.add_cinematic_talk(npc_id=11003259, illust_id='Anos_normal', msg='$52000133_QD__MAIN__18$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=112, sequence_name='Talk_A', duration=6300.0)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 케이틀린대사05(self.ctx)


"""
class 아노스대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 케이틀린대사05(self.ctx)
"""

class 케이틀린대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003258, illust_id='Caitlyn_normal', msg='$52000133_QD__MAIN__19$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Bore_B', duration=7900.0)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 케이틀린대사06(self.ctx)


"""
class 케이틀린대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 케이틀린대사06(self.ctx)
"""

class 케이틀린대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003258, illust_id='Caitlyn_normal', msg='$52000133_QD__MAIN__20$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Talk_A', duration=6800.0)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사06(self.ctx)


"""
class 케이틀린대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사06(self.ctx)
"""

class 아노스대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8140], return_view=False)
        self.add_cinematic_talk(npc_id=11003259, illust_id='Anos_serious', msg='$52000133_QD__MAIN__21$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=112, sequence_name='Bore_A', duration=5800.0)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사07(self.ctx)


"""
class 아노스대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사07(self.ctx)
"""

class 아노스대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8140], return_view=False)
        self.add_cinematic_talk(npc_id=11003259, illust_id='Anos_serious', msg='$52000133_QD__MAIN__22$', duration=3000, align=Align.Left)
        # Missing State: State,  setsceneskip 2 close
        self.set_scene_skip()
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출종료(self.ctx)


class 예민한아노스_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.spawn_monster(spawn_ids=[113])
        self.destroy_monster(spawn_ids=[112])
        self.move_user(map_id=52000133, portal_id=13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 빈집(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
