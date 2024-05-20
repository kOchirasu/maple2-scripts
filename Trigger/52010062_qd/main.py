""" trigger/52010062_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.spawn_monster(spawn_ids=[2000], auto_target=False) # 인페르녹
        self.spawn_monster(spawn_ids=[2001], auto_target=False) # 크림슨 발록
        self.spawn_monster(spawn_ids=[2002], auto_target=False) # 크림슨 발록
        self.spawn_monster(spawn_ids=[2003], auto_target=False) # 크림슨 발록
        self.set_effect(trigger_ids=[6000,6001,6002,6003,6010,6011,6031,6032,6033,6041,6042,6043,6051,6052,6053]) # 에너지충전이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000051], quest_states=[3]):
            return 돌아가(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000051], quest_states=[2]):
            return 돌아가(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000051], quest_states=[1]):
            return 스케치01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000050], quest_states=[3]):
            return 돌아가(self.ctx)
        if not self.quest_user_detected(box_ids=[9001], quest_ids=[91000051], quest_states=[1]):
            return 돌아가(self.ctx)


class 스케치01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 스케치02(self.ctx)


class 스케치02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[4000,4001], return_view=False)
        self.set_effect(trigger_ids=[6001,6002,6003,6010], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 스케치03(self.ctx)


class 스케치03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 크림슨발록대사01(self.ctx)


class 크림슨발록대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(trigger_ids=[6003], visible=True)
        self.add_cinematic_talk(npc_id=11003835, msg='$52010062_QD__main__0$', duration=7000, align=Align.Right) # 2003
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 크림슨발록대사02(self.ctx)


class 크림슨발록대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True)
        self.add_cinematic_talk(npc_id=11003833, msg='$52010062_QD__main__1$', duration=5000, align=Align.Right) # 2001
        self.select_camera_path(path_ids=[4004,4005], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=2001, sequence_name='Attack_01_C,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 크림슨발록대사03(self.ctx)


class 크림슨발록대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002], visible=True)
        self.add_cinematic_talk(npc_id=11003834, msg='$52010062_QD__main__2$', duration=5000, align=Align.Right) # 2002
        self.select_camera_path(path_ids=[4006,4007], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=2002, sequence_name='Attack_01_B,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 크림슨발록대사04(self.ctx)


class 크림슨발록대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001,6002,6003], visible=True)
        self.add_cinematic_talk(npc_id=11003793, msg='$52010062_QD__main__3$', duration=4000, align=Align.Right) # 원경 스케치 시작,인페르녹깨어나는장면 준비
        # &lt;font size='50'&gt;아니…그분의 손에 들어갈 테지…&lt;/font&gt;
        self.select_camera_path(path_ids=[4008,4009,4013,4014], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹부활00(self.ctx)


class 인페르녹부활00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(trigger_ids=[6031,6032,6033], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 인페르녹부활01(self.ctx)


class 인페르녹부활01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=0):
            return 인페르녹부활02(self.ctx)


class 인페르녹부활02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_cinematic_ui(type=1)
        # self.select_camera_path(path_ids=[4010,4011,4012], return_view=False)
        self.set_effect(trigger_ids=[6000], visible=True) # 화면흔들림 on
        self.set_effect(trigger_ids=[6041,6042,6043], visible=True)
        self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.1, duration=10.0, interpolator=1) # 10초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 인페르녹부활03(self.ctx)


class 인페르녹부활03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_effect(trigger_ids=[6051,6052,6053], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 인페르녹부활04(self.ctx)


class 인페르녹부활04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True) # 화면흔들림 on
        self.set_effect(trigger_ids=[6010]) # 대기이펙트 off

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 인페르녹부활05(self.ctx)


class 인페르녹부활05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6031,6032,6033,6041,6042,6043,6051,6052,6053])
        self.set_effect(trigger_ids=[6011], visible=True) # 폭주이펙트 on

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 인페르녹부활06(self.ctx)


class 인페르녹부활06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(trigger_ids=[6031,6032,6033,6041,6042,6043,6051,6052,6053])
        self.set_effect(trigger_ids=[6000]) # 화면흔들림 off

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 인페르녹대사00(self.ctx)


class 인페르녹대사00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010,4011,4012], return_view=False)
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 인페르녹대사01(self.ctx)


class 인페르녹대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4021], return_view=False)
        self.add_cinematic_talk(npc_id=11003831, illust_id='infernog_nomal', msg='$52010062_QD__main__4$', duration=4000, align=Align.Right)
        self.set_effect(trigger_ids=[6011]) # 폭주이펙트 off
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 인페르녹대사02(self.ctx)


class 인페르녹대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003831, illust_id='infernog_nomal', msg='$52010062_QD__main__5$', duration=4000, align=Align.Right)
        self.set_npc_emotion_sequence(spawn_id=2000, sequence_name='Attack_01_B')
        self.set_effect(trigger_ids=[6000], visible=True) # 화면흔들림 on
        self.set_effect(trigger_ids=[6011], visible=True) # 폭주이펙트 on

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 부하대사01(self.ctx)


class 부하대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003834, msg='$52010062_QD__main__6$', duration=4000, align=Align.Right) # 2002
        self.set_effect(trigger_ids=[6000]) # 화면흔들림 off
        self.set_effect(trigger_ids=[6011]) # 폭주이펙트 on
        self.select_camera_path(path_ids=[4006,4007], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=2002, sequence_name='Attack_01_B,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 부하대사02(self.ctx)


class 부하대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003835, msg='$52010062_QD__main__7$', duration=4000, align=Align.Right) # 2003
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=2003, sequence_name='Attack_01_B,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 부하대사03(self.ctx)


class 부하대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003833, msg='$52010062_QD__main__8$', duration=4000, align=Align.Right) # 2001
        self.select_camera_path(path_ids=[4004,4005], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=2001, sequence_name='Attack_01_C,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 인페르녹대사03(self.ctx)


class 인페르녹대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013,4012], return_view=False)
        self.add_cinematic_talk(npc_id=11003831, illust_id='infernog_nomal', msg='$52010062_QD__main__9$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 인페르녹대사04(self.ctx)


class 인페르녹대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4021], return_view=False)
        self.add_cinematic_talk(npc_id=11003831, illust_id='infernog_nomal', msg='$52010062_QD__main__10$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 인페르녹대사05(self.ctx)


class 인페르녹대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4021,4022], return_view=False)
        self.add_cinematic_talk(npc_id=11003831, illust_id='infernog_nomal', msg='$52010062_QD__main__11$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 인페르녹대사06(self.ctx)


class 인페르녹대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4022,4023], return_view=False)
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.add_cinematic_talk(npc_id=11003831, illust_id='infernog_nomal', msg='$52010062_QD__main__12$', duration=4000, align=Align.Right)
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        self.set_effect(trigger_ids=[6000], visible=True) # 흔들림 on

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출종료(self.ctx)


class 스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(trigger_ids=[6000,6001,6002,6003,6010,6011,6031,6032,6033,6041,6042,6043,6051,6052,6053]) # 이펙트다끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=9001, type='trigger', achieve='infernogrevive') # 퀘스트 완료 업적

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 최종맵이동(self.ctx)


class 최종맵이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010052, portal_id=1) # 작전실로 자동 이동
        self.visible_my_pc(is_visible=True)
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return 최종맵이동(self.ctx)


class 돌아가(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010052, portal_id=1) # 작전실로 자동 이동
        self.visible_my_pc(is_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return 돌아가(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
