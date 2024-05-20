""" trigger/02000429_bf/dropdebuff.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면,          750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 드랍어뷰징디버프_작동시작(self.ctx)


class 드랍어뷰징디버프_작동시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=780) >= 1:
            # MS2TriggerBox   TriggerObjectID = 780, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면,     780은 전투판에서의 추락 지점을 체크하기 위한 트리거 영역 범위임
            return 전투판에떨어지면디버프걸기(self.ctx)


class 전투판에떨어지면디버프걸기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MS2TriggerBox   TriggerObjectID = 780, 이 트리거 박스 안에 있는 플레이어 Sp 0 상태이상 걸리게 하기
        self.add_buff(box_ids=[780], skill_id=50000512, level=1, is_player=False, is_skill_set=False)
        # 50000512 레벨1 이 SP 0 10초 동안 상태이상

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 드랍어뷰징디버프_작동시작(self.ctx)


initial_state = Ready
