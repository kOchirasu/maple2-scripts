""" trigger/02000290_bf/npc_07.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001]) # 요미공주음성01
        self.set_effect(trigger_ids=[6002]) # 요미공주음성02
        self.set_interact_object(trigger_ids=[10000464], state=1)
        self.set_actor(trigger_id=9007, visible=True, initial_sequence='Down_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000464], state=0):
            return NPC대사(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=9007, initial_sequence='Down_Idle_A')
        self.set_user_value(trigger_id=9999995, key='dungeonclear', value=1)


class NPC대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[907])
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.set_effect(trigger_ids=[6001], visible=True)
            self.set_dialogue(type=1, spawn_id=907, script='$02000290_BF__NPC_07__0$', time=3)
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=4)
        self.move_npc(spawn_id=907, patrol_name='MS2PatrolData907')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            self.set_effect(trigger_ids=[6002], visible=True)
            self.set_dialogue(type=1, spawn_id=907, script='$02000290_BF__NPC_07__1$', time=3)
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.destroy_monster(spawn_ids=[907])
        pass


initial_state = 시작대기중
