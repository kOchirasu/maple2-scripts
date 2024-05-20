""" trigger/52000160_qd/52000160.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002742], quest_states=[3]):
            return 떠난다_01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002743], quest_states=[3]):
            return 프론티아재단으로_01(self.ctx)
        if self.user_detected(box_ids=[2001], job_code=0):
            return 전직컷씬01(self.ctx)


class 전직컷씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='jobChange_Assassin.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 다크윈드도착_01(self.ctx)
        if self.wait_tick(wait_tick=8000):
            return 다크윈드도착_01(self.ctx)


class 다크윈드도착_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다크윈드도착_02(self.ctx)


class 다크윈드도착_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다크윈드도착_03(self.ctx)


class 다크윈드도착_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다크윈드도착_04(self.ctx)


class 다크윈드도착_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4002], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 다크윈드도착_05(self.ctx)


class 다크윈드도착_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다크윈드도착_06(self.ctx)


class 다크윈드도착_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다크윈드도착_07(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다크윈드도착_07(self.ctx)


class 다크윈드도착_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전직한다(self.ctx)


class 전직한다(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002742], quest_states=[2]):
            return 전직이펙트_01(self.ctx)


class 전직이펙트_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전직이펙트_02(self.ctx)


class 전직이펙트_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 떠난다_01(self.ctx)


class 떠난다_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002743], quest_states=[3]):
            return 프론티아재단으로_01(self.ctx)


class 프론티아재단으로_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 프론티아재단으로_02(self.ctx)


class 프론티아재단으로_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000186, portal_id=1)


initial_state = wait_01
