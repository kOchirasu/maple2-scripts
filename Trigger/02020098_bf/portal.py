""" trigger/02020098_bf/portal.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 졸구간 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portal_id=2)
        # 1페이지 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portal_id=3)
        # 2페이지 7시 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portal_id=4)
        # 2페이지 5시 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portal_id=5)
        # 2페이지 12시 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portal_id=6)
        # 3페이지 마지막 전투판에 있는 던전 나가기 포탈 최초에 감추기
        self.set_portal(portal_id=7)
        # 변수 초기화, 보스AI로 부터 이 변수 1 신호를 받으면 이 트리거 작동시켜 1페이지 순간이동 포탈 Off 상태로 만들기
        self.set_user_value(key='BossOnePhaseEnd', value=0)
        # 1페이지의 왼쪽 순간이동 포탈 최초에 On 설정 하기
        self.set_portal(portal_id=40, visible=True, enable=True, minimap_visible=True)
        # 1페이지의 오른쪽 순간이동 포탈 최초에 On 설정 하기
        self.set_portal(portal_id=50, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10]):
            # MS2TriggerBox   TriggerObjectID = 10, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        10은 스타팅 포인트 지점만 커버하는 비교적 좁은 범위
            return 포탈체크시작(self.ctx)


class 포탈체크시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 포탈체크대기중(self.ctx)


class 포탈체크대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        # 인페르녹 보스가 죽으면 BossDead =  1, 신호를 보내서 전투 끝났음을 알림
        if self.user_value(key='BossOnePhaseEnd') == 1:
            return 순간이동포탈OFF(self.ctx)
        """
        중요: 보스 죽음 체크를 <condition name="몬스터가죽어있으면" arg1="98">   <condition name="몬스터가죽어있으면" arg1="99"> 방식을 사용하지 않는 이유는 
                이 맵은 한맵에 2개 난이도가 존재하는데, 만약 스폰포인트 99로 보스가 등장할 하여 트리거가 이 단계에 오면 98 스폰 포인트의 보스가 죽은 것으로 처리해 버리기 때문에 
                 보스AI에서 죽을때 변수 신호 보내는 방식을 사용하였음
        """
        if self.user_value(key='BossDead') == 1:
            return 나가기포탈생성잠시대기(self.ctx)


class 순간이동포탈OFF(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1페이지의 왼쪽 순간이동 포탈 Off 설정 하기
        self.set_portal(portal_id=40)
        # 1페이지의 오른쪽 순간이동 포탈 Off 설정 하기
        self.set_portal(portal_id=50)
        self.set_user_value(key='BossOnePhaseEnd', value=0) # 변수 초기화, 이거 안하면 무한루프에 빠짐

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 포탈체크대기중(self.ctx) # 다시 이전 단계로 돌아가기


class 나가기포탈생성잠시대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9500):
            # 던전 클리어 연출 뜨기 전에 나가기 포탈로 나가면 혹시 모를 버그가 나올 수 있어서 10여초 정도 잠시 딜레이 함
            return 나가기포탈생성(self.ctx)


class 나가기포탈생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PhasePortar') == 0:
            # 보스가 졸 구간에서 죽은 경우
            return 졸구간만포탈생성(self.ctx)
        if self.user_value(key='PhasePortar') == 1:
            # 보스가 1페이지 전투판에서 죽은 경우
            return 페이지전투판포탈생성1(self.ctx)
        if self.user_value(key='PhasePortar') == 2:
            # 보스가 2페이지 전투판에서 죽은 경우
            return 페이지전투판포탈생성2(self.ctx)
        if self.user_value(key='PhasePortar') == 3:
            # 보스가 3페이지 전투판에서 죽은 경우
            return 페이지전투판포탈생성3(self.ctx)


class 졸구간만포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스 죽이면 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트리거종료(self.ctx)


class 페이지전투판포탈생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스 죽이면 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 1페이지 전투판에서 나가기 포탈
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트리거종료(self.ctx)


class 페이지전투판포탈생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스 죽이면 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 2페이지 7시 전투판에서 나가기 포탈
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 2페이지 5시 전투판에서 나가기 포탈
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 2페이지 12시 전투판에서 나가기 포탈
        self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트리거종료(self.ctx)


class 페이지전투판포탈생성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스 죽이면 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 마지막 전투판에서 나가기 포탈
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트리거종료(self.ctx)


class 트리거종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
