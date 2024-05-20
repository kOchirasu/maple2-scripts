""" trigger/02000076_tw_henesysvillage/01_npcbackup08.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[1001], quest_ids=[10002041], quest_states=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.move_npc(spawn_id=108, patrol_name='MS2PatrolData_18')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=3008, spawn_ids=[108]):
            return 지원군이동(self.ctx)


class 지원군이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=108, patrol_name='MS2PatrolData_108')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=2001, spawn_ids=[108]):
            return 지원군소멸(self.ctx)


class 지원군소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[108])
        self.set_timer(timer_id='3', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 대기(self.ctx)


initial_state = 대기
