""" trigger/02010060_bf/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 남쪽 넓게 설정
        self.set_mesh(trigger_ids=[6001])
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 10시쪽 끊어진 다리 지점
        self.set_mesh(trigger_ids=[6002])
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 2시쪽 끊어진 다리 지점
        self.set_mesh(trigger_ids=[6003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=700) >= 1:
            return Ready_Idle(self.ctx)


class Ready_Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)


initial_state = Ready
