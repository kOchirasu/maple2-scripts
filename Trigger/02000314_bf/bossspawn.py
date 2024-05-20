""" trigger/02000314_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=12)
        self.set_portal(portal_id=13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003140, text_id=20003140, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.select_camera(trigger_id=301)
        self.add_buff(box_ids=[102], skill_id=70000107, level=1, is_player=False, is_skill_set=False)
        self.spawn_monster(spawn_ids=[99], auto_target=False)
        self.set_skip(state=종료체크)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 종료체크(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(trigger_id=301, enable=False)
        self.remove_buff(box_id=102, skill_id=70000107)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=12, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13, visible=True, enable=True, minimap_visible=True)


initial_state = 시작대기중
