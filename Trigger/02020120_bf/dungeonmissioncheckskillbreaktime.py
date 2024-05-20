""" trigger/02020120_bf/dungeonmissioncheckskillbreaktime.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            # MS2TriggerBox   TriggerObjectID = 199, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        199은 스타팅 포인트 지점만 커버하는 비교적 좁은 범위
            return 보스스킬브레이크시작_대기중(self.ctx)


class 보스스킬브레이크시작_대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=99, additional_effect_id=50004546, level=1):
            # 이슈라는 스폰포인트ID : 99임 , 50004546 는 이슈라의 스킬 브레이크 일때 쉴드 HP수치 설정과 특정 스킬로 공격해야 쉴드HP가 줄어드는 설정이 적용된 애디셔널임
            return 던전미션_체크(self.ctx)


class 던전미션_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        """
        all_of:  <쉴드가 깨지기까지 8초보다 많은 시간이 남은 경우 = 6초 이내로 파괴>
        all_of:  이슈라는 스폰포인트ID : 99임, 이 애디셔널은 이슈라가 스킬브레이크 공격이 플레이어한테 저지 당하면 실패 동작 출력때 이 70002171 애디셔널을 AI에서 인위적으로 적용시킴
        """
        if self.npc_extra_data(spawn_point_id=99, extra_data_key='brokenShieldRemainTick') >= 8000 and self.check_npc_additional_effect(spawn_id=99, additional_effect_id=70002171, level=1):
            return 던전미션_스킬브레이크저지_성공(self.ctx)
        if self.check_npc_additional_effect(spawn_id=99, additional_effect_id=50000367, level=1):
            # 이슈라는 스폰포인트ID : 99임, 이 애디셔널은 플레이어가 이슈라 스킬브레이크 저지 실패하면 극 광역 공격떄  이 50000367 애디셔널을 스킬에서 적용시켜 발생함
            return 던전미션_스킬브레이크저지_실패(self.ctx)


class 던전미션_스킬브레이크저지_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기
        self.dungeon_mission_complete(mission_id=23037004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # 스킬브레이크 성공했으니, 바로 종료 시켜도 괜찮음
            return 종료(self.ctx)


class 던전미션_스킬브레이크저지_실패(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.check_npc_additional_effect(spawn_id=99, additional_effect_id=50004546, level=1):
            # 이슈라는 스폰포인트ID : 99임 , 50004546 는 이슈라의 스킬 브레이크 일때 쉴드 HP수치 설정과 특정 스킬로 공격해야 쉴드HP가 줄어드는 설정이 적용된 애디셔널임
            # 즉 50004546  애디셔널이 이슈라 몸에서 사라졌다는 것은 스킬브레이크 공격 패턴이 다 끝났다는 뜻임
            return 시작대기중(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
