""" trigger/02000244_bf/lever.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2003])
        self.set_mesh(trigger_ids=[899])
        self.set_interact_object(trigger_ids=[10000303], state=1)
        self.set_interact_object(trigger_ids=[10000302], state=1)
        self.set_interact_object(trigger_ids=[10000301], state=1)
        self.set_mesh(trigger_ids=[801,802,803,804])
        self.set_mesh(trigger_ids=[805,806,807,808], visible=True)
        self.set_mesh(trigger_ids=[809,810,811,812], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000303], state=0):
            return 단계1(self.ctx)


class 단계1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000302], state=0):
            return 단계2(self.ctx)


class 단계2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000301], state=0):
            return 오픈(self.ctx)


class 오픈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8001,8002])
        self.set_effect(trigger_ids=[2003], visible=True)
        # self.set_mesh(trigger_ids=[899], visible=True)
        self.set_mesh(trigger_ids=[801,802,803,804], visible=True)
        self.set_mesh(trigger_ids=[805,806,807,808])
        self.set_mesh(trigger_ids=[809,810,811,812])
        self.set_timer(timer_id='1', seconds=180)
        self.set_mesh(trigger_ids=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145,2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166,2167,2168,2169,2170,2171,2172,2173,2174,2175,2176,2177,2178,2179,2180,2181,2182,2183,2184,2185,2186,2187,2188,2189,2190,2191,2192,2193,2194,2195,2196,2197,2198,2199])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return end(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145,2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166,2167,2168,2169,2170,2171,2172,2173,2174,2175,2176,2177,2178,2179,2180,2181,2182,2183,2184,2185,2186,2187,2188,2189,2190,2191,2192,2193,2194,2195,2196,2197,2198,2199], visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class end(trigger_api.Trigger):
    pass


initial_state = 대기
