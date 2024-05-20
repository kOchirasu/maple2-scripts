""" trigger/52000099_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 퀘스트체크50100520(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[50100520], quest_states=[3]):
            return phase_end_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50100520], quest_states=[2]):
            return phase_end_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50100520], quest_states=[1]):
            return ready(self.ctx)


class 퀘스트체크50100540(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[50100540], quest_states=[3]):
            return phase_end_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50100540], quest_states=[2]):
            return phase_end_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50100540], quest_states=[1]):
            return phase_end_01(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=701, skill_id=99910180)
        self.set_actor(trigger_id=3101, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=3102, initial_sequence='Attack_Idle_A')
        self.set_local_camera(camera_id=8017) # LocalTargetCamera
        self.set_visible_breakable_object(trigger_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=True)
        self.set_visible_breakable_object(trigger_ids=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=True)
        self.set_visible_breakable_object(trigger_ids=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], visible=True)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004])
        self.spawn_monster(spawn_ids=[101])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[7001])
        self.set_effect(trigger_ids=[7002])
        self.set_effect(trigger_ids=[7003])
        self.set_effect(trigger_ids=[7004], visible=True)
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return ready2(self.ctx)


"""
class start_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000099, portal_id=2)
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=11, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[200])
        self.set_npc_emotion_loop(spawn_id=200, sequence_name='Stun_A', duration=18000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마드라칸연출01(self.ctx)
"""

"""
class 마드라칸연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=11, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[1000,1001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드라칸연출02(self.ctx)
"""

"""
class 마드라칸연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1002,1003], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Jump_Damg_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 마드라칸연출03(self.ctx)
"""

"""
class 마드라칸연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1004,1008,1009,1010], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=18000):
            return 마드라칸연출04(self.ctx)
