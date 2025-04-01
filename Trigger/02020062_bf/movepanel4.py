""" trigger/02020062_bf/movepanel4.xml """
import trigger_api


class 발판초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[2300,2301,2302,2303,2304,2305,2306,2307,2308])
        self.set_visible_breakable_object(trigger_ids=[2300,2301,2302,2303,2304,2305,2306,2307,2308])
        self.set_user_value(trigger_id=99990027, key='MovePanel04', value=0)
        self.set_interact_object(trigger_ids=[12000118], state=2) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MovePanel04') == 1:
            # 이동발판 삭제 후 대기
            return 레버생성(self.ctx)


class 레버생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000118], state=1) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000118], state=0):
            return 발판이동(self.ctx)


class 발판이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[2300,2301,2302,2303,2304,2305,2306,2307,2308], visible=True)
        self.set_interact_object(trigger_ids=[12000118], state=2) # 이동발판트리거

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9203]):
            self.set_breakable(trigger_ids=[2300,2301,2302,2303,2304,2305,2306,2307,2308], enable=True)
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[2300,2301,2302,2303,2304,2305,2306,2307,2308])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 발판이동(self.ctx)


initial_state = 발판초기화
