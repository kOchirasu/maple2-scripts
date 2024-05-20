""" trigger/02010051_bf/portal02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=30)
        self.set_portal(portal_id=31)
        self.set_effect(trigger_ids=[836]) # light
        self.set_effect(trigger_ids=[6000]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[6001]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[6002]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[6003]) # DoorOpen vibrate
        self.set_mesh(trigger_ids=[1201,1202,1203,1204,1205,1206], visible=True) # grating
        self.set_mesh(trigger_ids=[12001,12002,12003,12004,12005,12006,12007,12008,12009,12010,12011,12012,12013,12014,12015,12016,12017,12018,12019,12020,12021,12022,12023,12024,12025,12026,12027,12028], visible=True)
        self.set_interact_object(trigger_ids=[10000836], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9011]):
            return 입장딜레이01(self.ctx)


class 입장딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 가이드준비01(self.ctx)


class 가이드준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20105101, text_id=20105101, duration=4000) # 길 찾기

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000836], state=0):
            return 포털개방01(self.ctx)


class 포털개방01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=1)
        self.set_effect(trigger_ids=[836], visible=True) # light
        self.set_effect(trigger_ids=[6002], visible=True) # vibrate
        self.set_mesh(trigger_ids=[1201,1202,1203,1204,1205,1206], fade=10.0) # grating
        self.set_mesh(trigger_ids=[12001,12002,12003,12004,12005,12006,12007,12008,12009,12010,12011,12012,12013,12014,12015,12016,12017,12018,12019,12020,12021,12022,12023,12024,12025,12026,12027,12028])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 포털개방02(self.ctx)


class 포털개방02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=30, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=31, visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000837], state=0):
            return 포털폐쇄(self.ctx)


class 포털폐쇄(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=30)
        self.set_portal(portal_id=31)
        self.set_mesh(trigger_ids=[1201,1202,1203,1204,1205,1206], visible=True, fade=2.0) # grating
        self.set_effect(trigger_ids=[6002]) # vibrate


initial_state = 대기
