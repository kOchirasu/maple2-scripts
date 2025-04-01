""" trigger/02100004_bf/achieve_tentomanfight.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='LastRoundStart', value=0)
        self.set_user_value(key='LastRoundEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='LastRoundStart') == 1:
            return MobCheck01(self.ctx)


class MobCheck01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[2000]):
            # 아마돈 등장
            return MobCheck02(self.ctx)


class MobCheck02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=102, spawn_ids=[2001]) and not self.npc_detected(box_id=102, spawn_ids=[2002]) and not self.npc_detected(box_id=102, spawn_ids=[2003]) and not self.npc_detected(box_id=102, spawn_ids=[2004]) and not self.npc_detected(box_id=102, spawn_ids=[2005]) and not self.npc_detected(box_id=102, spawn_ids=[2006]) and not self.npc_detected(box_id=102, spawn_ids=[2008]) and not self.npc_detected(box_id=102, spawn_ids=[2009]) and not self.npc_detected(box_id=102, spawn_ids=[2010]) and not self.npc_detected(box_id=102, spawn_ids=[2011]) and not self.npc_detected(box_id=102, spawn_ids=[2012]) and not self.npc_detected(box_id=102, spawn_ids=[2013]):
            return CheckSuccess(self.ctx)
        if self.user_value(key='LastRoundEnd') == 1:
            return Quit(self.ctx)


class CheckSuccess(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2000]):
            return MemberCheck(self.ctx)
        if self.user_value(key='LastRoundEnd') == 1:
            return Quit(self.ctx)


class MemberCheck(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=102) == 10:
            # 10명 체크
            return Achieve(self.ctx)
        if self.user_value(key='LastRoundEnd') == 1:
            return Quit(self.ctx)


class Achieve(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=102, type='trigger', achieve='TenToOneFight')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
