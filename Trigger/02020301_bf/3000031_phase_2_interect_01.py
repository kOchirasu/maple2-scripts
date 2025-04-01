""" trigger/02020301_bf/3000031_phase_2_interect_01.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10003131], state=2) # 2페이즈 인터렉트 오브젝트 대기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Phase_2_Interect_01') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__3000031_PHASE_2_INTERECT_01__0$', duration=3176)
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__3000031_PHASE_2_INTERECT_01__1$', duration=3176)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 인터렉트_설정(self.ctx)


class 인터렉트_설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020301_BF__3000031_PHASE_2_INTERECT_01__2$', duration=4000)
        self.spawn_monster(spawn_ids=[999], auto_target=False) # 탑승 아르케온 등장(연출용)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 탈것_등장(self.ctx)


class 탈것_등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10003131], state=1)
        self.destroy_monster(spawn_ids=[999])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003131], state=0):
            return 인터렉트_동작(self.ctx)
        if self.user_value(key='Phase_2_Interect_01') == 0:
            return 대기(self.ctx)


class 인터렉트_동작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 인터렉트_리셋(self.ctx)
        if self.user_value(key='Phase_2_Interect_01') == 0:
            return 대기(self.ctx)


class 인터렉트_리셋(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=101, additional_effect_id=62100152, level=1):
            # 아르케온 리셋 버프 조건 (62100152)
            return 리셋_대기(self.ctx)
        if self.user_value(key='Phase_2_Interect_01') == 0:
            return 대기(self.ctx)


class 리셋_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return 인터렉트_설정(self.ctx)
        if self.user_value(key='Phase_2_Interect_01') == 0:
            return 대기(self.ctx)


initial_state = 대기
