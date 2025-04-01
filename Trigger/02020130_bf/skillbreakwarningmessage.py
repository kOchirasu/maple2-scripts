""" trigger/02020130_bf/skillbreakwarningmessage.xml """
import trigger_api


# 이슈라 렌듀비앙 유페리아가 죽었을 때 메시지 알림 기능도 있음
class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=601) >= 1:
            # MS2TriggerBox  ID = 601, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면   601은 스타팅 지점과 1셋트 전투판 전체  포함하는 넓은 범위
            return 신호받기대기중(self.ctx)


class 신호받기대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 다음 사용을 위해 꼭 WarningMessage 변수 0으로 초기화 하기, 이 변수는 여기서 초기화 해야지 그렇지 않으면 3번 보내는 신호를 다 받아서 메지시 여러번 뜨게 됨
        self.set_user_value(key='WarningMessage', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WarningMessage') == 1:
            # 이슈라 유페리아 렌듀비앙 3개 중 한곳에서  WarningMessage =  1 신호를 받으면
            return 스킬브레이크메시지출력(self.ctx)
        if self.user_value(key='DeathIshuraRbladerDark') == 1:
            # 이슈라 죽으면 이 변수 1 신호를 받음
            return 이슈라죽음알림(self.ctx)
        if self.user_value(key='DeathRenduebianRbladerDark') == 1:
            # 렌듀비앙 죽으면 이 변수 1 신호를 받음
            return 렌듀비앙죽음알림(self.ctx)
        if self.user_value(key='DeathYuperiaRbladerDark') == 1:
            # 유페리아 죽으면 이 변수 1 신호를 받음
            return 유페리아죽음알림(self.ctx)


class 스킬브레이크메시지출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 스킬브레이크 작동되었음을 이 UI 메시지로 알려주기
        self.show_guide_summary(entity_id=20051001, text_id=20051001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 천천히다시처음으로돌아가기직전(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20051001)


class 이슈라죽음알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20051002, text_id=20051002) # 이슈라의 죽음을 이 UI 메시지로 알려주기
        # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림
        self.set_user_value(key='DeathIshuraRbladerDark', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        # 아슈라 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
        if self.wait_tick(wait_tick=3200):
            return 신호받기대기중(self.ctx)
        if self.user_value(key='DeathRenduebianRbladerDark') == 1:
            # 렌듀비앙 죽으면 이 변수 1 신호를 받음
            return 렌듀비앙죽음알림(self.ctx)
        if self.user_value(key='DeathYuperiaRbladerDark') == 1:
            # 유페리아 죽으면 이 변수 1 신호를 받음
            return 유페리아죽음알림(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20051002)


class 렌듀비앙죽음알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20051003, text_id=20051003) # 렌듀비앙의 죽음을 이 UI 메시지로 알려주기
        # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림
        self.set_user_value(key='DeathRenduebianRbladerDark', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        # 렌듀비앙 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
        if self.wait_tick(wait_tick=3200):
            return 신호받기대기중(self.ctx)
        if self.user_value(key='DeathIshuraRbladerDark') == 1:
            # 이슈라 죽으면 이 변수 1 신호를 받음
            return 이슈라죽음알림(self.ctx)
        if self.user_value(key='DeathYuperiaRbladerDark') == 1:
            # 유페리아 죽으면 이 변수 1 신호를 받음
            return 유페리아죽음알림(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20051003)


class 유페리아죽음알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20051004, text_id=20051004) # 유페리아의 죽음을 이 UI 메시지로 알려주기
        # 변수 0으로 초기화 하기, 이거 안하면 무한루프에 걸림
        self.set_user_value(key='DeathYuperiaRbladerDark', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        # 유페리아 죽음 메시지 출력 도중에 다른 보스가 죽었을 경우에 대한 처리
        if self.wait_tick(wait_tick=3200):
            return 신호받기대기중(self.ctx)
        if self.user_value(key='DeathIshuraRbladerDark') == 1:
            # 이슈라 죽으면 이 변수 1 신호를 받음
            return 이슈라죽음알림(self.ctx)
        if self.user_value(key='DeathRenduebianRbladerDark') == 1:
            # 렌듀비앙 죽으면 이 변수 1 신호를 받음
            return 렌듀비앙죽음알림(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20051004)


class 천천히다시처음으로돌아가기직전(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            # 이 waitTick 너무 길면 보스가 죽을 때 제때 메시지 출력이 안될 수 있어서 적당히 길게 설정해야 함
            return 신호받기대기중(self.ctx) # 다시 위 처음 단계로 돌아가기


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
