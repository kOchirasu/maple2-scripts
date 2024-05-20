""" trigger/02020098_bf/barricade.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 스타트포인트 지점의 칸막이 트리거메쉬 최초에는 감추기
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10]):
            # MS2TriggerBox   TriggerObjectID = 10, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        10은 스타팅 포인트 지점만 커버하는 비교적 좁은 범위
            return 칸막이대기시작(self.ctx)


class 칸막이대기시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 칸막이대기알림(self.ctx)


class 칸막이대기알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020098_BF__BARRICADE__0$', arg3='3000')
        self.dungeon_enable_give_up(is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=22000):
            return 칸막이막기(self.ctx)


class 칸막이막기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311], visible=True, start_delay=1, interval=120, fade=0.5) # 시작지점의 칸막이 막기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트리거종료(self.ctx)


class 트리거종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
