""" trigger/02000066_bf/npc06.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[605])
        self.set_actor(trigger_id=206, initial_sequence='Dead_A')
        self.set_interact_object(trigger_ids=[10000374], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return NPC생성(self.ctx)


class NPC생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.spawn_monster(spawn_ids=[2006], auto_target=False)
        self.set_interact_object(trigger_ids=[10000374], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return NPC생성조건(self.ctx)


class NPC생성조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2006]):
            self.set_effect(trigger_ids=[605], visible=True)
            self.show_guide_summary(entity_id=20000663, text_id=20000663)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.destroy_monster(spawn_ids=[2006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.hide_guide_summary(entity_id=20000663)
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=206, visible=True, initial_sequence='Dead_A')
        self.set_interact_object(trigger_ids=[10000374], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000374], state=0):
            return 부활(self.ctx)


class 부활(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.spawn_monster(spawn_ids=[2006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return NPC대사(self.ctx)


class NPC대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=206, initial_sequence='Dead_A')
        self.set_dialogue(type=1, spawn_id=2006, script='$02000066_BF__NPC06__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2006]):
            return NPC생성조건(self.ctx)


initial_state = 시작
