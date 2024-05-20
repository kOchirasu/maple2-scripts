""" trigger/52000106_qd/52000106.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002323], quest_states=[1]):
            # 몬스터 처치 훈련01
            return 그림자의침략01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002323], quest_states=[2]):
            return 그림자의침략완료02(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002325], quest_states=[2]):
            return 리엔을떠나다01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002323], quest_states=[3]):
            return 그림자의침략완료02(self.ctx)


# ########################그림자의침략 도입부 연출########################
class 그림자의침략01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 그림자의침략02(self.ctx)


class 그림자의침략02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1000,1001], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 그림자의침략03(self.ctx)


class 그림자의침략03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1002,1003], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_ririn_Turn')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 그림자의침략04(self.ctx)


class 그림자의침략04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[700,701,702,703], auto_target=False)
        self.set_effect(trigger_ids=[901], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 그림자의침략05(self.ctx)


class 그림자의침략05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[704,705,706,707], auto_target=False)
        self.set_effect(trigger_ids=[901], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 그림자의침략06(self.ctx)


class 그림자의침략06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[708,709,710,711], auto_target=False)
        self.set_effect(trigger_ids=[901], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 그림자의침략07(self.ctx)


class 그림자의침략07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[712,713,714,715], auto_target=False)
        self.set_effect(trigger_ids=[901], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 그림자의침략08(self.ctx)


class 그림자의침략08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[716,717,718,719], auto_target=False)
        self.set_effect(trigger_ids=[901], visible=True)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 그림자의침략09(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_ririn_Turn')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera(interpolation_time=0.5)
        self.spawn_monster(spawn_ids=[700,701,702,703], auto_target=False)
        self.spawn_monster(spawn_ids=[704,705,706,707], auto_target=False)
        self.spawn_monster(spawn_ids=[708,709,710,711], auto_target=False)
        self.spawn_monster(spawn_ids=[712,713,714,715], auto_target=False)
        self.spawn_monster(spawn_ids=[716,717,718,719], auto_target=False)
        self.spawn_monster(spawn_ids=[716,717,718,719], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 그림자의침략09(self.ctx)


# ########################그림자의침략 플레이 진행########################
class 그림자의침략09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[10011], skill_id=70000109, level=1, is_player=False, is_skill_set=False) # 초생회
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0.5)
        self.show_guide_summary(entity_id=25201061, text_id=25201061, duration=5000)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_ririn_go')
        self.add_balloon_talk(msg='$52000106_QD__52000106__0$', duration=6000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=101, msg='$52000106_QD__52000106__1$', duration=6000, delay_tick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002323], quest_states=[2]):
            return 그림자의침략완료01(self.ctx)


# ########################그림자의침략 마무리########################
class 그림자의침략완료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='$52000106_QD__52000106__2$', duration=6000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 그림자의침략완료02(self.ctx)


class 그림자의침략완료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 그림자의침략완료03(self.ctx)


class 그림자의침략완료03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0.5)
        self.set_onetime_effect(id=20, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.move_user(map_id=52000106, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002324], quest_states=[1]):
            return 할아버지의물품조사01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002324], quest_states=[2]):
            return 할아버지의물품조사01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002324], quest_states=[3]):
            return 할아버지의물품조사01(self.ctx)


# ########################할아버지의 물품 조사########################
class 할아버지의물품조사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[200])
        self.show_guide_summary(entity_id=25201062, text_id=25201062, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002325], quest_states=[2]):
            return 리엔을떠나다01(self.ctx)


# ########################PC,리엔을 떠나다########################
class 리엔을떠나다01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=리엔을떠나다09, action='exit')
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_ririn_goodBye_0')
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 리엔을떠나다02(self.ctx)


class 리엔을떠나다02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_onetime_effect(id=30, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1004,1005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 리엔을떠나다03(self.ctx)


class 리엔을떠나다03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003174, msg='$52000106_QD__52000106__3$', duration=4000, align=Align.Right)
        self.select_camera_path(path_ids=[1006,1007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 리엔을떠나다04(self.ctx)


class 리엔을떠나다04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003174, msg='$52000106_QD__52000106__4$', duration=5000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 리엔을떠나다05(self.ctx)


class 리엔을떠나다05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1008,1009], return_view=False)
        self.add_cinematic_talk(npc_id=11003174, illust_id='Ririn_normal', msg='$52000106_QD__52000106__5$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 리엔을떠나다06(self.ctx)


class 리엔을떠나다06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003174, illust_id='Ririn_normal', msg='$52000106_QD__52000106__6$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 리엔을떠나다07(self.ctx)


class 리엔을떠나다07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=40, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 리엔을떠나다08(self.ctx)


class 리엔을떠나다08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.show_caption(type='VerticalCaption', title='$52000106_QD__52000106__7$', desc='$52000106_QD__52000106__8$', align=Align.Bottom | Align.Left, duration=10000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 리엔을떠나다08_1(self.ctx)


class 리엔을떠나다08_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 리엔을떠나다09(self.ctx)


class 리엔을떠나다09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000115, portal_id=1)


initial_state = Wait
