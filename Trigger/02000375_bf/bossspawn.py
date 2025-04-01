""" trigger/02000375_bf/bossspawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1페이지 졸구간에 있는 나가기 포탈, 최초에는 감추기
        self.set_portal(portal_id=6)
        # 2페이지에 있는 나가기 포탈, 최초에는 감추기
        self.set_portal(portal_id=7)
        # 3페이지에 있는 나가기 포탈, 최초에는 감추기
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=3)
        self.set_portal(portal_id=4)
        self.set_portal(portal_id=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 난이도체크(self.ctx)


class 난이도체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_level() == 2:
            # 일반레이드 난이도로 던전입장을 했을 경우
            return 레이드(self.ctx)
        if self.dungeon_level() == 3:
            # 카오스 난이도로 던전입장을 했을 경우
            return 카오스레이드(self.ctx)
        if self.wait_tick(wait_tick=2000):
            # 그냥 테스트용으로 맵코드로 바로 들어왔으면 카오스용 보스 등장
            return 카오스레이드(self.ctx)


class 레이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False) # 일반레이드 난이도용 칸두라 보스 호출

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클리어_체크대기(self.ctx)


class 카오스레이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2101], auto_target=False) # 카오스 난이도용 칸두라 보스 호출

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클리어_체크대기(self.ctx)


class 클리어_체크대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='KanduraNormalDead') == 1:
            # 1페이지 변신전 칸두라가 스펙높은 유저에게 극딜 당해서 죽은 경우  AI_KanduraNormal.xml, AI_KanduraNormal_Chaos.xml 로 부터 KanduraNormalDead = 1신호를 받음
            return 클리어처리01(self.ctx)
        if self.user_value(key='ThirdPhaseEnd') == 1:
            # 칸두라가 변신 한 이후 죽은 경우  AI_KanduraBigBurster.xml, AI_KanduraBigBurster_Chaos.xml 로 부터 ThirdPhaseEnd = 1신호를 받음
            return 클리어처리01(self.ctx)


class 클리어처리01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # 칸두라 죽은 애니가 나오는 시간 6초 정도 되니, 이 연출 다 나오고 클리어 처리함
            return 클리어처리02(self.ctx)


class 클리어처리02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        # DungeonRoom.xlsx  의  clearType  trigger 로 설정한 경우 맵 트리거를 통해서 클리어 UI 띄우는 처리함
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 나가기포털생성(self.ctx)


class 나가기포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # move.xml  트리거에 BattleEnd = 1 신호 보내기
        self.set_user_value(trigger_id=99999002, key='BattleEnd', value=1)
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249,3250,3251,3252,3253,3254,3255,3256,3257,3258,3259,3260,3261,3262,3263,3264,3265,3266,3267,3268,3269,3270,3271,3272,3273,3274,3275,3276,3277,3278,3279,3280,3281,3282,3283,3284,3285,3286,3287,3288,3289,3290,3291,3292,3293,3294,3295,3296,3297,3298,3299,3300], visible=True)
        # 1페이지 왼쪽 전투판에 등장하는 나가기 포탈 생성
        self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)
        # 1페이지 오른쪽 전투판에 등장하는 나가기 포탈 생성
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)
        # 2페이지 전투판에 등장하는 나가기 포탈 생성
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        # 3페이지 전투판에 등장하는 나가기 포탈 생성
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
