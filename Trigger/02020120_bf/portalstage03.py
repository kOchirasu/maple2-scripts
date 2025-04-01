""" trigger/02020120_bf/portalstage03.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        self.set_user_value(key='DungeonReset', value=0)
        # 어느지점 포탈을 활성화 시킬지 결정하는데 사용하는 변수
        self.set_user_value(key='Stage03', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 스테이지3_시작(self.ctx)


class 스테이지3_시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Stage03') == 11:
            return 스테이지3_왼쪽_왼쪽진행(self.ctx)
        if self.user_value(key='Stage03') == 12:
            return 스테이지3_왼쪽_가운데진행(self.ctx)
        if self.user_value(key='Stage03') == 21:
            return 스테이지3_가운데_왼쪽진행(self.ctx)
        if self.user_value(key='Stage03') == 22:
            return 스테이지3_가운데_가운데진행(self.ctx)
        if self.user_value(key='Stage03') == 23:
            return 스테이지3_가운데_오른쪽진행(self.ctx)
        if self.user_value(key='Stage03') == 31:
            return 스테이지3_오른쪽_가운데진행(self.ctx)
        if self.user_value(key='Stage03') == 32:
            return 스테이지3_오른쪽_오른쪽진행(self.ctx)


class 스테이지3_왼쪽_왼쪽진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3101, visible=True, enable=True, minimap_visible=True) # 3스테이지로 가는 포탈 생성
        self.set_portal(portal_id=3102, visible=True, enable=True, minimap_visible=True) # 3스테이지로 가는 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지3_왼쪽_가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3103, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3104, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지3_가운데_왼쪽진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3201, visible=True, enable=True, minimap_visible=True) # 3스테이지로 가는 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지3_가운데_가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3202, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지3_가운데_오른쪽진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3203, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지3_오른쪽_가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3301, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3302, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3303, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지3_오른쪽_오른쪽진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3304, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3305, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3306, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 혹시모를_던전리셋신호_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonReset') == 1:
            return Ready(self.ctx)


initial_state = Ready
