""" trigger/02020140_bf/2phasetubeattackcheck.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 변수 최초 초기화: 이 변수가 1이 되면 튜브 대미지 필드 1단계 진행,  이 변수가 2이 되면 튜브 대미지 필드 2단계 진행
        self.set_user_value(key='2PhaseTubeStep', value=0)
        # 변수 최초 초기화: 마법 구슬 오브젝트가 등장하면, 이 오브젝트  AI_MarbleTurkaSupport.xml  AI로 부터 이 변수 +1 신호를 받고, 파괴되어 죽으면  AI_MarbleTurkaSupport.xml AI로 부터 이 변수 -1 신호를 받게 됨
        self.set_user_value(key='MarbleTurkaSupportMany', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 트리거작동신호받기대기중(self.ctx)


class 트리거작동신호받기대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='2PhaseTubeStep') >= 1:
            # 이 변수가 1 이상이 되면 본격 트리거 작동함, 이 변수는 0 1 2 이렇게 3가지 경우의 수가 있음
            return 트리거작동대기중(self.ctx)


class 트리거작동대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # 투르카가 2페이즈 시작떄 모든 파티원 잡아서 졸구간 건너띄우기 될 경우 튜브 대미지 필드가 1단계 진행되다가 바로 이어 2단계로 가는 어색한 경우가 있어서,  2PhaseTubeStep = 2 신호 다 받을 때까지 여기서 WaitTick = 3초 이상 설정함
            return 트리거작동시작(self.ctx)


class 트리거작동시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='2PhaseTubeStep') == 1:
            # 2페이즈 투르카 AI 에서 이 변수 1 신호 받으면,  튜브 대미지 필드 1단계 진행함
            return 튜브대미지필드_1단계진행(self.ctx)
        if self.user_value(key='2PhaseTubeStep') == 2:
            # 2페이즈 투르카 AI 에서 이 변수 2 신호 받으면,  튜브 대미지 필드 2단계 진행함
            return 튜브대미지필드_2단계전환_우선1단계제거(self.ctx)


class 튜브대미지필드_1단계진행(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MarbleTurkaSupportMany') >= 1:
            # 이 변수 1 이상이라는 것은 마법 구슬 오브젝트가 최소 1개라도 있어 보스한테 마력 에너지 제공하고 있다는 뜻이기 때문에, 튜브 대미지필드 생성 로직으로 진행해야 함
            return 단계_튜브대미지필드_생성1(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 보스가 마법 구슬 오브젝트로 부터 레이저를 맞지 않아서 애디셔널 걸리지 않은 상태면, 튜브 대미지필드 제거함
            return 단계_튜브대미지필드_제거1(self.ctx)


class 단계_튜브대미지필드_생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1단계 튜브대미지필드 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크
        self.add_buff(box_ids=[102], skill_id=50004566, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='2PhaseTubeStep') == 2:
            # 2페이즈 투르카 AI 에서 이 변수 2 신호 받으면,  튜브 대미지 필드 2단계 진행함
            return 튜브대미지필드_2단계전환_우선1단계제거(self.ctx)
        if self.user_value(key='MarbleTurkaSupportMany') == 0:
            # 혹시 이 타이밍에 구슬 오브젝트로 파괴되면 이 변수 0이 되는데, 튜브 대미지필드 제거 진행하기
            return 단계_튜브대미지필드_제거1(self.ctx)


class 단계_튜브대미지필드_제거1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.npc_remove_additional_effect(spawn_id=102, additional_effect_id=50004566) # 1단계 튜브대미지필드 제거

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='2PhaseTubeStep') == 2:
            # 2페이즈 투르카 AI 에서 이 변수 2 신호 받으면,  튜브 대미지 필드 2단계 진행함
            return 튜브대미지필드_2단계전환_우선1단계제거(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 튜브대미지필드_1단계진행(self.ctx)


class 튜브대미지필드_2단계전환_우선1단계제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.npc_remove_additional_effect(spawn_id=102, additional_effect_id=50004566) # 우선 1단계 튜브대미지필드  제거
        # 이 변수 최초 초기화: 보스가 마법 구슬 오브제트로 인한 애디셔널에 계속 걸려 있으면, 이 변수 1씩 더하는데, 이 변수가 10씩 쌓일 수록 튜브대미지필드 1단계씩 상승시킴
        self.set_user_value(key='TubeLeveStep', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            # 1단계 튜브대미지필드에서 2단계 튜브대미지필드로 넘어갈 때 바로 넘어가지 말고 잠시  WaitTick 딜레이 상황을 부여
            return 단계_튜브대미지필드_처음단계2(self.ctx)


class 단계_튜브대미지필드_처음단계2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MarbleTurkaSupportMany') >= 1:
            # 이 변수 1 이상이라는 것은 마법 구슬 오브젝트가 최소 1개라도 있어 보스한테 마력 에너지 제공하고 있다는 뜻이기 때문에, 튜브 대미지필드 생성 로직으로 진행해야 함
            return 단계_튜브대미지필드_1Lv생성2(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 보스가 마법 구슬 오브젝트로 부터 레이저를 맞지 않아서 애디셔널 걸리지 않은 상태면, 튜브 대미지필드 제거함
            return 단계_튜브대미지필드_제거2(self.ctx)


class 단계_튜브대미지필드_1Lv생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 튜브대미지필드 1Lv 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크
        self.add_buff(box_ids=[102], skill_id=50004563, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2(self.ctx)


class 단계_튜브대미지필드_2Lv생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.npc_remove_additional_effect(spawn_id=102, additional_effect_id=50004563) # 2단계 튜브대미지필드 1Lv  제거
        # 튜브대미지필드 2Lv 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크
        self.add_buff(box_ids=[102], skill_id=50004564, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2(self.ctx)


class 단계_튜브대미지필드_3Lv생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.npc_remove_additional_effect(spawn_id=102, additional_effect_id=50004564) # 2단계 튜브대미지필드 2Lv 제거
        # 튜브대미지필드 3Lv 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크
        self.add_buff(box_ids=[102], skill_id=50004565, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2(self.ctx)


class 단계_튜브대미지필드_TubeLeveStep_더하기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이 변수 1씩 더하는데, 이 변수가 10씩 쌓일 수록 튜브대미지필드 1단계씩 상승시킴
        self.add_user_value(key='TubeLeveStep', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 1초 마다 체크하게 하기 위해 waitTick="1000" 설정
            return 단계_튜브대미지필드_TubeLeveStep_체크2(self.ctx)
        if self.user_value(key='TubeLeveStep') == 30:
            # 이 변수가 30이되면 경고 메시지 띄우기
            return 버프부여구슬제거경고메시지(self.ctx)


class 단계_튜브대미지필드_TubeLeveStep_체크2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TubeLeveStep') == 10:
            # 이 변수가 1씩 계속 더해져서 10이 되면, 튜브대미지필드 2Lv를 실행함, 즉 마법구슬 에너지 노출 시간 10초면 1단계 상승됨
            return 단계_튜브대미지필드_2Lv생성2(self.ctx)
        if self.user_value(key='TubeLeveStep') == 20:
            # 이 변수가 1씩 계속 더해져서 20이 되면, 튜브대미지필드 3Lv를 실행함, 즉 마법구슬 에너지 노출 시간 10초면 1단계 상승됨
            return 단계_튜브대미지필드_3Lv생성2(self.ctx)
        if self.user_value(key='MarbleTurkaSupportMany') >= 1:
            # 이 변수 1 이상이라는 것은 마법 구슬 오브젝트가 최소 1개라도 있어 보스한테 마력 에너지 제공하고 있다는 뜻이기 때문에, 튜브 대미지필드 생성 로직으로 진행해야 함
            return 단계_튜브대미지필드_TubeLeveStep_더하기2(self.ctx)
        if self.wait_tick(wait_tick=1000):
            # 마법 구슬 오브젝트 전부 파괴하여, MarbleTurkaSupportMany 변수 0이 되기 때문에 튜브 대미지 필드 전부 제거함
            return 단계_튜브대미지필드_제거2(self.ctx)


class 버프부여구슬제거경고메시지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이 변수 -9를 빼서 21로 만들기, 절대 20 이하로 만들면 안됨!! 대박 버그임
        self.add_user_value(key='TubeLeveStep', value=-9)
        # 벙업 버프 (5중첩) 걸기(50000348 2Lv), 홀로그램 소녀 소환몹 몬스터가 보스한테 부여하는 버프랑 동일한 것임
        self.add_buff(box_ids=[102], skill_id=50000348, level=2)
        # 안내 메시지 호출하기, 메시지 글씨 작성 엑셀파일은 여기 stringGuide.xlsx
        self.show_guide_summary(entity_id=29200005, text_id=29200005, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 다시 메인 체크 단계로 돌아가기
            return 단계_튜브대미지필드_TubeLeveStep_체크2(self.ctx)


class 단계_튜브대미지필드_제거2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몇 Lv가 걸려있는지 모르니 일단 모든 레벨 다 제거함
        self.npc_remove_additional_effect(spawn_id=102, additional_effect_id=50004563) # 2단계 튜브대미지필드 1Lv  제거
        self.npc_remove_additional_effect(spawn_id=102, additional_effect_id=50004564) # 2단계 튜브대미지필드 2Lv 제거
        self.npc_remove_additional_effect(spawn_id=102, additional_effect_id=50004565) # 2단계 튜브대미지필드 3Lv 제거
        # 중첩 방업 버프도 제거하기 걸려있는지 모르니 무조건 제거
        self.npc_remove_additional_effect(spawn_id=102, additional_effect_id=50000348)
        # 다시 처음부터 시작하니 이 변수  초기화: 보스가 마법 구슬 오브제트로 인한 애디셔널에 계속 걸려 있으면, 이 변수 1씩 더하는데, 이 변수가 10씩 쌓일 수록 튜브대미지필드 1단계씩 상승시킴
        self.set_user_value(key='TubeLeveStep', value=0)
        # 혹시 마력의 구슬 제거하라는 경고 메시지 떠있는 상태일 경우를 대비해 메시지 제거 명령어 여기에 설정함
        self.hide_guide_summary(entity_id=29200005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 2단계_튜브대미지필드 로직 다시 처음부터 실행함
            return 단계_튜브대미지필드_처음단계2(self.ctx)


# 이 트리거에서는

"""
class 종료(trigger_api.Trigger):
    pass
"""

# 로 올일 없음

class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
