""" trigger/51000001_dg/endgame.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[144]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='0,0')
        self.select_camera(trigger_id=344)
        # self.set_event_ui(type=5, arg2='게임 오버', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.play_system_sound_in_box(sound='System_Ending_Popup_01')
            self.arcade_spring_farm_end_game()
            return 진짜끝(self.ctx)


class 진짜끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10, interval=1, v_offset=-30, type='TR')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 퇴장(self.ctx)


class 퇴장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()


initial_state = 대기
