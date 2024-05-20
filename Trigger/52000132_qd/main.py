""" trigger/52000132_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001599], quest_states=[3]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001584], quest_states=[2]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001584], quest_states=[1]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001583], quest_states=[3]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001583], quest_states=[2]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001583], quest_states=[1]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001582], quest_states=[3]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001582], quest_states=[2]):
            # 엘리넬 마법학원 : 50001582 퀘스트 진행 중인 상태
            return 아이들과만남_연출대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001582], quest_states=[1]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001581], quest_states=[3]):
            return 빈집(self.ctx)


class 아이들과만남_연출대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000132, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아이들과만남_연출시작(self.ctx)


class 아이들과만남_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user_path(patrol_name='MS2PatrolData_PC00')
        self.set_scene_skip(state=아이들과인사_스킵완료, action='exit') # setsceneskip set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 리안인사01(self.ctx)


class 리안인사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003253, illust_id='0', msg='$52000132_QD__MAIN__0$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Bore_B', duration=4000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 메린인사01(self.ctx)


"""
class 리안인사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 메린인사01(self.ctx)
"""

class 메린인사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003252, illust_id='0', msg='$52000132_QD__MAIN__1$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Bore_B', duration=6000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC인사01(self.ctx)


"""
class 메린인사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC인사01(self.ctx)
"""

class PC인사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000132_QD__MAIN__2$', duration=3000, align=Align.Right)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=3000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 리안대사01(self.ctx)


"""
class PC인사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 리안대사01(self.ctx)
"""

class 리안대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003253, illust_id='0', msg='$52000132_QD__MAIN__3$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 메린대사01(self.ctx)


"""
class 리안대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 메린대사01(self.ctx)
"""

class 메린대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003252, illust_id='0', msg='$52000132_QD__MAIN__4$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Bore_C', duration=7000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 리안대사02(self.ctx)


"""
class 메린대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 리안대사02(self.ctx)
"""

class 리안대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003253, illust_id='0', msg='$52000132_QD__MAIN__5$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Bore_A', duration=3000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC대사02(self.ctx)


"""
class 리안대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC대사02(self.ctx)
"""

class PC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000132_QD__MAIN__6$', duration=3000, align=Align.Right)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=1000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 리안대사03(self.ctx)


"""
class PC대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 리안대사03(self.ctx)
"""

class 리안대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003253, illust_id='0', msg='$52000132_QD__MAIN__7$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=6000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 메린대사02(self.ctx)


"""
class 리안대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 메린대사02(self.ctx)
"""

class 메린대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003252, illust_id='0', msg='$52000132_QD__MAIN__8$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4500.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아이들이동01(self.ctx)


"""
class 메린대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아이들이동01(self.ctx)
"""

class 아이들이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        # self.move_user_path(patrol_name='MS2PatrolData_PC01')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_boy01')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_girl01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 유저이동01(self.ctx)


class 유저이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 리안대사04(self.ctx)


class 리안대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8003], return_view=False)
        self.add_cinematic_talk(npc_id=11003253, illust_id='0', msg='$52000132_QD__MAIN__9$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=7000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 메린대사03(self.ctx)


"""
class 리안대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 메린대사03(self.ctx)
"""

class 메린대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003252, illust_id='0', msg='$52000132_QD__MAIN__10$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=13000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 리안대사05(self.ctx)


"""
class 메린대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 리안대사05(self.ctx)
"""

class 리안대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003253, illust_id='0', msg='$52000132_QD__MAIN__11$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=4300.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아이들이동02(self.ctx)


"""
class 리안대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아이들이동02(self.ctx)
"""

class 아이들이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        # self.move_user_path(patrol_name='MS2PatrolData_PC01')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_boy02')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_girl02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 유저이동02(self.ctx)


class 유저이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 메린대사04(self.ctx)


class 메린대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003252, illust_id='0', msg='$52000132_QD__MAIN__12$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=8900.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 메린대사05(self.ctx)


"""
class 메린대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 메린대사05(self.ctx)
"""

class 메린대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003252, illust_id='0', msg='$52000132_QD__MAIN__13$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4700.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC대사03(self.ctx)


"""
class 메린대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC대사03(self.ctx)
"""

class PC대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000132_QD__MAIN__14$', duration=3000, align=Align.Right)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=2000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 리안대사06(self.ctx)


"""
class PC대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 리안대사06(self.ctx)
"""

class 리안대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003253, illust_id='0', msg='$52000132_QD__MAIN__15$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3200.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 메린대사06(self.ctx)


"""
class 리안대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 메린대사06(self.ctx)
"""

class 메린대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003252, illust_id='0', msg='$52000132_QD__MAIN__16$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=2000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아이들이동03(self.ctx)


"""
class 메린대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아이들이동03(self.ctx)
"""

class 아이들이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        # self.move_user_path(patrol_name='MS2PatrolData_PC01')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_boy03')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_girl03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 유저이동03(self.ctx)


class 유저이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 메린대사07(self.ctx)


class 메린대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003252, illust_id='0', msg='$52000132_QD__MAIN__17$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=7400.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 리안대사07(self.ctx)


"""
class 메린대사07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 리안대사07(self.ctx)
"""

class 리안대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003253, illust_id='0', msg='$52000132_QD__MAIN__18$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3700.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 메린대사08(self.ctx)


"""
class 리안대사07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 메린대사08(self.ctx)
"""

class 메린대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003252, illust_id='0', msg='$52000132_QD__MAIN__19$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=2000.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아이들이동04(self.ctx)


"""
class 메린대사08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아이들이동04(self.ctx)
"""

class 아이들이동04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_boy04')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_girl04')
        self.move_user_path(patrol_name='MS2PatrolData_PC04')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 리안대사08(self.ctx)


class 리안대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)
        self.add_cinematic_talk(npc_id=11003253, illust_id='0', msg='$52000132_QD__MAIN__20$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3200.0)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 메린대사09(self.ctx)


"""
class 리안대사08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 메린대사09(self.ctx)
"""

class 메린대사09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003252, illust_id='0', msg='$52000132_QD__MAIN__21$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아이들달림(self.ctx)


class 아이들달림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_boy_run')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_girl_run')
        self.move_user_path(patrol_name='MS2PatrolData_PC05')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아이들과인사(self.ctx)


class 아이들과인사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC06')
        self.set_pc_emotion_sequence(sequence_names=['Hello_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 방정리(self.ctx)


class 방정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.destroy_monster(spawn_ids=[101,102])
        self.move_user_path(patrol_name='MS2PatrolData_PC06')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 유저맵이동_연출종료(self.ctx)


class 유저맵이동_연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.destroy_monster(spawn_ids=[101,102])
        self.move_user(map_id=52000132, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 빈집(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 아이들과인사_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=3.0)
        self.destroy_monster(spawn_ids=[101,102])
        self.move_user(map_id=52000132, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=3.0)
        self.move_user(map_id=52000133, portal_id=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
