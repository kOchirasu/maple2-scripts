""" trigger/02000207_bf/lavaflow.xml """
import trigger_api


# 현재 이거 사용 안함, 만약을 위해 남겨두었음, 이 부분은  999102_Lavaflow.xml   999108_Lavaflow.xml    999109_Lavaflow.xml   3개 xml 파일로 나누어서 분할 설정 했음
class 전투체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[2001]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='LavaflowHigh') == 1:
            # 자쿰 팔이 제거될 때 LavaflowHigh 혹은 LavaflowLow 신호를 보내서 이 부분 작동하게 됨
            return 칸분기3(self.ctx)
        if self.user_value(key='LavaflowLow') == 1:
            # 자쿰 팔이 제거될 때 LavaflowHigh 혹은 LavaflowLow 신호를 보내서 이 부분 작동하게 됨
            return 칸분기2(self.ctx)
        if self.user_value(key='LavaflowLeft') == 1:
            # 왼쪽 용암 담당 계약의 토템이 생성될때, 이 부분 작동,   LavaflowLeft 변수는 자쿰몸체 보스한테 LavaflowLeft = 1 설정되어서 넘어오는 것임
            return 왼쪽용암생성(self.ctx)
        if self.user_value(key='LavaflowRight') == 1:
            # 오른쪽 용암 담당 계약의 토템이 생성될때, 이 부분 작동,   LavaflowRight 변수는 자쿰몸체 보스한테 LavaflowRight = 1 설정되어서 넘어오는 것임
            return 오른쪽용암생성(self.ctx)
        if self.user_value(key='BattleEnd2') == 1:
            # BattleEnd2 변수는 보스 생성쪽 트리거 설정 xml 에서 보스가 죽을 경우 BattleEnd2 = 1 설정되어서 넘어오는 것임
            return 종료(self.ctx)


class 칸분기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999102, key='LavaflowHigh', value=0)
        self.set_effect(trigger_ids=[600], visible=True)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        # MS2PatrolData_1001A  이것이 용암 2층까지 올라오게 하는 설정값
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=52.0):
            # 용암이 2층까지 올라오는 확률은 약간 더 높게 설정
            return 칸이동3(self.ctx)
        if self.random_condition(weight=48.0):
            return 리턴(self.ctx)
        if self.user_value(key='BattleEnd2') == 1:
            return 종료(self.ctx)


class 칸이동3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=28000):
            return 리턴(self.ctx)
        if self.user_value(key='BattleEnd2') == 1:
            return 종료(self.ctx)


class 칸분기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999102, key='LavaflowLow', value=0)
        self.set_effect(trigger_ids=[600], visible=True)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        # MS2PatrolData_1001B  이것이 용암 1층까지 올라오게 하는 설정값
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=99.0):
            # 용암이 1층까지 올라오는 확률은 엄청 높게 설정
            return 칸이동2(self.ctx)
        if self.random_condition(weight=1.0):
            return 리턴(self.ctx)
        if self.user_value(key='BattleEnd2') == 1:
            return 종료(self.ctx)


class 칸이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return 리턴(self.ctx)
        if self.user_value(key='BattleEnd2') == 1:
            return 종료(self.ctx)


class 리턴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.destroy_monster(spawn_ids=[1001])
            return 대기(self.ctx)


# 왼쪽담당 계약의 토템을 소환하면서 자쿰몸체한테 신호 받아 용암 올라오는 경우임
class 왼쪽용암생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이 Lavaflow.xml 파일과 연결된  MS2TriggerModel의 TriggerModelID가 999102 임
        # LavaflowLeft 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        self.set_user_value(trigger_id=999102, key='LavaflowLeft', value=0)
        # ### 올라온 용암 내려가게 할 때 사용하는 LavaflowLeftStop 변수 이전에 이미 사용했을 수 있으므로 여기서  0으로 꼭 초기화 해야함
        self.set_user_value(trigger_id=999102, key='LavaflowLeftStop', value=0)
        self.set_effect(trigger_ids=[600], visible=True)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002A')

    def on_tick(self) -> trigger_api.Trigger:
        # 보스가 죽으면 보스 스폰시키는 트리거 xml 에서 BattleEnd2 = 1 신호를 보내서 올라와 있는 용암을 여기서 바로 제거 시키게 함
        if self.user_value(key='LavaflowLeftStop') == 1:
            return 왼쪽용암내려가기(self.ctx)
        if self.user_value(key='BattleEnd2') == 1:
            return 종료(self.ctx)


class 왼쪽용암내려가기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ### 왼쪽용암내려가기  신호받는 대기 상태에서 이 변수가 1이 되는 상황이 생길수도 있기 때문에 만약을 대비해 여기서도 다시한번 0으로 초기화 함
        self.set_user_value(trigger_id=999102, key='LavaflowLeft', value=0)
        # LavaflowLeftStop 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        self.set_user_value(trigger_id=999102, key='LavaflowLeftStop', value=0)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.destroy_monster(spawn_ids=[1002])
            return 대기(self.ctx)


# 오른쪽담당 계약의 토템을 소환하면서 자쿰몸체한테 신호 받아 용암 올라오는 경우임
class 오른쪽용암생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이 Lavaflow.xml 파일과 연결된  MS2TriggerModel의 TriggerModelID가 999102 임
        # LavaflowRight 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        self.set_user_value(trigger_id=999102, key='LavaflowRight', value=0)
        # ### 올라온 용암 내려가게 할 때 사용하는 LavaflowRightStop 변수 이전에 이미 사용했을 수 있으므로 여기서  0으로 꼭 초기화 해야함
        self.set_user_value(trigger_id=999102, key='LavaflowRightStop', value=0)
        self.set_effect(trigger_ids=[600], visible=True)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003A')

    def on_tick(self) -> trigger_api.Trigger:
        # 보스가 죽으면 보스 스폰시키는 트리거 xml 에서 BattleEnd2 = 1 신호를 보내서 올라와 있는 용암을 여기서 바로 제거 시키게 함
        if self.user_value(key='LavaflowRightStop') == 1:
            return 오른쪽용암내려가기(self.ctx)
        if self.user_value(key='BattleEnd2') == 1:
            return 종료(self.ctx)


class 오른쪽용암내려가기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ### 오른쪽용암내려가기  신호받는 대기 상태에서 이 변수가 1이 되는 상황이 생길수도 있기 때문에 만약을 대비해 여기서도 다시한번 0으로 초기화 함
        self.set_user_value(trigger_id=999102, key='LavaflowRight', value=0)
        # LavaflowRightStop 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        self.set_user_value(trigger_id=999102, key='LavaflowRightStop', value=0)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.destroy_monster(spawn_ids=[1003])
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1003])


initial_state = 전투체크
