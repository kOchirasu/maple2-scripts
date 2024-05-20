""" trigger/02000349_bf/fog.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000813], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=136, spawn_ids=[2006]):
            return 시작대기중(self.ctx)


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1098])
        self.set_effect(trigger_ids=[600]) # fog 500
        self.set_effect(trigger_ids=[602]) # fog 1500
        self.set_interact_object(trigger_ids=[10000813], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1098]):
            return 포그(self.ctx)


class 포그(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.set_interact_object(trigger_ids=[10000813], state=1)
        self.show_guide_summary(entity_id=20003494, text_id=20003494)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000813], state=0):
            return 대기시간(self.ctx)
        if self.monster_dead(spawn_ids=[1099]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20003494)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_interact_object(trigger_ids=[10000813], state=0)
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 시작대기중(self.ctx)


initial_state = 준비
