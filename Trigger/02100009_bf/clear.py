""" trigger/02100009_bf/clear.xml """
import trigger_api


class 끝1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1000049])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 끝2(self.ctx)


"""
class 끝2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=100000001, is_relative=True) <= 5:
            return 끝3(self.ctx)
"""

class 끝2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=100000001, is_relative=True) <= 5 and self.npc_hp(spawn_id=100000002, is_relative=True) <= 5:
            return 끝3(self.ctx)


class 끝3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[100000002], skill_id=50000217, level=1, is_skill_set=False)
        self.set_skill(trigger_ids=[1000049], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            pass


initial_state = 끝1
