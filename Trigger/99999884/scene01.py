""" trigger/99999884/scene01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # for test
        # self.spawn_monster(spawn_ids=[201])
        self.set_effect(trigger_ids=[401])
        self.set_effect(trigger_ids=[402])
        self.set_effect(trigger_ids=[403])
        self.set_effect(trigger_ids=[404])
        self.set_actor(trigger_id=405)
        self.set_effect(trigger_ids=[406])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            # for test
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라등장(self.ctx)


class 벨라등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202])
        self.set_effect(trigger_ids=[401], visible=True)
        self.set_timer(timer_id='1', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사1(self.ctx)


class 벨라대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[401])
        self.set_timer(timer_id='1', seconds=2)
        self.set_dialogue(type=2, spawn_id=11000057, script='$99999884__SCENE01__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사2(self.ctx)


class 벨라대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_dialogue(type=1, spawn_id=202, script='$99999884__SCENE01__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 프레이와오스칼등장(self.ctx)


class 프레이와오스칼등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[204])
        self.set_effect(trigger_ids=[402], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 프레이대사1(self.ctx)


class 프레이대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_dialogue(type=2, spawn_id=11000119, script='$99999884__SCENE01__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사3(self.ctx)


class 벨라대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_effect(trigger_ids=[402])
        self.move_npc(spawn_id=202, patrol_name='202_MS2PatrolData_Bella_TurnToFrey')
        self.set_dialogue(type=1, spawn_id=202, script='$99999884__SCENE01__3$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사4(self.ctx)


class 벨라대사4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.move_npc(spawn_id=202, patrol_name='202_MS2PatrolData_Bella_TurnToDevorak')
        self.set_dialogue(type=1, spawn_id=202, script='$99999884__SCENE01__4$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 이펙트지연(self.ctx)


class 이펙트지연(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_effect(trigger_ids=[402], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 프레이대사2(self.ctx)


class 프레이대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.move_npc(spawn_id=203, patrol_name='203_MS2PatrolData_Frey_MoveToBella')
        self.set_dialogue(type=1, spawn_id=203, script='$99999884__SCENE01__5$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사5(self.ctx)


class 벨라대사5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_effect(trigger_ids=[402])
        self.set_effect(trigger_ids=[403], visible=True)
        self.move_npc(spawn_id=202, patrol_name='202_MS2PatrolData_Bella_TurnToFrey')
        self.set_dialogue(type=1, spawn_id=202, script='$99999884__SCENE01__6$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 프레이피격(self.ctx)


class 프레이피격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.move_npc(spawn_id=203, patrol_name='203_MS2PatrolData_Frey_HitByBella')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 오스칼대사1(self.ctx)


class 오스칼대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.destroy_monster(spawn_ids=[203])
        self.set_effect(trigger_ids=[403])
        self.set_effect(trigger_ids=[406], visible=True)
        self.set_actor(trigger_id=405, visible=True, initial_sequence='Down_Idle_A')
        self.move_npc(spawn_id=204, patrol_name='204_MS2PatrolData_Oskhal_MoveToFrey')
        self.set_dialogue(type=2, spawn_id=11000015, script='$99999884__SCENE01__7$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 오스칼대사2(self.ctx)


class 오스칼대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_dialogue(type=1, spawn_id=204, script='$99999884__SCENE01__8$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 오스칼돌격(self.ctx)


class 오스칼돌격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.move_npc(spawn_id=204, patrol_name='204_MS2PatrolData_Oskhal_MoveToBella')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(path_ids=[302])
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    pass


initial_state = 시작대기중
