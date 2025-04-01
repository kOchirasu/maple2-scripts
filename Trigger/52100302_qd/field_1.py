""" trigger/52100302_qd/field_1.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000504], state=2)
        self.set_interact_object(trigger_ids=[12000505], state=2)
        self.set_interact_object(trigger_ids=[12000506], state=2)
        # self.set_visible_breakable_object(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])
        # self.set_visible_breakable_object(trigger_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
        # self.set_visible_breakable_object(trigger_ids=[1021,1022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block') == 1:
            self.set_user_value(trigger_id=900002, key='Block', value=0)
            return Block_1(self.ctx)
        if self.user_value(key='Block') == 2:
            self.set_user_value(trigger_id=900002, key='Block', value=0)
            return Block_2(self.ctx)
        if self.user_value(key='Block') == 3:
            self.set_user_value(trigger_id=900002, key='Block', value=0)
            return Block_3(self.ctx)


class Block_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1104,1150,1151,1152,1157,1158,1159,1160,1161]):
            self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_1__0$', duration=5000)
            self.set_interact_object(trigger_ids=[12000504], state=1)
            self.spawn_monster(spawn_ids=[1107], auto_target=False)
            self.spawn_monster(spawn_ids=[1108], auto_target=False)
            self.spawn_monster(spawn_ids=[1109], auto_target=False)
            self.spawn_monster(spawn_ids=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], auto_target=False)
            self.spawn_monster(spawn_ids=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], auto_target=False)
            self.spawn_monster(spawn_ids=[1221,1222,1223,1224], auto_target=False)
            self.spawn_monster(spawn_ids=[30001,30002,30003,30004], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=102)
            self.enable_spawn_point_pc(spawn_id=103, is_enable=True)
            return CableOn_04(self.ctx)


class Block_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1105,1153,1154,1162,1163,1164,1165,1166]):
            self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_1__1$', duration=5000)
            self.set_interact_object(trigger_ids=[12000505], state=1)
            self.spawn_monster(spawn_ids=[1107], auto_target=False)
            self.spawn_monster(spawn_ids=[1108], auto_target=False)
            self.spawn_monster(spawn_ids=[1109], auto_target=False)
            self.spawn_monster(spawn_ids=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], auto_target=False)
            self.spawn_monster(spawn_ids=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], auto_target=False)
            self.spawn_monster(spawn_ids=[1221,1222,1223,1224], auto_target=False)
            self.spawn_monster(spawn_ids=[30001,30002,30003,30004], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=102)
            self.enable_spawn_point_pc(spawn_id=104, is_enable=True)
            return CableOn_05(self.ctx)


class Block_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1106,1155,1156,1167,1168,1169,1170,1171,1172]):
            self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$52100302_QD__FIELD_1__2$', duration=5000)
            self.set_interact_object(trigger_ids=[12000506], state=1)
            self.spawn_monster(spawn_ids=[1107], auto_target=False)
            self.spawn_monster(spawn_ids=[1108], auto_target=False)
            self.spawn_monster(spawn_ids=[1109], auto_target=False)
            self.spawn_monster(spawn_ids=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], auto_target=False)
            self.spawn_monster(spawn_ids=[1211,1212,1213,1214,1215,1216,1217,1218,1219,1220], auto_target=False)
            self.spawn_monster(spawn_ids=[1221,1222,1223,1224], auto_target=False)
            self.spawn_monster(spawn_ids=[30001,30002,30003,30004], auto_target=False)
            self.enable_spawn_point_pc(spawn_id=102)
            self.enable_spawn_point_pc(spawn_id=105, is_enable=True)
            return CableOn_06(self.ctx)


class CableOn_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000504], state=0):
            self.set_interact_object(trigger_ids=[12000504], state=0)
            self.destroy_monster(spawn_ids=[30003,30004], arg2=False)
            self.set_mesh(trigger_ids=[1100101,1100102,1100103,1100104,1100105,1100106,1100107,1100108,1100109,1100110])
            return CableDelay_04(self.ctx)


class CableOn_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000505], state=0):
            self.set_interact_object(trigger_ids=[12000505], state=0)
            self.destroy_monster(spawn_ids=[30001,30002,30004], arg2=False)
            self.set_mesh(trigger_ids=[1100201,1100202,1100203,1100204,1100205,1100206,1100207,1100208,1100209,1100210])
            return CableDelay_05(self.ctx)


class CableOn_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000506], state=0):
            self.set_interact_object(trigger_ids=[12000506], state=0)
            self.destroy_monster(spawn_ids=[30001,30002,30003], arg2=False)
            self.set_mesh(trigger_ids=[1100301,1100302,1100303,1100304,1100305,1100306,1100307,1100308,1100309,1100310])
            return CableDelay_06(self.ctx)


class CableDelay_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__3$', duration=3000)
            return CableDelay_04_2(self.ctx)


class CableDelay_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__4$', duration=3000)
            return CableDelay_05_2(self.ctx)


class CableDelay_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__5$', duration=3000)
            return CableDelay_06_2(self.ctx)


class CableDelay_04_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__6$', duration=1000)
            return CableDelay_04_3(self.ctx)


class CableDelay_05_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__7$', duration=1000)
            return CableDelay_05_3(self.ctx)


class CableDelay_06_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__8$', duration=1000)
            return CableDelay_06_3(self.ctx)


class CableDelay_04_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__9$', duration=1000)
            return CableDelay_04_4(self.ctx)


class CableDelay_05_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__10$', duration=1000)
            return CableDelay_05_4(self.ctx)


class CableDelay_06_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__11$', duration=1000)
            return CableDelay_06_4(self.ctx)


class CableDelay_04_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__12$', duration=1000)
            return CableDelay_04_5(self.ctx)


class CableDelay_05_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__13$', duration=1000)
            return CableDelay_05_5(self.ctx)


class CableDelay_06_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_event_ui_script(type=BannerType.Text, script='$52100302_QD__FIELD_1__14$', duration=1000)
            return CableDelay_06_5(self.ctx)


class CableDelay_04_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1004], enable=True)
            self.move_npc(spawn_id=30001, patrol_name='MS2PatrolData_101')
            self.move_npc(spawn_id=30002, patrol_name='MS2PatrolData_102')
            return CableOff_04(self.ctx)


class CableDelay_05_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1005], enable=True)
            self.move_npc(spawn_id=30003, patrol_name='MS2PatrolData_103')
            return CableOff_05(self.ctx)


class CableDelay_06_5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1006], enable=True)
            self.move_npc(spawn_id=30004, patrol_name='MS2PatrolData_104')
            return CableOff_06(self.ctx)


class CableOff_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900003, key='Block', value=1)
            return End_01(self.ctx)


class CableOff_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900003, key='Block', value=2)
            return End_01(self.ctx)


class CableOff_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_user_value(trigger_id=900003, key='Block', value=3)
            return End_01(self.ctx)


class End_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대기(self.ctx)


initial_state = 대기
