""" trigger/52020004_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[3]):
            return 빈방(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[2]):
            return 트럭으로가세요_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[1]):
            return 세리하첫등장연출_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[3]):
            return 제이든만_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[2]):
            return 제이든만_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[1]):
            return 제이든만_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001761], quest_states=[3]):
            return 제이든만_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001761], quest_states=[2]):
            return 제이든호출_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001761], quest_states=[1]):
            return 제이든호출_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001760], quest_states=[3]):
            return 라딘에게돌아가_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001760], quest_states=[2]):
            return 라딘에게돌아가_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001760], quest_states=[1]):
            return 공주님과기사연출_대기(self.ctx)


class 기본(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 라딘에게돌아가_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001760], quest_states=[3]):
            return 라딘에게돌아가(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001760], quest_states=[2]):
            return 라딘에게돌아가(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001760], quest_states=[2]):
            return 퀘스트조건체크(self.ctx)


class 라딘에게돌아가(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020002, portal_id=1)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return 라딘에게돌아가(self.ctx)


class 제이든호출_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001761], quest_states=[2]):
            return 제이든호출_연출준비(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001761], quest_states=[1]):
            return 제이든호출_연출준비(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001761], quest_states=[2]):
            return 퀘스트조건체크(self.ctx)


class 기본_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[1]):
            return 세리하첫등장연출_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[3]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[2]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[1]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001761], quest_states=[3]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001773], quest_states=[1]):
            return 퀘스트조건체크(self.ctx)


class 조건확인_대기01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[1]):
            return 세리하첫등장연출_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[3]):
            return 조건확인_대기02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[2]):
            return 조건확인_대기02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[1]):
            return 몬스터체크(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001761], quest_states=[3]):
            return 조건확인_대기02(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[1]):
            return 조건확인_대기02(self.ctx)


class 조건확인_대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[1]):
            return 세리하첫등장연출_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[3]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[2]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001762], quest_states=[1]):
            return 몬스터체크(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001761], quest_states=[3]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[1]):
            return 조건확인_대기01(self.ctx)


class 트럭으로가세요_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[3]):
            return 트럭으로가세요(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[2]):
            return 트럭으로가세요(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001763], quest_states=[3]):
            return 퀘스트조건체크(self.ctx)


class 트럭으로가세요(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020005, portal_id=1)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return 트럭으로가세요(self.ctx)


class 빈방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,105,106,107,108,109,110,111,121,122,131,132,133])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 공주님과기사연출_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52020004, portal_id=1) # 유저 첫 위치 잡기
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=공주님과기사연출_스킵완료, action='exit') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 공주님과기사연출_시작(self.ctx)


class 공주님과기사연출_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.visible_my_pc(is_visible=False) # PC안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공주와기사00(self.ctx)


class 공주와기사00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003675, illust_id='Krantz_normal', msg='이곳은… 꽤나 오랜만에 오는 것 같군요. ', duration=3000)
        self.move_npc(spawn_id=102, patrol_name='krantz_walkin')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공주와기사01(self.ctx)


class 공주와기사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.add_cinematic_talk(npc_id=11003674, illust_id='Eone_normal', msg='그렇구나. …다시 올 일이 없을 줄 알았지만. ', duration=3000)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_Krantz_walking')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공주와기사02(self.ctx)


class 공주와기사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.add_cinematic_talk(npc_id=11003675, illust_id='Krantz_normal', msg='제게 내리실 명령이 무엇입니까?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공주와기사03(self.ctx)


class 공주와기사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_Krantz_promise')
        self.add_cinematic_talk(npc_id=11003674, illust_id='Eone_normal', msg='기다려 달라.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공주와기사04(self.ctx)


class 공주와기사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.add_cinematic_talk(npc_id=11003675, illust_id='Krantz_normal', msg='헐….', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.add_cinematic_talk(npc_id=11003674, illust_id='Eone_normal', msg='연출을 보강할 예정이니 기다려 달라.\\n이 연출엔 대사가 추가될 것이다.', duration=3000)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3000.0)
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공주님과기사연출_종료(self.ctx)


class 공주님과기사연출_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 공주님과기사연출_종료(self.ctx)


class 공주님과기사연출_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='PrincessMeetsHerKnight')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 라딘에게돌아가(self.ctx)


class 제이든만_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,110,111,112,121,122,131,132,133])
        self.spawn_monster(spawn_ids=[110], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 조건확인_대기01(self.ctx)


class 제이든호출_연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.spawn_monster(spawn_ids=[105,106,107,108,109], auto_target=False)
        self.destroy_monster(spawn_ids=[101,102,111,112,121,122,131,132,133])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 제이든호출_연출시작(self.ctx)


class 제이든호출_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=제이든호출_스킵완료, action='nextState') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC진입_놀람(self.ctx)


class PC진입_놀람(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007,8008,8009], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=0, msg='이건 대체… 무슨 상황이지?', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 제이든짜증01(self.ctx)


class 제이든짜증01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.add_cinematic_talk(npc_id=11003541, illust_id='Jaiden_normal', msg='…몰라서 물어?', duration=3000)
        # self.set_npc_emotion_loop(spawn_id=110, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 제이든짜증02(self.ctx)


class 제이든짜증02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8011], return_view=False)
        self.add_cinematic_talk(npc_id=11003541, illust_id='Jaiden_normal', msg='부주의한 누구 덕에 난리가 난 상황이다.', duration=3000)
        self.set_npc_emotion_loop(spawn_id=110, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 제이든짜증03(self.ctx)


class 제이든짜증03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8012], return_view=False)
        self.add_cinematic_talk(npc_id=11003541, illust_id='Jaiden_normal', msg='빨리 이쪽으로 넘어와! 어서!', duration=2000)
        self.set_npc_emotion_loop(spawn_id=110, sequence_name='Talk_A', duration=3000.0)
        # Missing State: State,  setsceneskip 2 close
        self.set_scene_skip()
        # setsceneskip 2 close
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 제이든호출_연출종료(self.ctx)


class 제이든호출_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 제이든호출_연출종료(self.ctx)


class 제이든호출_연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 조건확인_대기01(self.ctx)


class 몬스터체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[105,106,107,108,109]):
            return 몬스터추가스폰01(self.ctx)
        if self.monster_dead(spawn_ids=[105]):
            return 몬스터추가스폰105(self.ctx)
        if self.monster_dead(spawn_ids=[106]):
            return 몬스터추가스폰106(self.ctx)
        if self.monster_dead(spawn_ids=[107]):
            return 몬스터추가스폰107(self.ctx)
        if self.monster_dead(spawn_ids=[108]):
            return 몬스터추가스폰108(self.ctx)
        if self.monster_dead(spawn_ids=[109]):
            return 몬스터추가스폰109(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 조건확인_대기01(self.ctx)


class 몬스터추가스폰01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105,106,107,108,109])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[105,106,107,108,109]):
            return 조건확인_대기01(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 조건확인_대기01(self.ctx)


class 몬스터추가스폰105(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[105]):
            return 몬스터추가스폰106(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 조건확인_대기01(self.ctx)


class 몬스터추가스폰106(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[106])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[106]):
            return 몬스터추가스폰107(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 조건확인_대기01(self.ctx)


class 몬스터추가스폰107(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[107])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[107]):
            return 몬스터추가스폰108(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 조건확인_대기01(self.ctx)


class 몬스터추가스폰108(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[108])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[108]):
            return 몬스터추가스폰109(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 조건확인_대기01(self.ctx)


class 몬스터추가스폰109(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[109])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[109]):
            return 조건확인_대기01(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 조건확인_대기01(self.ctx)


class 세리하첫등장연출_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.destroy_monster(spawn_ids=[101,102,105,106,107,108,109,110,112,121,122,131,132,133])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세리하첫등장연출_준비(self.ctx)


class 세리하첫등장연출_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52020004, portal_id=10) # 유저 첫 위치 잡기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세리하첫등장연출_시작(self.ctx)


class 세리하첫등장연출_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8015], return_view=False)
        self.set_scene_skip(state=세리하첫등장연출_스킵완료, action='nextState') # setsceneskip 3 set
        # setsceneskip 3 set
        # setsceneskip 3 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 탐색실패01(self.ctx)


class 탐색실패01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8015], return_view=False)
        self.add_balloon_talk(msg='흐음….', duration=2000)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 탐색실패02(self.ctx)


class 탐색실패02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003541, illust_id='Jaiden_normal', msg='단서가 될 만한 게 없는 건지, 있는데도 모르겠는 건지.\\n답답하네, 좀.', duration=3000)
        self.move_user_path(patrol_name='PC_walkinCenter')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 흑성회등장01(self.ctx)


class 흑성회등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[121,122], auto_target=False)
        self.add_cinematic_talk(npc_id=11003659, illust_id='WeiHong_normal', msg='그럼, 답답한 사람들끼리 이야기를 좀 해보면 어떨까?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 흑성회등장02(self.ctx)


class 흑성회등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8020], return_view=False)
        self.move_npc(spawn_id=121, patrol_name='Weihong_walkin01')
        self.add_cinematic_talk(npc_id=11003659, illust_id='WeiHong_normal', msg='알고 있는 것을 나누면, 목표에 보다 빨리 다가갈 수 있을 테니.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 흑성회등장03(self.ctx)


class 흑성회등장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8021], return_view=False)
        self.move_npc(spawn_id=122, patrol_name='Seriha_walkin01')
        self.add_cinematic_talk(npc_id=11003659, illust_id='WeiHong_normal', msg='크리티아스의 왕족.\\n너희가 찾고 있는 건 바로 그들의 행적 아닌가.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 흑성회등장04(self.ctx)


class 흑성회등장04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003659, illust_id='WeiHong_normal', msg='아마 이곳에 들어온 모두가 그들을 찾고 있을 거야.\\n흑성회도 마찬가지다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 흑성회등장05(self.ctx)


class 흑성회등장05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8022], return_view=False)
        self.add_cinematic_talk(npc_id=11003659, illust_id='WeiHong_normal', msg='과연 누가 가장 먼저 목적을 이루게 될까… 궁금하지 않나?\\n물론, 나는 정답을 알 것 같지만.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC독백01(self.ctx)


class PC독백01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[131,132,133], auto_target=False)
        self.select_camera_path(path_ids=[8015], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='(흑성회라니… 일이 생각보다 복잡하게 돌아가는 것 같다.)', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 레지스탕스등장01(self.ctx)


class 레지스탕스등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8030], return_view=False)
        self.add_cinematic_talk(npc_id=11003663, msg='생각하고 계시는 그 답이 정답이 맞을까요, 영감님?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 레지스탕스등장02(self.ctx)


class 레지스탕스등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003661, msg='틀렸을 것 같은데?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 레지스탕스등장03(self.ctx)


class 레지스탕스등장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003662, msg='우리도 여기까지 힘들게 왔는데, 빈 손으로 갈 수는 없잖아요.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 레지스탕스등장04(self.ctx)


class 레지스탕스등장04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003662, msg='우리 등장이 좀 밋밋했죠?\\n멋있게 등장하도록 연출 보강 예정이니 참고해 주세요.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하등장01(self.ctx)


class 세리하등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8022], return_view=False)
        self.add_cinematic_talk(npc_id=11003659, illust_id='WeiHong_normal', msg='불청객이 많아서 그런가, 좀 시끄럽군.\\n나는 시끄러운 건 영 체질에 안 맞는단 말이야.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하등장02(self.ctx)


class 세리하등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003659, illust_id='WeiHong_normal', msg='$npc:11003660$, 정리해라.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하등장03(self.ctx)


class 세리하등장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=122, patrol_name='Seriha_walkinto')
        self.show_caption(type='NameCaption', title='$npc:11003660$', desc='흑성회 특수부대장, $npc:11003659$의 측근', align=Align.Center | Align.Left, offset_rate_x=0.5, offset_rate_y=0.15, duration=5000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하등장04(self.ctx)


class 세리하등장04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8023], return_view=False)
        self.add_cinematic_talk(npc_id=11003660, illust_id='Seriha_normal', msg='네, 보스.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 제이든경고01(self.ctx)


class 제이든경고01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8015], return_view=False)
        self.move_npc(spawn_id=111, patrol_name='Jaiden_whispertoPC')
        self.add_cinematic_talk(npc_id=11003541, illust_id='Jaiden_normal', msg='도망가자.', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 제이든경고02(self.ctx)


class 제이든경고02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='갑자기 그게 무슨 소리…', duration=2000)
        self.add_cinematic_talk(npc_id=11003541, illust_id='Jaiden_normal', msg='$npcName:11003660$$pp:가,이$ 나선 이상, 이제 여긴 불지옥이 될거야.\\n시간 없어. 빨리.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC제이든과도망(self.ctx)


class PC제이든과도망(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.add_balloon_talk(spawn_id=111, msg='저쪽으로. 서둘러…!', duration=2000)
        self.move_npc(spawn_id=111, patrol_name='Jaiden_run')
        self.move_user_path(patrol_name='PC_run')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세리하공격준비(self.ctx)


class 세리하공격준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8023], return_view=False)
        self.add_cinematic_talk(npc_id=11003660, illust_id='Seriha_normal', msg='입만 산 것들. 깨끗하게 정리해 주마.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 자막구간_준비(self.ctx)


# 설명문 출력
class 자막구간_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 자막구간_01(self.ctx)


class 자막구간_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='제이든과 함께 그곳을 빠져나오던 순간\\n들려왔던 어마어마한 소리.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 자막구간_02(self.ctx)


class 자막구간_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='왕족의 비상상황을 대비해 견고하게 지어졌을 지하실 내부는\\n순식간에 굉음을 내며 무너져 내렸다.')
        # Missing State: ShowCaption03Skip
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 자막구간_03(self.ctx)


class 자막구간_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='나는 달려야 했다.\\n오직 살아남는 것만을 생각하면서.')
        # Missing State: State,  setsceneskip 3 close
        self.set_scene_skip()
        # setsceneskip 3 close
        # setsceneskip 3 close
        # setsceneskip 3 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 세리하첫등장연출_종료(self.ctx)


class 세리하첫등장연출_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세리하첫등장연출_종료(self.ctx)


class 세리하첫등장연출_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_achievement(trigger_id=9000, type='trigger', achieve='BlackStarVSResistance')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 최종맵이동(self.ctx)


class 최종맵이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020005, portal_id=10) # 버려진 트럭으로 자동 이동
        self.visible_my_pc(is_visible=False) # PC안보이게
        self.visible_my_pc(is_visible=True) # PC보이게
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return 최종맵이동(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
