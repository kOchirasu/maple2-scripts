""" trigger/02000299_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005])
        self.spawn_monster(spawn_ids=[1010,1011,1012,1013])
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Closed_A')
        self.set_interact_object(trigger_ids=[10000494,10000495,10000496,10000497,10000498,10000499], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 클리어체크(self.ctx)


class 클리어체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601]) # Eff_dungeon_allert_01
        # 진동
        # Eff_Sound_Dungeon_Object_Scifi_Door_Open
        self.set_effect(trigger_ids=[602])
        # Eff_Sound_Dungeon_Object_Scifi_Door_Open
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604]) # Eff_UI_Sound_notice_01
        # Eff_sf_fi_prop_incubator_B02_wfx_Big
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[606]) # Eff_electricity
        self.set_effect(trigger_ids=[607]) # Eff_electricity
        self.set_effect(trigger_ids=[610]) # Eff_Sound_RedAllert

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 클리어체크2(self.ctx)


class 클리어체크2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005], fade=5.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1010]):
            return 타임머신중지(self.ctx)
        if self.monster_dead(spawn_ids=[1011]):
            return 타임머신중지(self.ctx)
        if self.monster_dead(spawn_ids=[1012]):
            return 타임머신중지(self.ctx)
        if self.monster_dead(spawn_ids=[1013]):
            return 타임머신중지(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 정황설명(self.ctx)


class 정황설명(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002990, text_id=20002990, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 시간반응대기(self.ctx)


class 시간반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002992, text_id=20002992, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(trigger_ids=[10000494,10000495], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000494], state=0):
            return 미래시간(self.ctx)
        if self.object_interacted(interact_ids=[10000495], state=0):
            return 과거시간(self.ctx)


class 미래시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_guide_summary(entity_id=20002987, text_id=20002987)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(trigger_ids=[10000495], state=0)
        self.set_interact_object(trigger_ids=[10000496,10000497,10000498,10000499], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000496], state=0):
            return 그런거없음(self.ctx)
        if self.object_interacted(interact_ids=[10000497], state=0):
            return 미래엘리니아(self.ctx)
        if self.object_interacted(interact_ids=[10000498], state=0):
            return 그런거없음(self.ctx)
        if self.object_interacted(interact_ids=[10000499], state=0):
            return 미래커닝시티(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20002987)
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_interact_object(trigger_ids=[10000496,10000497,10000498,10000499], state=0)


class 과거시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_guide_summary(entity_id=20002988, text_id=20002988)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(trigger_ids=[10000494], state=0)
        self.set_interact_object(trigger_ids=[10000496,10000497,10000498,10000499], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000496], state=0):
            return 과거헤네니스(self.ctx)
        if self.object_interacted(interact_ids=[10000497], state=0):
            return 그런거없음(self.ctx)
        if self.object_interacted(interact_ids=[10000498], state=0):
            return 과거페리온(self.ctx)
        if self.object_interacted(interact_ids=[10000499], state=0):
            return 그런거없음(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20002988)
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_interact_object(trigger_ids=[10000496,10000497,10000498,10000499], state=0)


class 미래엘리니아(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_guide_summary(entity_id=20002989, text_id=20002989)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.hide_guide_summary(entity_id=20002989)
            return 미래엘리니아2(self.ctx)


class 미래엘리니아2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000299, portal_id=2, box_id=104)
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Opened_A')
        self.show_count_ui(text='$02000299_BF__MAIN__3$', stage=1, count=3)
        self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 미래엘리니아이동(self.ctx)


class 미래엘리니아이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Closed_A')
        self.set_effect(trigger_ids=[605], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.move_user(map_id=2000302, portal_id=1, box_id=104)
            self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 클리어체크(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1010])
        self.set_effect(trigger_ids=[603])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005], visible=True, fade=5.0)


class 미래커닝시티(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_guide_summary(entity_id=20002989, text_id=20002989)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.hide_guide_summary(entity_id=20002989)
            return 미래커닝시티2(self.ctx)


class 미래커닝시티2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000299, portal_id=2, box_id=104)
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Opened_A')
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_count_ui(text='$02000299_BF__MAIN__5$', stage=1, count=3)
        self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 미래커닝시티이동(self.ctx)


class 미래커닝시티이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Closed_A')
        self.set_effect(trigger_ids=[605], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.move_user(map_id=2000301, portal_id=1, box_id=104)
            self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 클리어체크(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1011])
        self.set_effect(trigger_ids=[603])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005], visible=True, fade=5.0)


class 과거헤네니스(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_guide_summary(entity_id=20002989, text_id=20002989)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.hide_guide_summary(entity_id=20002989)
            return 과거헤네니스2(self.ctx)


class 과거헤네니스2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000299, portal_id=2, box_id=104)
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Opened_A')
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_count_ui(text='$02000299_BF__MAIN__7$', stage=1, count=3)
        self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 과거헤네니스이동(self.ctx)


class 과거헤네니스이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Closed_A')
        self.set_effect(trigger_ids=[605], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.move_user(map_id=2000303, portal_id=1, box_id=104)
            self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 클리어체크(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1012])
        self.set_effect(trigger_ids=[603])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005], visible=True, fade=5.0)


class 과거페리온(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_guide_summary(entity_id=20002989, text_id=20002989)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.hide_guide_summary(entity_id=20002989)
            return 과거페리온2(self.ctx)


class 과거페리온2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000299, portal_id=2, box_id=104)
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Opened_A')
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_count_ui(text='$02000299_BF__MAIN__9$', stage=1, count=3)
        self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 과거페리온이동(self.ctx)


class 과거페리온이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Closed_A')
        self.set_effect(trigger_ids=[605], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.move_user(map_id=2000300, portal_id=1, box_id=104)
            self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 클리어체크(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1013])
        self.set_effect(trigger_ids=[603])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005], visible=True, fade=5.0)


class 그런거없음(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[604], visible=True)
        self.show_guide_summary(entity_id=20002989, text_id=20002989)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.hide_guide_summary(entity_id=20002989)
            return 그런거없음2(self.ctx)


class 그런거없음2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606])
        self.set_effect(trigger_ids=[607])
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_timer(timer_id='4', seconds=4)
        self.show_guide_summary(entity_id=20002994, text_id=20002994)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            self.hide_guide_summary(entity_id=20002994)
            return 방어모드(self.ctx)


class 방어모드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.show_guide_summary(entity_id=20002995, text_id=20002995)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1001,1002,1003,1004]):
            self.hide_guide_summary(entity_id=20002995)
            self.set_effect(trigger_ids=[610])
            self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_Off')
            self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_Off')
            return 방어모드종료(self.ctx)


class 방어모드종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002996, text_id=20002996)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.hide_guide_summary(entity_id=20002996)
            return 시간반응대기(self.ctx)


class 타임머신중지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 보스방이동준비(self.ctx)


class 보스방이동준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.show_guide_summary(entity_id=20002997, text_id=20002997)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_effect(trigger_ids=[605], visible=True)
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_actor(trigger_id=290, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=291, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=292, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=293, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=294, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=295, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=296, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=297, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=298, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=299, visible=True, initial_sequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.hide_guide_summary(entity_id=20002997)
            return 보스방이동(self.ctx)


class 보스방이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=4)
        self.set_effect(trigger_ids=[603], visible=True)
        self.show_count_ui(text='$02000299_BF__MAIN__15$', stage=1, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            self.move_user(map_id=2000304, portal_id=1)
            return 반복체크(self.ctx)


class 반복체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_effect(trigger_ids=[603], visible=True)
        self.show_guide_summary(entity_id=20002997, text_id=20002997)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.hide_guide_summary(entity_id=20002997)
            return 보스방이동(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
