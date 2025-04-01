""" trigger/02020130_bf/debuff_ishurarenduebianyuperia.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 주요 3개 변수 0으로 초기화
        self.set_user_value(key='IshuraFirstSetEnd', value=0)
        self.set_user_value(key='RenduebianFirstSetEnd', value=0)
        self.set_user_value(key='YuperiaFirstSetEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=601) >= 1:
            # MS2TriggerBox  ID = 601, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면   601은 스타팅 지점과 1셋트 전투판 전체  포함하는 넓은 범위
            return 셋트전투판스킬트리거셋팅1(self.ctx)


class 셋트전투판스킬트리거셋팅1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이슈라 전투판 디버프 스킬 On으로 초기 셋팅하기
        self.set_skill(trigger_ids=[1301], enable=True)
        # 렌듀비앙 전투판 디버프 스킬 On으로 초기 셋팅하기
        self.set_skill(trigger_ids=[1302], enable=True)
        # 유페리아 전투판 디버프 스킬 On으로 초기 셋팅하기
        self.set_skill(trigger_ids=[1303], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=310):
            return 셋트전투판마무리신호대기1(self.ctx)


class 셋트전투판마무리신호대기1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        # 레듀비앙 보스 AI에게 변수 신호 받을때까지 대기하기
        if self.user_value(key='IshuraFirstSetEnd') == 1:
            # 이슈라가 첫번째 전투판에서 전투 끝나면 IshuraFirstSetEnd = 1  신호 보냄
            return 이슈라_디버프스킬끄기(self.ctx)
        # 유페리아 보스 AI에게 변수 신호 받을때까지 대기하기
        if self.user_value(key='RenduebianFirstSetEnd') == 1:
            # 레듀비앙이 첫번째 전투판에서 전투 끝나면 RenduebianFirstSetEnd = 1  신호 보냄
            return 렌듀비앙_디버프스킬끄기(self.ctx)
        if self.user_value(key='YuperiaFirstSetEnd') == 1:
            # 유페리아가 첫번째 전투판에서 전투 끝나면 YuperiaFirstSetEnd = 1  신호 보냄
            return 유페리아_디버프스킬끄기(self.ctx)


class 이슈라_디버프스킬끄기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # IshuraFirstSetEnd 변수 0으로 초기화
        self.set_user_value(key='IshuraFirstSetEnd', value=0)
        self.set_skill(trigger_ids=[1301]) # 이슈라 전투판 디버프 스킬 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=370):
            return 셋트전투판마무리신호대기1(self.ctx)


class 렌듀비앙_디버프스킬끄기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # RenduebianFirstSetEnd 변수 0으로 초기화
        self.set_user_value(key='RenduebianFirstSetEnd', value=0)
        self.set_skill(trigger_ids=[1302]) # 렌듀비앙 전투판 디버프 스킬 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=370):
            return 셋트전투판마무리신호대기1(self.ctx)


class 유페리아_디버프스킬끄기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # YuperiaFirstSetEnd 변수 0으로 초기화
        self.set_user_value(key='YuperiaFirstSetEnd', value=0)
        self.set_skill(trigger_ids=[1303]) # 유페리아 전투판 디버프 스킬 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=370):
            return 셋트전투판마무리신호대기1(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
