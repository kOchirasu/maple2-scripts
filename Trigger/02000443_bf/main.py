""" trigger/02000443_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001) # LocalTargetCamera
        self.set_effect(trigger_ids=[7001])
        self.enable_spawn_point_pc(spawn_id=11001, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=11002)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[101,102])
        self.set_mesh(trigger_ids=[1001,1002,1003])
        self.set_mesh(trigger_ids=[1004,1005,1006])
        self.set_mesh(trigger_ids=[1003])
        self.set_mesh(trigger_ids=[2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145,2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166,2167,2168,2169,2170,2171,2172,2173,2174,2175,2176,2177,2178,2179,2180,2181,2182,2183,2184,2185,2186,2187,2188,2189,2190,2191,2192,2193,2194,2195,2196,2197,2198,2199])
        self.set_mesh(trigger_ids=[2150], visible=True)
        self.move_user(map_id=2000443, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_gravity(gravity=-25.0)
        self.spawn_monster(spawn_ids=[210])
        self.enable_spawn_point_pc(spawn_id=11001)
        self.enable_spawn_point_pc(spawn_id=11002, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001) # LocalTargetCamera
        self.spawn_monster(spawn_ids=[211])
        self.set_dialogue(type=1, spawn_id=102, script='$02000443_BF__MAIN__0$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000443_BF__MAIN__3$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000443_BF__MAIN__1$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000443_BF__MAIN__2$', time=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2005')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2006')


initial_state = idle
