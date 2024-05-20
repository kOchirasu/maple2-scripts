""" trigger/02000304_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, initial_sequence='Closed_A')
        self.set_actor(trigger_id=202, initial_sequence='Closed_A')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='sf_functobj_monitor_C01_On')
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_portal(portal_id=98)
        self.set_portal(portal_id=99)
        self.set_interact_object(trigger_ids=[10000646], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            self.spawn_monster(spawn_ids=[2001], auto_target=False)
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 카메라이동대기(self.ctx)


class 카메라이동대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 전투시작대기(self.ctx)


class 전투시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003041, text_id=20003041, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[2001]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2001, script='$02000304_BF__MAIN__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            self.set_actor(trigger_id=203, initial_sequence='sf_functobj_monitor_C01_On')
            self.set_interact_object(trigger_ids=[10000646], state=1)
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603], visible=True)
        self.show_guide_summary(entity_id=20003003, text_id=20003003)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000646], state=0):
            self.hide_guide_summary(entity_id=20003003)
            self.set_effect(trigger_ids=[603])
            self.set_effect(trigger_ids=[602], visible=True)
            self.set_achievement(trigger_id=999, type='trigger', achieve='ClearTimehole')
            return 미션성공(self.ctx)


class 미션성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.show_guide_summary(entity_id=20003004, text_id=20003004)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Closed_A')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='Closed_A')
        self.set_portal(portal_id=99, enable=True, minimap_visible=True)
        self.set_portal(portal_id=98, enable=True, minimap_visible=True)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            # self.hide_guide_summary(entity_id=20003004)
            return 종료2(self.ctx)


class 종료2(trigger_api.Trigger):
    pass


initial_state = 대기
