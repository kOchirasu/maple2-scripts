""" trigger/02020130_bf/skilldebuff_2phase.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # SkillDebuffCheck_2Phase 변수 0으로 초기 세팅, 보스가 저주디버프스킬 사용할 때 이 트리거에거 이 변수 1 신호를 보냄
        self.set_user_value(key='SkillDebuffCheck_2Phase', value=0)
        # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함
        self.set_user_value(key='MonsterMany', value=0)
        # FirstBattleEnd변수 0으로 초기 셋팅, 첫번째 전투판에서 전투가 끝나면 이 변수 1 신호를 보냄
        self.set_user_value(key='FirstBattleEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=601) >= 1:
            # MS2TriggerBox  ID = 601, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면   601은 스타팅 지점과 1셋트 전투판 전체  포함하는 넓은 범위
            return 보스의저주디버프사용신호대기(self.ctx)


class 보스의저주디버프사용신호대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillDebuffCheck_2Phase') >= 1:
            # 보스가 플레이어에게 폭발 저주 디버프 부여 스킬 사용할 때 이 트리거에게  SkillDebuffCheck_2Phase = 1 신호를 보냄
            return 소환몹활성화될때까지잠시기다리기(self.ctx)
        if self.user_value(key='FirstBattleEnd') >= 1:
            # 보스전 첫번째 전투판에서의 전투가 끝났으면, 바로 폭발 저주 디버프 제거 단계로 넘어가도록 하기
            return 폭발저주디버프제거잠시대기(self.ctx)
        if self.user_value(key='FirstBattleEnd') >= 99:
            # 이슈라가 2페이즈 끝내고 3페이즈 넘어갈 때 이 변수 99 보내서 저주 디버프 제거 단계 실행 후 이 트리거 작동 정지시킴
            return 폭발저주디버프제거하고종료(self.ctx)


class 소환몹활성화될때까지잠시기다리기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            # !중요: 소환몹이 순차 등장하여  전투 상태로 전환 되어 MonsterMany 변수에 1씩 더해지는 상황이 될때까지 이 단계에서 13초 정도 머물기,13초 정도 해야 넉넉한 대기 시간임 혹시 3초 이하로 하면 넘 짧아서 베놈 스피릿이 공격 상태가 되기전에 트리거 단계가 넘어가 골치아픈 버그 생길 수 있으므로 넉넉히 6초 정도로 하자
            # 2페이즈 때 순차 저주걸기 소환몹 호출 때도 고려해야 하기 때문에 이 순차 행동이 다 끝날때까지 waitTick에서 머물러야 안정성이 있기 때문에 10초 이상 설정함
            # 이 waitTick 시간 10초 이상 설정 때문에 SkillDebuff_1Phase.xml,  SkillDebuff_1Phase.xml 트리거를 따로 나누었음
            return 소환몹전멸할때까지대기(self.ctx)


class 소환몹전멸할때까지대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') >= 0:
            # 등장하는 소환 졸몹이 전부 죽으면  MonsterMany 변수 -1씩하여 결국  0이 되어서 아래 <transition state="폭발저주디버프제거"> 단계로 넘어가게 됨
            return 폭발저주디버프제거잠시대기(self.ctx)
        if self.user_value(key='FirstBattleEnd') >= 1:
            # 첫번째 전투판에서 보스가 죽으면 높은 확률로 바로 스킬브레이크 발동될 수 있는데, 이때 폭발 저주 제거해 줘야 하기 때문에 이 조건을 설정함
            return 폭발저주디버프제거잠시대기(self.ctx)
        if self.user_value(key='FirstBattleEnd') >= 99:
            # 이슈라가 2페이즈 끝내고 3페이즈 넘어갈 때 이 변수 99 보내서 저주 디버프 제거 단계 실행 후 이 트리거 작동 정지시킴
            return 폭발저주디버프제거하고종료(self.ctx)


class 폭발저주디버프제거잠시대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 중요 변수 초기화는 여기서, 혹시  아래  waitTick="1200" 도중에 몬스터 AI에서 부터 변수 신호 받게 되면 로직이 꼬여 대박 버그 생길수 있어서 변수 초기화는 여기서
        # 중요:  여기 단계 끝나면 다시 처음인 <state name="보스의저주디버프사용신호대기"> 단계로 넘어가는데, 거기서의  SkillDebuffCheck_2Phase =  1 진행되지 않도록 이 변수 꼭 0 초기화 하기
        self.set_user_value(key='SkillDebuffCheck_2Phase', value=0)
        # FirstBattleEnd변수 0으로 초기 셋팅
        self.set_user_value(key='FirstBattleEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            # 소환 졸몹 다 죽이면 디버프가 바로 풀리는 것보다 약 1.2초 정도 뒤에 풀리게 waitTick 넣음
            return 폭발저주디버프제거(self.ctx)


class 폭발저주디버프제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 50001413은 보스한테 걸린 폭발 저주 디버프 제거해주는 애디셔널임, MS2TriggerBox  ID = 601 트리거 박스 크기는 1셋트 3개 전투판과 스타팅 지점까지 포함되는 넓은 범위임
        self.add_buff(box_ids=[601], skill_id=50001413, level=1, ignore_player=False)
        # 50001413 레벨1: 이 애디셔널에서 폭발 저주 디버프 뿐만 아니라 각종 SP 0 상태이상 공격력 저하 상태이상 즉 모든 상태이상 다 제거해줌

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1800):
            return 보스의저주디버프사용신호대기(self.ctx) # 다시 위 처음 단계로 돌아가기


class 폭발저주디버프제거하고종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 50001413은 보스한테 걸린 폭발 저주 디버프 제거해주는 애디셔널임, MS2TriggerBox  ID = 601 트리거 박스 크기는 1셋트 3개 전투판과 스타팅 지점까지 포함되는 넓은 범위임
        self.add_buff(box_ids=[601], skill_id=50001413, level=1, ignore_player=False)
        # 50001413 레벨1: 이 애디셔널에서 폭발 저주 디버프 뿐만 아니라 각종 SP 0 상태이상 공격력 저하 상태이상 즉 모든 상태이상 다 제거해줌

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            # 소환 졸몹 다 죽이면 디버프가 바로 풀리는 것보다 약 1.2초 정도 뒤에 풀리게 waitTick 넣음
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
