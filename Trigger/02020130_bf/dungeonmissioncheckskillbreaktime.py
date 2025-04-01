""" trigger/02020130_bf/dungeonmissioncheckskillbreaktime.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='IshuraSkillBreakClear', value=0) # 변수 초기 셋팅
        self.set_user_value(key='RenduebianSkillBreakClear', value=0) # 변수 초기 셋팅
        self.set_user_value(key='YuperiaSkillBreakClear', value=0) # 변수 초기 셋팅

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[601]):
            # MS2TriggerBox   TriggerObjectID = 601, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면, 1셋트 전투판 전체를 둘러싼 큰 범위
            return 보스스킬브레이크시작_대기중(self.ctx)


class 보스스킬브레이크시작_대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=701, additional_effect_id=50004546, level=2):
            # 이슈라는 스폰포인트ID : 701 , 50004546 는 이슈라의 스킬 브레이크 일때 쉴드 HP수치 설정과 특정 스킬로 공격해야 쉴드HP가 줄어드는 설정이 적용된 애디셔널임
            # 레벨2가 10인 던전 전용임, 참고로 레벨1은 4인 던전용
            return 던전미션_체크(self.ctx)
        if self.check_npc_additional_effect(spawn_id=702, additional_effect_id=62100024, level=2):
            # 유페리아는 스폰포인트ID : 702 , 62100024 는 유페리아의 스킬 브레이크 일때 쉴드 HP수치 설정과 특정 스킬로 공격해야 쉴드HP가 줄어드는 설정이 적용된 애디셔널임
            return 던전미션_체크(self.ctx)
        if self.check_npc_additional_effect(spawn_id=703, additional_effect_id=62100016, level=2):
            # 렌듀비앙은 스폰포인트ID : 703 , 62100016 는 렌듀비앙의 스킬 브레이크 일때 쉴드 HP수치 설정과 특정 스킬로 공격해야 쉴드HP가 줄어드는 설정이 적용된 애디셔널임
            return 던전미션_체크(self.ctx)


class 던전미션_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        # 3마리 보스 스킬브레이크 동시에 시간 이내 막을 경우에 대해서 보스 3명 복수 조건 체크 하기
        if self.user_value(key='IshuraSkillBreakClear') == 1 and self.user_value(key='YuperiaSkillBreakClear') == 1 and self.user_value(key='RenduebianSkillBreakClear') == 1:
            return 던전미션_스킬브레이크저지_성공(self.ctx)
        """
        all_of:  <쉴드가 깨지기까지 6초보다 많은 시간이 남은 경우 = 8초 이내로 파괴>
        all_of:  이슈라는 스폰포인트ID : 701, 이 애디셔널은 이슈라가 스킬브레이크 공격이 플레이어한테 저지 당하면 실패 동작 출력때 이 70002171 애디셔널을 AI에서 인위적으로 적용시켰음
        all_of:  <쉴드가 깨지기까지 6초보다 많은 시간이 남은 경우 = 8초 이내로 파괴>
        all_of:  유페리아는 스폰포인트ID : 702, 이 애디셔널은 유페리아가 스킬브레이크 공격이 플레이어한테 저지 당하면 실패 동작 출력때 이 70002171 애디셔널을 AI에서 인위적으로 적용시켰음
        all_of:  <쉴드가 깨지기까지 6초보다 많은 시간이 남은 경우 = 8초 이내로 파괴>
        all_of:  렌듀비앙는 스폰포인트ID : 703, 이 애디셔널은 렌듀비앙가 스킬브레이크 공격이 플레이어한테 저지 당하면 실패 동작 출력때 이 70002171 애디셔널을 AI에서 인위적으로 적용시켰음
        """
        # 이슈라 경우에만 스킬브레이크 시간 이내 클리어  체크하는 로직
        if self.npc_extra_data(spawn_point_id=701, extra_data_key='brokenShieldRemainTick') >= 6000 and self.check_npc_additional_effect(spawn_id=701, additional_effect_id=70002171, level=1) and self.npc_extra_data(spawn_point_id=702, extra_data_key='brokenShieldRemainTick') >= 6000 and self.check_npc_additional_effect(spawn_id=702, additional_effect_id=70002171, level=1) and self.npc_extra_data(spawn_point_id=703, extra_data_key='brokenShieldRemainTick') >= 6000 and self.check_npc_additional_effect(spawn_id=703, additional_effect_id=70002171, level=1):
            return 던전미션_3개변수1셋팅(self.ctx)
        """
        all_of:  <쉴드가 깨지기까지 8초보다 많은 시간이 남은 경우 = 6초 이내로 파괴>
        all_of:  이슈라는 스폰포인트ID : 701, 이 애디셔널은 이슈라가 스킬브레이크 공격이 플레이어한테 저지 당하면 실패 동작 출력때 이 70002171 애디셔널을 AI에서 인위적으로 적용시킴
        """
        # 유페리아 경우에만 스킬브레이크 시간 이내 클리어  체크하는 로직
        if self.npc_extra_data(spawn_point_id=701, extra_data_key='brokenShieldRemainTick') >= 8000 and self.check_npc_additional_effect(spawn_id=701, additional_effect_id=70002171, level=1):
            return 이슈라미션_변수1셋팅(self.ctx)
        """
        all_of:  <쉴드가 깨지기까지 8초보다 많은 시간이 남은 경우 = 6초 이내로 파괴>
        all_of:  유페리아는 스폰포인트ID : 702, 이 애디셔널은 유페리아가 스킬브레이크 공격이 플레이어한테 저지 당하면 실패 동작 출력때 이 70002171 애디셔널을 AI에서 인위적으로 적용시킴
        """
        # 렌듀비앙 경우에만 스킬브레이크 시간 이내 클리어  체크하는 로직
        if self.npc_extra_data(spawn_point_id=702, extra_data_key='brokenShieldRemainTick') >= 8000 and self.check_npc_additional_effect(spawn_id=702, additional_effect_id=70002171, level=1):
            return 유페리아미션_변수1셋팅(self.ctx)
        """
        all_of:  <쉴드가 깨지기까지 8초보다 많은 시간이 남은 경우 = 6초 이내로 파괴>
        all_of:  렌듀비앙는 스폰포인트ID : 703, 이 애디셔널은 렌듀비앙가 스킬브레이크 공격이 플레이어한테 저지 당하면 실패 동작 출력때 이 70002171 애디셔널을 AI에서 인위적으로 적용시킴
        """
        # 3마리 보스 중 하나라도 극 광역공격 실행하면 무조건 실패해서 트리거 처음으로 돌려놓기, 실패 체크 단계는 맨 마지막 쪽에 하는 것이 안정적임
        if self.npc_extra_data(spawn_point_id=703, extra_data_key='brokenShieldRemainTick') >= 8000 and self.check_npc_additional_effect(spawn_id=703, additional_effect_id=70002171, level=1):
            return 렌듀비앙미션_변수1셋팅(self.ctx)
        if self.check_npc_additional_effect(spawn_id=701, additional_effect_id=50000264, level=1):
            # 이슈라는 스폰포인트ID : 701, 이 애디셔널은 플레이어가 이슈라 스킬브레이크 저지 실패하면 극 광역 공격떄  무적 처리 되는데 이때 걸리는 애디셔널임, 이슈라는 레벨1 사용
            return 보스스킬브레이크시작_대기중(self.ctx)
        if self.check_npc_additional_effect(spawn_id=702, additional_effect_id=50000264, level=3):
            # 유페리아는 스폰포인트ID : 702, 이 애디셔널은 플레이어가 유페리아 스킬브레이크 저지 실패하면 극 광역 공격떄  무적 처리 되는데 이때 걸리는 애디셔널임, 유페리아는 레벨3 사용
            return 보스스킬브레이크시작_대기중(self.ctx)
        if self.check_npc_additional_effect(spawn_id=703, additional_effect_id=50000264, level=2):
            # 렌듀비앙는 스폰포인트ID : 703, 이 애디셔널은 플레이어가 렌듀비앙 스킬브레이크 저지 실패하면  극 광역 공격떄  무적 처리 되는데 이때 걸리는 애디셔널임, 렌듀비앙은 레벨2 사용
            return 보스스킬브레이크시작_대기중(self.ctx)


class 던전미션_3개변수1셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='IshuraSkillBreakClear', value=1)
        self.set_user_value(key='YuperiaSkillBreakClear', value=1)
        self.set_user_value(key='RenduebianSkillBreakClear', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            # 이 경우는 이미 달성한 상태라서 천천히 넘어가도 괜찮음
            return 던전미션_체크(self.ctx)


class 이슈라미션_변수1셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='IshuraSkillBreakClear', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            # 너무 길면 버그 날 수 있어서 신속하게 처리해야 함
            return 던전미션_체크(self.ctx)


class 유페리아미션_변수1셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='YuperiaSkillBreakClear', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            # 너무 길면 버그 날 수 있어서 신속하게 처리해야 함
            return 던전미션_체크(self.ctx)


class 렌듀비앙미션_변수1셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RenduebianSkillBreakClear', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            # 너무 길면 버그 날 수 있어서 신속하게 처리해야 함
            return 던전미션_체크(self.ctx)


class 던전미션_스킬브레이크저지_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기, 시간 이내 스킬브레이크 막기 클리어 미션 달성임
        self.dungeon_mission_complete(mission_id=23040004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            # 스킬브레이크 성공했으니, 바로 종료 시켜도 괜찮음
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
