""" trigger/63000030_cs/push02.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6107]) # Voice_Junta_00001768
        self.set_effect(trigger_ids=[6006]) # Voice_Tinchai_00001700
        self.set_agent(trigger_ids=[8100])
        self.set_agent(trigger_ids=[8101])
        self.set_agent(trigger_ids=[8102])
        self.set_agent(trigger_ids=[8103])
        self.set_agent(trigger_ids=[8104])
        self.set_agent(trigger_ids=[8105])
        self.set_agent(trigger_ids=[8106])
        self.set_agent(trigger_ids=[8107])
        self.set_agent(trigger_ids=[8108])
        self.set_agent(trigger_ids=[8109])
        self.set_agent(trigger_ids=[8110])
        self.set_agent(trigger_ids=[8111])
        self.set_agent(trigger_ids=[8112])
        self.set_skill(trigger_ids=[7000]) # Push
        self.set_mesh(trigger_ids=[3100]) # Invisible_Barrier
        self.set_user_value(key='PushStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PushStart') == 1:
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100], visible=True) # Invisible_Barrier
        self.set_agent(trigger_ids=[8100], visible=True)
        self.set_agent(trigger_ids=[8101], visible=True)
        self.set_agent(trigger_ids=[8102], visible=True)
        self.set_agent(trigger_ids=[8103], visible=True)
        self.set_agent(trigger_ids=[8104], visible=True)
        self.set_agent(trigger_ids=[8105], visible=True)
        self.set_agent(trigger_ids=[8106], visible=True)
        self.set_agent(trigger_ids=[8107], visible=True)
        self.set_agent(trigger_ids=[8108], visible=True)
        self.set_agent(trigger_ids=[8109], visible=True)
        self.set_agent(trigger_ids=[8110], visible=True)
        self.set_agent(trigger_ids=[8111], visible=True)
        self.set_agent(trigger_ids=[8112], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return Push01(self.ctx)


class Push01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7000], enable=True) # Push

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcTalkRandom(self.ctx)


class NpcTalkRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return JuntaTalk01(self.ctx)
        if self.random_condition(weight=50.0):
            return TinChaiTalk01(self.ctx)


class JuntaTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[6107], visible=True) # Voice_Junta_00001768
        self.set_dialogue(type=2, spawn_id=11001557, script='$63000030_CS__PUSH02__0$', time=5) # 준타 00001768

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Delay01(self.ctx)


class TinChaiTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[6006], visible=True) # Voice_Tinchai_00001700
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000030_CS__PUSH02__1$', time=4) # 틴차이 00001700

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Reset01(self.ctx)


class Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return Push01(self.ctx)


initial_state = Wait
