""" trigger/02000403_bf/event_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000030], state=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1001], interval=200, fade=15.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703]):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[101,102,103,104])
        self.select_camera_path(path_ids=[8001,8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=scene_06_ready)
        self.set_dialogue(type=2, spawn_id=11001956, script='$02000403_BF__EVENT_02__0$', time=5)
        self.move_npc(spawn_id=199, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=scene_06_ready)
        self.set_dialogue(type=2, spawn_id=11001956, script='$02000403_BF__EVENT_02__1$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=scene_06_ready)
        self.select_camera_path(path_ids=[8003,8004], return_view=False)
        self.set_mesh(trigger_ids=[1002], visible=True, interval=200, fade=35.0)
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192,1193,1194,1195,1196,1197,1198,1199], visible=True, interval=200, fade=35.0)
        self.set_dialogue(type=2, spawn_id=11001956, script='$02000403_BF__EVENT_02__2$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=scene_06_ready)
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=199, sequence_name='Bore_B')
        self.set_dialogue(type=2, spawn_id=11001956, script='$02000403_BF__EVENT_02__3$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[199])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_06_ready(self.ctx)


class scene_06_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000031], state=1)
        self.set_interact_object(trigger_ids=[12000032], state=1)
        self.set_interact_object(trigger_ids=[12000033], state=1)
        self.set_interact_object(trigger_ids=[12000034], state=1)
        self.set_interact_object(trigger_ids=[12000035], state=1)
        self.set_interact_object(trigger_ids=[12000036], state=1)
        self.destroy_monster(spawn_ids=[199])
        self.set_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_mesh(trigger_ids=[1002], visible=True, interval=200, fade=35.0)
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192,1193,1194,1195,1196,1197,1198,1199], visible=True, interval=200, fade=35.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition_open_boss_gauge(title='$02000403_BF__EVENT_02__9$', max_gauge_point=1000) # 진행 바 표기
        self.destroy_monster(spawn_ids=[199])
        self.spawn_monster(spawn_ids=[105,106,107,108,109,111,112,113,114,115,116,117,118,119], auto_target=False)
        self.spawn_monster(spawn_ids=[120,121,122,123,124,125,126,127,128,129], auto_target=False)
        self.spawn_monster(spawn_ids=[130,131,132,133,134,135,136], auto_target=False)
        self.spawn_monster(spawn_ids=[150,151,152,153,154,155,156], auto_target=False)
        self.reset_camera()
        self.set_event_ui(type=1, arg2='$02000403_BF__EVENT_02__4$', arg3='3000')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[106,105,116,115]):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=720, type='trigger', achieve='Hauntedmansion')
        self.spawn_monster(spawn_ids=[181,182,183,184], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_09(self.ctx)


class scene_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=181, script='$02000403_BF__EVENT_02__5$', time=3, arg5=2)
        self.set_dialogue(type=1, spawn_id=182, script='$02000403_BF__EVENT_02__6$', time=3, arg5=4)
        self.set_dialogue(type=1, spawn_id=183, script='$02000403_BF__EVENT_02__7$', time=3, arg5=8)
        self.set_dialogue(type=1, spawn_id=184, script='$02000403_BF__EVENT_02__8$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return scene_10(self.ctx)


class scene_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[181,182,183,184])


initial_state = idle
