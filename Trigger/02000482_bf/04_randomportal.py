""" trigger/02000482_bf/04_randomportal.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002035], state=0) # ToWall_True
        self.set_interact_object(trigger_ids=[10002036], state=0) # ToRoom_True
        self.set_interact_object(trigger_ids=[10002037], state=0) # ToTower_True
        self.set_mesh(trigger_ids=[3200], visible=True) # CurtainBarrier
        self.set_mesh(trigger_ids=[3201,3202], visible=True) # CurtainOpen
        self.set_mesh(trigger_ids=[3300], visible=True) # ToTowerDoorBarrier
        self.set_effect(trigger_ids=[5000]) # DoorOpen
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Closed') # NextMap
        self.set_portal(portal_id=10) # ToWall
        self.set_portal(portal_id=20) # ToRoom
        self.set_portal(portal_id=30) # ToTower
        self.set_user_value(key='SearchStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SearchStart') == 1:
            return PickRandomPortal(self.ctx)


# 3개의 문 중에서 하나 뽑기
class PickRandomPortal(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30.0):
            return ToWall01(self.ctx)
        if self.random_condition(weight=30.0):
            return ToRoom01(self.ctx)
        if self.random_condition(weight=30.0):
            return ToTower01(self.ctx)


# 테라스로 나가서 성 외벽으로
class ToWall01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002035], state=1) # ToWall_True
        self.set_user_value(trigger_id=6, key='ToRoomFalse', value=1) # ToRoom_False
        self.set_user_value(trigger_id=7, key='ToTowerFalse', value=1) # ToTowerFalse

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002035], state=0):
            return ToWall02(self.ctx)


class ToWall02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3200]) # CurtainBarrier
        self.set_mesh(trigger_ids=[3201,3202], fade=3.0) # CurtainOpen
        self.set_portal(portal_id=10, visible=True, enable=True) # ToWall
        self.set_event_ui_script(type=BannerType.Text, script='$02000482_BF__04_RANDOMPORTAL__0$', duration=2000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ToWallGuide01(self.ctx)


class ToWallGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000006, script='$02000482_BF__04_RANDOMPORTAL__1$', time=5) # 블랙아이
        self.set_skip(state=ToWallGuide01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ToWallGuide01Skip(self.ctx)


class ToWallGuide01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


# 문을 통해 다른 방으로
class ToRoom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002036], state=1) # ToRoom_True
        self.set_user_value(trigger_id=5, key='ToWallFalse', value=1) # ToWall_False
        self.set_user_value(trigger_id=7, key='ToTowerFalse', value=1) # ToTowerFalse

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002036], state=0):
            return ToRoom02(self.ctx)


class ToRoom02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000482_BF__04_RANDOMPORTAL__2$', duration=2000, box_ids=['0'])
        self.set_portal(portal_id=20, visible=True, enable=True) # ToRoom

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ToRoomGuide01(self.ctx)


class ToRoomGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000006, script='$02000482_BF__04_RANDOMPORTAL__3$', time=5) # 블랙아이
        self.set_skip(state=ToRoomGuide01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ToRoomGuide01Skip(self.ctx)


class ToRoomGuide01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


# 계단을 통해 탑으로
class ToTower01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=5, key='ToWallFalse', value=1) # ToWall_False
        self.set_user_value(trigger_id=6, key='ToRoomFalse', value=1) # ToRoom_False
        self.set_interact_object(trigger_ids=[10002037], state=1) # ToTower_True

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002037], state=0):
            return ToTower02(self.ctx)


class ToTower02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000482_BF__04_RANDOMPORTAL__4$', duration=2000, box_ids=['0'])
        self.set_mesh(trigger_ids=[3300]) # ToTowerDoorBarrier
        self.set_effect(trigger_ids=[5000], visible=True) # DoorOpen
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Opened') # NextMap
        self.set_portal(portal_id=30, visible=True, enable=True) # ToTower

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ToTowerGuide01(self.ctx)


class ToTowerGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000006, script='$02000482_BF__04_RANDOMPORTAL__5$', time=5) # 블랙아이
        self.set_skip(state=ToTowerGuide01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ToTowerGuide01Skip(self.ctx)


class ToTowerGuide01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='FindWay', value=1)


initial_state = Wait
