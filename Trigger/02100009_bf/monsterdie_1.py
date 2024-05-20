""" trigger/02100009_bf/monsterdie_1.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1000049])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[100000001]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[100000002], skill_id=50000217, level=1, is_skill_set=False)
        self.set_skill(trigger_ids=[1000049], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            pass


initial_state = 유저감지
