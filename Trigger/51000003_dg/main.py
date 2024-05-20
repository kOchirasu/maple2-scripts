""" trigger/51000003_dg/main.xml """
import trigger_api


# 여기서 부터 시작
class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7999]) # 카메라 사운드
        self.set_portal(portal_id=8)
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015,6016,6017,6018,6019,6020,6021,6022,6023,6024,6025,6026,6027,6028,6029,6030,6031,6032,6033,6034,6035,6036,6037,6038,6039,6040,6041,6042,6043,6044,6045,6046,6047,6048,6049,6050,6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066,6067,6068,6069,6070,6071,6072,6073,6074,6075,6076,6077,6078,6079,6080,6081,6082,6083,6084,6085,6086,6087,6088,6089,6090,6091,6092,6093,6094,6095,6096,6097,6098,6099,6100]) # 일반 존 투명 블록
        # self.set_mesh(trigger_ids=[6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122,6123,6124,6125,6126,6127,6128,6129,6130,6131,6132,6133,6134,6135,6136,6137,6138,6139,6140,6141,6142,6143,6144,6145,6146,6147,6148,6149,6150,6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162,6163,6164,6165,6166,6167,6168,6169,6170,6171,6172,6173,6174,6175,6176,6177,6178,6179,6180,6181,6182,6183,6184,6185,6186,6187,6188,6189,6190,6191,6192,6193,6194,6195,6196,6197,6198,6199,6200], visible=True) # 벽 설정
        self.set_mesh(trigger_ids=[6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211,6212,6213,6214,6215,6216,6217,6218,6219,6220,6221,6222,6223,6224,6225,6226,6227,6228,6229,6230,6231,6232,6233,6234,6235,6236,6237,6238,6239,6240,6241,6242,6243,6244,6245,6246,6247,6248,6249,6250,6251,6252,6253,6254,6255,6256,6257,6258,6259,6260,6261,6262,6263,6264,6265,6266,6267,6268,6269,6270,6271,6272,6273,6274,6275,6276,6277,6278,6279,6280,6281,6282,6283,6284,6285,6286,6287,6288,6289,6290,6291,6292,6293,6294,6295,6296,6297,6298,6299,6300]) # 히든 존 투명 블록

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return Tutorial(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[501,502,503,504,505,506,507,508,509])


class Tutorial(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7998], visible=True) # 컷신 사운드 AMB
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8100,8101,8104,8106,8103,8105,8107,8108], return_view=False) # 카메라 뒤로 당김

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Tutorial_01(self.ctx)


class Tutorial_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=Tutorial_02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9500):
            return Tutorial_02(self.ctx)


class Tutorial_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=51000003, portal_id=1, box_id=701)
        self.set_effect(trigger_ids=[7998]) # 컷신 사운드 AMB OFF
        self.select_camera_path(path_ids=[8005,8001,8002], return_view=False) # 카메라 뒤로 당김
        self.set_user_value(trigger_id=991109, key='Tutorial', value=0) # 튜토리얼 동안 무적 버프
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7) # 라이프 카운트 정의
        self.arcade_boom_boom_ocean_start_game(life_count=20)
        self.show_count_ui(text='$51000003_DG__MAIN__0$', count=5)
        self.set_user_value(trigger_id=991103, key='Fail', value=1) # Fail Event on
        self.add_buff(box_ids=[701], skill_id=70000087, level=1, is_skill_set=False) # 아케이드 포커스

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[501,502,503,504,505,506,507,508,509])


class Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # [02100226] System_Monkey_01 ~ 06 (원숭이 간헐적으로 우키키, 우카카)
        self.play_system_sound_in_box(sound='System_Monkey_01')
        self.set_achievement(trigger_id=701, type='trigger', achieve='boomocean_start') # 붐붐오션 시작하기 (트로피)
        self.set_achievement(trigger_id=701, type='trigger', achieve='arcade_startcheck') # 아케이드 참여 일괄 체크용
        self.set_mesh(trigger_ids=[6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122,6123,6124,6125,6126,6127,6128,6129,6130,6131,6132,6133,6134,6135,6136,6137,6138,6139,6140,6141,6142,6143,6144,6145,6146,6147,6148,6149,6150,6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162,6163,6164,6165,6166,6167,6168,6169,6170,6171,6172,6173,6174,6175,6176,6177,6178,6179,6180,6181,6182,6183,6184,6185,6186,6187,6188,6189,6190,6191,6192,6193,6194,6195,6196,6197,6198,6199,6200]) # 벽 설정
        self.remove_buff(box_id=49179004, skill_id=0) # 발사체 피격 감점 점수 정의
        self.arcade_boom_boom_ocean_set_skill_score(id=49210001, score=-500) # 일반 발사체
        self.arcade_boom_boom_ocean_set_skill_score(id=49210011, score=-500) # 일반 발사체
        self.arcade_boom_boom_ocean_set_skill_score(id=49210021, score=-500) # 일반 발사체
        self.arcade_boom_boom_ocean_set_skill_score(id=49210031, score=-500) # 일반 발사체
        self.arcade_boom_boom_ocean_set_skill_score(id=49200021, score=-500) # 파도 발사체
        self.arcade_boom_boom_ocean_set_skill_score(id=49200001, score=-500) # 튜브 발사체
        self.arcade_boom_boom_ocean_set_skill_score(id=49190012, score=-500) # 대포 발사체
        self.arcade_boom_boom_ocean_set_skill_score(id=49190022, score=-500) # 대포 발사체
        # 알쏭달쏭 큐브 점수 정의
        self.arcade_boom_boom_ocean_set_skill_score(id=70000080, score=1000)
        self.arcade_boom_boom_ocean_set_skill_score(id=70000081, score=1000)
        self.arcade_boom_boom_ocean_set_skill_score(id=70000082, score=1000)
        self.arcade_boom_boom_ocean_set_skill_score(id=70000083, score=1000)
        self.arcade_boom_boom_ocean_set_skill_score(id=70000085, score=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Step_01(self.ctx)


class Step_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=0, arg2='1,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991107, key='Round_01', value=1) # normal LV1
        self.arcade_boom_boom_ocean_start_round(round=1, round_duration=1500, time_score_rate=1033) # 20초
        # [02100216] System_Fruit_Throw_Loop_01 (과일 날라 다니는 효과음, 루핑)
        self.play_system_sound_in_box(sound='System_Fruit_Throw_Loop_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_02(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=0, arg2='2,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991107, key='Round_02', value=1) # normal LV2
        self.arcade_boom_boom_ocean_clear_round(round=1)
        self.arcade_boom_boom_ocean_start_round(round=2, round_duration=20000, time_score_rate=1033)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_03(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=0, arg2='3,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991111, key='Round_01', value=1) # item_01
        self.set_user_value(trigger_id=991107, key='Round_03', value=1) # normal LV3
        self.arcade_boom_boom_ocean_clear_round(round=2)
        self.arcade_boom_boom_ocean_start_round(round=3, round_duration=20000, time_score_rate=1033)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_04(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=701, type='trigger', achieve='boomocean_1min') # 붐붐오션 1분 버티기 트로피


class Step_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=0, arg2='4,25', arg3='0', arg4='0') # 라운드 표기
        self.select_camera_path(path_ids=[8002,8003], return_view=False) # 카메라 뒤로 당김
        self.set_effect(trigger_ids=[7999], visible=True) # 카메라 사운드
        self.set_user_value(trigger_id=991120, key='Round_01', value=1) # wave3 LV1
        self.set_user_value(trigger_id=991107, key='Round_04', value=1) # normal LV4
        self.arcade_boom_boom_ocean_clear_round(round=3)
        self.arcade_boom_boom_ocean_start_round(round=4, round_duration=20000, time_score_rate=1550)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_05(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[7999]) # 카메라 사운드


class Step_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=4)
        self.arcade_boom_boom_ocean_start_round(round=5, round_duration=20000, time_score_rate=1550)
        # self.set_event_ui(type=0, arg2='5,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991104, key='Round_01', value=1) # wave LV1

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_06(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=5)
        self.arcade_boom_boom_ocean_start_round(round=6, round_duration=20000, time_score_rate=1550)
        # self.set_event_ui(type=0, arg2='6,25', arg3='0', arg4='0') # 라운드 표기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_07(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=6)
        self.arcade_boom_boom_ocean_start_round(round=7, round_duration=20000, time_score_rate=2067)
        # self.set_event_ui(type=0, arg2='7,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991105, key='Round_00', value=1) # wave2 LV0
        self.set_user_value(trigger_id=991102, key='Treasure_box', value=1) # 보물상자 스폰 스위치 ON

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_08(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=7)
        self.arcade_boom_boom_ocean_start_round(round=8, round_duration=20000, time_score_rate=2067)
        # self.set_event_ui(type=0, arg2='8,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991121, key='Round_01', value=1) # wave4 LV1

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_09(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=8)
        self.arcade_boom_boom_ocean_start_round(round=9, round_duration=20000, time_score_rate=2067)
        # self.set_event_ui(type=0, arg2='9,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991122, key='Round_01', value=1) # wave5 LV1

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_10(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=701, type='trigger', achieve='boomocean_3min') # 붐붐오션 3분 버티기 트로피


class Step_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=9)
        self.arcade_boom_boom_ocean_start_round(round=10, round_duration=20000, time_score_rate=2583)
        # self.set_event_ui(type=0, arg2='10,25', arg3='0', arg4='0') # 라운드 표기
        self.set_effect(trigger_ids=[7999], visible=True) # 카메라 사운드
        self.select_camera_path(path_ids=[8003,8004], return_view=False) # 카메라 뒤로 당김
        self.set_user_value(trigger_id=991106, key='Round_01', value=1) # cannon LV 1

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_11(self.ctx)


