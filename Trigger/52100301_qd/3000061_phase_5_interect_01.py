""" trigger/52100301_qd/3000061_phase_5_interect_01.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200031,200032])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_5_Interect_01') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$52100301_QD__3000061_PHASE_5_INTERECT_01__0$', duration=4000)
        self.spawn_monster(spawn_ids=[999], auto_target=False) # 탑승 아르케온 등장(연출용)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 탈것_등장(self.ctx)


class 탈것_등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10003126], state=1)
        self.destroy_monster(spawn_ids=[999])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003126], state=0):
            return 인터렉트_동작(self.ctx)
        if self.user_value(key='Phase_5_Interect_01') == 0:
            return 대기(self.ctx)


class 인터렉트_동작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 인터렉트_리셋(self.ctx)
        if self.user_value(key='Phase_5_Interect_01') == 0:
            return 대기(self.ctx)


class 인터렉트_리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_any_user_additional_effect(box_id=0, additional_effect_id=62100152, level=1):
            # 아르케온 리셋 버프 조건 (62100152)
            return 리셋_대기(self.ctx)
        if self.user_value(key='Phase_5_Interect_01') == 0:
            return 대기(self.ctx)


class 리셋_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작(self.ctx)
        if self.user_value(key='Phase_5_Interect_01') == 0:
            return 대기(self.ctx)


initial_state = 대기
