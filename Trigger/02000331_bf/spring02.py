""" trigger/02000331_bf/spring02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7001])
        self.set_skill(trigger_ids=[7002])
        self.set_skill(trigger_ids=[7003])
        self.set_skill(trigger_ids=[7004])
        self.set_skill(trigger_ids=[7005])
        self.set_skill(trigger_ids=[7006])
        self.set_skill(trigger_ids=[7007])
        self.set_skill(trigger_ids=[7008])
        self.set_skill(trigger_ids=[7009])
        self.set_skill(trigger_ids=[7010])
        self.set_skill(trigger_ids=[7011])
        self.set_skill(trigger_ids=[7012])
        self.set_skill(trigger_ids=[7013])
        self.set_skill(trigger_ids=[7014])
        self.set_skill(trigger_ids=[7015])
        self.set_skill(trigger_ids=[7016])
        self.set_skill(trigger_ids=[7017])
        self.set_skill(trigger_ids=[7018])
        self.set_skill(trigger_ids=[7019])
        self.set_skill(trigger_ids=[7020])
        self.set_skill(trigger_ids=[7021])
        self.set_skill(trigger_ids=[7022])
        self.set_skill(trigger_ids=[7023])
        self.set_skill(trigger_ids=[7024])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[99991]):
            return 스킬발동(self.ctx)


class 스킬발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7001], enable=True)
        self.set_skill(trigger_ids=[7002], enable=True)
        self.set_skill(trigger_ids=[7003], enable=True)
        self.set_skill(trigger_ids=[7004], enable=True)
        self.set_skill(trigger_ids=[7005], enable=True)
        self.set_skill(trigger_ids=[7006], enable=True)
        self.set_skill(trigger_ids=[7007], enable=True)
        self.set_skill(trigger_ids=[7008], enable=True)
        self.set_skill(trigger_ids=[7009], enable=True)
        self.set_skill(trigger_ids=[7010], enable=True)
        self.set_skill(trigger_ids=[7011], enable=True)
        self.set_skill(trigger_ids=[7012], enable=True)
        self.set_skill(trigger_ids=[7013], enable=True)
        self.set_skill(trigger_ids=[7014], enable=True)
        self.set_skill(trigger_ids=[7015], enable=True)
        self.set_skill(trigger_ids=[7016], enable=True)
        self.set_skill(trigger_ids=[7017], enable=True)
        self.set_skill(trigger_ids=[7018], enable=True)
        self.set_skill(trigger_ids=[7019], enable=True)
        self.set_skill(trigger_ids=[7020], enable=True)
        self.set_skill(trigger_ids=[7021], enable=True)
        self.set_skill(trigger_ids=[7022], enable=True)
        self.set_skill(trigger_ids=[7023], enable=True)
        self.set_skill(trigger_ids=[7024], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대기(self.ctx)


initial_state = 대기
