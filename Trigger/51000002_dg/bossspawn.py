""" trigger/51000002_dg/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 여기서 모든 웨폰 오브젝트 set
        self.set_cube(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020], is_visible=True)
        self.arcade_boom_boom_ocean_start_game(life_count=20)
        self.select_camera_path(path_ids=[8001], return_view=False) # 카메라 뒤로 당김
        self.set_portal(portal_id=2)
        # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음
        self.spawn_monster(spawn_ids=[99], auto_target=False)
        self.set_timer(timer_id='6100', seconds=6100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료체크(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 종료체크(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[99])


class 종료체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = 시작대기중
