""" trigger/02020141_bf/playerdropheal.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 트리거시작(self.ctx)


class 트리거시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            # MS2TriggerBox   TriggerObjectID = 102, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        102는 공중에 떠있는 스타팅 포인트 지점 , 이전 첫번째 두번째 페이즈 맵을 통해서 정상 트리거를 타고 이 맵으로 오면 이 공중 떠있는 스타팅 포인트로 오게 될 것임
            return 드랍지점회복(self.ctx)


class 드랍지점회복(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MS2TriggerBox   TriggerObjectID = 102, 이 트리거 박스 안의 플레이어에게 애디셔널 50000554(레벨1) 회복 버프 부여하기, 이 맵은 추락하면서 시작하는데 추락 대미지에 의해 죽을 수있기 때문에 시작하자마자 무조건 HP회복 버프 부여함
        self.add_buff(box_ids=[102], skill_id=50000554, level=1, is_player=False, is_skill_set=False)
        # arg4 =1 이면 타겟이 npc로 변경 / arg1이 스폰 포인트 ID가 된다.       arg5 =1 이면 박스 외에 모든 맵/ 0은 박스 안

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 다시 처음 단계로 돌아가기
            return 트리거시작(self.ctx)


initial_state = 시작대기중
