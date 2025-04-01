""" trigger/02020016_bf/14000_minipuzzle_touchinginorder.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='10')
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001141 걸어서 71001041 제거
        self.set_interact_object(trigger_ids=[12000243], state=2)
        # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001041 부여
        self.set_interact_object(trigger_ids=[12000077], state=2)
        self.set_interact_object(trigger_ids=[12000088], state=0) # CheckPosition_Tree01
        self.set_interact_object(trigger_ids=[12000089], state=0) # CheckPosition_Tree02
        self.set_interact_object(trigger_ids=[12000090], state=0) # CheckPosition_Tree03
        self.set_interact_object(trigger_ids=[12000091], state=0) # CheckPosition_Tree04
        self.set_interact_object(trigger_ids=[12000092], state=0) # CheckPosition_Tree05
        self.set_actor(trigger_id=14011, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree01
        self.set_actor(trigger_id=14021, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree02
        self.set_actor(trigger_id=14022, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree02
        self.set_actor(trigger_id=14031, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree03
        self.set_actor(trigger_id=14032, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree03
        self.set_actor(trigger_id=14033, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree03
        self.set_actor(trigger_id=14041, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree04
        self.set_actor(trigger_id=14042, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree04
        self.set_actor(trigger_id=14043, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(trigger_id=14044, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(trigger_id=14051, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree05
        self.set_actor(trigger_id=14052, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree05
        self.set_actor(trigger_id=14053, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree05
        self.set_actor(trigger_id=14054, initial_sequence='Interaction_luminous_A02_off') # Flower04_Of_Tree05
        self.set_actor(trigger_id=14055, initial_sequence='Interaction_luminous_A02_off') # Flower05_Of_Tree05
        self.set_effect(trigger_ids=[14200]) # Success Sound Effect
        self.set_effect(trigger_ids=[14201]) # Right Sound Effect
        self.set_effect(trigger_ids=[14202]) # Wrong Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimeEventOn') == 1:
            return SettingDelay(self.ctx)


class SettingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Setting(self.ctx)
        if self.user_value(key='TimeEventOn') == 0:
            return Wait(self.ctx)


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001041 부여
        self.set_interact_object(trigger_ids=[12000077], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000077], state=0):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001041 지속시간 동일
            self.set_timer(timer_id='1', seconds=120, auto_remove=True)
            return TouchingInNumericalOrder_Start_Delay(self.ctx)
        if self.user_value(key='TimeEventOn') == 0:
            return Wait(self.ctx)


class TouchingInNumericalOrder_Start_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TouchingInNumericalOrder_Play01(self.ctx)


class TouchingInNumericalOrder_Play01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[14201], visible=True) # Right Sound Effect
        self.set_interact_object(trigger_ids=[12000088], state=1) # CheckPosition_Tree01
        self.set_interact_object(trigger_ids=[12000089], state=1) # CheckPosition_Tree02
        self.set_interact_object(trigger_ids=[12000090], state=1) # CheckPosition_Tree03
        self.set_interact_object(trigger_ids=[12000091], state=1) # CheckPosition_Tree04
        self.set_interact_object(trigger_ids=[12000092], state=1) # CheckPosition_Tree05
        self.set_actor(trigger_id=14011, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree01
        self.set_actor(trigger_id=14021, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree02
        self.set_actor(trigger_id=14022, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree02
        self.set_actor(trigger_id=14031, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree03
        self.set_actor(trigger_id=14032, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree03
        self.set_actor(trigger_id=14033, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree03
        self.set_actor(trigger_id=14041, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree04
        self.set_actor(trigger_id=14042, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree04
        self.set_actor(trigger_id=14043, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(trigger_id=14044, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(trigger_id=14051, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree05
        self.set_actor(trigger_id=14052, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree05
        self.set_actor(trigger_id=14053, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree05
        self.set_actor(trigger_id=14054, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower04_Of_Tree05
        self.set_actor(trigger_id=14055, visible=True, initial_sequence='Interaction_luminous_A02_off') # Flower05_Of_Tree05

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return ResetTimer(self.ctx)
        if self.object_interacted(interact_ids=[12000088], state=0):
            return TouchingInNumericalOrder_Play02(self.ctx)
        if self.object_interacted(interact_ids=[12000089], state=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interact_ids=[12000090], state=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interact_ids=[12000091], state=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interact_ids=[12000092], state=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)


class TouchingInNumericalOrder_Play02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000088], state=0) # CheckPosition_Tree01
        self.set_effect(trigger_ids=[14201], visible=True) # Right Sound Effect
        self.set_actor(trigger_id=14011, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower01_Of_Tree01

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return ResetTimer(self.ctx)
        if self.object_interacted(interact_ids=[12000089], state=0):
            return TouchingInNumericalOrder_Play03(self.ctx)
        if self.object_interacted(interact_ids=[12000090], state=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interact_ids=[12000091], state=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interact_ids=[12000092], state=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)


class TouchingInNumericalOrder_Play03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000089], state=0) # CheckPosition_Tree02
        self.set_effect(trigger_ids=[14201], visible=True) # Right Sound Effect
        self.set_actor(trigger_id=14021, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower01_Of_Tree02
        self.set_actor(trigger_id=14022, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower02_Of_Tree02

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return ResetTimer(self.ctx)
        if self.object_interacted(interact_ids=[12000090], state=0):
            return TouchingInNumericalOrder_Play04(self.ctx)
        if self.object_interacted(interact_ids=[12000091], state=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)
        if self.object_interacted(interact_ids=[12000092], state=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)


class TouchingInNumericalOrder_Play04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000090], state=0) # CheckPosition_Tree03
        self.set_effect(trigger_ids=[14201], visible=True) # Right Sound Effect
        self.set_actor(trigger_id=14031, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower01_Of_Tree03
        self.set_actor(trigger_id=14032, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower02_Of_Tree03
        self.set_actor(trigger_id=14033, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower03_Of_Tree03

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return ResetTimer(self.ctx)
        if self.object_interacted(interact_ids=[12000091], state=0):
            return TouchingInNumericalOrder_Play05(self.ctx)
        if self.object_interacted(interact_ids=[12000092], state=0):
            return TouchingInNumericalOrder_FailDelay(self.ctx)


class TouchingInNumericalOrder_Play05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000091], state=0) # CheckPosition_Tree04
        self.set_effect(trigger_ids=[14201], visible=True) # Right Sound Effect
        self.set_actor(trigger_id=14041, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower01_Of_Tree04
        self.set_actor(trigger_id=14042, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower02_Of_Tree04
        self.set_actor(trigger_id=14043, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower03_Of_Tree04
        self.set_actor(trigger_id=14044, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower03_Of_Tree04

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return ResetTimer(self.ctx)
        if self.object_interacted(interact_ids=[12000092], state=0):
            return TouchingInNumericalOrder_End(self.ctx)


class TouchingInNumericalOrder_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000092], state=0) # CheckPosition_Tree05
        self.set_effect(trigger_ids=[14201], visible=True) # Right Sound Effect
        self.set_actor(trigger_id=14051, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower01_Of_Tree05
        self.set_actor(trigger_id=14052, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower02_Of_Tree05
        self.set_actor(trigger_id=14053, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower03_Of_Tree05
        self.set_actor(trigger_id=14054, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower04_Of_Tree05
        self.set_actor(trigger_id=14055, visible=True, initial_sequence='Interaction_luminous_A02_on') # Flower05_Of_Tree05

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TouchingInNumericalOrder_Success(self.ctx)


# 퍼즐 성공 후 종료
class TouchingInNumericalOrder_Success(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=61, auto_remove=True)
        self.add_buff(box_ids=[140001], skill_id=71001042, level=1, ignore_player=False, is_skill_set=False)
        self.set_effect(trigger_ids=[14200], visible=True) # Success Sound Effect
        # RareBox / 기믹 종료 오브젝트 / Additional Effect 71001141 걸어서 71001041 제거
        self.set_interact_object(trigger_ids=[12000243], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000243], state=0):
            return TouchingInNumericalOrder_SuccessDelay(self.ctx)
        if self.time_expired(timer_id='10'):
            return ResetTimer(self.ctx)


class TouchingInNumericalOrder_SuccessDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TouchingInNumericalOrder_Quit(self.ctx)


class TouchingInNumericalOrder_Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=14000, key='TimeEventOn', value=0)
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='10')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


# 오답 터치
class TouchingInNumericalOrder_FailDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[14202], visible=True) # Wrong Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TouchingInNumericalOrder_Fail(self.ctx)
        if self.time_expired(timer_id='1'):
            return ResetTimer(self.ctx)
        if self.user_value(key='TimeEventOn') == 0:
            return ResetTimer(self.ctx)


class TouchingInNumericalOrder_Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000088], state=0) # CheckPosition_Tree01
        self.set_interact_object(trigger_ids=[12000089], state=0) # CheckPosition_Tree02
        self.set_interact_object(trigger_ids=[12000090], state=0) # CheckPosition_Tree03
        self.set_interact_object(trigger_ids=[12000091], state=0) # CheckPosition_Tree04
        self.set_interact_object(trigger_ids=[12000092], state=0) # CheckPosition_Tree05
        self.set_actor(trigger_id=14011, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree01
        self.set_actor(trigger_id=14021, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree02
        self.set_actor(trigger_id=14022, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree02
        self.set_actor(trigger_id=14031, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree03
        self.set_actor(trigger_id=14032, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree03
        self.set_actor(trigger_id=14033, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree03
        self.set_actor(trigger_id=14041, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree04
        self.set_actor(trigger_id=14042, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree04
        self.set_actor(trigger_id=14043, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(trigger_id=14044, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree04
        self.set_actor(trigger_id=14051, initial_sequence='Interaction_luminous_A02_off') # Flower01_Of_Tree05
        self.set_actor(trigger_id=14052, initial_sequence='Interaction_luminous_A02_off') # Flower02_Of_Tree05
        self.set_actor(trigger_id=14053, initial_sequence='Interaction_luminous_A02_off') # Flower03_Of_Tree05
        self.set_actor(trigger_id=14054, initial_sequence='Interaction_luminous_A02_off') # Flower04_Of_Tree05
        self.set_actor(trigger_id=14055, initial_sequence='Interaction_luminous_A02_off') # Flower05_Of_Tree05

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TouchingInNumericalOrder_Play01(self.ctx)
        if self.time_expired(timer_id='1'):
            # 타임 이벤트가 종료했으면
            return ResetTimer(self.ctx)
        if self.user_value(key='TimeEventOn') == 0:
            return ResetTimer(self.ctx)


class ResetTimer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
