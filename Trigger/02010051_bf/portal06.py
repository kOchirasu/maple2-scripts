""" trigger/02010051_bf/portal06.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[900])
        self.set_mesh(trigger_ids=[1501,1502,1503,1504,1505,1506], visible=True) # Gate Close grating
        self.set_mesh(trigger_ids=[1511,1512,1513]) # Gate Open grating
        self.set_effect(trigger_ids=[914]) # light
        self.set_interact_object(trigger_ids=[10000914], state=0)
        self.set_mesh(trigger_ids=[1601,1602,1603,1604,1605,1606], visible=True) # grating
        self.set_effect(trigger_ids=[6000]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[6001]) # vibrate
        self.set_effect(trigger_ids=[6002]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[6003]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[6005]) # MainGateOpen vibrate
        self.set_portal(portal_id=10)
        self.set_portal(portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return 입장딜레이01(self.ctx)


class 입장딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대화연출준비01(self.ctx)


class 대화연출준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 연출대화01(self.ctx)


class 연출대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=3)
        self.set_dialogue(type=2, spawn_id=11001319, script='$02010051_BF__PORTAL06__0$', time=3)
        self.set_skip(state=연출대화02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 연출대화02대기(self.ctx)


class 연출대화02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 연출대화02(self.ctx)


class 연출대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=4)
        self.set_dialogue(type=2, spawn_id=11001319, script='$02010051_BF__PORTAL06__1$', time=3)
        self.set_skip(state=대화연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 대화연출종료01(self.ctx)


class 대화연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 문열기01(self.ctx)


class 문열기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[6005], visible=True) # MainGateOpen vibrate
        self.set_mesh(trigger_ids=[1501,1502,1503,1504,1505,1506], fade=10.0) # Gate Close grating
        self.set_mesh(trigger_ids=[1511,1512,1513], visible=True, start_delay=1) # Gate Open grating

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 유저입장01(self.ctx)


class 유저입장01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 가이드준비(self.ctx)


class 가이드준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=7) # VoicePlay

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 가이드시작(self.ctx)


class 가이드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20105101, text_id=20105101, duration=4000) # 길 찾기
        self.set_interact_object(trigger_ids=[10000914], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000914], state=0):
            return 포털개방01(self.ctx)


class 포털개방01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=1)
        self.set_effect(trigger_ids=[914], visible=True) # light
        self.set_effect(trigger_ids=[6000], visible=True) # DoorOpen vibrate
        self.set_mesh(trigger_ids=[1601,1602,1603,1604,1605,1606], fade=10.0) # grating

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 포털개방02(self.ctx)


class 포털개방02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=11, visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000835], state=0):
            return 포털폐쇄(self.ctx)


class 포털폐쇄(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10)
        self.set_portal(portal_id=11)
        self.set_mesh(trigger_ids=[1601,1602,1603,1604,1605,1606], visible=True, fade=2.0) # grating
        self.set_effect(trigger_ids=[6000]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[6005]) # MainGateOpen vibrate


initial_state = 대기
