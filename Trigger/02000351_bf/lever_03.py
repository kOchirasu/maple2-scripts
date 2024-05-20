""" trigger/02000351_bf/lever_03.xml """
import trigger_api


class 닫힘상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000820], state=0)
        self.set_mesh(trigger_ids=[6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162], visible=True) # 빨간 선 보이게
        self.set_mesh(trigger_ids=[6181,6182,6183,6184,6185,6186,6187,6188,6189,6190,6191,6192]) # 파란 선 안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000820], state=1):
            return 작동(self.ctx)


class 작동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000820], state=0):
            return 열림상태(self.ctx)


class 열림상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[9000004], visible=True) # Object_Electricity_On_01
        self.set_mesh(trigger_ids=[6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162], interval=200, fade=15.0) # 빨간선 사라지게
        self.set_mesh(trigger_ids=[6181,6182,6183,6184,6185,6186,6187,6188,6189,6190,6191,6192], visible=True, interval=200) # 파란선 나타나게

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 열림(self.ctx)


class 열림(trigger_api.Trigger):
    pass


initial_state = 닫힘상태
