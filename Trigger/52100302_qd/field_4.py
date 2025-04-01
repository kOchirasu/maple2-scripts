""" trigger/52100302_qd/field_4.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000519], state=2)
        self.set_interact_object(trigger_ids=[12000520], state=2)
        self.set_interact_object(trigger_ids=[12000521], state=2)
        # self.set_visible_breakable_object(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])
        # self.set_visible_breakable_object(trigger_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
        # self.set_visible_breakable_object(trigger_ids=[1021,1022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block') == 1:
            self.set_user_value(trigger_id=900005, key='Block', value=0)
            return ArriveBlock_1(self.ctx)
        if self.user_value(key='Block') == 2:
            self.set_user_value(trigger_id=900005, key='Block', value=0)
            return ArriveBlock_2(self.ctx)
        if self.user_value(key='Block') == 3:
            self.set_user_value(trigger_id=900005, key='Block', value=0)
            return ArriveBlock_3(self.ctx)


class ArriveBlock_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9008]):
            self.spawn_monster(spawn_ids=[2008], auto_target=False)
            return ArriveBlock_Delay_1(self.ctx)


class ArriveBlock_Delay_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Block_1_01(self.ctx)
        if self.monster_dead(spawn_ids=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000007], arg2=False)
            self.destroy_monster(spawn_ids=[1000008], arg2=False)
            self.set_interact_object(trigger_ids=[12000519], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=109)
            self.enable_spawn_point_pc(spawn_id=110)
            self.enable_spawn_point_pc(spawn_id=111)
            self.enable_spawn_point_pc(spawn_id=113, is_enable=True)
            return CableOn_19(self.ctx)


class Block_1_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5167):
            self.spawn_monster(spawn_ids=[1000007], auto_target=False)
            return Block_1_02(self.ctx)
        if self.monster_dead(spawn_ids=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000007], arg2=False)
            self.destroy_monster(spawn_ids=[1000008], arg2=False)
            self.set_interact_object(trigger_ids=[12000519], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=109)
            self.enable_spawn_point_pc(spawn_id=110)
            self.enable_spawn_point_pc(spawn_id=111)
            self.enable_spawn_point_pc(spawn_id=113, is_enable=True)
            return CableOn_19(self.ctx)


class Block_1_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4067):
            self.spawn_monster(spawn_ids=[1000008], auto_target=False)
            return Block_1(self.ctx)
        if self.monster_dead(spawn_ids=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000007], arg2=False)
            self.destroy_monster(spawn_ids=[1000008], arg2=False)
            self.set_interact_object(trigger_ids=[12000519], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=109)
            self.enable_spawn_point_pc(spawn_id=110)
            self.enable_spawn_point_pc(spawn_id=111)
            self.enable_spawn_point_pc(spawn_id=113, is_enable=True)
            return CableOn_19(self.ctx)


class Block_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1114,1401,1402,1407,1408,1409,1410,1411,1412,1413,1414,1415]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000007], arg2=False)
            self.destroy_monster(spawn_ids=[1000008], arg2=False)
            self.set_interact_object(trigger_ids=[12000519], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=109)
            self.enable_spawn_point_pc(spawn_id=110)
            self.enable_spawn_point_pc(spawn_id=111)
            self.enable_spawn_point_pc(spawn_id=113, is_enable=True)
            return CableOn_19(self.ctx)


class ArriveBlock_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9009]):
            self.spawn_monster(spawn_ids=[2009], auto_target=False)
            return ArriveBlock_Delay_2(self.ctx)


class ArriveBlock_Delay_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Block_2_01(self.ctx)
        if self.monster_dead(spawn_ids=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000009], arg2=False)
            self.destroy_monster(spawn_ids=[1000010], arg2=False)
            self.set_interact_object(trigger_ids=[12000520], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=110)
            self.enable_spawn_point_pc(spawn_id=111)
            self.enable_spawn_point_pc(spawn_id=114, is_enable=True)
            return CableOn_20(self.ctx)


class Block_2_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5167):
            self.spawn_monster(spawn_ids=[1000009], auto_target=False)
            return Block_2_02(self.ctx)
        if self.monster_dead(spawn_ids=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000009], arg2=False)
            self.destroy_monster(spawn_ids=[1000010], arg2=False)
            self.set_interact_object(trigger_ids=[12000520], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=110)
            self.enable_spawn_point_pc(spawn_id=111)
            self.enable_spawn_point_pc(spawn_id=114, is_enable=True)
            return CableOn_20(self.ctx)


class Block_2_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4067):
            self.spawn_monster(spawn_ids=[1000010], auto_target=False)
            return Block_2(self.ctx)
        if self.monster_dead(spawn_ids=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000009], arg2=False)
            self.destroy_monster(spawn_ids=[1000010], arg2=False)
            self.set_interact_object(trigger_ids=[12000520], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=110)
            self.enable_spawn_point_pc(spawn_id=111)
            self.enable_spawn_point_pc(spawn_id=114, is_enable=True)
            return CableOn_20(self.ctx)


class Block_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1115,1403,1404,1424,1425,1426,1427,1428,1429,1430]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000009], arg2=False)
            self.destroy_monster(spawn_ids=[1000010], arg2=False)
            self.set_interact_object(trigger_ids=[12000520], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=110)
            self.enable_spawn_point_pc(spawn_id=111)
            self.enable_spawn_point_pc(spawn_id=114, is_enable=True)
            return CableOn_20(self.ctx)


class ArriveBlock_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9010]):
            self.spawn_monster(spawn_ids=[2010], auto_target=False)
            return ArriveBlock_Delay_3(self.ctx)


class ArriveBlock_Delay_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Block_3_01(self.ctx)
        if self.monster_dead(spawn_ids=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000011], arg2=False)
            self.destroy_monster(spawn_ids=[1000012], arg2=False)
            self.set_interact_object(trigger_ids=[12000521], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=112)
            self.enable_spawn_point_pc(spawn_id=115, is_enable=True)
            return CableOn_21(self.ctx)


class Block_3_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5167):
            self.spawn_monster(spawn_ids=[1000011], auto_target=False)
            return Block_3_02(self.ctx)
        if self.monster_dead(spawn_ids=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000011], arg2=False)
            self.destroy_monster(spawn_ids=[1000012], arg2=False)
            self.set_interact_object(trigger_ids=[12000521], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=112)
            self.enable_spawn_point_pc(spawn_id=115, is_enable=True)
            return CableOn_21(self.ctx)


class Block_3_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4067):
            self.spawn_monster(spawn_ids=[1000012], auto_target=False)
            return Block_3(self.ctx)
        if self.monster_dead(spawn_ids=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000011], arg2=False)
            self.destroy_monster(spawn_ids=[1000012], arg2=False)
            self.set_interact_object(trigger_ids=[12000521], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=112)
            self.enable_spawn_point_pc(spawn_id=115, is_enable=True)
            return CableOn_21(self.ctx)


class Block_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1116,1405,1406,1416,1417,1418,1419,1420,1421,1422,1423]):
            self.set_ai_extra_data(key='BossDie', value=2)
            self.destroy_monster(spawn_ids=[1000011], arg2=False)
            self.destroy_monster(spawn_ids=[1000012], arg2=False)
            self.set_interact_object(trigger_ids=[12000521], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            self.spawn_monster(spawn_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], auto_target=False)
            self.spawn_monster(spawn_ids=[1511,1512,1513], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=112)
            self.enable_spawn_point_pc(spawn_id=115, is_enable=True)
            return CableOn_21(self.ctx)


class CableOn_19(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000519], state=0):
            self.set_interact_object(trigger_ids=[12000519], state=0)
            self.set_mesh(trigger_ids=[1210001,1210002,1210003,1210004,1210005,1210006,1210007,1210008,1210009,1210010])
            return CableDelay_19(self.ctx)


class CableOn_20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000520], state=0):
            self.set_interact_object(trigger_ids=[12000520], state=0)
            self.set_mesh(trigger_ids=[1310001,1310002,1310003,1310004,1310005,1310006,1310007,1310008,1310009,1310010])
            return CableDelay_20(self.ctx)


class CableOn_21(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000521], state=0):
            self.set_interact_object(trigger_ids=[12000521], state=0)
            self.set_mesh(trigger_ids=[1410001,1410002,1410003,1410004,1410005,1410006,1410007,1410008,1410009,1410010])
            return CableDelay_21(self.ctx)


class CableDelay_19(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__0$', duration=3000)
            return CableDelay_19_2(self.ctx)


class CableDelay_20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__1$', duration=3000)
            return CableDelay_20_2(self.ctx)


class CableDelay_21(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__2$', duration=3000)
            return CableDelay_21_2(self.ctx)


class CableDelay_19_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__3$', duration=1000)
            return CableDelay_19_3(self.ctx)


class CableDelay_20_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__4$', duration=1000)
            return CableDelay_20_3(self.ctx)


class CableDelay_21_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__5$', duration=1000)
            return CableDelay_21_3(self.ctx)


class CableDelay_19_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__6$', duration=1000)
            return CableDelay_19_4(self.ctx)


class CableDelay_20_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__7$', duration=1000)
            return CableDelay_20_4(self.ctx)


class CableDelay_21_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__8$', duration=1000)
            return CableDelay_21_4(self.ctx)


class CableDelay_19_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__9$', duration=1000)
            return CableDelay_19_5(self.ctx)


class CableDelay_20_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__10$', duration=1000)
            return CableDelay_20_5(self.ctx)


class CableDelay_21_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_4__11$', duration=1000)
            return CableDelay_21_5(self.ctx)


class CableDelay_19_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_4__12$', duration=5000)
            self.set_breakable(trigger_ids=[1019], enable=True)
            return CableOff_19(self.ctx)


class CableDelay_20_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_4__13$', duration=5000)
            self.set_breakable(trigger_ids=[1020], enable=True)
            return CableOff_20(self.ctx)


class CableDelay_21_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_4__14$', duration=5000)
            self.set_breakable(trigger_ids=[1021], enable=True)
            return CableOff_21(self.ctx)


class CableOff_19(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900006, key='Block', value=1)
            return End_04(self.ctx)


class CableOff_20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900006, key='Block', value=1)
            return End_04(self.ctx)


class CableOff_21(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900006, key='Block', value=1)
            return End_04(self.ctx)


class End_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # self.set_visible_breakable_object(trigger_ids=[1021])
            return 대기(self.ctx)


initial_state = 대기
