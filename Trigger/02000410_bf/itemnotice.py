""" trigger/02000410_bf/itemnotice.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면          750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNotice01') == 1:
            # 인페르녹이 최초 등장하여 광역기폭발 공격할 때 이 신호를 보냄
            return 필수아이템01(self.ctx)


class 필수아이템01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 부활불가 되었고 이제 파티가 전멸되면 게임오버 된다는 내여을 시스템메시지를 통해서 알려줌, 참고로 파티원전멸 체크 트리거는 ClearCheck.xml 이것임
        self.show_guide_summary(entity_id=20041008, text_id=20041008)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 다음대기(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20041008)


class 다음대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNotice02') == 1:
            # 인페르녹이 광역공격 할때 이 신호를 보냄
            return 필수아이템02(self.ctx)


class 필수아이템02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 부활불가 되었고 이제 파티가 전멸되면 게임오버 된다는 내여을 시스템메시지를 통해서 알려줌, 참고로 파티원전멸 체크 트리거는 ClearCheck.xml 이것임
        self.show_guide_summary(entity_id=20041009, text_id=20041009)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20041009)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
