""" trigger/52000065_qd/tutorial.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1000], visible=True) # 강철 결계
        self.set_mesh(trigger_ids=[2000], visible=True) # Invisible
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=10)
        self.set_portal(portal_id=20)
        self.set_portal(portal_id=30)
        self.set_portal(portal_id=40)
        self.set_portal(portal_id=50)
        self.set_portal(portal_id=60)
        self.set_portal(portal_id=70)
        self.set_portal(portal_id=80)
        self.create_widget(type='Guide')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 영상재생_01(self.ctx)


class 영상재생_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='common\\Common_Opening.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상완료_01(self.ctx)
        if self.wait_tick(wait_tick=190000):
            return 영상완료_01(self.ctx)


class 영상완료_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Guide', name='IsTriggerEvent') == 251:
            # 가이드 To 트리거 -: 몹 생성
            return 몬스터소환(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 해제(self.ctx)


class 해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1000]) # 강철 결계
        self.set_mesh(trigger_ids=[2000]) # Invisible
        self.guide_event(event_id=260)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001], job_code=90):
            # 룬 블레이더
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            self.start_tutorial()
        if self.user_detected(box_ids=[9001], job_code=110):
            # 소울바인더
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            self.start_tutorial()
        if self.user_detected(box_ids=[9001], job_code=100):
            # 스트라이커
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            self.start_tutorial()
        if self.user_detected(box_ids=[9001], job_code=1):
            # 초보자
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            self.start_tutorial()
        if self.user_detected(box_ids=[9001], job_code=10):
            # 나이트
            self.set_portal(portal_id=10, visible=True, enable=True, minimap_visible=True)
        if self.user_detected(box_ids=[9001], job_code=20):
            # 버서커
            self.set_portal(portal_id=20, visible=True, enable=True, minimap_visible=True)
        if self.user_detected(box_ids=[9001], job_code=30):
            # 위자드
            self.set_portal(portal_id=30, visible=True, enable=True, minimap_visible=True)
        if self.user_detected(box_ids=[9001], job_code=40):
            # 프리스트
            self.set_portal(portal_id=40, visible=True, enable=True, minimap_visible=True)
        if self.user_detected(box_ids=[9001], job_code=50):
            # 레인저
            self.set_portal(portal_id=50, visible=True, enable=True, minimap_visible=True)
        if self.user_detected(box_ids=[9001], job_code=60):
            # 헤비거너
            self.set_portal(portal_id=60, visible=True, enable=True, minimap_visible=True)
        if self.user_detected(box_ids=[9001], job_code=70):
            # 시프
            self.set_portal(portal_id=70, visible=True, enable=True, minimap_visible=True)
        if self.user_detected(box_ids=[9001], job_code=80):
            # 어쌔신
            self.set_portal(portal_id=80, visible=True, enable=True, minimap_visible=True)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
