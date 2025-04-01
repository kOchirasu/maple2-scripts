""" trigger/52100301_qd/300002_phase_1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AI_Phase') == 1:
            return 텍스트_대기(self.ctx)


class 텍스트_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 패이즈_1_시작(self.ctx)


class 패이즈_1_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='AI_Phase', value=0)
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_unfair', script='$52100301_QD__300002_PHASE_1__0$', duration=4176)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


initial_state = 대기
