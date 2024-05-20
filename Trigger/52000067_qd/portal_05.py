""" trigger/52000067_qd/portal_05.xml """
import trigger_api


# 포탈 파괴 연출
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return portal(self.ctx)


class portal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[802]) # 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[802]):
            return portal_off(self.ctx)


class portal_off(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7014]) # 다크 포탈
        self.set_effect(trigger_ids=[7114], visible=True) # 다크 포탈 폭발


initial_state = idle
