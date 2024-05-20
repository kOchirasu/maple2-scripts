""" trigger/52000014_qd/collapse_2900.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[2900,2901,2902,2903,2904,2905], visible=True)
        self.set_effect(trigger_ids=[12900]) # Vibrate Short
        self.set_effect(trigger_ids=[22900]) # Vibrate Sound
        self.set_effect(trigger_ids=[12901]) # Vibrate Short
        self.set_effect(trigger_ids=[22901]) # Vibrate Sound
        self.set_effect(trigger_ids=[12902]) # Vibrate Short
        self.set_effect(trigger_ids=[22902]) # Vibrate Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 로딩딜레이(self.ctx)


class 로딩딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 무너짐01(self.ctx)


class 무너짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='2', seconds=2)
        self.set_effect(trigger_ids=[12900], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22900], visible=True) # Vibrate Sound
        self.set_random_mesh(trigger_ids=[2900,2901,2902,2903,2904,2905], start_delay=6, interval=100, fade=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 카메라연출01(self.ctx)


class 카메라연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=2)
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 카메라연출02(self.ctx)


class 카메라연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000014_QD__COLLAPSE_2900__0$')
        self.set_skip(state=카메라연출03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 카메라연출03(self.ctx)


class 카메라연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=3)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=601, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 무너짐02(self.ctx)


class 무너짐02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2900__1$', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return 무너짐03(self.ctx)


class 무너짐03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=5)
        self.set_effect(trigger_ids=[12901], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22901], visible=True) # Vibrate Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 무너짐04(self.ctx)


class 무너짐04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 무너짐05(self.ctx)


class 무너짐05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            return 반응안내01(self.ctx)


class 반응안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=4)
        self.set_effect(trigger_ids=[12902], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22902], visible=True) # Vibrate Sound
        self.set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2900__2$', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 줍기안내01(self.ctx)


class 줍기안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2900__3$', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001250], quest_states=[2]):
            # Knight
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001251], quest_states=[2]):
            # Beginer
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001252], quest_states=[2]):
            # Berserker
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001253], quest_states=[2]):
            # Wizard
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001254], quest_states=[2]):
            # Priest
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001255], quest_states=[2]):
            # Ranger
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001256], quest_states=[2]):
            # HeavyGunner
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001257], quest_states=[2]):
            # Thief
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001258], quest_states=[2]):
            # Assassin
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001259], quest_states=[2]):
            # RuneBlader
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001370], quest_states=[2]):
            # Striker
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001371], quest_states=[2]): # 완료 유저
            # Soulbinder
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001250], quest_states=[3]):
            # Knight
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001251], quest_states=[3]):
            # Beginer
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001252], quest_states=[3]):
            # Berserker
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001253], quest_states=[3]):
            # Wizard
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001254], quest_states=[3]):
            # Priest
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001255], quest_states=[3]):
            # Ranger
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001256], quest_states=[3]):
            # HeavyGunner
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001257], quest_states=[3]):
            # Thief
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001258], quest_states=[3]):
            # Assassin
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001259], quest_states=[3]):
            # RuneBlader
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001370], quest_states=[3]):
            # Striker
            return 포털생성01(self.ctx)
        if self.quest_user_detected(box_ids=[9004], quest_ids=[50001371], quest_states=[3]):
            # Soulbinder
            return 포털생성01(self.ctx)


class 포털생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12900]) # Vibrate Short
        self.set_effect(trigger_ids=[22900]) # Vibrate Sound
        self.set_effect(trigger_ids=[12901]) # Vibrate Short
        self.set_effect(trigger_ids=[22901]) # Vibrate Sound
        self.set_effect(trigger_ids=[12902]) # Vibrate Short
        self.set_effect(trigger_ids=[22902]) # Vibrate Sound


initial_state = 대기
