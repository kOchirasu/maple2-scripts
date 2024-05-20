""" trigger/99999946/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[500,501,502,503,504,505,506,507,508,509], random_count=10)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006], auto_target=False)
        self.select_camera(trigger_id=301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_cube(trigger_ids=[500,501,502,503,504,505,506,507,508,509], random_count=3, is_visible=True)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
