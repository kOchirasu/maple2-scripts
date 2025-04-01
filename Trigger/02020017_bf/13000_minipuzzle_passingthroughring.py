""" trigger/02020017_bf/13000_minipuzzle_passingthroughring.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='10')
        self.set_mesh(trigger_ids=[13001]) # off_01
        self.set_mesh(trigger_ids=[13011]) # on_01
        self.set_mesh(trigger_ids=[13002]) # off_02
        self.set_mesh(trigger_ids=[13012]) # on_02
        self.set_mesh(trigger_ids=[13003]) # off_03
        self.set_mesh(trigger_ids=[13013]) # on_03
        self.set_mesh_animation(trigger_ids=[13011]) # on_01
        self.set_mesh_animation(trigger_ids=[13012]) # on_02
        self.set_mesh_animation(trigger_ids=[13013]) # on_03
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001131 걸어서 71001031 제거
        self.set_interact_object(trigger_ids=[12000232], state=2)
        # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001031 부여
        self.set_interact_object(trigger_ids=[12000076], state=2)
        self.set_effect(trigger_ids=[13101]) # Right Sound Effect
        self.set_effect(trigger_ids=[13102]) # Right Sound Effect
        self.set_effect(trigger_ids=[13103]) # Right Sound Effect
        self.set_effect(trigger_ids=[13200]) # Success Sound Effect
        self.set_mesh(trigger_ids=[13300]) # Final_FootHold

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimeEventOn') == 1:
            return SettingDelay(self.ctx)


class SettingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Setting(self.ctx)
        if self.user_value(key='EventStart') == 0:
            return Wait(self.ctx)


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001031 부여
        self.set_interact_object(trigger_ids=[12000076], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000076], state=0):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001031 지속시간 동일
            self.set_timer(timer_id='1', seconds=120, auto_remove=True)
            return PassingThroughRing_Start_Delay(self.ctx)
        if self.user_value(key='TimeEventOn') == 0:
            return Wait(self.ctx)


class PassingThroughRing_Start_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PassingThroughRing_Play01(self.ctx)


class PassingThroughRing_Play01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[13001], visible=True, fade=1.0) # off_01

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_any_user_additional_effect(box_id=13401, additional_effect_id=71001031, level=1):
            return PassingThroughRing_Play01_Delay(self.ctx)
        if self.time_expired(timer_id='1'):
            # 제한 시간 종료
            return PassingThroughRing_Fail(self.ctx)


class PassingThroughRing_Play01_Delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[13001], start_delay=1, fade=1.0) # off_01
        self.set_mesh(trigger_ids=[13011], visible=True, fade=1.0) # on_01
        self.set_mesh_animation(trigger_ids=[13011], visible=True) # on_01
        self.set_effect(trigger_ids=[13101], visible=True) # Right Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PassingThroughRing_Play02(self.ctx)
        if self.time_expired(timer_id='1'):
            # 제한 시간 종료
            return PassingThroughRing_Fail(self.ctx)


class PassingThroughRing_Play02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[13002], visible=True, fade=1.0) # off_02

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_any_user_additional_effect(box_id=13402, additional_effect_id=71001031, level=1):
            return PassingThroughRing_Play02_Delay(self.ctx)
        if self.time_expired(timer_id='1'):
            # 제한 시간 종료
            return PassingThroughRing_Fail(self.ctx)


class PassingThroughRing_Play02_Delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[13002], start_delay=1, fade=1.0) # off_02
        self.set_mesh(trigger_ids=[13012], visible=True, fade=1.0) # on_02
        self.set_mesh_animation(trigger_ids=[13012], visible=True) # on_02
        self.set_effect(trigger_ids=[13102], visible=True) # Right Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PassingThroughRing_Play03(self.ctx)
        if self.time_expired(timer_id='1'):
            # 제한 시간 종료
            return PassingThroughRing_Fail(self.ctx)


class PassingThroughRing_Play03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[13003], visible=True, fade=1.0) # off_03

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_any_user_additional_effect(box_id=13403, additional_effect_id=71001031, level=1):
            return PassingThroughRing_Play03_Delay(self.ctx)
        if self.time_expired(timer_id='1'):
            # 제한 시간 종료
            return PassingThroughRing_Fail(self.ctx)


class PassingThroughRing_Play03_Delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[13003], start_delay=1, fade=1.0) # off_03
        self.set_mesh(trigger_ids=[13013], visible=True, fade=1.0) # on_03
        self.set_mesh_animation(trigger_ids=[13013], visible=True) # on_03
        self.set_effect(trigger_ids=[13103], visible=True) # Right Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PassingThroughRing_Success(self.ctx)


# 퍼즐 성공 후 종료
class PassingThroughRing_Success(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[130001], skill_id=71001032, level=1, ignore_player=False, is_skill_set=False)
        # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001031 지속시간 동일
        self.set_timer(timer_id='10', seconds=61, auto_remove=True)
        self.set_effect(trigger_ids=[13200], visible=True) # Success Sound Effect
        self.set_mesh(trigger_ids=[13300], visible=True) # Final_FootHold
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001131 걸어서 71001031 제거
        self.set_interact_object(trigger_ids=[12000232], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000232], state=0):
            return PassingThroughRing_SuccessDelay(self.ctx)
        if self.time_expired(timer_id='10'):
            return ResetTimer(self.ctx)


class PassingThroughRing_SuccessDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=13000, key='TimeEventOn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ResetTimer(self.ctx)


"""
class PassingThroughRing_End(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return ResetTimer(self.ctx)
"""

# 제한 시간 종료

class PassingThroughRing_Fail(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.reset_timer(timer_id='1')
            self.reset_timer(timer_id='10')
            return Wait(self.ctx)


class ResetTimer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='10')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
