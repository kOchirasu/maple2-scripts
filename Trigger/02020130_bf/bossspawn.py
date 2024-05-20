""" trigger/02020130_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 공중에서 등장하는 소환몹이 밟는  트리거박스임
        self.set_mesh(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
        # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 2셋트 전투판에 배치된 포탈
        self.set_portal(portal_id=20)
        # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 1셋트 12시 전투판에 배치된 포탈
        self.set_portal(portal_id=21)
        # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 1셋트 8시 전투판에 배치된 포탈
        self.set_portal(portal_id=22)
        # 던전 클리어 되면 나가는 포탈 최초에는 감추기, 1셋트 4시 전투판에 배치된 포탈
        self.set_portal(portal_id=23)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[600]):
            # ID 600 인 트리거 박스 안에 플레어가 들어서면 보스 생성시키기, 660 ID 트리거 박스는 스타트 지점만 포함되는 영역임
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[701,702,703], auto_target=False) # 이슈라 렌듀비아 유페리아  등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[701,702,703]):
            return 종료딜레이(self.ctx)
        if self.dungeon_timeout():
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스 3마리 다 죽이면 제일 먼저 던전 시간 멈추게 하기
        self.dungeon_stop_timer()
        # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기, 던전 클리어 미션 달성임
        self.dungeon_mission_complete(mission_id=23040000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            # 보스 죽음 동작 연출이 끝날때까지 8초 정도 기다린 다음, 클리어 UI 화면연출 시작되도록 함
            self.dungeon_clear()
            # arg1 = "특정트리거 박스 안에 있는 유저만 체크하고자 할때"   arg2 = "trigger"    즉 trigger 이거만 쓸수 있음  특정 트리거 박스 안의 유저만 체크 방식을 사용하고자 할때 이 2개 넣어야 함
            self.set_achievement(achieve='IshuraFinalDungeonClear')
            # arg1 , arg2  넣지 않으면 맵 안에 있는 모든 유저에게 이 업적이 반영됨
            return 종료(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 던전 클리어 되면 나가는 포탈 등장 시키기
        self.set_portal(portal_id=20, visible=True, enable=True, minimap_visible=True)
        # 던전 클리어 되면 나가는 포탈 등장 시키기
        self.set_portal(portal_id=21, visible=True, enable=True, minimap_visible=True)
        # 던전 클리어 되면 나가는 포탈 등장 시키기
        self.set_portal(portal_id=22, visible=True, enable=True, minimap_visible=True)
        # 던전 클리어 되면 나가는 포탈 등장 시키기
        self.set_portal(portal_id=23, visible=True, enable=True, minimap_visible=True)
        self.dungeon_enable_give_up()


initial_state = 시작대기중
