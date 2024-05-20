""" trigger/52010056_qd/eventsection.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[9005], visible=True)
        self.set_mesh_animation(trigger_ids=[9005], visible=True)
        self.set_mesh(trigger_ids=[9006])
        self.set_mesh_animation(trigger_ids=[9006])
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005]) # 포탈 생성
        self.set_effect(trigger_ids=[5006]) # 포탈 생성
        self.set_effect(trigger_ids=[5007]) # 포탈 생성
        self.set_effect(trigger_ids=[5008]) # 포탈 사운드
        self.set_effect(trigger_ids=[5009]) # 포탈 사운드
        self.set_effect(trigger_ids=[5010]) # 포탈 사운드
        self.set_effect(trigger_ids=[5011]) # 몸체 이펙트
        self.set_effect(trigger_ids=[5012]) # 몸체 이펙트
        self.set_effect(trigger_ids=[5013]) # 포탈 사운드
        self.set_effect(trigger_ids=[5014]) # 트리스탄 바닥이펙트
        self.set_effect(trigger_ids=[5101])
        self.set_effect(trigger_ids=[5102])
        self.set_effect(trigger_ids=[5103])
        self.set_effect(trigger_ids=[5104])
        self.set_effect(trigger_ids=[5105])
        self.set_effect(trigger_ids=[5106])
        self.set_effect(trigger_ids=[5107])
        self.set_effect(trigger_ids=[5108])
        self.set_effect(trigger_ids=[5109])
        self.set_effect(trigger_ids=[5110])
        self.set_effect(trigger_ids=[5111])
        self.set_effect(trigger_ids=[5112])
        self.set_effect(trigger_ids=[5113])
        self.set_effect(trigger_ids=[5114])
        self.set_effect(trigger_ids=[5115])
        self.set_effect(trigger_ids=[5116])
        self.set_effect(trigger_ids=[5117])
        self.set_effect(trigger_ids=[5118])
        self.set_effect(trigger_ids=[5201])
        self.set_effect(trigger_ids=[5202])
        self.set_effect(trigger_ids=[5203])
        self.set_effect(trigger_ids=[5204])
        self.set_effect(trigger_ids=[5205])
        self.set_effect(trigger_ids=[5206])
        self.set_effect(trigger_ids=[5207])
        self.set_effect(trigger_ids=[5208])
        self.set_effect(trigger_ids=[5209])
        self.set_effect(trigger_ids=[5210])
        self.set_effect(trigger_ids=[5211])
        self.set_effect(trigger_ids=[5212])
        self.set_effect(trigger_ids=[5213])
        self.set_effect(trigger_ids=[5214])
        self.set_effect(trigger_ids=[5215])
        self.set_effect(trigger_ids=[5216])
        self.set_effect(trigger_ids=[5218])
        self.set_effect(trigger_ids=[5218])
        self.set_effect(trigger_ids=[5301])
        self.set_effect(trigger_ids=[5302])
        self.set_effect(trigger_ids=[5303])
        self.set_effect(trigger_ids=[5304])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml') # 페이드 아웃 끔

    def on_tick(self) -> trigger_api.Trigger:
        return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False) # 유저 투명화
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.spawn_monster(spawn_ids=[111], auto_target=False) # 보초1
        self.spawn_monster(spawn_ids=[112], auto_target=False) # 보초2
        self.spawn_monster(spawn_ids=[121], auto_target=False) # 크림슨 발록: 11003817
        self.spawn_monster(spawn_ids=[122], auto_target=False) # 크림슨 스피어 참모: 11003816
        self.spawn_monster(spawn_ids=[123], auto_target=False) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[124], auto_target=False) # 크림슨 스피어2: 11003816
        self.spawn_monster(spawn_ids=[125], auto_target=False) # 크림슨 스피어3: 11003816
        self.spawn_monster(spawn_ids=[126], auto_target=False) # 크림슨 스피어4: 11003816
        self.spawn_monster(spawn_ids=[191], auto_target=False) # 인페르녹의 혼
        self.move_user(map_id=52010056, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        return 인트로_준비(self.ctx)


class 인트로_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52010056_QD__EventSection__52$')
        self.select_camera_path(path_ids=[4001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000054], quest_states=[2]):
            return 연출종료(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000054], quest_states=[1]):
            return 의외의효능_화면끔(self.ctx)
        if self.wait_tick(wait_tick=4000):
            return 인트로_지역소개(self.ctx)


class 인트로_지역소개(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.show_caption(type='VerticalCaption', title='$52010056_QD__EventSection__54$', desc='$52010056_QD__EventSection__0$', align=Align.Bottom | Align.Left, duration=3500, scale=1.0)
        self.set_scene_skip(state=시작연출_준비, action='nextState') # 크림슨 발록 연출 스킵
        # 트리스탄 등장 연출로 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 크림슨스피어_대사_A(self.ctx)


class 크림슨스피어_대사_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=126, patrol_name='MS2PatrolData_3001')
        self.add_cinematic_talk(npc_id=11003816, msg='$52010056_QD__EventSection__1$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록_대사_A(self.ctx)


class 크림슨발록_대사_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=121, sequence_name='Stun_A')
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__2$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록_대사_B(self.ctx)


class 크림슨발록_대사_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__3$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록_대사_C(self.ctx)


class 크림슨발록_대사_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__4$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록_대사_D(self.ctx)


class 크림슨발록_대사_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__5$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록_대사_E(self.ctx)


class 크림슨발록_대사_E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__6$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록_대사_F(self.ctx)


class 크림슨발록_대사_F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__7$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 크림슨스피어_대사_B(self.ctx)

    def on_exit(self) -> None:
        self.set_npc_emotion_sequence(spawn_id=121, sequence_name='Attack_01_C')


class 크림슨스피어_대사_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=125, patrol_name='MS2PatrolData_3002')
        self.move_npc(spawn_id=124, patrol_name='MS2PatrolData_3003')
        self.move_npc(spawn_id=123, patrol_name='MS2PatrolData_3004')
        self.add_balloon_talk(spawn_id=123, msg='$52010056_QD__EventSection__8$', duration=2800)
        self.add_balloon_talk(spawn_id=124, msg='$52010056_QD__EventSection__8$', duration=2800)
        self.add_balloon_talk(spawn_id=125, msg='$52010056_QD__EventSection__8$', duration=2800)
        self.add_balloon_talk(spawn_id=126, msg='$52010056_QD__EventSection__8$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인트로_종료(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬


class 인트로_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        # Missing State: State,  스킵 기능 끊어주기
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 시작연출_준비(self.ctx)


class 시작연출_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52010056_QD__EventSection__53$')
        self.select_camera_path(path_ids=[4002], return_view=False)
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 트리스탄: 11003812

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 시작연출_지역소개(self.ctx)


class 시작연출_지역소개(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.show_caption(type='VerticalCaption', title='$52010056_QD__EventSection__12$', align=Align.Bottom | Align.Left, duration=3500, scale=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 트리스탄_침입(self.ctx)


class 트리스탄_침입(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_3005')
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_3006')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3007')
        self.add_balloon_talk(spawn_id=111, msg='$52010056_QD__EventSection__13$', duration=2800)
        self.add_balloon_talk(spawn_id=112, msg='$52010056_QD__EventSection__14$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트리스탄_공격(self.ctx)


class 트리스탄_공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_effect(trigger_ids=[5003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2100):
            return 트리스탄_마무리(self.ctx)


class 트리스탄_마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.set_effect(trigger_ids=[5004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보초_쓰러짐(self.ctx)


class 보초_쓰러짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Dead_B', duration=1000000000.0)
        self.set_npc_emotion_loop(spawn_id=112, sequence_name='Dead_B', duration=1000000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄_대사A(self.ctx)


class 트리스탄_대사A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__15$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄_대사B(self.ctx)


class 트리스탄_대사B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__16$', duration=2800, illust_id='Tristan_normal', align=Align.Center)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 조작_준비(self.ctx)


class 조작_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101]) # 트리스탄
        self.destroy_monster(spawn_ids=[111]) # 보초1
        self.destroy_monster(spawn_ids=[112]) # 보초2
        self.destroy_monster(spawn_ids=[121]) # 크림슨 발록: 11003817
        self.destroy_monster(spawn_ids=[122]) # 크림슨 참모: 11003816
        self.destroy_monster(spawn_ids=[123]) # 크림슨 스피어1: 11003816
        self.destroy_monster(spawn_ids=[124]) # 크림슨 스피어2: 11003816
        self.destroy_monster(spawn_ids=[125]) # 크림슨 스피어3: 11003816
        self.destroy_monster(spawn_ids=[126]) # 크림슨 스피어4: 11003816
        self.reset_camera(interpolation_time=1.0)
        self.visible_my_pc(is_visible=True) # 유저 투명 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 조작_시작(self.ctx)


class 조작_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.set_event_ui(type=1, arg2='$52010056_QD__EventSection__17$', arg3='3000', arg4='0')
        self.set_quest_accept(quest_id=91000053)
        self.set_visible_ui(ui_names=['UpperHudDialog','MessengerBrowser','ExpBar','GroupMessengerBrowser','QuestGuideDialog','MinimapDialog','AdPushDialog','SnowmanEventDialog'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2010], quest_ids=[91000054], quest_states=[2]):
            return 의외의효능_화면끔(self.ctx)
        if self.quest_user_detected(box_ids=[2010], quest_ids=[91000054], quest_states=[1]):
            return 의외의효능_화면끔(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_sound(trigger_id=7001)


# 여기서부터 각성 연출
class 의외의효능_화면끔(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 의외의효능_준비(self.ctx)

    def on_exit(self) -> None:
        self.visible_my_pc(is_visible=False) # 유저 투명화
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 트리스탄: 11003812
        self.destroy_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[112])
        self.destroy_monster(spawn_ids=[121])
        self.destroy_monster(spawn_ids=[122])
        self.destroy_monster(spawn_ids=[123])
        self.destroy_monster(spawn_ids=[124])
        self.destroy_monster(spawn_ids=[125])
        self.destroy_monster(spawn_ids=[126])


class 의외의효능_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=2001, skill_id=99910300)
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.move_user(map_id=52010056, portal_id=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 의외의효능_연출A(self.ctx)


class 의외의효능_연출A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__18$', duration=4569)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4569):
            return 의외의효능_연출B(self.ctx)


class 의외의효능_연출B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5005], visible=True)
        self.set_effect(trigger_ids=[5008], visible=True)
        self.spawn_monster(spawn_ids=[801], auto_target=False) # 크림슨 스피어1: 11003816
        self.select_camera_path(path_ids=[4009,4010], return_view=False)
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__19$', duration=2800)
        self.set_scene_skip(state=각성_전투준비, action='nextState') # 트리스탄 각성 전투로 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5008])
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__20$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크림슨군단생성(self.ctx)


class 크림슨군단생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5006], visible=True)
        self.set_effect(trigger_ids=[5007], visible=True)
        self.set_effect(trigger_ids=[5009], visible=True)
        self.set_effect(trigger_ids=[5010], visible=True)
        self.set_effect(trigger_ids=[5012], visible=True)
        self.set_effect(trigger_ids=[5013], visible=True)
        self.spawn_monster(spawn_ids=[802], auto_target=False) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[803], auto_target=False) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[804], auto_target=False) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[805], auto_target=False) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[806], auto_target=False) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[807], auto_target=False) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 크림슨군단진영(self.ctx)


class 크림슨군단진영(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5006])
        self.set_effect(trigger_ids=[5007])
        self.set_effect(trigger_ids=[5009])
        self.set_effect(trigger_ids=[5010])
        self.set_effect(trigger_ids=[5012])
        self.set_effect(trigger_ids=[5013])
        self.set_npc_emotion_sequence(spawn_id=801, sequence_name='Stun_A')
        self.move_npc(spawn_id=802, patrol_name='MS2PatrolData_3009')
        self.move_npc(spawn_id=803, patrol_name='MS2PatrolData_3010')
        self.move_npc(spawn_id=804, patrol_name='MS2PatrolData_3011')
        self.move_npc(spawn_id=805, patrol_name='MS2PatrolData_3012')
        self.move_npc(spawn_id=806, patrol_name='MS2PatrolData_3013')
        self.move_npc(spawn_id=807, patrol_name='MS2PatrolData_3014')
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__21$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 크림슨발록분노(self.ctx)


class 크림슨발록분노(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=801, sequence_name='Attack_01_B')
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__22$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄대사_A(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬


class 트리스탄대사_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__23$', duration=2800, illust_id='Tristan_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄대사_B(self.ctx)


class 트리스탄대사_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__24$', duration=2800, illust_id='Tristan_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록대사_A(self.ctx)


class 크림슨발록대사_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011], return_view=False)
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__25$', duration=2800, illust_id='balrog_normal', align=Align.Center)
        self.set_effect(trigger_ids=[5011], visible=True) # 몸체 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_A(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔


class 인페르녹의혼_흡수연출_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Attack_02_B', duration=1000000000.0)
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__26$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_B(self.ctx)


class 인페르녹의혼_흡수연출_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4012], return_view=False)
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__27$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_C(self.ctx)


class 인페르녹의혼_흡수연출_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5012], visible=True) # 몸체 이펙트
        self.set_effect(trigger_ids=[5013], visible=True) # 펑
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__28$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 인페르녹의혼_흡수연출_D(self.ctx)


class 인페르녹의혼_흡수연출_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 인페르녹의혼_흡수연출_E(self.ctx)


class 인페르녹의혼_흡수연출_E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003821, msg='$52010056_QD__EventSection__29$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_F(self.ctx)


class 인페르녹의혼_흡수연출_F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__30$', duration=2800, illust_id='Tristan_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_G(self.ctx)


class 인페르녹의혼_흡수연출_G(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003821, msg='$52010056_QD__EventSection__31$', duration=2800, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_H(self.ctx)


class 인페르녹의혼_흡수연출_H(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003821, msg='$52010056_QD__EventSection__32$', duration=2800, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_I(self.ctx)


class 인페르녹의혼_흡수연출_I(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__33$', duration=2800, illust_id='Tristan_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_J(self.ctx)


class 인페르녹의혼_흡수연출_J(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003821, msg='$52010056_QD__EventSection__34$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_K(self.ctx)


class 인페르녹의혼_흡수연출_K(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__35$', duration=2800, illust_id='Tristan_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_L(self.ctx)


class 인페르녹의혼_흡수연출_L(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003821, msg='$52010056_QD__EventSection__36$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_M(self.ctx)


class 인페르녹의혼_흡수연출_M(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003821, msg='$52010056_QD__EventSection__37$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹의혼_흡수연출_N(self.ctx)


class 인페르녹의혼_흡수연출_N(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.add_cinematic_talk(npc_id=11003821, msg='$52010056_QD__EventSection__38$', duration=2800)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 각성_전투준비(self.ctx)


class 각성_전투준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_mesh(trigger_ids=[9005])
        self.set_mesh_animation(trigger_ids=[9005])
        self.set_mesh(trigger_ids=[9006], visible=True)
        self.set_mesh_animation(trigger_ids=[9006], visible=True)
        self.destroy_monster(spawn_ids=[102]) # 트리스탄
        self.destroy_monster(spawn_ids=[802])
        self.destroy_monster(spawn_ids=[803])
        self.destroy_monster(spawn_ids=[804])
        self.destroy_monster(spawn_ids=[805])
        self.destroy_monster(spawn_ids=[806])
        self.destroy_monster(spawn_ids=[807])
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5006])
        self.set_effect(trigger_ids=[5007])
        self.set_effect(trigger_ids=[5008])
        self.set_effect(trigger_ids=[5009])
        self.set_effect(trigger_ids=[5010])
        self.set_effect(trigger_ids=[5009])
        self.set_effect(trigger_ids=[5010])
        self.set_effect(trigger_ids=[5011])
        self.set_effect(trigger_ids=[5012])
        self.set_effect(trigger_ids=[5013])
        self.visible_my_pc(is_visible=True) # 유저 투명 해제
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 각성_전투시작(self.ctx)


class 각성_전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__39$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 조작제어_해제(self.ctx)


class 조작제어_해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크림슨발록군단생성_A(self.ctx)


class 크림슨발록군단생성_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[701]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[702]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[703]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[704]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[705]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[706]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[707]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[708]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[709]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[710]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[711]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[712]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[713]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[714]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[715]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[716]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[717]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[718]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[719]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[720]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[721]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[722]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[723]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[724]) # 크림슨 스피어1: 11003816
        self.set_event_ui(type=1, arg2='$52010056_QD__EventSection__40$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록군단생성_B(self.ctx)


class 크림슨발록군단생성_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[701]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[702]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[703]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[704]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[705]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[706]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[707]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[708]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[709]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[710]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[711]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[712]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[713]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[714]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[715]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[716]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[717]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[718]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[719]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[720]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[721]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[722]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[723]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[724]) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록군단생성_C(self.ctx)


class 크림슨발록군단생성_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[701]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[702]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[703]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[704]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[705]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[706]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[707]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[708]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[709]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[710]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[711]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[712]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[713]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[714]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[715]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[716]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[717]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[718]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[719]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[720]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[721]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[722]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[723]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[724]) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크림슨발록군단생성_D(self.ctx)


class 크림슨발록군단생성_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[701]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[702]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[703]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[704]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[705]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[706]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[707]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[708]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[709]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[710]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[711]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[712]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[713]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[714]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[715]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[716]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[717]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[718]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[719]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[720]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[721]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[722]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[723]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[724]) # 크림슨 스피어1: 11003816
        self.set_event_ui(type=1, arg2='$52010056_QD__EventSection__41$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크림슨발록군단생성_E(self.ctx)


class 크림슨발록군단생성_E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[701]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[702]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[703]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[704]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[705]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[706]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[707]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[708]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[709]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[710]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[711]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[712]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[713]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[714]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[715]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[716]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[717]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[718]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[719]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[720]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[721]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[722]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[723]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[724]) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크림슨발록군단생성_F(self.ctx)


class 크림슨발록군단생성_F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[701]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[702]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[703]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[704]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[705]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[706]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[707]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[708]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[709]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[710]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[711]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[712]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[713]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[714]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[715]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[716]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[717]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[718]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[719]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[720]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[721]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[722]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[723]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[724]) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724]):
            return 필살기연출_암전(self.ctx)


class 필살기연출_암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False) # 유저 투명
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 켬
        self.move_user(map_id=52010056, portal_id=6003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 필살기연출_준비A(self.ctx)


class 필살기연출_준비A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[701])
        self.destroy_monster(spawn_ids=[702])
        self.destroy_monster(spawn_ids=[703])
        self.destroy_monster(spawn_ids=[704])
        self.destroy_monster(spawn_ids=[705])
        self.destroy_monster(spawn_ids=[706])
        self.destroy_monster(spawn_ids=[707])
        self.destroy_monster(spawn_ids=[708])
        self.destroy_monster(spawn_ids=[709])
        self.destroy_monster(spawn_ids=[710])
        self.destroy_monster(spawn_ids=[711])
        self.destroy_monster(spawn_ids=[712])
        self.destroy_monster(spawn_ids=[713])
        self.destroy_monster(spawn_ids=[714])
        self.destroy_monster(spawn_ids=[715])
        self.destroy_monster(spawn_ids=[716])
        self.destroy_monster(spawn_ids=[717])
        self.destroy_monster(spawn_ids=[718])
        self.destroy_monster(spawn_ids=[719])
        self.destroy_monster(spawn_ids=[720])
        self.destroy_monster(spawn_ids=[721])
        self.destroy_monster(spawn_ids=[722])
        self.destroy_monster(spawn_ids=[723])
        self.destroy_monster(spawn_ids=[724])
        self.spawn_monster(spawn_ids=[103]) # 트리스탄
        self.spawn_monster(spawn_ids=[808]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[809]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[810]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[811]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[812]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[813]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[814]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[815]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[816]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[817]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[818]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[819]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[820]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[821]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[822]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[823]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[824]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[825]) # 크림슨 스피어1: 11003816
        self.spawn_monster(spawn_ids=[826]) # 크림슨 스피어1: 11003816

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 필살기연출_준비B(self.ctx)


class 필살기연출_준비B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=808, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=809, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=810, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=811, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=812, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=813, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=814, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=815, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=816, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=817, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=818, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=819, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=820, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=821, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=822, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=823, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=824, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=825, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=826, sequence_name='Attack_Idle_A', duration=9999999.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 카메라_온A(self.ctx)


class 카메라_온A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml') # 페이드 아웃 끔
        self.select_camera_path(path_ids=[4014], return_view=False)
        self.set_scene_skip(state=트리거업적, action='nextState') # 크림슨 발록 연출 스킵
        # 트리스탄 등장 연출로 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 카메라_온B(self.ctx)


class 카메라_온B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4015], return_view=False)
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__42$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 카메라_온C(self.ctx)


class 카메라_온C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4016], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 카메라_리셋(self.ctx)


class 카메라_리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 크림슨발록_대사_G(self.ctx)


class 크림슨발록_대사_G(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=801, sequence_name='Attack_01_B')
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__43$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄_대사_H(self.ctx)


class 트리스탄_대사_H(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__44$', duration=2800, illust_id='Tristan_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록_대사_I(self.ctx)


class 크림슨발록_대사_I(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__45$', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄_대사D(self.ctx)


class 트리스탄_대사D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__46$', duration=2800, illust_id='Tristan_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄_대사E(self.ctx)


class 트리스탄_대사E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__47$', duration=2800, illust_id='Tristan_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 필살기연출_모션A(self.ctx)


class 필살기연출_모션A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Attack_02_B', duration=9999999.0)
        self.set_effect(trigger_ids=[5014], visible=True) # 트리스탄 바닥이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 필살기연출_모션B(self.ctx)


class 필살기연출_모션B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Attack_01_B', duration=9999999.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 크림슨발록_대사_J(self.ctx)


class 크림슨발록_대사_J(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__48$', duration=1800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1800):
            return 크림슨발록_대사_K(self.ctx)


class 크림슨발록_대사_K(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # 트리스탄 바닥이펙트
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__55$', duration=1800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_A(self.ctx)


class 바닥이펙트_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=808, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5102], visible=True)
        self.set_effect(trigger_ids=[5202], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_B(self.ctx)


class 바닥이펙트_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=809, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5103], visible=True)
        self.set_effect(trigger_ids=[5203], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_C(self.ctx)


class 바닥이펙트_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=810, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5104], visible=True)
        self.set_effect(trigger_ids=[5204], visible=True)
        self.set_effect(trigger_ids=[5302], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_D(self.ctx)


class 바닥이펙트_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=811, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5105], visible=True)
        self.set_effect(trigger_ids=[5205], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_E(self.ctx)


class 바닥이펙트_E(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=812, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5106], visible=True)
        self.set_effect(trigger_ids=[5206], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_F(self.ctx)


class 바닥이펙트_F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=813, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5107], visible=True)
        self.set_effect(trigger_ids=[5207], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_G(self.ctx)


class 바닥이펙트_G(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=814, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5108], visible=True)
        self.set_effect(trigger_ids=[5208], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_H(self.ctx)


class 바닥이펙트_H(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=815, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5109], visible=True)
        self.set_effect(trigger_ids=[5209], visible=True)
        self.set_effect(trigger_ids=[5303], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_I(self.ctx)


class 바닥이펙트_I(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=816, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5110], visible=True)
        self.set_effect(trigger_ids=[5210], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_J(self.ctx)


class 바닥이펙트_J(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=817, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5111], visible=True)
        self.set_effect(trigger_ids=[5211], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_K(self.ctx)


class 바닥이펙트_K(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=818, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5112], visible=True)
        self.set_effect(trigger_ids=[5212], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_L(self.ctx)


class 바닥이펙트_L(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=819, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5113], visible=True)
        self.set_effect(trigger_ids=[5213], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_M(self.ctx)


class 바닥이펙트_M(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=820, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5114], visible=True)
        self.set_effect(trigger_ids=[5214], visible=True)
        self.set_effect(trigger_ids=[5304], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_N(self.ctx)


class 바닥이펙트_N(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=821, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5115], visible=True)
        self.set_effect(trigger_ids=[5215], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_O(self.ctx)


class 바닥이펙트_O(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=822, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5116], visible=True)
        self.set_effect(trigger_ids=[5216], visible=True)
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml') # 페이드 아웃 켬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_P(self.ctx)


class 바닥이펙트_P(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=823, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5117], visible=True)
        self.set_effect(trigger_ids=[5217], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_Q(self.ctx)


class 바닥이펙트_Q(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=824, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5118], visible=True)
        self.set_effect(trigger_ids=[5218], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 바닥이펙트_R(self.ctx)


class 바닥이펙트_R(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=825, sequence_name='Damg_A', duration=9999999.0)
        self.set_effect(trigger_ids=[5202], visible=True)
        self.set_effect(trigger_ids=[5301], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨발록_대사_L(self.ctx)


class 크림슨발록_대사_L(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003817, msg='$52010056_QD__EventSection__50$', duration=2800, illust_id='balrog_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마지막연출_세팅(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[103])
        self.spawn_monster(spawn_ids=[104]) # 트리스탄


class 마지막연출_세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101])
        self.set_effect(trigger_ids=[5102])
        self.set_effect(trigger_ids=[5103])
        self.set_effect(trigger_ids=[5104])
        self.set_effect(trigger_ids=[5105])
        self.set_effect(trigger_ids=[5106])
        self.set_effect(trigger_ids=[5107])
        self.set_effect(trigger_ids=[5108])
        self.set_effect(trigger_ids=[5109])
        self.set_effect(trigger_ids=[5110])
        self.set_effect(trigger_ids=[5111])
        self.set_effect(trigger_ids=[5112])
        self.set_effect(trigger_ids=[5113])
        self.set_effect(trigger_ids=[5114])
        self.set_effect(trigger_ids=[5115])
        self.set_effect(trigger_ids=[5116])
        self.set_effect(trigger_ids=[5117])
        self.set_effect(trigger_ids=[5118])
        self.set_effect(trigger_ids=[5201])
        self.set_effect(trigger_ids=[5202])
        self.set_effect(trigger_ids=[5203])
        self.set_effect(trigger_ids=[5204])
        self.set_effect(trigger_ids=[5205])
        self.set_effect(trigger_ids=[5206])
        self.set_effect(trigger_ids=[5207])
        self.set_effect(trigger_ids=[5208])
        self.set_effect(trigger_ids=[5209])
        self.set_effect(trigger_ids=[5210])
        self.set_effect(trigger_ids=[5211])
        self.set_effect(trigger_ids=[5212])
        self.set_effect(trigger_ids=[5213])
        self.set_effect(trigger_ids=[5214])
        self.set_effect(trigger_ids=[5215])
        self.set_effect(trigger_ids=[5216])
        self.set_effect(trigger_ids=[5218])
        self.set_effect(trigger_ids=[5218])
        self.set_effect(trigger_ids=[5301])
        self.set_effect(trigger_ids=[5302])
        self.set_effect(trigger_ids=[5303])
        self.set_effect(trigger_ids=[5304])
        self.reset_camera()
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Attack_Idle_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=801, sequence_name='Dead_01_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=808, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=809, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=810, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=811, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=812, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=813, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=814, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=815, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=816, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=817, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=818, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=819, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=820, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=821, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=822, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=823, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=824, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=825, sequence_name='Dead_A', duration=9999999.0)
        self.set_npc_emotion_loop(spawn_id=826, sequence_name='Dead_A', duration=9999999.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마지막연출_온(self.ctx)


class 마지막연출_온(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml') # 페이드 아웃 켬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 트리스탄_대사F(self.ctx)


class 트리스탄_대사F(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003812, msg='$52010056_QD__EventSection__51$', duration=2800, illust_id='Tristan_normal', align=Align.Center)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리거업적(self.ctx)


class 트리거업적(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2009, type='trigger', achieve='tristanarousal')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010052, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000054], quest_states=[2]):
            return 연출종료(self.ctx)


initial_state = Idle
