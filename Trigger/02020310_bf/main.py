""" trigger/02020310_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10000)
        self.set_portal(portal_id=10001)
        self.set_portal(portal_id=10002)
        self.set_portal(portal_id=10003)
        self.set_portal(portal_id=10004)
        self.set_portal(portal_id=10005)
        self.set_portal(portal_id=10006)
        self.set_portal(portal_id=10007)
        self.set_portal(portal_id=10008)
        self.enable_spawn_point_pc(spawn_id=101, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=102)
        self.enable_spawn_point_pc(spawn_id=103)
        self.enable_spawn_point_pc(spawn_id=104)
        self.enable_spawn_point_pc(spawn_id=105)
        self.enable_spawn_point_pc(spawn_id=106)
        self.enable_spawn_point_pc(spawn_id=107)
        self.enable_spawn_point_pc(spawn_id=108)
        self.enable_spawn_point_pc(spawn_id=109)
        self.enable_spawn_point_pc(spawn_id=110)
        self.enable_spawn_point_pc(spawn_id=111)
        self.enable_spawn_point_pc(spawn_id=112)
        self.enable_spawn_point_pc(spawn_id=113)
        self.enable_spawn_point_pc(spawn_id=114)
        self.enable_spawn_point_pc(spawn_id=115)
        self.enable_spawn_point_pc(spawn_id=116)
        self.enable_spawn_point_pc(spawn_id=117)
        self.set_interact_object(trigger_ids=[12000301], state=0)
        self.set_interact_object(trigger_ids=[12000302], state=0)
        self.set_interact_object(trigger_ids=[12000303], state=0)
        self.set_interact_object(trigger_ids=[12000304], state=0)
        self.set_interact_object(trigger_ids=[12000305], state=0)
        self.set_interact_object(trigger_ids=[12000306], state=0)
        self.set_interact_object(trigger_ids=[12000307], state=0)
        self.set_interact_object(trigger_ids=[12000308], state=0)
        self.set_interact_object(trigger_ids=[12000309], state=0)
        self.set_interact_object(trigger_ids=[12000310], state=0)
        self.set_interact_object(trigger_ids=[12000311], state=0)
        self.set_interact_object(trigger_ids=[12000312], state=0)
        self.set_interact_object(trigger_ids=[12000313], state=0)
        self.set_interact_object(trigger_ids=[12000314], state=0)
        self.set_interact_object(trigger_ids=[12000315], state=0)
        self.set_interact_object(trigger_ids=[12000316], state=0)
        self.set_interact_object(trigger_ids=[12000317], state=0)
        self.set_interact_object(trigger_ids=[12000318], state=0)
        self.set_interact_object(trigger_ids=[12000319], state=0)
        self.set_interact_object(trigger_ids=[12000320], state=0)
        self.set_interact_object(trigger_ids=[12000321], state=0)
        # self.set_interact_object(trigger_ids=[12000322], state=2)
        self.set_interact_object(trigger_ids=[12000404], state=1)
        self.set_interact_object(trigger_ids=[12000405], state=1)
        # self.set_mesh(trigger_ids=[1001], visible=True)
        # self.set_mesh(trigger_ids=[1002], visible=True)
        # self.set_mesh(trigger_ids=[1003], visible=True)
        # self.set_mesh(trigger_ids=[1004], visible=True)
        # self.set_mesh(trigger_ids=[1005], visible=True)
        # self.set_mesh(trigger_ids=[1006], visible=True)
        # self.set_mesh(trigger_ids=[2001], visible=True)
        # self.set_mesh(trigger_ids=[2002], visible=True)
        # self.set_mesh(trigger_ids=[2003], visible=True)
        # self.set_mesh(trigger_ids=[2004], visible=True)
        # self.set_mesh(trigger_ids=[2005], visible=True)
        # self.set_mesh(trigger_ids=[2006], visible=True)
        # self.set_mesh(trigger_ids=[2007], visible=True)
        # self.set_mesh(trigger_ids=[2008], visible=True)
        # self.set_mesh(trigger_ids=[3001], visible=True)
        # self.set_mesh(trigger_ids=[3002], visible=True)
        # self.set_mesh(trigger_ids=[3003], visible=True)
        # self.set_mesh(trigger_ids=[3004], visible=True)
        # self.set_mesh(trigger_ids=[3005], visible=True)
        # self.set_mesh(trigger_ids=[3006], visible=True)
        self.set_mesh(trigger_ids=[8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8011,8012,8013,8014,8015,8016,8017,8018,8019,8020,8021,8022,8023,8024,8025,8026,8027,8028,8029,8030,8031,8032,8033,8034,8035,8036,8037,8038,8039,8040,8041,8042,8043,8044,8045,8046,8047,8048,8049,8050,8051,8052,8053,8054,8055,8056,8057,8058,8059,8060,8061,8062,8063,8064,8065,8066,8067,8068,8069,8070,8071,8072,8073,8074,8075,8076,8077,8078,8079,8080,8081,8082,8083,8084,8085,8086,8087,8088,8089,8090,8091,8092,8093,8094,8095,8096,8097,8098,8099,8100,8101,8102,8103,8104,8105,8106,8107,8108,8109,8110,8111,8112,8113,8114,8115,8116,8117,8118,8119,8120,8121,8122,8123,8124,8125,8126,8127,8128,8129,8130,8131,8132,8133,8134,8135,8136,8137,8138,8139,8140,8141,8142,8143,8144,8145,8146,8147,8148,8149,8150,8151,8152,8153,8154,8155,8156,8157,8158,8159,8160,8161,8162,8163,8164,8165,8166,8167,8168,8169,8170,8171,8172,8173,8174,8175,8176,8177,8178,8179,8180,8181,8182,8183,8184,8185,8186,8187,8188,8189,8190,8191,8192,8193,8194,8195,8196,8197,8198])
        self.set_mesh(trigger_ids=[88001,88002,88003,88004,88005,88006,88007,88008,88009,88010,88011,88012,88013,88014,88015,88016,88017,88018,88019,88020,88021,88022,88023,88024,88025,88026,88027,88028,88029,88030,88031,88032,88033,88034,88035,88036,88037,88038,88039,88040,88041,88042,88043,88044,88045,88046,88047,88048])
        self.set_mesh(trigger_ids=[89001,89002,89003,89004,89005,89006,89007,89008,89009,89010,89011,89012,89013,89014,89015,89016,89017,89018,89019,89020,89021,89022,89023,89024,89025,89026,89027,89028,89029,89030,89031,89032,89033,89034,89035,89036,89037,89038,89039,89040,89041,89042,89043,89044,89045,89046,89047,89048])
        self.set_mesh(trigger_ids=[1100001,1100002,1100003,1100004,1100005,1100006,1100007,1100008,1100009,1100010], visible=True)
        self.set_mesh(trigger_ids=[1100021,1100022,1100023,1100024,1100025,1100026,1100027,1100028,1100029,1100030], visible=True)
        self.set_mesh(trigger_ids=[1100031,1100032,1100033,1100034,1100035,1100036,1100037,1100038,1100039,1100040], visible=True)
        self.set_mesh(trigger_ids=[1100101,1100102,1100103,1100104,1100105,1100106,1100107,1100108,1100109,1100110], visible=True)
        self.set_mesh(trigger_ids=[1100201,1100202,1100203,1100204,1100205,1100206,1100207,1100208,1100209,1100210], visible=True)
        self.set_mesh(trigger_ids=[1100301,1100302,1100303,1100304,1100305,1100306,1100307,1100308,1100309,1100310], visible=True)
        self.set_mesh(trigger_ids=[1101001,1101002,1101003,1101004,1101005,1101006,1101007,1101008,1101009,1101010], visible=True)
        self.set_mesh(trigger_ids=[1102001,1102002,1102003,1102004,1102005,1102006,1102007,1102008,1102009,1102010], visible=True)
        self.set_mesh(trigger_ids=[1103001,1103002,1103003,1103004,1103005,1103006,1103007,1103008,1103009,1103010], visible=True)
        self.set_mesh(trigger_ids=[1104001,1104002,1104003,1104004,1104005,1104006,1104007,1104008,1104009,1104010], visible=True)
        self.set_mesh(trigger_ids=[1105001,1105002,1105003,1105004,1105005,1105006,1105007,1105008,1105009,1105010], visible=True)
        self.set_mesh(trigger_ids=[1106001,1106002,1106003,1106004,1106005,1106006,1106007,1106008,1106009,1106010], visible=True)
        self.set_mesh(trigger_ids=[1110001,1110002,1110003,1110004,1110005,1110006,1110007,1110008,1110009,1110010], visible=True)
        self.set_mesh(trigger_ids=[1120001,1120002,1120003,1120004,1120005,1120006,1120007,1120008,1120009,1120010], visible=True)
        self.set_mesh(trigger_ids=[1130001,1130002,1130003,1130004,1130005,1130006,1130007,1130008,1130009,1130010], visible=True)
        self.set_mesh(trigger_ids=[1140001,1140002,1140003,1140004,1140005,1140006,1140007,1140008,1140009,1140010], visible=True)
        self.set_mesh(trigger_ids=[1150001,1150002,1150003,1150004,1150005,1150006,1150007,1150008,1150009,1150010], visible=True)
        self.set_mesh(trigger_ids=[1160001,1160002,1160003,1160004,1160005,1160006,1160007,1160008,1160009,1160010], visible=True)
        self.set_mesh(trigger_ids=[1210001,1210002,1210003,1210004,1210005,1210006,1210007,1210008,1210009,1210010], visible=True)
        self.set_mesh(trigger_ids=[1310001,1310002,1310003,1310004,1310005,1310006,1310007,1310008,1310009,1310010], visible=True)
        self.set_mesh(trigger_ids=[1410001,1410002,1410003,1410004,1410005,1410006,1410007,1410008,1410009,1410010], visible=True)
        self.set_mesh_animation(trigger_ids=[1100001,1100002,1100003,1100004,1100005,1100006,1100007,1100008,1100009,1100010], visible=True)
        self.set_mesh_animation(trigger_ids=[1100021,1100022,1100023,1100024,1100025,1100026,1100027,1100028,1100029,1100030], visible=True)
        self.set_mesh_animation(trigger_ids=[1100031,1100032,1100033,1100034,1100035,1100036,1100037,1100038,1100039,1100040], visible=True)
        self.set_mesh_animation(trigger_ids=[1100101,1100102,1100103,1100104,1100105,1100106,1100107,1100108,1100109,1100110], visible=True)
        self.set_mesh_animation(trigger_ids=[1100201,1100202,1100203,1100204,1100205,1100206,1100207,1100208,1100209,1100210], visible=True)
        self.set_mesh_animation(trigger_ids=[1100301,1100302,1100303,1100304,1100305,1100306,1100307,1100308,1100309,1100310], visible=True)
        self.set_mesh_animation(trigger_ids=[1101001,1101002,1101003,1101004,1101005,1101006,1101007,1101008,1101009,1101010], visible=True)
        self.set_mesh_animation(trigger_ids=[1102001,1102002,1102003,1102004,1102005,1102006,1102007,1102008,1102009,1102010], visible=True)
        self.set_mesh_animation(trigger_ids=[1103001,1103002,1103003,1103004,1103005,1103006,1103007,1103008,1103009,1103010], visible=True)
        self.set_mesh_animation(trigger_ids=[1104001,1104002,1104003,1104004,1104005,1104006,1104007,1104008,1104009,1104010], visible=True)
        self.set_mesh_animation(trigger_ids=[1105001,1105002,1105003,1105004,1105005,1105006,1105007,1105008,1105009,1105010], visible=True)
        self.set_mesh_animation(trigger_ids=[1106001,1106002,1106003,1106004,1106005,1106006,1106007,1106008,1106009,1106010], visible=True)
        self.set_mesh_animation(trigger_ids=[1110001,1110002,1110003,1110004,1110005,1110006,1110007,1110008,1110009,1110010], visible=True)
        self.set_mesh_animation(trigger_ids=[1120001,1120002,1120003,1120004,1120005,1120006,1120007,1120008,1120009,1120010], visible=True)
        self.set_mesh_animation(trigger_ids=[1130001,1130002,1130003,1130004,1130005,1130006,1130007,1130008,1130009,1130010], visible=True)
        self.set_mesh_animation(trigger_ids=[1140001,1140002,1140003,1140004,1140005,1140006,1140007,1140008,1140009,1140010], visible=True)
        self.set_mesh_animation(trigger_ids=[1150001,1150002,1150003,1150004,1150006,1150006,1150007,1150008,1150009,1150010], visible=True)
        self.set_mesh_animation(trigger_ids=[1160001,1160002,1160003,1160004,1160005,1160006,1160007,1160008,1160009,1160010], visible=True)
        self.set_mesh_animation(trigger_ids=[1210001,1210002,1210003,1210004,1210005,1210006,1210007,1210008,1210009,1210010], visible=True)
        self.set_mesh_animation(trigger_ids=[1310001,1310002,1310003,1310004,1310005,1310006,1310007,1310008,1310009,1310010], visible=True)
        self.set_mesh_animation(trigger_ids=[1410001,1410002,1410003,1410004,1410005,1410006,1410007,1410008,1410009,1410010], visible=True)
        self.set_visible_breakable_object(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], visible=True)
        self.set_visible_breakable_object(trigger_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020], visible=True)
        self.set_visible_breakable_object(trigger_ids=[1021,1022], visible=True)
        # self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[900]):
            return 카메라시작(self.ctx)


class 카메라시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=카메라종료, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # self.select_camera_path(path_ids=[101,102,112,113,103,114,104,105,115,106,107,108,109], return_view=False)
        self.select_camera_path(path_ids=[100001,100002,100003,100004,100005], return_view=False)
        # self.set_dialogue(type=2, spawn_id=23501001, script='하아...복잡한 곳이로군요... 어떤 비밀이 있는지 한 번 알아볼게요.', time=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마를레네대사(self.ctx)


class 마를레네대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004582, msg='$02020310_BF__MAIN__0$', align=Align.Left, illust_id='Eone_serious', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9500):
            return 카메라종료(self.ctx)


class 카메라종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        self.side_npc_talk(npc_id=11004582, illust='Eone_normal', script='$02020310_BF__MAIN__1$', duration=6000)
        self.set_scene_skip() # Missing State: State
        return 시작딜레이(self.ctx)


class 시작딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.spawn_monster(spawn_ids=[1101], auto_target=False)
            # self.spawn_monster(spawn_ids=[1102], auto_target=False)
            # self.spawn_monster(spawn_ids=[1103], auto_target=False)
            self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], auto_target=False)
            self.spawn_monster(spawn_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020], auto_target=False)
            return LineStart(self.ctx)


class LineStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1101,1001,1002,1005,1006,1009,1010,1011,1012,1015,1016,1017,1018,1019,1020]):
            self.side_npc_talk(npc_id=11004582, illust='Eone_normal', script='$02020310_BF__MAIN__2$', duration=8000)
            self.enable_spawn_point_pc(spawn_id=101)
            self.enable_spawn_point_pc(spawn_id=102, is_enable=True)
            # self.set_visible_breakable_object(trigger_ids=[1001,1002,1003], visible=True)
            self.set_interact_object(trigger_ids=[12000301], state=1)
            self.set_interact_object(trigger_ids=[12000302], state=1)
            self.set_interact_object(trigger_ids=[12000303], state=1)
            self.spawn_monster(spawn_ids=[1104], auto_target=False)
            self.spawn_monster(spawn_ids=[1105], auto_target=False)
            self.spawn_monster(spawn_ids=[1106], auto_target=False)
            self.spawn_monster(spawn_ids=[1150,1151,1152,1153,1154,1155,1156,1157,1158,1159], auto_target=False)
            self.spawn_monster(spawn_ids=[1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172], auto_target=False)
            return CableOn_01(self.ctx)


class CableOn_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000301], state=0):
            self.set_interact_object(trigger_ids=[12000302], state=0)
            self.set_interact_object(trigger_ids=[12000303], state=0)
            self.set_mesh(trigger_ids=[1100001,1100002,1100003,1100004,1100005,1100006,1100007,1100008,1100009,1100010])
            return CableDelay_01_1(self.ctx)
        if self.object_interacted(interact_ids=[12000302], state=0):
            self.set_interact_object(trigger_ids=[12000301], state=0)
            self.set_interact_object(trigger_ids=[12000303], state=0)
            self.set_mesh(trigger_ids=[1100031,1100032,1100033,1100034,1100035,1100036,1100037,1100038,1100039,1100040])
            return CableDelay_01_2(self.ctx)
        if self.object_interacted(interact_ids=[12000303], state=0):
            self.set_interact_object(trigger_ids=[12000301], state=0)
            self.set_interact_object(trigger_ids=[12000302], state=0)
            self.set_mesh(trigger_ids=[1100021,1100022,1100023,1100024,1100025,1100026,1100027,1100028,1100029,1100030])
            return CableDelay_01_3(self.ctx)


class CableDelay_01_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__3$', arg3='3000')
            return CableDelay_02_1(self.ctx)


class CableDelay_01_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__4$', arg3='3000')
            return CableDelay_02_2(self.ctx)


class CableDelay_01_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__5$', arg3='3000')
            return CableDelay_02_3(self.ctx)


class CableDelay_02_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__6$', arg3='1000')
            return CableDelay_03_1(self.ctx)


class CableDelay_02_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__7$', arg3='1000')
            return CableDelay_03_2(self.ctx)


class CableDelay_02_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__8$', arg3='1000')
            return CableDelay_03_3(self.ctx)


class CableDelay_03_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__9$', arg3='1000')
            return CableDelay_04_1(self.ctx)


class CableDelay_03_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__10$', arg3='1000')
            return CableDelay_04_2(self.ctx)


class CableDelay_03_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__11$', arg3='1000')
            return CableDelay_04_3(self.ctx)


class CableDelay_04_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__12$', arg3='1000')
            return CableDelay_05_1(self.ctx)


class CableDelay_04_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__13$', arg3='1000')
            return CableDelay_05_2(self.ctx)


class CableDelay_04_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__14$', arg3='1000')
            return CableDelay_05_3(self.ctx)


class CableDelay_05_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1001], enable=True)
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__15$', arg3='5000')
            return CableOff_01(self.ctx)


class CableDelay_05_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1002], enable=True)
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__16$', arg3='5000')
            return CableOff_02(self.ctx)


class CableDelay_05_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1003], enable=True)
            self.set_event_ui(type=1, arg2='$02020310_BF__MAIN__17$', arg3='5000')
            return CableOff_03(self.ctx)


class CableOff_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-13125,75,2550))
            self.set_user_value(trigger_id=900002, key='Block', value=1)
            return End_01(self.ctx)


class CableOff_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-13275,-5025,1650))
            self.set_user_value(trigger_id=900002, key='Block', value=2)
            return End_01(self.ctx)


class CableOff_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-12925,5025,550))
            self.set_user_value(trigger_id=900002, key='Block', value=3)
            return End_01(self.ctx)


class End_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # self.set_visible_breakable_object(trigger_ids=[1001])
            # self.set_visible_breakable_object(trigger_ids=[1002])
            # # <transition state="대기"/>
            self.set_visible_breakable_object(trigger_ids=[1003])
            pass


initial_state = 대기
