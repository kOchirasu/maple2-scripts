""" trigger/02000551_bf/main.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portal_id=2) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portal_id=3) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portal_id=4) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portal_id=5) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portal_id=6) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portal_id=7) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portal_id=8) # 2페이즈 가는 포탈 최초에는 감추기
        self.set_portal(portal_id=9) # 2페이즈 가는 포탈 최초에는 감추기
        # 게임포기 할때 던전 밖으로 가는  다수 포탈  최초 감추기
        self.set_portal(portal_id=21)
        self.set_portal(portal_id=22)
        self.set_portal(portal_id=23)
        self.set_portal(portal_id=24)
        self.set_portal(portal_id=25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 난이도체크(self.ctx)


class 난이도체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_id() == 23050003:
            # 현재 입장한 던전ID가 23050003  이라면 ,<transition state="쉬운난이도보스등장" /> 실행
            return 쉬운난이도보스등장(self.ctx)
        if self.dungeon_id() == 23051003:
            # 현재 입장한 던전ID가 23051003  이라면 , <transition state="여려움난이도보스등장" /> 실행
            return 여려움난이도보스등장(self.ctx)
        if self.wait_tick(wait_tick=1100):
            # 던전 로직을 통해 입장하지 않고, 걍 디버그 모드 맵툴로 들어오면 이 부분 실행됨
            return 여려움난이도보스등장(self.ctx)


class 여려움난이도보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음, 스폰ID 101 어려움 난이도
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1800):
            return 일러스트대화창(self.ctx)


class 쉬운난이도보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음, 스폰ID 102 쉬운 난이도
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1800):
            return 일러스트대화창(self.ctx)


class 일러스트대화창(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23000101, illust='BlackBean_Smile', script='$02000551_BF__BOSSSPAWN__0$', duration=7000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2100):
            return 전투진행중(self.ctx)


class 전투진행중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='GuideMessage', value=0) # GuideMessage 0으로 초기 셋팅

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GuideMessage') == 1:
            # 자동차AI에서 GuideMessage = 1 신호를 보냄
            return 메시지출력(self.ctx)
        if self.user_value(key='NextPortal') == 1:
            # 블랙빈AI에서 NextPortal = 1 신호를 보냄
            return 다음진행딜레이(self.ctx)
        if self.dungeon_timeout():
            # 던전 시간 다 된경우
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 메시지출력(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 안내 메시지 호출하기
        self.show_guide_summary(entity_id=29200007, text_id=29200007, duration=7000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 전투진행중(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            self.dungeon_fail()
            return 게임오버(self.ctx)


class 게임오버(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # StartPortal.xml 트리거에서 <action name="DungeonEnableGiveUp" isEnable="1" /> 설정함
        self.dungeon_enable_give_up()
        # 게임포기 했으니 던전 밖으로 가는 다수 포탈  등장시키기
        self.set_portal(portal_id=21, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=22, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=23, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=24, visible=True, enable=True, minimap_visible=True)
        # 최초 입구에 있는 전투판으로 가는  포탈 다시 등장하기  StartPortal.xml 트리거에서 이 포탈 초기화 셋팅 감추기 등을 관리함
        self.set_portal(portal_id=25, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)


class 다음진행딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5800):
            return 다음맵가는포탈등장(self.ctx)


class 다음맵가는포탈등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 2페이즈 전투판으로 가는 포탈 등장하기
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True)
        # 최초 입구에 있는 전투판으로 가는  포탈 다시 등장하기  StartPortal.xml 트리거에서 이 포탈 초기화 셋팅 감추기 등을 관리함
        self.set_portal(portal_id=9, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)


initial_state = 시작대기중
