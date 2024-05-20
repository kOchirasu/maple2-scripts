""" trigger/61000005_me/mainprocess.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[196]):
            return 퍼즐대기중(self.ctx)


# 퍼즐 시작하기 전의 맵 상태로 정리
class 퍼즐대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg1은 상태그룹의 ID, arg2 상태그룹에 포함되는 상태이름들, arg3 0이면 순서대로 1이면 상태그룹을 랜덤하게 섞는다.
        self.set_state(id=1, states=[퍼즐패턴1,퍼즐패턴2,퍼즐패턴3], randomize=True)
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176], visible=True) # 퍼즐 큐브를 모두 보인다(arg2=1)
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208], visible=True) # 순간 이동 발판이 보인다 (arg2=1)
        self.set_mesh(trigger_ids=[211,212], visible=True) # 닫힌 문이 보인다 (arg2=1)
        self.set_mesh(trigger_ids=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436], visible=True) # 퍼즐 펜스 모두 보인다 (arg2=1)
        # 퍼즐 큐브 바운딩 모두 살린다 (arg2=1)
        self.set_mesh(trigger_ids=[451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494], visible=True)
        # 퍼즐 큐브 외곽 발판 모두 가린다 (arg2=0)
        self.set_mesh(trigger_ids=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544])
        self.set_mesh(trigger_ids=[551,552]) # 열린 문을 가린다 (arg2=0)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=101, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=102, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=103, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=104, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=115, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=116, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=117, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=118, enable=True)
        # 탈락자용 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=500, enable=True)
        # 202 스폰 포인트의 NPC(문 안의 퍼즈룬)를 없앤다
        self.destroy_monster(spawn_ids=[202], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=90000):
            return 시작대기멘트1(self.ctx)
        if self.count_users(box_id=196) >= 20:
            return 시작대기멘트1(self.ctx)


# 곧 게임을 시작할 거지만, 조금 더 시간을 줘서 퍼즐 구간으로 넘어오도록
class 시작대기멘트1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        self.set_event_ui(type=1, arg2='$61000005_ME__MAINPROCESS__0$', arg3='4500')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기멘트2(self.ctx)


class 시작대기멘트2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5) # arg2는 시간 (초)
        # arg1=1인 경우 최대 3줄, arg3는 시간(1/1000초)
        self.set_event_ui(type=1, arg2='$61000005_ME__MAINPROCESS__1$', arg3='4500')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기멘트3(self.ctx)


class 시작대기멘트3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        self.set_event_ui(type=1, arg2='$61000005_ME__MAINPROCESS__2$', arg3='4500')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기멘트4(self.ctx)


class 시작대기멘트4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        self.set_event_ui(type=1, arg2='$61000005_ME__MAINPROCESS__3$', arg3='4500')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기멘트5(self.ctx)


class 시작대기멘트5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        self.set_event_ui(type=1, arg2='$61000005_ME__MAINPROCESS__4$', arg3='4500')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기(self.ctx)


# 퍼즐 시작을 위한 세팅
class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 퍼즐 대기에서 패턴을 섞을 경우 섞이지 않는 경우가 있어서 여기에서 퍼즐 패턴을 한번 더 섞어줌
        # arg1은 상태그룹의 ID, arg2 상태그룹에 포함되는 상태이름들, arg3 0이면 순서대로 1이면 상태그룹을 랜덤하게 섞는다.
        self.set_state(id=1, states=[퍼즐패턴1,퍼즐패턴2,퍼즐패턴3], randomize=True)
        # 퍼즐 패턴 섞기 종료
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208]) # 순간 이동 발판이 사라진다
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=101)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=102)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=103)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=104)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=115)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=116)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=117)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=118)
        # 202 스폰 포인트의 NPC(문 안의 퍼즈룬)를 리젠시킨다. 타겟지정 안 한다(arg2=0)
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.set_event_ui(type=1, arg2='$61000005_ME__MAINPROCESS__5$', arg3='4500')
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 멘트1(self.ctx)


# 퍼즐 시작
class 멘트1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 5초 카운트하는 UI 쓸 때, 본 스테이트는 7초 정도를 줘야 안 어색함
        self.set_timer(timer_id='1', seconds=6)
        self.set_event_ui(type=0, arg2='1,3') # 1/3 스테이지
        self.show_count_ui(text='$61000005_ME__MAINPROCESS__6$', stage=1, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계1(self.ctx)


# 퍼즐 1단계
class 퍼즐단계1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=14) # 바닥이 사라지는 데 걸리는 시간과 맞출 것
        self.use_state(id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 퍼즐단계1정리(self.ctx)


class 퍼즐단계1정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176], visible=True) # 퍼즐 큐브를 모두 보인다(arg2=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계1종료(self.ctx)
        if not self.user_detected(box_ids=[197,198,199]):
            # 아무도 살아남지 못한다면
            return 모두실패(self.ctx)


class 퍼즐단계1종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[197,198,199]):
            # 살아 남은 사람이 있다면 (사실 위에서 걸러지지 않았기 때문에 살아 남은 사람이 있어야 함
            return 퍼즐단계2대기(self.ctx)


# 2단계 퍼즐
class 퍼즐단계2대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 5초 카운트하는 UI 쓸 때, 본 스테이트는 7초 정도를 줘야 안 어색함
        self.set_timer(timer_id='1', seconds=6)
        self.set_event_ui(type=0, arg2='2,3') # 2/3 스테이지
        self.show_count_ui(text='$61000005_ME__MAINPROCESS__7$', stage=2, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=14) # 바닥이 사라지는 데 걸리는 시간과 맞출 것
        self.use_state(id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 퍼즐단계2정리(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='99')


class 퍼즐단계2정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176], visible=True) # 퍼즐 큐브를 모두 보인다(arg2=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계2종료(self.ctx)
        if not self.user_detected(box_ids=[197,198,199]):
            # 아무도 살아남지 못한다면
            return 모두실패(self.ctx)


class 퍼즐단계2종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[197,198,199]):
            # 살아 남은 사람이 있다면 (사실 위에서 걸러지지 않았기 때문에 살아 남은 사람이 있어야 함
            return 퍼즐단계3대기(self.ctx)


# 3단계 퍼즐
class 퍼즐단계3대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 5초 카운트하는 UI 쓸 때, 본 스테이트는 7초 정도를 줘야 안 어색함
        self.set_timer(timer_id='1', seconds=6)
        self.set_event_ui(type=0, arg2='3,3') # 3/3 스테이지
        self.show_count_ui(text='$61000005_ME__MAINPROCESS__8$', stage=3, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계3(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 퍼즐단계3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=14)
        self.use_state(id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 퍼즐단계3정리(self.ctx)


class 퍼즐단계3정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176], visible=True) # 퍼즐 큐브를 모두 보인다(arg2=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐단계3종료(self.ctx)
        if not self.user_detected(box_ids=[197,198,199]):
            # 아무도 살아남지 못한다면
            return 모두실패(self.ctx)


class 퍼즐단계3종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[197,198,199]):
            self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176], visible=True) # 퍼즐 큐브를 모두 보인다(arg2=1)
            return 보상단계(self.ctx)


# 성공한 사람이 있을 경우 보상
class 보상단계(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=7)
        self.set_event_ui(type=0, arg2='0,0') # 이벤트 UI 사라짐
        self.set_event_ui(type=1, arg2='$61000005_ME__MAINPROCESS__9$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 돈벼락(self.ctx)


class 돈벼락(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=15)
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=1, arg2='$61000005_ME__MAINPROCESS__10$', arg3='5000', arg4='0')
        self.add_buff(box_ids=[197,198,199], skill_id=70000020, level=1)
        self.create_item(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐종료처리(self.ctx)


# 모두 실패했을 경우 처리
class 모두실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=7)
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=5, arg2='$61000005_ME__MAINPROCESS__11$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 퍼즐종료처리(self.ctx)


# 퍼즐 종료
class 퍼즐종료처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=1, arg2='$61000005_ME__MAINPROCESS__12$', arg3='5000')
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176], visible=True) # 퍼즐 큐브를 모두 보인다
        self.set_mesh(trigger_ids=[211,212]) # 닫힌 문을 가린다
        self.set_mesh(trigger_ids=[401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436]) # 퍼즐 펜스 모두 가린다
        self.set_mesh(trigger_ids=[451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494]) # 퍼즐 큐브 바운딩 모두 죽인다
        self.set_mesh(trigger_ids=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544], visible=True) # 퍼즐 큐브 외곽 발판 모두 보인다
        self.set_mesh(trigger_ids=[551,552], visible=True) # 열린 문을 보인다
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=101)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=102)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=103)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=104)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=115)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=116)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=117)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=118)
        # 탈락자용 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=500, enable=True)
        self.set_timer(timer_id='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 강제종료(self.ctx)


# 혹시라도 안 나가고 남아 있는 사람 있을 까봐 모두 밖으로 내보내는 처리
class 강제종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.move_user(map_id=63000001, portal_id=5) # 단풍나무 광장 5번 포털로 이동
        return 종료(self.ctx)


"""
퍼즐 패턴 시작
밖에서 안으로 없어지면서 들어온다. 살아남는 건 가운데 4개
"""
class 퍼즐패턴1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg3:start delay / arg4:떨어지는 간격 / 모두  1/1000초 단위
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[101,102,103,104], interval=300)
        self.set_mesh(trigger_ids=[128,138,148,158], interval=300)
        self.set_mesh(trigger_ids=[176,175,174,173], interval=300)
        self.set_mesh(trigger_ids=[149,139,129,119], interval=300)
        self.set_mesh(trigger_ids=[110,109,108,107,106,105], start_delay=2500, interval=300)
        self.set_mesh(trigger_ids=[166,157,147,137,127,118], start_delay=2500, interval=300)
        self.set_mesh(trigger_ids=[167,168,169,170,171,172], start_delay=2500, interval=300)
        self.set_mesh(trigger_ids=[111,120,130,140,150,159], start_delay=2500, interval=300)
        self.set_mesh(trigger_ids=[112,113,114,115,116], start_delay=4500, interval=300)
        self.set_mesh(trigger_ids=[117,126,136,146,156], start_delay=4500, interval=300)
        self.set_mesh(trigger_ids=[165,164,163,162,161], start_delay=4500, interval=300)
        self.set_mesh(trigger_ids=[160,151,141,131,121], start_delay=4500, interval=300)
        self.set_mesh(trigger_ids=[125,124,123], start_delay=6500, interval=300)
        self.set_mesh(trigger_ids=[122,132,142], start_delay=6500, interval=300)
        self.set_mesh(trigger_ids=[152,153,154], start_delay=6500, interval=300)
        self.set_mesh(trigger_ids=[155,145,135], start_delay=6500, interval=300)


# 안에서 밖으로 없어지면서 나간다. 살아남는 건 최 외곽의 4개씩
class 퍼즐패턴2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg3:start delay / arg4:떨어지는 간격 / 모두  1/1000초 단위
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[133,134,144,143], interval=300)
        self.set_mesh(trigger_ids=[142,132,122,123,124,125], start_delay=2500, interval=300)
        self.set_mesh(trigger_ids=[135,145,155,154,153,152], start_delay=2500, interval=300)
        self.set_mesh(trigger_ids=[113,114,115,116,117,126,136,146,156,165], start_delay=5500, interval=300)
        self.set_mesh(trigger_ids=[164,163,162,161,160,151,141,131,121,112], start_delay=5500, interval=300)
        self.set_mesh(trigger_ids=[105,106,107,108,109,110], start_delay=9500, interval=300)
        self.set_mesh(trigger_ids=[118,127,137,147,157,166], start_delay=9500, interval=300)
        self.set_mesh(trigger_ids=[172,171,170,169,168,167], start_delay=9500, interval=300)
        self.set_mesh(trigger_ids=[159,150,140,130,120,111], start_delay=9500, interval=300)


# 안과 밖에서 동시에 없어지는 패턴, 도넛 모양으로 살아 남는다
class 퍼즐패턴3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg3:start delay / arg4:떨어지는 간격 / 모두  1/1000초 단위
        self.set_timer(timer_id='1', seconds=14)
        self.set_mesh(trigger_ids=[101,102,103,104], interval=300)
        self.set_mesh(trigger_ids=[128,138,148,158], interval=300)
        self.set_mesh(trigger_ids=[176,175,174,173], interval=300)
        self.set_mesh(trigger_ids=[149,139,129,119], interval=300)
        self.set_mesh(trigger_ids=[133,134,144,143], interval=300)
        self.set_mesh(trigger_ids=[105,106,107,108,109,110], start_delay=2500, interval=300)
        self.set_mesh(trigger_ids=[118,127,137,147,157,166], start_delay=2500, interval=300)
        self.set_mesh(trigger_ids=[172,171,170,169,168,167], start_delay=2500, interval=300)
        self.set_mesh(trigger_ids=[159,150,140,130,120,111], start_delay=2500, interval=300)
        self.set_mesh(trigger_ids=[122,123,124], start_delay=2500, interval=600)
        self.set_mesh(trigger_ids=[125,135,145], start_delay=2500, interval=600)
        self.set_mesh(trigger_ids=[155,154,153], start_delay=2500, interval=600)
        self.set_mesh(trigger_ids=[152,142,132], start_delay=2500, interval=600)
        self.set_mesh(trigger_ids=[112,117,165,160], start_delay=6500, interval=300)


# 퍼즐 패턴 끝
class 종료(trigger_api.Trigger):
    pass


initial_state = 입장
