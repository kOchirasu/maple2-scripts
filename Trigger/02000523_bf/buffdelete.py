""" trigger/02000523_bf/buffdelete.xml """
import trigger_api


# TriggerModelID =  7 , 이 트리거는   AI_SandstoneGiantBlueShine.xml    AI_SandstoneDwarf2CloseAttack.xml   AI_SandstoneDwarf2LongAttack.xml 로 부터 신호를 받음
class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함, 몬스터 등장 이전에 이 변수 0 초기화 하기
        self.set_user_value(key='MonsterMany', value=0)
        # BuffDeleteOk 0으로 초기 셋팅, 보스가 소환몹 호출하면 AI_SandstoneGiantBlueShine.xml로 부터 1 셋팅 신호를 받게 됨
        self.set_user_value(key='BuffDeleteOk', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 트리거작동01(self.ctx)


class 트리거작동01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BuffDeleteOk') == 1:
            # 보스가 버프 사용 행동을 한 다음 바로, 이 트리거에게 BuffDeleteOk= 1 셋팅 신호를 보냄, (AI_SandstoneGiantBlueShine.xml로 )
            return 트리거작동02대기중(self.ctx)


class 트리거작동02대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return 트리거작동02(self.ctx)


class 트리거작동02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterMany') == 0:
            # 소환몹이 다 죽어 이 변수가 0되면 버프 제거 단계로 가기
            return 버프제거(self.ctx)


class 버프제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 어떤 버프가 걸려있는지 잘 모르겠으니 그냥 3개 버프 다 제거함 (트리거 박스 ID 안에 있는 대상 ) ,  참고로 버프 부여는 보스AI인 AI_SandstoneGiantBlueShine.xml 에서 진행함
        # 물방업, 마방업, 공업 버프 제거 하는 기능이 있는 버프 부여하기 ,   arg1="900" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨
        self.add_buff(box_ids=[900], skill_id=50001098, level=1)
        # 몬스터에게 애디셔널 거는 경우:  arg4 = "타겟이 몬스터로 하려면 1 인 경우  ->    arg1 = "몬스터스폰ID", arg2 = "애디셔널코드", arg3 = "애디셔널레벨", arg4 = "타겟이 몬스터로 하려면 1설정"
        # 이 변수 0 초기화 시켜, 보스가 졸몹 소환때까지 다시 대기 상태가 되도록 함
        self.set_user_value(key='BuffDeleteOk', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3700):
            # 트리거나 다음 단계로 너무 빨리 넘어가면 꼬일 수 있어서 WaitTick 천천히 넘어가도록 함
            return 트리거작동01(self.ctx)


initial_state = 시작대기중
