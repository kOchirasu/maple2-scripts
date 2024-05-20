""" trigger/02020140_bf/timecheck.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 던전시간체크(self.ctx)


class 던전시간체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 던전 Fail 처리용, 던전 나가기 포탈 처음에 감추기
        self.set_portal(portal_id=41)
        self.set_portal(portal_id=42)
        self.set_portal(portal_id=43)
        self.set_portal(portal_id=44)
        self.set_portal(portal_id=45)
        self.set_portal(portal_id=46)
        self.set_portal(portal_id=47)
        self.set_portal(portal_id=48)
        self.set_portal(portal_id=49)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_timeout():
            # 던전 시간 다 된경우
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        # 던전 Fail 처리, 던전 나가기 포탈 생성하기
        self.destroy_monster(spawn_ids=[-1])
        self.set_portal(portal_id=41, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=42, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=43, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=44, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=45, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=46, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=47, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=48, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=49, visible=True, enable=True, minimap_visible=True)
        # 이 맵에서 전투 끝났으니, 보스BGM끄고 일반BGM이 나오게 하기,  main.xml 트리거에서도 같은 BGM 교체 트리거 사용함
        self.set_sound(trigger_id=140140, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_enable_give_up()


initial_state = 시작대기중
