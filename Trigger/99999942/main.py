""" trigger/99999942/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import FieldGame


class StateNone(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_field_game(type=FieldGame.WaterGunBattle, reset=True) # 데이터 셋팅
        # 유저대기중 의 arg2와 같도록
        self.field_game_constant(key='WaitUserTick', value='15000') # 유저이동의 arg2와 같도록
        self.field_game_constant(key='WaitPlayTick', value='5000')
        self.field_game_constant(key='ResizeWaitTick', value='15000,15000,15000,15000')
        self.field_game_constant(key='ResizeWarningTick', value='5000,5000,5000,5000')
        self.field_game_constant(key='SkillSetID', value='99930047')
        self.field_game_constant(key='MinPlayer', value='2') # 포탈 셋팅
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WaitUser') == 1:
            return 유저대기중(self.ctx)


class 유저대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=15, display=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MoveUser') == 1:
            return 유저이동(self.ctx)
        if self.user_value(key='End') == 1:
            return 종료(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5, display=True)
        self.move_user(map_id=99999942, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Play') == 1:
            return 게임시작(self.ctx)


class 게임시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PlayRound1') == 1:
            return 라운드1(self.ctx)


class 라운드1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PlayRound2') == 1:
            return 라운드2(self.ctx)
        if self.user_value(key='End') == 1:
            return 종료(self.ctx)


class 라운드2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], start_delay=2, interval=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PlayRound3') == 1:
            return 라운드3(self.ctx)
        if self.user_value(key='End') == 1:
            return 종료(self.ctx)


class 라운드3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48], start_delay=2, interval=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PlayRound4') == 1:
            return 라운드4(self.ctx)
        if self.user_value(key='End') == 1:
            return 종료(self.ctx)


class 라운드4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[49,50,51,52,53,54,55,56,57,58,59,60], start_delay=2, interval=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End') == 1:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64], visible=True)
        # self.set_portal(portal_id=1, visible=True, enable=True)
        self.move_user(map_id=99999942, portal_id=1)


initial_state = StateNone
