""" trigger/02000426_bf/bossspawn.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        self.set_mesh(trigger_ids=[3000,3001])
        self.set_mesh(trigger_ids=[3002], visible=True)
        # 이 변수 신호 받아서 자쿰 몸체 등장시키는데 사용함
        self.set_user_value(key='ZakumBodyAppearance', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 던전코드별보스등장(self.ctx)


class 던전코드별보스등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_id() == 23040003:
            # 10인던전으로 입장하면 10인용 보스 등장,   dungeonID 의 숫자는 DungeonRoom.xlsx 에 정의된 던전코드
            return 어려운난이도보스등장(self.ctx)
        if self.dungeon_id() == 23041003:
            # 6인던전으로 입장하면 6인용 보스 등장
            return 쉬운난이도보스등장(self.ctx)
        if self.wait_tick(wait_tick=2000):
            # 그냥 테스트용으로 맵코드로 바로 들어왔으면 10인용 보스 등장
            return 어려운난이도보스등장(self.ctx)


class 어려운난이도보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False) # 어려운 난이도의 자쿰 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기(self.ctx)


class 쉬운난이도보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2002], auto_target=False) # 쉬운 난이도의 자쿰 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ZakumBodyAppearance') == 1:
            # AI_ZakumBrownImitation.xml 로 부터 신호 받아서 자쿰몸체를 스폰시키기
            return 자쿰몸체등장(self.ctx)
        if self.user_value(key='ZakumDungeonEnd') == 1:
            return 종료딜레이(self.ctx)
        if self.dungeon_timeout():
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 자쿰몸체등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이 변수 0 초기화 하여 무한루프 빠지는거 방지
        self.set_user_value(key='ZakumBodyAppearance', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_id() == 23040003:
            # 10인던전으로 입장하면 10인용 자쿰몸 등장,   dungeonID 의 숫자는 DungeonRoom.xlsx 에 정의된 던전코드
            return 어려운난이도_자쿰몸등장(self.ctx)
        if self.dungeon_id() == 23041003:
            # 4인던전으로 입장하면 4인용 자쿰몸 등장
            return 쉬운난이도_자쿰몸등장(self.ctx)
        if self.wait_tick(wait_tick=2000):
            # 그냥 테스트용으로 맵코드로 바로 들어왔으면 10인용 자쿰몸 등장
            return 어려운난이도_자쿰몸등장(self.ctx)


class 어려운난이도_자쿰몸등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2011], auto_target=False) # 어려운 난이도의 자쿰몸 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기(self.ctx)


class 쉬운난이도_자쿰몸등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2012], auto_target=False) # 쉬운 난이도의 자쿰몸 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_set_end_time() # 시간 기능 종료시킴
        self.dungeon_close_timer()
        # arg3="ZakumKritiasClear" 는 퀘스트와 트로피 업적 당설 완료 조건 처리 키값임, arg1="??" arg2="trigger" 은 해당 트리거 안에 만 있으면 클리어 처리 할때 사용하는 것인데, 이거 생략하면 맵 안에만 있으면 무조건 퀘스트와 트로피 업적을 완료 처리함
        self.set_achievement(achieve='ZakumKritiasClear')
        self.set_user_value(trigger_id=999103, key='BattleEnd', value=1)
        # 자쿰 팔 제거때 용암 올라오게 하는 트리거 xml 담당, 999102_Lavaflow.xml
        self.set_user_value(trigger_id=999102, key='BattleEnd2', value=1)
        # 계약의 토템에 의해 왼쪽 용암 올라오게 하는 트리거 xml 담당, 999108_Lavaflow.xm
        self.set_user_value(trigger_id=999108, key='BattleEnd2', value=1)
        # 계약의 토템에 의해 오른쪽 용암 올라오게 하는 트리거 xml 담당, 999109_Lavaflow.xml
        self.set_user_value(trigger_id=999109, key='BattleEnd2', value=1)
        # 자쿰 몸통 아래쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.set_mesh(trigger_ids=[3002])
        # 자쿰 몸통 위쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.set_mesh(trigger_ids=[3003])
        # 던전 클리어 하면 토템의 저주 자쿰의 저주 제거하기
        self.remove_buff(box_id=199, skill_id=50005300)
        self.remove_buff(box_id=199, skill_id=50005301)
        # 죽음의 저주 걸렸을때 자쿰 클리어 하면, 해제함
        self.remove_buff(box_id=199, skill_id=50001450)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.dungeon_clear()
            return 종료(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        self.set_user_value(trigger_id=999103, key='BattleEnd', value=1)
        # 자쿰 몸통 아래쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.set_mesh(trigger_ids=[3002])
        # 자쿰 몸통 위쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.set_mesh(trigger_ids=[3003])
        # 던전 클리어 하면 토템의 저주 자쿰의 저주 제거하기
        self.remove_buff(box_id=199, skill_id=50005300)
        self.remove_buff(box_id=199, skill_id=50005301)
        # 죽음의 저주 걸렸을때 자쿰 클리어 하면, 해제함
        self.remove_buff(box_id=199, skill_id=50001450)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_enable_give_up()


initial_state = 시작
