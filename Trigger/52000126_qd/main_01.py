""" trigger/52000126_qd/main_01.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100210], quest_states=[2]):
            return ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100210], quest_states=[3]):
            return ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100215], quest_states=[1]):
            return ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100215], quest_states=[2]):
            return ready(self.ctx)


# 준비
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000126, portal_id=6001)
        self.set_sound(trigger_id=7002, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[201])
        self.set_scene_skip(state=endwaiting, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return move(self.ctx)


class move(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_3001')
        self.add_balloon_talk(spawn_id=201, msg='$52000126_QD__MAIN_01__0$', duration=7000, delay_tick=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return talk(self.ctx)


class talk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Clap_A')
        self.add_balloon_talk(spawn_id=201, msg='$52000126_QD__MAIN_01__1$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return endtalk(self.ctx)


class endtalk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=201, msg='$52000126_QD__MAIN_01__2$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return endwaiting(self.ctx)


class endwaiting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
