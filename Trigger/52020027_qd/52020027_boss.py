""" trigger/52020027_qd/52020027_boss.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Boss') == 1:
            return 페이즈1(self.ctx)


class 페이즈1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SerihaAI') == 1:
            # <AI에서 신호 쏴줌(AI_Seriha.xml)>
            return 도약(self.ctx)


class 도약(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=903, spawn_ids=[111]):
            return 페이즈2(self.ctx)


class 페이즈2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=111, script='조심하는 게 좋을걸?', time=4)
        self.spawn_monster(spawn_ids=[112])
        self.spawn_monster(spawn_ids=[113])
        self.spawn_monster(spawn_ids=[114])
        self.spawn_monster(spawn_ids=[115])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NPC애니세팅(self.ctx)


class NPC애니세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=114, sequence_name='Attack_01_A', duration=2000.0)
        self.set_npc_emotion_loop(spawn_id=115, sequence_name='Attack_01_A', duration=2000.0)


initial_state = 감지
