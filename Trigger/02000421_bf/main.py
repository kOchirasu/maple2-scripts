""" trigger/02000421_bf/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(trigger_ids=[6001])
        self.set_mesh(trigger_ids=[6002])
        self.set_mesh(trigger_ids=[6003])
        self.set_mesh(trigger_ids=[6004])
        self.set_mesh(trigger_ids=[6005])
        self.set_mesh(trigger_ids=[6006])
        self.set_mesh(trigger_ids=[6007])
        self.set_mesh(trigger_ids=[6008])
        self.set_mesh(trigger_ids=[6009])
        self.set_mesh(trigger_ids=[6010])
        self.set_mesh(trigger_ids=[6011])
        self.set_mesh(trigger_ids=[6012])
        self.set_mesh(trigger_ids=[6013])
        self.set_mesh(trigger_ids=[6014])
        self.set_mesh(trigger_ids=[6015])
        self.set_mesh(trigger_ids=[6016])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=700) >= 1:
            return Ready_Idle(self.ctx)


class Ready_Idle(trigger_api.Trigger):
    pass


initial_state = Ready
