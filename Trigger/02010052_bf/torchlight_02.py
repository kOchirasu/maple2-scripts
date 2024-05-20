""" trigger/02010052_bf/torchlight_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7010]) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[110]):
            return burn_state(self.ctx)


class burn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7502], visible=True) # 얼음 녹는 소리
        self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025,5026], start_delay=800, interval=100) # 벽 해제
        self.set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_02__0$', arg3='3000')
        self.set_effect(trigger_ids=[7010], visible=True) # 횃불에 불이 붙는 이펙트
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return spawn_state(self.ctx)


class spawn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=200)


initial_state = idle
