""" trigger/51000003_dg/fog.xml """
import trigger_api


# 포그 이펙트
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001])
        self.set_effect(trigger_ids=[7002])
        self.set_effect(trigger_ids=[7003])
        self.set_effect(trigger_ids=[7004])
        self.set_effect(trigger_ids=[7005])
        self.set_effect(trigger_ids=[7010], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01') == 1:
            return None # Missing State: Round_01
        if self.user_value(key='Round_02') == 1:
            return Round_02_Ready(self.ctx)
        if self.user_value(key='Round_03') == 1:
            return Round_03_Ready(self.ctx)
        if self.user_value(key='Round_04') == 1:
            return Round_04_Ready(self.ctx)


class Round_02_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return Round_02_Start(self.ctx)


class Round_03_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return Round_03_Start(self.ctx)


class Round_04_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return Round_04_Start(self.ctx)


class Round_05_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return Round_05_Start(self.ctx)


class Round_06_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return Round_06_Start(self.ctx)


class Round_02_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.show_guide_summary(entity_id=61000901, text_id=61000901, duration=3000) # 안개가 펼쳐집니다.
        self.set_effect(trigger_ids=[7001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_02') == 0:
            return Round_check(self.ctx)
        if self.wait_tick(wait_tick=30000):
            return Round_check(self.ctx)


class Round_03_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.show_guide_summary(entity_id=61000901, text_id=61000901, duration=3000) # 안개가 펼쳐집니다.
        self.set_effect(trigger_ids=[7002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_03') == 0:
            return Round_check(self.ctx)
        if self.wait_tick(wait_tick=30000):
            return Round_check(self.ctx)


class Round_04_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.show_guide_summary(entity_id=61000901, text_id=61000901, duration=3000) # 안개가 펼쳐집니다.
        self.set_effect(trigger_ids=[7002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_04') == 0:
            return Round_check(self.ctx)
        if self.wait_tick(wait_tick=30000):
            return Round_check(self.ctx)


class Round_05_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.show_guide_summary(entity_id=61000901, text_id=61000901, duration=3000) # 안개가 펼쳐집니다.
        self.set_effect(trigger_ids=[7003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_05') == 0:
            return Round_check(self.ctx)
        if self.wait_tick(wait_tick=30000):
            return Round_check(self.ctx)


class Round_06_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.show_guide_summary(entity_id=61000901, text_id=61000901, duration=3000) # 안개가 펼쳐집니다.
        self.set_effect(trigger_ids=[7005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_06') == 0:
            return Round_check(self.ctx)
        if self.wait_tick(wait_tick=30000):
            return Round_check(self.ctx)


initial_state = Round_check
