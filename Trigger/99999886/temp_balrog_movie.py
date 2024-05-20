""" trigger/99999886/temp_balrog_movie.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=200, initial_sequence='Idle_A') # 인비저블 상태

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 연출시작(self.ctx)

    def on_exit(self) -> None:
        self.select_camera_path(path_ids=[101,102], return_view=False)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=7)
        self.set_actor(trigger_id=200, visible=True, initial_sequence='Skill_Chain_Ready_A') # 비저블 상태

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


initial_state = 시작대기중
