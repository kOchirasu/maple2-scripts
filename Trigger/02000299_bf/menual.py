""" trigger/02000299_bf/menual.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604])
        self.set_interact_object(trigger_ids=[10000490], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000490], state=0):
            return 안내시작(self.ctx)


class 안내시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        self.select_camera(trigger_id=301)
        self.add_buff(box_ids=[104], skill_id=70000107, level=1, is_player=False, is_skill_set=False)
        self.show_guide_summary(entity_id=20003011, text_id=20003011, duration=2500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 안내01(self.ctx)


class 안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_guide_summary(entity_id=20003012, text_id=20003012, duration=3000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 안내02(self.ctx)


class 안내02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        self.select_camera(trigger_id=302)
        self.show_guide_summary(entity_id=20003013, text_id=20003013, duration=3000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 안내03(self.ctx)


class 안내03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        self.select_camera(trigger_id=303)
        self.set_interact_object(trigger_ids=[10000496,10000497,10000498,10000499], state=1)
        self.show_guide_summary(entity_id=20003014, text_id=20003014, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 안내04(self.ctx)


class 안내04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[104], skill_id=70000107, level=1, is_player=False, is_skill_set=False)
        self.set_interact_object(trigger_ids=[10000496,10000497,10000498,10000499], state=0)
        self.set_effect(trigger_ids=[604], visible=True)
        self.select_camera(trigger_id=301)
        self.show_guide_summary(entity_id=20003015, text_id=20003015, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 안내05(self.ctx)


class 안내05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=104, skill_id=70000107)
        self.set_effect(trigger_ids=[604], visible=True)
        self.select_camera(trigger_id=303, enable=False)
        self.show_guide_summary(entity_id=20003016, text_id=20003016, duration=2000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 대기(self.ctx)


initial_state = 대기
