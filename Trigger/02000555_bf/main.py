""" trigger/02000555_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


# 플레이어 감지
class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8100,8101,8102,8103,8104])
        self.set_effect(trigger_ids=[8200,8201,8202,8203])
        self.set_effect(trigger_ids=[8300,8301,8302,8303,8304])
        self.set_effect(trigger_ids=[8400,8401,8402,8403,8404,8405,8406,8407,8408,8409,8410,8411,8412,8413,8414,8415,8416,8417,8418,8419,8420,8421,8422,8423,8424,8425,8426])
        self.set_effect(trigger_ids=[8500,8501,8502,8503,8504,8505,8506,8507,8508,8509,8510,8511,8512,8513,8514,8515,8516,8517])
        self.set_effect(trigger_ids=[8600,8601,8602])
        self.set_effect(trigger_ids=[8801]) # 1스테이지 유리문 파괴 효과음 초기화
        self.set_effect(trigger_ids=[8802]) # 2스테이지 유리문 파괴 효과음 초기화
        self.set_effect(trigger_ids=[8803]) # 3스테이지 유리문 파괴 효과음 초기화
        self.set_effect(trigger_ids=[8804]) # 4스테이지 유리문 파괴 효과음 초기화
        self.set_effect(trigger_ids=[8805]) # 5스테이지 철문 Open 효과음 초기화
        self.set_portal(portal_id=2) # 최종 보스방으로 가기 포탈 최초에는 끄기
        # 4스테이지의 벽쪽 구멍 몬스터 등장하는 지점 투명벽으로 막기
        self.set_mesh(trigger_ids=[4012,4013], visible=True)
        # 마지막 보스 방으로 가기 위한 입구, 문짝과 투명벽 트리거 막기
        self.set_mesh(trigger_ids=[4014,4015], visible=True)
        # 각 스테이지 진입을 막는 유리문 뒤에 설치된 투명벽, 플레이어만 막음
        self.set_mesh(trigger_ids=[4001,4002,4003,4004], visible=True)
        # 최종 보스방으로 가기 위한 번호 누르기용 오브젝트 초기화 하기
        self.set_interact_object(trigger_ids=[10003145], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return 스테이지1_시작(self.ctx)


class 스테이지1_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함, 몬스터 등장 이전에 이 변수 0 초기화 하기
        self.set_user_value(key='MonsterMany', value=0)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2900):
            # 몬스터가 등장해서 AI 로직 타서 MonsterMany 변수가 1 이상 된 상태로 다음 단계로 넘어가야 하기 때문에, AI 로직 탈때까지 WaitTick 2~3초 머둘도록 함
            return 스테이지1_추가등장대기01(self.ctx)


class 스테이지1_추가등장대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__37$', duration=5000) # 시작안내문

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') <= 6:
            return 스테이지1_추가등장01(self.ctx)


class 스테이지1_추가등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2837):
            # 몬스터가 등장해서 AI 로직 타서 MonsterMany 변수가 1 이상 된 상태로 다음 단계로 넘어가야 하기 때문에, AI 로직 탈때까지 WaitTick 2~3초 머둘도록 함
            return 스테이지1_대기01(self.ctx)


class 스테이지1_대기01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') <= 6:
            return 스테이지1_추가등장02(self.ctx)


class 스테이지1_추가등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2837):
            # 몬스터가 등장해서 AI 로직 타서 MonsterMany 변수가 1 이상 된 상태로 다음 단계로 넘어가야 하기 때문에, AI 로직 탈때까지 WaitTick 2~3초 머둘도록 함
            return 스테이지1_대기02(self.ctx)


class 스테이지1_대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') <= 6:
            return 스테이지1_추가등장03(self.ctx)


class 스테이지1_추가등장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1401,1402,1403,1404,1405,1406,1407,1408,1409,1410])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3549):
            # 몬스터가 등장해서 AI 로직 타서 MonsterMany 변수가 1 이상 된 상태로 다음 단계로 넘어가야 하기 때문에, AI 로직 탈때까지 WaitTick 3~4초 머물도록 함
            return 스테이지1_대기03(self.ctx)


class 스테이지1_대기03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') == 0:
            # 1스테이지의 몹 다 죽이면 이 변수 0이됨
            return 스테이지1문파괴대기_스테이지2몬스터등장(self.ctx)


class 스테이지1문파괴대기_스테이지2몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함, 몬스터 등장 이전에 이 변수 0 초기화 하기
        self.set_user_value(key='MonsterMany', value=0)
        self.spawn_monster(spawn_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1750):
            # 몬스터 다 죽이면 1~2초 후에 문 파괴되기
            return 스테이지1_완료(self.ctx)


class 스테이지1_완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1스테이지 완료용 스킬 작동해서 막힌 유리문 파괴하기
        self.set_skill(trigger_ids=[61], enable=True)
        self.set_effect(trigger_ids=[8801], visible=True) # 1스테이지 유리문 파괴 효과음 출력
        # 1 스테이지 진입을 막는 유리문 뒤에 설치된 투명벽 제거
        self.set_mesh(trigger_ids=[4001])
        self.set_effect(trigger_ids=[8100,8101,8102,8103,8104], visible=True) # 진행방향 화살표 표시

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 스테이지2_시작(self.ctx)


class 스테이지2_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[61]) # 스킬 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            # 몬스터가 등장해서 AI 로직 타서 MonsterMany 변수가 1 이상 된 상태로 다음 단계로 넘어가야 하기 때문에, AI 로직 탈때까지 WaitTick 2~3초 머둘도록 함
            return 스테이지2_대기01(self.ctx)


class 스테이지2_대기01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') <= 4:
            return 스테이지2_추가등장01(self.ctx)


class 스테이지2_추가등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220,2221])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3549):
            # 몬스터가 등장해서 AI 로직 타서 MonsterMany 변수가 1 이상 된 상태로 다음 단계로 넘어가야 하기 때문에, AI 로직 탈때까지 WaitTick 3~4초 머물도록 함
            return 스테이지2_대기02(self.ctx)


class 스테이지2_대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') == 0:
            # 2스테이지의 몹 다 죽이면 이 변수 0이됨
            return 스테이지2문파괴대기_스테이지3몬스터등장(self.ctx)


class 스테이지2문파괴대기_스테이지3몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함, 몬스터 등장 이전에 이 변수 0 초기화 하기
        self.set_user_value(key='MonsterMany', value=0)
        self.spawn_monster(spawn_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1750):
            # 몬스터 다 죽이면 1~2초 후에 문 파괴되기
            return 스테이지2_완료(self.ctx)


class 스테이지2_완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 2스테이지 완료용 스킬 작동해서 막힌 유리문 파괴하기
        self.set_skill(trigger_ids=[62], enable=True)
        self.set_effect(trigger_ids=[8802], visible=True) # 2스테이지 유리문 파괴 효과음 출력
        # 2스테이지 진입을 막는 유리문 뒤에 설치된 투명벽 제거
        self.set_mesh(trigger_ids=[4002])
        self.set_effect(trigger_ids=[8200,8201,8202,8203], visible=True) # 진입 방향 화살표 표시

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 스테이지3_시작(self.ctx)


class 스테이지3_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[62]) # 스킬 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2853):
            # 몬스터가 등장해서 AI 로직 타서 MonsterMany 변수가 1 이상 된 상태로 다음 단계로 넘어가야 하기 때문에, AI 로직 탈때까지 WaitTick 2~3초 머둘도록 함
            return 스테이지3_진행중(self.ctx)


class 스테이지3_진행중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') == 0:
            # 3스테이지의 몹 다 죽이면 이 변수 0이됨
            return 스테이지3문파괴대기_스테이지4몬스터등장(self.ctx)


class 스테이지3문파괴대기_스테이지4몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함, 몬스터 등장 이전에 이 변수 0 초기화 하기
        self.set_user_value(key='MonsterMany', value=0)
        # 그외 나머지 몬스터는 AI_SignalSummon.xml 에서 소환함
        self.spawn_monster(spawn_ids=[4001])
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__36$', duration=5000) # 앞으로더가세요 안내문

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2470):
            # 몬스터 다 죽이면 2~3초 후에 문 파괴되기, 몬스터가 등장해서 시호 주고 받을 때까지 충분한 시간이 필요하기 때문에  waitTick 시간 2~3초 부여
            return 스테이지3_완료(self.ctx)


class 스테이지3_완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 3스테이지 완료용 스킬 작동해서 막힌 유리문 파괴하기
        self.set_skill(trigger_ids=[63], enable=True)
        self.set_effect(trigger_ids=[8803], visible=True) # 3스테이지 유리문 파괴 효과음 출력
        # 3스테이지 진입을 막는 유리문 뒤에 설치된 투명벽 제거
        self.set_mesh(trigger_ids=[4003])
        self.set_effect(trigger_ids=[8300,8301,8302,8303,8304], visible=True) # 진입 방향 화살표 표시

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 스테이지4_시작(self.ctx)


class 스테이지4_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[63]) # 스킬 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2700):
            # 몬스터가 등장해서 AI 로직 타서 MonsterMany 변수가 1 이상 된 상태로 다음 단계로 넘어가야 하기 때문에, AI 로직 탈때까지 WaitTick 2~3초 머둘도록 함
            return 스테이지4_진행중(self.ctx)


class 스테이지4_진행중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') == 0:
            # 4스테이지의 몹 다 죽이면 이 변수 0이됨
            return 스테이지4문파괴대기_스테이지5몬스터등장(self.ctx)


class 스테이지4문파괴대기_스테이지5몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함, 몬스터 등장 이전에 이 변수 0 초기화 하기
        self.set_user_value(key='MonsterMany', value=0)
        self.spawn_monster(spawn_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1750):
            # 몬스터 다 죽이면 1~2초 후에 문 파괴되기
            return 스테이지4_완료(self.ctx)


class 스테이지4_완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 4스테이지 완료용 스킬 작동해서 막힌 유리문 파괴하기
        self.set_skill(trigger_ids=[64], enable=True)
        self.set_effect(trigger_ids=[8804], visible=True) # 4스테이지 유리문 파괴 효과음 출력
        # 4스테이지 진입을 막는 유리문 뒤에 설치된 투명벽 제거
        self.set_mesh(trigger_ids=[4004])
        self.set_effect(trigger_ids=[8400,8401,8402,8403,8404,8405,8406,8407,8408,8409,8410,8411,8412,8413,8414,8415,8416,8417,8418,8419,8420,8421,8422,8423,8424,8425,8426], visible=True) # 진입 방향 화살표 표시

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 스테이지5_시작(self.ctx)


class 스테이지5_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[64]) # 스킬 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            # 몬스터가 등장해서 AI 로직 타서 MonsterMany 변수가 1 이상 된 상태로 다음 단계로 넘어가야 하기 때문에, AI 로직 탈때까지 WaitTick 2~3초 머둘도록 함
            return 스테이지5_완료대기(self.ctx)


class 스테이지5_완료대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') == 0:
            # 5스테이지의 몹 다 죽이면 이 변수 0이됨
            return 스테이지5_완료(self.ctx)


class 스테이지5_완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8500,8501,8502,8503,8504,8505,8506,8507,8508,8509,8510,8511,8512,8513,8514,8515,8516,8517], visible=True) # 진입 방향 화살표 표시

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 보안게임준비중(self.ctx)


class 보안게임준비중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 금고로 가는 입구를 발견했습니다.\n안으로 들어가 당신의 능력을 증명하세요!
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__38$', duration=5000)
        self.set_interact_object(trigger_ids=[10003145], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003145], state=0):
            return 보안게임시작(self.ctx)


class 보안게임시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='GameLogicEnd', value=999)
        self.widget_action(type='Round', func='InitWidgetRound')
        self.set_user_value(trigger_id=9002, key='GameLogicStart', value=999)
        self.lock_my_pc(is_lock=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 문열기시작2(self.ctx)


class 문열기시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # [보안 시스템 동작]\n관리자 검증 코드를 입력해주세요.\n3번 실패 시, 시스템이 잠깁니다.
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__39$', duration=4000)
        self.lock_my_pc(is_lock=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            # 이 변수가 1이 되면 gameLogic_9002.xml 트리거 작동함
            self.set_user_value(trigger_id=9002, key='GameLogicStart', value=1)
            return 게임로직종료대기(self.ctx)


class 게임로직종료대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GameLogicEnd') == 1:
            return 게임로직종료및성공(self.ctx)
        if self.user_value(key='GameLogicEnd') == 2:
            return 게임로직종료및실패(self.ctx)


class 게임로직종료및성공(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 게임로직종료(self.ctx)


class 게임로직종료및실패(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 실패게임로직종료(self.ctx)


class 게임로직종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=3000.0)
        # 인증이 완료 되었습니다.\n금고 포탈이 활성화됩니다
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__40$', duration=3000)
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이동하자(self.ctx)


class 실패게임로직종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=3000.0)
        # 인증이 실패하였습니다.\n시스템이 잠깁니다.
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__41$', duration=3000)
        self.add_balloon_talk(msg='$02000535_BF__MAIN__42$', duration=3500) # 에잇! 실패하다니…
        self.lock_my_pc()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 문파괴안내(self.ctx)


class 문파괴안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui_script(type=BannerType.Text, script='$02000535_BF__MAIN__43$', duration=7000) # 금고 문을 파괴하여 포탈을 활성화시키세요.
        self.lock_my_pc()
        self.spawn_monster(spawn_ids=[611])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[611]):
            return 이동하자(self.ctx)


class 이동하자(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.lock_my_pc()
        # 뭐야, 금고 문이 열린 거야? 그렇다면… 내가 나설 차례군!
        self.side_npc_talk(npc_id=23300001, illust='Haren_smile', duration=4000, script='$02000535_BF__MAIN__44$')
        # 마지막 보스 방으로 가기 위한 입구, 철문짝과 투명벽 트리거 제거
        self.set_mesh(trigger_ids=[4014,4015])
        self.set_effect(trigger_ids=[8805], visible=True) # 5스테이지 철문Opne 효과음 출력
        self.set_portal(portal_id=2, visible=True) # 보스방 맵으로 가는 포탈 활성화 시키기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 이동하자2(self.ctx)


class 이동하자2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8500,8501,8502,8503,8504,8505,8506,8507,8508,8509,8510,8511,8512,8513,8514,8515,8516,8517]) # 숫자입력용 진입 방향 화살표 표시 끄기
        self.set_effect(trigger_ids=[8600,8601,8602], visible=True) # 보스방 진입 방향 화살표 표시 하기
        # Pc혼잣말 : 금고로 들어가는 입구를 발견했어
        self.add_balloon_talk(msg='$02000535_BF__MAIN__45$', duration=3500)


initial_state = 시작대기중
