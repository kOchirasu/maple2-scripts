""" trigger/52000105_qd/52000105.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 텐

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002320], quest_states=[1]):
            # 몬스터 처치 훈련01
            return 몬스터처치훈련01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002321], quest_states=[1]):
            # 몬스터 처치 훈련01
            return 몬스터처치훈련02(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002322], quest_states=[1]):
            # 할아버지대련01
            return 할아버지대련01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002322], quest_states=[2]):
            # 대련 퀘스트를 받으면 할아버지 등장
            return 대련종료씬시작01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002322], quest_states=[3]):
            return 대련종료씬시작01(self.ctx)


# ########################씬2 몬스터 소환 교육01~02########################
class 몬스터처치훈련01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[300,301,302], auto_target=False)
        self.show_guide_summary(entity_id=25201051, text_id=25201051, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002321], quest_states=[1]):
            # 몬스터 처치 훈련01
            return 몬스터처치훈련02(self.ctx)


class 몬스터처치훈련02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[400,401,402], auto_target=False)
        self.show_guide_summary(entity_id=25201052, text_id=25201052, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002322], quest_states=[1]):
            # 할아버지대련01
            return 할아버지대련01(self.ctx)


# ########################씬3 할아버지 대련########################
class 할아버지대련01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000105, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 할아버지대련02_b(self.ctx)


class 할아버지대련02_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_ten_comeFront')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1000,1001,1002,1003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return 할아버지대련03(self.ctx)


class 할아버지대련03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.5, duration=2.0, interpolator=2) # 2초간 느려지기 시작
        self.set_npc_emotion_loop(spawn_id=200, sequence_name='Attack_Idle_A', duration=15000.0)
        self.select_camera_path(path_ids=[1004,1005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 할아버지대련04(self.ctx)


class 할아버지대련04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=6000.0)
        self.select_camera_path(path_ids=[1006,1007], return_view=False)
        self.add_balloon_talk(msg='$52000105_QD__52000105__0$', duration=6000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 할아버지대련05_B(self.ctx)


class 할아버지대련05_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC_Run_0')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 할아버지대련05(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 할아버지대련05(self.ctx)


class 할아버지대련05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.destroy_monster(spawn_ids=[200])
        self.spawn_monster(spawn_ids=[500], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0.5)
        self.show_guide_summary(entity_id=25201053, text_id=25201053, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002322], quest_states=[2]):
            # 대련 퀘스트를 받으면 할아버지 등장
            return 대련종료씬시작01(self.ctx)


class 대련종료씬시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_cinematic_ui(type=1)
        self.destroy_monster(spawn_ids=[203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 대련종료씬시작02(self.ctx)


# ########################대련 종료씬########################
class 대련종료씬시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[200])
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.move_user(map_id=52000105, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 대련종료씬시작02_01(self.ctx)


class 대련종료씬시작02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 대련종료씬시작03(self.ctx)


class 대련종료씬시작03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Attack_Idle_A', duration=5000.0)
        self.move_user_path(patrol_name='MS2PatrolData_PC_Run_0')
        self.select_camera_path(path_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2012,2013], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 대련종료씬시작04(self.ctx)


class 대련종료씬시작04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2014,2015], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대련종료씬시작06(self.ctx)


class 대련종료씬시작06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=0.3, end_scale=0.3, duration=2.5, interpolator=3) # 2초간 느려지기 시작
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Attack_01_B')
        self.select_camera_path(path_ids=[2016,2017], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return 대련종료씬시작07(self.ctx)


class 대련종료씬시작07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Dead_A'])
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 대련종료씬시작07_b(self.ctx)


class 대련종료씬시작07_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=100, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 대련종료씬시작08(self.ctx)


class 대련종료씬시작08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=100, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_pc_emotion_sequence(sequence_names=['Stuck_A'])
        self.select_camera_path(path_ids=[2018,2019], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대련종료씬시작09(self.ctx)


class 대련종료씬시작09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대련종료씬시작10(self.ctx)


class 대련종료씬시작10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_onetime_effect(id=10, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera(interpolation_time=1.0)
        self.set_pc_emotion_loop(sequence_name='Stun_A', duration=6500.0)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_ririn_go')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대련종료씬시작11(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolation_time=1.0)
        self.set_pc_emotion_loop(sequence_name='Stun_A', duration=6500.0)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_ririn_go')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 대련종료씬시작11(self.ctx)


class 대련종료씬시작11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002322], quest_states=[3]):
            return 떠나는할아버지01(self.ctx)


# ########################씬4 떠나는할아버지01########################
class 떠나는할아버지01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=떠나는할아버지07, action='exit')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 떠나는할아버지02(self.ctx)


class 떠나는할아버지02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_ten_exit_0')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_ririn_Turn')
        self.move_user_path(patrol_name='MS2PatrolData_PC_Turn')
        self.select_camera_path(path_ids=[1008,1009], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 떠나는할아버지03(self.ctx)


class 떠나는할아버지03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003175, illust_id='Ten_normal', msg='$52000105_QD__52000105__1$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 떠나는할아버지04(self.ctx)


class 떠나는할아버지04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_tenExit_1')
        self.add_balloon_talk(msg='$52000105_QD__52000105__2$', duration=6000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=201, msg='$52000105_QD__52000105__3$', duration=6000, delay_tick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 떠나는할아버지05(self.ctx)


class 떠나는할아버지05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 떠나는할아버지06(self.ctx)


class 떠나는할아버지06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.show_caption(type='VerticalCaption', title='$52000105_QD__52000105__4$', desc='$52000105_QD__52000105__5$', align=Align.Bottom | Align.Left, duration=10000, scale=2.5)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 떠나는할아버지07(self.ctx)


class 떠나는할아버지07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=52000106, portal_id=1)


initial_state = Wait
