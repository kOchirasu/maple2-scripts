""" trigger/02020111_bf/skillbreakmission2.xml """
import trigger_api


class 대기1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=111, additional_effect_id=62100016, level=1):
            return 던전미션_체크1(self.ctx)


class 던전미션_체크1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=101, additional_effect_id=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공1(self.ctx)


class 던전미션_스킬브레이크저지_성공1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=23039005)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_npc_additional_effect(spawn_id=101, additional_effect_id=62100016, level=1):
            # <보스가 스킬 브레이크 발동 상태인지를 체크해서 루프시킴>
            return 대기2(self.ctx)


class 대기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=151, additional_effect_id=62100016, level=1):
            return 던전미션_체크2(self.ctx)


class 던전미션_체크2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=101, additional_effect_id=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공2(self.ctx)


class 던전미션_스킬브레이크저지_성공2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=23039005)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기1
