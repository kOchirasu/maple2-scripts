""" trigger/02010086_bf/laser_01.xml """
import trigger_api


class 레이저_01_소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=712) >= 1:
            return 레이저_02(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[999])


class 레이저_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=707) >= 1:
            return 레이저_02_생성(self.ctx)


class 레이저_02_생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[998]) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=708) >= 1:
            return 레이저_03_생성(self.ctx)


class 레이저_03_생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[995]) # 몬스터 등장


initial_state = 레이저_01_소멸
