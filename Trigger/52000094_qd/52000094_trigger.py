""" trigger/52000094_qd/52000094_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3003,3004])
        self.destroy_monster(spawn_ids=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9100], quest_ids=[50100500], quest_states=[1]):
            return 진행중일때20002275(self.ctx)
        if self.quest_user_detected(box_ids=[9100], quest_ids=[20002275], quest_states=[1]):
            return 진행중일때20002275(self.ctx)


class 진행중일때20002275(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터들이 소환된다
        self.spawn_monster(spawn_ids=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009], auto_target=False) # ,90537,90539

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]):
            return 진행중일때20002275(self.ctx)


initial_state = 대기
