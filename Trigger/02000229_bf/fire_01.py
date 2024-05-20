""" trigger/02000229_bf/fire_01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000051], state=1)
        self.set_effect(trigger_ids=[501])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000051], state=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 딜레이(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[501], visible=True)
        self.spawn_monster(spawn_ids=[101])


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000229_BF__FIRE_01__0$', time=2)
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 딜레이2(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[501])
        self.destroy_monster(spawn_ids=[101])


class 딜레이2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
