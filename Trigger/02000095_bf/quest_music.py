""" trigger/02000095_bf/quest_music.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[101])
        self.set_interact_object(trigger_ids=[10000465], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000465], state=0):
            return NPC대화(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[892])
        self.spawn_monster(spawn_ids=[893])
        self.spawn_monster(spawn_ids=[894])


class NPC대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=892, script='$02000095_BF__QUEST_MUSIC__0$', time=2)
        self.set_dialogue(type=1, spawn_id=893, script='$02000095_BF__QUEST_MUSIC__1$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=894, script='$02000095_BF__QUEST_MUSIC__2$', time=2, arg5=4)
        self.set_timer(timer_id='1', seconds=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[101], visible=True)
        self.destroy_monster(spawn_ids=[892])
        self.destroy_monster(spawn_ids=[893])
        self.destroy_monster(spawn_ids=[894])
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
