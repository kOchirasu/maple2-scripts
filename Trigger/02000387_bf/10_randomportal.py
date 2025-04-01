""" trigger/02000387_bf/10_randomportal.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2011,2012,2013,2014], visible=True) # DoorMesh_AlwaysOn
        self.set_effect(trigger_ids=[5001]) # FrontDoorStep
        self.set_effect(trigger_ids=[5002]) # FrontDoorStep
        self.set_effect(trigger_ids=[5003]) # FrontDoorStep
        self.set_effect(trigger_ids=[5004]) # FrontDoorStep
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=12)
        self.set_portal(portal_id=13)
        self.set_portal(portal_id=14)
        self.set_portal(portal_id=21)
        self.set_portal(portal_id=22)
        self.set_portal(portal_id=23)
        self.set_portal(portal_id=24)
        self.set_actor(trigger_id=4101, visible=True, initial_sequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(trigger_id=4102, visible=True, initial_sequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(trigger_id=4103, visible=True, initial_sequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(trigger_id=4104, visible=True, initial_sequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_user_value(key='RandomPortalOn', value=0)
        self.set_user_value(key='CounterDoorPick', value=0)
        self.set_user_value(key='DungeonClear', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RandomPortalOn') == 1:
            return Guide01(self.ctx)


class Guide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000387_BF__10_RANDOMPORTAL__0$', duration=3000, box_ids=['0'])
        self.set_effect(trigger_ids=[5001], visible=True) # FrontDoorStep
        self.set_effect(trigger_ids=[5002], visible=True) # FrontDoorStep
        self.set_effect(trigger_ids=[5003], visible=True) # FrontDoorStep
        self.set_effect(trigger_ids=[5004], visible=True) # FrontDoorStep

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckMember01(self.ctx)


class CheckMember01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) == 1:
            # 1인용 테스트 임시
            # 1인용 테스트 임시
            return CheckMember02(self.ctx) # CheckMember02


class CheckMember02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) != 1:
            return CheckMember01(self.ctx)
        if self.count_users(box_id=9002) == 1:
            return CheckMember03(self.ctx)


class CheckMember03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) != 1:
            return CheckMember01(self.ctx)
        if self.count_users(box_id=9002) != 1:
            return CheckMember01(self.ctx)
        if self.count_users(box_id=9003) == 1:
            return CheckMember04(self.ctx)


class CheckMember04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) != 1:
            return CheckMember01(self.ctx)
        if self.count_users(box_id=9002) != 1:
            return CheckMember01(self.ctx)
        if self.count_users(box_id=9003) != 1:
            return CheckMember01(self.ctx)
        if self.count_users(box_id=9004) == 1:
            return DoorActivate01(self.ctx)


class DoorActivate01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return DoorActivate02(self.ctx)


class DoorActivate02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4101, visible=True, initial_sequence='ry_functobj_door_B01_on') # OfficeDoor
        self.set_actor(trigger_id=4102, visible=True, initial_sequence='ry_functobj_door_B01_on') # OfficeDoor
        self.set_actor(trigger_id=4103, visible=True, initial_sequence='ry_functobj_door_B01_on') # OfficeDoor
        self.set_actor(trigger_id=4104, visible=True, initial_sequence='ry_functobj_door_B01_on') # OfficeDoor

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PickPortalPattern(self.ctx)


# 4개의 문 중에서 하나만 카운터로
class PickPortalPattern(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return FirstDoorPick(self.ctx)
        if self.random_condition(weight=25.0):
            return SecondDoorPick(self.ctx)
        if self.random_condition(weight=25.0):
            return ThirdDoorPick(self.ctx)
        if self.random_condition(weight=25.0):
            return rdDoorPick4(self.ctx)


class FirstDoorPick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11, enable=True)
        self.set_portal(portal_id=22, enable=True)
        self.set_portal(portal_id=23, enable=True)
        self.set_portal(portal_id=24, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GameStart00(self.ctx)


class SecondDoorPick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=12, enable=True)
        self.set_portal(portal_id=21, enable=True)
        self.set_portal(portal_id=23, enable=True)
        self.set_portal(portal_id=24, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GameStart00(self.ctx)


class ThirdDoorPick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=13, enable=True)
        self.set_portal(portal_id=21, enable=True)
        self.set_portal(portal_id=22, enable=True)
        self.set_portal(portal_id=24, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GameStart00(self.ctx)


class rdDoorPick4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=14, enable=True)
        self.set_portal(portal_id=21, enable=True)
        self.set_portal(portal_id=22, enable=True)
        self.set_portal(portal_id=23, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GameStart00(self.ctx)


class GameStart00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9800) == 4:
            # InTheStore
            return GameStart01(self.ctx)
        if self.count_users(box_id=9800) < 4:
            # InTheStore
            return GameStartDelay01(self.ctx)


class GameStartDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GameStart01(self.ctx)


class GameStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=12)
        self.set_portal(portal_id=13)
        self.set_portal(portal_id=14)
        self.set_portal(portal_id=21)
        self.set_portal(portal_id=22)
        self.set_portal(portal_id=23)
        self.set_portal(portal_id=24)
        self.set_actor(trigger_id=4101, visible=True, initial_sequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(trigger_id=4102, visible=True, initial_sequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(trigger_id=4103, visible=True, initial_sequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(trigger_id=4104, visible=True, initial_sequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_effect(trigger_ids=[5001]) # FrontDoorStep
        self.set_effect(trigger_ids=[5002]) # FrontDoorStep
        self.set_effect(trigger_ids=[5003]) # FrontDoorStep
        self.set_effect(trigger_ids=[5004]) # FrontDoorStep

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9005) == 1:
            # 카운터 1명
            return GameStart02(self.ctx) # 1인 테스트용 임시
        if self.count_users(box_id=9900) < 4:
            return EndGame01(self.ctx)


class GameStart02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9006) == 3:
            return secondsWait10(self.ctx)
        if self.count_users(box_id=9900) < 4:
            return EndGame01(self.ctx)


class secondsWait10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonClear') == 1:
            return Quit(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return CheckMemeberAgain(self.ctx) # 1인 테스트용 임시


class CheckMemeberAgain(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9900) == 4:
            return secondsWait10(self.ctx)
        if self.count_users(box_id=9900) < 4:
            return EndGame01(self.ctx)
        if self.user_value(key='DungeonClear') == 1:
            return Quit(self.ctx)


class EndGame01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000387_BF__10_RANDOMPORTAL__1$', duration=3000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return PCMoveOut01(self.ctx)
        if self.user_value(key='DungeonClear') == 1:
            return Quit(self.ctx)


class PCMoveOut01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000387, portal_id=1, box_id=9900) # 사무실로 강제 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FieredNotice01(self.ctx)


class FieredNotice01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000491, script='$02000387_BF__10_RANDOMPORTAL__2$', time=4)
        self.set_skip(state=FieredNotice01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FieredNotice01Skip(self.ctx)


class FieredNotice01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FieredNotice02(self.ctx)


class FieredNotice02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000491, script='$02000387_BF__10_RANDOMPORTAL__3$', time=4)
        self.set_skip(state=FieredNotice02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FieredNotice02Skip(self.ctx)


class FieredNotice02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCForceToLeave(self.ctx)


class PCForceToLeave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[100])


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
