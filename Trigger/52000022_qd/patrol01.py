""" trigger/52000022_qd/patrol01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001])
        self.set_effect(trigger_ids=[601])
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.spawn_monster(spawn_ids=[211], auto_target=False)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60001041], quest_states=[1]):
            # 변절자의 흔적 퀘스트 진행 중 상태 연출 및 전투 개시!
            return 연출준비(self.ctx)


# 말풍선 연출 : 이슈라와 추격대원 대화하면서 걷기
class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.destroy_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[211])
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 연출용 이슈라
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 연출용 추격대원

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 말풍선연출01(self.ctx)


class 말풍선연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=1, spawn_id=101, script='$52000022_QD__PATROL01__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 말풍선연출02(self.ctx)


class 말풍선연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=4)
        self.set_dialogue(type=1, spawn_id=201, script='$52000022_QD__PATROL01__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 말풍선연출03(self.ctx)


class 말풍선연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=1, spawn_id=101, script='$52000022_QD__PATROL01__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 이슈라이동(self.ctx)


class 이슈라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 추격대원이동(self.ctx)


class 추격대원이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=1, spawn_id=201, script='$52000022_QD__PATROL01__3$', time=3)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 말풍선연출04(self.ctx)


class 말풍선연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=1, spawn_id=101, script='$52000022_QD__PATROL01__4$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 말풍선연출05(self.ctx)


class 말풍선연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_dialogue(type=1, spawn_id=101, script='$52000022_QD__PATROL01__5$', time=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 말풍선연출06(self.ctx)


class 말풍선연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_dialogue(type=1, spawn_id=101, script='$52000022_QD__PATROL01__6$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 감옥이펙트(self.ctx)


class 감옥이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_mesh(trigger_ids=[3001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 말풍선연출07(self.ctx)


class 말풍선연출07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_dialogue(type=1, spawn_id=201, script='$52000022_QD__PATROL01__7$', time=2)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 말풍선연출08(self.ctx)


class 말풍선연출08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_dialogue(type=1, spawn_id=101, script='$52000022_QD__PATROL01__8$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 몹소환(self.ctx)


class 몹소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52000022_QD__PATROL01__9$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$52000022_QD__PATROL01__10$', time=3)
        self.spawn_monster(spawn_ids=[1001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1001]):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001])
        self.set_timer(timer_id='2', seconds=2)
        self.set_effect(trigger_ids=[601])
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[111], auto_target=False) # 연출용 이슈라
        self.spawn_monster(spawn_ids=[211], auto_target=False) # 연출용 추격대원

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
