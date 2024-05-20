""" trigger/63000042_cs/wakeup01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001484], quest_states=[2]):
            # 그 길에서 만난 것은 퀘스트 완료 가능 상태
            return LodingDelay00(self.ctx)


class LodingDelay00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_portal(portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000042, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LodingDelay02(self.ctx)


class LodingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.select_camera(trigger_id=500)
        self.set_pc_emotion_loop(sequence_name='Down_Idle_D', duration=6000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCDownIdle01(self.ctx)


class PCDownIdle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=PCDownIdle02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCDownIdle02(self.ctx)


class PCDownIdle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DoctorTalk01(self.ctx)


class DoctorTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000038, script='$63000042_CS__WAKEUP01__0$', time=4)
        self.set_skip(state=DoctorTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return DoctorTalk01Skip(self.ctx)


class DoctorTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return LookAround01(self.ctx)


class LookAround01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500, enable=False)
        self.select_camera(trigger_id=501)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')
        self.set_pc_emotion_loop(sequence_name='Sit_Ground_Idle_A', duration=18000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LookAround02(self.ctx)


class LookAround02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return DoctorTalk02(self.ctx)


class DoctorTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=5000.0)
        self.set_dialogue(type=2, spawn_id=11000038, script='$63000042_CS__WAKEUP01__1$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DoctorTalk03(self.ctx)


class DoctorTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=5000.0)
        self.set_dialogue(type=2, spawn_id=11000038, script='$63000042_CS__WAKEUP01__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return DoctorTalk04(self.ctx)


class DoctorTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=5000.0)
        self.set_dialogue(type=2, spawn_id=11000038, script='$63000042_CS__WAKEUP01__3$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return SceneEnd01(self.ctx)


class SceneEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SceneEnd02(self.ctx)


class SceneEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501, enable=False)
        self.set_pc_emotion_sequence(sequence_names=['Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)


initial_state = Wait
