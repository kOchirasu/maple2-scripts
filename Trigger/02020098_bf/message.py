""" trigger/02020098_bf/message.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[11]):
            # MS2TriggerBox   TriggerObjectID = 11, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        11은 1페이지 보스 전투판으로 가는 계단 영역에 설치된 영역임
            return 크리스탈활용안내메시지출력(self.ctx)


class 크리스탈활용안내메시지출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 안내 메시지 호출하기   stringGuide.xlsx
        self.show_guide_summary(entity_id=29200002, text_id=29200002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6300):
            return 트리거종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=29200002)


class 트리거종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
