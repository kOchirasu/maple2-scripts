""" trigger/99999840/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990002, key='Team1Battle', value=0)
        self.set_user_value(trigger_id=99990003, key='Start', value=0)
        self.set_user_value(trigger_id=99990004, key='Start', value=0)
        self.set_user_value(trigger_id=99990005, key='Start', value=0)
        self.set_user_value(trigger_id=99990015, key='Start', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001) == 6:
            return 세팅(self.ctx)


class 세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(map_id=99999841, portal_id=1, box_id=9001, count=3)
        self.set_event_ui(type=1, arg2='잠시 후 경기가 시작됩니다.', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=1) == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='경기 시작!\\n당신은 A팀입니다.', arg3='3000')
        self.set_user_value(trigger_id=99990002, key='Team1Battle', value=1)
        self.set_user_value(trigger_id=99990003, key='Start', value=1)
        self.set_user_value(trigger_id=99990004, key='Start', value=1)
        self.set_user_value(trigger_id=99990005, key='Start', value=1)
        self.set_user_value(trigger_id=99990015, key='Start', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 메시지1(self.ctx)


class 메시지1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='검은 군단을 해치우고 자원을 획득하세요.\\n획득한 자원을 20개 모아서 보스를 불러내세요.\\n한번에 최대 9개의 자원을 들 수 있습니다.', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return A팀승리(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return B팀승리(self.ctx)


class A팀승리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='A팀이 승리했습니다!', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class B팀승리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='B팀이 승리했습니다!', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990002, key='Team1Battle', value=0)
        self.set_user_value(trigger_id=99990003, key='Start', value=0)
        self.set_user_value(trigger_id=99990004, key='Start', value=0)
        self.set_user_value(trigger_id=99990005, key='Start', value=0)
        self.set_interact_object(trigger_ids=[10002175], state=0)
        self.set_interact_object(trigger_ids=[10002176], state=0)
        self.set_interact_object(trigger_ids=[10002177], state=0)
        self.set_interact_object(trigger_ids=[10002178], state=0)


initial_state = 대기
