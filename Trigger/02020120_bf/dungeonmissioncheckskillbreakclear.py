""" trigger/02020120_bf/dungeonmissioncheckskillbreakclear.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakSuccess') == 1:
            # 스킬브레이크 막기 공했으면, 이슈라 AI에서  SkillBreakSuccess = 1 신호를 보냄
            return 스킬브레이크성공_던전미션랭크(self.ctx)


class 스킬브레이크성공_던전미션랭크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 스킬브레이크 막기 성공하면 SkillBreakSuccess = 1 신호를 받아서, DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기
        self.dungeon_mission_complete(mission_id=23037005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
