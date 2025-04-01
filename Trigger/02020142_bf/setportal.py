""" trigger/02020142_bf/setportal.xml """
import trigger_api


class 전투체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 대기99(self.ctx) # 테스트용


class 대기99(trigger_api.Trigger):
    pass


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1스테이지에서 맨 왼쪽 지점으로 진행하는 포탈
        self.set_portal(portal_id=118)
        self.set_portal(portal_id=128) # 1스테이지에서 가운데 지점으로 진행하는 포탈
        # 1스테이지에서 맨 오른쪽 지점으로 진행하는 포탈
        self.set_portal(portal_id=138)
        # 맨 왼쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portal_id=218)
        # 가운데 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portal_id=228)
        # 맨 오른쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portal_id=238)
        # 맨 왼쪽 지점에서 보스 전투판으로 넘어가는 포탈
        self.set_portal(portal_id=318)
        # 가운데 지점에서 마지막 스테이지로 넘어가는 포탈
        self.set_portal(portal_id=328)
        # 맨 오른쪽 지점에서 보스 전투판으로 넘어가는 포탈
        self.set_portal(portal_id=338)
        # 가운데 지점 마지막 스테이지에서 보스 전투판으로 넘어가는 포탈
        self.set_portal(portal_id=428)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            # waitTick 시간 조절을 넣음
            return 포탈생성(self.ctx)
        if self.user_value(key='SetLight') == 1:
            return 포탈생성(self.ctx)


class 포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1스테이지에서 맨 왼쪽 지점으로 진행하는 포탈
        self.set_portal(portal_id=118, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=128, visible=True, enable=True, minimap_visible=True) # 1스테이지에서 가운데 지점으로 진행하는 포탈
        # 1스테이지에서 맨 오른쪽 지점으로 진행하는 포탈
        self.set_portal(portal_id=138, visible=True, enable=True, minimap_visible=True)
        # 맨 왼쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portal_id=218, visible=True, enable=True, minimap_visible=True)
        # 가운데 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portal_id=228, visible=True, enable=True, minimap_visible=True)
        # 맨 오른쪽 지점 2스테이지에서 다음 단계 넘어가는 포탈
        self.set_portal(portal_id=238, visible=True, enable=True, minimap_visible=True)
        # 맨 왼쪽 지점에서 보스 전투판으로 넘어가는 포탈
        self.set_portal(portal_id=318, visible=True, enable=True, minimap_visible=True)
        # 가운데 지점에서 마지막 스테이지로 넘어가는 포탈
        self.set_portal(portal_id=328, visible=True, enable=True, minimap_visible=True)
        # 맨 오른쪽 지점에서 보스 전투판으로 넘어가는 포탈
        self.set_portal(portal_id=338, visible=True, enable=True, minimap_visible=True)
        # 가운데 지점 마지막 스테이지에서 보스 전투판으로 넘어가는 포탈
        self.set_portal(portal_id=428, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 전투체크
