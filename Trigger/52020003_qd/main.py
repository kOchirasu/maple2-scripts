""" trigger/52020003_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,111,112,113,121,122,123,124,125,126])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001760], quest_states=[3]):
            return 기본(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001760], quest_states=[2]):
            return 제이든등장_완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001760], quest_states=[1]):
            return 제이든등장_완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001759], quest_states=[3]):
            return 제이든등장_완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001759], quest_states=[2]):
            return 제이든등장_완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001759], quest_states=[1]):
            return 흑성회전투_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001758], quest_states=[3]):
            return 기본(self.ctx)


class 기본(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 흑성회전투_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52020003, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC등장_준비(self.ctx)


class PC등장_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC등장(self.ctx)


class PC등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_PC_Walkin_01')
        self.add_balloon_talk(msg='꽤 넓네, 생각보다…', duration=2000)
        self.set_scene_skip(state=전투직전_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip set
        # setsceneskip set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 누군가있다(self.ctx)


class 누군가있다(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_PC_Walkin_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 누군가있다_발견(self.ctx)


class 누군가있다_발견(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.add_balloon_talk(msg='잠깐… 누가 있나?', duration=3000)
        self.move_user_path(patrol_name='MS2PatrolData_PC_Walkin_03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 요원등장_준비(self.ctx)


class 요원등장_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.spawn_monster(spawn_ids=[113], auto_target=False)
        self.add_balloon_talk(spawn_id=113, msg='하하하!', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 요원등장(self.ctx)


class 요원등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003666, msg='아주 멍청하지는 않구나.\\n내 존재를 눈치채다니.', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC반응01(self.ctx)


class PC반응01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='흑성회…? 여기서 뭘 하는 거지?', duration=3000, align=Align.Left)
        self.set_pc_emotion_loop(sequence_name='Talk_B', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 요원협박(self.ctx)


class 요원협박(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.add_cinematic_talk(npc_id=11003666, msg='그건 알 필요 없고, 서로 바쁜데 시간 끌지 말자고~\\n찾아낸 물건이 있으면 순순히 넘겨라.', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC반응02(self.ctx)


class PC반응02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='그런 건 없고… 오히려 듣고 싶은 이야기가 많은데.\\n여기서 뭘 하고 있었던 건지 말해 보라고.', duration=3000, align=Align.Left)
        self.set_pc_emotion_loop(sequence_name='Emotion_Cinematic_ShakeHead_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 요원반응(self.ctx)


class 요원반응(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.add_cinematic_talk(npc_id=11003666, msg='그럴 시간 없어. 우린 아주 바쁘거든.\\n얘들아! 제압하자!', duration=3000, align=Align.Left)
        self.spawn_monster(spawn_ids=[111,112], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 요원소환01(self.ctx)


class 요원소환01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.move_npc(spawn_id=111, patrol_name='111_blackstars_patrol_00')
        self.add_balloon_talk(spawn_id=111, msg='각오해라!', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 요원소환02(self.ctx)


class 요원소환02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8011], return_view=False)
        self.move_npc(spawn_id=112, patrol_name='112_blackstars_patrol_01')
        self.add_balloon_talk(spawn_id=112, msg='혼내주마!', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 전투대기00(self.ctx)


class 전투대기00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[111,112,113])
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전투직전_스킵완료(self.ctx)


class 전투직전_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[111,112,113])
        self.move_user(map_id=52020003, portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투시작01(self.ctx)


class 전투시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.spawn_monster(spawn_ids=[121,122])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[121,122]):
            return 전투시작02(self.ctx)


class 전투시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[123,124])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[123,124]):
            return 전투시작03(self.ctx)


class 전투시작03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[125,126])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[125,126]):
            return 전투끝(self.ctx)


class 전투끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52020003, portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 제이든_등장_대기(self.ctx)


class 제이든_등장_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111,112,113,121,122,123,124,125,126])
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 제이든대기(self.ctx)


class 제이든대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8040], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003539, msg='…$MyPCName$?', duration=3000, align=Align.Left)
        self.set_scene_skip(state=제이든등장_스킵완료, action='exit') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 제이든대사01(self.ctx)


class 제이든대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003541, msg='아주 시끄러운 소리가 난 것 같은데…', duration=2000, align=Align.Left)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_PC_Walkin_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 제이든대사02(self.ctx)


class 제이든대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8021,8022], return_view=False)
        self.add_cinematic_talk(npc_id=11003541, msg='무슨 일 있었어?', duration=3000, align=Align.Left)
        self.move_npc(spawn_id=101, patrol_name='101_MS2PatrolData_Jaiden_Walkin')
        # Missing State: State,  setsceneskip 2 close
        self.set_scene_skip()
        # setsceneskip 2 close
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 제이든등장_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9000, type='trigger', achieve='BlackStarAttack01')
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 제이든등장_완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,111,112,113,121,122,123,124,125,126])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
