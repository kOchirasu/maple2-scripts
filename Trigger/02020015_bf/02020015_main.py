""" trigger/02020015_bf/02020015_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019])
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122])
        self.set_mesh(trigger_ids=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246,1247,1248,1249,1250,1251,1252,1253,1254,1255])
        self.set_mesh(trigger_ids=[1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311,1312,1313,1314,1315,1316,1317,1318,1319,1320,1321,1322,1323,1324,1325,1326,1327,1328,1329,1330,1331,1332,1333,1334,1335,1336,1337,1338,1339,1340,1341,1342,1343,1344,1345,1346,1347,1348], visible=True)
        self.set_cube(trigger_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410,1411,1412,1413,1414,1415,1416,1417,1418,1419,1420,1421,1422,1423,1424,1425,1426,1427,1428,1429,1430,1431,1432,1433,1434,1435,1436,1437,1438,1439,1440,1441,1442,1443,1444,1445,1446,1447,1448])
        self.set_user_value(trigger_id=99990002, key='Timer', value=0)
        self.set_ladder(trigger_ids=[2001])
        self.set_ladder(trigger_ids=[2002])
        self.set_ladder(trigger_ids=[2003])
        self.set_ladder(trigger_ids=[2004])
        self.set_ladder(trigger_ids=[2005])
        self.set_ladder(trigger_ids=[2006])
        self.set_ladder(trigger_ids=[2007])
        self.set_ladder(trigger_ids=[2008])
        self.set_ladder(trigger_ids=[2009])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 엘리베이터(self.ctx)


class 엘리베이터(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            return 복도(self.ctx)


class 복도(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.spawn_monster(spawn_ids=[111,112,113,114,115], auto_target=False)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            return 내부진입(self.ctx)


class 내부진입(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[903], job_code=0):
            return 발판생성(self.ctx)


class 발판생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='20초 후 발판이 사라집니다.', arg3='3000')
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019], visible=True)
        self.set_user_value(trigger_id=99990002, key='Timer', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 보스전(self.ctx)


class 보스전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.set_mesh(trigger_ids=[1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311,1312,1313,1314,1315,1316,1317,1318,1319,1320,1321,1322,1323,1324,1325,1326,1327,1328,1329,1330,1331,1332,1333,1334,1335,1336,1337,1338,1339,1340,1341,1342,1343,1344,1345,1346,1347,1348])
        self.set_cube(trigger_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410,1411,1412,1413,1414,1415,1416,1417,1418,1419,1420,1421,1422,1423,1424,1425,1426,1427,1428,1429,1430,1431,1432,1433,1434,1435,1436,1437,1438,1439,1440,1441,1442,1443,1444,1445,1446,1447,1448], is_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 감지
