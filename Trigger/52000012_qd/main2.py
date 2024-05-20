""" trigger/52000012_qd/main2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_actor(trigger_id=10001, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=10002, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[10011], visible=True)
        self.set_mesh(trigger_ids=[10012], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002610], quest_states=[2]):
            return 문열림1(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002610], quest_states=[3]):
            return 문열림1(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[2000], auto_target=False)
        self.destroy_monster(spawn_ids=[5000])
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])


class 문열림1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='19', seconds=1)
        self.set_actor(trigger_id=10001, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[10011])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='19'):
            return 문열림2(self.ctx)


class 문열림2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=10002, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[10012])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[10002611], quest_states=[2]):
            return 포털생성(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[10002611], quest_states=[3]):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9001]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


initial_state = 대기
