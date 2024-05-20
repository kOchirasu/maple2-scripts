""" trigger/99999841/badmob_message.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=901) == 1:
            return 쫄몹1(self.ctx)
        if self.dungeon_variable(var_id=902) == 1:
            return 쫄몹2(self.ctx)
        if self.dungeon_variable(var_id=903) == 1:
            return 쫄몹3(self.ctx)


class 쫄몹1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='방해쫄몹1이 생성되었습니다.\\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return 대기(self.ctx)


class 쫄몹2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='방해쫄몹2가 생성되었습니다.\\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return 대기(self.ctx)


class 쫄몹3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='방해쫄몹3이 생성되었습니다.\\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=2) == 1:
            return 종료(self.ctx)
        if self.dungeon_variable(var_id=3) == 1:
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
