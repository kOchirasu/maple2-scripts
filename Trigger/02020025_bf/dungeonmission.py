""" trigger/02020025_bf/dungeonmission.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 던전미션체크대기(self.ctx)


class 던전미션체크대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=904, spawn_ids=[201]):
            return 체력90이하체크(self.ctx)


class 체력90이하체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=201, is_relative=True) <= 90:
            return 지하1층(self.ctx)


class 지하1층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=24092001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=201, is_relative=True) <= 70:
            return 지하2층(self.ctx)


class 지하2층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=24092002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=201, is_relative=True) <= 55:
            return 지하3층(self.ctx)


class 지하3층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=24092003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=201, is_relative=True) <= 40:
            return 지하4층(self.ctx)


class 지하4층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=24092004)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
