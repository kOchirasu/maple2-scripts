""" trigger/02000328_bf/event4.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301])

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
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1401,1402,1403,1404,1405]):
            return 진행3(self.ctx)


class 진행3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301,302], visible=True, start_delay=100, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[303,304,305,306], visible=True, start_delay=200, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[307,308,309,310,311,312], visible=True, start_delay=300, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[313,314,315,316,317,318,319,320], visible=True, start_delay=400, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[321,322,323,324,325,326,327,328,329,330], visible=True, start_delay=500, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[331,332,333,334,335,336,337,338,339,340,341,342], visible=True, start_delay=600, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[343,344,345,346,347,348,349,350,351,352,353,354], visible=True, start_delay=700, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[355,356,357,358,359,360,361,362,363,364], visible=True, start_delay=800, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[365,366,367,368,369,370,371,372], visible=True, start_delay=900, interval=50, fade=2.0)
        self.set_mesh(trigger_ids=[373,374,375,376], visible=True, start_delay=1000, interval=50, fade=2.0)
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
