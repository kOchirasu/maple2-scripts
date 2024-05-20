""" trigger/52020020_qd/main_a.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200130], quest_states=[2]):
            return ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200130], quest_states=[3]):
            return end(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52020020, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Monologue_01(self.ctx)


class Monologue_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='으으.......', duration=2500, align=Align.Right)
        self.set_scene_skip(state=end, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return Monologue_02(self.ctx)


class Monologue_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='도대체 무슨 일이 일어난 거지?', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return Monologue_03(self.ctx)


class Monologue_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='.......', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Monologue_04(self.ctx)


class Monologue_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequence_name='Sit_Ground_Idle_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=0, msg='잠깐! 여기는?!', duration=3000, align=Align.Right)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


initial_state = Idle
