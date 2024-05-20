""" trigger/02000076_tw_henesysvillage/02_npcbackup01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[1002], quest_ids=[10002041], quest_states=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_21')
        self.set_dialogue(type=1, spawn_id=201, script='$02000076_TW_HenesysVillage__02_NPCBACKUP01__0$', time=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=4001, spawn_ids=[201]):
            return 지원군이동(self.ctx)


class 지원군이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=2001, spawn_ids=[201]):
            return 지원군소멸(self.ctx)


class 지원군소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])
        self.set_timer(timer_id='1', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
