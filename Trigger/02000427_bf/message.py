""" trigger/02000427_bf/message.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Message') == 1:
            # 파풀라투스 AI에서 Message = 1 신호를 받으면 진행함
            return 메시지출력01(self.ctx)


class 메시지출력01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # "파풀라투스의 보호막은 태엽 폭탄을 던져 제거해야 합니다." 메시지 출력
        self.show_guide_summary(entity_id=20042001, text_id=20042001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 메시지출력02대기(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20042001)


class 메시지출력02대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Message') == 2:
            # 파풀라투스 AI에서 Message = 2 신호를 받으면 진행함
            return 메시지출력02(self.ctx)


class 메시지출력02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # "연산 큐브를 밟아서 보호막 유지 시간을 조절해야 합니다." 메시지 출력
        self.show_guide_summary(entity_id=20042002, text_id=20042002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 메시지출력03대기(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20042002)


class 메시지출력03대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Message') == 3:
            # 파풀라투스 AI에서 Message = 3 신호를 받으면 진행함
            return 메시지출력03(self.ctx)


class 메시지출력03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # "떨어지는 물체로 바닥 유리를 파괴하여 태엽 폭탄을 꺼내야 합니다."  메시지 출력
        self.show_guide_summary(entity_id=20042003, text_id=20042003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20042003)


class 종료(trigger_api.Trigger):
    pass


initial_state = 전투시작
