""" trigger/02000329_bf/bossbattle_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[611])
        self.set_interact_object(trigger_ids=[10000759], state=2)
        self.set_portal(portal_id=2)
        self.set_actor(trigger_id=211, visible=True, initial_sequence='Closed')
        self.spawn_monster(spawn_ids=[1011,1012,1013,1014,1015,1016,1017,1018], auto_target=False)
        self.set_effect(trigger_ids=[6811])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[5001]):
            return 보스소환(self.ctx)
        if self.monster_dead(spawn_ids=[5001,5002]):
            return 닭장열기(self.ctx)


class 보스소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=109, text_id=20000070) # 보스를 처치하세요!
        # self.set_cinematic_ui(type=1)
        # self.set_cinematic_ui(type=3, script='$02000329_BF__BOSSBATTLE_01__0$')
        # self.set_timer(timer_id='3', seconds=3)
        self.set_skip(state=보스전투시작)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[5001,5002]):
            return 닭장열기(self.ctx)
        if self.time_expired(timer_id='3'):
            return 보스전투시작(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 보스전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[5001,5002]):
            return 닭장열기(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=109)


class 닭장열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[611], visible=True)
        self.set_interact_object(trigger_ids=[10000759], state=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=103, text_id=20000050) # 닭장을 여세요
        # self.set_event_ui(type=1, arg2='$02000329_BF__BOSSBATTLE_01__2$', arg3='3000')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000759], state=0):
            return 보스전투끝(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=103)


class 보스전투끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[611])
        self.set_effect(trigger_ids=[6811], visible=True)
        self.set_timer(timer_id='6', seconds=6)
        self.set_timer(timer_id='2', seconds=2)
        self.set_actor(trigger_id=211, visible=True, initial_sequence='Opened')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 닭장오픈(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=106, type='trigger', achieve='ClearSavetheChicken') # ClearSavetheChicken 퀘스트


class 닭장오픈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.dungeon_clear()
        self.move_npc(spawn_id=1011, patrol_name='MS2PatrolData_1010')
        self.move_npc(spawn_id=1012, patrol_name='MS2PatrolData_1009')
        self.move_npc(spawn_id=1013, patrol_name='MS2PatrolData_1008')
        self.move_npc(spawn_id=1014, patrol_name='MS2PatrolData_1007')
        self.move_npc(spawn_id=1015, patrol_name='MS2PatrolData_1006')
        self.move_npc(spawn_id=1016, patrol_name='MS2PatrolData_1005')
        self.move_npc(spawn_id=1017, patrol_name='MS2PatrolData_1004')
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
