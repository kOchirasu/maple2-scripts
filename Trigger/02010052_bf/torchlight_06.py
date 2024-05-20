""" trigger/02010052_bf/torchlight_06.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[6100,6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122]) # 벽 해제
        self.set_effect(trigger_ids=[7006]) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=709) >= 1:
            return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7543], visible=True) # 얼음이 어는 소리
        self.set_mesh(trigger_ids=[6100,6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122], visible=True, start_delay=80, interval=70, fade=8.0) # 얼음!
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return Event_05_01(self.ctx)


class Event_05_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[994]) # 카나 사라짐
        self.spawn_monster(spawn_ids=[106], auto_target=False) # 화롯불 생성
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=200, text_id=20105201) # 화로를 공격하여 불을 붙이세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[106]):
            return burn_state(self.ctx)


class burn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=200)
        self.set_effect(trigger_ids=[7506], visible=True) # 얼음 녹는 소리
        self.set_mesh(trigger_ids=[6100,6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122], start_delay=800, interval=100) # 벽 해제
        self.set_mesh(trigger_ids=[600002]) # 벽 해제 (투명 벽)
        self.set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_06__0$', arg3='3000')
        self.set_effect(trigger_ids=[7006], visible=True) # 횃불에 불이 붙는 이펙트
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return spawn_state(self.ctx)


class spawn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = idle
