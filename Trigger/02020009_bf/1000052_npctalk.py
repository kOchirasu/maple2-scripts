""" trigger/02020009_bf/1000052_npctalk.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NPCTalk') == 1:
            return NPCTalkOnWait(self.ctx)


class NPCTalkOnWait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return NPCTalkOn(self.ctx)


class NPCTalkOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=15501, msg='$02020009_BF__1000052_NPCTALK__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TalkDelay(self.ctx)


class TalkDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=17000):
            return NPCTalkOn(self.ctx)
        if self.user_value(key='NPCTalk') == 0:
            return None # Missing State: NPCTalkOff


class PortalOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=15501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
