""" trigger/02020141_bf/message.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 메시지작동준비(self.ctx)


class 메시지작동준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='MessageAlarm', value=0) # 메시지 출력 유무를 결정하는 변수
        # 이 변수 99가 되면 이 트리거 작동 중지함, 이 변수 99 신호는 AI_TurkaHoodForce_Phase03.xml에서 받음
        self.set_user_value(key='TriggerEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            # 보스 등장해서 활성화 될때까지 여기서 WaitTick 잠시 대기
            return 메시지작동대기버프체크(self.ctx)


class 메시지작동대기버프체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TriggerEnd') == 99:
            # AI_TurkaHoodForce_Phase03.xml로 부터 이 변수 99 신호 받으면 트리거 종료함
            return 트리거종료(self.ctx)
        # 애디셔널 50000348(레벨1) 졸몹이 보스에게 보호 5중첩 버프 애디셔널 부여함
        if self.user_value(key='MessageAlarm') == 13:
            # 이 변수가 1씩 계속 더해져서 13이 되면, 경고 메시지 출력하는 단계로 넘어가기
            return 경고메시지출력(self.ctx)
        if self.check_npc_additional_effect(spawn_id=99, additional_effect_id=50000348, level=1):
            # EventSpawnPointNPC 의 SpawnPointID가 99 번, 즉   spawnPointID="99"
            return 카운트다운체크(self.ctx) # 보스가 방업버프인 상태라면 이 부분 실행
        if not self.check_npc_additional_effect(spawn_id=99, additional_effect_id=50000348, level=1):
            # EventSpawnPointNPC 의 SpawnPointID가 99 번, 즉   spawnPointID="99"
            # 보스가 방업버프 없는 평상시 상태라면 이 부분 실행
            return 카운트다운초기화(self.ctx)


class 카운트다운체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이 변수 1씩 더하는데, 이 변수가 13이 되면 메시지 출력함
        self.add_user_value(key='MessageAlarm', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 메시지작동대기버프체크(self.ctx)


class 카운트다운초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스가 50000348 버프가 없는 상태라면 이 변수 0 초기화
        self.set_user_value(key='MessageAlarm', value=0)
        self.hide_guide_summary(entity_id=29200006)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 메시지작동대기버프체크(self.ctx)


class 경고메시지출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 경고 안내 메시지 출력하기, 메시지 글씨 작성 엑셀파일은 여기 stringGuide.xlsx
        self.show_guide_summary(entity_id=29200006, text_id=29200006, duration=4000)
        # 이 변수 -11을 빼서 2로 만들기, 계속 보스가 버프 상태를 유지한다면 11초 뒤에 다시 메시지 출력될 것임
        self.add_user_value(key='MessageAlarm', value=-11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 다시 메인 체크 단계로 돌아가기
            return 메시지작동대기버프체크(self.ctx)


class 트리거종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=29200006)


initial_state = 시작대기중
