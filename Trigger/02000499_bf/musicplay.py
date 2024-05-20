""" trigger/02000499_bf/musicplay.xml """
import trigger_api


class wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101]) # PlayClarinet
        self.set_effect(trigger_ids=[5103]) # PlayCello
        self.set_effect(trigger_ids=[5102]) # PlayViolin
        self.set_effect(trigger_ids=[5104]) # PlayBox
        self.set_effect(trigger_ids=[5105]) # PlayBox
        self.set_interact_object(trigger_ids=[11000093], state=1)
        self.destroy_monster(spawn_ids=[210])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[11000093], state=0):
            return ready(self.ctx)


# 
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.write_log(log_name='Survival', event='MushkingLand_musicPlay') # 로그
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Play_A', duration=30500.0)
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Play_A', duration=30500.0)
        self.set_npc_emotion_loop(spawn_id=203, sequence_name='Play_A', duration=30500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCPlayMusic02(self.ctx)


class PCPlayMusic02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True) # PlayClarinet
        self.set_effect(trigger_ids=[5103], visible=True) # PlayCello
        self.set_effect(trigger_ids=[5102], visible=True) # PlayViolin
        self.set_effect(trigger_ids=[5104], visible=True) # PlayBox
        self.set_effect(trigger_ids=[5105], visible=True) # PlayBox
        self.spawn_monster(spawn_ids=[210], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Play_A', duration=30500.0)
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Play_A', duration=30500.0)
        self.set_npc_emotion_loop(spawn_id=203, sequence_name='Play_A', duration=30500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30500):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101]) # PlayClarinet
        self.set_effect(trigger_ids=[5103]) # PlayCello
        self.set_effect(trigger_ids=[5102]) # PlayViolin
        self.set_effect(trigger_ids=[5104]) # PlayBox
        self.set_effect(trigger_ids=[5105]) # PlayBox
        self.destroy_monster(spawn_ids=[210])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wait(self.ctx)


initial_state = wait
