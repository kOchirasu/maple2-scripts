""" trigger/63000036_cs/listen01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice_DarkShadow_02000986
        self.set_effect(trigger_ids=[5000])
        self.set_effect(trigger_ids=[5001]) # Voice_Kandura_00001863
        self.set_effect(trigger_ids=[5002]) # Voice_Kandura_00001864

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000455], quest_states=[1]):
            # 하산 퀘스트 진행중 상태
            return CameraWalk01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[90000455], quest_states=[2]):
            # 하산 퀘스트 완료 가능 상태, 안전 장치
            return CameraWalk01(self.ctx)
        if self.wait_tick(wait_tick=4000):
            return PCTeleport02(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102], auto_target=False)
        self.select_camera(trigger_id=500)
        self.set_scene_skip(state=DialogueSkip03, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraWalk02(self.ctx)


class CameraWalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraWalk03(self.ctx)


class CameraWalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Dialogue01(self.ctx)


class Dialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Voice_DarkShadow_02000986
        self.set_effect(trigger_ids=[5000], visible=True)
        self.set_dialogue(type=2, spawn_id=11001701, script='$63000036_CS__LISTEN01__0$', time=12) # 검은 그림자 02000986

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return DialogueSkip01(self.ctx)


class DialogueSkip01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue02(self.ctx)


class Dialogue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # Voice_Kandura_00001863
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000036_CS__LISTEN01__1$', time=11) # 칸두라 00001863
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return DialogueSkip02(self.ctx)


class DialogueSkip02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Dialogue03(self.ctx)


class Dialogue03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # Voice_Kandura_00001864
        self.set_dialogue(type=2, spawn_id=11001559, script='$63000036_CS__LISTEN01__2$', time=9) # 칸두라 00001864

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return DialogueSkip03(self.ctx)


class DialogueSkip03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return PCTeleport01(self.ctx)


class PCTeleport01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCTeleport02(self.ctx)


class PCTeleport02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000062, portal_id=13)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
