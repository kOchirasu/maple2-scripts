""" trigger/02000328_bf/event3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[201])

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
        self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1301,1302,1303,1304,1305]):
            return 진행3(self.ctx)


class 진행3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[201,202], visible=True, start_delay=100, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[203,204,205,206], visible=True, start_delay=200, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[207,208,209,210,211,212], visible=True, start_delay=300, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[213,214,215,216,217,218,219,220], visible=True, start_delay=400, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[221,222,223,224,225,226,227,228,229,230], visible=True, start_delay=500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[231,232,233,234,235,236,237,238,239,240,241,242], visible=True, start_delay=600, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[243,244,245,246,247,248,249,250,251,252,253,254], visible=True, start_delay=700, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[255,256,257,258,259,260,261,262,263,264], visible=True, start_delay=800, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[265,266,267,268,269,270,271,272], visible=True, start_delay=900, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[273,274,275,276], visible=True, start_delay=1000, interval=50, fade=2.0)
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
