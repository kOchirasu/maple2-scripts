""" trigger/02000331_bf/switch07.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7773]) # 발판 휠 내려옴 사운드
        self.set_breakable(trigger_ids=[5001])
        self.set_breakable(trigger_ids=[5002])
        self.set_breakable(trigger_ids=[5011])
        self.set_breakable(trigger_ids=[5012])
        self.set_breakable(trigger_ids=[5021])
        self.set_breakable(trigger_ids=[5022])
        self.set_breakable(trigger_ids=[5031])
        self.set_breakable(trigger_ids=[5032])
        self.set_mesh(trigger_ids=[40000,40001]) # TOK용 투명한 매쉬

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000793], state=0):
            # 3rd 스위치03
            return 발판내리기(self.ctx)


class 발판내리기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[5001], enable=True)
        self.set_breakable(trigger_ids=[5002], enable=True)
        self.set_breakable(trigger_ids=[5011], enable=True)
        self.set_breakable(trigger_ids=[5012], enable=True)
        self.set_breakable(trigger_ids=[5021], enable=True)
        self.set_breakable(trigger_ids=[5022], enable=True)
        self.set_breakable(trigger_ids=[5031], enable=True)
        self.set_breakable(trigger_ids=[5032], enable=True)
        self.set_effect(trigger_ids=[7773], visible=True) # 발판 내려올 때 휠 사운드
        self.set_mesh(trigger_ids=[40000,40001], visible=True) # TOK용 투명한 매쉬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[5001])
        self.set_breakable(trigger_ids=[5002])
        self.set_breakable(trigger_ids=[5011])
        self.set_breakable(trigger_ids=[5012])
        self.set_breakable(trigger_ids=[5021])
        self.set_breakable(trigger_ids=[5022])
        self.set_breakable(trigger_ids=[5031])
        self.set_breakable(trigger_ids=[5032])
        self.set_effect(trigger_ids=[7773]) # 발판 휠 내려옴 사운드
        self.set_mesh(trigger_ids=[40000,40001]) # TOK용 투명한 매쉬


initial_state = 대기
