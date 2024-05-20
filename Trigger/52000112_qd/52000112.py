""" trigger/52000112_qd/52000112.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class START(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5300]) # 재즈바 비밀통로 경로 안내
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 바텐더
        self.set_actor(trigger_id=231, visible=True, initial_sequence='Closed')
        self.set_effect(trigger_ids=[400])
        self.set_effect(trigger_ids=[401])
        self.set_effect(trigger_ids=[402])
        self.set_effect(trigger_ids=[403])
        self.set_effect(trigger_ids=[404])
        self.set_effect(trigger_ids=[405])
        self.set_effect(trigger_ids=[406])
        self.set_effect(trigger_ids=[407])
        self.set_mesh(trigger_ids=[300,301,302,303,304,305,306,307], visible=True, interval=1000, fade=1000.0) # 큐브하나씩부셔지는연출

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002306], quest_states=[2]):
            return 재즈바1층습격_완료가능01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002306], quest_states=[1]):
            return 재즈바1층습격_진행중01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002308], quest_states=[2]):
            return 재즈바_지하습격_완료가능01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002313], quest_states=[2]):
            return 쉐도우클로전투_완료연출01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002311], quest_states=[3]):
            return 재즈바_지하습격_완료가능01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002308], quest_states=[3]):
            return 재즈바_지하습격_완료가능01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002306], quest_states=[3]):
            return 재즈바1층습격_완료가능01(self.ctx)


# ########################씬1 재즈바_1층습격########################
class 재즈바1층습격_진행중01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[102,103,104,105,106,107], is_auto_targeting=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002306], quest_states=[2]):
            return 재즈바1층습격_완료가능01_b(self.ctx)


class 재즈바1층습격_완료가능01_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='$52000112_QD__52000112__0$', duration=6000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 재즈바1층습격_완료가능01(self.ctx)


class 재즈바1층습격_완료가능01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 재즈바1층습격_완료가능02(self.ctx)


class 재즈바1층습격_완료가능02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200], auto_target=False)
        self.destroy_monster(spawn_ids=[102,103,104,105,106,107])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 재즈바1층습격_완료가능03(self.ctx)


class 재즈바1층습격_완료가능03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_shadowClawMove') # 쉐도우클로 이동
        self.add_balloon_talk(spawn_id=111, msg='$52000112_QD__52000112__1$', duration=6000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002308], quest_states=[1]):
            return 재즈바_지하습격_진행중01(self.ctx)


# ########################씬2 재즈바_지하습격########################
class 재즈바_지하습격_진행중01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5300], visible=True) # 재즈바 비밀통로 경로 안내
        self.set_actor(trigger_id=231, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[200,209,204,205,210,206], auto_target=False) # 지하층 다크윈드 요원 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002308], quest_states=[2]):
            return 재즈바_지하습격_완료가능01_b(self.ctx)


class 재즈바_지하습격_완료가능01_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='$52000112_QD__52000112__2$', duration=6000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 재즈바_지하습격_완료가능01(self.ctx)


class 재즈바_지하습격_완료가능01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 재즈바_지하습격_완료가능02(self.ctx)


class 재즈바_지하습격_완료가능02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=20, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.spawn_monster(spawn_ids=[208], auto_target=False) # 쉐도우클로
        self.spawn_monster(spawn_ids=[201,202,203], auto_target=False) # 다크윈드 포로
        self.spawn_monster(spawn_ids=[211,212,213,214,215,216,217,218,219], auto_target=False) # 로그스 대원
        self.destroy_monster(spawn_ids=[108,109,110,111,200,209,204,205,210,206])
        self.move_user(map_id=52000112, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 재즈바_지하습격_완료가능03(self.ctx)


class 재즈바_지하습격_완료가능03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002311], quest_states=[3]):
            return PC_로그스거역_진행중01(self.ctx)


# ########################씬3 PC_로그스거역_대원들 전투준비########################
class PC_로그스거역_진행중01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=211, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=212, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=213, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=214, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=215, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=216, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=217, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=218, sequence_name='Attack_Idle_A', duration=15000.0)
        self.set_npc_emotion_loop(spawn_id=219, sequence_name='Attack_Idle_A', duration=15000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002312], quest_states=[3]):
            return PC_로그스거역_대원들01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002312], quest_states=[2]):
            return PC_로그스거역_대원들01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002312], quest_states=[1]):
            return PC_로그스거역_대원들01(self.ctx)


# ########################씬3 PC_로그스거역_대원들 전투########################
class PC_로그스거역_대원들01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[211,212,213,214,215,216,217,218,219]) # 로그스 대원 npc버전 삭제
        self.spawn_monster(spawn_ids=[220,221,222,223,224,225,226,227,228], auto_target=False) # 로그스 대원 몬스터 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002313], quest_states=[1]):
            return 쉐도우클로전투_진행중01(self.ctx)


# ########################씬4 쉐도우클로전투########################
class 쉐도우클로전투_진행중01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[211,212,213,214,215,216,217,218,219]) # 로그스 대원 npc버전 삭제
        self.destroy_monster(spawn_ids=[220,221,222,223,224,225,226,227,228]) # 로그스 대원 몬스터 삭제
        self.set_sound(trigger_id=9000, enable=True)
        self.destroy_monster(spawn_ids=[208])
        self.spawn_monster(spawn_ids=[229], auto_target=False) # 쉐도우클로

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002313], quest_states=[2]):
            return 쉐도우클로전투_완료연출01(self.ctx)


# ########################씬5 쉐도우클로전투_완료연출########################
class 쉐도우클로전투_완료연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=9000)
        self.visible_my_pc(is_visible=True) # 유저 투명 처리
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[207])
        self.spawn_monster(spawn_ids=[208], auto_target=False) # 쉐도우클로
        self.move_user(map_id=52000112, portal_id=3)
        self.set_npc_emotion_loop(spawn_id=208, sequence_name='Attack_Idle_A', duration=17500.0)
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Sit_Down_A', duration=17500.0)
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Sit_Down_A', duration=17500.0)
        self.set_npc_emotion_loop(spawn_id=203, sequence_name='Sit_Down_A', duration=17500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 쉐도우클로전투_완료연출02(self.ctx)


class 쉐도우클로전투_완료연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=쉐도우클로전투_완료연출09, action='exit')
        self.set_onetime_effect(id=30, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.select_camera_path(path_ids=[3000,3001], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Push_A', duration=5000.0)
        self.face_emotion(emotion_name='PC_Pain_86000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 쉐도우클로전투_완료연출03(self.ctx)


class 쉐도우클로전투_완료연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3002,3003], return_view=False)
        self.add_cinematic_talk(npc_id=11003185, illust_id='0', msg='$52000112_QD__52000112__3$', duration=5000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 쉐도우클로전투_완료연출04(self.ctx)


class 쉐도우클로전투_완료연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000112_QD__52000112__4$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 쉐도우클로전투_완료연출05(self.ctx)


class 쉐도우클로전투_완료연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.1, duration=5.5, interpolator=2) # 2초간 느려지기 시작
        self.select_camera_path(path_ids=[3004], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Assassin_DarkSight_A'])
        self.set_pc_emotion_loop(sequence_name='Assassin_DarkSight_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 쉐도우클로전투_완료연출06(self.ctx)


class 쉐도우클로전투_완료연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3005,3006], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Assassin_Enterance_A'])
        self.set_pc_emotion_loop(sequence_name='Assassin_Enterance_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 쉐도우클로전투_완료연출07_b(self.ctx)


class 쉐도우클로전투_완료연출07_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[400], visible=True)
        self.set_effect(trigger_ids=[401], visible=True)
        self.set_effect(trigger_ids=[402], visible=True)
        self.set_effect(trigger_ids=[403], visible=True)
        self.set_effect(trigger_ids=[404], visible=True)
        self.set_effect(trigger_ids=[405], visible=True)
        self.set_effect(trigger_ids=[406], visible=True)
        self.set_effect(trigger_ids=[407], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1700):
            return 쉐도우클로전투_완료연출07(self.ctx)


class 쉐도우클로전투_완료연출07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3007,3008], return_view=False)
        self.add_cinematic_talk(npc_id=11003185, illust_id='0', msg='$52000112_QD__52000112__5$', duration=4000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=208, sequence_name='Stun_A', duration=15500.0)
        self.set_mesh(trigger_ids=[300,301,302,303,304,305,306,307], interval=700) # 큐브하나씩부셔지는연출

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 쉐도우클로전투_완료연출08(self.ctx)


class 쉐도우클로전투_완료연출08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3009,3010], return_view=False)
        self.destroy_monster(spawn_ids=[201,202,203])
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.add_cinematic_talk(npc_id=11003185, illust_id='0', msg='$52000112_QD__52000112__6$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 쉐도우클로전투_완료연출08_1(self.ctx)


class 쉐도우클로전투_완료연출08_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 쉐도우클로전투_완료연출09(self.ctx)


class 쉐도우클로전투_완료연출09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000111, portal_id=11)


initial_state = START
