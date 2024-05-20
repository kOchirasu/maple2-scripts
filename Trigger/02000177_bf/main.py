""" trigger/02000177_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001058], state=1)
        self.set_interact_object(trigger_ids=[10001059], state=1)
        self.set_interact_object(trigger_ids=[10001060], state=1)
        self.spawn_monster(spawn_ids=[101,102,103,104], auto_target=False)
        self.spawn_monster(spawn_ids=[110,111,112,113,114,115,116,117], auto_target=False)
        self.spawn_monster(spawn_ids=[120,121,122,123,124,125,126,127,128,129,130], auto_target=False)
        self.spawn_monster(spawn_ids=[141,142,143,144,145,146], auto_target=False)
        self.spawn_monster(spawn_ids=[150,151,152,153,154,155,156,157,158,159], auto_target=False)
        self.set_mesh(trigger_ids=[1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099])
        self.set_mesh(trigger_ids=[1300,1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311,1312,1313,1314,1315,1316,1317,1318,1319,1320,1321,1322,1323,1324,1325,1326,1327,1328,1329,1330,1331,1332,1333,1334,1335,1336,1337,1338,1339,1340,1341,1342,1343,1344,1345,1346,1347,1348,1349,1350,1351,1352,1353,1354,1355,1356,1357,1358,1359,1360,1361,1362,1363,1364,1365,1366,1367,1368,1369,1370,1371,1372,1373,1374,1375,1376,1377,1378,1379,1380,1381,1382,1383,1384,1385,1386,1387,1388,1389,1390,1391,1392,1393,1394,1395,1396,1397,1398,1399])
        self.set_mesh(trigger_ids=[741,742,743,744,745,746,747,748,749,750], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[999], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8001,8002])
        self.set_mesh(trigger_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110], fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Start_02(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class Start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000177_BF__MAIN__0$', arg3='3000', arg4='0')
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20001773, text_id=20001773, duration=4000)
        self.move_npc(spawn_id=999, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001058], state=0):
            return Step_2(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10001058], state=2)
        # self.set_mesh(trigger_ids=[741], fade=10.0)
        self.set_effect(trigger_ids=[6661])


class Step_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012], visible=True, interval=100, fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001059], state=0):
            return Step_3(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10001059], state=2)
        # self.set_mesh(trigger_ids=[742], fade=10.0)
        self.set_effect(trigger_ids=[6662])


class Step_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032], visible=True, interval=100, fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001060], state=0):
            return Step_4(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10001060], state=2)
        # self.set_mesh(trigger_ids=[743], fade=10.0)
        self.set_effect(trigger_ids=[6663])


class Step_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060], visible=True, interval=100, fade=10.0)


initial_state = idle
