""" trigger/02020310_bf/field_2.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000307], state=2)
        self.set_interact_object(trigger_ids=[12000308], state=2)
        self.set_interact_object(trigger_ids=[12000309], state=2)
        self.set_interact_object(trigger_ids=[12000310], state=2)
        self.set_interact_object(trigger_ids=[12000311], state=2)
        self.set_interact_object(trigger_ids=[12000312], state=2)
        # self.set_visible_breakable_object(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])
        # self.set_visible_breakable_object(trigger_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
        # self.set_visible_breakable_object(trigger_ids=[1021,1022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block') == 1:
            self.set_user_value(trigger_id=900003, key='Block', value=0)
            return ArriveBlock_1(self.ctx)
        if self.user_value(key='Block') == 2:
            self.set_user_value(trigger_id=900003, key='Block', value=0)
            return ArriveBlock_2(self.ctx)
        if self.user_value(key='Block') == 3:
            self.set_user_value(trigger_id=900003, key='Block', value=0)
            return ArriveBlock_3(self.ctx)


# =================================================================================================================================================
class ArriveBlock_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            self.spawn_monster(spawn_ids=[2001], auto_target=False)
            return ArriveBlock_Delay_1(self.ctx)


class ArriveBlock_Delay_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$02020310_BF__FIELD_2__0$', duration=7000)
            return Block_1_01(self.ctx)
        if self.monster_dead(spawn_ids=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000001], arg2=False)
            self.destroy_monster(spawn_ids=[1000002], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000307], state=1)
            self.set_interact_object(trigger_ids=[12000308], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=103)
            self.enable_spawn_point_pc(spawn_id=106, is_enable=True)
            return CableOn_07_08(self.ctx)


class Block_1_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5167):
            self.spawn_monster(spawn_ids=[1000001], auto_target=False)
            return Block_1_02(self.ctx)
        if self.monster_dead(spawn_ids=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000001], arg2=False)
            self.destroy_monster(spawn_ids=[1000002], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000307], state=1)
            self.set_interact_object(trigger_ids=[12000308], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=103)
            self.enable_spawn_point_pc(spawn_id=106, is_enable=True)
            return CableOn_07_08(self.ctx)


class Block_1_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4067):
            self.spawn_monster(spawn_ids=[1000002], auto_target=False)
            return Block_1(self.ctx)
        if self.monster_dead(spawn_ids=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000001], arg2=False)
            self.destroy_monster(spawn_ids=[1000002], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000307], state=1)
            self.set_interact_object(trigger_ids=[12000308], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=103)
            self.enable_spawn_point_pc(spawn_id=106, is_enable=True)
            return CableOn_07_08(self.ctx)


class Block_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1107,1203,1204,1213,1214,1215,1216,1217,1218]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000001], arg2=False)
            self.destroy_monster(spawn_ids=[1000002], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000307], state=1)
            self.set_interact_object(trigger_ids=[12000308], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=103)
            self.enable_spawn_point_pc(spawn_id=106, is_enable=True)
            return CableOn_07_08(self.ctx)


# ==========================================================================================================================================
class ArriveBlock_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            self.spawn_monster(spawn_ids=[2002], auto_target=False)
            return ArriveBlock_Delay_2(self.ctx)


class ArriveBlock_Delay_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$02020310_BF__FIELD_2__1$', duration=7000)
            return Block_2_01(self.ctx)
        if self.monster_dead(spawn_ids=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000003], arg2=False)
            self.destroy_monster(spawn_ids=[1000004], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000309], state=1)
            self.set_interact_object(trigger_ids=[12000310], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=104)
            self.enable_spawn_point_pc(spawn_id=107, is_enable=True)
            return CableOn_09_10(self.ctx)


class Block_2_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5167):
            self.spawn_monster(spawn_ids=[1000003], auto_target=False)
            return Block_2_02(self.ctx)
        if self.monster_dead(spawn_ids=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000003], arg2=False)
            self.destroy_monster(spawn_ids=[1000004], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000309], state=1)
            self.set_interact_object(trigger_ids=[12000310], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=104)
            self.enable_spawn_point_pc(spawn_id=107, is_enable=True)
            return CableOn_09_10(self.ctx)


class Block_2_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4067):
            self.spawn_monster(spawn_ids=[1000004], auto_target=False)
            return Block_2(self.ctx)
        if self.monster_dead(spawn_ids=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000003], arg2=False)
            self.destroy_monster(spawn_ids=[1000004], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000309], state=1)
            self.set_interact_object(trigger_ids=[12000310], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=104)
            self.enable_spawn_point_pc(spawn_id=107, is_enable=True)
            return CableOn_09_10(self.ctx)


class Block_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1108,1205,1206,1207,1208,1209,1210,1211,1212]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000003], arg2=False)
            self.destroy_monster(spawn_ids=[1000004], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000309], state=1)
            self.set_interact_object(trigger_ids=[12000310], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=104)
            self.enable_spawn_point_pc(spawn_id=107, is_enable=True)
            return CableOn_09_10(self.ctx)


# ==========================================================================================================================================
class ArriveBlock_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            self.spawn_monster(spawn_ids=[2003], auto_target=False)
            return ArriveBlock_Delay_3(self.ctx)


class ArriveBlock_Delay_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$02020310_BF__FIELD_2__2$', duration=7000)
            return Block_3_01(self.ctx)
        if self.monster_dead(spawn_ids=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000005], arg2=False)
            self.destroy_monster(spawn_ids=[1000006], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000311], state=1)
            self.set_interact_object(trigger_ids=[12000312], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=105)
            self.enable_spawn_point_pc(spawn_id=108, is_enable=True)
            return CableOn_11_12(self.ctx)


class Block_3_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5167):
            self.spawn_monster(spawn_ids=[1000005], auto_target=False)
            return Block_3_02(self.ctx)
        if self.monster_dead(spawn_ids=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000005], arg2=False)
            self.destroy_monster(spawn_ids=[1000006], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000311], state=1)
            self.set_interact_object(trigger_ids=[12000312], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=105)
            self.enable_spawn_point_pc(spawn_id=108, is_enable=True)
            return CableOn_11_12(self.ctx)


class Block_3_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4067):
            self.spawn_monster(spawn_ids=[1000006], auto_target=False)
            return Block_3(self.ctx)
        if self.monster_dead(spawn_ids=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000005], arg2=False)
            self.destroy_monster(spawn_ids=[1000006], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000311], state=1)
            self.set_interact_object(trigger_ids=[12000312], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=105)
            self.enable_spawn_point_pc(spawn_id=108, is_enable=True)
            return CableOn_11_12(self.ctx)


class Block_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1109,1201,1202,1219,1220,1221,1222,1223,1224]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000005], arg2=False)
            self.destroy_monster(spawn_ids=[1000006], arg2=False)
            self.destroy_monster(spawn_ids=[30001,30002,30003,30004], arg2=False)
            self.set_interact_object(trigger_ids=[12000311], state=1)
            self.set_interact_object(trigger_ids=[12000312], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            self.spawn_monster(spawn_ids=[1301,1302,1304,1305,1306,1307,1308,1309,1310], auto_target=False)
            self.spawn_monster(spawn_ids=[1311,1312,1314,1315,1316,1317,1318,1319,1320], auto_target=False)
            self.spawn_monster(spawn_ids=[1321,1322,1324,1325,1326,1327,1328,1329,1330], auto_target=False)
            self.spawn_monster(spawn_ids=[1331,1332], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=105)
            self.enable_spawn_point_pc(spawn_id=108, is_enable=True)
            return CableOn_11_12(self.ctx)


class CableOn_07_08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000307], state=0):
            self.set_interact_object(trigger_ids=[12000307], state=0)
            self.set_interact_object(trigger_ids=[12000308], state=0)
            self.spawn_monster(spawn_ids=[30005], auto_target=False)
            self.set_mesh(trigger_ids=[1101001,1101002,1101003,1101004,1101005,1101006,1101007,1101008,1101009,1101010])
            return CableDelay_07(self.ctx)
        if self.object_interacted(interact_ids=[12000308], state=0):
            self.set_interact_object(trigger_ids=[12000307], state=0)
            self.set_interact_object(trigger_ids=[12000308], state=0)
            self.spawn_monster(spawn_ids=[30006,30007], auto_target=False)
            self.set_mesh(trigger_ids=[1102001,1102002,1102003,1102004,1102005,1102006,1102007,1102008,1102009,1102010])
            return CableDelay_08(self.ctx)


class CableOn_09_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000309], state=0):
            self.set_interact_object(trigger_ids=[12000309], state=0)
            self.set_interact_object(trigger_ids=[12000310], state=0)
            self.spawn_monster(spawn_ids=[30008], auto_target=False)
            self.set_mesh(trigger_ids=[1103001,1103002,1103003,1103004,1103005,1103006,1103007,1103008,1103009,1103010])
            return CableDelay_09(self.ctx)
        if self.object_interacted(interact_ids=[12000310], state=0):
            self.set_interact_object(trigger_ids=[12000309], state=0)
            self.set_interact_object(trigger_ids=[12000310], state=0)
            self.spawn_monster(spawn_ids=[30009], auto_target=False)
            self.set_mesh(trigger_ids=[1104001,1104002,1104003,1104004,1104005,1104006,1104007,1104008,1104009,1104010])
            return CableDelay_10(self.ctx)


class CableOn_11_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000311], state=0):
            self.set_interact_object(trigger_ids=[12000311], state=0)
            self.set_interact_object(trigger_ids=[12000312], state=0)
            self.spawn_monster(spawn_ids=[30010,30011], auto_target=False)
            self.set_mesh(trigger_ids=[1105001,1105002,1105003,1105004,1105005,1105006,1105007,1105008,1105009,1105010])
            return CableDelay_11(self.ctx)
        if self.object_interacted(interact_ids=[12000312], state=0):
            self.set_interact_object(trigger_ids=[12000311], state=0)
            self.set_interact_object(trigger_ids=[12000312], state=0)
            self.spawn_monster(spawn_ids=[30012], auto_target=False)
            self.set_mesh(trigger_ids=[1106001,1106002,1106003,1106004,1106005,1106006,1106007,1106008,1106009,1106010])
            return CableDelay_12(self.ctx)


class CableDelay_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__3$', duration=3000)
            return CableDelay_07_2(self.ctx)


class CableDelay_08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__4$', duration=3000)
            return CableDelay_08_2(self.ctx)


class CableDelay_09(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__5$', duration=3000)
            return CableDelay_09_2(self.ctx)


class CableDelay_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__6$', duration=3000)
            return CableDelay_10_2(self.ctx)


class CableDelay_11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__7$', duration=3000)
            return CableDelay_11_2(self.ctx)


class CableDelay_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__8$', duration=3000)
            return CableDelay_12_2(self.ctx)


class CableDelay_07_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__9$', duration=1000)
            return CableDelay_07_3(self.ctx)


class CableDelay_08_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__10$', duration=1000)
            return CableDelay_08_3(self.ctx)


class CableDelay_09_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__11$', duration=1000)
            return CableDelay_09_3(self.ctx)


class CableDelay_10_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__12$', duration=1000)
            return CableDelay_10_3(self.ctx)


class CableDelay_11_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__13$', duration=1000)
            return CableDelay_11_3(self.ctx)


class CableDelay_12_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__14$', duration=1000)
            return CableDelay_12_3(self.ctx)


class CableDelay_07_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__15$', duration=1000)
            return CableDelay_07_4(self.ctx)


class CableDelay_08_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__16$', duration=1000)
            return CableDelay_08_4(self.ctx)


class CableDelay_09_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__17$', duration=1000)
            return CableDelay_09_4(self.ctx)


class CableDelay_10_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__18$', duration=1000)
            return CableDelay_10_4(self.ctx)


class CableDelay_11_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__19$', duration=1000)
            return CableDelay_11_4(self.ctx)


class CableDelay_12_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__20$', duration=1000)
            return CableDelay_12_4(self.ctx)


class CableDelay_07_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__21$', duration=1000)
            return CableDelay_07_5(self.ctx)


class CableDelay_08_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__22$', duration=1000)
            return CableDelay_08_5(self.ctx)


class CableDelay_09_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__23$', duration=1000)
            return CableDelay_09_5(self.ctx)


class CableDelay_10_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__24$', duration=1000)
            return CableDelay_10_5(self.ctx)


class CableDelay_11_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.move_npc(spawn_id=30010, patrol_name='MS2PatrolData_110')
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__25$', duration=1000)
            return CableDelay_11_5(self.ctx)


class CableDelay_12_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020310_BF__FIELD_2__26$', duration=1000)
            return CableDelay_12_5(self.ctx)


class CableDelay_07_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_normal', script='$02020310_BF__FIELD_2__27$', duration=6000)
            self.move_npc(spawn_id=30005, patrol_name='MS2PatrolData_105')
            self.set_breakable(trigger_ids=[1007], enable=True)
            return CableOff_07(self.ctx)


class CableDelay_08_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_normal', script='$02020310_BF__FIELD_2__28$', duration=6000)
            self.move_npc(spawn_id=30006, patrol_name='MS2PatrolData_106')
            self.move_npc(spawn_id=30007, patrol_name='MS2PatrolData_107')
            self.set_breakable(trigger_ids=[1008], enable=True)
            return CableOff_08(self.ctx)


class CableDelay_09_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_normal', script='$02020310_BF__FIELD_2__29$', duration=6000)
            self.move_npc(spawn_id=30008, patrol_name='MS2PatrolData_108')
            self.set_breakable(trigger_ids=[1009], enable=True)
            return CableOff_09(self.ctx)


class CableDelay_10_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_normal', script='$02020310_BF__FIELD_2__30$', duration=6000)
            self.move_npc(spawn_id=30009, patrol_name='MS2PatrolData_109')
            self.set_breakable(trigger_ids=[1010], enable=True)
            return CableOff_10(self.ctx)


class CableDelay_11_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_normal', script='$02020310_BF__FIELD_2__31$', duration=6000)
            self.move_npc(spawn_id=30011, patrol_name='MS2PatrolData_111')
            self.set_breakable(trigger_ids=[1011], enable=True)
            return CableOff_11(self.ctx)


class CableDelay_12_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_normal', script='$02020310_BF__FIELD_2__32$', duration=6000)
            self.move_npc(spawn_id=30012, patrol_name='MS2PatrolData_112')
            self.set_breakable(trigger_ids=[1012], enable=True)
            return CableOff_12(self.ctx)


class CableOff_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900004, key='Block', value=1)
            return End_02(self.ctx)


class CableOff_08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900004, key='Block', value=2)
            return End_02(self.ctx)


class CableOff_09(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900004, key='Block', value=2)
            return End_02(self.ctx)


class CableOff_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900004, key='Block', value=3)
            return End_02(self.ctx)


class CableOff_11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900004, key='Block', value=4)
            return End_02(self.ctx)


class CableOff_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900004, key='Block', value=1)
            return End_02(self.ctx)


class End_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대기(self.ctx)


initial_state = 대기
