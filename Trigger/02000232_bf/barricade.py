""" trigger/02000232_bf/barricade.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=202, spawn_ids=[301]):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=1200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 차단(self.ctx)


class 차단(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112], visible=True, interval=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[301]):
            return 차단해제(self.ctx)
        if not self.user_detected(box_ids=[202]):
            return 대기(self.ctx)


class 차단해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112], interval=200)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[202]):
            return 대기(self.ctx)


initial_state = 대기
