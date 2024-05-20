""" trigger/02000419_bf/1122338_barricade.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014]) # 시작지점 철창벽 셋팅 최초에는 숨김 설정

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[2000]):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000419_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 차단(self.ctx)


class 차단(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014], visible=True, start_delay=1, interval=1, fade=1.0) # 시작지점 철창벽 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2000]):
            return 차단해제(self.ctx)


class 차단해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014]) # 보스가 죽으면 시작지점 철창벽 제거


initial_state = 대기
