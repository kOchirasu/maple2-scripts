""" trigger/02020130_bf/bridge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032])
        # 1셋트 전투 끝나야 나오는 순간이동 맵 내부 포탈 최초에 감추기
        self.set_portal(portal_id=8)
        # 1셋트 전투 끝나야 나오는 순간이동 맵 내부 포탈 최초에 감추기
        self.set_portal(portal_id=9)
        # 1셋트 전투 끝나서 2셋트 전투판으로 이동하는 순간이동 맵 내부 포탈 최초에 감추기
        self.set_portal(portal_id=12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[600]):
            # ID 600 인 트리거 박스 안에 플레어가 들어서면 보스 생성시키기, 이 트리거 박스 크기는 스타팅지점을 감싸는 비교적 작은 크기임
            return 작동대기상태(self.ctx)


class 작동대기상태(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BridgeAppear') >= 3:
            # 이슈라 랜듀비앙 유페리아 가 두번째 전투판으로 순간이동 하거나 죽을 때 이 변수 +1 신호를 보내서 3이 되면  다리생성 트리거 작동시킴
            # 이슈라 랜듀비앙 유페리아 가 두번째 전투판으로 순간이동 하거나 죽을 때 이 변수 +1 신호를 보내는데, 혹시 타이밍이 꼬여 이 숫자가 4 이상이 될 수도 있을거 같아서 안전하게 3 이상 으로 설정함(operator="GreaterEqual")
            return 다리생성(self.ctx)


class 다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1셋트 전투 끝나야 나오는, 8시 전투판 위에 있는 순간이동 맵 내부 포탈 최초에 감추기
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True)
        # 1셋트 전투 끝나야 나오는, 4시 전투판 위에 있는 순간이동 맵 내부 포탈 최초에 감추기
        self.set_portal(portal_id=9, visible=True, enable=True, minimap_visible=True)
        # BridgeSeconds, 두번째 전투판으로 이동하기 위한 다리가 순차적으로 생성
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032], visible=True, start_delay=1, interval=120, fade=0.5)
        # 1셋트 전투 끝나 2셋트 전투판으로 이동하는, 거대문의 순간이동 맵 내부 포탈 최초에 감추기
        self.set_portal(portal_id=12, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    pass


initial_state = 대기
