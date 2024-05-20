""" trigger/52000109_qd/52000109.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 아이샤등장
        self.spawn_monster(spawn_ids=[2001], auto_target=False) # 아이샤등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10010]):
            return Wait02(self.ctx)


class Wait02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Wait03(self.ctx)


class Wait03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000109_QD__52000109__0$', desc='$52000109_QD__52000109__1$', align=Align.Bottom | Align.Left, duration=6000, scale=2.5)
        self.set_onetime_effect(id=40, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.move_user(map_id=52000109, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에델슈타인전경씬01(self.ctx)


class 에델슈타인전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1000], return_view=False)
        self.set_onetime_effect(id=40, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_balloon_talk(msg='$52000109_QD__52000109__2$', duration=5000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=200, msg='$52000109_QD__52000109__3$', duration=6000, delay_tick=4000)
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=15000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬02(self.ctx)


class 에델슈타인전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003292, illust_id='Ayesha_normal', msg='$52000109_QD__52000109__4$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000982, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000982.xml')
        self.set_onetime_effect(id=50, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬03(self.ctx)


class 에델슈타인전경씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000109_QD__52000109__5$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=60, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬04(self.ctx)


class 에델슈타인전경씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003292, illust_id='Ayesha_normal', msg='$52000109_QD__52000109__6$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000983, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000983.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬05(self.ctx)


class 에델슈타인전경씬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000109_QD__52000109__7$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬06(self.ctx)


class 에델슈타인전경씬06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000109_QD__52000109__8$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬07(self.ctx)


class 에델슈타인전경씬07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003292, illust_id='Ayesha_normal', msg='$52000109_QD__52000109__9$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000984, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000984.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬08(self.ctx)


class 에델슈타인전경씬08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000109_QD__52000109__10$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬10(self.ctx)


class 에델슈타인전경씬10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1001], return_view=False)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_Isha')
        self.move_user_path(patrol_name='MS2PatrolData_PC')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬11(self.ctx)


class 에델슈타인전경씬11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000109_QD__52000109__11$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬12(self.ctx)


class 에델슈타인전경씬12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000109_QD__52000109__12$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬13(self.ctx)


class 에델슈타인전경씬13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1002,1003], return_view=False)
        self.add_balloon_talk(msg='$52000109_QD__52000109__13$', duration=5000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=200, msg='$52000109_QD__52000109__14$', duration=6000, delay_tick=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에델슈타인전경씬14(self.ctx)


class 에델슈타인전경씬14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트대기01_20002302(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_Isha')
        self.move_user(map_id=52000109, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트대기01_20002302(self.ctx)


class 퀘스트대기01_20002302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=25201091, text_id=25201091, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002304], quest_states=[2]):
            return 라딘대화씬03(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002303], quest_states=[3]):
            return 라딘대화씬01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002302], quest_states=[3]):
            return 라딘등장씬01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002302], quest_states=[2]):
            return 라딘등장씬01(self.ctx)


# ########################20002302, 라딘 등장########################
class 라딘등장씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[2002], auto_target=False) # 라딘등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 라딘등장씬02(self.ctx)


class 라딘등장씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_radin')
        self.select_camera_path(path_ids=[1004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라딘등장씬03(self.ctx)


class 라딘등장씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003295, illust_id='Radin_normal', msg='$52000109_QD__52000109__15$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 라딘등장씬04(self.ctx)


class 라딘등장씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=200, emotion_name='hello_Cait')
        self.show_caption(type='NameCaption', title='$52000109_QD__52000109__16$', desc='$52000109_QD__52000109__17$', align=Align.Center, offset_rate_x=-0.15, offset_rate_y=0.15, duration=10000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 라딘등장씬04_1(self.ctx)


class 라딘등장씬04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라딘등장씬05(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_radin')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라딘등장씬05(self.ctx)


class 라딘등장씬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002303], quest_states=[2]):
            return 라딘대화씬01(self.ctx)


# ########################20002302, 라딘 등장########################
class 라딘대화씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[2004,302], auto_target=False) # 라딘등장
        self.destroy_monster(spawn_ids=[2002,200])
        self.move_user(map_id=52000109, portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 라딘대화씬02(self.ctx)


class 라딘대화씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002304], quest_states=[2]):
            return 라딘대화씬03(self.ctx)


class 라딘대화씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=라딘대화씬05, action='exit')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 라딘대화씬04(self.ctx)


class 라딘대화씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000109_QD__52000109__18$', desc='$52000109_QD__52000109__19$', align=Align.Bottom | Align.Left, duration=10000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 라딘대화씬04_1(self.ctx)


class 라딘대화씬04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라딘대화씬05(self.ctx)


class 라딘대화씬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000062, portal_id=13)


initial_state = Wait01
