""" trigger/02000551_bf/portalspeedracingmode.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 순간이동포탈감추기(self.ctx)


class 순간이동포탈감추기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 12시 3시 6시 9시 넓은 전투판의 순간이동 포탈
        self.set_portal(portal_id=12000)
        self.set_portal(portal_id=3000)
        self.set_portal(portal_id=6000)
        # 4계절 도로에 2개씩 배치한 순간이동 포탈
        self.set_portal(portal_id=9000)
        self.set_portal(portal_id=12201)
        self.set_portal(portal_id=12202)
        self.set_portal(portal_id=4501)
        self.set_portal(portal_id=4502)
        self.set_portal(portal_id=7801)
        self.set_portal(portal_id=7802)
        self.set_portal(portal_id=10111)
        # 중앙 넓은 전투판에서 12시 3시 6시 9시 넓은 전투판으로 가는 순간이동 포탈
        self.set_portal(portal_id=10112)
        self.set_portal(portal_id=13003)
        self.set_portal(portal_id=13006)
        self.set_portal(portal_id=13009)
        self.set_portal(portal_id=13012) # 다리도로에 1개씩 배치한 순간이동 포탈
        self.set_portal(portal_id=13121)
        self.set_portal(portal_id=13031)
        self.set_portal(portal_id=13061)
        self.set_portal(portal_id=13091)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpeedRacingMode') == 1:
            # 블랙빈 AI에서 이 신호를 SpeedRacingMode = 1 보냄
            return 순간이동포탈등장(self.ctx)
        if self.user_value(key='SpeedRacingMode') == 2:
            # 블랙빈 AI에서 이 신호를 SpeedRacingMode = 2 보냄, 1페이지 블랙빈이 죽으면 보내는 숫자 2
            return 종료딜레이(self.ctx)


class 순간이동포탈등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 12시 3시 6시 9시 넓은 전투판의 순간이동 포탈
        self.set_portal(portal_id=12000, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3000, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6000, visible=True, enable=True, minimap_visible=True)
        # 4계절 도로에 2개씩 배치한 순간이동 포탈
        self.set_portal(portal_id=9000, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=12201, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=12202, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4501, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4502, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=7801, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=7802, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=10111, visible=True, enable=True, minimap_visible=True)
        # 중앙 넓은 전투판에서 12시 3시 6시 9시 넓은 전투판으로 가는 순간이동 포탈
        self.set_portal(portal_id=10112, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13003, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13006, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13009, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13012, visible=True, enable=True, minimap_visible=True) # 다리도로에 1개씩 배치한 순간이동 포탈
        self.set_portal(portal_id=13121, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13031, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13061, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13091, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpeedRacingMode') == 0:
            # 블랙빈 AI에서 이 신호를 SpeedRacingMode = 0 보냄
            return 잠시대기(self.ctx)


class 잠시대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 순간이동포탈감추기(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3800):
            return 순간이동포탈등장(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
