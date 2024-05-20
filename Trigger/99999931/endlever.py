""" trigger/99999931/endlever.xml """
import trigger_api


class 게임종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[211,212], visible=True) # 닫힌 문이 보인다 (arg2=1)
        self.set_mesh(trigger_ids=[551,552]) # 열린 문을 가린다 (arg2=0)
        self.set_interact_object(trigger_ids=[10000216], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000216], state=0):
            return 종료안내(self.ctx)


class 종료안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.set_event_ui(type=5, arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 문열기(self.ctx)


class 문열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=7)
        self.set_mesh(trigger_ids=[211,212]) # 닫힌 문을 가린다
        self.set_mesh(trigger_ids=[551,552], visible=True) # 열린 문을 보인다

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 문닫기(self.ctx)


class 문닫기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_mesh(trigger_ids=[211,212], visible=True) # 닫힌 문을 가린다
        self.set_mesh(trigger_ids=[551,552]) # 열린 문을 보인다
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208], visible=True) # 순간 이동 발판이 보인다 (arg2=1)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=101, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=102, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=103, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=104, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=115, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=116, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=117, enable=True)
        # 순간 이동 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=118, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 게임종료(self.ctx)


initial_state = 게임종료
