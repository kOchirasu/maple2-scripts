""" trigger/02000429_bf/startportalremove.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면,          750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 시작지점포탈_우선생성(self.ctx)


class 시작지점포탈_우선생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 최초 스타팅 포인트 지점에 배치된 메인 전투판으로 들어서기 위한 포탈 최초에 활성화 시키기,   arg1="3" 은 포탈ID
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        # 툴벤치 포탈 기능의 버그때문에 이렇게 설정하였는데, 툴벤치 포탈 설정이 IsVisible=Ture 인 상태에서 트리거로 트리거 기능을 제거해도 포탈 모양의 이펙트는 남아있는 버그가 있기 때문에, 최초에는 포탈을  IsVisible=False로 해놓고 트리거로 활성화 상태로 해놓고 이후 비활성화 상태로 해야 버그가 발생 안함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=40000):
            # 던전 최초 진임 후 40초 지나면 메인 전투판 진입 포탈 제거직전 단계로 넘어가기, 던전 입장하면 거의 30초 넘도록 각종 팝업창 일러스트 이벤트가 뜨기 때문에 40초가 적당함
            return 시작지점포탈제거_직전(self.ctx)


class 시작지점포탈제거_직전(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=770) >= 1:
            # MS2TriggerBox   TriggerObjectID = 770, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면,          770은 최초 스타팅 지점만 포함하는 아주 작은 범위
            # 던전 입장 후 30초 지났는데도, 계속 스타팅 지점에 있으면 진입포탈 제거 알림 경고 메시지 보여주기
            return 시작지점포탈_제거알림메시지생성(self.ctx)
        if self.wait_tick(wait_tick=10000):
            # 10초 지나면 메인 전투판 진입 포탈 제거하기
            return 시작지점포탈제거_실행(self.ctx)


class 시작지점포탈_제거알림메시지생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000428_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            # 경고 메시지 출력 후 10초 지나면 메인 전투판 진입 포탈 제거하기
            return 시작지점포탈제거_실행(self.ctx)


class 시작지점포탈제거_실행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 최초 스타팅 포인트 지점에 배치된 메인 전투판으로 들어서기 위한 포탈을 비활성화 상태로 만들기,   arg1="3" 은 포탈ID
        self.set_portal(portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
