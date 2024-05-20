""" trigger/52010063_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 트리스탄
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 인페르녹
        self.spawn_monster(spawn_ids=[111,112,113,114,115], auto_target=False) # npc 부하 크림슨 발록
        self.destroy_monster(spawn_ids=[211,212,213,214,215]) # 몬스터 부하 크림슨 발록
        self.set_effect(trigger_ids=[6000,6001,6002,6003,6004,6010,6011]) # 기빨고기빨리는이펙트
        self.set_mesh(trigger_ids=[4001,4002,4003,4004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            # <transition state="연출시작"/>
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000066], quest_states=[3]):
            return 맵이동_작전실로(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000066], quest_states=[2]):
            return 처치후_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000066], quest_states=[1]):
            return 처치후_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000065], quest_states=[3]):
            return 처치후_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000065], quest_states=[2]):
            return 처치후_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000065], quest_states=[1]):
            return 처치후_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000064], quest_states=[3]):
            return 처치후_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000064], quest_states=[2]):
            return 처치후_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000064], quest_states=[1]):
            return 연출시작(self.ctx)


class 처치후_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawn_ids=[101,102,111,112,113,114,115,211,212,213,214,215,221,222,223,224,225,226]) # 전체 npc
        self.move_user(map_id=52010063, portal_id=20) # 유저 퀘 시작 위치로
        self.spawn_monster(spawn_ids=[103], auto_target=False) # 퀘스트용 트리스탄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 처치후(self.ctx)


class 처치후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 맵이동_작전실로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,111,112,113,114,115,211,212,213,214,215,221,222,223,224,225,226]) # 트리스탄 제외 전체 npc

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 최종맵이동(self.ctx)


class 최종맵이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user(map_id=52010052, portal_id=1) # 스카이 포트리스 작전실로

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 최종맵이동(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=전투전스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Dead_A', duration=999999.0)
        # self.set_npc_emotion_loop(spawn_id=101, sequence_name='Attack_02_B', duration=999999.0) # 트리스탄 기빨림 모션
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Attack_02_D', duration=17000.0) # 인페르녹 기빨기 모션
        self.set_effect(trigger_ids=[6000,6003], visible=True) # 인페르녹 기빨기 이펙트
        self.set_effect(trigger_ids=[6001], visible=True) # 트리스탄 바닥 이펙트
        self.set_effect(trigger_ids=[6002], visible=True) # 트리스탄 기빨림 이펙트
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 인페르녹줌인00(self.ctx)


class 인페르녹줌인00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 인페르녹줌인01(self.ctx)


class 인페르녹줌인01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000,8001,8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return PC놀람01(self.ctx)


class PC놀람01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC놀람02(self.ctx)


class PC놀람02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52010063_QD__main__0$', duration=3000, align=Align.Right) # 트리스탄…?
        # pc

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹줌인02(self.ctx)


class 인페르녹줌인02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.add_cinematic_talk(npc_id=11003832, illust_id='infernog_nomal', msg='$52010063_QD__main__1$', duration=5000, align=Align.Right)
        self.set_effect(trigger_ids=[6000,6003]) # 인페르녹 기빨기 이펙트
        # 아니…?
        # 인페르녹
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Attack_03_D') # 인페르녹

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 인페르녹줌인03(self.ctx)


class 인페르녹줌인03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # action name="카메라경로를선택한다" arg1="8004" arg2="0"/>
        # 네놈은 누구인가.\n대체 어떻게 이곳에 들어올 수 있었단 말인가.
        self.add_cinematic_talk(npc_id=11003832, illust_id='infernog_nomal', msg='$52010063_QD__main__2$', duration=5000, align=Align.Right)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Attack_03_F')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 인페르녹줌인04(self.ctx)


class 인페르녹줌인04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        # 크르르… 너희는 대체 뭘 하고 있었던 것이냐!\n침입자가 들어오게 내버려두다니!
        self.add_cinematic_talk(npc_id=11003832, illust_id='infernog_nomal', msg='$52010063_QD__main__3$', duration=5000, align=Align.Right)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_Infernog_goforward') # 인페르녹 전진

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 부하대사01(self.ctx)


class 부하대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8011], return_view=False)
        self.add_cinematic_talk(npc_id=11003839, msg='$52010063_QD__main__4$', duration=3000, align=Align.Right) # 죄…죄송합니다!
        # 크림슨발록
        self.set_npc_emotion_sequence(spawn_id=114, sequence_name='Attack_01_A') # 크림슨발록

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 부하대사02(self.ctx)


class 부하대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8012], return_view=False)
        self.add_cinematic_talk(npc_id=11003839, msg='$52010063_QD__main__5$', duration=3000, align=Align.Right) # 지금 당장 처단을…! />
        self.set_npc_emotion_sequence(spawn_id=115, sequence_name='Attack_01_A') # 크림슨발록

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹대사01(self.ctx)


class 인페르녹대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        # 멍청한 녀석들.\n침입자가 들어온 순간 이번 의식은 끝난 것이다. />
        self.add_cinematic_talk(npc_id=11003832, illust_id='infernog_nomal', msg='$52010063_QD__main__6$', duration=4000, align=Align.Right)
        # 인페르녹
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Attack_02_F') # 인페르녹

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 인페르녹대사02(self.ctx)


class 인페르녹대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003,8005], return_view=False)
        # 이 가문의 버러지들은 사사건건 나를 성가시게 만드는구나….\n본래 내 것인데, 돌려받기 위해 이런 번거로운 일을 하게 만들다니
        self.add_cinematic_talk(npc_id=11003832, illust_id='infernog_nomal', msg='$52010063_QD__main__7$', duration=6000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 인페르녹대사03(self.ctx)


class 인페르녹대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8005], return_view=False)
        # 하지만… 다음 기회를 만드는 것은 아주 쉬운 일이지.\n내 혼을 먹은 이상, 이 녀석은 내 손바닥 안에 있는 것이나 마찬가지니까.
        self.add_cinematic_talk(npc_id=11003832, illust_id='infernog_nomal', msg='$52010063_QD__main__8$', duration=5000, align=Align.Right)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Attack_02_E')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 인페르녹대사04(self.ctx)


class 인페르녹대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003832, illust_id='infernog_nomal', msg='$52010063_QD__main__9$', duration=5000, align=Align.Right)
        # self.set_npc_emotion_loop(spawn_id=102, sequence_name='Attack_01_C, Attack_01_E', duration=4000.0) # 인페르녹
        # 나의 충실한 종복들이여. 실수를 만회할 기회를 주겠노라.\n침입자를 깨끗하게 정리하라." />
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Attack_03_D')
        # 인페르녹 뒤로

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 인페르녹대사05(self.ctx)


class 인페르녹대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004,8000], return_view=False)
        # 내가 이번 의식을 마무리하러 떠나 있는 동안 임무를 끝내라.\n두 번의 실수는 없어야 할 것이야!
        self.add_cinematic_talk(npc_id=11003832, illust_id='infernog_nomal', msg='$52010063_QD__main__10$', duration=5000, align=Align.Right)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Leave_01_A,Leave_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 부하들준비00(self.ctx)


class 부하들준비00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.add_cinematic_talk(npc_id=11003839, msg='$52010063_QD__main__11$', duration=3000, align=Align.Right) # 받들겠습니다…!
        self.set_effect(trigger_ids=[6010], visible=True) # 인페르녹 붉은 안개
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Leave_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 부하들등장00(self.ctx)


class 부하들등장00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 부하들등장01(self.ctx)


class 전투전스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawn_ids=[102]) # 인페르녹
        self.destroy_monster(spawn_ids=[111,112,113,114,115]) # npc 크림슨 발록
        self.spawn_monster(spawn_ids=[211]) # 몬스터 크림슨 발록
        self.move_user(map_id=52010063, portal_id=11) # 유저 전투 시작 위치로
        self.set_effect(trigger_ids=[6000,6003]) # 인페르녹 기빨기 이펙트
        self.set_effect(trigger_ids=[6010], visible=True) # 인페르녹 붉은 안개

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 부하들등장02(self.ctx)


class 부하들등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102]) # 인페르녹
        self.destroy_monster(spawn_ids=[111,112,113,114,115]) # npc 크림슨 발록
        self.spawn_monster(spawn_ids=[211,221,222,223,224,225,226], auto_target=False) # 몬스터 크림슨 발록
        self.move_user(map_id=52010063, portal_id=11) # 유저 전투 시작 위치로

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 부하들등장02(self.ctx)


class 부하들등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 부하들등장211(self.ctx)


class 부하들등장211(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[212])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[211]):
            return 부하들등장212(self.ctx)


class 부하들등장212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[213])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[212]):
            return 부하들등장213(self.ctx)


class 부하들등장213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[214])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[213]):
            return 부하들등장214215(self.ctx)


class 부하들등장214215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[215])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[214,215]):
            return 트리스탄구출00(self.ctx)


class 트리스탄구출00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawn_ids=[111,112,113,114,115,211,212,213,214,215,221,222,223,224,225,226]) # 부하 몬스터 청소
        self.set_achievement(trigger_id=9000, type='trigger', achieve='crimsonbalrogwipeout')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_mesh(trigger_ids=[4001,4002,4003,4004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄구출01(self.ctx)


class 트리스탄구출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawn_ids=[101]) # 트리스탄
        self.spawn_monster(spawn_ids=[103], auto_target=False) # 퀘스트용 트리스탄
        self.move_user(map_id=52010063, portal_id=20) # 유저 전투 시작 위치로
        self.set_effect(trigger_ids=[6001,6002]) # 트리스탄 바닥 이펙트
        # self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.1, duration=10.0, interpolator=1) # 10초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄구출02(self.ctx)


class 트리스탄구출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=전투후스킵완료, action='nextState') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set
        self.select_camera_path(path_ids=[8003,8013,8014], return_view=False)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Dead_A', duration=5000.0) # 트리스탄
        self.set_effect(trigger_ids=[6004], visible=True) # 트리스탄 잡힌 효과 꺼짐
        self.add_cinematic_talk(npc_id=11003825, illust_id='Tristan_normal', msg='$52010063_QD__main__12$', duration=5000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 트리스탄구출03(self.ctx)


class 트리스탄구출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6010]) # 인페르녹 붉은 안개
        self.set_effect(trigger_ids=[6011], visible=True) # 인페르녹 붉은 안개 꺼짐
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_Tristan_walk') # 트리스탄 전진

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄구출04(self.ctx)


class 트리스탄구출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8022,8021], return_view=False)
        self.add_cinematic_talk(npc_id=11003825, illust_id='Tristan_normal', msg='$52010063_QD__main__13$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='ChatUp_A', duration=3000.0) # 트리스탄
        self.set_effect(trigger_ids=[6004])
        self.set_effect(trigger_ids=[6011]) # 인페르녹 붉은 안개 꺼짐
        # Missing State: State,  setsceneskip 2 close
        self.set_scene_skip()
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출종료(self.ctx)


class 전투후스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000,6001,6002,6003,6004,6005,6010,6011])
        self.move_user(map_id=52010063, portal_id=20) # 유저 전투 시작 위치로
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_Tristan_walk') # 트리스탄 전진

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_mesh(trigger_ids=[4001,4002,4003,4004])
        self.set_achievement(trigger_id=9000, type='trigger', achieve='tristanrescue') # 퀘스트 완료 업적

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000065], quest_states=[3]):
            return 콘대르_대사(self.ctx)


class 콘대르_대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003534, illust='Conder_normal', script='$52010063_QD__main__15$', duration=12098, voice='ko/Npc/00002170')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12098):
            return 퀘스트유저감지_대사(self.ctx)


class 퀘스트유저감지_대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000066], quest_states=[3]):
            return 블리체_대사(self.ctx)


class 블리체_대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', script='$52010063_QD__main__14$', duration=13000, voice='ko/Npc/00002153')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return 마지막체크(self.ctx)


class 마지막체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000066], quest_states=[3]):
            return 맵이동_작전실로(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
