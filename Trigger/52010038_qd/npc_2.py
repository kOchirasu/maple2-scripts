""" trigger/52010038_qd/npc_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6202])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GaugeStart') == 1:
            return npc체크(self.ctx)


class npc체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[1802]):
            return 이펙트(self.ctx)
        if not self.monster_in_combat(spawn_ids=[1802]):
            return 생성(self.ctx)
        if self.user_value(key='GaugeClosed') == 1:
            return 종료(self.ctx)


class 이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6202], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.monster_in_combat(spawn_ids=[1802]):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6202])
        self.init_npc_rotation(spawn_ids=[1802])
        self.spawn_monster(spawn_ids=[4000], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return npc체크(self.ctx)
        if self.user_value(key='GaugeClosed') == 1:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
