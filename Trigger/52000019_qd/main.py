""" trigger/52000019_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2002], auto_target=False)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[100], quest_ids=[60001012], quest_states=[1]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2002])
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__0$', time=5)
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=101, spawn_ids=[2001]):
            return 첫번째구덩이도착(self.ctx)


class 첫번째구덩이도착(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 첫번째구덩이(self.ctx)


class 첫번째구덩이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 첫번째꿈틀이(self.ctx)


class 첫번째꿈틀이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__3$', time=3)
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001B')
        self.spawn_monster(spawn_ids=[1001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1001]):
            return 첫번째구덩이완료(self.ctx)


class 첫번째구덩이완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__4$', time=3)
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[2001]):
            return 두번째구덩이시작(self.ctx)


class 두번째구덩이시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__5$', time=5)
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=103, spawn_ids=[2001]):
            return 두번째구덩이도착(self.ctx)


class 두번째구덩이도착(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__6$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 두번째구덩이(self.ctx)


class 두번째구덩이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__7$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 두번째꿈틀이(self.ctx)


class 두번째꿈틀이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__8$', time=3)
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001E')
        self.spawn_monster(spawn_ids=[1002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1002]):
            return 두번째구덩이완료(self.ctx)


class 두번째구덩이완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__9$', time=3)
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001F')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=104, spawn_ids=[2001]):
            return 세번째구덩이시작(self.ctx)


class 세번째구덩이시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__10$', time=5)
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=105, spawn_ids=[2001]):
            return 세번째구덩이도착(self.ctx)


class 세번째구덩이도착(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=4)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__11$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 세번째구덩이(self.ctx)


class 세번째구덩이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__12$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 세번째꿈틀이(self.ctx)


class 세번째꿈틀이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001H')
        self.spawn_monster(spawn_ids=[1003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1003]):
            return 세번째구덩이완료(self.ctx)


class 세번째구덩이완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=1, spawn_id=2001, script='$52000019_QD__MAIN__13$', time=5)
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.spawn_monster(spawn_ids=[2003], auto_target=False)
            self.destroy_monster(spawn_ids=[2001])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
