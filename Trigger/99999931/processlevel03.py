""" trigger/99999931/processlevel03.xml """
import trigger_api


class 레버당기기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000219], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000219], state=0):
            return 카운트다운1(self.ctx)


class 카운트다운1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='31', seconds=1)
        self.set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='31'):
            return 카운트다운2(self.ctx)


class 카운트다운2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='32', seconds=1)
        self.set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='32'):
            return 카운트다운3(self.ctx)


class 카운트다운3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='33', seconds=1)
        self.set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='33'):
            return 게임시작(self.ctx)


class 게임시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='34', seconds=1) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,112,113,115,116,118,119,121,122,124,125,130,131,132,133,134,135,136], enable=True) # 움직이는 발판을 이동한다 (arg2=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='34'):
            return 게임진행1(self.ctx)


class 게임진행1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='35', seconds=1) # arg2는 시간 (초)
        self.set_breakable(trigger_ids=[101,102,103,104,105,106,107,112,113,115,116,118,119,121,122,124,125,130,131,132,133,134,135,136]) # 움직이는 발판을 멈춘다 (arg2=0)
        self.set_skill(trigger_ids=[801], enable=True)
        self.set_skill(trigger_ids=[802], enable=True)
        self.set_skill(trigger_ids=[803], enable=True)
        self.set_skill(trigger_ids=[804], enable=True)
        self.set_skill(trigger_ids=[805], enable=True)
        self.set_skill(trigger_ids=[806], enable=True)
        self.set_skill(trigger_ids=[807], enable=True)
        self.set_skill(trigger_ids=[812], enable=True)
        self.set_skill(trigger_ids=[813], enable=True)
        self.set_skill(trigger_ids=[815], enable=True)
        self.set_skill(trigger_ids=[816], enable=True)
        self.set_skill(trigger_ids=[818], enable=True)
        self.set_skill(trigger_ids=[819], enable=True)
        self.set_skill(trigger_ids=[821], enable=True)
        self.set_skill(trigger_ids=[822], enable=True)
        self.set_skill(trigger_ids=[824], enable=True)
        self.set_skill(trigger_ids=[825], enable=True)
        self.set_skill(trigger_ids=[830], enable=True)
        self.set_skill(trigger_ids=[831], enable=True)
        self.set_skill(trigger_ids=[832], enable=True)
        self.set_skill(trigger_ids=[833], enable=True)
        self.set_skill(trigger_ids=[834], enable=True)
        self.set_skill(trigger_ids=[835], enable=True)
        self.set_skill(trigger_ids=[836], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='35'):
            return 게임진행2(self.ctx)


class 게임진행2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='36', seconds=2) # arg2는 시간 (초)
        self.set_skill(trigger_ids=[801])
        self.set_skill(trigger_ids=[802])
        self.set_skill(trigger_ids=[803])
        self.set_skill(trigger_ids=[804])
        self.set_skill(trigger_ids=[805])
        self.set_skill(trigger_ids=[806])
        self.set_skill(trigger_ids=[807])
        self.set_skill(trigger_ids=[812])
        self.set_skill(trigger_ids=[813])
        self.set_skill(trigger_ids=[815])
        self.set_skill(trigger_ids=[816])
        self.set_skill(trigger_ids=[818])
        self.set_skill(trigger_ids=[819])
        self.set_skill(trigger_ids=[821])
        self.set_skill(trigger_ids=[822])
        self.set_skill(trigger_ids=[824])
        self.set_skill(trigger_ids=[825])
        self.set_skill(trigger_ids=[830])
        self.set_skill(trigger_ids=[831])
        self.set_skill(trigger_ids=[832])
        self.set_skill(trigger_ids=[833])
        self.set_skill(trigger_ids=[834])
        self.set_skill(trigger_ids=[835])
        self.set_skill(trigger_ids=[836])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='36'):
            return 레버당기기(self.ctx)


initial_state = 레버당기기
