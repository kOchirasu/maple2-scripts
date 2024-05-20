""" trigger/02000253_bf/ground.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[701]) # 벨라 음성
        self.set_effect(trigger_ids=[702]) # 벨라 음성
        self.set_mesh(trigger_ids=[107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=906) >= 1:
            return 벨라소환(self.ctx)


class 벨라소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        self.spawn_monster(spawn_ids=[1001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라이동(self.ctx)


class 벨라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        # self.set_effect(trigger_ids=[701], visible=True)
        self.set_dialogue(type=1, spawn_id=1001, script='$02000253_BF__GROUND__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라이동2(self.ctx)


class 벨라이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        # self.set_effect(trigger_ids=[702], visible=True)
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1')
        self.set_dialogue(type=1, spawn_id=1001, script='$02000253_BF__GROUND__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라소멸(self.ctx)


class 벨라소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=140)
        self.destroy_monster(spawn_ids=[1001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 지진(self.ctx)


class 지진(trigger_api.Trigger):
    pass


initial_state = 대기
