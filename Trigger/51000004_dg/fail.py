""" trigger/51000004_dg/fail.xml """
import trigger_api


class gameset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8011, enable=False) # 카메라 옆으로 보냄, 줌인

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Fail') == 1:
            return Fail_condition(self.ctx)


class Fail_condition(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return Fail(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Result_01')
        self.write_log(log_name='PinkBeanThreeTwoOne_log', trigger_id=9001, event='char_event', sub_event='gameover')
        self.set_timer(timer_id='10', seconds=10, display=True)
        self.select_camera_path(path_ids=[8011,8010], return_view=False) # 카메라 뒤로 당김
        self.arcade_three_two_one_end_game()

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()


initial_state = gameset
