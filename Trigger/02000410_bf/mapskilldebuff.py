""" trigger/02000410_bf/mapskilldebuff.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[444]) # 맵 스킬 초기화 셋팅
        self.set_skill(trigger_ids=[666]) # 맵 스킬 초기화 셋팅

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면           750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        # 언제든지  파티원이 전멸하거나 파티장이 던전 포기를 해서 몬스터가 전부 제거 될 수 있어서, 맵셋팅 스킬은 트리거 영역 안의 몬스터가 없으면 꺼지도록 매 턴마다 체크할 수 있도록 함
        if self.dungeon_play_time() >= 600:
            # 플레이 시간이 10분 되면, 1단계 필수 아이템 없는 유저 디버프로 죽이기, 이 것은 인페르녹이 스킬로 사용하는데, 혹시 보스쪽이 오류라면 대박 버그라서 안정 장치로 맵트리거 설정도 넣음
            return 단계_70000103_1(self.ctx)
        if not self.npc_detected(box_id=700, spawn_ids=[0]):
            # MS2TriggerBox   TriggerObjectID = 700 , 이 트리거 박스 안에 플레이어가 한명도 없다면, 700은 전투판만 포함되는 범위, 750은 스타팅 지점 전투판 다  포함되는 범위
            # arg2 에는  SpawnPointID를 넣는데, 여기에 0 넣으면 모든 몬스터 전부 체크함
            return 스킬끄기(self.ctx)


class 단계_70000103_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[444], enable=True) # 70000103  스킬 사용함

    def on_tick(self) -> trigger_api.Trigger:
        # 언제든지  파티원이 전멸하거나 파티장이 던전 포기를 해서 몬스터가 전부 제거 될 수 있어서, 맵셋팅 스킬은 트리거 영역 안의 몬스터가 없으면 꺼지도록 매 턴마다 체크할 수 있도록 함
        if self.dungeon_play_time() >= 780:
            # 플레이 시간이 13분 되면, 2단계 필수 아이템 없는 유저 디버프로 죽이기, 이 것은 인페르녹이 스킬로 사용하는데, 혹시 보스쪽이 오류라면 대박 버그라서 안정 장치로 맵트리거 설정도 넣음
            return 단계_70000104_2(self.ctx)
        if not self.npc_detected(box_id=700, spawn_ids=[0]):
            # MS2TriggerBox   TriggerObjectID = 700 , 이 트리거 박스 안에 플레이어가 한명도 없다면, 700은 전투판만 포함되는 범위, 750은 스타팅 지점 전투판 다  포함되는 범위
            # arg2 에는  SpawnPointID를 넣는데, 여기에 0 넣으면 모든 몬스터 전부 체크함
            return 스킬끄기(self.ctx)


class 단계_70000104_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[666], enable=True) # 70000104 스킬 사용함

    def on_tick(self) -> trigger_api.Trigger:
        # 언제든지  파티원이 전멸하거나 파티장이 던전 포기를 해서 몬스터가 전부 제거 될 수 있어서, 맵셋팅 스킬은 트리거 영역 안의 몬스터가 없으면 꺼지도록 매 턴마다 체크할 수 있도록 함
        if self.dungeon_play_time() >= 900:
            # 플레이 시간이 15분 되면, 2개 맵스킬 끄기
            return 스킬끄기(self.ctx)
        if not self.npc_detected(box_id=700, spawn_ids=[0]):
            # MS2TriggerBox   TriggerObjectID = 700 , 이 트리거 박스 안에 플레이어가 한명도 없다면, 700은 전투판만 포함되는 범위, 750은 스타팅 지점 전투판 다  포함되는 범위
            # arg2 에는  SpawnPointID를 넣는데, 여기에 0 넣으면 모든 몬스터 전부 체크함
            return 스킬끄기(self.ctx)


class 스킬끄기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[444]) # 맵 스킬 끄기
        # 던전실패 하거나 던전성공 하거나 어쨌든 끝나면 혹시 몸에 걸려있는 지옥의 불 시리즈 디버프를 제거해 주기 위해 아래 애디셔널을 걸어줌
        self.set_skill(trigger_ids=[666])
        # 지옥의 불 디버프 제거해주는 애디샤날던 던전 끝나면 걸어주기, MS2TriggerBox   TriggerObjectID = 750,   750은 스타팅 지점 전투판 다  포함되는 범위
        self.add_buff(box_ids=[750], skill_id=50004524, level=1, is_player=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
