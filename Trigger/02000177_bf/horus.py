""" trigger/02000177_bf/horus.xml """
import trigger_api


class Horus(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=710) >= 1:
            return Horus_move_01(self.ctx)


class Horus_move_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20001772, text_id=20001772, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Horus_01_broken(self.ctx)


class Horus_01_broken(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=999, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Horus_01_End(self.ctx)


class Horus_01_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[3001], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2300):
            return Horus_01_End_02(self.ctx)
        if self.count_users(box_id=711) >= 1:
            return Horus_move_02(self.ctx)


class Horus_01_End_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[999])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=711) >= 1:
            return Horus_move_02(self.ctx)


class Horus_move_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20001772, text_id=20001772, duration=5000)
        self.spawn_monster(spawn_ids=[998], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=751, spawn_ids=[998]):
            return Horus_02_End(self.ctx)
        if self.object_interacted(interact_ids=[10001060], state=2):
            return Horus_move_03(self.ctx)


class Horus_02_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[998])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=752) >= 1:
            return Horus_move_03(self.ctx)


class Horus_move_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20001772, text_id=20001772, duration=5000)
        self.spawn_monster(spawn_ids=[997], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=753, spawn_ids=[997]):
            return Horus_03_End(self.ctx)


class Horus_03_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[997])


initial_state = Horus
