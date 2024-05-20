""" trigger/52000152_qd/52000152.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1000)
        self.move_user(map_id=52000152, portal_id=1010)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='jobChangeStory.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 묘지전경씬01(self.ctx)
        if self.wait_tick(wait_tick=85000):
            return 묘지전경씬01(self.ctx)


class 묘지전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 묘지전경씬02_1(self.ctx)


class 묘지전경씬02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user_path(patrol_name='MS2PatrolData_PC_Walk')
        self.select_camera_path(path_ids=[4000,4001], return_view=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 묘지전경씬02(self.ctx)


class 묘지전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003,4004,4005], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52000152_QD__52000152__0$', desc='$52000152_QD__52000152__1$', align=Align.Bottom | Align.Left, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
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
        self.add_balloon_talk(msg='$52000152_QD__52000152__2$', duration=6000, delay_tick=1000)
        self.show_guide_summary(entity_id=25201521, text_id=25201521, duration=10000)
        self.spawn_monster(spawn_ids=[2000], auto_target=False) # 조디의무덤

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002328], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 제니아등장01(self.ctx)


# ########################씬2 케이틀린 등장########################
class 제니아등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False) # 제니아
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_xeniaMove')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002332], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 수련장이동01(self.ctx)


class 수련장이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 수련장이동02(self.ctx)


class 수련장이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000153, portal_id=1)


initial_state = Wait
