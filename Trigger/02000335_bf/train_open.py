""" trigger/02000335_bf/train_open.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6920]) # Train_bomb_03
        self.set_mesh(trigger_ids=[6091,6092,6093]) # 안보이는 상태
        self.set_interact_object(trigger_ids=[10000786], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=709) >= 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # [b:레버]를 조작하여 드럼통을 폭파시키세요.
        self.show_guide_summary(entity_id=113, text_id=20003363)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000786], state=0):
            return 작동_01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=113)


class 작동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6922], visible=True) # Train_bomb_03
        self.set_mesh(trigger_ids=[6081,6082,6083], interval=300, fade=10.0) # 빨간 선이
        self.set_mesh(trigger_ids=[6091,6092,6093], visible=True, interval=300, fade=10.0) # 파란 선으로
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 작동_02(self.ctx)


class 작동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6099,6076], interval=30) # 드럼통 폭발
        self.set_mesh(trigger_ids=[6091,6092,6093], fade=10.0) # 파란 선도 마저 삭제
        self.set_mesh(trigger_ids=[6000], interval=50, fade=1.0) # 유리창 해제
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벽제거(self.ctx)


class 벽제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6920], visible=True) # Train_bomb_03
        self.set_skill(trigger_ids=[5807], enable=True) # 벽 날리는 스킬
        self.set_skill(trigger_ids=[5808], enable=True) # 벽 날리는 스킬
        self.set_skill(trigger_ids=[5809], enable=True) # 벽 날리는 스킬
        self.set_mesh(trigger_ids=[7071,7072,7073,7074], interval=15, fade=8.0) # 벽 해제
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return 몬스터등장(self.ctx)


class 몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[113]) # 추가 이벤트 스폰 몬스터
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 관문_01_조건(self.ctx)


class 관문_01_조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=105, text_id=20003361) # 키 몬스터를 처치하세요.
        self.spawn_monster(spawn_ids=[115,116,137,139]) # 추가 이벤트 스폰 몬스터

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[113]):
            return 관문_01_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=105)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=106, text_id=20003362) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(trigger_ids=[6211,6212,6213,6214,6215,6216,6217,6218], fade=10.0) # 벽 해제
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 관문_01_개방_02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=106)


class 관문_01_개방_02(trigger_api.Trigger):
    pass


initial_state = 대기
