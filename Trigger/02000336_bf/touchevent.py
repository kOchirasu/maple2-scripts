""" trigger/02000336_bf/touchevent.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[118,119], auto_target=False) # 기본 배치 될 몬스터 등장


initial_state = 시작
