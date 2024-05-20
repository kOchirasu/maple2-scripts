""" trigger/02000336_bf/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[16003,16004]) # 벽 해제
        self.spawn_monster(spawn_ids=[122,123,301,302], auto_target=False) # 기본 배치 될 몬스터 등장
        self.spawn_monster(spawn_ids=[110,111,112,113,114,116,117,120,121,124,125,126,127,128,129,131,132,133,134,135,137,139,141,142,144], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return 관문_01_개방_준비(self.ctx)


class 관문_01_개방_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=105, text_id=20003361) # 키 몬스터를 처치하세요.
        self.spawn_monster(spawn_ids=[309,311,313,172,173], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[127]):
            return 관문_01_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=105)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(trigger_ids=[8010,8011,8012,8013,8014], fade=10.0) # 벽 해제
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[125]):
            return 관문_02_개방(self.ctx)


class 관문_02_개방_준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[127]):
            return 관문_01_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=113)


class 관문_02_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[16017,16018], fade=10.0) # 벽 해제


initial_state = 시작
