""" trigger/02000207_bf/999990_ground.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 자쿰과의 전투 장소 3층 지형의 일부 바닥 큐브를 숨김 처리함
        self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005,5006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ZakumBodyAppearance') == 1:
            return 층지형의숨겨진바닥생성3(self.ctx)


class 층지형의숨겨진바닥생성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 자쿰 본체 하고 전투가 시작되면 자쿰본체한테 신호 받아서 3층 지형의 일부 바닥이 생성되도록 함
        self.set_mesh(trigger_ids=[5001,5002,5003,5004,5005,5006], visible=True, start_delay=1, interval=120, fade=0.5)


initial_state = 시작대기중
