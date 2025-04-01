""" trigger/02000207_bf/bossspawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        self.set_mesh(trigger_ids=[3000,3001])
        self.set_mesh(trigger_ids=[3002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 소환(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ZakumDungeonEnd') == 1:
            return 종료딜레이(self.ctx)
        if self.dungeon_timeout():
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.dungeon_clear()
            return 종료(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_user_value(trigger_id=999103, key='BattleEnd', value=1)
        # 자쿰 몸통 아래쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.set_mesh(trigger_ids=[3002])
        # 자쿰 몸통 위쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        self.set_mesh(trigger_ids=[3003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_enable_give_up()


initial_state = 대기
