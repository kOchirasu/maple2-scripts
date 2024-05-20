""" trigger/02020112_bf/safezone1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990002, key='Safe', value=0)
        self.set_interact_object(trigger_ids=[10002117], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902], job_code=0):
            return 감지(self.ctx)


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103]):
            return 안전장치_활성화(self.ctx)


class 안전장치_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002117], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002117], state=0):
            return 안전장치_작동(self.ctx)


class 안전장치_작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020112_BF__SAFEZONE1__0$', arg3='5000')
        self.set_user_value(trigger_id=99990002, key='Safe', value=1)


initial_state = 대기
