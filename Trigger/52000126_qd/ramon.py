""" trigger/52000126_qd/ramon.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 장사꾼의 목격담(60100205) 완료 가능 상태 연출
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100205], quest_states=[2]):
            return fadein(self.ctx)


# 준비
class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=end, action='exit')
        self.select_camera_path(path_ids=[4101], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return camera_01(self.ctx)


class camera_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')
        self.select_camera_path(path_ids=[4101,4102], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return camera_02(self.ctx)


class camera_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')
        self.select_camera_path(path_ids=[4102,4103], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return camera_03(self.ctx)


class camera_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003209, msg='$52000126_QD__RAMON__0$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()


initial_state = idle
