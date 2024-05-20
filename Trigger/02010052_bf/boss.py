""" trigger/02010052_bf/boss.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4)
        self.set_mesh(trigger_ids=[6801,6802,6803,6804,6805,6806,6807,6808,6809,6810,6811,6812,6813,6814,6815,6816,6817,6818,6819,6820,6821,6822,6823,6824,6825,6826,6827,6828,6829,6830,6831,6832,6833,6834,6835,6836,6837,6838,6839,6840,6841,6842,6843,6844,6845,6846,6847,6848,6849,6850,6851,6852,6853,6854,6855,6856,6857,6858,6859,6860,6861,6862,6863,6864,6865,6866,6867,6868,6869,6870,6871,6872,6873,6874,6875,6876,6877,6878,6879,6880,6881,6882,6883,6884,6885,6886,6887,6888,6889,6890,6891,6892,6893,6894,6895,6896,6897,6898,6899,6900]) # 블록 없음
        self.set_effect(trigger_ids=[7031]) # 횃불에 불이 붙는 이펙트
        self.set_effect(trigger_ids=[7032]) # 횃불에 불이 붙는 이펙트
        self.set_effect(trigger_ids=[7033]) # 횃불에 불이 붙는 이펙트
        self.set_effect(trigger_ids=[7034]) # 횃불에 불이 붙는 이펙트
        self.set_effect(trigger_ids=[7035]) # 횃불에 불이 붙는 이펙트
        self.set_effect(trigger_ids=[7999]) # 인트로 사운드
        self.set_effect(trigger_ids=[7910]) # 카나 텔레포트
        self.set_effect(trigger_ids=[7911]) # 카나 텔레포트
        self.set_effect(trigger_ids=[7912]) # 카나 텔레포트
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            return Echo(self.ctx)

    def on_exit(self) -> None:
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)


class Echo(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7800], visible=True) # 카나 메아리

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=720) >= 1:
            return Boss_01(self.ctx)


class Boss_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7531], visible=True) # 얼어붙는 소리
        self.set_mesh(trigger_ids=[6801,6802,6803,6804,6805,6806,6807,6808,6809,6810], visible=True, start_delay=80, interval=70, fade=8.0) # 얼음!
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Boss_01b(self.ctx)


class Boss_01b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7910], visible=True) # 카나 텔레포트
        self.spawn_monster(spawn_ids=[995], auto_target=False) # 카나 (995)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Boss_01c(self.ctx)


class Boss_01c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=200, text_id=20105201) # 화로를 공격하여 불을 붙이세요
        self.set_dialogue(type=1, spawn_id=995, script='$02010052_BF__BOSS__0$', time=3) # 카나 말풍선 대사
        self.spawn_monster(spawn_ids=[120], auto_target=False) # 화로 (107)
        self.spawn_monster(spawn_ids=[621,622,623,624,625]) # 몬스터 웨이브

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[120]):
            return burn_state_01(self.ctx)


class burn_state_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=200)
        self.set_effect(trigger_ids=[7507], visible=True) # 얼음 녹는 소리
        self.set_mesh(trigger_ids=[6801,6802,6803,6804,6805,6806,6807,6808,6809,6810], start_delay=800, interval=100) # 벽 해제
        self.set_mesh(trigger_ids=[600003], start_delay=800, interval=100) # 벽 해제
        self.set_effect(trigger_ids=[7910], visible=True) # 카나 텔레포트
        self.destroy_monster(spawn_ids=[995]) # 카나 사라짐 (995)
        self.set_event_ui(type=1, arg2='$02010052_BF__BOSS__1$', arg3='3000')
        self.set_effect(trigger_ids=[7031], visible=True) # 횃불에 불이 붙는 이펙트
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Boss_02_idle(self.ctx)


class Boss_02_idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=721) >= 1:
            return Boss_02(self.ctx)


class Boss_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7532], visible=True) # 얼어붙는 소리
        self.set_mesh(trigger_ids=[6821,6822,6823,6824,6825,6826,6827,6828,6829,6830], visible=True, start_delay=80, interval=70, fade=8.0) # 얼음!
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Boss_02b(self.ctx)


class Boss_02b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7911], visible=True) # 카나 텔레포트
        self.spawn_monster(spawn_ids=[996], auto_target=False) # 카나 (995)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Boss_02c(self.ctx)


class Boss_02c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=200, text_id=20105201) # 화로를 공격하여 불을 붙이세요
        self.set_dialogue(type=1, spawn_id=996, script='$02010052_BF__BOSS__2$', time=3) # 카나 말풍선 대사
        self.spawn_monster(spawn_ids=[121], auto_target=False) # 화로 (107)
        self.spawn_monster(spawn_ids=[631,632,633,634,635]) # 몬스터 웨이브

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[121]):
            return burn_state_02(self.ctx)


class burn_state_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=200)
        self.set_effect(trigger_ids=[7508], visible=True) # 얼음 녹는 소리
        self.set_mesh(trigger_ids=[6821,6822,6823,6824,6825,6826,6827,6828,6829,6830], start_delay=800, interval=100) # 벽 해제
        self.set_mesh(trigger_ids=[600004], start_delay=800, interval=100) # 벽 해제
        self.set_effect(trigger_ids=[7911], visible=True) # 카나 텔레포트
        self.destroy_monster(spawn_ids=[996]) # 카나 사라짐 (995)
        self.set_event_ui(type=1, arg2='$02010052_BF__BOSS__3$', arg3='3000')
        self.set_effect(trigger_ids=[7032], visible=True) # 횃불에 불이 붙는 이펙트
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Boss_03_idle(self.ctx)


class Boss_03_idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=722) >= 1:
            return Boss_03(self.ctx)


class Boss_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7533], visible=True) # 얼어붙는 소리
        self.set_mesh(trigger_ids=[6830,6831,6832,6833,6834,6835,6836,6837,6838,6839,6840], visible=True, start_delay=80, interval=70, fade=8.0) # 얼음!
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Boss_03b(self.ctx)


class Boss_03b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7912], visible=True) # 카나 텔레포트
        self.spawn_monster(spawn_ids=[997], auto_target=False) # 카나 (995)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Boss_03c(self.ctx)


class Boss_03c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=200, text_id=20105201) # 화로를 공격하여 불을 붙이세요
        self.set_dialogue(type=1, spawn_id=997, script='$02010052_BF__BOSS__4$', time=3) # 카나 말풍선 대사
        self.spawn_monster(spawn_ids=[641,642,643,644,645]) # 몬스터 웨이브
        self.spawn_monster(spawn_ids=[122], auto_target=False) # 화로 (107)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[122]):
            return burn_state_03(self.ctx)


class burn_state_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=200)
        self.set_effect(trigger_ids=[7509], visible=True) # 얼음 녹는 소리
        self.set_mesh(trigger_ids=[6830,6831,6832,6833,6834,6835,6836,6837,6838,6839,6840], start_delay=800, interval=100) # 벽 해제
        self.set_mesh(trigger_ids=[600005], start_delay=800, interval=100) # 벽 해제
        self.set_effect(trigger_ids=[7912], visible=True) # 카나 텔레포트
        self.destroy_monster(spawn_ids=[997]) # 카나 사라짐 (995)
        self.set_event_ui(type=1, arg2='$02010052_BF__BOSS__5$', arg3='3000')
        self.set_effect(trigger_ids=[7033], visible=True) # 횃불에 불이 붙는 이펙트
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.time_expired(timer_id='1'):
            return Boss_04_idle(self.ctx)
        """
        if self.count_users(box_id=724) >= 1:
            return Boss_04_idle(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[123,124], auto_target=False) # 마지막 두 화로


