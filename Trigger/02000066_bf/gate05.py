""" trigger/02000066_bf/gate05.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[3005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604])
        self.set_interact_object(trigger_ids=[10000337], state=0)
        self.spawn_monster(spawn_ids=[3005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3005]):
            return 게이트열림(self.ctx)


class 게이트열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_interact_object(trigger_ids=[10000337], state=1)
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_guide_summary(entity_id=20000664, text_id=20000664)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.hide_guide_summary(entity_id=20000664)
            return 게이트닫힘(self.ctx)


class 게이트닫힘(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000337], state=0):
            return 생성(self.ctx)


initial_state = 시작
