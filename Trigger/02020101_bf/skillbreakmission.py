""" trigger/02020101_bf/skillbreakmission.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=101, additional_effect_id=62100024, level=1):
            return 던전미션_체크(self.ctx)


class 던전미션_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        """
        all_of:  <쉴드가 깨지기까지 8초보다 많은 시간이 남은 경우 = 6초 이내로 파괴>
        all_of:  <스킬 브레이크 성공 애디셔널>
        """
        if self.npc_extra_data(spawn_point_id=101, extra_data_key='brokenShieldRemainTick') >= 8000 and self.check_npc_additional_effect(spawn_id=101, additional_effect_id=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공(self.ctx)
        if self.check_npc_additional_effect(spawn_id=101, additional_effect_id=70002181, level=1):
            # <스킬 브레이크 실패 애디셔널>
            return 던전미션_스킬브레이크저지_실패(self.ctx)


class 던전미션_스킬브레이크저지_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=23038004)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_npc_additional_effect(spawn_id=101, additional_effect_id=62100024, level=1):
            # <보스가 스킬 브레이크 발동 상태인지를 체크해서 루프시킴>
            return 대기(self.ctx)


class 던전미션_스킬브레이크저지_실패(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_npc_additional_effect(spawn_id=101, additional_effect_id=62100024, level=1):
            # <보스가 스킬 브레이크 발동 상태인지를 체크해서 루프시킴>
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
