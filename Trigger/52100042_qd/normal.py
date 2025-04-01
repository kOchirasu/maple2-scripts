""" trigger/52100042_qd/normal.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.spawn_monster(spawn_ids=[101,102,103,104,105], auto_target=False)
        self.set_mesh(trigger_ids=[1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917]) # 1층 피직
        self.set_mesh(trigger_ids=[1800,1801,1802,1803,1804,1805,1806,1807,1808,1809]) # 3층 피직
        # 1, 2, 3층 사다리 안보이기 처리
        self.set_ladder(trigger_ids=[1101])
        self.set_ladder(trigger_ids=[1102])
        self.set_ladder(trigger_ids=[1103])
        self.set_ladder(trigger_ids=[1104])
        self.set_ladder(trigger_ids=[1105])
        self.set_ladder(trigger_ids=[1106])
        self.set_ladder(trigger_ids=[1107])
        self.set_ladder(trigger_ids=[1108])
        self.set_ladder(trigger_ids=[1109])
        self.set_ladder(trigger_ids=[1110])
        self.set_ladder(trigger_ids=[1111])
        self.set_ladder(trigger_ids=[1112])
        self.set_ladder(trigger_ids=[1113])
        self.set_ladder(trigger_ids=[1114])
        self.set_ladder(trigger_ids=[1115])
        self.set_ladder(trigger_ids=[1116])
        self.set_ladder(trigger_ids=[1117])
        self.set_ladder(trigger_ids=[1118])
        self.set_ladder(trigger_ids=[1201])
        self.set_ladder(trigger_ids=[1202])
        self.set_ladder(trigger_ids=[1203])
        self.set_ladder(trigger_ids=[1204])
        self.set_ladder(trigger_ids=[1205])
        self.set_ladder(trigger_ids=[1206])
        self.set_ladder(trigger_ids=[1207])
        self.set_ladder(trigger_ids=[1208])
        self.set_ladder(trigger_ids=[1209])
        self.set_ladder(trigger_ids=[1210])
        self.set_ladder(trigger_ids=[1211])
        self.set_ladder(trigger_ids=[1212])
        self.set_ladder(trigger_ids=[1213])
        self.set_ladder(trigger_ids=[1214])
        self.set_ladder(trigger_ids=[1215])
        self.set_ladder(trigger_ids=[1216])
        self.set_ladder(trigger_ids=[1217])
        self.set_ladder(trigger_ids=[1218])
        self.set_ladder(trigger_ids=[1301])
        self.set_ladder(trigger_ids=[1302])
        self.set_ladder(trigger_ids=[1303])
        self.set_ladder(trigger_ids=[1304])
        self.set_ladder(trigger_ids=[1305])
        self.set_ladder(trigger_ids=[1306])
        self.set_ladder(trigger_ids=[1307])
        self.set_ladder(trigger_ids=[1308])
        self.set_ladder(trigger_ids=[1309])
        self.set_ladder(trigger_ids=[1310])
        self.set_ladder(trigger_ids=[1311])
        self.set_ladder(trigger_ids=[1312])
        self.set_ladder(trigger_ids=[1313])
        self.set_ladder(trigger_ids=[1314])
        self.set_ladder(trigger_ids=[1315])
        self.set_ladder(trigger_ids=[1316])
        self.set_ladder(trigger_ids=[1317])
        self.set_ladder(trigger_ids=[1318])
        self.set_ladder(trigger_ids=[1401])
        self.set_ladder(trigger_ids=[1402])
        self.set_ladder(trigger_ids=[1403])
        self.set_ladder(trigger_ids=[1404])
        self.set_ladder(trigger_ids=[1405])
        self.set_ladder(trigger_ids=[1406])
        self.set_ladder(trigger_ids=[1407])
        self.set_ladder(trigger_ids=[1408])
        self.set_ladder(trigger_ids=[1409])
        self.set_ladder(trigger_ids=[1410])
        self.set_ladder(trigger_ids=[1411])
        self.set_ladder(trigger_ids=[1412])
        self.set_ladder(trigger_ids=[1413])
        self.set_ladder(trigger_ids=[1414])
        self.set_ladder(trigger_ids=[1415])
        self.set_ladder(trigger_ids=[1416])
        self.set_ladder(trigger_ids=[1417])
        self.set_ladder(trigger_ids=[1418])
        self.set_ladder(trigger_ids=[1501])
        self.set_ladder(trigger_ids=[1502])
        self.set_ladder(trigger_ids=[1503])
        self.set_ladder(trigger_ids=[1504])
        self.set_ladder(trigger_ids=[1505])
        self.set_ladder(trigger_ids=[1506])
        self.set_ladder(trigger_ids=[1507])
        self.set_ladder(trigger_ids=[1508])
        self.set_ladder(trigger_ids=[1509])
        self.set_ladder(trigger_ids=[1510])
        self.set_ladder(trigger_ids=[1511])
        self.set_ladder(trigger_ids=[1512])
        self.set_ladder(trigger_ids=[1513])
        self.set_ladder(trigger_ids=[1514])
        self.set_ladder(trigger_ids=[1515])
        self.set_ladder(trigger_ids=[1516])
        self.set_ladder(trigger_ids=[1517])
        self.set_ladder(trigger_ids=[1518])
        self.set_ladder(trigger_ids=[1601])
        self.set_ladder(trigger_ids=[1602])
        self.set_ladder(trigger_ids=[1603])
        self.set_ladder(trigger_ids=[1604])
        self.set_ladder(trigger_ids=[1605])
        self.set_ladder(trigger_ids=[1606])
        self.set_ladder(trigger_ids=[1607])
        self.set_ladder(trigger_ids=[1608])
        self.set_ladder(trigger_ids=[1609])
        self.set_ladder(trigger_ids=[1610])
        self.set_ladder(trigger_ids=[1611])
        self.set_ladder(trigger_ids=[1612])
        self.set_ladder(trigger_ids=[1613])
        self.set_ladder(trigger_ids=[1614])
        self.set_ladder(trigger_ids=[1615])
        self.set_ladder(trigger_ids=[1616])
        self.set_ladder(trigger_ids=[1617])
        self.set_ladder(trigger_ids=[1618])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104,105]):
            return step_02(self.ctx)


class step_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917], visible=True) # 1층 피직
        # 1, 2, 3층 사다리 보이기 처리
        self.set_ladder(trigger_ids=[1101], visible=True, enable=True, fade=1)
        self.set_ladder(trigger_ids=[1102], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1103], visible=True, enable=True, fade=3)
        self.set_ladder(trigger_ids=[1104], visible=True, enable=True, fade=4)
        self.set_ladder(trigger_ids=[1105], visible=True, enable=True, fade=5)
        self.set_ladder(trigger_ids=[1106], visible=True, enable=True, fade=6)
        self.set_ladder(trigger_ids=[1107], visible=True, enable=True, fade=7)
        self.set_ladder(trigger_ids=[1108], visible=True, enable=True, fade=8)
        self.set_ladder(trigger_ids=[1109], visible=True, enable=True, fade=9)
        self.set_ladder(trigger_ids=[1110], visible=True, enable=True, fade=10)
        self.set_ladder(trigger_ids=[1111], visible=True, enable=True, fade=11)
        self.set_ladder(trigger_ids=[1112], visible=True, enable=True, fade=12)
        self.set_ladder(trigger_ids=[1113], visible=True, enable=True, fade=13)
        self.set_ladder(trigger_ids=[1114], visible=True, enable=True, fade=14)
        self.set_ladder(trigger_ids=[1115], visible=True, enable=True, fade=15)
        self.set_ladder(trigger_ids=[1116], visible=True, enable=True, fade=16)
        self.set_ladder(trigger_ids=[1117], visible=True, enable=True, fade=17)
        self.set_ladder(trigger_ids=[1118], visible=True, enable=True, fade=18)
        self.set_ladder(trigger_ids=[1201], visible=True, enable=True, fade=1)
        self.set_ladder(trigger_ids=[1202], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1203], visible=True, enable=True, fade=3)
        self.set_ladder(trigger_ids=[1204], visible=True, enable=True, fade=4)
        self.set_ladder(trigger_ids=[1205], visible=True, enable=True, fade=5)
        self.set_ladder(trigger_ids=[1206], visible=True, enable=True, fade=6)
        self.set_ladder(trigger_ids=[1207], visible=True, enable=True, fade=7)
        self.set_ladder(trigger_ids=[1208], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1209], visible=True, enable=True, fade=8)
        self.set_ladder(trigger_ids=[1210], visible=True, enable=True, fade=9)
        self.set_ladder(trigger_ids=[1211], visible=True, enable=True, fade=10)
        self.set_ladder(trigger_ids=[1212], visible=True, enable=True, fade=11)
        self.set_ladder(trigger_ids=[1213], visible=True, enable=True, fade=12)
        self.set_ladder(trigger_ids=[1214], visible=True, enable=True, fade=13)
        self.set_ladder(trigger_ids=[1215], visible=True, enable=True, fade=14)
        self.set_ladder(trigger_ids=[1216], visible=True, enable=True, fade=15)
        self.set_ladder(trigger_ids=[1217], visible=True, enable=True, fade=16)
        self.set_ladder(trigger_ids=[1218], visible=True, enable=True, fade=17)
        self.set_ladder(trigger_ids=[1301], visible=True, enable=True, fade=1)
        self.set_ladder(trigger_ids=[1302], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1303], visible=True, enable=True, fade=3)
        self.set_ladder(trigger_ids=[1304], visible=True, enable=True, fade=4)
        self.set_ladder(trigger_ids=[1305], visible=True, enable=True, fade=5)
        self.set_ladder(trigger_ids=[1306], visible=True, enable=True, fade=6)
        self.set_ladder(trigger_ids=[1307], visible=True, enable=True, fade=7)
        self.set_ladder(trigger_ids=[1308], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1309], visible=True, enable=True, fade=8)
        self.set_ladder(trigger_ids=[1310], visible=True, enable=True, fade=9)
        self.set_ladder(trigger_ids=[1311], visible=True, enable=True, fade=10)
        self.set_ladder(trigger_ids=[1312], visible=True, enable=True, fade=11)
        self.set_ladder(trigger_ids=[1313], visible=True, enable=True, fade=12)
        self.set_ladder(trigger_ids=[1314], visible=True, enable=True, fade=13)
        self.set_ladder(trigger_ids=[1315], visible=True, enable=True, fade=14)
        self.set_ladder(trigger_ids=[1316], visible=True, enable=True, fade=15)
        self.set_ladder(trigger_ids=[1317], visible=True, enable=True, fade=16)
        self.set_ladder(trigger_ids=[1318], visible=True, enable=True, fade=17)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return step_03(self.ctx)


class step_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.spawn_monster(spawn_ids=[201,202,203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203]):
            return step_04(self.ctx)


class step_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.set_ladder(trigger_ids=[1401], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1402], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1403], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1404], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1405], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1406], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1407], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1408], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1409], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1410], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1411], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1412], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1413], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1414], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1415], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1416], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1417], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1418], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1501], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1502], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1503], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1504], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1505], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1506], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1507], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1508], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1509], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1510], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1511], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1512], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1513], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1514], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1515], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1516], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1517], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1518], visible=True, enable=True, fade=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703]):
            return step_05(self.ctx)


class step_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.spawn_monster(spawn_ids=[301,302,303], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[301,302,303]):
            return step_06(self.ctx)


class step_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='LadderGoBossRoom') == 1:
            return step_07(self.ctx)


class step_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1800,1801,1802,1803,1804,1805,1806,1807,1808,1809], visible=True) # 3층 피직
        self.set_ladder(trigger_ids=[1601], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1602], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1603], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1604], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1605], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1606], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1607], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1608], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1609], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1610], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1611], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1612], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1613], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1614], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1615], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1616], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1617], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1618], visible=True, enable=True, fade=2)


initial_state = idle
