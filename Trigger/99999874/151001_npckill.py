""" trigger/99999874/151001_npckill.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NPCKill') == 1:
            return NPCKillWait(self.ctx)


class NPCKillWait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7500):
            return NPCKill(self.ctx)


class NPCKill(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[15401,15402,15501,15502])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return KillEnd(self.ctx)


class KillEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=151001, key='NPCKill', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
