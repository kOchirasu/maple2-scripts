""" trigger/02000551_bf/startportal.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 최초 입구에 있는 전투판으로 가는  포탈 최초에는 감추기
        self.set_portal(portal_id=11)
        self.set_effect(trigger_ids=[8101,8102,8103,8104,8105]) # 최초 시작 지점에 나오는 화살표 표시 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 포탈활성화(self.ctx)


class 포탈활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 최초 입구에 있는 전투판으로 가는  포탈 활성화
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)
        # self.set_effect(trigger_ids=[8101,8102,8103,8104,8105], visible=True) # 최초 시작 지점에 나오는 화살표 표시
        self.dungeon_enable_give_up(is_enable=True)
        self.set_event_ui(type=1, arg2='$02020140_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_timeout():
            # 던전 시간 다 된경우
            return 던전실패종료(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패종료(self.ctx)
        if self.wait_tick(wait_tick=30000):
            return 포탈감추기(self.ctx)


class 포탈감추기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11) # 전투판으로 가는  포탈  감추기
        # # 최초 시작 지점에 나오는 화살표 표시 끄기
        self.set_effect(trigger_ids=[8101,8102,8103,8104,8105])

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_timeout():
            # 던전 시간 다 된경우
            return 던전실패종료(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패종료(self.ctx)


class 던전실패종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 던전실패로 던전 종료되면 시작지점 포탈 다시 등장 풀기
        # 최초 입구에 있는 전투판으로 가는  포탈 활성화
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)


initial_state = 시작대기중
