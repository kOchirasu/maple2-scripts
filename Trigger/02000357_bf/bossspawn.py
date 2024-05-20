""" trigger/02000357_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[99], auto_target=False)
        self.set_skip(state=종료체크)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 종료체크(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(trigger_id=301, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 종료체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20001945, text_id=20001945, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=102, type='trigger', achieve='ClearPP')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = 시작대기중
