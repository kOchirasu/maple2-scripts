""" trigger/63000035_cs/report01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # Beep_Loop
        self.set_effect(trigger_ids=[5001]) # MonitorOn_Pop
        # Voice_Kandura_Satisfied_00001866
        self.set_effect(trigger_ids=[6000])
        # Voice_Kandura_Think_00001867
        self.set_effect(trigger_ids=[6001])
        self.set_sound(trigger_id=10000) # BGM
        self.set_sound(trigger_id=10001) # AMB_BrokenTV
        self.set_sound(trigger_id=10002) # AMB_AbandonedFacility
        self.set_mesh(trigger_ids=[3000], visible=True) # MonitorOff
        self.set_mesh(trigger_ids=[3001]) # MonitorOn
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PlayOpeningMovie02(self.ctx)


class PlayOpeningMovie02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='common\\Common_Opening.usm', movie_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 2:
            return PlayMovie01(self.ctx)
        if self.wait_tick(wait_tick=190000):
            return PlayMovie01(self.ctx)


class PlayMovie01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PlayMovie02(self.ctx)


class PlayMovie02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Cut_Vivid_Dream.swf', movie_id=1) # 소울바인더 인트로 컷신

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return LodingDelay01(self.ctx)
        if self.wait_tick(wait_tick=77000):
            return LodingDelay01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=10000, enable=True) # BGM
        self.set_sound(trigger_id=10001, enable=True) # AMB_BrokenTV
        self.set_sound(trigger_id=10002, enable=True) # AMB_AbandonedFacility
        self.set_effect(trigger_ids=[5000], visible=True) # Beep_Loop
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Operator01(self.ctx)


class Operator01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001705, script='$63000035_CS__REPORT01__0$', time=6) # 오퍼레이터
        self.set_scene_skip(state=PCTeleport01, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return OperatorSkip01(self.ctx)


class OperatorSkip01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Operator02(self.ctx)


class Operator02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001705, script='$63000035_CS__REPORT01__1$', time=6) # 오퍼레이터

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return OperatorSkip02(self.ctx)


class OperatorSkip02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return MonitorOn01(self.ctx)


class MonitorOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=502)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return MonitorOn02(self.ctx)


class MonitorOn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # Beep_Loop
        self.set_effect(trigger_ids=[5001], visible=True) # MonitorOn_Pop
        self.set_mesh(trigger_ids=[3001], visible=True) # MonitorOn
        self.set_mesh(trigger_ids=[3000], start_delay=100) # MonitorOff

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return MonitorOn03(self.ctx)


class MonitorOn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=503)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return KahnTalk01(self.ctx)


class KahnTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000035_CS__REPORT01__2$', time=6) # 칸두라 00001867
        # Voice_Kandura_Think_00001867
        self.set_effect(trigger_ids=[6001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return KahnTalk02(self.ctx)


class KahnTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return KahnTalk03(self.ctx)


class KahnTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=504)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A') # 칸두라

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return KahnTalk04(self.ctx)


class KahnTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return KahnTalk05(self.ctx)


class KahnTalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000035_CS__REPORT01__3$', time=6) # 칸두라 00001866
        # Voice_Kandura_Satisfied_00001866
        self.set_effect(trigger_ids=[6000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return KahnTalk06(self.ctx)


class KahnTalk06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCTeleport01(self.ctx)


class PCTeleport01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCTeleport02(self.ctx)


class PCTeleport02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=10000) # BGM
        self.set_sound(trigger_id=10001) # AMB_BrokenTV
        self.set_sound(trigger_id=10002) # AMB_AbandonedFacility

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PCTeleport03(self.ctx)


class PCTeleport03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000024, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=504, enable=False)


initial_state = Wait
