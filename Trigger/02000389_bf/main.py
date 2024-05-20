""" trigger/02000389_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=11001, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=11002)
        self.spawn_monster(spawn_ids=[101,102])
        self.set_mesh(trigger_ids=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827,1828,1829,1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850,1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871,1872,1873,1874,1875,1876,1877,1878,1879,1880,1881,1882,1883,1884,1885,1886,1887,1888,1889,1890,1891,1892,1893,1894,1895,1896,1897,1898,1899,1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000]) # 배 안에서 차오르는 물
        self.set_effect(trigger_ids=[7001])
        self.set_effect(trigger_ids=[7002])
        self.set_effect(trigger_ids=[7003])
        self.set_effect(trigger_ids=[7004])
        self.set_effect(trigger_ids=[7005])
        self.set_effect(trigger_ids=[7011])
        self.set_effect(trigger_ids=[7012])
        self.set_effect(trigger_ids=[7013])
        self.set_mesh(trigger_ids=[3007,3008,3009], visible=True)
        self.set_actor(trigger_id=3001, visible=True, initial_sequence='Run_A')
        self.set_actor(trigger_id=3002, visible=True, initial_sequence='Run_A')
        self.set_actor(trigger_id=3003, visible=True, initial_sequence='Run_A')
        self.set_actor(trigger_id=3004, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=3005, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=3006, visible=True, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=3101, initial_sequence='Run_A')
        self.set_actor(trigger_id=3102, initial_sequence='Run_A')
        self.set_actor(trigger_id=3103, initial_sequence='Run_A')
        self.set_actor(trigger_id=3104, initial_sequence='Run_A')
        self.set_breakable(trigger_ids=[1801,1802,1803,1804,1805,1806,1807])
        self.set_local_camera(camera_id=8100) # LocalTargetCamera
        self.set_local_camera(camera_id=8101) # LocalTargetCamera
        self.set_mesh(trigger_ids=[1001])
        self.set_mesh(trigger_ids=[1990,1991,1992,1993], visible=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_mesh(trigger_ids=[3007,3008,3009])
        # self.set_actor(trigger_id=3001, initial_sequence='Run_A')
        # self.set_actor(trigger_id=3002, initial_sequence='Run_A')
        # self.set_actor(trigger_id=3003, initial_sequence='Run_A')
        # self.set_actor(trigger_id=3004, initial_sequence='Attack_Idle_A')
        # self.set_actor(trigger_id=3005, initial_sequence='Attack_Idle_A')
        # self.set_actor(trigger_id=3006, initial_sequence='Attack_Idle_A')
        self.set_skip(state=start_ready)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Walk_A', duration=10000000000000000.0)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Walk_A', duration=10000000000000000.0)
        self.select_camera_path(path_ids=[8001,8002,8003], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ready_02(self.ctx)


class ready_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000389_BF__MAIN__0$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000389_BF__MAIN__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_ready(self.ctx)


class start_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8100, enable=True) # LocalTargetCamera
        self.spawn_monster(spawn_ids=[201,202,203,204,205], auto_target=False)
        self.set_dialogue(type=1, spawn_id=201, script='$02000389_BF__MAIN__2$', time=2, arg5=5)
        self.set_dialogue(type=1, spawn_id=202, script='$02000389_BF__MAIN__3$', time=2, arg5=4)
        self.set_dialogue(type=1, spawn_id=204, script='$02000389_BF__MAIN__4$', time=2, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204,205]):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[206,207,208,209], auto_target=False)
        self.set_event_ui(type=1, arg2='$02000389_BF__MAIN__5$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[206,207,208,209]):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[210,211,212,213,214], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[210,211,212,213,214]):
            return scene_04(self.ctx)


class scene_04_ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=scene_07_ready)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8004,8005,8006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000389_BF__MAIN__6$', time=2)
        self.set_dialogue(type=1, spawn_id=101, script='$02000389_BF__MAIN__7$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2003')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_07_ready(self.ctx)


class scene_07_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_actor(trigger_id=3001, initial_sequence='Run_A')
        self.set_actor(trigger_id=3002, initial_sequence='Run_A')
        self.set_actor(trigger_id=3003, initial_sequence='Run_A')
        self.set_actor(trigger_id=3004, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=3005, initial_sequence='Attack_Idle_A')
        self.set_actor(trigger_id=3006, initial_sequence='Attack_Idle_A')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_local_camera(camera_id=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[214], auto_target=False)
        self.spawn_monster(spawn_ids=[206,207,208], auto_target=False)
        self.spawn_monster(spawn_ids=[201,202,203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return boss_leftTurn(self.ctx)


# 보스 좌현 공격
class boss_leftTurn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[302], auto_target=False)
        self.set_onetime_effect(id=1, enable=True, path='BG\\Common\\Sound\\Eff_Object_WaterJump_Splash_01.xml')
        self.set_dialogue(type=1, spawn_id=302, script='$02000389_BF__MAIN__8$', time=3)
        self.set_dialogue(type=1, spawn_id=302, script='$02000389_BF__MAIN__9$', time=2, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return boss_leftTurn_01(self.ctx)


class boss_leftTurn_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=302, sequence_name='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            return boss_leftTurn_02(self.ctx)


class boss_leftTurn_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7002], visible=True)
        self.set_skill(trigger_ids=[30002], enable=True)
        self.set_skill(trigger_ids=[30010], enable=True) # 적
        self.set_skill(trigger_ids=[30011], enable=True) # 아군
        self.enable_spawn_point_pc(spawn_id=11002, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=11001)
        self.set_user_value(trigger_id=10000002, key='Error', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return boss_leftTurn_03(self.ctx)


class boss_leftTurn_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[215,216,217,218], auto_target=False)
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return boss_leftTurn_04(self.ctx)


class boss_leftTurn_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[302])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            return boss_rightTurn(self.ctx)


# 보스 우현 공격
class boss_rightTurn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, enable=True, path='BG\\Common\\Sound\\Eff_Object_WaterJump_Splash_01.xml')
        self.spawn_monster(spawn_ids=[301], auto_target=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2003')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2003')
        self.set_dialogue(type=1, spawn_id=301, script='$02000389_BF__MAIN__10$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return boss_rightTurn_01(self.ctx)


class boss_rightTurn_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            return boss_rightTurn_02(self.ctx)


class boss_rightTurn_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001], visible=True)
        self.set_skill(trigger_ids=[30001], enable=True)
        self.set_skill(trigger_ids=[30010], enable=True) # 적
        self.set_skill(trigger_ids=[30011], enable=True) # 아군

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return boss_rightTurn_03(self.ctx)


class boss_rightTurn_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[219,220,222,223], auto_target=False)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return boss_rightTurn_04(self.ctx)


class boss_rightTurn_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[301])
        self.set_mesh(trigger_ids=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827,1828,1829,1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850,1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871,1872,1873,1874,1875,1876,1877,1878,1879,1880,1881,1882,1883,1884,1885,1886,1887,1888,1889,1890,1891,1892,1893,1894,1895,1896,1897,1898,1899,1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000], visible=True, start_delay=800, interval=50, fade=50.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return boss_leftTurn_b(self.ctx)


# 보스 좌현 공격 2
class boss_leftTurn_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=11, enable=True, path='BG\\Common\\Sound\\Eff_Object_WaterJump_Splash_01.xml')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2003')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2003')
        self.spawn_monster(spawn_ids=[305], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return boss_leftTurn_b_01(self.ctx)


class boss_leftTurn_b_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 난파가 될 시 멈출 블록들
        self.set_dialogue(type=1, spawn_id=305, script='$02000389_BF__MAIN__11$', time=3)
        self.set_breakable(trigger_ids=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246,1247,1248,1249,1250,1251,1252,1253,1254,1255,1256,1257,1258,1259,1260,1261,1262,1263,1264,1265,1266,1267,1268,1269,1270,1271,1272,1273,1274,1275,1276,1277,1278,1279,1280,1281,1282,1283,1284,1285,1286,1287,1288,1289,1290,1291,1292,1293,1294,1295,1296,1297,1298,1299,1300,1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311,1312,1313,1314,1315,1316,1317,1318,1319,1320,1321,1322,1323,1324,1325,1326,1327,1328,1329,1330,1331,1332,1333,1334,1335,1336,1337,1338,1339,1340,1341,1342,1343,1344,1345,1346,1347,1348,1349,1350,1351,1352,1353,1354])
        self.set_breakable(trigger_ids=[1356,1357,1358,1359,1360,1361,1362,1363,1364,1365,1366,1367,1368,1369,1370,1371,1372,1373,1374,1375,1376,1377,1378,1379,1380,1381,1382,1383,1384,1385,1386,1387,1388,1389,1390,1391,1392,1393,1394,1395,1396,1397,1398,1399,1400,1401,1402,1403,1404,1405,1406,1407,1408,1409,1410,1411,1412,1413,1414,1415,1416,1417,1418,1419,1420,1421,1422,1423,1424,1425,1426,1427,1428,1429,1430,1431,1432,1433,1434,1435,1436,1437,1438,1439,1440,1441,1442,1443,1444,1445,1446,1447,1448,1449,1450,1451,1452,1453,1454,1455,1456,1457,1458,1459,1460,1461,1462,1463,1464,1465,1466,1467,1468,1469,1470,1471,1472,1473,1474,1475,1476,1477,1478,1479,1480,1481,1482,1483,1484,1485,1486,1487,1488,1489,1490,1491,1492,1493,1494,1495,1496,1497,1498,1499,1500,1501,1502,1503,1504,1505,1506,1507,1508,1509])
        self.set_breakable(trigger_ids=[1509,1510,1511,1512,1513,1514,1515,1516,1517,1518,1519,1520,1521,1522,1523,1524,1525,1526,1527,1528,1529,1530,1531,1532,1533,1534,1535,1536,1537,1538,1539,1540,1541,1542,1543,1544,1545,1546,1547,1548,1549,1550,1551,1552,1553,1554,1555,1556,1557,1558,1559,1560,1561,1562,1563,1564,1565,1566,1567,1568,1569,1570,1571,1572,1573,1574,1575,1576,1577,1578,1579,1580,1581,1582,1583,1584,1585,1586,1587,1588,1589,1590,1591,1592,1593,1594,1595,1596,1597,1598,1599,1600,1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640,1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660,1661,1662])
        self.set_breakable(trigger_ids=[1662,1663,1664,1665,1666,1667,1668,1669,1670,1671,1672,1673,1674,1675,1676,1677,1678,1679,1680,1681,1682,1683,1684,1685,1686,1687,1688,1689,1690,1691,1692,1693,1694,1695,1696,1697,1698,1699,1700,1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799,1800,1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815])
        self.set_npc_emotion_sequence(spawn_id=305, sequence_name='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return boss_leftTurn_b_02(self.ctx)


class boss_leftTurn_b_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7005], visible=True)
        self.set_skill(trigger_ids=[30005], enable=True)
        self.set_skill(trigger_ids=[30010], enable=True) # 적
        self.set_skill(trigger_ids=[30011], enable=True) # 아군

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return boss_leftTurn_b_03(self.ctx)


class boss_leftTurn_b_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=305, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return boss_leftTurn_b_04_ready(self.ctx)


class boss_leftTurn_b_04_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            return boss_leftTurn_b_04(self.ctx)


class boss_leftTurn_b_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[305])
        self.destroy_monster(spawn_ids=[303,101,102])
        self.spawn_monster(spawn_ids=[103,104], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ending_01(self.ctx)


class Ending_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=Ending_03_ready)
        self.set_mesh(trigger_ids=[1990,1991,1992,1993])
        self.set_actor(trigger_id=3101, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=3102, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=3103, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=3104, visible=True, initial_sequence='Idle_A')
        self.select_camera_path(path_ids=[8007], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_dialogue(type=1, spawn_id=104, script='$02000389_BF__MAIN__12$', time=2)
        self.set_dialogue(type=1, spawn_id=103, script='$02000389_BF__MAIN__13$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Ending_02(self.ctx)

    def on_exit(self) -> None:
        self.reset_camera()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


class Ending_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return End(self.ctx)


class Ending_03_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_local_camera(camera_id=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8100, enable=True) # LocalTargetCamera
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        self.set_effect(trigger_ids=[7001])
        self.set_effect(trigger_ids=[7002])
        self.set_effect(trigger_ids=[7003])
        self.set_effect(trigger_ids=[7004])
        self.set_effect(trigger_ids=[7005])
        self.set_effect(trigger_ids=[7011])
        self.set_effect(trigger_ids=[7012])
        self.set_effect(trigger_ids=[7013])
        self.set_dialogue(type=1, spawn_id=104, script='$02000389_BF__MAIN__14$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=103, script='$02000389_BF__MAIN__15$', time=2, arg5=4)
        self.set_dialogue(type=1, spawn_id=104, script='$02000389_BF__MAIN__16$', time=2, arg5=7)
        self.set_dialogue(type=1, spawn_id=103, script='$02000389_BF__MAIN__17$', time=2, arg5=9)


initial_state = idle
