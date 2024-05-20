""" trigger/52010015_qd/act01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002824], quest_states=[2]):
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='100', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='100'):
            return 미카교체01(self.ctx)


# 1st Quest
class 미카교체01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 미카이동01(self.ctx)


class 미카이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_2020')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8000, spawn_ids=[202]):
            return 미카소멸01(self.ctx)


class 미카소멸01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202])


initial_state = 대기
