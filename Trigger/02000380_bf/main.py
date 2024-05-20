""" trigger/02000380_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001064], state=2)
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='ry_functobj_door_A01_Off')
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='ry_functobj_door_A01_On')
        self.set_actor(trigger_id=4007, visible=True, initial_sequence='ry_functobj_door_A01_On')
        self.set_mesh(trigger_ids=[2001,2002,2003,2004], visible=True)
        self.set_mesh(trigger_ids=[2005,2006,2007,2008])
        self.set_mesh(trigger_ids=[2010,2011,2012], visible=True)
        self.set_mesh(trigger_ids=[2020,2021,2022,2023], visible=True)
        self.set_portal(portal_id=13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2001,2002,2003,2004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8001,8002,8003])
        self.spawn_monster(spawn_ids=[101])
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__0$', time=3)
        self.set_dialogue(type=2, spawn_id=11001836, script='$02000380_BF__MAIN__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Start_02(self.ctx)


class Start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__2$', time=3)
        self.set_dialogue(type=2, spawn_id=11001836, script='$02000380_BF__MAIN__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Start_03(self.ctx)


class Start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Start_03_02(self.ctx)


class Start_03_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003801, text_id=20003801, duration=5000)
        self.set_mesh(trigger_ids=[2001,2002,2003,2004], interval=10, fade=10.0)
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__4$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Start_04(self.ctx)


class Start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[101]):
            return Start_05(self.ctx)


class Start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__5$', time=3)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Start_06(self.ctx)


class Start_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__6$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Start_07(self.ctx)


class Start_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__7$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Start_08(self.ctx)


class Start_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=110, text_id=40009, duration=5000) # 포탈 이용하세요
        self.set_mesh(trigger_ids=[2010,2011,2012], interval=10, fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.random_condition(weight=33.0):
            return Portal_11(self.ctx)
        """
        if self.random_condition(weight=33.0):
            return Portal_10(self.ctx)


class Portal_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='ry_functobj_door_A01_On')
        self.set_portal(portal_id=10, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Start_09(self.ctx)


class Portal_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='ry_functobj_door_A01_On')
        self.set_portal(portal_id=11, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Start_09(self.ctx)


class Portal_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='ry_functobj_door_A01_On')
        self.set_portal(portal_id=12, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Start_09(self.ctx)


class Start_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__8$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if not self.user_detected(box_ids=[710]):
            return Start_09_02(self.ctx)
        """
        if self.dungeon_variable(var_id=1) == 1:
            # 1번 던전이 클리어 됐다면?
            return Start_09_02(self.ctx)

    def on_exit(self) -> None:
        # self.set_mesh(trigger_ids=[2005,2006,2007,2008], visible=True)
        pass


class Start_09_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return Round_2_03(self.ctx)

    def on_exit(self) -> None:
        # 한명이라도 2라운드 지역으로 이동하면 포탈 셋팅 변경
        self.set_mesh(trigger_ids=[2005,2006,2007,2008], fade=10.0)
        self.set_portal(portal_id=10)
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=12)
        self.set_portal(portal_id=13, visible=True)


class Round_2_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Round_2_03(self.ctx)


class Round_2_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__9$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round_2_04(self.ctx)


class Round_2_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2205')
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__10$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Round_2_05(self.ctx)


class Round_2_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__11$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round_2_06(self.ctx)


class Round_2_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2207')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=705, spawn_ids=[101]):
            return Round_2_08(self.ctx)


"""
class Round_2_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2013,2014,2015], interval=10, fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Round_2_08(self.ctx)
"""

class Round_2_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2208')
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__12$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round_2_09(self.ctx)


class Round_2_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__13$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round_2_10(self.ctx)


class Round_2_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=110, text_id=40009, duration=5000) # 포탈 이용하세요
        self.set_mesh(trigger_ids=[2013,2014,2015], interval=10, fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Portal_22(self.ctx)


class Portal_21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='ry_functobj_door_A01_On')
        self.set_portal(portal_id=21, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Round_2_11(self.ctx)


class Portal_22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='ry_functobj_door_A01_On')
        self.set_portal(portal_id=22, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Round_2_11(self.ctx)


class Round_2_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__14$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if not self.user_detected(box_ids=[710]):
            return Round_2_12(self.ctx)
        """
        if self.dungeon_variable(var_id=2) == 1:
            # 2번 던전이 클리어 됐다면?
            return Round_2_12(self.ctx)

    def on_exit(self) -> None:
        # self.set_mesh(trigger_ids=[2005,2006,2007,2008], visible=True)
        pass


class Round_2_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return Round_3_02(self.ctx)

    def on_exit(self) -> None:
        # 한명이라도 3라운드 지역으로 이동하면 포탈 셋팅 변경
        self.set_mesh(trigger_ids=[2005,2006,2007,2008], fade=10.0)
        self.set_portal(portal_id=21)
        self.set_portal(portal_id=22)
        self.set_portal(portal_id=23, visible=True)


"""
class Round_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=708) >= 1:
            return Round_3_02(self.ctx)
"""

class Round_3_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2208')
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__15$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round_3_03(self.ctx)


class Round_3_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2208')
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__16$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=706, spawn_ids=[101]):
            return Round_3_04(self.ctx)


class Round_3_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000380_BF__MAIN__17$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Clear(self.ctx)


class Clear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003802, text_id=20003802) # 포탈 이용하세요
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[199])
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
