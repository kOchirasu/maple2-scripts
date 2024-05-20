""" trigger/52000074_qd/questnpcspawn01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,201], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002679], quest_states=[3]):
            return NpcRemove01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002679], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002679], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002678], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002678], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002678], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002677], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002677], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002677], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002676], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002676], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002676], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002675], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002675], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002675], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002674], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002674], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002674], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002673], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002673], quest_states=[2]):
            return NpcTalk01(self.ctx)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,201])


class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)


class NpcTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraSet01(self.ctx)


class CameraSet01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=TalkEnd01, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EveTalk01(self.ctx)


class EveTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001962, script='$52000074_QD__QUESTNPCSPAWN01__0$', time=5) # 이브
        # self.set_skip(state=EveTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EveTalk01Skip(self.ctx)


class EveTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return LennonTalk01(self.ctx)


class LennonTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001961, script='$52000074_QD__QUESTNPCSPAWN01__1$', time=5) # 레논
        # self.set_skip(state=LennonTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LennonTalk01Skip(self.ctx)


class LennonTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return EveTalk02(self.ctx)


class EveTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001962, script='$52000074_QD__QUESTNPCSPAWN01__2$', time=3) # 이브
        # self.set_skip(state=EveTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EveTalk02Skip(self.ctx)


class EveTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkEnd01(self.ctx)


class TalkEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.select_camera(trigger_id=600, enable=False)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)


initial_state = Wait
