""" trigger/52000121_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[121,122,123,124,125,126,127,128,129,130,131], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001563], quest_states=[1]):
            # 50001563 퀘스트 진행 중 상태!
            return 연출준비(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001563], quest_states=[2]):
            # 맵 튕기고 완료가능 상태일 때 대비 위한 스테이트
            return 최종맵이동(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103,104], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 위기상황00(self.ctx)


class 위기상황00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_scene_skip(state=전투직전_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return 위기상황01(self.ctx)


class 위기상황01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 위기상황02(self.ctx)


class 위기상황02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 위기상황03(self.ctx)


class 위기상황03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 위기상황04(self.ctx)


class 위기상황04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 대치상황시작(self.ctx)


class 대치상황시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 오스칼대사01(self.ctx)


class 오스칼대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003309, script='$52000121_QD__MAIN__0$', time=4)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_B', duration=4000.0)
        self.set_skip(state=오스칼대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 투르카대사01(self.ctx)


class 오스칼대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 투르카대사01(self.ctx)


class 투르카대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003362, script='$52000121_QD__MAIN__1$', time=4)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Bore_B', duration=4000.0)
        self.set_skip(state=투르카대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 마노비치대사01(self.ctx)


class 투르카대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 마노비치대사01(self.ctx)


class 마노비치대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8022], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003308, script='$52000121_QD__MAIN__2$', time=3)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=3000.0)
        self.set_skip(state=마노비치대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카대사02(self.ctx)


class 마노비치대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 투르카대사02(self.ctx)


class 투르카대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8023], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003362, script='$52000121_QD__MAIN__3$', time=3)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3000.0)
        self.set_skip(state=투르카대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카대사03(self.ctx)


class 투르카대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 투르카대사03(self.ctx)


class 투르카대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003362, script='$52000121_QD__MAIN__4$', time=3)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3000.0)
        self.set_skip(state=투르카대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오스칼대사02(self.ctx)


class 투르카대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 오스칼대사02(self.ctx)


class 오스칼대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8021], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003309, script='$52000121_QD__MAIN__5$', time=3)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Attack_Idle_A', duration=4000.0)
        self.set_skip(state=오스칼대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카대사04(self.ctx)


class 오스칼대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 투르카대사04(self.ctx)


class 투르카대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8023], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003362, script='$52000121_QD__MAIN__6$', time=4)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=투르카대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아르마노열폭준비(self.ctx)


class 투르카대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노열폭준비(self.ctx)


class 아르마노열폭준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8025], return_view=False)
        self.face_emotion(spawn_id=104, emotion_name='Angry')
        # self.set_npc_emotion_loop(spawn_id=104, sequence_name='Talk_A', duration=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아르마노열폭시작(self.ctx)


class 아르마노열폭시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=104, emotion_name='Angry')
        self.add_cinematic_talk(npc_id=11003364, msg='$52000121_QD__MAIN__7$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아르마노달려(self.ctx)


class 아르마노달려(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8024], return_view=False)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_104_run')
        # self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101_Attack')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카공격00(self.ctx)


class 투르카공격00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8030], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101_Attack')
        self.add_cinematic_talk(npc_id=11003362, msg='$52000121_QD__MAIN__8$', duration=1000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카공격01(self.ctx)


class 투르카공격01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8031], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Attack_02_B')
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Run_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마노비치대사02(self.ctx)


class 마노비치대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8022], return_view=False)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Attack_Idle_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=11003308, msg='$52000121_QD__MAIN__9$', duration=1500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 리셋대기01(self.ctx)


class 리셋대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,104])
        self.spawn_monster(spawn_ids=[105,106], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 리셋대기02(self.ctx)


class 리셋대기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8040], return_view=False)
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Down_Idle_A', duration=30000.0)
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 잠시후(self.ctx)


class 잠시후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8041], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 불효자멘붕(self.ctx)


class 불효자멘붕(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=106, emotion_name='Cry')
        self.add_cinematic_talk(npc_id=11003364, msg='$52000121_QD__MAIN__10$', duration=1500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 오스칼멘붕(self.ctx)


class 오스칼멘붕(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Stun_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=11003309, illust_id='Oskhal_normal', msg='$52000121_QD__MAIN__11$', duration=2000, align=Align.Left)
        self.set_skip(state=오스칼멘붕_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 투르카대사05(self.ctx)


class 오스칼멘붕_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 투르카대사05(self.ctx)


class 투르카대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8035], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101_disappear_01')
        self.set_dialogue(type=2, spawn_id=11003362, script='$52000121_QD__MAIN__12$', time=4)
        self.set_skip(state=투르카대사05_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PC등장대기(self.ctx)


class 투르카대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC등장대기(self.ctx)


class PC등장대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8036], return_view=False)
        self.move_user(map_id=52000121, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 투르카대사06(self.ctx)


class 투르카대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101_disappear_02')
        self.set_dialogue(type=2, spawn_id=11003362, script='$52000121_QD__MAIN__13$', time=3)
        # # Missing State: 투르카대사06_skip
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC등장(self.ctx)


"""
class 투르카대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC등장(self.ctx)
"""

class PC등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8034], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_PC_Run')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101_disappear_04')
        self.set_dialogue(type=1, script='$52000121_QD__MAIN__14$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 투르카대사07(self.ctx)


class 투르카대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8036], return_view=False)
        # self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101_disappear_02')
        self.set_dialogue(type=2, spawn_id=11003362, script='$52000121_QD__MAIN__15$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카대사08(self.ctx)


class 투르카대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101_disappear_03')
        self.set_dialogue(type=2, spawn_id=11003362, script='$52000121_QD__MAIN__16$', time=2)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몬스터등장00(self.ctx)


class 몬스터등장00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[101])
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터등장01(self.ctx)


class 몬스터등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8037], return_view=False)
        self.destroy_monster(spawn_ids=[103])
        self.spawn_monster(spawn_ids=[110])
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터등장02(self.ctx)


class 몬스터등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8038], return_view=False)
        self.spawn_monster(spawn_ids=[108])
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터등장03(self.ctx)


class 몬스터등장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8039], return_view=False)
        self.spawn_monster(spawn_ids=[112])
        self.set_skip() # Missing State: State
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투대기01(self.ctx)


class 전투직전_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(path_ids=[8036], return_view=False)
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,108])
        self.spawn_monster(spawn_ids=[105,106], auto_target=False)
        self.spawn_monster(spawn_ids=[108,110,111,112])
        self.move_user(map_id=52000121, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투대기01(self.ctx)


class 전투대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        # self.add_cinematic_talk(npc_id=29000251, illust_id='Oskhal_normal', msg='$52000121_QD__MAIN__17$', duration=2000, align=Align.Left)
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투준비01(self.ctx)


class 전투준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[110,111,112]):
            return 전투시작02(self.ctx)


class 전투시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[113,114,115])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[113,114,115]):
            return 전투끝(self.ctx)


class 전투끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8040], return_view=False)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='ManovichMobKill')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 암전02(self.ctx)


class 암전02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return npc교체01(self.ctx)


class npc교체01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[108])
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아빠와아들대기(self.ctx)


class 아빠와아들대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8040], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=마노비치리타이어_스킵완료, action='exit') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마노비치대사03(self.ctx)


class 마노비치대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003361, script='$52000121_QD__MAIN__18$', time=2)
        self.set_skip(state=마노비치대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아르마노대사01(self.ctx)


class 마노비치대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사01(self.ctx)


class 아르마노대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8042], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003364, script='$52000121_QD__MAIN__19$', time=3)
        self.set_skip(state=아르마노대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아르마노대사02(self.ctx)


class 아르마노대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사02(self.ctx)


class 아르마노대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003364, script='$52000121_QD__MAIN__20$', time=3)
        self.set_skip(state=아르마노대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마노비치대사04(self.ctx)


class 아르마노대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 마노비치대사04(self.ctx)


class 마노비치대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8041], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003361, script='$52000121_QD__MAIN__21$', time=3)
        self.set_skip(state=마노비치대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마노비치대사05(self.ctx)


class 마노비치대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 마노비치대사05(self.ctx)


class 마노비치대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8045], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003361, script='$52000121_QD__MAIN__22$', time=3)
        self.set_skip(state=마노비치대사05_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마노비치대사06(self.ctx)


class 마노비치대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 마노비치대사06(self.ctx)


class 마노비치대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8046], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003361, script='$52000121_QD__MAIN__23$', time=3)
        self.set_skip(state=마노비치대사06_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마노비치대사07(self.ctx)


class 마노비치대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 마노비치대사07(self.ctx)


class 마노비치대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8043], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003361, script='$52000121_QD__MAIN__24$', time=2)
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Event_02_A')
        self.set_skip(state=마노비치대사07_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마노비치대사08(self.ctx)


class 마노비치대사07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 마노비치대사08(self.ctx)


class 마노비치대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8047], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003361, script='$52000121_QD__MAIN__25$', time=2)
        # self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Event_03_A')
        self.set_npc_emotion_loop(spawn_id=105, sequence_name='Event_03_A', duration=10000.0)
        self.set_skip(state=마노비치대사08_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마노비치죽음(self.ctx)


class 마노비치대사08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 마노비치죽음(self.ctx)


class 마노비치죽음(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8044], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Event_04_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 아르마노오열(self.ctx)


class 아르마노오열(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8050], return_view=False)
        self.add_cinematic_talk(npc_id=11003364, msg='$52000121_QD__MAIN__26$', duration=4000, align=Align.Left)
        # Missing State: State,  setsceneskip 2 close
        self.set_scene_skip()
        # setsceneskip 2 close
        # setsceneskip 2 close
        # setsceneskip 2 close
        # self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출종료(self.ctx)


class 마노비치리타이어_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[108])
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9000, type='trigger', achieve='ManovichRetire')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 최종맵이동(self.ctx)


class 최종맵이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000072, portal_id=1)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return 최종맵이동(self.ctx)


initial_state = 대기
