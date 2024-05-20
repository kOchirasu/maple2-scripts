""" trigger/52000039_qd/main.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.hide_guide_summary(entity_id=20020030)
        self.hide_guide_summary(entity_id=20020031)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003054], quest_states=[3]):
            # 다시 돌아오다 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003054], quest_states=[2]):
            # 다시 돌아오다 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003054], quest_states=[1]):
            # 다시 돌아오다 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[3]):
            # 스승의 발자취 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[2]):
            # 스승의 발자취 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[1]):
            # 스승의 발자취 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003052], quest_states=[3]):
            # 멈출 수 없어 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003052], quest_states=[2]):
            # 멈출 수 없어 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003052], quest_states=[1]):
            # 멈출 수 없어 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003051], quest_states=[3]):
            # 진심어린 충고 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003051], quest_states=[2]):
            # 진심어린 충고 퀘스트
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003051], quest_states=[1]):
            # 진심어린 충고 퀘스트 수락한 상태
            self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(trigger_ids=[6001])
            self.set_mesh(trigger_ids=[6010])
            self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
            return PCPatrol01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002635], quest_states=[3]):
            # 포탈 생성 되어있음
            self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(trigger_ids=[6001])
            self.set_mesh(trigger_ids=[6010])
            self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
            return scene_c_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002635], quest_states=[2]):
            # 포탈 생성 되어있음
            self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(trigger_ids=[6001])
            self.set_mesh(trigger_ids=[6010])
            self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
            return scene_c_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002635], quest_states=[1]):
            # 포탈 생성 되어있음
            self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(trigger_ids=[6001])
            self.set_mesh(trigger_ids=[6010])
            self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
            return scene_c_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002634], quest_states=[3]):
            # 완료 가능상태
            self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(trigger_ids=[6001])
            self.set_mesh(trigger_ids=[6010])
            self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
            return scene_b_07(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002634], quest_states=[2]):
            # 완료 가능상태
            self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(trigger_ids=[6001])
            self.set_mesh(trigger_ids=[6010])
            self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
            return scene_b_07(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002635], quest_states=[1]):
            # 포탈 생성 되어있음
            self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(trigger_ids=[6001])
            self.set_mesh(trigger_ids=[6010])
            self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
            return scene_c_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002633], quest_states=[1]):
            return ready_02(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002633], quest_states=[2]):
            # 비욘드로이드 3명 처치 후 완료 가능 상태
            self.spawn_monster(spawn_ids=[101])
            return scene_b_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002633], quest_states=[3]):
            # 비욘드로이드 3명 처치 후 완료 상태
            self.spawn_monster(spawn_ids=[101])
            return scene_b_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002634], quest_states=[1]):
            # 자베스 뛰어감
            self.spawn_monster(spawn_ids=[101])
            self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2001')
            self.spawn_monster(spawn_ids=[122])
            return scene_b_02(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002635], quest_states=[2]):
            # 포탈 생성 되어있음
            self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(trigger_ids=[6001])
            self.set_mesh(trigger_ids=[6010])
            self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
            return scene_c_01(self.ctx)
        if self.user_detected(box_ids=[701], job_code=110):
            # 소울 바인더가 입장시에는 포탈 생성 되어있음
            self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(trigger_ids=[6001])
            self.set_mesh(trigger_ids=[6010])
            self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
            return scene_c_01(self.ctx)


class ready_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201,202,203], auto_target=False)
        self.spawn_monster(spawn_ids=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002633], quest_states=[1]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=7001)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000039_QD__MAIN__0$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            self.select_camera(trigger_id=7001, enable=False)
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20020030, text_id=20020030)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203]):
            self.destroy_monster(spawn_ids=[102])
            self.hide_guide_summary(entity_id=20020030)
            return scene_b_01(self.ctx)


class scene_b_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='beyondroid2')
        self.spawn_monster(spawn_ids=[112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002634], quest_states=[1]):
            self.destroy_monster(spawn_ids=[112])
            self.spawn_monster(spawn_ids=[122])
            return scene_b_02(self.ctx)


class scene_b_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_2004')
        self.set_dialogue(type=1, spawn_id=122, script='$52000039_QD__MAIN__1$', time=3)
        self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
        self.set_mesh(trigger_ids=[6001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=703, spawn_ids=[122]):
            self.set_cinematic_ui(type=1)
            self.set_cinematic_ui(type=3)
            self.select_camera(trigger_id=7002)
            self.move_user(map_id=52000039, portal_id=3)
            self.set_mesh(trigger_ids=[6010])
            return scene_b_03(self.ctx)


class scene_b_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_2006')
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000039_QD__MAIN__2$', time=3)
        self.set_actor(trigger_id=3010, visible=True, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_b_04(self.ctx)


class scene_b_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=7003)
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_2008')
        self.set_dialogue(type=1, spawn_id=122, script='$52000039_QD__MAIN__3$', time=3)
        self.set_actor(trigger_id=3010, visible=True, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_b_05(self.ctx)


class scene_b_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3010, visible=True, initial_sequence='Attack_01_D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=650):
            return scene_b_06(self.ctx)


class scene_b_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=4)
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_2010')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
            self.spawn_monster(spawn_ids=[210])
            return scene_b_07(self.ctx)


class scene_b_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20020031, text_id=20020031)
        self.select_camera(trigger_id=7003, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[210]):
            self.hide_guide_summary(entity_id=20020031)
            self.set_achievement(trigger_id=701, type='trigger', achieve='beyondguard')
            self.destroy_monster(spawn_ids=[101,122])
            return scene_b_08(self.ctx)


class scene_b_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111,132])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return scene_b_09(self.ctx)


class scene_b_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=132, script='$52000039_QD__MAIN__4$', time=3)
        self.set_npc_emotion_loop(spawn_id=132, sequence_name='Sit_Down_A', duration=3000.0)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Sit_Down_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_b_10(self.ctx)


class scene_b_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=132, script='$52000039_QD__MAIN__5$', time=3)
        self.set_npc_emotion_loop(spawn_id=132, sequence_name='Stun_A', duration=3000.0)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Stun_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002635], quest_states=[1]):
            return scene_c_01(self.ctx)


class scene_c_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=132, script='$52000039_QD__MAIN__6$', time=3)
        self.move_npc(spawn_id=132, patrol_name='MS2PatrolData_2012')
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_2011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_c_02(self.ctx)


class scene_c_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.destroy_monster(spawn_ids=[132,111])


# 비욘드 링크 중앙 컴퓨터실 포탈 열림
class NextMapPortalOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3001, visible=True, initial_sequence='sf_fi_funct_door_A01_Opened')
        self.set_mesh(trigger_ids=[6001])
        self.set_mesh(trigger_ids=[6010])
        self.set_actor(trigger_id=3010, initial_sequence='Idle_A')
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


# 흑성회 본부 지하 밀실 이동
class PCPatrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCPatrol02(self.ctx)


class PCPatrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCPatrol03(self.ctx)


class PCPatrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LookAround01(self.ctx)


class LookAround01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Bore_C'])
        self.set_dialogue(type=1, script='$52000039_QD__MAIN__7$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return LookAround02(self.ctx)


class LookAround02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)
        self.set_dialogue(type=1, script='$52000039_QD__MAIN__8$', time=2)
        self.move_user_path(patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return LookAround03(self.ctx)


class LookAround03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1002')
        self.set_dialogue(type=1, script='$52000039_QD__MAIN__9$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1600):
            return PCFainted01(self.ctx)


class PCFainted01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)
        self.set_pc_emotion_sequence(sequence_names=['Down2_A','Down_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2667):
            return PCTeleport01(self.ctx)


class PCTeleport01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=10000.0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCTeleport02(self.ctx)


class PCTeleport02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000045, portal_id=2, box_id=701)
        self.select_camera(trigger_id=502, enable=False)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = ready
