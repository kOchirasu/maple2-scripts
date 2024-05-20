""" trigger/02000213_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)
        self.set_interact_object(trigger_ids=[10000259,10000260,10000261], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000259,10000260,10000261], state=2):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1099])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1099]):
            return 종료체크(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1099])


class 종료체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)


initial_state = 시작대기중
