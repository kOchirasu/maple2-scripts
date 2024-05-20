""" trigger/63000062_cs/main.xml """
import trigger_api


class 날짜체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') in [4]:
            # 수요일이면 사랑의 섬에서 둘이 만남 121 122
            return 만남(self.ctx)
        if self.day_of_week(desc='1(일)-7(토)') in [1,2,3,5,6,7]:
            # 수요일이 아니면 동섬, 서섬에 각각 떨어져 있음 111 112
            return 헤어짐(self.ctx)


class 만남(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111,112])
        self.spawn_monster(spawn_ids=[121,122], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') in [1,2,3,5,6,7]:
            # 수요일이 아니면 헤어짐
            return 헤어짐(self.ctx)


class 헤어짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[121,122])
        self.spawn_monster(spawn_ids=[111,112], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') in [4]:
            # 수요일이면 만남
            return 만남(self.ctx)


initial_state = 날짜체크
