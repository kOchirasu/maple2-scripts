""" trigger/02000298_bf/hack_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000370], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[116]):
            return 스폰(self.ctx)


class 스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1032], auto_target=False)
        self.set_interact_object(trigger_ids=[10000370], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000370], state=0):
            return 코드체크(self.ctx)


class 코드체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=197, spawn_ids=[1279]):
            return 코드_1279(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[1238]):
            return 코드_1238(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[1358]):
            return 코드_1358(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[1489]):
            return 코드_1489(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[1567]):
            return 코드_1567(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[1679]):
            return 코드_1679(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2389]):
            return 코드_2389(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2347]):
            return 코드_2347(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2478]):
            return 코드_2478(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2456]):
            return 코드_2456(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2569]):
            return 코드_2569(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[2678]):
            return 코드_2678(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[3458]):
            return 코드_3458(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[3589]):
            return 코드_3589(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[3679]):
            return 코드_3679(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[3789]):
            return 코드_3789(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[4567]):
            return 코드_4567(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[4578]):
            return 코드_4578(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[4689]):
            return 코드_4689(self.ctx)
        if self.npc_detected(box_id=197, spawn_ids=[4789]):
            return 코드_4789(self.ctx)


class 코드_1279(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__0$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_1238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__1$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_1358(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__2$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_1489(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__3$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_1567(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__4$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_1679(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__5$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2389(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__6$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2347(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__7$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2478(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__8$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2456(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__9$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2569(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__10$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2678(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__11$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_3458(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__12$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_3589(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__13$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_3679(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__14$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_3789(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__15$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_4567(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__16$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_4578(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__17$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_4689(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__18$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_4789(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui(type=1, arg2='$02000298_BF__HACK_02__19$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
