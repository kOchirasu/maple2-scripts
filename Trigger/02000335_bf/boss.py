""" trigger/02000335_bf/boss.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=991, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=992)
        self.set_mesh(trigger_ids=[6311,6312,6313,6314,6315], visible=True, interval=1, fade=1.0) # 벽 생성
        # BG\Common\Eff_Com_ObjectShake.xml
        self.set_effect(trigger_ids=[6921])
        self.spawn_monster(spawn_ids=[149], auto_target=False) # 기본 배치 될 NPC 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=710) >= 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=105, text_id=20003361) # 키 몬스터를 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[149]):
            return 화물문_개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=105)


class 화물문_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=991)
        self.enable_spawn_point_pc(spawn_id=992, is_enable=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=106, text_id=20003362) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(trigger_ids=[7991,7992,7993]) # 문 파괴
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 화물문_개방_종료(self.ctx)
        if self.count_users(box_id=711) >= 1:
            return 보스등장연출_00(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=106)


class 화물문_개방_종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=711) >= 1:
            return 보스등장연출_00(self.ctx)


class 보스등장연출_00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000335_BF__BOSS__0$', arg3='3000')
        # BG\Common\Eff_Com_ObjectShake.xml
        self.set_effect(trigger_ids=[6921], visible=True)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 보스등장연출_01(self.ctx)


class 보스등장연출_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[141,142,143,144,145,146,147,148]) # 기본 배치 된 NPC 삭제
        self.set_skill(trigger_ids=[5801], enable=True) # 벽 날리는 스킬
        self.set_skill(trigger_ids=[5802], enable=True) # 벽 날리는 스킬
        self.set_effect(trigger_ids=[6911], visible=True)
        self.set_effect(trigger_ids=[6912], visible=True)
        self.spawn_monster(spawn_ids=[199], auto_target=False) # 보스 몬스터 등장
        self.move_npc(spawn_id=199, patrol_name='MS2PatrolData_1003')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 보스등장연출_02(self.ctx)
        if self.monster_dead(spawn_ids=[199]):
            return 포탈_개방(self.ctx)


class 보스등장연출_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[5803], enable=True) # 벽 날리는 스킬
        self.set_skill(trigger_ids=[5804], enable=True) # 벽 날리는 스킬
        self.set_effect(trigger_ids=[6913], visible=True)
        self.set_effect(trigger_ids=[6914], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 보스등장연출_03(self.ctx)
        if self.monster_dead(spawn_ids=[199]):
            return 포탈_개방(self.ctx)


class 보스등장연출_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[5805], enable=True) # 벽 날리는 스킬
        self.set_skill(trigger_ids=[5806], enable=True) # 벽 날리는 스킬
        self.set_effect(trigger_ids=[6915], visible=True)
        self.set_effect(trigger_ids=[6916], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[199]):
            return 포탈_개방(self.ctx)


class 포탈_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=112, text_id=40009) # 포탈을 타세요
        self.set_mesh(trigger_ids=[6311,6312,6313,6314,6315], fade=10.0) # 벽 해제
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True) # 포탈 개방

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=112)


initial_state = 대기
