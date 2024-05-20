""" trigger/99999931/startlever.xml """
import trigger_api


class 시작레버(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[211,212], visible=True) # 닫힌 문이 보인다 (arg2=1)
        self.set_mesh(trigger_ids=[551,552]) # 열린 문을 가린다 (arg2=0)
        # 탈락자용 포털을 안 보이게(arg2=0) 하고 동작하게(arg3=1) 한다
        self.set_portal(portal_id=500, enable=True)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136]) # 움직이는 발판을 멈춘다 (arg2=0)
        self.set_interact_object(trigger_ids=[10000215], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000215], state=0):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208]) # 순간 이동 발판이 사라진다
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=101)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=102)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=103)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=104)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=115)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=116)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=117)
        # 순간 이동 포털을 안 보이게 하고 동작 안하게 한다
        self.set_portal(portal_id=118)

    def on_tick(self) -> trigger_api.Trigger:
        return 게임준비(self.ctx)


class 게임준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=3)
        self.set_event_ui(type=1, arg2='$99999931__STARTLEVER__0$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 시작레버(self.ctx)


initial_state = 시작레버
