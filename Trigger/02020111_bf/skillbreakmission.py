""" trigger/02020111_bf/skillbreakmission.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset') == 1:
            return 대기_1차_발동체크(self.ctx)


class 대기_1차_발동체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset') == 0:
            return 대기(self.ctx)
        if self.check_npc_additional_effect(spawn_id=111, additional_effect_id=62100016, level=1):
            # <블루라펜샤드 1차 스킬 브레이크 체크>
            return 던전미션1차_체크(self.ctx)


class 던전미션1차_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset') == 0:
            return 대기(self.ctx)
        """
        all_of:  <쉴드가 깨지기까지 8초보다 많은 시간이 남은 경우 = 6초 이내로 파괴>
        all_of:  <스킬 브레이크 성공 애디셔널>
        """
        if self.npc_extra_data(spawn_point_id=111, extra_data_key='brokenShieldRemainTick') >= 8000 and self.check_npc_additional_effect(spawn_id=101, additional_effect_id=70002171, level=1):
            return 던전미션1차_스킬브레이크저지_성공(self.ctx)
        if self.check_npc_additional_effect(spawn_id=101, additional_effect_id=70002181, level=1):
            # <스킬 브레이크 실패 애디셔널>
            return 던전미션1차_스킬브레이크저지_실패(self.ctx)


class 던전미션1차_스킬브레이크저지_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=23039004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset') == 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 대기_2차(self.ctx)


class 던전미션1차_스킬브레이크저지_실패(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset') == 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 대기_2차(self.ctx)


class 대기_2차(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset') == 0:
            return 대기(self.ctx)
        if self.check_npc_additional_effect(spawn_id=115, additional_effect_id=62100016, level=1):
            # <블루라펜샤드 2차 스킬 브레이크 체크>
            return 던전미션2차_체크(self.ctx)


class 던전미션2차_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset') == 0:
            return 대기(self.ctx)
        """
        all_of:  <쉴드가 깨지기까지 8초보다 많은 시간이 남은 경우 = 6초 이내로 파괴>
        all_of:  <스킬 브레이크 성공 애디셔널>
        """
        if self.npc_extra_data(spawn_point_id=115, extra_data_key='brokenShieldRemainTick') >= 8000 and self.check_npc_additional_effect(spawn_id=101, additional_effect_id=70002171, level=1):
            return 던전미션2차_스킬브레이크저지_성공(self.ctx)
        if self.check_npc_additional_effect(spawn_id=101, additional_effect_id=70002181, level=1):
            # <스킬 브레이크 실패 애디셔널>
            return 던전미션2차_스킬브레이크저지_실패(self.ctx)


class 던전미션2차_스킬브레이크저지_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=23039004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset') == 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 던전미션2차_스킬브레이크저지_실패(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakMissionReset') == 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
