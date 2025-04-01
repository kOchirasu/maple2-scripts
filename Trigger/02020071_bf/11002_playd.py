""" trigger/02020071_bf/11002_playd.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PlayD', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PlayD') == 1:
            return ActorOff(self.ctx)


class ActorOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11002, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell D

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000059], state=0):
            # Bell D
            return ActorOn(self.ctx)
        if self.user_value(key='PlayD') == 0:
            return ResetDelay(self.ctx)


class ActorOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11002, visible=True, initial_sequence='ks_quest_musical_B01_orange') # Bell D

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return ResetDelay(self.ctx)
        if self.user_value(key='PlayD') == 0:
            return ResetDelay(self.ctx)


class ResetDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11002, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell D

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return ActorOff(self.ctx)
        if self.user_value(key='PlayD') == 0:
            return Wait(self.ctx)


initial_state = Wait