"""

"""
class 마드라칸연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드라칸연출05(self.ctx)
"""

"""
class 마드라칸연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ready2(self.ctx)
"""

class ready2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.move_user(map_id=52000099, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start2(self.ctx)


class start2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=scene_07)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8001,8002,8003], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2002')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003087, illust_id='11003087', msg='$52000099_QD__MAIN__20$', duration=5000, align=Align.Left)
        self.select_camera_path(path_ids=[8004,8005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2003')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2004')
        self.add_cinematic_talk(npc_id=11003087, illust_id='11003087', msg='$52000099_QD__MAIN__21$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006,8007], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_2006')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2005')
        self.add_cinematic_talk(npc_id=11003087, illust_id='11003087', msg='$52000099_QD__MAIN__22$', duration=3000, align=Align.Left)
        self.set_effect(trigger_ids=[7001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7002], visible=True)
        self.add_cinematic_talk(npc_id=11003087, illust_id='11003087', msg='$52000099_QD__MAIN__23$', duration=3000, align=Align.Left)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='IceSphere_A,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8009], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=71000007, level=1, is_player=False, is_skill_set=False)
        self.add_buff(box_ids=[701], skill_id=71000008, level=1, is_player=False, is_skill_set=False)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Attack_Idle_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25200991, text_id=25200991, duration=5000)
        # self.destroy_monster(spawn_ids=[101])
        # self.spawn_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[201,202,205,204])
        self.reset_camera()
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # self.set_local_camera(camera_id=8011, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_09(self.ctx)


class scene_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220])
        self.set_visible_breakable_object(trigger_ids=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240])
        self.set_visible_breakable_object(trigger_ids=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270])
        self.add_balloon_talk(spawn_id=101, msg='$52000099_QD__MAIN__24$', duration=3000)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,204,205]):
            return scene_10(self.ctx)


class scene_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='$52000099_QD__MAIN__25$', duration=3000)
        self.spawn_monster(spawn_ids=[201,202,203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203]):
            return scene_11(self.ctx)


class scene_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='$52000099_QD__MAIN__26$', duration=3000)
        self.spawn_monster(spawn_ids=[206,207,203,202])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[206,207,203,202]):
            return scene_12(self.ctx)


class scene_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[123])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_13(self.ctx)


class scene_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000099, portal_id=2)
        self.set_visible_breakable_object(trigger_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=True)
        self.set_visible_breakable_object(trigger_ids=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=True)
        self.set_visible_breakable_object(trigger_ids=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], visible=True)
        self.select_camera_path(path_ids=[8011,8012], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_14(self.ctx)


class scene_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=phase_b_scene_05)
        self.remove_buff(box_id=103, skill_id=71000007)
        self.remove_buff(box_id=103, skill_id=71000008)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return phase_b_scene_02(self.ctx)


class phase_b_scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(trigger_id=701, type='trigger', achieve='Defence1Clear')
        self.move_npc(spawn_id=123, patrol_name='MS2PatrolData_2102')
        self.move_user(map_id=52000099, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return phase_b_scene_03(self.ctx)


class phase_b_scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8015,8016], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_2008')
        self.add_cinematic_talk(npc_id=11003087, illust_id='11003087', msg='$52000099_QD__MAIN__27$', duration=5000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003087, illust_id='11003087', msg='$52000099_QD__MAIN__28$', duration=5000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003087, illust_id='11003087', msg='$52000099_QD__MAIN__17$', duration=3000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003087, illust_id='11003087', msg='$52000099_QD__MAIN__18$', duration=3000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003087, illust_id='11003087', msg='$52000099_QD__MAIN__19$', duration=5000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return phase_b_scene_04(self.ctx)


class phase_b_scene_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return phase_b_scene_05(self.ctx)


class phase_b_scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[122])
        self.destroy_monster(spawn_ids=[123])
        self.spawn_monster(spawn_ids=[124])
        self.set_visible_breakable_object(trigger_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220])
        self.set_visible_breakable_object(trigger_ids=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240])
        self.set_visible_breakable_object(trigger_ids=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270])
        self.add_buff(box_ids=[701], skill_id=71000007, level=1, is_player=False, is_skill_set=False)
        self.add_buff(box_ids=[701], skill_id=71000008, level=1, is_player=False, is_skill_set=False)
        self.set_mesh(trigger_ids=[3001,3003,3004], visible=True)
        self.move_user(map_id=52000099, portal_id=3)
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_local_camera(camera_id=8017, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return phase_b_scene_06(self.ctx)


class phase_b_scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='81', seconds=81, start_delay=1, interval=1)
        self.show_guide_summary(entity_id=25200993, text_id=25200993)
        self.spawn_monster(spawn_ids=[208])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_07(self.ctx)


class phase_b_scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[209])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_08(self.ctx)


class phase_b_scene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[210])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_09(self.ctx)


class phase_b_scene_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[212,213])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_10(self.ctx)


class phase_b_scene_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[211])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_11(self.ctx)


class phase_b_scene_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[214,216])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_12(self.ctx)


class phase_b_scene_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[209,210])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_13(self.ctx)


class phase_b_scene_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[211,211])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_14(self.ctx)


class phase_b_scene_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[213,214])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_15(self.ctx)


class phase_b_scene_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[215,216])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_16(self.ctx)


class phase_b_scene_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[210,211])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_17(self.ctx)


class phase_b_scene_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[212,213])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_18(self.ctx)


class phase_b_scene_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[212,213,214])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return phase_b_scene_19(self.ctx)


class phase_b_scene_19(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='81'):
            return phase_b_scene_end(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[207,208,209,210,211,212,213,214,215,216,217,218,219,220])


class phase_b_scene_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=True)
        self.set_visible_breakable_object(trigger_ids=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240], visible=True)
        self.set_visible_breakable_object(trigger_ids=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270], visible=True)
        self.set_mesh(trigger_ids=[3001,3002,3003,3004])
        self.hide_guide_summary(entity_id=25200993)
        self.set_local_camera(camera_id=8017) # LocalTargetCamera
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=phase_b_skip_1)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52000099, portal_id=3)
        self.set_achievement(trigger_id=701, type='trigger', achieve='Defence2Clear')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return phase_b_scene_end_02(self.ctx)


class phase_b_scene_end_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A'])
        # self.set_pc_emotion_loop(sequence_name='Emotion_Disappoint_Idle_A', duration=7000.0)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8018,8017], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return phase_b_scene_end_03(self.ctx)


class phase_b_scene_end_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8019,8020], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return phase_b_scene_end_04(self.ctx)


class phase_b_scene_end_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3101, visible=True, initial_sequence='Regen_A')
        self.set_actor(trigger_id=3102, visible=True, initial_sequence='Regen_A')
        self.set_effect(trigger_ids=[7006], visible=True)
        self.set_effect(trigger_ids=[7007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return phase_b_scene_end_05(self.ctx)


class phase_b_scene_end_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3101, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=3102, visible=True, initial_sequence='Idle_A')
        self.set_pc_emotion_sequence(sequence_names=['Jump_Damg_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A','Attack_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return phase_b_scene_end_06(self.ctx)


class phase_b_scene_end_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3101, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=3102, visible=True, initial_sequence='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return phase_b_scene_end_07(self.ctx)


class phase_b_scene_end_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7004], visible=True)
        self.move_user(map_id=52000099, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return phase_b_scene_end_07_ready(self.ctx)


class phase_b_scene_end_07_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3102, visible=True, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return phase_b_scene_end_08(self.ctx)


class phase_b_scene_end_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[124])
        self.select_camera_path(path_ids=[8021], return_view=False)
        self.spawn_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[103])
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A','Emotion_Disappoint_Idle_A'])
        self.add_cinematic_talk(npc_id=11004034, illust_id='LapentaMage_Idle', msg='$52000099_QD__MAIN__33$', duration=4000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003087, illust_id='11003087', msg='$52000099_QD__MAIN__34$', duration=2000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return phase_b_scene_end_09(self.ctx)


class phase_b_scene_end_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8022], return_view=False)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2009')
        self.add_cinematic_talk(npc_id=11000076, illust_id='11000076', msg='$52000099_QD__MAIN__29$', duration=5000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11004034, illust_id='LapentaMage_Idle', msg='$52000099_QD__MAIN__30$', duration=5000, align=Align.Left)
        self.set_actor(trigger_id=3101, initial_sequence='Regen_A')
        self.set_actor(trigger_id=3102, initial_sequence='Regen_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return phase_b_scene_end_10(self.ctx)


class phase_b_scene_end_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Attack_Idle_A,Attack_Idle_A,Attack_Idle_A,Attack_Idle_A')
        self.add_cinematic_talk(npc_id=11000076, illust_id='11000076', msg='$52000099_QD__MAIN__31$', duration=5000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return phase_c_01(self.ctx)


class phase_c_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8023], return_view=False)
        self.spawn_monster(spawn_ids=[110])
        self.spawn_monster(spawn_ids=[126])
        self.set_effect(trigger_ids=[7100], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_02(self.ctx)


class phase_c_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111])
        self.set_effect(trigger_ids=[7101], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_03(self.ctx)


class phase_c_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[112])
        self.set_effect(trigger_ids=[7102], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_04(self.ctx)


class phase_c_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[113])
        self.set_effect(trigger_ids=[7103], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_05(self.ctx)


class phase_c_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[114])
        self.set_effect(trigger_ids=[7104], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_06(self.ctx)


class phase_c_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[115])
        self.set_effect(trigger_ids=[7105], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_07(self.ctx)


class phase_c_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[116])
        self.set_effect(trigger_ids=[7106], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_08(self.ctx)


class phase_c_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[117])
        self.set_effect(trigger_ids=[7107], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_09(self.ctx)


class phase_c_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[118])
        self.set_effect(trigger_ids=[7108], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_10(self.ctx)


class phase_c_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[119])
        self.set_effect(trigger_ids=[7109], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_11(self.ctx)


class phase_c_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[120])
        self.set_effect(trigger_ids=[7110], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_c_12(self.ctx)


class phase_c_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[121])
        self.set_effect(trigger_ids=[7111], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return phase_c_13(self.ctx)


class phase_c_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8022], return_view=False)
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000099_QD__MAIN__32$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return phase_c_14(self.ctx)


class phase_c_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=121, patrol_name='MS2PatrolData_2081')
        self.move_npc(spawn_id=120, patrol_name='MS2PatrolData_2082')
        self.move_npc(spawn_id=119, patrol_name='MS2PatrolData_2083')
        self.move_npc(spawn_id=118, patrol_name='MS2PatrolData_2085')
        self.move_npc(spawn_id=117, patrol_name='MS2PatrolData_2091')
        self.move_npc(spawn_id=116, patrol_name='MS2PatrolData_2092')
        self.move_npc(spawn_id=115, patrol_name='MS2PatrolData_2087')
        self.move_npc(spawn_id=114, patrol_name='MS2PatrolData_2088')
        self.move_npc(spawn_id=113, patrol_name='MS2PatrolData_2084')
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_2089')
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_2086')
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2090')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return phase_c_15(self.ctx)


class phase_c_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return phase_c_16(self.ctx)


class phase_c_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220])
        self.set_visible_breakable_object(trigger_ids=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240])
        self.set_visible_breakable_object(trigger_ids=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270,3101,3102])
        self.spawn_monster(spawn_ids=[201,202,205,204])
        self.spawn_monster(spawn_ids=[211,212,215,214])
        self.spawn_monster(spawn_ids=[215,216,217,218])
        self.add_buff(box_ids=[701], skill_id=99910180, level=1, is_player=False, is_skill_set=False)
        self.destroy_monster(spawn_ids=[103])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timer_id='82', seconds=82, start_delay=1, interval=1)
        self.reset_camera()
        self.set_local_camera(camera_id=8023, enable=True) # LocalTargetCamera
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,205,204,211,212,215,214]):
            return phase_c_end(self.ctx)
        if self.time_expired(timer_id='82'):
            return phase_c_end(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='82')
        self.destroy_monster(spawn_ids=[201,202,205,204,211,212,215,214])


class phase_c_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_local_camera(camera_id=8023) # LocalTargetCamera
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return phase_c_end_02(self.ctx)

    def on_exit(self) -> None:
        self.move_npc(spawn_id=121, patrol_name='MS2PatrolData_2081')
        self.move_npc(spawn_id=120, patrol_name='MS2PatrolData_2082')
        self.move_npc(spawn_id=119, patrol_name='MS2PatrolData_2083')
        self.move_npc(spawn_id=118, patrol_name='MS2PatrolData_2085')
        self.move_npc(spawn_id=117, patrol_name='MS2PatrolData_2091')
        self.move_npc(spawn_id=116, patrol_name='MS2PatrolData_2092')
        self.move_npc(spawn_id=115, patrol_name='MS2PatrolData_2087')
        self.move_npc(spawn_id=114, patrol_name='MS2PatrolData_2088')
        self.move_npc(spawn_id=113, patrol_name='MS2PatrolData_2084')
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_2089')
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_2086')
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2090')


class phase_b_skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3101)
        self.set_actor(trigger_id=3102)
        self.destroy_monster(spawn_ids=[124]) # 전두용 오르데 삭제
        self.destroy_monster(spawn_ids=[126])
        self.destroy_monster(spawn_ids=[110])
        self.destroy_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[112])
        self.destroy_monster(spawn_ids=[113])
        self.destroy_monster(spawn_ids=[114])
        self.destroy_monster(spawn_ids=[115])
        self.destroy_monster(spawn_ids=[116])
        self.destroy_monster(spawn_ids=[117])
        self.destroy_monster(spawn_ids=[118])
        self.destroy_monster(spawn_ids=[119])
        self.destroy_monster(spawn_ids=[120])
        self.destroy_monster(spawn_ids=[121])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_b_skip_2(self.ctx)


class phase_b_skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[126]) # 비전두용 오르데 소환
        self.spawn_monster(spawn_ids=[106]) # 비전투 라네모네 소환
        self.spawn_monster(spawn_ids=[110])
        self.spawn_monster(spawn_ids=[111])
        self.spawn_monster(spawn_ids=[112])
        self.spawn_monster(spawn_ids=[113])
        self.spawn_monster(spawn_ids=[114])
        self.spawn_monster(spawn_ids=[115])
        self.spawn_monster(spawn_ids=[116])
        self.spawn_monster(spawn_ids=[117])
        self.spawn_monster(spawn_ids=[118])
        self.spawn_monster(spawn_ids=[119])
        self.spawn_monster(spawn_ids=[120])
        self.spawn_monster(spawn_ids=[121])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_b_skip_3(self.ctx)


class phase_b_skip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=121, patrol_name='MS2PatrolData_2081')
        self.move_npc(spawn_id=120, patrol_name='MS2PatrolData_2082')
        self.move_npc(spawn_id=119, patrol_name='MS2PatrolData_2083')
        self.move_npc(spawn_id=118, patrol_name='MS2PatrolData_2085')
        self.move_npc(spawn_id=117, patrol_name='MS2PatrolData_2091')
        self.move_npc(spawn_id=116, patrol_name='MS2PatrolData_2092')
        self.move_npc(spawn_id=115, patrol_name='MS2PatrolData_2087')
        self.move_npc(spawn_id=114, patrol_name='MS2PatrolData_2088')
        self.move_npc(spawn_id=113, patrol_name='MS2PatrolData_2084')
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_2089')
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_2086')
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2090')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return phase_b_skip_4(self.ctx)


class phase_b_skip_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52000099, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return phase_b_skip_5(self.ctx)


class phase_b_skip_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220])
        self.set_visible_breakable_object(trigger_ids=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240])
        self.set_visible_breakable_object(trigger_ids=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270,3101,3102])
        self.spawn_monster(spawn_ids=[201,202,205,204])
        self.spawn_monster(spawn_ids=[211,212,215,214])
        self.spawn_monster(spawn_ids=[215,216,217,218])
        self.add_buff(box_ids=[701], skill_id=99910180, level=1, is_player=False, is_skill_set=False)
        self.destroy_monster(spawn_ids=[103])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timer_id='82', seconds=82, start_delay=1, interval=1)
        self.reset_camera()
        self.set_local_camera(camera_id=8023, enable=True) # LocalTargetCamera
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,205,204,211,212,215,214]):
            return phase_b_skip_end(self.ctx)
        if self.time_expired(timer_id='82'):
            return phase_b_skip_end(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='82')
        self.destroy_monster(spawn_ids=[201,202,205,204,211,212,215,214])


class phase_b_skip_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_local_camera(camera_id=8023) # LocalTargetCamera
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return phase_c_end_02(self.ctx)

    def on_exit(self) -> None:
        self.move_npc(spawn_id=121, patrol_name='MS2PatrolData_2081')
        self.move_npc(spawn_id=120, patrol_name='MS2PatrolData_2082')
        self.move_npc(spawn_id=119, patrol_name='MS2PatrolData_2083')
        self.move_npc(spawn_id=118, patrol_name='MS2PatrolData_2085')
        self.move_npc(spawn_id=117, patrol_name='MS2PatrolData_2091')
        self.move_npc(spawn_id=116, patrol_name='MS2PatrolData_2092')
        self.move_npc(spawn_id=115, patrol_name='MS2PatrolData_2087')
        self.move_npc(spawn_id=114, patrol_name='MS2PatrolData_2088')
        self.move_npc(spawn_id=113, patrol_name='MS2PatrolData_2084')
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_2089')
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_2086')
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2090')


class phase_end_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3101)
        self.set_actor(trigger_id=3102)
        self.set_visible_breakable_object(trigger_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220])
        self.set_visible_breakable_object(trigger_ids=[2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240])
        self.set_visible_breakable_object(trigger_ids=[2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2263,2264,2265,2266,2267,2268,2269,2270])
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_02(self.ctx)


class phase_end_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[126]) # 비전투 오르데 소환
        self.spawn_monster(spawn_ids=[110])
        self.spawn_monster(spawn_ids=[106]) # 비전투 라네모네 소환
        self.spawn_monster(spawn_ids=[111])
        self.set_effect(trigger_ids=[7101], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_03(self.ctx)


class phase_end_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[112])
        self.set_effect(trigger_ids=[7102], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_04(self.ctx)


class phase_end_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[113])
        self.set_effect(trigger_ids=[7103], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_05(self.ctx)


class phase_end_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[114])
        self.set_effect(trigger_ids=[7104], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_06(self.ctx)


class phase_end_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[115])
        self.set_effect(trigger_ids=[7105], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_07(self.ctx)


class phase_end_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[116])
        self.set_effect(trigger_ids=[7106], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_08(self.ctx)


class phase_end_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[117])
        self.set_effect(trigger_ids=[7107], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_09(self.ctx)


class phase_end_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[118])
        self.set_effect(trigger_ids=[7108], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_10(self.ctx)


class phase_end_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[119])
        self.set_effect(trigger_ids=[7109], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_11(self.ctx)


class phase_end_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[120])
        self.set_effect(trigger_ids=[7110], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return phase_end_12(self.ctx)


class phase_end_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[121])
        self.set_effect(trigger_ids=[7111], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return phase_end(self.ctx)


class phase_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8023) # LocalTargetCamera
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return phase_c_end_02(self.ctx)

    def on_exit(self) -> None:
        self.move_npc(spawn_id=121, patrol_name='MS2PatrolData_2081')
        self.move_npc(spawn_id=120, patrol_name='MS2PatrolData_2082')
        self.move_npc(spawn_id=119, patrol_name='MS2PatrolData_2083')
        self.move_npc(spawn_id=118, patrol_name='MS2PatrolData_2085')
        self.move_npc(spawn_id=117, patrol_name='MS2PatrolData_2091')
        self.move_npc(spawn_id=116, patrol_name='MS2PatrolData_2092')
        self.move_npc(spawn_id=115, patrol_name='MS2PatrolData_2087')
        self.move_npc(spawn_id=114, patrol_name='MS2PatrolData_2088')
        self.move_npc(spawn_id=113, patrol_name='MS2PatrolData_2084')
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_2089')
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_2086')
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2090')


class phase_c_end_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(trigger_id=701, type='trigger', achieve='AlonRpClear')
        self.reset_camera()
        self.move_user(map_id=52000099, portal_id=2)
        self.spawn_monster(spawn_ids=[104])
        self.remove_buff(box_id=701, skill_id=99910180)


initial_state = 퀘스트체크50100520
