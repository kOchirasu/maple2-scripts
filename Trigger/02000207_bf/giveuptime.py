""" trigger/02000207_bf/giveuptime.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 타이머(self.ctx)


class 타이머(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            self.set_event_ui(type=1, arg2='$DUNGEON__GIVEUP__TIME__0$', arg3='3000')
            self.dungeon_enable_give_up(is_enable=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
