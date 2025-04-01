""" trigger/02000426_bf/999991_zakumarmsudden.xml """
import trigger_api


# MS2TriggerModel ID : 999991, 자쿰 몸통과 싸울 때 자쿰팔이 소환되면, 자쿰 몸체에 무적 버프 걸거, 자쿰팔 다 제거되면 자쿰몸 무적버프 지우는 기능의 트리거임
class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 변수 0 초기화, 이 변수는 자쿰 몸통AI에서 자쿰손 소환할 때 이 변수 1로 만드는 신호를 보내서, 자쿰 손 마리수 체크 작업 시작하도록 함
        self.set_user_value(key='SummonZakumArmRegenCheck', value=0)
        # 변수 0 초기화, 이 변수 신호는 자쿰 몸통하고 싸울때 등장하는 소환몹 자쿰팔AI에서 보냄
        self.set_user_value(key='SummonZakumArmMany', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 대기중(self.ctx)


class 대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SummonZakumArmRegenCheck') == 1:
            # 자쿰몸통 AI에서 이 변수 1 신호를 보내서 자쿰팔 소환을 소환하는데, 트리거는 이 변수 1 신호를 받게 되어서 자쿰팔 등장 유무를 알수있게 되는 것임
            return 자쿰몸통무적버프로직_시작대기중(self.ctx)


class 자쿰몸통무적버프로직_시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 중요!: 자쿰팔 리젠 동작 끝날때 쯤 버프 걸도록 설정함, 자쿰팔 리젠 애니 길이는 약 3.74초 임 이 시간보다 넉넉히 길게 설정함
            return 자쿰몸통무적버프로직_작동(self.ctx)


class 자쿰몸통무적버프로직_작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 자쿰 몸통에 일단 무적 버프 부여함
        # 어려운 난이도 일반 난이도 어떤 곳에서 실행되는지 알지 못하니 2개 다 부여함 , 무적 애디셔널 50000265(레벨1)
        # 어려움 난이도 자쿰몸 스폰 ID가  arg1 = 2011    arg3="1" 은 애디셔널의 레벨, arg4="1" 은 대상이 몬스터라는 뜻 참고로 arg4="0"은 플레이어
        self.add_buff(box_ids=[2011], skill_id=50000265, level=1, is_skill_set=False)
        # 일반  난이도 자쿰몸 스폰 ID가  arg1 = 2012
        self.add_buff(box_ids=[2012], skill_id=50000265, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SummonZakumArmMany') == 0:
            # 모든 자쿰팔 제거 되어서 이 변수 0이 되면, 버프 제거함
            return 자쿰몸통무적버프_제거대기(self.ctx)


class 자쿰몸통무적버프_제거대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 마지막 자쿰팔 죽이면 1초 뒤에 버프 사라지도록 함
            return 자쿰몸통무적버프_제거작업(self.ctx)


class 자쿰몸통무적버프_제거작업(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 어려운 난이도 일반 난이도 어떤 곳에서 실행되는지 알지 못하니 2개 다 제거함, 몬스터의 애디셔널을 트리거로 제거할 때는  NpcRemoveAdditionalEffect 사용해야 함 , 무적 애디셔널 50000265(레벨1)
        # 어려움 난이도 자쿰몸 스폰 ID가  2011
        self.npc_remove_additional_effect(spawn_id=2011, additional_effect_id=50000265)
        # 일반  난이도 자쿰몸 스폰 ID가  2012
        self.npc_remove_additional_effect(spawn_id=2012, additional_effect_id=50000265)
        # 자쿰팔 제거되고 무적버프 제거되었으면 이 변수 0 초기화 시켜 "대기중" 상태가 되도록 함
        self.set_user_value(key='SummonZakumArmRegenCheck', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return 대기중(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
