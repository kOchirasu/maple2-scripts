""" trigger/52000199_qd/52000199_2.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003448], quest_states=[2]):
            # 예언의 때 퀘스트 진행 유저
            return CameraEffect01(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user(map_id=52000199, portal_id=5001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000199_QD__52000199_2__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return CameraEffect02_2(self.ctx)


class CameraEffect02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_ui(ui_names=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'])
        self.add_buff(box_ids=[2001], skill_id=99910403, level=1, is_player=False) # 다크로드 변신
        self.add_buff(box_ids=[2001], skill_id=99910403, level=1, is_player=False, is_skill_set=False) # 다크로드 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = start
