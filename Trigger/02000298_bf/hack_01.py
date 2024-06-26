""" trigger/02000298_bf/hack_01.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000369], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return 스폰(self.ctx)
        if self.user_detected(box_ids=[107]):
            return 스폰(self.ctx)


class 스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1030], auto_target=False)
        self.set_interact_object(trigger_ids=[10000369], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000369], state=0):
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
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__0$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_1238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__1$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_1358(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__2$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_1489(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__3$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_1567(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__4$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_1679(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__5$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2389(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__6$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2347(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__7$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2478(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__8$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2456(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__9$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2569(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__10$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_2678(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__11$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_3458(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__12$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_3589(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__13$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_3679(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__14$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_3789(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__15$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_4567(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__16$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_4578(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__17$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_4689(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__18$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 코드_4789(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000298_BF__HACK_01__19$', duration=2000)

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
