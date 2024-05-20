""" trigger/02000388_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[301,302,303,304,305])
        self.set_actor(trigger_id=3001, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=3002, visible=True, initial_sequence='Closed')
        self.set_interact_object(trigger_ids=[10001096], state=1)
        self.set_breakable(trigger_ids=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821])
        self.set_breakable(trigger_ids=[1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850])
        self.set_breakable(trigger_ids=[1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return RoomCheck(self.ctx)


class RoomCheck(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return CheckUserCount(self.ctx)
        if not self.is_dungeon_room():
            return QuestDungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return mermaid_01(self.ctx)


class QuestDungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[50001517], quest_states=[1]): # >
            return mermaid_01(self.ctx)
        if self.quest_user_detected(box_ids=[702], quest_ids=[50001517], quest_states=[2]):
            return moveuser_00(self.ctx)
        if self.quest_user_detected(box_ids=[702], quest_ids=[50001518], quest_states=[1]):
            return moveuser_00(self.ctx)


class moveuser_00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000390, portal_id=2)


class mermaid_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8001,8002], return_view=False)
        self.spawn_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return mermaid_02(self.ctx)


class mermaid_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.set_skip(state=scene_04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return mermaid_02_talk(self.ctx)


class mermaid_02_talk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000388_BF__MAIN__0$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000388_BF__MAIN__1$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.select_camera(trigger_id=8006)
        self.set_dialogue(type=1, spawn_id=102, script='$02000388_BF__MAIN__2$', time=3)
        self.set_dialogue(type=1, spawn_id=101, script='$02000388_BF__MAIN__3$', time=3, arg5=3)
        self.set_dialogue(type=1, spawn_id=102, script='$02000388_BF__MAIN__4$', time=3, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2002')
        self.set_dialogue(type=1, spawn_id=102, script='$02000388_BF__MAIN__5$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Attack_01_A')
        self.set_mesh(trigger_ids=[7001,7002])
        self.set_actor(trigger_id=3001, visible=True, initial_sequence='Opening')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return open_door_01(self.ctx)


class open_door_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000388_BF__MAIN__6$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000388_BF__MAIN__7$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_local_camera(camera_id=8100, enable=True)
        self.set_breakable(trigger_ids=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821], enable=True)
        self.set_effect(trigger_ids=[7101], visible=True)
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703]):
            return battle_01(self.ctx)


class battle_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8100, enable=True) # LocalTargetCamera
        self.set_dialogue(type=1, spawn_id=102, script='$02000388_BF__MAIN__8$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000388_BF__MAIN__9$', time=2, arg5=1)
        self.spawn_monster(spawn_ids=[201,202,203,204])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204]):
            return battle_02(self.ctx)


class battle_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=open_door_03)
        self.select_camera(trigger_id=8007)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2005')
        self.set_dialogue(type=1, spawn_id=101, script='$02000388_BF__MAIN__10$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=704, spawn_ids=[101]):
            return open_door_ready(self.ctx)


class open_door_ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return open_door_02(self.ctx)


class open_door_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2007')
        self.set_mesh(trigger_ids=[7003,7004])
        self.set_actor(trigger_id=3002, visible=True, initial_sequence='Opening')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return open_door_03(self.ctx)


class open_door_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_local_camera(camera_id=8100, enable=True)
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2006')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2008')
        self.set_dialogue(type=1, spawn_id=102, script='$02000388_BF__MAIN__11$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=101, script='$02000388_BF__MAIN__12$', time=2)
        self.set_breakable(trigger_ids=[1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850], enable=True)
        self.set_effect(trigger_ids=[7102], visible=True)
        self.spawn_monster(spawn_ids=[205,206,207,208,209])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[205,206,207,208,209]):
            return battle_03(self.ctx)


class battle_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000388_BF__MAIN__13$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000388_BF__MAIN__14$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001096], state=0):
            return battle_04(self.ctx)


class battle_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7103], visible=True)
        self.set_breakable(trigger_ids=[1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871], enable=True)
        self.set_dialogue(type=1, spawn_id=102, script='$02000388_BF__MAIN__15$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000388_BF__MAIN__16$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return move_02(self.ctx)


class move_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2010')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2009')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705]):
            return ship_01(self.ctx)


class ship_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000388_BF__MAIN__17$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000388_BF__MAIN__18$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706]):
            return ship_02(self.ctx)


class ship_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000388_BF__MAIN__19$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001097], state=0):
            return ship_03(self.ctx)


class ship_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001098], state=0):
            return ship_end(self.ctx)


class ship_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=ending_02)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ending(self.ctx)


class ending(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7104], visible=True)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8003,8004,8005,8006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return ending_02(self.ctx)


class ending_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ending_03(self.ctx)


class ending_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000389)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ending_04(self.ctx)


class ending_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_local_camera(camera_id=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7101])
        self.set_effect(trigger_ids=[7102])
        self.set_effect(trigger_ids=[7103])
        self.set_effect(trigger_ids=[7104])
        self.destroy_monster(spawn_ids=[101,102])


initial_state = idle
