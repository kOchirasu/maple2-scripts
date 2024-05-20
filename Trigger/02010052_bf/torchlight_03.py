""" trigger/02010052_bf/torchlight_03.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=20499, initial_sequence='Closed')
        self.set_actor(trigger_id=20501, visible=True, initial_sequence='Closed') # 얼어붙은 문
        self.set_mesh(trigger_ids=[20500], visible=True, start_delay=1, interval=1, fade=1.0) # 철문
        self.set_effect(trigger_ids=[7002]) # 횃불에 불이 붙는 이펙트
        self.set_effect(trigger_ids=[7003]) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102]):
            return burn_state_01(self.ctx)
        if self.monster_dead(spawn_ids=[103]):
            return burn_state_02(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[71001], visible=True)
        self.set_effect(trigger_ids=[71002], visible=True)
        self.set_effect(trigger_ids=[71003], visible=True)
        self.set_effect(trigger_ids=[71004], visible=True)
        self.set_effect(trigger_ids=[71005], visible=True)
        self.set_actor(trigger_id=8001, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8002, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8003, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8004, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8005, initial_sequence='Dmg_A')
        self.spawn_monster(spawn_ids=[301,302,303,304,305], auto_target=False) # 기본 배치 될 몬스터 등장
        self.set_dialogue(type=1, spawn_id=993, script='$02010052_BF__TORCHLIGHT_03__0$', time=3) # 카나 말풍선 대사


class burn_state_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103]):
            return burn_state_complete(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[7003], visible=True)


class burn_state_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102]):
            return burn_state_complete(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[7002], visible=True)


class burn_state_complete(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7503], visible=True) # 얼음 녹는 소리
        self.set_mesh(trigger_ids=[6021,6022,6023,6024,6025,6026,6027,6028,6029,6030,6031,6032], start_delay=800, interval=100, fade=8.0) # 벽 해제
        self.set_dialogue(type=1, spawn_id=9999, script='$02010052_BF__TORCHLIGHT_03__1$', time=3) # 카나 말풍선 대사
        self.hide_guide_summary(entity_id=200)
        self.set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_03__2$', arg3='3000')
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return spawn_state(self.ctx)


class spawn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=299, text_id=20105203) # 거대 다크 슬링을 처치하세요
        self.set_mesh(trigger_ids=[5100,5101,5102,5103,5104,5105,5106,5107,5108,5109,5110], start_delay=800, interval=100, fade=8.0) # 카나 위에 있는 벽 해제
        self.set_effect(trigger_ids=[7902], visible=True) # 카나 사라짐
        self.destroy_monster(spawn_ids=[9999]) # 카나 사라짐
        self.set_actor(trigger_id=8100, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8006, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8007, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8008, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8009, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8010, initial_sequence='Dmg_A')
        self.spawn_monster(spawn_ids=[199]) # 얼음이 녹으며 등장하는 몬스터들 (중간)
        self.spawn_monster(spawn_ids=[321,322,323,324,325]) # 얼음이 녹으며 등장하는 몬스터들

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[199]):
            return monsterkill(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=299)


class monsterkill(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=20499, visible=True, initial_sequence='Opening')
        self.set_actor(trigger_id=20501, initial_sequence='Closed') # 얼어붙은 문
        self.set_mesh(trigger_ids=[20500]) # 철문


initial_state = idle
