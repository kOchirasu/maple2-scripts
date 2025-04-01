""" trigger/02000521_bf/main.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6001])
        self.set_mesh(trigger_ids=[6002])
        self.set_mesh(trigger_ids=[6003])
        self.set_mesh(trigger_ids=[6004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return chaos_raid(self.ctx)


class chaos_raid(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[402], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ExitPortal') == 1:
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)


initial_state = ready
