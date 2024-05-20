""" trigger/52000186_qd/52000186.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='common\\jp\\Lapenta_Frontier.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 묘지전경씬01(self.ctx)
        if self.wait_tick(wait_tick=110000):
            return 묘지전경씬01(self.ctx)


class 묘지전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[8000,8001,8002,8003], return_view=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 묘지전경씬02(self.ctx)


class 묘지전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004,8005], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52000186_QD__52000186__0$', desc='$52000186_QD__52000186__1$', align=Align.Bottom | Align.Left, duration=7000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 묘지전경씬03(self.ctx)


class 묘지전경씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.add_balloon_talk(msg='$52000186_QD__52000186__2$', duration=6000, delay_tick=1000)
        self.show_guide_summary(entity_id=25201861, text_id=25201861, duration=10000)
        self.spawn_monster(spawn_ids=[4000], auto_target=False)
        self.spawn_monster(spawn_ids=[4001], auto_target=False)
        self.spawn_monster(spawn_ids=[4002], auto_target=False)
        self.spawn_monster(spawn_ids=[4003], auto_target=False)
        self.spawn_monster(spawn_ids=[4004], auto_target=False)
        self.spawn_monster(spawn_ids=[4005], auto_target=False)
        self.spawn_monster(spawn_ids=[4006], auto_target=False)
        self.spawn_monster(spawn_ids=[4007], auto_target=False)
        self.spawn_monster(spawn_ids=[4008], auto_target=False)
        self.spawn_monster(spawn_ids=[4009], auto_target=False)
        self.spawn_monster(spawn_ids=[4010], auto_target=False)
        self.spawn_monster(spawn_ids=[2000], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002777], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002778], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002779], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002780], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002781], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002782], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002783], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002784], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002785], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002786], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[40002787], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 출범연설시작01(self.ctx)


# ########################씬2 케이틀린 등장########################
class 출범연설시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 출범연설시작02(self.ctx)


class 출범연설시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000186, portal_id=20)
        self.destroy_monster(spawn_ids=[4000])
        self.destroy_monster(spawn_ids=[4001])
        self.destroy_monster(spawn_ids=[4002])
        self.destroy_monster(spawn_ids=[4003])
        self.destroy_monster(spawn_ids=[4004])
        self.destroy_monster(spawn_ids=[4005])
        self.destroy_monster(spawn_ids=[4006])
        self.destroy_monster(spawn_ids=[4007])
        self.destroy_monster(spawn_ids=[4008])
        self.destroy_monster(spawn_ids=[4009])
        self.destroy_monster(spawn_ids=[4010])
        self.spawn_monster(spawn_ids=[5000], auto_target=False)
        self.spawn_monster(spawn_ids=[5001], auto_target=False)
        self.spawn_monster(spawn_ids=[5002], auto_target=False)
        self.spawn_monster(spawn_ids=[5003], auto_target=False)
        self.spawn_monster(spawn_ids=[5004], auto_target=False)
        self.spawn_monster(spawn_ids=[5005], auto_target=False)
        self.spawn_monster(spawn_ids=[5006], auto_target=False)
        self.spawn_monster(spawn_ids=[5007], auto_target=False)
        self.spawn_monster(spawn_ids=[5008], auto_target=False)
        self.spawn_monster(spawn_ids=[5009], auto_target=False)
        self.spawn_monster(spawn_ids=[5010], auto_target=False)
        self.spawn_monster(spawn_ids=[3000], auto_target=False)
        self.spawn_monster(spawn_ids=[3001], auto_target=False)
        self.spawn_monster(spawn_ids=[3002], auto_target=False)
        self.spawn_monster(spawn_ids=[3003], auto_target=False)
        self.spawn_monster(spawn_ids=[3004], auto_target=False)
        self.spawn_monster(spawn_ids=[3005], auto_target=False)
        self.spawn_monster(spawn_ids=[3006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 출범연설시작03(self.ctx)


class 출범연설시작03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002388], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 베아트리체움직임01(self.ctx)


class 베아트리체움직임01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=3000, patrol_name='MS2PatrolData_bche_Run')
        self.move_npc(spawn_id=3001, patrol_name='MS2PatrolData_alf_Run')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002389], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 연설시퀀스종료01(self.ctx)


class 연설시퀀스종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연설시퀀스종료02(self.ctx)


class 연설시퀀스종료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5000])
        self.destroy_monster(spawn_ids=[5001])
        self.destroy_monster(spawn_ids=[5002])
        self.destroy_monster(spawn_ids=[5003])
        self.destroy_monster(spawn_ids=[5004])
        self.destroy_monster(spawn_ids=[5005])
        self.destroy_monster(spawn_ids=[5006])
        self.destroy_monster(spawn_ids=[5007])
        self.destroy_monster(spawn_ids=[5008])
        self.destroy_monster(spawn_ids=[5009])
        self.destroy_monster(spawn_ids=[5010])
        self.destroy_monster(spawn_ids=[3000])
        self.destroy_monster(spawn_ids=[3001])
        self.destroy_monster(spawn_ids=[3002])
        self.destroy_monster(spawn_ids=[3003])
        self.destroy_monster(spawn_ids=[3004])
        self.destroy_monster(spawn_ids=[3005])
        self.destroy_monster(spawn_ids=[3006])
        self.move_user(map_id=52010068, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연설시퀀스종료03(self.ctx)


class 연설시퀀스종료03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=20, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = Wait
