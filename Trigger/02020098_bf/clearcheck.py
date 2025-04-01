""" trigger/02020098_bf/clearcheck.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10]):
            # MS2TriggerBox   TriggerObjectID = 10, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        10은 스타팅 포인트 지점만 커버하는 비교적 좁은 범위
            return 클리어성공유무체크시작(self.ctx)


class 클리어성공유무체크시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        """
        중요: 보스 죽음 체크를 <condition name="몬스터가죽어있으면" arg1="98">   <condition name="몬스터가죽어있으면" arg1="99"> 방식을 사용하지 않는 이유는 
                이 맵은 한맵에 2개 난이도가 존재하는데, 만약 스폰포인트 99로 보스가 등장할 하여 트리거가 이 단계에 오면 98 스폰 포인트의 보스가 죽은 것으로 처리해 버리기 때문에 
                 보스AI에서 죽을때 변수 신호 보내는 방식을 사용하였음
        """
        if self.user_value(key='BossDead') == 1:
            return 연출딜레이(self.ctx)
        if self.dungeon_timeout():
            # 던전 시간 다 된경우
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 연출딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg3="BalrogMagicBursterKritiasClear" 는 퀘스트와 트로피 업적 당설 완료 조건 처리 키값임, arg1="??" arg2="trigger" 은 해당 트리거 안에 만 있으면 클리어 처리 할때 사용하는 것인데, 이거 생략하면 맵 안에만 있으면 무조건 퀘스트와 트로피 업적을 완료 처리함
        self.set_achievement(achieve='BalrogMagicBursterKritiasClear')
        # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_set_end_time()
        self.dungeon_close_timer()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            # 보스 죽으면 보스 죽음 동작 충분히 본 다음에(7초 딜레이) 클리어 UI 나오도록 함
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        # 스타트포인트 지점의 칸막이 트리거메쉬 제거하기
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311])
        # 나가기 포탈 생성은 portal.xml 에서 설정함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 종료(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        # 스타트포인트 지점의 칸막이 트리거메쉬 제거하기
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311])
        self.destroy_monster(spawn_ids=[-1]) # 모든 구간에 나가기 포탈 생성하기
        # 보스 죽이면 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 1페이지 전투판에서 나가기 포탈
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 2페이지 7시 전투판에서 나가기 포탈
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 2페이지 5시 전투판에서 나가기 포탈
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 2페이지 12시 전투판에서 나가기 포탈
        self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)
        # 보스 죽이면 나가기 포탈 생성하기, 마지막 전투판에서 나가기 포탈
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_enable_give_up()


initial_state = 시작대기중
