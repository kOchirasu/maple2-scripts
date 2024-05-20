""" trigger/02000352_bf/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)
        self.set_effect(trigger_ids=[900001]) # Sound EFfect Off
        self.set_effect(trigger_ids=[900002]) # Sound EFfect Off
        self.set_effect(trigger_ids=[900003]) # Sound EFfect Off
        self.set_effect(trigger_ids=[900004]) # Sound EFfect Off
        self.set_effect(trigger_ids=[900005]) # Sound EFfect Off
        self.set_interact_object(trigger_ids=[10000822], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return 관문01_시작(self.ctx)
        if self.count_users(box_id=703) >= 1:
            return 관문_03_시작(self.ctx)


class 관문01_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[11,12,13,14,15,16,17], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[11,12,13,14,15,16,17]):
            return 관문_01_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000822], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return 관문_02_시작(self.ctx)


class 관문_02_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.spawn_monster(spawn_ids=[21,22,23,24,25,26,27,28,29], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[21,22,23,24,25,26,27,28,29]):
            return 관문_02_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class 관문_02_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=111, text_id=20000080) # 스위치를 정지하세요
        self.set_interact_object(trigger_ids=[10000823], state=1)
        self.set_interact_object(trigger_ids=[10000824], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return 관문_03_시작(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=111)


class 관문_03_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[31,32,33], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[31,32]):
            return 관문_03_개방(self.ctx)


class 관문_03_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6004], fade=10.0) # 벽 해제
        self.set_mesh(trigger_ids=[6007], visible=True, fade=10.0) # 화살표 표시
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=112, text_id=40009) # 포탈을 타세요
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)


initial_state = 시작
