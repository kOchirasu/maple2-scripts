""" trigger/02000427_bf/right202.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[202]):
            # 플레이어가 오른쪽지점 태엽폭탄 있는 곳에 들어서면
            return 오른쪽지점견제(self.ctx)


class 오른쪽지점견제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.show_guide_summary(entity_id=20041008, text_id=20041008)
        # 플레이어가 오른쪽지점 태엽폭탄 있는 곳에 들어서면, 파풀라투스가 사용하는 이 변수를 1로 만들어서 파풀라투스가 오른쪽 태엽폭탄 지점 플레이어 견제하도록 함
        self.set_ai_extra_data(key='RightPositionCheck', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[202]):
            # 플레이어가 오른쪽지점 태엽폭탄 있는 곳에 벗어나면
            return 오른쪽지점견제풀기(self.ctx)


class 오른쪽지점견제풀기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.show_guide_summary(entity_id=20000664, text_id=20000664)
        # 플레이어가 오른쪽지점 태엽폭탄 있는 곳에 벗어나면 , 파풀라투스가 사용하는 이 변수를 0로 만들어 초기화 하기
        self.set_ai_extra_data(key='RightPositionCheck', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 시작(self.ctx)


initial_state = 시작
