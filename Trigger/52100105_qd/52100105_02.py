""" trigger/52100105_qd/52100105_02.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2002], quest_ids=[50101030], quest_states=[3]):
            return wait_03(self.ctx)
        if self.quest_user_detected(box_ids=[2002], quest_ids=[50101020], quest_states=[2]):
            return wait_03(self.ctx)


class wait_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출보러(self.ctx)


class 연출보러(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52100105, portal_id=4)


initial_state = wait_01
