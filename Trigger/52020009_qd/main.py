""" trigger/52020009_qd/main.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8001])
        self.set_interact_object(trigger_ids=[10001266], state=0)
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5006])
        self.set_effect(trigger_ids=[5100], visible=True) # 웃는 소리
        self.set_effect(trigger_ids=[5101], visible=True) # 까마귀 소리
        self.set_effect(trigger_ids=[5102], visible=True) # 뛰는 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200020], quest_states=[1]):
            return Ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200020], quest_states=[2]):
            return MeshOff(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200020], quest_states=[3]):
            return MeshOff(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[204])
        self.spawn_monster(spawn_ids=[205])
        self.spawn_monster(spawn_ids=[206])
        self.spawn_monster(spawn_ids=[207])
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_effect(trigger_ids=[5004], visible=True)
        self.set_effect(trigger_ids=[5005], visible=True)
        self.set_effect(trigger_ids=[5006], visible=True)
        self.set_mesh(trigger_ids=[8001], visible=True)
        self.add_balloon_talk(msg='!', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204,205,206,207]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001266], state=1)
        self.set_mesh(trigger_ids=[8001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000449], state=0):
            return MeshOff(self.ctx)


class MeshOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200020], quest_states=[1]):
            return Event_01(self.ctx)


initial_state = Idle
