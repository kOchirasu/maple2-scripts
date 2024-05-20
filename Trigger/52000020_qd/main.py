""" trigger/52000020_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[60001022], quest_states=[1]):
            return camera_01(self.ctx)


class camera_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return monster_spawn_01(self.ctx)


class monster_spawn_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[111,112,113,114]) # 1차 스폰
        self.set_dialogue(type=1, spawn_id=111, script='$52000020_QD__MAIN__2$', time=5)
        self.set_dialogue(type=1, spawn_id=112, script='$52000020_QD__MAIN__3$', time=5)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return battle_01(self.ctx)
        if self.monster_dead(spawn_ids=[111,112,113,114]):
            return camera_02(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class battle_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111,112,113,114]):
            return camera_02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class camera_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='1', seconds=1)
        self.select_camera_path(path_ids=[8003,8004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return monster_spawn_02(self.ctx)


class monster_spawn_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[121,122,123,124,125,126]) # 2차 스폰
        self.set_dialogue(type=1, spawn_id=121, script='$52000020_QD__MAIN__4$', time=5)
        self.set_dialogue(type=1, spawn_id=124, script='$52000020_QD__MAIN__5$', time=5)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return battle_02(self.ctx)
        if self.monster_dead(spawn_ids=[121,122,123,124,125,126]):
            return camera_03(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class battle_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[121,122,123,124,125,126]):
            return camera_03(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class camera_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='1', seconds=1)
        self.select_camera_path(path_ids=[8005,8006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return monster_spawn_03(self.ctx)


class monster_spawn_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[131,132,133,134,135,136]) # 3차 스폰
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return battle_03(self.ctx)
        if self.monster_dead(spawn_ids=[131,132,133,134,135,136]):
            return complete(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_dialogue(type=1, spawn_id=131, script='$52000020_QD__MAIN__1$', time=5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class battle_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[131,132,133,134,135,136]):
            return complete(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class complete(trigger_api.Trigger):
    pass


initial_state = idle
