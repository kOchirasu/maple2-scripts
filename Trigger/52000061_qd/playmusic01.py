""" trigger/52000061_qd/playmusic01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # PlayPiano
        self.set_effect(trigger_ids=[5001]) # PlayGuitar
        self.set_effect(trigger_ids=[5002]) # PlayClarinet
        self.set_effect(trigger_ids=[5003]) # PlayCello
        self.set_effect(trigger_ids=[5004]) # PlayViolin
        self.set_effect(trigger_ids=[5100]) # SpotLight
        self.set_effect(trigger_ids=[5200]) # Applause
        self.set_sound(trigger_id=10000) # PlayMusic
        self.spawn_monster(spawn_ids=[101,201,202,203,204], auto_target=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000550], quest_states=[1]):
            # 퀘스트 수락한 상태
            return LodingDelay01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000550], quest_states=[2]):
            # 퀘스트 수락한 상태
            return Quit(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LodingDelay02(self.ctx)


class LodingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCWalkInStage01(self.ctx)


class PCWalkInStage01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000061, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCWalkInStage02(self.ctx)


class PCWalkInStage02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1000')
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCWalkInStage03(self.ctx)


class PCWalkInStage03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[601,602])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return PCWalkInStage04(self.ctx)


class PCWalkInStage04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=603)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCBow01(self.ctx)


class PCBow01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Chin_Chin_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return PCBow02(self.ctx)


class PCBow02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCBow03(self.ctx)


class PCBow03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.select_camera(trigger_id=610)
        self.move_user(map_id=52000061, portal_id=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCReadyToPlayThePiano01(self.ctx)


class PCReadyToPlayThePiano01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Music_Piano_Idle_A', duration=31500.0)
        self.set_effect(trigger_ids=[5100], visible=True) # SpotLight

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCPlayMusic01(self.ctx)


class PCPlayMusic01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_sound(trigger_id=10000, enable=True) # PlayMusic

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCPlayMusic02(self.ctx)


class PCPlayMusic02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # PlayPiano
        self.set_effect(trigger_ids=[5001], visible=True) # PlayGuitar
        self.set_effect(trigger_ids=[5002], visible=True) # PlayClarinet
        self.set_effect(trigger_ids=[5003], visible=True) # PlayCello
        self.set_effect(trigger_ids=[5004], visible=True) # PlayViolin
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Play_A', duration=30500.0)
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Play_A', duration=30500.0)
        self.set_npc_emotion_loop(spawn_id=203, sequence_name='Play_A', duration=30500.0)
        self.set_npc_emotion_loop(spawn_id=204, sequence_name='Play_A', duration=30500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30500):
            return PCPlayMusic03(self.ctx)


class PCPlayMusic03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=10000) # PlayMusic
        self.set_effect(trigger_ids=[5000]) # PlayPiano
        self.set_effect(trigger_ids=[5001]) # PlayGuitar
        self.set_effect(trigger_ids=[5002]) # PlayClarinet
        self.set_effect(trigger_ids=[5003]) # PlayCello
        self.set_effect(trigger_ids=[5004]) # PlayViolin
        self.set_effect(trigger_ids=[5200], visible=True) # Applause

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCPlayQuit01(self.ctx)


class PCPlayQuit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[5100]) # SpotLight

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return PCPlayQuit02(self.ctx)


class PCPlayQuit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000061, portal_id=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCPlayQuit03(self.ctx)


class PCPlayQuit03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.set_achievement(trigger_id=9900, type='trigger', achieve='PerformanceWithNPC')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[90000550], quest_states=[3]):
            # 퀘스트 수락한 완료 가능 상태
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
