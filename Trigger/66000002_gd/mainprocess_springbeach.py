""" trigger/66000002_gd/mainprocess_springbeach.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[302]):
            return 이벤트대기중(self.ctx)


class 이벤트대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=901, visible=True, enable=True, minimap_visible=True)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164]) # 움직이는 발판을 멈춘다 (arg2=0)
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624])
        self.set_mesh(trigger_ids=[651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677], visible=True)
        self.set_mesh(trigger_ids=[701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832], visible=True)
        self.set_effect(trigger_ids=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=302) >= 50:
            return 준비멘트1(self.ctx)
        if self.wait_tick(wait_tick=30000):
            return 준비멘트1(self.ctx)


class 준비멘트1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=6)
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__0$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 준비멘트2(self.ctx)


class 준비멘트2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=4)
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__1$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 경기장입장(self.ctx)


class 경기장입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        self.move_user(map_id=66000002, portal_id=902, box_id=302)
        return 잠시대기(self.ctx)


class 잠시대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='13', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='13'):
            return 시작멘트1(self.ctx)


class 시작멘트1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mini_game_area_for_hack(box_id=301) # 해킹 보안용 시작 box 설정
        self.set_timer(timer_id='13', seconds=5)
        # 로그에서 해당 이벤트에 참여한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__2$', arg3='4000')
        # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
        # self.set_achievement(trigger_id=301, type='trigger', achieve='springbeach_start')
        # self.set_achievement(trigger_id=301, type='trigger', achieve='dailyquest_start')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='13'):
            return 시작멘트2(self.ctx)


class 시작멘트2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='14', seconds=5)
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__3$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 시작멘트3(self.ctx)


class 시작멘트3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=5)
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__4$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 라운드1(self.ctx)


# 1라운드
class 라운드1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='16', seconds=4)
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__5$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='16'):
            return 게임시작1(self.ctx)


class 게임시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='17', seconds=6)
        self.set_event_ui(type=0, arg2='1,5')
        self.show_count_ui(text='$61000007_ME__MAINPROCESS_SPRINGBEACH__6$', stage=1, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='17'):
            return 스프링섞기01(self.ctx)


class 스프링섞기01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return 스프링공격01_1(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격02_1(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격03_1(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격04_1(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격05_1(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격06_1(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격07_1(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격08_1(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격09_1(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격10_1(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격11_1(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격12_1(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격13_1(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격14_1(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격15_1(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격16_1(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격17_1(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격18_1(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격19_1(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격20_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격21_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격22_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격23_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격24_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격25_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격26_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격27_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격28_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격29_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격30_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격31_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격32_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격33_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격34_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격35_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격36_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격37_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격38_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격39_1(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격40_1(self.ctx)


class 공격중지01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='19', seconds=3)
        self.set_skill(trigger_ids=[201])
        self.set_skill(trigger_ids=[202])
        self.set_skill(trigger_ids=[203])
        self.set_skill(trigger_ids=[204])
        self.set_skill(trigger_ids=[205])
        self.set_skill(trigger_ids=[206])
        self.set_skill(trigger_ids=[207])
        self.set_skill(trigger_ids=[208])
        self.set_skill(trigger_ids=[209])
        self.set_skill(trigger_ids=[210])
        self.set_skill(trigger_ids=[211])
        self.set_skill(trigger_ids=[212])
        self.set_skill(trigger_ids=[213])
        self.set_skill(trigger_ids=[214])
        self.set_skill(trigger_ids=[215])
        self.set_skill(trigger_ids=[216])
        self.set_skill(trigger_ids=[217])
        self.set_skill(trigger_ids=[218])
        self.set_skill(trigger_ids=[219])
        self.set_skill(trigger_ids=[220])
        self.set_skill(trigger_ids=[221])
        self.set_skill(trigger_ids=[222])
        self.set_skill(trigger_ids=[223])
        self.set_skill(trigger_ids=[224])
        self.set_skill(trigger_ids=[225])
        self.set_skill(trigger_ids=[226])
        self.set_skill(trigger_ids=[227])
        self.set_skill(trigger_ids=[228])
        self.set_skill(trigger_ids=[229])
        self.set_skill(trigger_ids=[230])
        self.set_skill(trigger_ids=[231])
        self.set_skill(trigger_ids=[232])
        self.set_skill(trigger_ids=[233])
        self.set_skill(trigger_ids=[234])
        self.set_skill(trigger_ids=[235])
        self.set_skill(trigger_ids=[236])
        self.set_skill(trigger_ids=[237])
        self.set_skill(trigger_ids=[238])
        self.set_skill(trigger_ids=[239])
        self.set_skill(trigger_ids=[240])
        self.set_skill(trigger_ids=[241])
        self.set_skill(trigger_ids=[242])
        self.set_skill(trigger_ids=[243])
        self.set_skill(trigger_ids=[244])
        self.set_skill(trigger_ids=[245])
        self.set_skill(trigger_ids=[246])
        self.set_skill(trigger_ids=[247])
        self.set_skill(trigger_ids=[248])
        self.set_skill(trigger_ids=[249])
        self.set_skill(trigger_ids=[250])
        self.set_skill(trigger_ids=[251])
        self.set_skill(trigger_ids=[252])
        self.set_skill(trigger_ids=[253])
        self.set_skill(trigger_ids=[254])
        self.set_skill(trigger_ids=[255])
        self.set_skill(trigger_ids=[256])
        self.set_skill(trigger_ids=[257])
        self.set_skill(trigger_ids=[258])
        self.set_skill(trigger_ids=[259])
        self.set_skill(trigger_ids=[260])
        self.set_skill(trigger_ids=[261])
        self.set_skill(trigger_ids=[262])
        self.set_skill(trigger_ids=[263])
        self.set_skill(trigger_ids=[264])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='19'):
            return 생존자수색01(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 모두탈락(self.ctx)


class 생존자수색01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            return 한숨돌리기01(self.ctx)


class 한숨돌리기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 라운드2(self.ctx)


# 2라운드
class 라운드2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='21', seconds=4)
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__7$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='21'):
            return 게임시작2(self.ctx)


class 게임시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='22', seconds=6)
        self.set_event_ui(type=0, arg2='2,5')
        self.show_count_ui(text='$61000007_ME__MAINPROCESS_SPRINGBEACH__8$', stage=2, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='22'):
            return 스프링섞기02(self.ctx)


class 스프링섞기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=2.0):
            return 스프링공격01_2(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격02_2(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격03_2(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격04_2(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격05_2(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격06_2(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격07_2(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격08_2(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격09_2(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격10_2(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격11_2(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격12_2(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격13_2(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격14_2(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격15_2(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격16_2(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격17_2(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격18_2(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격19_2(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격20_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격21_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격22_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격23_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격24_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격25_2(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격26_2(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격27_2(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격28_2(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격29_2(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격30_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격31_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격32_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격33_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격34_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격35_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격36_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격37_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격38_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격39_2(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격40_2(self.ctx)


class 공격중지02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='23', seconds=3)
        self.set_skill(trigger_ids=[201])
        self.set_skill(trigger_ids=[202])
        self.set_skill(trigger_ids=[203])
        self.set_skill(trigger_ids=[204])
        self.set_skill(trigger_ids=[205])
        self.set_skill(trigger_ids=[206])
        self.set_skill(trigger_ids=[207])
        self.set_skill(trigger_ids=[208])
        self.set_skill(trigger_ids=[209])
        self.set_skill(trigger_ids=[210])
        self.set_skill(trigger_ids=[211])
        self.set_skill(trigger_ids=[212])
        self.set_skill(trigger_ids=[213])
        self.set_skill(trigger_ids=[214])
        self.set_skill(trigger_ids=[215])
        self.set_skill(trigger_ids=[216])
        self.set_skill(trigger_ids=[217])
        self.set_skill(trigger_ids=[218])
        self.set_skill(trigger_ids=[219])
        self.set_skill(trigger_ids=[220])
        self.set_skill(trigger_ids=[221])
        self.set_skill(trigger_ids=[222])
        self.set_skill(trigger_ids=[223])
        self.set_skill(trigger_ids=[224])
        self.set_skill(trigger_ids=[225])
        self.set_skill(trigger_ids=[226])
        self.set_skill(trigger_ids=[227])
        self.set_skill(trigger_ids=[228])
        self.set_skill(trigger_ids=[229])
        self.set_skill(trigger_ids=[230])
        self.set_skill(trigger_ids=[231])
        self.set_skill(trigger_ids=[232])
        self.set_skill(trigger_ids=[233])
        self.set_skill(trigger_ids=[234])
        self.set_skill(trigger_ids=[235])
        self.set_skill(trigger_ids=[236])
        self.set_skill(trigger_ids=[237])
        self.set_skill(trigger_ids=[238])
        self.set_skill(trigger_ids=[239])
        self.set_skill(trigger_ids=[240])
        self.set_skill(trigger_ids=[241])
        self.set_skill(trigger_ids=[242])
        self.set_skill(trigger_ids=[243])
        self.set_skill(trigger_ids=[244])
        self.set_skill(trigger_ids=[245])
        self.set_skill(trigger_ids=[246])
        self.set_skill(trigger_ids=[247])
        self.set_skill(trigger_ids=[248])
        self.set_skill(trigger_ids=[249])
        self.set_skill(trigger_ids=[250])
        self.set_skill(trigger_ids=[251])
        self.set_skill(trigger_ids=[252])
        self.set_skill(trigger_ids=[253])
        self.set_skill(trigger_ids=[254])
        self.set_skill(trigger_ids=[255])
        self.set_skill(trigger_ids=[256])
        self.set_skill(trigger_ids=[257])
        self.set_skill(trigger_ids=[258])
        self.set_skill(trigger_ids=[259])
        self.set_skill(trigger_ids=[260])
        self.set_skill(trigger_ids=[261])
        self.set_skill(trigger_ids=[262])
        self.set_skill(trigger_ids=[263])
        self.set_skill(trigger_ids=[264])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='23'):
            return 생존자수색02(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 모두탈락(self.ctx)


class 생존자수색02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            return 한숨돌리기02(self.ctx)


class 한숨돌리기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='24', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='24'):
            return 라운드3(self.ctx)


# 3라운드
class 라운드3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='25', seconds=4)
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__9$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='25'):
            return 게임시작3(self.ctx)


class 게임시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='26', seconds=6)
        self.set_event_ui(type=0, arg2='3,5')
        self.show_count_ui(text='$61000007_ME__MAINPROCESS_SPRINGBEACH__10$', stage=3, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='26'):
            return 스프링섞기03(self.ctx)


class 스프링섞기03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return 스프링공격01_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격02_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격03_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격04_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격05_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격06_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격07_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격08_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격09_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격10_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격11_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격12_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격13_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격14_3(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격15_3(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격16_3(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격17_3(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격18_3(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격19_3(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격20_3(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격21_3(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격22_3(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격23_3(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격24_3(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격25_3(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격26_3(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격27_3(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격28_3(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격29_3(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격30_3(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격31_3(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격32_3(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격33_3(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격34_3(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격35_3(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격36_3(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격37_3(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격38_3(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격39_3(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격40_3(self.ctx)


class 공격중지03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='27', seconds=3)
        self.set_skill(trigger_ids=[201])
        self.set_skill(trigger_ids=[202])
        self.set_skill(trigger_ids=[203])
        self.set_skill(trigger_ids=[204])
        self.set_skill(trigger_ids=[205])
        self.set_skill(trigger_ids=[206])
        self.set_skill(trigger_ids=[207])
        self.set_skill(trigger_ids=[208])
        self.set_skill(trigger_ids=[209])
        self.set_skill(trigger_ids=[210])
        self.set_skill(trigger_ids=[211])
        self.set_skill(trigger_ids=[212])
        self.set_skill(trigger_ids=[213])
        self.set_skill(trigger_ids=[214])
        self.set_skill(trigger_ids=[215])
        self.set_skill(trigger_ids=[216])
        self.set_skill(trigger_ids=[217])
        self.set_skill(trigger_ids=[218])
        self.set_skill(trigger_ids=[219])
        self.set_skill(trigger_ids=[220])
        self.set_skill(trigger_ids=[221])
        self.set_skill(trigger_ids=[222])
        self.set_skill(trigger_ids=[223])
        self.set_skill(trigger_ids=[224])
        self.set_skill(trigger_ids=[225])
        self.set_skill(trigger_ids=[226])
        self.set_skill(trigger_ids=[227])
        self.set_skill(trigger_ids=[228])
        self.set_skill(trigger_ids=[229])
        self.set_skill(trigger_ids=[230])
        self.set_skill(trigger_ids=[231])
        self.set_skill(trigger_ids=[232])
        self.set_skill(trigger_ids=[233])
        self.set_skill(trigger_ids=[234])
        self.set_skill(trigger_ids=[235])
        self.set_skill(trigger_ids=[236])
        self.set_skill(trigger_ids=[237])
        self.set_skill(trigger_ids=[238])
        self.set_skill(trigger_ids=[239])
        self.set_skill(trigger_ids=[240])
        self.set_skill(trigger_ids=[241])
        self.set_skill(trigger_ids=[242])
        self.set_skill(trigger_ids=[243])
        self.set_skill(trigger_ids=[244])
        self.set_skill(trigger_ids=[245])
        self.set_skill(trigger_ids=[246])
        self.set_skill(trigger_ids=[247])
        self.set_skill(trigger_ids=[248])
        self.set_skill(trigger_ids=[249])
        self.set_skill(trigger_ids=[250])
        self.set_skill(trigger_ids=[251])
        self.set_skill(trigger_ids=[252])
        self.set_skill(trigger_ids=[253])
        self.set_skill(trigger_ids=[254])
        self.set_skill(trigger_ids=[255])
        self.set_skill(trigger_ids=[256])
        self.set_skill(trigger_ids=[257])
        self.set_skill(trigger_ids=[258])
        self.set_skill(trigger_ids=[259])
        self.set_skill(trigger_ids=[260])
        self.set_skill(trigger_ids=[261])
        self.set_skill(trigger_ids=[262])
        self.set_skill(trigger_ids=[263])
        self.set_skill(trigger_ids=[264])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='27'):
            return 생존자수색03(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 모두탈락(self.ctx)


class 생존자수색03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            return 한숨돌리기03(self.ctx)


class 한숨돌리기03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='28', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='28'):
            return 라운드4(self.ctx)


# 4라운드
class 라운드4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='29', seconds=4)
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__11$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='29'):
            return 게임시작4(self.ctx)


class 게임시작4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=6)
        self.set_event_ui(type=0, arg2='4,5')
        self.show_count_ui(text='$61000007_ME__MAINPROCESS_SPRINGBEACH__12$', stage=4, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 스프링섞기04(self.ctx)


class 스프링섞기04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return 스프링공격01_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격02_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격03_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격04_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격05_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격06_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격07_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격08_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격09_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격10_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격11_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격12_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격13_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격14_4(self.ctx)
        if self.random_condition(weight=1.0):
            return 스프링공격15_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격16_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격17_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격18_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격19_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격20_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격21_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격22_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격23_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격24_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격25_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격26_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격27_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격28_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격29_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격30_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격31_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격32_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격33_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격34_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격35_4(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격36_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격37_4(self.ctx)
        if self.random_condition(weight=3.0):
            return 스프링공격38_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격39_4(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격40_4(self.ctx)


class 공격중지04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='31', seconds=3)
        self.set_skill(trigger_ids=[201])
        self.set_skill(trigger_ids=[202])
        self.set_skill(trigger_ids=[203])
        self.set_skill(trigger_ids=[204])
        self.set_skill(trigger_ids=[205])
        self.set_skill(trigger_ids=[206])
        self.set_skill(trigger_ids=[207])
        self.set_skill(trigger_ids=[208])
        self.set_skill(trigger_ids=[209])
        self.set_skill(trigger_ids=[210])
        self.set_skill(trigger_ids=[211])
        self.set_skill(trigger_ids=[212])
        self.set_skill(trigger_ids=[213])
        self.set_skill(trigger_ids=[214])
        self.set_skill(trigger_ids=[215])
        self.set_skill(trigger_ids=[216])
        self.set_skill(trigger_ids=[217])
        self.set_skill(trigger_ids=[218])
        self.set_skill(trigger_ids=[219])
        self.set_skill(trigger_ids=[220])
        self.set_skill(trigger_ids=[221])
        self.set_skill(trigger_ids=[222])
        self.set_skill(trigger_ids=[223])
        self.set_skill(trigger_ids=[224])
        self.set_skill(trigger_ids=[225])
        self.set_skill(trigger_ids=[226])
        self.set_skill(trigger_ids=[227])
        self.set_skill(trigger_ids=[228])
        self.set_skill(trigger_ids=[229])
        self.set_skill(trigger_ids=[230])
        self.set_skill(trigger_ids=[231])
        self.set_skill(trigger_ids=[232])
        self.set_skill(trigger_ids=[233])
        self.set_skill(trigger_ids=[234])
        self.set_skill(trigger_ids=[235])
        self.set_skill(trigger_ids=[236])
        self.set_skill(trigger_ids=[237])
        self.set_skill(trigger_ids=[238])
        self.set_skill(trigger_ids=[239])
        self.set_skill(trigger_ids=[240])
        self.set_skill(trigger_ids=[241])
        self.set_skill(trigger_ids=[242])
        self.set_skill(trigger_ids=[243])
        self.set_skill(trigger_ids=[244])
        self.set_skill(trigger_ids=[245])
        self.set_skill(trigger_ids=[246])
        self.set_skill(trigger_ids=[247])
        self.set_skill(trigger_ids=[248])
        self.set_skill(trigger_ids=[249])
        self.set_skill(trigger_ids=[250])
        self.set_skill(trigger_ids=[251])
        self.set_skill(trigger_ids=[252])
        self.set_skill(trigger_ids=[253])
        self.set_skill(trigger_ids=[254])
        self.set_skill(trigger_ids=[255])
        self.set_skill(trigger_ids=[256])
        self.set_skill(trigger_ids=[257])
        self.set_skill(trigger_ids=[258])
        self.set_skill(trigger_ids=[259])
        self.set_skill(trigger_ids=[260])
        self.set_skill(trigger_ids=[261])
        self.set_skill(trigger_ids=[262])
        self.set_skill(trigger_ids=[263])
        self.set_skill(trigger_ids=[264])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='31'):
            return 생존자수색04(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 모두탈락(self.ctx)


class 생존자수색04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            return 한숨돌리기04(self.ctx)


class 한숨돌리기04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='32', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='32'):
            return 라운드5(self.ctx)


# 5라운드
class 라운드5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='33', seconds=4)
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__13$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='33'):
            return 게임시작5(self.ctx)


class 게임시작5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='34', seconds=6)
        self.set_event_ui(type=0, arg2='5,5')
        self.show_count_ui(text='$61000007_ME__MAINPROCESS_SPRINGBEACH__14$', stage=5, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='34'):
            return 스프링섞기05(self.ctx)


class 스프링섞기05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=2.0):
            return 스프링공격16_5(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격17_5(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격18_5(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격19_5(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격20_5(self.ctx)
        if self.random_condition(weight=6.0):
            return 스프링공격21_5(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격22_5(self.ctx)
        if self.random_condition(weight=6.0):
            return 스프링공격23_5(self.ctx)
        if self.random_condition(weight=6.0):
            return 스프링공격24_5(self.ctx)
        if self.random_condition(weight=6.0):
            return 스프링공격25_5(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격26_5(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격27_5(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격28_5(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격29_5(self.ctx)
        if self.random_condition(weight=2.0):
            return 스프링공격30_5(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격31_5(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격32_5(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격33_5(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격34_5(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격35_5(self.ctx)
        if self.random_condition(weight=4.0):
            return 스프링공격36_5(self.ctx)
        if self.random_condition(weight=6.0):
            return 스프링공격37_5(self.ctx)
        if self.random_condition(weight=6.0):
            return 스프링공격38_5(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격39_5(self.ctx)
        if self.random_condition(weight=5.0):
            return 스프링공격40_5(self.ctx)


class 공격중지05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='35', seconds=3)
        self.set_skill(trigger_ids=[201])
        self.set_skill(trigger_ids=[202])
        self.set_skill(trigger_ids=[203])
        self.set_skill(trigger_ids=[204])
        self.set_skill(trigger_ids=[205])
        self.set_skill(trigger_ids=[206])
        self.set_skill(trigger_ids=[207])
        self.set_skill(trigger_ids=[208])
        self.set_skill(trigger_ids=[209])
        self.set_skill(trigger_ids=[210])
        self.set_skill(trigger_ids=[211])
        self.set_skill(trigger_ids=[212])
        self.set_skill(trigger_ids=[213])
        self.set_skill(trigger_ids=[214])
        self.set_skill(trigger_ids=[215])
        self.set_skill(trigger_ids=[216])
        self.set_skill(trigger_ids=[217])
        self.set_skill(trigger_ids=[218])
        self.set_skill(trigger_ids=[219])
        self.set_skill(trigger_ids=[220])
        self.set_skill(trigger_ids=[221])
        self.set_skill(trigger_ids=[222])
        self.set_skill(trigger_ids=[223])
        self.set_skill(trigger_ids=[224])
        self.set_skill(trigger_ids=[225])
        self.set_skill(trigger_ids=[226])
        self.set_skill(trigger_ids=[227])
        self.set_skill(trigger_ids=[228])
        self.set_skill(trigger_ids=[229])
        self.set_skill(trigger_ids=[230])
        self.set_skill(trigger_ids=[231])
        self.set_skill(trigger_ids=[232])
        self.set_skill(trigger_ids=[233])
        self.set_skill(trigger_ids=[234])
        self.set_skill(trigger_ids=[235])
        self.set_skill(trigger_ids=[236])
        self.set_skill(trigger_ids=[237])
        self.set_skill(trigger_ids=[238])
        self.set_skill(trigger_ids=[239])
        self.set_skill(trigger_ids=[240])
        self.set_skill(trigger_ids=[241])
        self.set_skill(trigger_ids=[242])
        self.set_skill(trigger_ids=[243])
        self.set_skill(trigger_ids=[244])
        self.set_skill(trigger_ids=[245])
        self.set_skill(trigger_ids=[246])
        self.set_skill(trigger_ids=[247])
        self.set_skill(trigger_ids=[248])
        self.set_skill(trigger_ids=[249])
        self.set_skill(trigger_ids=[250])
        self.set_skill(trigger_ids=[251])
        self.set_skill(trigger_ids=[252])
        self.set_skill(trigger_ids=[253])
        self.set_skill(trigger_ids=[254])
        self.set_skill(trigger_ids=[255])
        self.set_skill(trigger_ids=[256])
        self.set_skill(trigger_ids=[257])
        self.set_skill(trigger_ids=[258])
        self.set_skill(trigger_ids=[259])
        self.set_skill(trigger_ids=[260])
        self.set_skill(trigger_ids=[261])
        self.set_skill(trigger_ids=[262])
        self.set_skill(trigger_ids=[263])
        self.set_skill(trigger_ids=[264])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='35'):
            return 생존자수색05(self.ctx)
        if not self.user_detected(box_ids=[301]):
            return 모두탈락(self.ctx)


class 생존자수색05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            return 한숨돌리기05(self.ctx)


class 한숨돌리기05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='36', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='36'):
            return 보상단계(self.ctx)


class 보상단계(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='37', seconds=7)
        self.set_event_ui(type=3, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__15$', arg3='5000', arg4='301')
        # 로그에서 해당 이벤트에서 우승한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id
        self.set_event_ui(type=6, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__16$', arg3='5000', arg4='303,304,305,306')
        # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
        # self.set_achievement(trigger_id=301, type='trigger', achieve='springbeach_win')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='37'):
            return 경험치지급(self.ctx)


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
        self.set_timer(timer_id='38', seconds=6)
        # self.set_event_ui(type=3, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__17$', arg3='5000', arg4='301')
        # self.set_event_ui(type=6, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__18$', arg3='5000', arg4='303,304,305,306')
        # self.add_buff(box_ids=[301], skill_id=70000019, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='38'):
            return 다리등장(self.ctx)


"""
class 돈벼락(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='39', seconds=20)
        self.set_event_ui(type=3, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__19$', arg3='5000', arg4='301')
        self.set_event_ui(type=6, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__20$', arg3='5000', arg4='303,304,305,306')
        self.create_item(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='39'):
            return 다리등장(self.ctx)
"""

# 생존자없음
class 모두탈락(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='40', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='40'):
            return 탈락멘트(self.ctx)


class 탈락멘트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='40', seconds=6)
        self.set_event_ui(type=5, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__21$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='40'):
            return 다리등장(self.ctx)


# 마무리
class 다리등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_timer(timer_id='41', seconds=10)
        self.set_mesh(trigger_ids=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624], visible=True)
        self.set_mesh(trigger_ids=[651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677])
        self.set_mesh(trigger_ids=[701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832])
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__22$', arg3='10000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='41'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__23$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=120000):
            self.move_user()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


# 패턴 목록_라운드1
class 스프링공격01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[105,106,107,108,117,118,119,120,129,130,131,132,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_101(self.ctx)


class 게임진행1_101(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,137,138,139,140,150,151,152,153], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_102(self.ctx)


class 게임진행1_102(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,109,110,111,112,113,114,115,116,121,122,123,124,129,130,131,132,141,142,143,144,145,154,155,156,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_103(self.ctx)


class 게임진행1_103(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[107,117,118,119,120,121,127,128,129,133,134,135,137,138,139,147,148,149,150,151,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_104(self.ctx)


class 게임진행1_104(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격05_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[104,105,108,109,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,140,141,145,146,153,154,160,161], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_105(self.ctx)


class 게임진행1_105(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격06_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,108,109,110,111,112,113,114,115,116,117,120,121,128,129,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_106(self.ctx)


class 게임진행1_106(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격07_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,111,112,115,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,137,138,143,148,149,150,151,156,157,158,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_107(self.ctx)


class 게임진행1_107(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격08_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[107,108,109,110,111,112,113,114,115,116,117,118,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,151,152,155,156], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_108(self.ctx)


class 게임진행1_108(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격09_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,112,113,115,116,117,118,119,122,124,125,127,130,131,132,133,134,136,137,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_109(self.ctx)


class 게임진행1_109(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격10_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,106,107,110,111,112,113,114,115,118,131,134,135,136,137,138,139,142,143,144,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_110(self.ctx)


class 게임진행1_110(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격11_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,112,113,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_111(self.ctx)


class 게임진행1_111(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격12_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,107,108,113,114,115,116,119,120,125,126,127,128,131,132,138,140,142,146,147,148,149,151,153,155,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_112(self.ctx)


class 게임진행1_112(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격13_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_113(self.ctx)


class 게임진행1_113(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격14_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,106,108,109,111,114,116,117,119,120,121,122,124,125,127,128,129,130,132,133,135,138,139,142,143,145,146,148,150,153,154,157,159,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_114(self.ctx)


class 게임진행1_114(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격15_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,105,106,109,110,111,112,115,116,117,118,119,120,123,124,125,126,127,128,131,132,133,134,137,138,140,141,143,144,145,148,149,151,153,154,156,157,158,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_115(self.ctx)


class 게임진행1_115(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격16_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_116(self.ctx)


class 게임진행1_116(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격17_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,119,120,121,122,125,126,127,128,129,130,131,132,135,136,138,139,140,142,143,146,147,148,149,151,152,153,155,156,157,158,159,160,161,162], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_117(self.ctx)


class 게임진행1_117(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격18_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,104,105,106,107,109,110,111,113,114,116,117,118,119,121,122,123,125,126,128,129,130,131,133,134,135,138,140,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_118(self.ctx)


class 게임진행1_118(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격19_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,138,139,142,143,144,145,146,147,148,150,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_119(self.ctx)


class 게임진행1_119(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격20_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,105,106,107,108,109,110,111,112,115,116,117,118,119,121,122,123,124,125,126,127,129,130,131,132,133,134,137,138,140,141,143,144,145,146,147,148,149,150,151,153,154,156,157,158,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_120(self.ctx)


class 게임진행1_120(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격21_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,111,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_121(self.ctx)


class 게임진행1_121(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격22_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,120,121,122,123,125,126,127,128,129,130,131,132,134,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156,157,158,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_122(self.ctx)


class 게임진행1_122(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격23_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_123(self.ctx)


class 게임진행1_123(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격24_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_124(self.ctx)


class 게임진행1_124(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격25_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_125(self.ctx)


class 게임진행1_125(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격26_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,120,122,124,125,127,129,130,132,133,135,136,137,138,139,142,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_126(self.ctx)


class 게임진행1_126(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격27_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,110,111,112,113,114,116,117,120,121,122,123,124,125,126,127,130,132,133,134,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_127(self.ctx)


class 게임진행1_127(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격28_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,110,111,112,113,116,118,119,120,122,123,126,127,129,130,131,133,136,137,139,140,142,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_128(self.ctx)


class 게임진행1_128(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격29_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,109,110,112,113,115,117,118,119,120,122,124,125,127,129,130,131,132,134,136,137,138,143,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_129(self.ctx)


class 게임진행1_129(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격30_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,112,113,114,115,116,117,119,121,122,123,124,125,126,127,129,130,131,132,133,135,136,137,139,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_130(self.ctx)


class 게임진행1_130(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격31_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,113,115,116,117,118,119,120,121,123,124,125,126,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_131(self.ctx)


class 게임진행1_131(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격32_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,131,132,133,134,135,136,137,138,140,141,143,144,145,146,147,148,149,150,152,153,154,155,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_132(self.ctx)


class 게임진행1_132(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격33_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,105,106,107,108,109,111,112,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,156,157,158,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_133(self.ctx)


class 게임진행1_133(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격34_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,110,111,112,113,114,116,118,119,121,122,123,124,125,126,127,128,130,131,133,134,135,136,137,138,139,140,141,142,143,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_134(self.ctx)


class 게임진행1_134(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격35_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,122,123,126,127,128,129,130,131,132,133,134,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_135(self.ctx)


class 게임진행1_135(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격36_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,158,159,160,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_136(self.ctx)


class 게임진행1_136(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격37_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_137(self.ctx)


class 게임진행1_137(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격38_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_138(self.ctx)


class 게임진행1_138(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격39_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,133,135,136,137,138,139,140,141,142,144,145,146,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_139(self.ctx)


class 게임진행1_139(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


class 스프링공격40_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[102,103,104,105,106,107,108,109,110,112,113,114,116,117,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_140(self.ctx)


class 게임진행1_140(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지01(self.ctx)


# 패턴 목록_라운드2
class 스프링공격01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[105,106,107,108,117,118,119,120,129,130,131,132,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_201(self.ctx)


class 게임진행1_201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,137,138,139,140,150,151,152,153], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_202(self.ctx)


class 게임진행1_202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격03_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,109,110,111,112,113,114,115,116,121,122,123,124,129,130,131,132,141,142,143,144,145,154,155,156,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_203(self.ctx)


class 게임진행1_203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격04_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[107,117,118,119,120,121,127,128,129,133,134,135,137,138,139,147,148,149,150,151,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_204(self.ctx)


class 게임진행1_204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=2)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격05_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[104,105,108,109,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,140,141,145,146,153,154,160,161], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_205(self.ctx)


class 게임진행1_205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격06_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,108,109,110,111,112,113,114,115,116,117,120,121,128,129,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_206(self.ctx)


class 게임진행1_206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격07_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,111,112,115,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,137,138,143,148,149,150,151,156,157,158,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_207(self.ctx)


class 게임진행1_207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격08_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[107,108,109,110,111,112,113,114,115,116,117,118,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,151,152,155,156], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_208(self.ctx)


class 게임진행1_208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격09_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,112,113,115,116,117,118,119,122,124,125,127,130,131,132,133,134,136,137,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_209(self.ctx)


class 게임진행1_209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격10_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,106,107,110,111,112,113,114,115,118,131,134,135,136,137,138,139,142,143,144,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_210(self.ctx)


class 게임진행1_210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격11_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,112,113,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_211(self.ctx)


class 게임진행1_211(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격12_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,107,108,113,114,115,116,119,120,125,126,127,128,131,132,138,140,142,146,147,148,149,151,153,155,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_212(self.ctx)


class 게임진행1_212(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격13_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_213(self.ctx)


class 게임진행1_213(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격14_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,106,108,109,111,114,116,117,119,120,121,122,124,125,127,128,129,130,132,133,135,138,139,142,143,145,146,148,150,153,154,157,159,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_214(self.ctx)


class 게임진행1_214(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격15_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,105,106,109,110,111,112,115,116,117,118,119,120,123,124,125,126,127,128,131,132,133,134,137,138,140,141,143,144,145,148,149,151,153,154,156,157,158,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_215(self.ctx)


class 게임진행1_215(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격16_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_216(self.ctx)


class 게임진행1_216(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격17_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,119,120,121,122,125,126,127,128,129,130,131,132,135,136,138,139,140,142,143,146,147,148,149,151,152,153,155,156,157,158,159,160,161,162], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_217(self.ctx)


class 게임진행1_217(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격18_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,104,105,106,107,109,110,111,113,114,116,117,118,119,121,122,123,125,126,128,129,130,131,133,134,135,138,140,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_218(self.ctx)


class 게임진행1_218(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격19_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,138,139,142,143,144,145,146,147,148,150,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_219(self.ctx)


class 게임진행1_219(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격20_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,105,106,107,108,109,110,111,112,115,116,117,118,119,121,122,123,124,125,126,127,129,130,131,132,133,134,137,138,140,141,143,144,145,146,147,148,149,150,151,153,154,156,157,158,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_220(self.ctx)


class 게임진행1_220(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격21_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,111,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_221(self.ctx)


class 게임진행1_221(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격22_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,120,121,122,123,125,126,127,128,129,130,131,132,134,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156,157,158,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_222(self.ctx)


class 게임진행1_222(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격23_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_223(self.ctx)


class 게임진행1_223(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격24_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_224(self.ctx)


class 게임진행1_224(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격25_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_225(self.ctx)


class 게임진행1_225(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격26_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,120,122,124,125,127,129,130,132,133,135,136,137,138,139,142,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_226(self.ctx)


class 게임진행1_226(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격27_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,110,111,112,113,114,116,117,120,121,122,123,124,125,126,127,130,132,133,134,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_227(self.ctx)


class 게임진행1_227(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격28_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,110,111,112,113,116,118,119,120,122,123,126,127,129,130,131,133,136,137,139,140,142,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_228(self.ctx)


class 게임진행1_228(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격29_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,109,110,112,113,115,117,118,119,120,122,124,125,127,129,130,131,132,134,136,137,138,143,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_229(self.ctx)


class 게임진행1_229(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격30_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,112,113,114,115,116,117,119,121,122,123,124,125,126,127,129,130,131,132,133,135,136,137,139,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_230(self.ctx)


class 게임진행1_230(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격31_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,113,115,116,117,118,119,120,121,123,124,125,126,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_231(self.ctx)


class 게임진행1_231(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격32_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,131,132,133,134,135,136,137,138,140,141,143,144,145,146,147,148,149,150,152,153,154,155,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_232(self.ctx)


class 게임진행1_232(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격33_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,105,106,107,108,109,111,112,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,156,157,158,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_233(self.ctx)


class 게임진행1_233(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격34_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,110,111,112,113,114,116,118,119,121,122,123,124,125,126,127,128,130,131,133,134,135,136,137,138,139,140,141,142,143,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_234(self.ctx)


class 게임진행1_234(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격35_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,122,123,126,127,128,129,130,131,132,133,134,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_235(self.ctx)


class 게임진행1_235(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격36_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,158,159,160,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_236(self.ctx)


class 게임진행1_236(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격37_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_237(self.ctx)


class 게임진행1_237(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격38_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_238(self.ctx)


class 게임진행1_238(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격39_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,133,135,136,137,138,139,140,141,142,144,145,146,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_239(self.ctx)


class 게임진행1_239(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


class 스프링공격40_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[102,103,104,105,106,107,108,109,110,112,113,114,116,117,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_240(self.ctx)


class 게임진행1_240(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지02(self.ctx)


# 패턴 목록_라운드3
class 스프링공격01_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[105,106,107,108,117,118,119,120,129,130,131,132,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_301(self.ctx)


class 게임진행1_301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격02_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,137,138,139,140,150,151,152,153], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_302(self.ctx)


class 게임진행1_302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,109,110,111,112,113,114,115,116,121,122,123,124,129,130,131,132,141,142,143,144,145,154,155,156,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_303(self.ctx)


class 게임진행1_303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격04_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[107,117,118,119,120,121,127,128,129,133,134,135,137,138,139,147,148,149,150,151,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_304(self.ctx)


class 게임진행1_304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격05_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[104,105,108,109,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,140,141,145,146,153,154,160,161], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_305(self.ctx)


class 게임진행1_305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격06_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,108,109,110,111,112,113,114,115,116,117,120,121,128,129,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_306(self.ctx)


class 게임진행1_306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격07_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,111,112,115,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,137,138,143,148,149,150,151,156,157,158,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_307(self.ctx)


class 게임진행1_307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격08_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[107,108,109,110,111,112,113,114,115,116,117,118,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,151,152,155,156], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_308(self.ctx)


class 게임진행1_308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격09_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,112,113,115,116,117,118,119,122,124,125,127,130,131,132,133,134,136,137,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_309(self.ctx)


class 게임진행1_309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격10_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,106,107,110,111,112,113,114,115,118,131,134,135,136,137,138,139,142,143,144,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_310(self.ctx)


class 게임진행1_310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격11_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,112,113,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_311(self.ctx)


class 게임진행1_311(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격12_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,107,108,113,114,115,116,119,120,125,126,127,128,131,132,138,140,142,146,147,148,149,151,153,155,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_312(self.ctx)


class 게임진행1_312(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격13_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_313(self.ctx)


class 게임진행1_313(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격14_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,106,108,109,111,114,116,117,119,120,121,122,124,125,127,128,129,130,132,133,135,138,139,142,143,145,146,148,150,153,154,157,159,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_314(self.ctx)


class 게임진행1_314(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격15_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,105,106,109,110,111,112,115,116,117,118,119,120,123,124,125,126,127,128,131,132,133,134,137,138,140,141,143,144,145,148,149,151,153,154,156,157,158,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_315(self.ctx)


class 게임진행1_315(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격16_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_316(self.ctx)


class 게임진행1_316(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격17_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,119,120,121,122,125,126,127,128,129,130,131,132,135,136,138,139,140,142,143,146,147,148,149,151,152,153,155,156,157,158,159,160,161,162], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_317(self.ctx)


class 게임진행1_317(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격18_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,104,105,106,107,109,110,111,113,114,116,117,118,119,121,122,123,125,126,128,129,130,131,133,134,135,138,140,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_318(self.ctx)


class 게임진행1_318(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격19_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,138,139,142,143,144,145,146,147,148,150,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_319(self.ctx)


class 게임진행1_319(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격20_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,105,106,107,108,109,110,111,112,115,116,117,118,119,121,122,123,124,125,126,127,129,130,131,132,133,134,137,138,140,141,143,144,145,146,147,148,149,150,151,153,154,156,157,158,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_320(self.ctx)


class 게임진행1_320(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격21_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,111,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_321(self.ctx)


class 게임진행1_321(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격22_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,120,121,122,123,125,126,127,128,129,130,131,132,134,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156,157,158,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_322(self.ctx)


class 게임진행1_322(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격23_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_323(self.ctx)


class 게임진행1_323(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격24_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_324(self.ctx)


class 게임진행1_324(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격25_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_325(self.ctx)


class 게임진행1_325(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격26_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,120,122,124,125,127,129,130,132,133,135,136,137,138,139,142,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_326(self.ctx)


class 게임진행1_326(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격27_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,110,111,112,113,114,116,117,120,121,122,123,124,125,126,127,130,132,133,134,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_327(self.ctx)


class 게임진행1_327(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격28_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,110,111,112,113,116,118,119,120,122,123,126,127,129,130,131,133,136,137,139,140,142,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_328(self.ctx)


class 게임진행1_328(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격29_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,109,110,112,113,115,117,118,119,120,122,124,125,127,129,130,131,132,134,136,137,138,143,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_329(self.ctx)


class 게임진행1_329(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격30_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,112,113,114,115,116,117,119,121,122,123,124,125,126,127,129,130,131,132,133,135,136,137,139,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_330(self.ctx)


class 게임진행1_330(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격31_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,113,115,116,117,118,119,120,121,123,124,125,126,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_331(self.ctx)


class 게임진행1_331(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격32_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,131,132,133,134,135,136,137,138,140,141,143,144,145,146,147,148,149,150,152,153,154,155,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_332(self.ctx)


class 게임진행1_332(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격33_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,105,106,107,108,109,111,112,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,156,157,158,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_333(self.ctx)


class 게임진행1_333(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격34_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,110,111,112,113,114,116,118,119,121,122,123,124,125,126,127,128,130,131,133,134,135,136,137,138,139,140,141,142,143,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_334(self.ctx)


class 게임진행1_334(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격35_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,122,123,126,127,128,129,130,131,132,133,134,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_335(self.ctx)


class 게임진행1_335(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격36_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,158,159,160,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_336(self.ctx)


class 게임진행1_336(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격37_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_337(self.ctx)


class 게임진행1_337(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격38_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_338(self.ctx)


class 게임진행1_338(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격39_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,133,135,136,137,138,139,140,141,142,144,145,146,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_339(self.ctx)


class 게임진행1_339(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


class 스프링공격40_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[102,103,104,105,106,107,108,109,110,112,113,114,116,117,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_340(self.ctx)


class 게임진행1_340(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지03(self.ctx)


# 패턴 목록_라운드4
class 스프링공격01_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[105,106,107,108,117,118,119,120,129,130,131,132,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_401(self.ctx)


class 게임진행1_401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격02_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,137,138,139,140,150,151,152,153], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_402(self.ctx)


class 게임진행1_402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격03_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,109,110,111,112,113,114,115,116,121,122,123,124,129,130,131,132,141,142,143,144,145,154,155,156,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_403(self.ctx)


class 게임진행1_403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격04_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[107,117,118,119,120,121,127,128,129,133,134,135,137,138,139,147,148,149,150,151,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_404(self.ctx)


class 게임진행1_404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격05_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[104,105,108,109,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,140,141,145,146,153,154,160,161], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_405(self.ctx)


class 게임진행1_405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격06_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,108,109,110,111,112,113,114,115,116,117,120,121,128,129,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_406(self.ctx)


class 게임진행1_406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격07_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,111,112,115,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,137,138,143,148,149,150,151,156,157,158,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_407(self.ctx)


class 게임진행1_407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격08_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[107,108,109,110,111,112,113,114,115,116,117,118,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,151,152,155,156], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_408(self.ctx)


class 게임진행1_408(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격09_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,112,113,115,116,117,118,119,122,124,125,127,130,131,132,133,134,136,137,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_409(self.ctx)


class 게임진행1_409(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격10_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,106,107,110,111,112,113,114,115,118,131,134,135,136,137,138,139,142,143,144,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_410(self.ctx)


class 게임진행1_410(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격11_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,112,113,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_411(self.ctx)


class 게임진행1_411(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격12_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,107,108,113,114,115,116,119,120,125,126,127,128,131,132,138,140,142,146,147,148,149,151,153,155,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_412(self.ctx)


class 게임진행1_412(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격13_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_413(self.ctx)


class 게임진행1_413(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격14_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,106,108,109,111,114,116,117,119,120,121,122,124,125,127,128,129,130,132,133,135,138,139,142,143,145,146,148,150,153,154,157,159,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_414(self.ctx)


class 게임진행1_414(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격15_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,105,106,109,110,111,112,115,116,117,118,119,120,123,124,125,126,127,128,131,132,133,134,137,138,140,141,143,144,145,148,149,151,153,154,156,157,158,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_415(self.ctx)


class 게임진행1_415(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격16_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_416(self.ctx)


class 게임진행1_416(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격17_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,119,120,121,122,125,126,127,128,129,130,131,132,135,136,138,139,140,142,143,146,147,148,149,151,152,153,155,156,157,158,159,160,161,162], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_417(self.ctx)


class 게임진행1_417(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격18_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,104,105,106,107,109,110,111,113,114,116,117,118,119,121,122,123,125,126,128,129,130,131,133,134,135,138,140,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_418(self.ctx)


class 게임진행1_418(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격19_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,138,139,142,143,144,145,146,147,148,150,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_419(self.ctx)


class 게임진행1_419(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격20_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,105,106,107,108,109,110,111,112,115,116,117,118,119,121,122,123,124,125,126,127,129,130,131,132,133,134,137,138,140,141,143,144,145,146,147,148,149,150,151,153,154,156,157,158,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_420(self.ctx)


class 게임진행1_420(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격21_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,111,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_421(self.ctx)


class 게임진행1_421(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격22_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,120,121,122,123,125,126,127,128,129,130,131,132,134,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156,157,158,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_422(self.ctx)


class 게임진행1_422(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격23_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_423(self.ctx)


class 게임진행1_423(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격24_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_424(self.ctx)


class 게임진행1_424(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격25_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_425(self.ctx)


class 게임진행1_425(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격26_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,120,122,124,125,127,129,130,132,133,135,136,137,138,139,142,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_426(self.ctx)


class 게임진행1_426(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격27_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,110,111,112,113,114,116,117,120,121,122,123,124,125,126,127,130,132,133,134,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_427(self.ctx)


class 게임진행1_427(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격28_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,110,111,112,113,116,118,119,120,122,123,126,127,129,130,131,133,136,137,139,140,142,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_428(self.ctx)


class 게임진행1_428(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격29_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,109,110,112,113,115,117,118,119,120,122,124,125,127,129,130,131,132,134,136,137,138,143,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_429(self.ctx)


class 게임진행1_429(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격30_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,112,113,114,115,116,117,119,121,122,123,124,125,126,127,129,130,131,132,133,135,136,137,139,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_430(self.ctx)


class 게임진행1_430(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격31_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,113,115,116,117,118,119,120,121,123,124,125,126,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_431(self.ctx)


class 게임진행1_431(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격32_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,131,132,133,134,135,136,137,138,140,141,143,144,145,146,147,148,149,150,152,153,154,155,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_432(self.ctx)


class 게임진행1_432(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격33_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,105,106,107,108,109,111,112,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,156,157,158,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_433(self.ctx)


class 게임진행1_433(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격34_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,110,111,112,113,114,116,118,119,121,122,123,124,125,126,127,128,130,131,133,134,135,136,137,138,139,140,141,142,143,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_434(self.ctx)


class 게임진행1_434(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격35_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,122,123,126,127,128,129,130,131,132,133,134,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_435(self.ctx)


class 게임진행1_435(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격36_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,158,159,160,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_436(self.ctx)


class 게임진행1_436(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격37_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_437(self.ctx)


class 게임진행1_437(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격38_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_438(self.ctx)


class 게임진행1_438(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격39_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,133,135,136,137,138,139,140,141,142,144,145,146,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_439(self.ctx)


class 게임진행1_439(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


class 스프링공격40_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[102,103,104,105,106,107,108,109,110,112,113,114,116,117,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_440(self.ctx)


class 게임진행1_440(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지04(self.ctx)


# 패턴 목록_라운드5
class 스프링공격01_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[105,106,107,108,117,118,119,120,129,130,131,132,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_501(self.ctx)


class 게임진행1_501(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격02_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,137,138,139,140,150,151,152,153], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_502(self.ctx)


class 게임진행1_502(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격03_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,109,110,111,112,113,114,115,116,121,122,123,124,129,130,131,132,141,142,143,144,145,154,155,156,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_503(self.ctx)


class 게임진행1_503(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격04_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[107,117,118,119,120,121,127,128,129,133,134,135,137,138,139,147,148,149,150,151,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_504(self.ctx)


class 게임진행1_504(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격05_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[104,105,108,109,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,140,141,145,146,153,154,160,161], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_505(self.ctx)


class 게임진행1_505(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격06_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,108,109,110,111,112,113,114,115,116,117,120,121,128,129,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_506(self.ctx)


class 게임진행1_506(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격07_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,111,112,115,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,137,138,143,148,149,150,151,156,157,158,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_507(self.ctx)


class 게임진행1_507(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격08_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[107,108,109,110,111,112,113,114,115,116,117,118,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,151,152,155,156], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_508(self.ctx)


class 게임진행1_508(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격09_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,112,113,115,116,117,118,119,122,124,125,127,130,131,132,133,134,136,137,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_509(self.ctx)


class 게임진행1_509(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격10_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,106,107,110,111,112,113,114,115,118,131,134,135,136,137,138,139,142,143,144,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_510(self.ctx)


class 게임진행1_510(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격11_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,112,113,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_511(self.ctx)


class 게임진행1_511(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격12_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,107,108,113,114,115,116,119,120,125,126,127,128,131,132,138,140,142,146,147,148,149,151,153,155,157,158,159,160], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_512(self.ctx)


class 게임진행1_512(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격13_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_513(self.ctx)


class 게임진행1_513(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격14_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,106,108,109,111,114,116,117,119,120,121,122,124,125,127,128,129,130,132,133,135,138,139,142,143,145,146,148,150,153,154,157,159,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_514(self.ctx)


class 게임진행1_514(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격15_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,105,106,109,110,111,112,115,116,117,118,119,120,123,124,125,126,127,128,131,132,133,134,137,138,140,141,143,144,145,148,149,151,153,154,156,157,158,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_515(self.ctx)


class 게임진행1_515(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격16_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_516(self.ctx)


class 게임진행1_516(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격17_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,119,120,121,122,125,126,127,128,129,130,131,132,135,136,138,139,140,142,143,146,147,148,149,151,152,153,155,156,157,158,159,160,161,162], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_517(self.ctx)


class 게임진행1_517(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격18_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,104,105,106,107,109,110,111,113,114,116,117,118,119,121,122,123,125,126,128,129,130,131,133,134,135,138,140,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_518(self.ctx)


class 게임진행1_518(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격19_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,138,139,142,143,144,145,146,147,148,150,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_519(self.ctx)


class 게임진행1_519(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격20_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,105,106,107,108,109,110,111,112,115,116,117,118,119,121,122,123,124,125,126,127,129,130,131,132,133,134,137,138,140,141,143,144,145,146,147,148,149,150,151,153,154,156,157,158,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_520(self.ctx)


class 게임진행1_520(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격21_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,111,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_521(self.ctx)


class 게임진행1_521(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격22_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,120,121,122,123,125,126,127,128,129,130,131,132,134,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156,157,158,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_522(self.ctx)


class 게임진행1_522(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격23_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_523(self.ctx)


class 게임진행1_523(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격24_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_524(self.ctx)


class 게임진행1_524(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격25_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_525(self.ctx)


class 게임진행1_525(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격26_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,120,122,124,125,127,129,130,132,133,135,136,137,138,139,142,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_526(self.ctx)


class 게임진행1_526(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격27_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,110,111,112,113,114,116,117,120,121,122,123,124,125,126,127,130,132,133,134,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_527(self.ctx)


class 게임진행1_527(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격28_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,108,109,110,111,112,113,116,118,119,120,122,123,126,127,129,130,131,133,136,137,139,140,142,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_528(self.ctx)


class 게임진행1_528(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격29_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,109,110,112,113,115,117,118,119,120,122,124,125,127,129,130,131,132,134,136,137,138,143,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_529(self.ctx)


class 게임진행1_529(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격30_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,112,113,114,115,116,117,119,121,122,123,124,125,126,127,129,130,131,132,133,135,136,137,139,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_530(self.ctx)


class 게임진행1_530(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격31_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,113,115,116,117,118,119,120,121,123,124,125,126,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_531(self.ctx)


class 게임진행1_531(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격32_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,131,132,133,134,135,136,137,138,140,141,143,144,145,146,147,148,149,150,152,153,154,155,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_532(self.ctx)


class 게임진행1_532(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격33_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,105,106,107,108,109,111,112,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,156,157,158,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_533(self.ctx)


class 게임진행1_533(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격34_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,110,111,112,113,114,116,118,119,121,122,123,124,125,126,127,128,130,131,133,134,135,136,137,138,139,140,141,142,143,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_534(self.ctx)


class 게임진행1_534(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격35_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,122,123,126,127,128,129,130,131,132,133,134,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_535(self.ctx)


class 게임진행1_535(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격36_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,158,159,160,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_536(self.ctx)


class 게임진행1_536(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격37_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_537(self.ctx)


class 게임진행1_537(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격38_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_538(self.ctx)


class 게임진행1_538(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격39_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,133,135,136,137,138,139,140,141,142,144,145,146,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[201], enable=True)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[211], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[215], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[218], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[220], enable=True)
        self.set_skill(trigger_ids=[221], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[238], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[250], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_539(self.ctx)


class 게임진행1_539(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


class 스프링공격40_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=2) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[102,103,104,105,106,107,108,109,110,112,113,114,116,117,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enable=True) # 움직이는 발판을 이동한다 (arg2=1)
        self.set_skill(trigger_ids=[202], enable=True)
        self.set_skill(trigger_ids=[203], enable=True)
        self.set_skill(trigger_ids=[204], enable=True)
        self.set_skill(trigger_ids=[205], enable=True)
        self.set_skill(trigger_ids=[206], enable=True)
        self.set_skill(trigger_ids=[207], enable=True)
        self.set_skill(trigger_ids=[208], enable=True)
        self.set_skill(trigger_ids=[209], enable=True)
        self.set_skill(trigger_ids=[210], enable=True)
        self.set_skill(trigger_ids=[212], enable=True)
        self.set_skill(trigger_ids=[213], enable=True)
        self.set_skill(trigger_ids=[214], enable=True)
        self.set_skill(trigger_ids=[216], enable=True)
        self.set_skill(trigger_ids=[217], enable=True)
        self.set_skill(trigger_ids=[219], enable=True)
        self.set_skill(trigger_ids=[222], enable=True)
        self.set_skill(trigger_ids=[223], enable=True)
        self.set_skill(trigger_ids=[224], enable=True)
        self.set_skill(trigger_ids=[225], enable=True)
        self.set_skill(trigger_ids=[226], enable=True)
        self.set_skill(trigger_ids=[227], enable=True)
        self.set_skill(trigger_ids=[228], enable=True)
        self.set_skill(trigger_ids=[229], enable=True)
        self.set_skill(trigger_ids=[230], enable=True)
        self.set_skill(trigger_ids=[231], enable=True)
        self.set_skill(trigger_ids=[232], enable=True)
        self.set_skill(trigger_ids=[233], enable=True)
        self.set_skill(trigger_ids=[234], enable=True)
        self.set_skill(trigger_ids=[235], enable=True)
        self.set_skill(trigger_ids=[236], enable=True)
        self.set_skill(trigger_ids=[237], enable=True)
        self.set_skill(trigger_ids=[239], enable=True)
        self.set_skill(trigger_ids=[240], enable=True)
        self.set_skill(trigger_ids=[241], enable=True)
        self.set_skill(trigger_ids=[242], enable=True)
        self.set_skill(trigger_ids=[243], enable=True)
        self.set_skill(trigger_ids=[244], enable=True)
        self.set_skill(trigger_ids=[245], enable=True)
        self.set_skill(trigger_ids=[246], enable=True)
        self.set_skill(trigger_ids=[247], enable=True)
        self.set_skill(trigger_ids=[248], enable=True)
        self.set_skill(trigger_ids=[249], enable=True)
        self.set_skill(trigger_ids=[251], enable=True)
        self.set_skill(trigger_ids=[252], enable=True)
        self.set_skill(trigger_ids=[253], enable=True)
        self.set_skill(trigger_ids=[254], enable=True)
        self.set_skill(trigger_ids=[255], enable=True)
        self.set_skill(trigger_ids=[256], enable=True)
        self.set_skill(trigger_ids=[257], enable=True)
        self.set_skill(trigger_ids=[258], enable=True)
        self.set_skill(trigger_ids=[259], enable=True)
        self.set_skill(trigger_ids=[260], enable=True)
        self.set_skill(trigger_ids=[261], enable=True)
        self.set_skill(trigger_ids=[262], enable=True)
        self.set_skill(trigger_ids=[263], enable=True)
        self.set_skill(trigger_ids=[264], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 게임진행1_540(self.ctx)


class 게임진행1_540(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='98', seconds=1)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616]) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='98'):
            return 공격중지05(self.ctx)


initial_state = 대기
