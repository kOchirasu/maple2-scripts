""" trigger/02000486_bf/106_resurrection_2.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[901]):
            return 타임(self.ctx)


class 타임(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=240000):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='RageBuff_3', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 버프_종료(self.ctx)


class 버프_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='RageBuff_3', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


initial_state = 전투시작
