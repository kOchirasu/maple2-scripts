""" trigger/52100201_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10000, visible=True, enable=True, minimap_visible=True)
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=1)
        # self.set_skill(trigger_ids=[10001])
        self.set_interact_object(trigger_ids=[12000319], state=0)
        self.set_interact_object(trigger_ids=[12000320], state=0)
        self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022])
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070])
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174])
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126])
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222])
        self.set_mesh(trigger_ids=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            self.set_interact_object(trigger_ids=[12000319], state=1)
            return 루트생성_1(self.ctx)


class 루트생성_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000319], state=0):
            return 루트생성_1_1(self.ctx)


class 루트생성_1_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_interact_object(trigger_ids=[12000319], state=1)
            self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126], visible=True, interval=20, fade=3.0)
            self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026], visible=True, interval=20, fade=3.0)
            return 배경생성_1(self.ctx)


class 배경생성_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070], visible=True)
            return 루트진행_1(self.ctx)


class 루트진행_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            self.set_interact_object(trigger_ids=[12000320], state=1)
            # self.set_interact_object(trigger_ids=[12000320], state=1)
            return 루트생성_2(self.ctx)
        if self.object_interacted(interact_ids=[12000319], state=0):
            self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070])
            self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026])
            self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126])
            return 루트생성_1_1(self.ctx)


class 루트생성_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000320], state=0):
            return 루트생성_2_1(self.ctx)


class 루트생성_2_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_interact_object(trigger_ids=[12000320], state=1)
            self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222], visible=True, interval=20, fade=3.0)
            self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022], visible=True, interval=20, fade=3.0)
            return 배경생성_2(self.ctx)


class 배경생성_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174], visible=True)
            return 루트진행_2(self.ctx)


class 루트진행_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            self.enable_spawn_point_pc(spawn_id=0)
            self.enable_spawn_point_pc(spawn_id=1, is_enable=True)
            # self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022])
            # self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222])
            # self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174])
            return 기믹2(self.ctx)
        if self.object_interacted(interact_ids=[12000320], state=0):
            self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022])
            self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222])
            self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174])
            return 루트생성_2_1(self.ctx)


class 기믹2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005], auto_target=False)
        self.set_mesh(trigger_ids=[4001,4002], visible=True)
        self.set_mesh(trigger_ids=[4004,4005], visible=True)
        self.set_mesh(trigger_ids=[4008], visible=True)
        self.set_mesh(trigger_ids=[4009], visible=True)
        self.set_mesh(trigger_ids=[4018], visible=True)
        self.set_mesh(trigger_ids=[4020,4021], visible=True)
        self.set_mesh(trigger_ids=[4025,4026], visible=True)
        self.set_mesh(trigger_ids=[4027], visible=True)
        self.set_mesh(trigger_ids=[4033,4034], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # self.set_user_value(trigger_id=910001, key='Cube', value=1)
            self.set_user_value(trigger_id=910002, key='Cube', value=1)
            # self.set_user_value(trigger_id=910003, key='Cube', value=1)
            self.set_user_value(trigger_id=910004, key='Cube', value=1)
            # self.set_user_value(trigger_id=910005, key='Cube', value=1)
            # self.set_user_value(trigger_id=910006, key='Cube', value=1)
            self.set_user_value(trigger_id=910007, key='Cube', value=1)
            self.set_user_value(trigger_id=910008, key='Cube', value=1)
            self.set_user_value(trigger_id=910009, key='Cube', value=1)
            # self.set_user_value(trigger_id=910010, key='Cube', value=1)
            self.set_user_value(trigger_id=910011, key='Cube', value=1)
            # self.set_user_value(trigger_id=910012, key='Cube', value=1)
            self.set_user_value(trigger_id=910013, key='Cube', value=1)
            # self.set_user_value(trigger_id=910014, key='Cube', value=1)
            # self.set_user_value(trigger_id=910015, key='Cube', value=1)
            self.set_user_value(trigger_id=910016, key='Cube', value=1)
            self.set_user_value(trigger_id=910017, key='Cube', value=1)
            # self.set_user_value(trigger_id=910018, key='Cube', value=1)
            self.set_user_value(trigger_id=910019, key='Cube', value=1)
            self.set_user_value(trigger_id=910020, key='Cube', value=1)
            return 기믹끝(self.ctx)


class 기믹끝(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9005]):
            self.destroy_monster(spawn_ids=[1001,1002,1003,1004,1005], arg2=False)
            return 대기(self.ctx)


initial_state = 대기
