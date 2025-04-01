""" trigger/02000552_bf/buffcheck.xml """
import trigger_api


# TriggerModelID =  553
class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함, 몬스터 등장 이전에 이 변수 0 초기화 하기
        self.set_user_value(key='MonsterMany', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 트리거작동시작(self.ctx)


class 트리거작동시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') >= 1:
            # 졸몹이 등장해 이 변수가 1 이상의 숫자가 되면, 블랙빈에게 버프 부여하기
            return 블랙빈에게버프부여(self.ctx)


class 블랙빈에게버프부여(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg2은 몬스터 스폰ID 101는 어려운 난이도    102는 쉬운 난이도
        # 50003307(레벨2)는 버프 시간 엄청 긴거
        # 공격반사 버프 부여하기 ,   arg1="101" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨
        self.add_buff(box_ids=[101], skill_id=50003307, level=2)
        # 몬스터에게 애디셔널 거는 경우:  arg4 = "타겟이 몬스터로 하려면 1 인 경우  ->    arg1 = "몬스터스폰ID", arg2 = "애디셔널코드", arg3 = "애디셔널레벨", arg4 = "타겟이 몬스터로 하려면 1설정"
        # 50003307(레벨2)는 버프 시간 엄청 긴거
        # 공격반사 버프 부여하기 ,   arg1="102" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨
        self.add_buff(box_ids=[102], skill_id=50003307, level=2)
        # 몬스터에게 애디셔널 거는 경우:  arg4 = "타겟이 몬스터로 하려면 1 인 경우  ->    arg1 = "몬스터스폰ID", arg2 = "애디셔널코드", arg3 = "애디셔널레벨", arg4 = "타겟이 몬스터로 하려면 1설정"

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 블랙빈에게버프삭제체크(self.ctx)


class 블랙빈에게버프삭제체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') == 0:
            # 졸몹이 전멸해 이 변수가 0이 되면
            return 블랙빈에게버프삭제대기(self.ctx)


class 블랙빈에게버프삭제대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return 블랙빈에게버프삭제실시(self.ctx)


class 블랙빈에게버프삭제실시(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg2은 몬스터 스폰ID 101는 어려운 난이도    102는 쉬운 난이도
        # 50003309(레벨1)은 50003307 애디셔널 제거하는 기능이 있음
        # 공격반사 버프 버프 제거 ,   arg1="101" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨
        self.add_buff(box_ids=[101], skill_id=50003309, level=1)
        # 몬스터에게 애디셔널 거는 경우:  arg4 = "타겟이 몬스터로 하려면 1 인 경우  ->    arg1 = "몬스터스폰ID", arg2 = "애디셔널코드", arg3 = "애디셔널레벨", arg4 = "타겟이 몬스터로 하려면 1설정"
        # 50003309(레벨1)은 50003307 애디셔널 제거하는 기능이 있음
        # 공격반사 버프 버프 제거 ,   arg1="102" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨
        self.add_buff(box_ids=[102], skill_id=50003309, level=1)
        # 몬스터에게 애디셔널 거는 경우:  arg4 = "타겟이 몬스터로 하려면 1 인 경우  ->    arg1 = "몬스터스폰ID", arg2 = "애디셔널코드", arg3 = "애디셔널레벨", arg4 = "타겟이 몬스터로 하려면 1설정"

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 트리거작동시작(self.ctx) # 다시 처음단계로 되돌아가기


initial_state = 시작대기중
