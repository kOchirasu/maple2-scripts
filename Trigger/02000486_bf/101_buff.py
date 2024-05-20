""" trigger/02000486_bf/101_buff.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[900]):
            return 타임(self.ctx)


class 타임(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900]) or self.monster_dead(spawn_ids=[901]):
            return None # Missing State: Move01


class 버프_종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


initial_state = 전투시작
