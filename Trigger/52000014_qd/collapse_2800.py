""" trigger/52000014_qd/collapse_2800.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2800,2801,2802,2803], visible=True) # 첫 번째, 위, 4
        self.set_mesh(trigger_ids=[2810,2811,2812,2813,2814,2815], visible=True) # 두 번째, 위, 6
        self.set_mesh(trigger_ids=[2820,2821,2822,2823,2824], visible=True) # 세 번째, 위, 5
        self.set_mesh(trigger_ids=[2830,2831,2832,2833], visible=True) # 네 번째, 위, 4
        self.set_mesh(trigger_ids=[2840,2841,2842,2843], visible=True) # 다섯 번째, 위, 4
        self.set_mesh(trigger_ids=[2850,2851,2852,2853,2854,2855], visible=True) # 첫 번째, 아래, 6
        self.set_mesh(trigger_ids=[2860,2861,2862,2863], visible=True) # 두 번째, 아래, 4
        self.set_mesh(trigger_ids=[2870,2871,2872,2873,2874], visible=True) # 세 번째, 아래, 5
        self.set_mesh(trigger_ids=[2880,2881,2882,2883], visible=True) # 네 번째, 아래, 4
        self.set_mesh(trigger_ids=[2890,2891,2892,2893], visible=True) # 다섯 번째, 아래, 4
        self.set_effect(trigger_ids=[12800]) # Vibrate Short
        self.set_effect(trigger_ids=[22800]) # Vibrate Sound
        self.set_effect(trigger_ids=[12810]) # Vibrate Short
        self.set_effect(trigger_ids=[22810]) # Vibrate Sound
        self.set_effect(trigger_ids=[12820]) # Vibrate Short
        self.set_effect(trigger_ids=[22820]) # Vibrate Sound
        self.set_effect(trigger_ids=[12830]) # Vibrate Short
        self.set_effect(trigger_ids=[22830]) # Vibrate Sound
        self.set_effect(trigger_ids=[12840]) # Vibrate Short
        self.set_effect(trigger_ids=[22840]) # Vibrate Sound
        self.set_effect(trigger_ids=[12850]) # Vibrate Short
        self.set_effect(trigger_ids=[22850]) # Vibrate Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[92800]):
            # 첫 번째
            return 무너짐경고01(self.ctx)


class 무너짐경고01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2800__0$', arg3='4000', arg4='0')
        self.set_effect(trigger_ids=[12800], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22800], visible=True) # Vibrate Sound
        self.set_random_mesh(trigger_ids=[2850,2851,2852,2853,2854,2855], start_delay=6, fade=300) # 첫 번째, 아래, 6

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[92801]):
            # 두 번째
            return 무너짐경고02(self.ctx)


class 무너짐경고02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12810], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22810], visible=True) # Vibrate Sound
        self.set_random_mesh(trigger_ids=[2860,2861,2862,2863], start_delay=4, fade=200) # 두 번째, 아래, 4
        self.set_random_mesh(trigger_ids=[2800,2801,2802,2803], start_delay=4, interval=300, fade=400) # 첫 번째, 위, 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[92802]):
            # 세 번째
            return 무너짐경고03(self.ctx)


class 무너짐경고03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12820], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22820], visible=True) # Vibrate Sound
        self.set_random_mesh(trigger_ids=[2870,2871,2872,2873,2874], start_delay=5, fade=250) # 세 번째, 아래, 5
        self.set_random_mesh(trigger_ids=[2810,2811,2812,2813,2814,2815], start_delay=6, interval=300, fade=200) # 두 번째, 위, 6

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[92803]):
            # 네 번째
            return 무너짐경고04(self.ctx)


class 무너짐경고04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12830], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22830], visible=True) # Vibrate Sound
        self.set_random_mesh(trigger_ids=[2880,2881,2882,2883], start_delay=4, fade=300) # 네 번째, 아래, 4
        self.set_random_mesh(trigger_ids=[2820,2821,2822,2823,2824], start_delay=5, interval=200, fade=300) # 세 번째, 위, 5

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[92804]):
            # 다섯 번째
            return 무너짐경고05(self.ctx)


class 무너짐경고05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12840], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22840], visible=True) # Vibrate Sound
        self.set_random_mesh(trigger_ids=[2890,2891,2892,2893], start_delay=4, fade=200) # 다섯 번째, 아래, 4
        self.set_random_mesh(trigger_ids=[2830,2831,2832,2833], start_delay=4, interval=300, fade=200) # 네 번째, 위, 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            # 도착
            return 무너짐경고06(self.ctx)


class 무너짐경고06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10)
        self.set_effect(trigger_ids=[12850], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22850], visible=True) # Vibrate Sound
        self.set_random_mesh(trigger_ids=[2840,2841,2842,2843], start_delay=4, interval=100, fade=150) # 다섯 번째, 위, 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12800]) # Vibrate Short
        self.set_effect(trigger_ids=[22800]) # Vibrate Sound
        self.set_effect(trigger_ids=[12810]) # Vibrate Short
        self.set_effect(trigger_ids=[22810]) # Vibrate Sound
        self.set_effect(trigger_ids=[12820]) # Vibrate Short
        self.set_effect(trigger_ids=[22820]) # Vibrate Sound
        self.set_effect(trigger_ids=[12830]) # Vibrate Short
        self.set_effect(trigger_ids=[22830]) # Vibrate Sound
        self.set_effect(trigger_ids=[12840]) # Vibrate Short
        self.set_effect(trigger_ids=[22840]) # Vibrate Sound
        self.set_effect(trigger_ids=[12850]) # Vibrate Short
        self.set_effect(trigger_ids=[22850]) # Vibrate Sound


initial_state = 대기
