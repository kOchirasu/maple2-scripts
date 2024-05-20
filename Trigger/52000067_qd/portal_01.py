""" trigger/52000067_qd/portal_01.xml """
import trigger_api


# 포탈 파괴 연출
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return portal(self.ctx)


class portal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[803]) # 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[803]):
            return portal_off(self.ctx)


class portal_off(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$52000067_QD__PORTAL_01__0$', time=3)
        self.set_dialogue(type=1, spawn_id=101, script='$52000067_QD__PORTAL_01__1$', time=3, arg5=2)
        self.set_effect(trigger_ids=[7010]) # 다크 포탈
        self.set_effect(trigger_ids=[7110], visible=True) # 다크 포탈 폭발


initial_state = idle
