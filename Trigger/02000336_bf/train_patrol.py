""" trigger/02000336_bf/train_patrol.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7002])
        self.set_effect(trigger_ids=[7003])
        self.set_effect(trigger_ids=[7004])
        self.set_mesh(trigger_ids=[16004]) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=704) >= 1:
            return 패트롤_01(self.ctx)
        if self.count_users(box_id=707) >= 1:
            return 패트롤_03(self.ctx)


class 패트롤_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[147,148,149], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=707) >= 1:
            return 패트롤_03(self.ctx)


class 패트롤_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 기본 배치 될 몬스터 등장
        pass


class 패트롤_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=105, text_id=20003361) # 키 몬스터를 처치하세요.
        self.spawn_monster(spawn_ids=[191,192,193,194,195,196,197,198], auto_target=False)
        self.set_effect(trigger_ids=[7002], visible=True)
        self.set_skill(trigger_ids=[5803], enable=True) # 벽 날리는 스킬
        self.set_skill(trigger_ids=[5804], enable=True) # 벽 날리는 스킬
        self.set_skill(trigger_ids=[5805], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[196]):
            return 관문_03_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=105)


class 관문_03_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(trigger_ids=[8030,8031,8032,8033,8034], fade=10.0) # 벽 해제


initial_state = 시작
