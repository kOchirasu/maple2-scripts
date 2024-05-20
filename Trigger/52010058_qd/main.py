""" trigger/52010058_qd/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9010) >= 2:
            return 성공연출시작(self.ctx)


class 성공연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='common\\WorldInvasionScene6.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return quit02(self.ctx)
        if self.wait_tick(wait_tick=9000):
            return quit02(self.ctx)


class quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000422, portal_id=3)


initial_state = Ready
