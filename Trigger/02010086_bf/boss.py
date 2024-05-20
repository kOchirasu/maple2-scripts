""" trigger/02010086_bf/boss.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_npc(spawn_id=181, patrol_name='MS2PatrolData_1005')
        # self.move_npc(spawn_id=182, patrol_name='MS2PatrolData_1006')
        # self.move_npc(spawn_id=183, patrol_name='MS2PatrolData_1007')
        # self.move_npc(spawn_id=184, patrol_name='MS2PatrolData_1008')
        # self.move_npc(spawn_id=185, patrol_name='MS2PatrolData_1004')
        # self.move_npc(spawn_id=186, patrol_name='MS2PatrolData_1003')
        # self.move_npc(spawn_id=187, patrol_name='MS2PatrolData_1002')
        # self.move_npc(spawn_id=188, patrol_name='MS2PatrolData_1001')
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=799) >= 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[995,999,998])
        self.spawn_monster(spawn_ids=[199]) # (임시) 보스몹 스폰
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[199]):
            return 포탈_개방(self.ctx)
        if self.time_expired(timer_id='10'):
            return 소환_01(self.ctx)


class 소환_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[181,188]) # (임시) 보스몹 스폰
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[199]):
            return 포탈_개방(self.ctx)
        if self.time_expired(timer_id='10'):
            return 소환_02(self.ctx)


class 소환_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[182,187]) # (임시) 보스몹 스폰
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[199]):
            return 포탈_개방(self.ctx)
        if self.time_expired(timer_id='10'):
            return 소환_03(self.ctx)


class 소환_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[183,186]) # (임시) 보스몹 스폰
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[199]):
            return 포탈_개방(self.ctx)
        if self.time_expired(timer_id='10'):
            return 소환_04(self.ctx)


class 소환_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[184,185]) # (임시) 보스몹 스폰
        self.set_timer(timer_id='20', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[199]):
            return 포탈_개방(self.ctx)
        if self.time_expired(timer_id='20'):
            return 소환_05(self.ctx)


class 소환_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[996]) # (임시) 보스몹 스폰

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[199]):
            return 포탈_개방(self.ctx)


class 포탈_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[181,182,183,184,185,186,187,188,997,996,995])
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=112, text_id=40009) # 포탈을 타세요
        self.set_mesh(trigger_ids=[1098], fade=10.0) # 벽 해제
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True) # 포탈 개방

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=112)


initial_state = 대기
