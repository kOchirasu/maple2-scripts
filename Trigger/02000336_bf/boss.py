""" trigger/02000336_bf/boss.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90,92,93])
        self.set_portal(portal_id=1) # 보상으로 연결되는 포탈 제어 (끔)
        self.set_effect(trigger_ids=[7001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return 시작_01(self.ctx)


class 시작_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7015], visible=True)
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 조직원등장(self.ctx)


class 조직원등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001], visible=True)
        self.set_mesh(trigger_ids=[8041,8042,8043,8044], fade=10.0) # 벽 해제
        self.set_skill(trigger_ids=[5801], enable=True) # 벽 날리는 스킬
        self.spawn_monster(spawn_ids=[181,182,183])
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 웨이홍_대사01(self.ctx)


class 웨이홍_대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[91])
        self.destroy_monster(spawn_ids=[90])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=8001)
        self.set_dialogue(type=2, spawn_id=11003124, script='$02000336_BF__BOSS__0$', time=3) # 웨이홍 대사
        self.set_skip(state=웨이홍_대사02)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 웨이홍_대사02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 웨이홍_대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003124, script='$02000336_BF__BOSS__1$', time=3) # 웨이홍 대사
        self.set_skip(state=종료)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=112, text_id=40009) # 포탈을 타세요
        self.select_camera(trigger_id=8001, enable=False)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True) # 보상으로 연결되는 포탈 제어 (켬)


initial_state = 시작
