""" trigger/52020011_qd/main_b.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_actor(trigger_id=8001, initial_sequence='Attack_Idle_A')
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200130], quest_states=[2]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Set(self.ctx)


class Set(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020011, portal_id=6001)
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_actor(trigger_id=8001, visible=True, initial_sequence='Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Go(self.ctx)


class Go(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003599, msg='나 $npcName:11003599$의 이름으로 명한다.', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Scene_01(self.ctx)


class Scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003599, msg='이 땅의 모든 저주받은 존재여! 깊고 어두운 곳으로 떨어져라!', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Scene_02(self.ctx)


class Scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Scene_03(self.ctx)


class Scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_effect(trigger_ids=[5004], visible=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.add_balloon_talk(msg='!', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return Scene_Exit(self.ctx)


class Scene_Exit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020020, portal_id=6001)


initial_state = Idle
