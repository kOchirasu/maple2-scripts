""" trigger/63000054_cs/01_portalevent.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 미니맵 아이콘 on/off 정보는 코드에서 visible 와 동일하게 제어되므로 트리거에서는 항상 켜놓는 값으로 설정한다.
        self.set_portal(portal_id=20007001, minimap_visible=True) # 자쿰
        self.set_portal(portal_id=20023001, minimap_visible=True) # 핑크빈
        self.create_widget(type='ReverseRaidPortal')


initial_state = Wait
