""" trigger/02000055_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[14]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=12)
        self.set_portal(portal_id=13)
        self.spawn_monster(spawn_ids=[91], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[91]):
            return 종료체크(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[91])


class 종료체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=12, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13, visible=True, enable=True, minimap_visible=True)


initial_state = 시작대기중
