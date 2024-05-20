""" trigger/02000483_bf/07_chamberbattle.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True) # ToNextMap
        self.set_interact_object(trigger_ids=[10002046], state=0) # Chair
        self.destroy_monster(spawn_ids=[940,941,942]) # Mob
        self.set_breakable(trigger_ids=[6200]) # Rock
        self.set_visible_breakable_object(trigger_ids=[6200]) # Rock
        self.set_mesh(trigger_ids=[3910], visible=True) # RockClosed
        self.set_mesh(trigger_ids=[3920]) # RockOpened
        self.set_effect(trigger_ids=[5300]) # StoneGate

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9400]):
            # 회랑 진입
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GuideFindPortal(self.ctx)


class GuideFindPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 다른 방으로 이동할 단서를 찾으세요
        self.show_guide_summary(entity_id=20039706, text_id=20039706)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MobTrapOn(self.ctx)


class MobTrapOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[940,941,942], auto_target=False) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        return MobTrapOnEnd(self.ctx)


class MobTrapOnEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[940,941,942]):
            return SwichOn(self.ctx)


class SwichOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002046], state=1) # LeverForLadder01

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002046], state=0):
            return RockMove01(self.ctx)


class RockMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3910], start_delay=100, fade=2.0) # RockClosed
        self.set_breakable(trigger_ids=[6200], enable=True) # Rock
        self.set_visible_breakable_object(trigger_ids=[6200], visible=True) # Rock
        self.set_effect(trigger_ids=[5300], visible=True) # StoneGate

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return RockMove02(self.ctx)


class RockMove02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True) # ToNextMap

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return RockMove03(self.ctx)


class RockMove03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3920], visible=True) # RockOpened
        self.set_breakable(trigger_ids=[6200]) # Rock
        self.set_visible_breakable_object(trigger_ids=[6200]) # Rock


initial_state = Wait
