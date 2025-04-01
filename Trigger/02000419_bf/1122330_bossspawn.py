""" trigger/02000419_bf/1122330_bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스 Kill하고 맵에 나가기 포탈 초기화 설정
        self.set_portal(portal_id=2)
        # 보스 Kill하고 맵에 나가기 포탈 초기화설정
        self.set_portal(portal_id=3)
        # 스타팅 포인트에서 다리가 사라지면 맵으로 바로 순간이동하는 맵 내부 포탈 설정
        self.set_portal(portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 몬스터등장(self.ctx)


class 몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2000], auto_target=False)
        # BridgeSeconds 지점의 다리 순차적으로 제거하기
        self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], interval=200, fade=0.5)
        # 시작지점에서 전투판으로 순간이도 시켜주는 포탈 생성
        self.set_portal(portal_id=10, visible=True, enable=True, minimap_visible=True)
        # BridgeStart  지점의 다리 순차적으로 제거하기
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025], interval=200, fade=0.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NextMove') == 1: # 보스가 죽을 경우
            return 두번째전투판이동다리생성(self.ctx)
        if self.monster_dead(spawn_ids=[2000]):
            return 연출딜레이(self.ctx)


class 두번째전투판이동다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # BridgeSeconds, 두번째 전투판으로 이동하기 위한 다리가 순차적으로 생성
        self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], visible=True, start_delay=1, interval=120, fade=0.5)
        # 두번째 전투판으로 이동하기 위한 다리가 생성되면 5001 : 투명 벽 제거하기, 5002 : 지란트 소환몹이 등장하는 곳에 설치된 투명벽도 제거하기
        self.set_mesh(trigger_ids=[5001,5002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2000]):
            return 연출딜레이(self.ctx)


class 연출딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스 죽이면 나가기 포탈 생성하기, 두번째 전투판에서 생성
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 첫번째 전투판에서 생성
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        # 스타팅 포인트에서 다리가 사라지면 맵으로 바로 순간이동하는 맵 내부 포탈 설정
        self.set_portal(portal_id=10)
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025], visible=True, start_delay=1, interval=1, fade=1.0) # BridgeStart
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014]) # 시작지점 철창벽
        # 원래 이 설정은 보스가 두번째 전투판 점프 이동할 때 설정하는 것인데,  점프 이동 없이 첫번째 전투판에서 보스가 죽을 수도 있기 때문에 여기서도 다시한번 설정함
        # BridgeSeconds, 두번째 전투판으로 이동하기 위한 다리가 순차적으로 생성
        self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015], visible=True, start_delay=1, interval=120, fade=0.5)
        # 두번째 전투판으로 이동하기 위한 다리가 생성되면 5001 : 투명 벽 제거하기, 5002 : 지란트 소환몹이 등장하는 곳에 설치된 투명벽도 제거하기
        self.set_mesh(trigger_ids=[5001,5002])
        self.dungeon_clear()


initial_state = 시작대기중
