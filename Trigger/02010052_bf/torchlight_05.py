""" trigger/02010052_bf/torchlight_05.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7542]) # 얼음이 어는 소리
        self.set_mesh(trigger_ids=[6083,6084,6085,6086,6087,6088,6089,6090]) # 얼음!
        self.set_mesh(trigger_ids=[6071,6072,6073,6074,6075,6076,6077,6078,6079,6080,6081,6082]) # 벽 해제
        self.set_effect(trigger_ids=[7005]) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=708) >= 1:
            return freeze(self.ctx)


class freeze(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7542], visible=True) # 얼음이 어는 소리
        self.set_dialogue(type=1, spawn_id=994, script='$02010052_BF__TORCHLIGHT_05__0$', time=3) # 카나 말풍선 대사
        self.set_mesh(trigger_ids=[6071,6072,6073,6074,6075,6076,6077,6078,6079,6080,6081,6082], visible=True, start_delay=80, interval=100, fade=8.0) # 얼음!
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return idle_02(self.ctx)


class idle_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=200, text_id=20105201) # 화로를 공격하여 불을 붙이세요
        self.spawn_monster(spawn_ids=[105], auto_target=False) # 횃불 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[105]):
            return burn_state(self.ctx)


class burn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7505], visible=True) # 얼음 녹는 소리
        self.set_mesh(trigger_ids=[6071,6072,6073,6074,6075,6076,6077,6078,6079,6080,6081,6082], start_delay=800, interval=100, fade=8.0) # 벽 해제
        self.set_mesh(trigger_ids=[600001]) # 벽 해제 (투명 벽)
        self.set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_05__1$', arg3='3000')
        self.set_effect(trigger_ids=[7005], visible=True) # 횃불에 불이 붙는 이펙트
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return spawn_state(self.ctx)


class spawn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=205, text_id=20105202) # 카나를 쫓아가세요
        self.set_dialogue(type=1, spawn_id=994, script='$02010052_BF__TORCHLIGHT_05__2$', time=3) # 카나 말풍선 대사
        self.move_npc(spawn_id=994, patrol_name='MS2PatrolData_1007') # 카나의 분신 994 (이동)
        self.spawn_monster(spawn_ids=[510,511,512,513,514,515]) # 카나 정령 몬스터 등장
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return block_spawn(self.ctx)


class block_spawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6083,6084,6085,6086,6087,6088,6089,6090], visible=True, start_delay=80, interval=500, fade=8.0) # 얼음!


initial_state = idle
