""" trigger/02020097_bf/message.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10]):
            # MS2TriggerBox   TriggerObjectID = 10, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        10은 스타팅 포인트 지점만 커버하는 비교적 좁은 범위
            return 대기상태(self.ctx)


class 대기상태(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        # 2페이즈 전투 다 끝나고 , AI_Balrog_Kritias.xml 발록에게   StairsOk2nd = 1 신호를 받으면 이 부분 실행, 2페이즈 건너띄기가 되었기 때문에 경비병 도움 메시지 출력 안함
        if self.user_detected(box_ids=[12]):
            # MS2TriggerBox   TriggerObjectID = 12, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        12은 2페이지 전투판 진입로에 설치된 영역임
            return 경비병도움안내(self.ctx)
        if self.user_value(key='StairsOk2nd') == 1:
            return 트리거종료(self.ctx)


class 경비병도움안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 안내 메시지 호출하기
        self.show_guide_summary(entity_id=29200001, text_id=29200001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 트리거종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=29200001)


class 트리거종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
