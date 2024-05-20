""" trigger/02000328_bf/event1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999998]):
            return 진행1(self.ctx)


class 진행1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 진행2(self.ctx)


class 진행2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1101,1102,1103,1104,1105]):
            return 진행3(self.ctx)


class 진행3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1,2], visible=True, start_delay=100, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[3,4,5,6], visible=True, start_delay=200, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[7,8,9,10,11,12], visible=True, start_delay=300, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[13,14,15,16,17,18,19,20], visible=True, start_delay=400, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[21,22,23,24,25,26,27,28,29,30], visible=True, start_delay=500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[31,32,33,34,35,36,37,38,39,40,41,42], visible=True, start_delay=600, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[43,44,45,46,47,48,49,50,51,52,53,54], visible=True, start_delay=700, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[55,56,57,58,59,60,61,62,63,64], visible=True, start_delay=800, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[65,66,67,68,69,70,71,72], visible=True, start_delay=900, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[73,74,75,76], visible=True, start_delay=1000, interval=50, fade=2.0)
        self.show_guide_summary(entity_id=20003281, text_id=20003281)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_timer(timer_id='100', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='100'):
            return 종료2(self.ctx)


class 종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20003281)


initial_state = 대기
