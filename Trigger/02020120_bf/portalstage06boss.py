""" trigger/02020120_bf/portalstage06boss.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        self.set_user_value(key='DungeonReset', value=0)
        # 어느지점 포탈을 활성화 시킬지 결정하는데 사용하는 변수
        self.set_user_value(key='Stage06', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 스테이지6_시작(self.ctx) # 스테이지 6 보스 전투판으로 가기


class 스테이지6_시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Stage06') == 11:
            return 스테이지6_왼쪽_가운데진행(self.ctx)
        if self.user_value(key='Stage06') == 21:
            return 스테이지6_가운데_가운데진행(self.ctx)
        if self.user_value(key='Stage06') == 31:
            return 스테이지6_오른쪽_가운데진행(self.ctx)


class 스테이지6_왼쪽_가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=6101, visible=True, enable=True, minimap_visible=True) # 6스테이지 보스로 가는 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지6_가운데_가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=6201, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지6_오른쪽_가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=6301, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6302, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6303, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6304, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 혹시모를_던전리셋신호_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonReset') == 1:
            return Ready(self.ctx)


initial_state = Ready