class Step_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=10)
        self.arcade_boom_boom_ocean_start_round(round=11, round_duration=20000, time_score_rate=2583)
        # self.set_event_ui(type=0, arg2='11,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991106, key='Round_02', value=1) # cannon LV 2

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_12(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=11)
        self.arcade_boom_boom_ocean_start_round(round=12, round_duration=20000, time_score_rate=2583)
        # self.set_event_ui(type=0, arg2='12,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991106, key='Round_03', value=1) # cannon LV 3

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_13(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=12)
        self.arcade_boom_boom_ocean_start_round(round=13, round_duration=20000, time_score_rate=3100)
        # self.set_event_ui(type=0, arg2='13,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991106, key='Round_04', value=1) # cannon LV 4
        self.set_user_value(trigger_id=991105, key='Round_01', value=1) # wave2 LV1

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_14(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=13)
        self.arcade_boom_boom_ocean_start_round(round=14, round_duration=20000, time_score_rate=3100)
        # self.set_event_ui(type=0, arg2='14,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991123, key='Round_01', value=1) # normal2 LV1
        self.set_user_value(trigger_id=991108, key='Round_03', value=1) # fog

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_15(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=14)
        self.arcade_boom_boom_ocean_start_round(round=15, round_duration=20000, time_score_rate=3100)
        # self.set_event_ui(type=0, arg2='15,25', arg3='0', arg4='0') # 라운드 표기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_16(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=701, type='trigger', achieve='boomocean_5min') # 붐붐오션 5분 버티기 트로피


class Step_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=15)
        self.arcade_boom_boom_ocean_start_round(round=16, round_duration=20000, time_score_rate=1350)
        # self.set_event_ui(type=0, arg2='16,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991123, key='Round_02', value=1) # normal2 LV2
        self.set_user_value(trigger_id=991105, key='Round_02', value=1) # wave2 LV2

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_17(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=16)
        self.arcade_boom_boom_ocean_start_round(round=17, round_duration=20000, time_score_rate=1350)
        # self.set_event_ui(type=0, arg2='17,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991106, key='Round_05', value=1) # cannon LV 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_18(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=17)
        self.arcade_boom_boom_ocean_start_round(round=18, round_duration=20000, time_score_rate=1350)
        # self.set_event_ui(type=0, arg2='18,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991123, key='Round_03', value=1) # normal2 LV3
        self.set_user_value(trigger_id=991122, key='Round_02', value=1) # wave5 LV1

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_19(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=18)
        self.arcade_boom_boom_ocean_start_round(round=19, round_duration=20000, time_score_rate=1125)
        # self.set_event_ui(type=0, arg2='18,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991107, key='Round_06', value=1) # normal LV4

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_20(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=19)
        self.arcade_boom_boom_ocean_start_round(round=20, round_duration=20000, time_score_rate=1125)
        # self.set_event_ui(type=0, arg2='20,25', arg3='0', arg4='0') # 라운드 표기
        self.set_user_value(trigger_id=991123, key='Round_04', value=1) # normal2 LV4

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_21(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=20)
        self.arcade_boom_boom_ocean_start_round(round=21, round_duration=20000, time_score_rate=1125)
        # self.set_event_ui(type=0, arg2='21,25', arg3='0', arg4='0') # 라운드 표기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_22(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=21)
        self.arcade_boom_boom_ocean_start_round(round=22, round_duration=20000, time_score_rate=900)
        # self.set_event_ui(type=0, arg2='22,25', arg3='0', arg4='0') # 라운드 표기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_23(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=22)
        self.arcade_boom_boom_ocean_start_round(round=23, round_duration=20000, time_score_rate=900)
        # self.set_event_ui(type=0, arg2='23,25', arg3='0', arg4='0') # 라운드 표기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_24(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=23)
        self.arcade_boom_boom_ocean_start_round(round=24, round_duration=20000, time_score_rate=900)
        # self.set_event_ui(type=0, arg2='24,25', arg3='0', arg4='0') # 라운드 표기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return Step_25(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_clear_round(round=24)
        self.arcade_boom_boom_ocean_start_round(round=25, round_duration=20000, time_score_rate=562)
        # self.set_event_ui(type=0, arg2='25,25', arg3='0', arg4='0') # 라운드 표기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=120000):
            return Step_26(self.ctx)
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class Step_26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_end_game()
        self.set_achievement(trigger_id=701, type='trigger', achieve='boomocean_10min') # 붐붐오션 10분 버티기 트로피

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=705) >= 1:
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_boom_boom_ocean_end_game()


initial_state = Idle
