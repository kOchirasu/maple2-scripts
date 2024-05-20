""" trigger/52020011_qd/main_a.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200015], quest_states=[2]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Setting(self.ctx)


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.move_user(map_id=52020011, portal_id=6001)
        self.set_scene_skip(state=Exit, action='Exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4002], return_view=False)
        self.show_caption(type='VerticalCaption', title='$map:52020011$', desc='$NpcName:11003599$의 임시 거처', align=Align.Center | Align.Left, offset_rate_x=0.05, offset_rate_y=0.15, duration=3000, scale=1.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003,4004,4005,4006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return scene_03(self.ctx)

    def on_exit(self) -> None:
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Chin_Chin_A'])


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007,4008], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='NameCaption', title='$NpcName:11003599$', desc='크리티아스 왕녀', align=Align.Center | Align.Left, offset_rate_x=0.05, offset_rate_y=0.15, duration=3000, scale=2.0)
        self.add_cinematic_talk(npc_id=11003599, msg='그래, 반갑구나.', duration=2800)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Exit(self.ctx)


class Exit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()


initial_state = Idle
