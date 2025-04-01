""" trigger/02100001_bf/05_getmusicbuff.xml """
import trigger_api


# 아프렐라 오지 : 연주 시 특수 효과가 발동되는 패시브 버프 부여
class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='GiveBuffSlowly', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9900]):
            return GiveBuff01(self.ctx)


# 시작 초반에 철창 문이 닫히기 전까지 1초마다 버프 지급
class GiveBuff01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9900], skill_id=71000030, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GiveBuff01(self.ctx)
        if self.user_value(key='GiveBuffSlowly') == 1:
            return GiveBuff02(self.ctx)


# 철창문이 닫힌 이후에는 세이프 존에 유저를 감지하면 세이프 존에 있는 유저에게 버프 지급
class GiveBuff02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9901], skill_id=71000030, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9901]):
            return GiveBuff02(self.ctx)
        if self.user_value(key='GiveBuffSlowly') == 2:
            return Quit(self.ctx)


# 플레이 제한 시간이 끝나면 버프 지급을 멈춤
class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9900], skill_id=71000034, level=1)


initial_state = Wait
