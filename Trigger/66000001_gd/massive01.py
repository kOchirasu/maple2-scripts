""" trigger/66000001_gd/massive01.xml """
import trigger_api


# 파이널서바이버
class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            return 퍼즐대기중(self.ctx)


class 퍼즐대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211], visible=True)
        self.set_actor(trigger_id=251, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=252, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=253, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=254, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=255, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=256, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=257, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=258, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=259, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=260, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=261, visible=True, initial_sequence='Eff_MassiveEvent_Door_Opened')
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        self.set_portal(portal_id=777, enable=True)
        self.set_portal(portal_id=778, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=779, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=301) >= 50:
            return 계단없애기(self.ctx)
        if self.wait_tick(wait_tick=30000):
            return 계단없애기(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=261, visible=True, initial_sequence='Eff_MassiveEvent_Door_Vanished')
        self.set_portal(portal_id=777)


class 계단없애기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mini_game_area_for_hack(box_id=301) # 해킹 보안용 시작 box 설정
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 계단없애기2(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[206,207,208,209,210,211])
        self.set_actor(trigger_id=256, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=257, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=258, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=259, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=260, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=261, initial_sequence='Eff_MassiveEvent_Door_Vanished')
        self.reset_timer(timer_id='1')


class 계단없애기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[201,202,203,204,205])
        self.set_actor(trigger_id=251, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=252, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=253, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=254, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=255, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=256, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=257, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=258, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=259, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(trigger_id=260, initial_sequence='Eff_MassiveEvent_Stair_Closed')
        self.reset_timer(timer_id='1')


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트0(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        # 로그에서 해당 이벤트에 참여한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id
        self.set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__0$', arg3='6000')
        # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
        # self.set_achievement(trigger_id=301, type='trigger', achieve='finalsurvivor_start')
        # self.set_achievement(trigger_id=301, type='trigger', achieve='dailyquest_start')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트1(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)
        self.set_event_ui(type=1, arg2='$66000001_GD__MASSIVE01__0$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        self.set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__2$', arg3='6000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트3(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 멘트3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=6)
        self.set_event_ui(type=0, arg2='1,4')
        self.show_count_ui(text='$61000002_ME_002__MASSIVE01__3$', stage=1, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계1대기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계1대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계1(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=40)
        self.set_random_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], start_delay=20, fade=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계1정리(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계1정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계1정리2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계1정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            self.set_event_ui(type=0, arg2='2,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__4$', stage=2, count=5)
            return 퍼즐단계2대기(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 실패(self.ctx)


class 퍼즐단계2대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)
        self.set_random_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], start_delay=30, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계2정리(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계2정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계2정리2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계2정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            self.set_event_ui(type=0, arg2='3,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__5$', stage=3, count=5)
            return 퍼즐단계3대기(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 실패(self.ctx)


class 퍼즐단계3대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계3(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=15)
        self.set_random_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], start_delay=30, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계3정리(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계3정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계3정리2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계3정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            self.set_event_ui(type=0, arg2='4,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__6$', stage=4, count=5)
            return 퍼즐단계4대기(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 실패(self.ctx)


class 퍼즐단계4대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계4(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        self.set_random_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], start_delay=15, fade=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계4정리(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계4정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계4정리2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계4정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
            return 보상단계(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 실패(self.ctx)


class 보상단계(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=7)
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=3, arg2='$61000002_ME_002__MASSIVE01__7$', arg3='7000', arg4='301')
        # 로그에서 해당 이벤트에서 우승한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id
        self.set_event_ui(type=6, arg2='$61000002_ME_002__MASSIVE01__8$', arg3='7000', arg4='!301')
        # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
        # self.set_achievement(trigger_id=301, type='trigger', achieve='finalsurvivor_win')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 경험치지급(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 경험치지급(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.give_exp(box_id=301, rate=40.5)
        # self.give_exp(box_id=301, rate=9.0, arg3=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 버프걸기(self.ctx)


class 버프걸기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=7)
        self.set_event_ui(type=0, arg2='0,0')
        # self.add_buff(box_ids=[301], skill_id=70000019, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐종료계단보이기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


"""
class 돈벼락(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=15)
        self.set_event_ui(type=3, arg2='$61000002_ME_002__MASSIVE01__11$', arg3='5000', arg4='301')
        self.set_event_ui(type=6, arg2='$61000002_ME_002__MASSIVE01__12$', arg3='5000', arg4='!301')
        self.create_item(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐종료계단보이기(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')
"""

class 퍼즐종료계단보이기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='0,0')
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        self.set_mesh(trigger_ids=[201,202,203,204,205], visible=True)
        self.set_actor(trigger_id=251, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=252, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=253, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=254, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=255, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐종료계단보이기2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐종료계단보이기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[206,207,208,209,210], visible=True)
        self.set_actor(trigger_id=256, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=257, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=258, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=259, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=260, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐종료(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[211], visible=True)
        self.set_actor(trigger_id=261, visible=True, initial_sequence='Eff_MassiveEvent_Door_Opened')
        self.reset_timer(timer_id='1')


class 퍼즐종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_event_ui(type=0, arg2='0,0')
        self.set_portal(portal_id=777, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 유저이동(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=5, arg2='$61000002_ME_002__MASSIVE01__13$', arg3='5000')
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        self.set_portal(portal_id=777, enable=True)
        self.set_mesh(trigger_ids=[201,202,203,204,205], visible=True)
        self.set_actor(trigger_id=251, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=252, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=253, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=254, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=255, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 실패계단보이기2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 실패계단보이기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[206,207,208,209,210], visible=True)
        self.set_actor(trigger_id=256, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=257, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=258, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=259, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(trigger_id=260, visible=True, initial_sequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 유저이동(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[211], visible=True)
        self.set_actor(trigger_id=261, visible=True, initial_sequence='Eff_MassiveEvent_Door_Opened')
        self.reset_timer(timer_id='1')


class 유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__23$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=120000):
            self.move_user()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
