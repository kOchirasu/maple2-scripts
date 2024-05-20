""" trigger/02000533_bf/main2.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703], job_code=0):
            return 서브몬스터1(self.ctx)


class 서브몬스터1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[601,602,607,608,609,610], auto_target=False)
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData_5000')
        self.move_npc(spawn_id=602, patrol_name='MS2PatrolData_5001')
        self.set_npc_emotion_loop(spawn_id=607, sequence_name='Sit_Down_A', duration=10000000.0)
        self.set_npc_emotion_loop(spawn_id=608, sequence_name='Sit_Down_A', duration=10000000.0)
        self.set_npc_emotion_loop(spawn_id=610, sequence_name='Bore_A', duration=10000000.0)
        self.add_balloon_talk(spawn_id=601, msg='$02000533_BF__MAIN2__0$', duration=3500)
        self.add_balloon_talk(spawn_id=602, msg='$02000533_BF__MAIN2__1$', duration=3500, delay_tick=500)
        self.add_balloon_talk(spawn_id=601, msg='$02000533_BF__MAIN2__2$', duration=3500, delay_tick=1500)
        self.add_balloon_talk(spawn_id=607, msg='$02000533_BF__MAIN2__3$', duration=3500, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 서브몬스터2(self.ctx)


class 서브몬스터2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[601,602,607,608,609,610])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 서브몬스터3(self.ctx)


class 서브몬스터3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[6601,6602,6607,6608,6609,6610])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[6601,6602,6607,6608,6609,6610]):
            return None # Missing State: State


initial_state = idle
