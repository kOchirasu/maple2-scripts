""" trigger/02000347_bf/main.xml """
import trigger_api


# 플레이어 감지
class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[9001]) # 사다리 가려
        self.set_ladder(trigger_ids=[9002]) # 사다리 가려
        self.set_ladder(trigger_ids=[9003]) # 사다리 가려
        self.set_portal(portal_id=4) # 보상으로 연결되는 포탈 제어 (끔)
        self.set_interact_object(trigger_ids=[10000787], state=0) # 보상 상태 (없음)
        self.set_mesh(trigger_ids=[6001,6011], visible=True) # 벽 생성
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010]) # 길 차단

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=60001) >= 1:
            return 오브젝티브_01(self.ctx)


class 오브젝티브_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 오브젝티브_02(self.ctx)


class 오브젝티브_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001,8002]) # 연출 카메라
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[101]) # 보스 등장
        # self.move_user(map_id=2000347, portal_id=3)
        self.set_cinematic_ui(type=3, script='$02000347_BF__MAIN1__0$') # 오브젝티브
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 시작_01(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


# 플레이어 감지하면 1초 대기
class 시작_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$02000347_BF__MAIN1__2$', count=3)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 시작_02(self.ctx)


class 시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[9001], visible=True, enable=True) # 사다리 보여
        self.set_ladder(trigger_ids=[9002], visible=True, enable=True) # 사다리 보여
        self.set_ladder(trigger_ids=[9003], visible=True, enable=True) # 사다리 보여

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 클리어(self.ctx)


class 클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True) # 보상으로 연결되는 포탈 제어 (on)
        self.set_event_ui(type=7, arg2='$02000347_BF__MAIN1__1$', arg3='3000')
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], visible=True, fade=10.0) # 길 생성
        self.set_mesh(trigger_ids=[6011]) # 벽 삭제
        self.set_interact_object(trigger_ids=[10000787], state=1) # 보상 상태 (없음)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 클리어_02(self.ctx)


class 클리어_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=110, text_id=40009) # 포탈 이용하세요


initial_state = 대기
