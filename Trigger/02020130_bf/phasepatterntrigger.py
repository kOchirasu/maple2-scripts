""" trigger/02020130_bf/phasepatterntrigger.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # PhaseSumTotal 변수 0으로 초기 세팅
        self.set_user_value(key='PhaseSumTotal', value=0)
        # PhasePatternTrigger 변수 0으로 초기 세팅
        self.set_user_value(key='PhasePatternTrigger', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=601) >= 1:
            # MS2TriggerBox  ID = 601, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면   601은 스타팅 지점과 1셋트 전투판 전체  포함하는 넓은 범위
            return 보스3마리_페이즈전환계산(self.ctx)


class 보스3마리_페이즈전환계산(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PhaseSumTotal') >= 3:
            # PhaseSumTotal 이 변수가 3마리 보스의 AI에서 신호를 받아서 1씩 더해지는데, 일정 이상의 숫자가 되면 각 3마리 보스에게 신호 보내 동시에 페이즈가 변화되도록 설정함
            return 보스3마리_페이즈전환실행_2페이즈(self.ctx)


class 보스3마리_페이즈전환실행_2페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # PhasePatternTrigger = 2 신호를 보스 3마리한테 보내서 2페이즈로 전환하도록 함
        self.set_ai_extra_data(key='PhasePatternTrigger', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PhaseSumTotal') >= 9:
            # PhaseSumTotal 이 변수가 3마리 보스의 AI에서 신호를 받아서 1씩 더해지는데, 일정 이상의 숫자가 되면 각 3마리 보스에게 신호 보내 동시에 페이즈가 변화되도록 설정함
            return 보스3마리_페이즈전환실행_3페이즈(self.ctx)


class 보스3마리_페이즈전환실행_3페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # PhasePatternTrigger = 3 신호를 보스 3마리한테 보내서 3페이즈로 전환하도록 함
        self.set_ai_extra_data(key='PhasePatternTrigger', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PhaseSumTotal') >= 15:
            # PhaseSumTotal 이 변수가 3마리 보스의 AI에서 신호를 받아서 1씩 더해지는데, 일정 이상의 숫자가 되면 각 3마리 보스에게 신호 보내 동시에 페이즈가 변화되도록 설정함
            return 보스3마리_페이즈전환실행_4페이즈(self.ctx)


class 보스3마리_페이즈전환실행_4페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # PhasePatternTrigger = 4 신호를 보스 3마리한테 보내서 4페이즈로 전환하도록 함
        self.set_ai_extra_data(key='PhasePatternTrigger', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PhaseSumTotal') >= 18:
            # PhaseSumTotal 이 변수가 3마리 보스의 AI에서 신호를 받아서 1씩 더해지는데, 일정 이상의 숫자가 되면 각 3마리 보스에게 신호 보내 동시에 페이즈가 변화되도록 설정함
            return 보스3마리_페이즈전환실행_5페이즈(self.ctx)


class 보스3마리_페이즈전환실행_5페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # PhasePatternTrigger = 5 신호를 보스 3마리한테 보내서 5페이즈로 전환하도록 함
        self.set_ai_extra_data(key='PhasePatternTrigger', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
