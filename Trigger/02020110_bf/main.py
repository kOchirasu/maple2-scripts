""" trigger/02020110_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=3)
        self.set_portal(portal_id=4)
        self.set_portal(portal_id=5)
        self.set_portal(portal_id=6)
        self.set_portal(portal_id=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901], job_code=0):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            return 번방1(self.ctx)


class 번방1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,120], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,120]):
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            return 번방2(self.ctx)


class 번방2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102,103,104,105,106,107], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102,103,104,105,106,107]):
            self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
            self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
            return 번방3(self.ctx)


class 번방3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[108,109,110,111,112,113], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[108,109,110,111,112,113]):
            self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)
            self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)
            return 번방4(self.ctx)


class 번방4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[114,115,116,117,118,119], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[114,115,116,117,118,119]):
            return 다음블록이동(self.ctx)


class 다음블록이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
