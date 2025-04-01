""" trigger/82000006_survival/04_invincible.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return MakeInvincible(self.ctx)


class MakeInvincible(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9000], skill_id=71000049, level=1, ignore_player=False, is_skill_set=False) # 대기공간 무적

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return MakeInvincible(self.ctx)
        if self.user_value(key='InvincibleOff') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