class Boss_04_idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=200, text_id=20105201) # 화로를 공격하여 불을 붙이세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[123]):
            return Boss_04_idle_A(self.ctx)
        if self.monster_dead(spawn_ids=[124]):
            return Boss_04_idle_B(self.ctx)


class Boss_04_idle_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7034], visible=True) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[124]):
            return burn_state_04(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[7035], visible=True) # 횃불에 불이 붙는 이펙트


class Boss_04_idle_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7035], visible=True) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[123]):
            return burn_state_04(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[7034], visible=True) # 횃불에 불이 붙는 이펙트


class burn_state_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=200)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[7999], visible=True) # 컷인 사운드
        self.set_dialogue(type=2, spawn_id=21800073, script='$02010052_BF__BOSS__6$', time=5) # 카나 대사
        # Missing State: Boss_Battle
        self.set_skip()
        self.set_mesh(trigger_ids=[6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211,6212,6213,6214,6215,6216,6217,6218,6219,6220,6221,6222,6223,6224,6225,6226,6227,6228,6229,6230,6231,6232,6233,6234,6235,6236,6237,6238,6239,6240,6241,6242,6243,6244,6245,6246,6247,6248,6249,6250,6251,6252,6253,6254,6255,6256,6257,6258,6259,6260,6261,6262,6263,6264,6265,6266,6267,6268,6269,6270,6271,6272,6273,6274,6275,6276,6277,6278,6279,6280,6281,6282,6283,6284,6285,6286,6287,6288,6289,6290,6291,6292,6293,6294,6295,6296,6297,6298,6299,6300,6301,6302,6303,6304,6305,6306,6307,6308,6309,6310,6311,6312,6313,6314,6315,6316,6317,6318,6319,6320,6321,6322,6323,6324,6325,6326,6327,6328,6329,6330,6331,6332,6333,6334,6335,6336,6337,6338,6339,6340,6341,6342,6343,6344,6345,6346,6347,6348,6349,6350,6351,6352,6353,6354,6355,6356,6357,6358,6359,6360,6361,6362,6363,6364,6365,6366,6367,6368,6369,6370,6371,6372,6373,6374,6375,6376,6377,6378,6379,6380,6381,6382,6383,6384,6385,6386,6387,6388,6389,6390,6391,6392,6393,6394,6395,6396,6397,6398,6399,6400,6401,6402,6403,6404,6405,6406,6407,6408,6409,6410,6411,6412,6413,6414,6415,6416,6417,6418,6419,6420,6421,6422,6423,6424,6425,6426,6427,6428,6429,6430,6431,6432,6433,6434,6435,6436,6437,6438,6439,6440,6441,6442,6443,6444,6445,6446,6447,6448,6449,6450,6451,6452,6453,6454,6455,6456,6457,6458,6459,6460,6461,6462,6463,6464,6465,6466,6467,6468,6469,6470,6471,6472,6473,6474,6475,6476,6477,6478,6479,6480,6481,6482,6483,6484,6485,6486,6487,6488,6489,6490,6491,6492,6493,6494,6495,6496,6497,6498,6499,6500,6501,6502,6503,6504,6505,6506,6507,6508,6509,6510,6511,6512,6513,6514,6515,6516,6517,6518,6519,6520,6521,6522,6523,6524,6525,6526,6527,6528,6529,6530,6531,6532,6533,6534,6535,6536,6537,6538,6539,6540,6541,6542,6543,6544,6545,6546,6547,6548,6549,6550,6551,6552,6553,6554,6555,6556,6557,6558,6559,6560,6561,6562,6563,6564,6565,6566,6567,6568,6569,6570,6571,6572,6573,6574,6575,6576,6577,6578,6579,6580,6581,6582,6583,6584,6585,6586,6587,6588,6589,6590,6591,6592,6593,6594,6595,6596,6597,6598,6599,6600,6601,6602,6603,6604,6605,6606,6607,6608,6609,6610,6611,6612,6613,6614,6615,6616,6617,6618,6619,6620,6621,6622,6623,6624,6625,6626,6627,6628,6629,6630,6631,6632,6633,6634,6635,6636,6637,6638,6639,6640,6641,6642,6643,6644,6645,6646,6647,6648,6649,6650,6651,6652,6653,6654,6655,6656,6657,6658,6659,6660,6661,6662,6663,6664,6665,6666,6667,6668,6669,6670,6671,6672,6673,6674,6675,6676,6677,6678,6679,6680,6681,6682,6683,6684,6685,6686,6687,6688,6689,6690,6691,6692,6693,6694,6695,6696,6697,6698,6699], start_delay=80, interval=10) # 벽 해제
        self.select_camera_path(path_ids=[80004,80005]) # 연출 카메라
        self.set_timer(timer_id='6', seconds=6, start_delay=1)
        self.spawn_monster(spawn_ids=[998], auto_target=False) # 기본 배치 될 몬스터 등장
        self.move_npc(spawn_id=998, patrol_name='MS2PatrolData_1008') # 카나의 분신 991 (이동)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Boss_battle_01(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[6890,6891,6892,6893,6894,6895], visible=True, start_delay=50, interval=70) # 벽 생성
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class Boss_battle_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6701,6702,6703,6704,6705,6706,6707,6708,6709,6710,6711,6712,6713,6714,6715,6716,6717,6718,6719,6720,6721,6722,6723,6724,6725,6726,6727,6728,6729,6730,6731,6732,6733,6734,6735,6736,6737,6738,6739,6740,6741,6742,6743,6744,6745,6746,6747,6748,6749,6750,6751,6752,6753,6754,6755,6756,6757,6758,6759,6760,6761,6762,6763,6764,6765,6766,6767,6768,6769,6770,6771,6772,6773,6774,6775,6776,6777,6778,6779,6780,6781,6782,6783,6784,6785,6786,6787,6788,6789,6790,6791,6792,6793,6794,6795,6796,6797,6798,6799], start_delay=80, interval=50) # 벽 해제
        self.set_event_ui(type=1, arg2='$02010052_BF__BOSS__7$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=723) >= 1:
            return Boss_Spawn_01(self.ctx)


class Boss_Spawn_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[998]) # 카나 사라짐 (998)
        self.spawn_monster(spawn_ids=[999], auto_target=False) # 보스 카나 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[999]):
            return Clear_01(self.ctx)


class Clear_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=80006)
        self.spawn_monster(spawn_ids=[9998], auto_target=False) # 카나 등장
        self.set_effect(trigger_ids=[7998], visible=True) # 텔레포트
        self.move_npc(spawn_id=9998, patrol_name='MS2PatrolData_1009') # 카나의 분신 991 (이동)
        self.set_dialogue(type=2, spawn_id=21800073, script='$02010052_BF__BOSS__8$', time=4) # 카나 대사
        self.set_timer(timer_id='5', seconds=5, start_delay=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return Clear(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.set_effect(trigger_ids=[7998], visible=True) # 텔레포트
        self.destroy_monster(spawn_ids=[9998]) # 카나 사라짐 (998)
        self.select_camera(trigger_id=80006, enable=False)


class Clear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=7, arg2='미션 성공!', arg3='3000', arg4='0')
        # self.show_guide_summary(entity_id=112, text_id=40009) # 포탈을 타세요
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6890,6891,6892,6893,6894,6895], start_delay=80, interval=10) # 벽 해제
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        self.dungeon_clear()


initial_state = Idle
