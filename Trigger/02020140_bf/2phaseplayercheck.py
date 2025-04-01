""" trigger/02020140_bf/2phaseplayercheck.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 안잡힌플레이어체크(self.ctx)


class 안잡힌플레이어체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='2PhasePlayerCheckStart') == 1:
            # 2페이즈 트루카AI에서 전투 시작때 플레이어 잡기 행동이후, 안잡힌 남은 플레이어의 유무 체크 시작을 위해, 이  변수 1을 보냄
            return 페이즈지점체크하기1(self.ctx)


class 페이즈지점체크하기1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[98]):
            # MS2TriggerBox   TriggerObjectID = 98, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        98는 1페이즈 지점과 졸구간 전체를 커버하는 넓은 범위
            # 안잡힌 플레이어가 1페이지 전투판 지점 혹은 줄구가에 설치한 트리거 영역에 있음을 확인했으면, 그냥 종료 처리하기
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=900):
            return 추가로최초시작지점체크하기(self.ctx)


class 추가로최초시작지점체크하기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[99]):
            # MS2TriggerBox   TriggerObjectID = 99, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        99는 스타팅 포인트 지점 커버하는 범위
            # 안잡힌 플레이어가 최초 시작 지점 트리거 영역에 있음을 확인했으면, 그냥 종료 처리하기
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=900):
            return 안잡힌플레이어없음확인(self.ctx)


class 안잡힌플레이어없음확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='TwoPhaseMainBattle', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 페이즈복격진행_안내메시지출력2(self.ctx)


class 페이즈복격진행_안내메시지출력2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # CubeBreak ,  MS2TriggerSkill = 91 스킬코드 70000105(레벨1) 발동시켜 마법구슬 지점에 계단을 막고 있는 큐브 제거함
        self.set_skill(trigger_ids=[91], enable=True)
        # 안내 메시지 호출하기, 메시지 글씨 작성 엑셀파일은 여기 stringGuide.xlsx
        self.show_guide_summary(entity_id=29200003, text_id=29200003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            # 안내 메시지 5~6초 정도 출력후 다시 "졸구간진행체크중" 으로 되돌아가기
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=29200003)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
