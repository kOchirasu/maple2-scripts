""" trigger/02000284_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000428], state=2)
        self.set_interact_object(trigger_ids=[10000430], state=2)
        self.set_interact_object(trigger_ids=[10000431], state=2)
        self.set_interact_object(trigger_ids=[10000432], state=2)
        self.set_interact_object(trigger_ids=[10000433], state=2)
        self.set_portal(portal_id=1)
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 보스연출(self.ctx)


class 보스연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.select_camera(trigger_id=3001)
        self.set_skip(state=준비)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 준비(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=3001, enable=False)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002815, text_id=20002815, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            # self.set_interact_object(trigger_ids=[10000430], state=1)
            # self.set_interact_object(trigger_ids=[10000431], state=1)
            # self.set_interact_object(trigger_ids=[10000432], state=1)
            # self.set_interact_object(trigger_ids=[10000433], state=1)
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.set_interact_object(trigger_ids=[10000428], state=1)
            self.show_guide_summary(entity_id=20002814, text_id=20002814)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            return 반응체크(self.ctx)


class 반응체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000428], state=0):
            self.hide_guide_summary(entity_id=20002814)
            self.dungeon_clear()
            self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308], visible=True, interval=100)
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    pass


initial_state = 대기
