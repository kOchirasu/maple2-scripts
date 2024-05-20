""" trigger/02010086_bf/boss_bomb.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=799) >= 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[6001], enable=True)
        self.set_skill(trigger_ids=[6002], enable=True)
        self.set_skill(trigger_ids=[6003], enable=True)
        self.set_skill(trigger_ids=[6004], enable=True)
        self.set_effect(trigger_ids=[6010], visible=True) # 폭발
        self.set_effect(trigger_ids=[6011], visible=True) # 폭발
        self.set_effect(trigger_ids=[6012], visible=True) # 폭발


initial_state = 대기
