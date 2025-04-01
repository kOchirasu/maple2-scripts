""" trigger/02020120_bf/portalstage04.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        self.set_user_value(key='DungeonReset', value=0)
        # 어느지점 포탈을 활성화 시킬지 결정하는데 사용하는 변수
        self.set_user_value(key='Stage04', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 스테이지4_시작(self.ctx)


class 스테이지4_시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Stage04') == 11:
            return 스테이지4_왼쪽_왼쪽진행(self.ctx)
        if self.user_value(key='Stage04') == 12:
            return 스테이지4_왼쪽_왼쪽가운데진행(self.ctx)
        if self.user_value(key='Stage04') == 21:
            return 스테이지4_가운데_왼쪽가운데진행(self.ctx)
        if self.user_value(key='Stage04') == 22:
            return 스테이지4_가운데_오른쪽가운데진행(self.ctx)
        if self.user_value(key='Stage04') == 31:
            return 스테이지4_오른쪽_오른쪽가운데진행(self.ctx)
        if self.user_value(key='Stage04') == 32:
            return 스테이지4_오른쪽_오른쪽진행(self.ctx)


class 스테이지4_왼쪽_왼쪽진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4101, visible=True, enable=True, minimap_visible=True) # 4스테이지로 가는 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지4_왼쪽_왼쪽가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4102, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지4_가운데_왼쪽가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4201, visible=True, enable=True, minimap_visible=True) # 4스테이지로 가는 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지4_가운데_오른쪽가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4202, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지4_오른쪽_오른쪽가운데진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4301, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 스테이지4_오른쪽_오른쪽진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4302, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 혹시모를_던전리셋신호_대기(self.ctx)


class 혹시모를_던전리셋신호_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonReset') == 1:
            return Ready(self.ctx)


initial_state = Ready
