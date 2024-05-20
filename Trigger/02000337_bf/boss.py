""" trigger/02000337_bf/boss.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7301])
        self.set_effect(trigger_ids=[7302])
        self.set_effect(trigger_ids=[7303])
        self.set_effect(trigger_ids=[7304])
        self.set_effect(trigger_ids=[7305])
        self.set_effect(trigger_ids=[7306])
        self.set_effect(trigger_ids=[7307])
        self.set_effect(trigger_ids=[7308])
        self.set_effect(trigger_ids=[7309])
        self.set_effect(trigger_ids=[7310], visible=True)
        self.set_portal(portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 폭발예고(self.ctx)


class 폭발예고(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=8002)
        self.set_mesh(trigger_ids=[6001,6002,6003,6004], fade=10.0) # 벽 해제
        self.set_effect(trigger_ids=[7308], visible=True) # 지진 이펙트
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 폭발(self.ctx)


class 폭발(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7306], visible=True) # 폭발 이펙트
        self.set_skill(trigger_ids=[8306], enable=True) # 벽 날리는 스킬
        self.set_skill(trigger_ids=[8307], enable=True) # 벽 날리는 스킬
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 폭발후(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 폭발후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8002, enable=False)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=111, text_id=20003371) # [b:기관실] 내부로 이동하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=705) >= 1:
            return 폭발후_02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=111)


class 폭발후_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=112, text_id=20003372) # 스위치를 작동시키세요
        self.set_interact_object(trigger_ids=[10000891], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000891], state=0):
            return 클리어(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=112)


class 클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])
        self.set_effect(trigger_ids=[7301])
        self.set_effect(trigger_ids=[7302])
        self.set_effect(trigger_ids=[7303])
        self.set_effect(trigger_ids=[7304])
        self.set_effect(trigger_ids=[7305])
        self.set_effect(trigger_ids=[7306])
        self.set_effect(trigger_ids=[7307])
        self.set_effect(trigger_ids=[7308])
        self.set_effect(trigger_ids=[7309])
        self.set_effect(trigger_ids=[7310])
        self.set_effect(trigger_ids=[7311])
        self.play_system_sound_in_box(sound='System_Dark_Ending_Chord_01')
        self.set_actor(trigger_id=5001, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=5002, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=5003, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=5004, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=5005, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=5006, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=5007, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=5008, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 웨이홍_대사01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)


class 웨이홍_대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[199]) # 웨이홍
        self.select_camera(trigger_id=8001)
        self.set_dialogue(type=2, spawn_id=11003124, script='$02000337_BF__BOSS__0$', time=3) # 웨이홍 대사
        self.set_skip(state=웨이홍_대사02)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 웨이홍_대사02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 웨이홍_대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003124, script='$02000337_BF__BOSS__1$', time=3) # 웨이홍 대사
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


class 웨이홍_대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003124, script='$02000337_BF__BOSS__2$', time=3) # 웨이홍 대사
        self.set_skip(state=종료)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear() # 해당 던전은 클리어 처리 됨
        # self.show_guide_summary(entity_id=112, text_id=40009) # 포탈을 타세요
        self.select_camera(trigger_id=8001, enable=False)
        self.set_dialogue(type=1, spawn_id=199, script='$02000337_BF__BOSS__3$', time=3, arg5=2) # 웨이홍 말풍선 대사
        self.set_portal(portal_id=10, visible=True, enable=True, minimap_visible=True) # 보상으로 연결되는 포탈 제어 (켬)


initial_state = 시작
