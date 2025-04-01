""" trigger/52100301_qd/300006_phase_5.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AI_Phase') == 5:
            return 패이즈_5_시작(self.ctx)


class 패이즈_5_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_unfair', script='$52100301_QD__300006_PHASE_5__0$', duration=3176)
        self.set_effect(trigger_ids=[200021,200022,200023,200024,200025,200026,200027,200028])
        self.set_user_value(key='AI_Phase', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3000051, key='Phase_4_Interect_01', value=0) # 페이즈4 장치 삭제
        self.set_user_value(trigger_id=3000052, key='Phase_4_Interect_02', value=0)
        self.set_user_value(trigger_id=3000053, key='Phase_4_Interect_03', value=0)
        self.set_user_value(trigger_id=3000054, key='Phase_4_Interect_04', value=0)
        self.set_effect(trigger_ids=[200001,200002,200003,200004,200005,200006,200007,200008])
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_unfair', script='$52100301_QD__300006_PHASE_5__1$', duration=3176)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아르케온_등장(self.ctx)


class 아르케온_등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='AI_Phase', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아르케온_탈것_생성(self.ctx)


class 아르케온_탈것_생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3000061, key='Phase_5_Interect_01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return None # Missing State: 게임종료


initial_state = 대기
