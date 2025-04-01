""" trigger/02020120_bf/daynightchangedebuff.xml """
import trigger_api
from System.Numerics import Vector3


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 맵 스킬 초기화 셋팅, 태양빛의 저주 디버프 스킬 On으로 초기 셋팅하기, 이 맵은 낮으로 시작하기 때문에
        self.set_skill(trigger_ids=[2222], enable=True)
        # 맵 스킬 초기화 셋팅, 달빛의 저주 디버프 스킬 Off으로 초기 셋팅하기
        self.set_skill(trigger_ids=[1212])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=199) >= 1:
            # MS2TriggerBox   TriggerObjectID = 199, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        199은 스타팅 지점   포함되는 범위
            return 낮밤변환신호대기(self.ctx)


class 낮밤변환신호대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DayNightChange') == 1:
            # 이슈라가 밤에서 낮으로 변화시킬때  DayNightChange 이 변수 1로 설정하는 신호를 AI에서 보냄
            return 낮시간으로변화대기단계(self.ctx)
        if self.user_value(key='DayNightChange') == 2:
            # 이슈라가 낮에서 밤으로 변화시킬때  DayNightChange 이 변수 2로 설정하는 신호를 AI에서 보냄
            return 밤시간으로변화대기단계(self.ctx)
        # 스킬 브레이크 막기 실패하면 이슈라AI에서  DungeonReset = 1 신호를 보내서 던전 초기화 시킴
        if self.user_value(key='DayNightChange') == 3:
            # 이슈라가 스킬브레이크 패턴 사용하거나 죽을 때  DayNightChange 이 변수 3으로로 설정하는 신호를 AI에서 보냄
            return 디버프모조리제거(self.ctx)
        if self.user_value(key='DungeonReset') == 1:
            # 낮으로 시간으로 셋팅하는 것이 이 맵의 초기화 셋팅임
            return 낮시간으로변화하기_맵초기화(self.ctx)


class 낮시간으로변화대기단계(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1400):
            # 이슈라 보스 낮밤 변화 마법 동작에 맞추어 타이밍 맞게 트리거 신호 변화를 하기 위해, 여기  waitTick 시간 조절을 넣음
            return 낮시간으로변화하기(self.ctx)


class 낮시간으로변화하기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_background(dds='BG_RedLapenta_A.dds')
        # arg1 = ambient color RGB값
        self.set_ambient_light(primary=Vector3(226,197,211))
        # arg1 = diffuse color RGB값,  arg2 = specular color RGB값
        self.set_directional_light(diffuse_color=Vector3(224,246,249), specular_color=Vector3(170,170,170))
        self.set_skill(trigger_ids=[2222], enable=True) # 태양빛의 저주 디버프 스킬 On
        self.set_skill(trigger_ids=[1212]) # 달빛의 저주 디버프 스킬 Off
        # DayNightChange 변수 0으로 초기하 하여 위쪽 단계 "낮밤변환신호대기" 에서 대기 상태가 되도록 하기
        self.set_user_value(key='DayNightChange', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 낮밤변환신호대기(self.ctx)


class 낮시간으로변화하기_맵초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 레벨2: 시야 효과 8초 이상, 낮으로 변하면서 필터 이펙트 시야효과 애디녀설 부여하기, MS2TriggerBox   TriggerObjectID = 299,   299는 모든 전투판 범위임,  arg3 는 애디셔널 레벨임
        self.add_buff(box_ids=[299], skill_id=50004547, level=2, ignore_player=False)
        # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        self.set_user_value(key='DungeonReset', value=0)
        # DayNightChange 변수 0으로 초기하 하여 위쪽 단계 "낮밤변환신호대기" 에서 대기 상태가 되도록 하기
        self.set_user_value(key='DayNightChange', value=0)
        self.change_background(dds='BG_RedLapenta_A.dds')
        # arg1 = ambient color RGB값
        self.set_ambient_light(primary=Vector3(226,197,211))
        # arg1 = diffuse color RGB값,  arg2 = specular color RGB값
        self.set_directional_light(diffuse_color=Vector3(224,246,249), specular_color=Vector3(170,170,170))
        self.set_skill(trigger_ids=[2222], enable=True) # 태양빛의 저주 디버프 스킬 On
        self.set_skill(trigger_ids=[1212]) # 달빛의 저주 디버프 스킬 Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 낮밤변환신호대기(self.ctx)


class 밤시간으로변화대기단계(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1400):
            # 이슈라 보스 낮밤 변화 마법 동작에 맞추어 타이밍 맞게 트리거 신호 변화를 하기 위해, 여기  waitTick 시간 조절을 넣음
            return 밤시간으로변화하기(self.ctx)


class 밤시간으로변화하기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이슈라 보스 낮밤 변화 마법 동작에 맞추어 타이밍 맞게 트리거 신호 변화를 하기 위해, 여기  waitTick 시간 조절을 넣음
        self.change_background(dds='BG_RedLapenta_B.dds')
        # arg1 = ambient color RGB값
        self.set_ambient_light(primary=Vector3(120,119,183))
        # arg1 = diffuse color RGB값,  arg2 = specular color RGB값
        self.set_directional_light(diffuse_color=Vector3(193,100,119), specular_color=Vector3(170,170,170))
        self.set_skill(trigger_ids=[2222]) # 태양빛의 저주 디버프 스킬 Off
        self.set_skill(trigger_ids=[1212], enable=True) # 달빛의 저주 디버프 스킬 On
        # DayNightChange 변수 0으로 초기하 하여 위쪽 단계 "낮밤변환신호대기" 에서 대기 상태가 되도록 하기
        self.set_user_value(key='DayNightChange', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 낮밤변환신호대기(self.ctx)


class 디버프모조리제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 태양빛 달빛 각종 저주 디버프 전부 제거하기, MS2TriggerBox   TriggerObjectID = 299,   299는 모든 전투판 범위임,  arg3 는 애디셔널 레벨임
        self.add_buff(box_ids=[299], skill_id=50005315, level=1, ignore_player=False)
        # DayNightChange 변수 0으로 초기하 하여 위쪽 단계 "낮밤변환신호대기" 에서 대기 상태가 되도록 하기
        self.set_user_value(key='DayNightChange', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1100):
            return 낮밤변환신호대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
