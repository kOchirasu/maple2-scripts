""" trigger/02000207_bf/999102_lavaflow.xml """
import trigger_api


class 전투체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='LavaflowHigh') == 1:
            # 자쿰 팔이 제거될 때 LavaflowHigh 혹은 LavaflowLow 신호를 보내서 이 부분 작동하게 됨
            self.set_user_value(trigger_id=999102, key='LavaflowHigh', value=0)
            return 칸이동3(self.ctx)
        if self.user_value(key='LavaflowLow') == 1:
            # 자쿰 팔이 제거될 때 LavaflowHigh 혹은 LavaflowLow 신호를 보내서 이 부분 작동하게 됨
            self.set_user_value(trigger_id=999102, key='LavaflowLow', value=0)
            return 칸이동2(self.ctx)
        if self.user_value(key='BattleEnd2') == 1:
            # BattleEnd2 변수는 보스 생성쪽 트리거 설정 xml 에서 보스가 죽을 경우 BattleEnd2 = 1 설정되어서 넘어오는 것임
            return 종료(self.ctx)


class 칸이동3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=28000):
            return 리턴(self.ctx)
        if self.user_value(key='BattleEnd2') == 1:
            return 종료(self.ctx)


class 칸이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
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


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001])


initial_state = 전투체크
