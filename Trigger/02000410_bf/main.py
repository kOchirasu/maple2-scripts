""" trigger/02000410_bf/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 맨 오른쪽 지점에서 대포 배치하기 위한 오프젝트 생성하기 , TriggerObjectID: 6010, 6011
        self.set_mesh(trigger_ids=[6010,6011], visible=True, start_delay=1, interval=1)
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(trigger_ids=[6000,6001,6002,6003])
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(trigger_ids=[6004,6005])
        # 던전 나가기 위한 포탈 초기화 설정,   arg1="1" 은 포탈ID, 전투판에 있는 포탈
        self.set_portal(portal_id=1)
        # 던전 나가기 위한 포탈 초기화 설정,   arg1="2" 은 포탈ID, 안전 부활 지점에 있는 포탈
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면,          750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 전투시작_인페르녹전함(self.ctx)


class 전투시작_인페르녹전함(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_timer(timer_id='1', seconds=1)
        # 인페르녹 전함 스폰하기, 스폰ID : 101
        self.spawn_monster(spawn_ids=[101])
        # 월드인베이젼 던전 Type에서 사용하는 보스 HP바 위에 있는 타임 게이지UI 위에 보스 등장을 알리는 첫번째 아이콘을 띄우며 어느 위치에 띄울지를 정의하는 부분, 15분 즉 900000을 풀 게이지 기준으로 어느 위치에 띄울지를 정의함
        self.dungeon_set_lap_time(id=1, lap_time=420000)
        # 월드인베이젼 던전 Type에서 사용하는 보스 HP바 위에 있는 타임 게이지UI 위에 보스 폭주를 알리는 두번째 아이콘을 띄우며 어느 위치에 띄울지를 정의하는 부분, 15분 즉 900000을 풀 게이지 기준으로 어느 위치에 띄울지를 정의함
        self.dungeon_set_lap_time(id=2, lap_time=720000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 첫번째페이즈_인페르녹전함(self.ctx)


class 첫번째페이즈_인페르녹전함(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SecondPhase') == 1:
            # 1페이즈 전투 진행하면서  SecondPhase = 1 신호를 받을때까지 여기서 대기
            return 두번째페이즈_인페르녹전함(self.ctx)


class 두번째페이즈_인페르녹전함(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 맨 오른쪽 건너편 막힌 벽 제거하기 ,    오른쪽 지점 대포 배치하기 위한 오프젝트는 TriggerObjectID: 6010, 6011  이거 제거해야 전투가 쾌적함
        self.set_mesh(trigger_ids=[6010,6011,6012,6013,6014,6015,6016], fade=0.5)
        # ## 한국용 던전랭크 코드: 인페르녹의 전함 측면파괴 던전랭크 달성을 위한 신호
        self.dungeon_mission_complete(feature='DungeonRankBalance_01', mission_id=24090007)
        # ## 중국용 던전랭크 코드: 인페르녹의 전함 측면파괴 던전랭크 달성을 위한 신호
        self.dungeon_mission_complete(feature='DungeonRankBalance_02', mission_id=24090017)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ThirdPhase') == 1:
            # 2페이즈 전투 진행하면서, 인페르녹 전함에게   ThirdPhase = 1 신호를 받을때까지 여기서 대기
            return 세번째페이즈_인페르녹등장(self.ctx)


class 세번째페이즈_인페르녹등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 위에서 선언한   <action name="DungeonSetLapTime" id="1" lapTime="420000" /> 의 첫번째 아이콘을(id="1") 현재 시간 기준 게이지 위치로 옮기고자 할때 이렇게 설정
        self.dungeon_move_lap_time_to_now(id=1)
        # 즉 보스가 등장하는 상황을 명확히 알리기 위한 목적으로 첫번째 아이콘을(id="1")  현재 시간 기준으로 이동시킴
        # 인페르녹 보스 스폰하기, 스폰ID : 102
        self.spawn_monster(spawn_ids=[102])
        self.set_sound(trigger_id=8410, enable=True) # 보스 등장하면 보스용 BGM으로 교체하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BalrogMagicBursterBattlePhase') == 1:
            # 인페르녹과 전투 시작할 때 몬스터 AI에서 이 신호를 보낼때까지 대기
            # 즉  BalrogMagicBursterBattlePhase = 1 신호를 AI에서 부터 트리거가  받을때까지 여기서 대기
            return 인페르녹전투시작(self.ctx)


class 인페르녹전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 트리거에서 인페르녹 보스 AI에게  Phase = 1 신호를 보내서, 행동에 영향 받도록 함
        self.set_ai_extra_data(key='Phase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_play_time() >= 720:
            # 던전 전투 시작 15분 중 라스트 3분 남았으면, 이 부분은 맵으로 바로 들어가지 말고 던전로직을 통해서 정식으로 입장해야 작동함
            return 네번째페이즈_인페르녹광폭화(self.ctx)


class 네번째페이즈_인페르녹광폭화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 트리거에서 인페르녹 보스 AI에게  Phase = 2 신호를 보내서, 광폭화 공격 스킬 사용하도록 함
        self.set_ai_extra_data(key='Phase', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
