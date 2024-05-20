""" trigger/02000328_bf/event2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101])

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
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1201,1202,1203,1204,1205]):
            return 진행3(self.ctx)


class 진행3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101,102], visible=True, start_delay=100, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[103,104,105,106], visible=True, start_delay=200, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[107,108,109,110,111,112], visible=True, start_delay=300, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[113,114,115,116,117,118,119,120], visible=True, start_delay=400, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[121,122,123,124,125,126,127,128,129,130], visible=True, start_delay=500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[131,132,133,134,135,136,137,138,139,140,141,142], visible=True, start_delay=600, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[143,144,145,146,147,148,149,150,151,152,153,154], visible=True, start_delay=700, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[155,156,157,158,159,160,161,162,163,164], visible=True, start_delay=800, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[165,166,167,168,169,170,171,172], visible=True, start_delay=900, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[173,174,175,176], visible=True, start_delay=1000, interval=50, fade=2.0)
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
