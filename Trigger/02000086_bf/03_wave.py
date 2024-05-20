""" trigger/02000086_bf/03_wave.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000159], state=1)
        self.set_effect(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326])
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226])
        self.set_actor(trigger_id=501, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=502, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=503, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=504, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=505, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=506, visible=True, initial_sequence='Closed')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000159], state=0):
            return 딜레이1(self.ctx)


class 딜레이1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326], visible=True)
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226], visible=True)
        self.set_timer(timer_id='3', seconds=2)
        self.set_actor(trigger_id=501, visible=True, initial_sequence='Opened')
        self.set_actor(trigger_id=502, visible=True, initial_sequence='Opened')
        self.set_actor(trigger_id=503, visible=True, initial_sequence='Opened')
        self.set_actor(trigger_id=504, visible=True, initial_sequence='Opened')
        self.set_actor(trigger_id=505, visible=True, initial_sequence='Opened')
        self.set_actor(trigger_id=506, visible=True, initial_sequence='Opened')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 웨이브1(self.ctx)


class 웨이브1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000086_BF__03_WAVE__0$', arg3='3000', arg4='401')
        self.spawn_monster(spawn_ids=[101,102,103,104,105,106], auto_target=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_601')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_602')
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_603')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_604')
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_605')
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_606')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104,105,106]):
            return 대기(self.ctx)


class 딜레이2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 웨이브2(self.ctx)


class 웨이브2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103,104,105,106])
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_601')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_602')
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_603')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_604')
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_605')
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_606')
        self.set_timer(timer_id='3', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104,105,106]):
            return 딜레이4(self.ctx)
        if self.time_expired(timer_id='3'):
            return 대기(self.ctx)


class 딜레이3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 웨이브3(self.ctx)


class 웨이브3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000086_BF__03_WAVE__1$', arg3='3000', arg4='401')
        self.spawn_monster(spawn_ids=[101,102,103,104,105,106])
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_601')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_602')
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_603')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_604')
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_605')
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_606')
        self.set_timer(timer_id='3', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104,105,106]):
            return 딜레이4(self.ctx)
        if self.time_expired(timer_id='3'):
            return 대기(self.ctx)


class 딜레이4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 딜레이5(self.ctx)


class 딜레이5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000159], state=1)
        self.set_effect(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326])
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226])
        self.set_actor(trigger_id=501, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=502, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=503, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=504, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=505, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=506, visible=True, initial_sequence='Closed')
        self.set_timer(timer_id='3', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 딜레이6(self.ctx)


class 딜레이6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 대기(self.ctx)


initial_state = 대기
