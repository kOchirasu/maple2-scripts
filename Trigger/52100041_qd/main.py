""" trigger/52100041_qd/main.xml """
import trigger_api
from System.Numerics import Vector3


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition_close_boss_gauge()
        self.set_interact_object(trigger_ids=[10002071], state=1)
        self.set_interact_object(trigger_ids=[10002072], state=1)
        self.set_interact_object(trigger_ids=[10002073], state=1)
        self.set_interact_object(trigger_ids=[10002074], state=1)
        self.set_interact_object(trigger_ids=[10002075], state=1)
        self.set_interact_object(trigger_ids=[10002076], state=1)
        self.set_interact_object(trigger_ids=[10002077], state=1)
        self.set_mesh(trigger_ids=[1001], visible=True)
        self.set_mesh(trigger_ids=[1002])
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192,1193,1194,1195,1196,1197,1198,1199])
        self.set_mesh(trigger_ids=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220])
        self.set_mesh(trigger_ids=[1801,1802], visible=True)
        self.spawn_monster(spawn_ids=[101,102,103,104], auto_target=False)
        self.spawn_monster(spawn_ids=[199], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            # <transition state="CheckUserCount"/>
            return DungeonStart(self.ctx)


# <import path="./Data/Xml/Trigger/Dungeon_Common/CheckUserCount.xml" />
class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=start)
        self.select_camera_path(path_ids=[8100,8101,8102], return_view=False)
        self.set_ambient_light(primary=Vector3(120,120,120))
        self.set_directional_light(diffuse_color=Vector3(10,10,10))
        self.add_buff(box_ids=[701], skill_id=71000009, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return start(self.ctx)
        if self.shadow_expedition_points() >= 1000:
            self.shadow_expedition_close_boss_gauge()
            return boss_scene(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1801,1802])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 1000:
            self.shadow_expedition_close_boss_gauge()
            return boss_scene(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[105,106,107,108,109,111,112,113,114,115,116,117,118,119])
        self.destroy_monster(spawn_ids=[120,121,122,123,124,125,126,127,128,129])
        self.destroy_monster(spawn_ids=[130,131,132,133,134,135,136])
        self.destroy_monster(spawn_ids=[150,151,152,153,154,155,156])


class boss_scene(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_mesh(trigger_ids=[1002], interval=200, fade=35.0)
        # self.set_mesh(trigger_ids=[1201,1202,1203,1204,1205,1206], interval=200, fade=35.0)
        self.set_effect(trigger_ids=[7999], visible=True)
        self.spawn_monster(spawn_ids=[1999], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=boss)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return boss_scene_02(self.ctx)


class boss_scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=boss)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8006,8007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return boss_scene_03(self.ctx)


class boss_scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=boss)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return boss_scene_04(self.ctx)


class boss_scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_skip(state=boss)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return boss(self.ctx)

    def on_exit(self) -> None:
        self.reset_camera()


class boss(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.set_event_ui(type=1, arg2='$52100041_QD__MAIN__0$', arg3='3000')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1999]):
            return dungeonClear_ready(self.ctx)


class dungeonClear_ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return dungeonClear(self.ctx)


class dungeonClear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010068, portal_id=6001)
        # self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        # self.set_ambient_light(primary=Vector3(250,250,250))
        # self.set_directional_light(diffuse_color=Vector3(100,100,100))
        self.set_effect(trigger_ids=[7999])
        self.set_effect(trigger_ids=[7998], visible=True)
        self.dungeon_clear()


initial_state = idle
