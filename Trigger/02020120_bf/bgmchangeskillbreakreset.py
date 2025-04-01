""" trigger/02020120_bf/bgmchangeskillbreakreset.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 포탈ID 1220 , 큐브 파괴되어 추락된 플레이어 이전 전투판으로 보내는 순간이동 포탈 초기화 시키기
        self.set_portal(portal_id=1220)
        # SkillBreakStart 변수 0으로 초기화
        self.set_user_value(key='SkillBreakStart', value=0)
        self.set_user_value(key='DungeonReset', value=0) # DungeonReset 변수 0으로 초기화

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=299) >= 1:
            # MS2TriggerBox   TriggerObjectID = 299, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        299은 모든 전투판 포함되는 엄청 넓은 범위
            return 던전시간작동대기(self.ctx)


class 던전시간작동대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=399) >= 1:
            # MS2TriggerBox   TriggerObjectID = 399, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        399은 보스 메인 전투판만 포함되는 범위
            return 스킬브레이크신호대기_BGM교체(self.ctx)
        if self.user_value(key='BgmChangeTriggerCancel') == 1:
            # 이슈라가 메인 전투판에 오기 전에 죽으면 BGM 변경 트리거 자체를 종료 시키기 , 이슈라가 Kill되면 나오는 이벤트 연출용 AI_IshuraRbladerDark_EventLeave.xml 에서 신호 보냄
            return 종료(self.ctx)


class 스킬브레이크신호대기_BGM교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스 메인 전투판으로 들어서면 보스용 BGM으로 교체하기, 스킬브레이크 막기 실패해서 원래 BGM으로 되돌리는 초기화 설정은 bossSpawn.xml 에 있음
        self.set_sound(trigger_id=19600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SkillBreakStart') >= 1:
            # 이슈라가 스킬브레이크 광역맵파괴 스킬 사용시  SkillBreakStart 이 변수 1로 설정하는 신호를 AI에서 보냄
            return 스킬브레이크로직작동(self.ctx)


class 스킬브레이크로직작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 5스테이지 가운데 전투판에 보스 메인 전투판으로 보내는 순간이동 포탈 이때 감추기, 이 포탈 PortalStage06Boss.xml 에서도 사용함
        self.set_portal(portal_id=6201)
        # 혹시 5스테이지 가운데로 진행했을 경우, 이 포탈이 미리 생성되어있을 수 있어서 그려면 파괴된 바닥 큐브가 재생되기 전에 플레이어가  미리 가버려서 허공에 도착하는 버그 상황이 생길 수 있어서 이 포탈 이 타이밍에 감추기 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 스킬브레이크 스킬 동작 연출에 맞게 타이밍 맞추어 신호 변화를 하기 위해, 여기  waitTick 시간 조절을 넣음
            return 스킬브레이크실패초기화처리(self.ctx)


class 스킬브레이크실패초기화처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 포탈ID 1220 , 큐브 파괴되어 추락된 플레이어 이전 전투판으로 보내는 순간이동 포탈 활성화 시키기
        self.set_portal(portal_id=1220, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 스킬브레이크실패연출출력(self.ctx)


class 스킬브레이크실패연출출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui_script(type=BannerType.Text, script='10년은 이르다!!!', duration=4000)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonReset') == 1:
            return Ready(self.ctx)


class 종료(trigger_api.Trigger):
    pass


# 여기 아래는 사용 안함
class 보스한테보내는포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 5스테이지 가운데 전투판에 보스 메인 전투판으로 보내는 순간이동 포탈 생성시키기, 이 포탈 PortalStage06Boss.xml 에서도 사용함
        self.set_portal(portal_id=6201, visible=True, enable=True, minimap_visible=True)
        # 포탈ID 1220 , 큐브 파괴되어 추락된 플레이어 이전 전투판으로 보내는 순간이동 포탈 다시 감추기
        self.set_portal(portal_id=1220)
        # SkillBreakStart 변수 0으로 초기화
        self.set_user_value(key='SkillBreakStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            # 다시 처음 단계로 돌아가서 다시 던전시간 초기화 하기
            return None # Missing State: 스킬브레이크신호대기_시간다시셋팅


class 보스한테보내는포탈생성_시간초기화안함01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            # 파괴된 전투판 큐브 다시 생성되는 타이밍에 맞추어 보스 전투판으로 가는 포탈을 생성해야 하기 때문에 waitTick 시간 조절 함
            return 보스한테보내는포탈생성_시간초기화안함02(self.ctx) # 던전시간 셋팅 하는 거 없는 초기화


class 보스한테보내는포탈생성_시간초기화안함02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 5스테이지 가운데 전투판에 보스 메인 전투판으로 보내는 순간이동 포탈 생성시키기, 이 포탈 PortalStage06Boss.xml 에서도 사용함
        self.set_portal(portal_id=6201, visible=True, enable=True, minimap_visible=True)
        # 포탈ID 1220 , 큐브 파괴되어 추락된 플레이어 이전 전투판으로 보내는 순간이동 포탈 다시 감추기
        self.set_portal(portal_id=1220)
        # SkillBreakStart 변수 0으로 초기화
        self.set_user_value(key='SkillBreakStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            # 파괴된 전투판 큐브 다시 생성되는 타이밍에 맞추어 보스 전투판으로 가는 포탈을 생성해야 하기 때문에 waitTick 시간 조절 함
            # 던전시간 셋팅 하는 거 없는 초기화
            return None # Missing State: 스킬브레이크신호대기_시간셋팅안함


initial_state = Ready
