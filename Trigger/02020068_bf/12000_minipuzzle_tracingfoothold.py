""" trigger/02020068_bf/12000_minipuzzle_tracingfoothold.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='2')
        self.set_interact_object(trigger_ids=[12000082], state=2) # Flower01
        self.set_interact_object(trigger_ids=[12000083], state=2) # Flower02
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001121 걸어서 71001021 제거
        self.set_interact_object(trigger_ids=[12000225], state=2)
        # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001021 부여
        self.set_interact_object(trigger_ids=[12000075], state=2)
        self.set_mesh(trigger_ids=[12001]) # FootHold01
        self.set_mesh(trigger_ids=[12002]) # FootHold02
        self.set_mesh(trigger_ids=[12003]) # FootHold03
        self.set_actor(trigger_id=12201, initial_sequence='Interaction_luminous_A01_on') # Actor_FlowerOn01
        self.set_actor(trigger_id=12202, initial_sequence='Interaction_luminous_A01_on') # Actor_FlowerOn02
        self.set_effect(trigger_ids=[12100]) # Success Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimeEventOn') == 1:
            return SettingDelay(self.ctx)


class SettingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Setting(self.ctx)


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001021 부여
        self.set_interact_object(trigger_ids=[12000075], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000075], state=0):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001021 지속시간 동일
            self.set_timer(timer_id='1', seconds=120, auto_remove=True)
            return TracingFootHold_Start_Delay(self.ctx)


class TracingFootHold_Start_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TracingFootHold_Play01(self.ctx)


class TracingFootHold_Play01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[12001], visible=True, fade=1.0) # FootHold01
        self.set_interact_object(trigger_ids=[12000082], state=1) # Flower01

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000082], state=0):
            return TracingFootHold_Play01_Delay(self.ctx)
        if self.time_expired(timer_id='1'):
            return TracingFootHold_Fail(self.ctx)


class TracingFootHold_Play01_Delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=12201, visible=True, initial_sequence='Interaction_luminous_A01_on') # Actor_FlowerOn01
        self.set_interact_object(trigger_ids=[12000082], state=2) # Flower01

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TracingFootHold_Play02(self.ctx)
        if self.time_expired(timer_id='1'):
            return TracingFootHold_Fail(self.ctx)


class TracingFootHold_Play02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[12002], visible=True, fade=1.0) # FootHold02
        self.set_interact_object(trigger_ids=[12000083], state=1) # Flower02

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000083], state=0):
            return TracingFootHold_Play02_Delay(self.ctx)
        if self.time_expired(timer_id='1'):
            return TracingFootHold_Fail(self.ctx)


class TracingFootHold_Play02_Delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=12202, visible=True, initial_sequence='Interaction_luminous_A01_on') # Actor_FlowerOn02
        self.set_interact_object(trigger_ids=[12000083], state=2) # Flower02

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TracingFootHold_Success(self.ctx)


# 퍼즐 성공 후 종료
class TracingFootHold_Success(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[120001], skill_id=71001022, level=1, ignore_player=False, is_skill_set=False)
        self.set_effect(trigger_ids=[12100], visible=True) # Success Sound Effect
        self.set_mesh(trigger_ids=[12003], visible=True, fade=1.0) # FootHold03
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001121 걸어서 71001021 제거
        self.set_interact_object(trigger_ids=[12000225], state=1)
        self.set_timer(timer_id='2', seconds=60, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000225], state=0):
            return TracingFootHold_SuccessDelay(self.ctx)
        if self.time_expired(timer_id='2'):
            # 타임 이벤트가 종료했으면
            self.set_interact_object(trigger_ids=[12000225], state=2)
            return ResetTimer(self.ctx)


class TracingFootHold_SuccessDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=12000, key='TimeEventOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ResetTimer(self.ctx)


"""
class TracingFootHold_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return ResetTimer(self.ctx)
"""

# 제한 시간 종료

class TracingFootHold_Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=12201, initial_sequence='Interaction_luminous_A01_on') # Actor_FlowerOn01
        self.set_actor(trigger_id=12202, initial_sequence='Interaction_luminous_A01_on') # Actor_FlowerOn02

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ResetTimer(self.ctx)


class ResetTimer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
