""" trigger/02000244_bf/trigger_01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[701,702], visible=True)
        self.set_mesh(trigger_ids=[709,710], visible=True)
        self.destroy_monster(spawn_ids=[631,632,633,634,635,636,637,638,639])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[201]):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[631,632,633,634,635,636,637,638,639], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[631,632,633,634,635,636,637,638,639]):
            return 통과(self.ctx)
        if self.object_interacted(interact_ids=[10000303], state=0):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[701,702])
        self.set_mesh(trigger_ids=[709,710])
        self.set_timer(timer_id='1', seconds=180)


initial_state = 대기
