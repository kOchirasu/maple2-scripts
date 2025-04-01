""" trigger/52000068_qd/tria_seige.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 퀘스트분기(self.ctx)


class 퀘스트분기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11010, initial_sequence='Dead_A')
        self.set_actor(trigger_id=16000, initial_sequence='Stun_A')
        self.set_actor(trigger_id=16001, initial_sequence='Stun_A')
        self.set_actor(trigger_id=16002, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16003, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16004, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16005, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16006, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16007, initial_sequence='Stun_A')
        self.set_actor(trigger_id=16008, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16009, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16010, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16011, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16012, initial_sequence='Stun_A')
        self.set_interact_object(trigger_ids=[10001074], state=2)
        self.set_interact_object(trigger_ids=[10001075], state=2)
        self.set_interact_object(trigger_ids=[10001076], state=2)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_portal(portal_id=2)
        self.set_breakable(trigger_ids=[5000,5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[20002264], quest_states=[3]):
            # 챕터6 에필로그 [20002264 진정한 트라이아의 방패] 완료 시
            return 재접속유저케어(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[20002263], quest_states=[3]):
            return 조디사망연출(self.ctx)
        if not self.quest_user_detected(box_ids=[199], quest_ids=[20002263], quest_states=[3]):
            return 침공이벤트시작(self.ctx)


class 재접속유저케어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10000,10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023], auto_target=False)
        self.spawn_monster(spawn_ids=[10024,10025,10026,10027,10028,10029,10030,10031,10032,10033,10034], auto_target=False)
        self.set_visible_breakable_object(trigger_ids=[5000,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012])
        self.set_sound(trigger_id=90000, enable=True) # TriaAttack

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 트리거멈춤(self.ctx)


class 트리거멈춤(trigger_api.Trigger):
    pass


# 여기서부터 NPC조디 사망연출
class 조디사망연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 모든 agent 개방
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])
        self.set_agent(trigger_ids=[8013])
        self.set_agent(trigger_ids=[8014])
        self.set_agent(trigger_ids=[8015])
        self.set_agent(trigger_ids=[8016])
        self.set_agent(trigger_ids=[8017])
        self.set_agent(trigger_ids=[8018])
        self.set_agent(trigger_ids=[8019])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 연출트리거로고고(self.ctx)


class 연출트리거로고고(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99999201, key='tria_seige', value=1)


# 여기서부터 군단 침공 이벤트
class 침공이벤트시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001])
        self.set_skill(trigger_ids=[701])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])
        self.set_agent(trigger_ids=[8013])
        self.set_agent(trigger_ids=[8014])
        self.set_agent(trigger_ids=[8015])
        self.set_agent(trigger_ids=[8016])
        self.set_agent(trigger_ids=[8017])
        self.set_agent(trigger_ids=[8018])
        self.set_agent(trigger_ids=[8019])
        self.spawn_monster(spawn_ids=[1001,2001,2002], auto_target=False)
        self.spawn_monster(spawn_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026], auto_target=False)
        self.spawn_monster(spawn_ids=[4100,4101,4102,4103,4104,4105,4106,4107,4108,4109,4110,4111,4112,4113,4114,4115,4116,4117,4118,4119,4120,4121,4122,4123,4124], auto_target=False)
        self.set_breakable(trigger_ids=[5000,5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라이동2(self.ctx)


class 카메라이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 데블린동작(self.ctx)


class 데블린동작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=11100101, enable=True, path='BG/Common/Sound/Eff_Object_Devlin_Appear_01.xml ')
        self.set_npc_emotion_sequence(spawn_id=2001, sequence_name='AttackReady_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 마드리아카메라(self.ctx)


class 마드리아카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=311)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마드리아백샷(self.ctx)


class 마드리아백샷(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2002, script='$52000068_QD__TRIA_SEIGE__0$', time=3)
        self.set_onetime_effect(id=1990, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_01_00001990.xml')
        self.select_camera(trigger_id=303)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 레논대사01(self.ctx)


class 레논대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000068_QD__TRIA_SEIGE__1$', time=4)
        self.select_camera(trigger_id=304)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 레논대사02(self.ctx)


class 레논대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000068_QD__TRIA_SEIGE__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 레논대사03(self.ctx)


class 레논대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000068_QD__TRIA_SEIGE__3$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 레논대사03_1(self.ctx)


class 레논대사03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolation_time=0.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[199], skill_id=70000109, level=1, ignore_player=False, is_skill_set=False) # 초생회
        self.select_camera(trigger_id=304, enable=False)
        # self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_dialogue(type=1, spawn_id=1001, script='$52000068_QD__TRIA_SEIGE__4$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return 임무01(self.ctx)
        if self.user_detected(box_ids=[101]):
            return 임무01(self.ctx)


class 임무01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_interact_object(trigger_ids=[10001074], state=1)
        self.set_interact_object(trigger_ids=[10001075], state=1)
        self.set_interact_object(trigger_ids=[10001076], state=1)
        self.add_buff(box_ids=[199], skill_id=70000107, level=1, ignore_player=False, is_skill_set=False)
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000068_QD__TRIA_SEIGE__5$', time=4)
        self.set_scene_skip(state=임무01반응대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 임무01반응대기(self.ctx)


class 임무01반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_buff(box_id=199, skill_id=70000107)
        self.select_camera(trigger_id=305, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001074,10001075,10001076], state=2):
            self.set_dialogue(type=1, spawn_id=1001, script='$52000068_QD__TRIA_SEIGE__6$', time=4)
            self.create_item(spawn_ids=[9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012])
            self.add_buff(box_ids=[199], skill_id=70000058, level=1, ignore_player=False, is_skill_set=False) # 이속증가
            return 임무02대기(self.ctx)


class 임무02대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 임무02(self.ctx)


class 임무02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)
        self.set_agent(trigger_ids=[8009], visible=True)
        self.set_agent(trigger_ids=[8010], visible=True)
        self.set_agent(trigger_ids=[8011], visible=True)
        self.set_agent(trigger_ids=[8012], visible=True)
        self.set_agent(trigger_ids=[8013], visible=True)
        self.set_agent(trigger_ids=[8014], visible=True)
        self.set_agent(trigger_ids=[8015], visible=True)
        self.set_agent(trigger_ids=[8016], visible=True)
        self.set_agent(trigger_ids=[8017], visible=True)
        self.set_agent(trigger_ids=[8018], visible=True)
        self.set_agent(trigger_ids=[8019], visible=True)
        self.add_buff(box_ids=[199], skill_id=70000107, level=1, ignore_player=False, is_skill_set=False)
        self.select_camera(trigger_id=306)
        self.set_dialogue(type=2, spawn_id=11001838, script='$52000068_QD__TRIA_SEIGE__7$', time=4)
        self.spawn_monster(spawn_ids=[1101,1102,1103,1104], auto_target=False, delay=6000)
        self.move_npc(spawn_id=1101, patrol_name='MS2PatrolData_1101')
        self.move_npc(spawn_id=1102, patrol_name='MS2PatrolData_1102')
        self.move_npc(spawn_id=1103, patrol_name='MS2PatrolData_1103')
        self.move_npc(spawn_id=1104, patrol_name='MS2PatrolData_1104')
        self.set_scene_skip(state=대사스킵용01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 임무02_2(self.ctx)


class 대사스킵용01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 임무02_2(self.ctx)


class 임무02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])
        self.set_agent(trigger_ids=[8013])
        self.set_agent(trigger_ids=[8014])
        self.set_agent(trigger_ids=[8015])
        self.set_agent(trigger_ids=[8016])
        self.set_agent(trigger_ids=[8017])
        self.set_agent(trigger_ids=[8018])
        self.set_agent(trigger_ids=[8019])
        self.set_effect(trigger_ids=[602], visible=True)
        self.select_camera(trigger_id=307)
        self.spawn_monster(spawn_ids=[2003], auto_target=False)
        self.set_dialogue(type=2, spawn_id=11001838, script='$52000068_QD__TRIA_SEIGE__8$', time=4)
        self.set_npc_emotion_sequence(spawn_id=2003, sequence_name='AttackReady_A')
        self.set_scene_skip(state=임무02종료대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 임무02종료대기(self.ctx)


class 임무02종료대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_buff(box_id=199, skill_id=70000107)
        self.select_camera(trigger_id=307, enable=False)
        self.set_effect(trigger_ids=[602])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 임무02종료(self.ctx)
        if self.monster_dead(spawn_ids=[2003]):
            return 임무02종료(self.ctx)


class 임무02종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=309)
        self.add_buff(box_ids=[199], skill_id=70000107, level=1, ignore_player=False, is_skill_set=False)
        self.destroy_monster(spawn_ids=[2001])
        self.spawn_monster(spawn_ids=[2004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SetSkillA') == 1:
            return 데블린카메라이동(self.ctx)


class 데블린카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=310)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SetSkillB') == 1:
            return 벽파괴대기(self.ctx)


class 벽파괴대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 벽파괴(self.ctx)


class 벽파괴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2101,2102,2103,2104], auto_target=False, delay=6000)
        self.move_npc(spawn_id=2101, patrol_name='MS2PatrolData_air')
        self.move_npc(spawn_id=2102, patrol_name='MS2PatrolData_air')
        self.move_npc(spawn_id=2103, patrol_name='MS2PatrolData_air')
        self.move_npc(spawn_id=2104, patrol_name='MS2PatrolData_air')
        self.select_camera(trigger_id=308)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_skill(trigger_ids=[701], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 조디대화(self.ctx)


class 조디대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_dialogue(type=2, spawn_id=11001838, script='$52000068_QD__TRIA_SEIGE__9$', time=4)
        self.set_scene_skip(state=대사스킵용02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 조디대화2(self.ctx)


class 대사스킵용02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 조디대화2(self.ctx)


class 조디대화2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_dialogue(type=2, spawn_id=11001838, script='$52000068_QD__TRIA_SEIGE__10$', time=4)
        self.set_scene_skip(state=벽파괴종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 벽파괴종료(self.ctx)


class 벽파괴종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()
        self.set_portal(portal_id=2, enable=True, minimap_visible=True)
        self.destroy_monster(spawn_ids=[2101,2102,2103,2104])
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[603])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_buff(box_id=199, skill_id=70000107)
        self.select_camera(trigger_id=308, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Wait
