""" trigger/52010027_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 바람의 골짜기 : 52010027
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003073], quest_states=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301]) # 습격지역 꼭대기 집
        self.spawn_monster(spawn_ids=[302]) # 습격지역 꼭대기 입구
        self.spawn_monster(spawn_ids=[303]) # 습격지역 꼭대기 주민
        self.spawn_monster(spawn_ids=[304]) # 진입부 주민 1층
        self.spawn_monster(spawn_ids=[305]) # 진입부 주민 2층
        self.spawn_monster(spawn_ids=[401]) # 악당NPC_1
        self.spawn_monster(spawn_ids=[402]) # 악당NPC_2
        self.spawn_monster(spawn_ids=[403]) # 악당NPC_3
        self.spawn_monster(spawn_ids=[404]) # 악당NPC_4
        self.spawn_monster(spawn_ids=[405]) # 악당NPC_5
        self.spawn_monster(spawn_ids=[406]) # 악당NPC_6
        self.spawn_monster(spawn_ids=[407]) # 악당NPC_7
        self.spawn_monster(spawn_ids=[408]) # 악당NPC_8
        self.spawn_monster(spawn_ids=[409]) # 악당NPC_9
        self.spawn_monster(spawn_ids=[501]) # 보스NPC_1
        self.spawn_monster(spawn_ids=[502]) # 보스NPC_1
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라_전환(self.ctx)


class 카메라_전환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52010027_QD__MAIN__0$', desc='$52010027_QD__MAIN__1$', align=Align.Center | Align.Left, duration=3000, scale=2.0)
        self.set_npc_emotion_loop(spawn_id=303, sequence_name='Down_Idle_A', duration=150000.0)
        self.face_emotion(spawn_id=302, emotion_name='down_Idle')
        self.face_emotion(spawn_id=303, emotion_name='down_Idle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 연출_습격현장(self.ctx)


class 연출_습격현장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.add_balloon_talk(spawn_id=301, msg='$52010027_QD__MAIN__2$', duration=3000)
        self.add_balloon_talk(spawn_id=403, msg='$52010027_QD__MAIN__3$', duration=3000)
        self.add_balloon_talk(spawn_id=303, msg='$52010027_QD__MAIN__4$', duration=2000, delay_tick=1000)
        self.set_npc_emotion_sequence(spawn_id=402, sequence_name='Attack_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4200):
            return 연출_습격현장_02(self.ctx)


class 연출_습격현장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출_습격현장_02_01(self.ctx)


class 연출_습격현장_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=401, msg='$52010027_QD__MAIN__5$', duration=2000)
        self.set_npc_emotion_sequence(spawn_id=401, sequence_name='Attack_02_A')
        self.add_balloon_talk(spawn_id=304, msg='$52010027_QD__MAIN__6$', duration=2000, delay_tick=500)
        self.add_balloon_talk(spawn_id=305, msg='$52010027_QD__MAIN__7$', duration=3000, delay_tick=1500)
        self.set_npc_emotion_loop(spawn_id=305, sequence_name='Down_Idle_A', duration=150000.0)
        self.face_emotion(spawn_id=304, emotion_name='down_Idle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 연출_습격현장확인_PC(self.ctx)


class 연출_습격현장확인_PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN__8$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN__9$', duration=3000)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=10000.0)
        self.add_balloon_talk(msg='$52010027_QD__MAIN__10$', duration=2000, delay_tick=6000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__11$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 연출_습격현장_보스등장(self.ctx)


class 연출_습격현장_보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.move_npc(spawn_id=502, patrol_name='MS2PatrolData_3004')
        self.show_caption(type='VerticalCaption', title='$52010027_QD__MAIN__12$', desc='$52010027_QD__MAIN__13$', align=Align.Center | Align.Left, duration=3000, scale=2.0)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__14$', duration=3500)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__15$', duration=3500)
        self.add_balloon_talk(spawn_id=405, msg='$52010027_QD__MAIN__16$', duration=2000, delay_tick=2000)
        self.add_balloon_talk(spawn_id=406, msg='$52010027_QD__MAIN__17$', duration=2000, delay_tick=1800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출_습격현장_보스이동(self.ctx)


class 연출_습격현장_보스이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=501, sequence_name='Attack_01_G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출_습격현장_보스소환연출(self.ctx)


class 연출_습격현장_보스소환연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[502]) # 보스NPC_1
        self.set_effect(trigger_ids=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출_습격현장_보스소환연출_02(self.ctx)


class 연출_습격현장_보스소환연출_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 연출_습격현장_보스소환연출_03(self.ctx)


class 연출_습격현장_보스소환연출_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__18$', duration=3000)
        self.set_npc_emotion_sequence(spawn_id=501, sequence_name='Attack_01_D')
        self.move_user(map_id=52010027, portal_id=6001)
        self.destroy_monster(spawn_ids=[401])
        self.destroy_monster(spawn_ids=[402])
        self.destroy_monster(spawn_ids=[403])
        self.destroy_monster(spawn_ids=[404])
        self.destroy_monster(spawn_ids=[405])
        self.destroy_monster(spawn_ids=[406])
        self.destroy_monster(spawn_ids=[407])
        self.destroy_monster(spawn_ids=[408])
        self.destroy_monster(spawn_ids=[409])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3800):
            return 연출_습격현장_PC연출(self.ctx)


class 연출_습격현장_PC연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=3500.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN__19$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출_습격현장_PC연출_1(self.ctx)


class 연출_습격현장_PC연출_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출_습격현장_전투준비(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52010027, portal_id=6001)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.destroy_monster(spawn_ids=[502]) # 보스NPC_1
        self.destroy_monster(spawn_ids=[401])
        self.destroy_monster(spawn_ids=[402])
        self.destroy_monster(spawn_ids=[403])
        self.destroy_monster(spawn_ids=[404])
        self.destroy_monster(spawn_ids=[405])
        self.destroy_monster(spawn_ids=[406])
        self.destroy_monster(spawn_ids=[407])
        self.destroy_monster(spawn_ids=[408])
        self.destroy_monster(spawn_ids=[409])
        self.select_camera_path(path_ids=[4008], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출_습격현장_전투준비(self.ctx)


class 연출_습격현장_전투준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[601]) # 악당Mob_1
        self.spawn_monster(spawn_ids=[602]) # 악당Mob_2
        self.spawn_monster(spawn_ids=[603]) # 악당Mob_3
        self.spawn_monster(spawn_ids=[604]) # 악당Mob_4
        self.spawn_monster(spawn_ids=[605]) # 악당Mob_5
        self.spawn_monster(spawn_ids=[606]) # 악당Mob_6
        self.add_balloon_talk(spawn_id=602, msg='$52010027_QD__MAIN__20$', duration=2000)
        self.add_balloon_talk(spawn_id=606, msg='$52010027_QD__MAIN__21$', duration=2000, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출_습격현장_전투준비_02(self.ctx)


class 연출_습격현장_전투준비_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차_전투1(self.ctx)


class 차_전투1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$52010027_QD__MAIN__22$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,602,603,604,605,606]):
            return 연출_잠시쉬기(self.ctx)


class 연출_잠시쉬기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차_전투_보스몬스터대사1(self.ctx)


class 차_전투_보스몬스터대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__23$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차_전투_보스소환연출2(self.ctx)


class 차_전투_보스소환연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__24$', duration=3000)
        self.set_npc_emotion_sequence(spawn_id=501, sequence_name='Attack_01_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차_전투_보스소환연출_1_2(self.ctx)


class 차_전투_보스소환연출_1_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차_전투2(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차_전투2(self.ctx)


class 차_전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=1, arg2='$52010027_QD__MAIN__25$', arg3='3000', arg4='0')
        self.spawn_monster(spawn_ids=[701]) # 악당Mob_1
        self.spawn_monster(spawn_ids=[702]) # 악당Mob_2
        self.spawn_monster(spawn_ids=[703]) # 악당Mob_3
        self.spawn_monster(spawn_ids=[704]) # 악당Mob_4
        self.spawn_monster(spawn_ids=[705]) # 악당Mob_5
        self.spawn_monster(spawn_ids=[706]) # 악당Mob_6
        self.add_balloon_talk(spawn_id=701, msg='$52010027_QD__MAIN__26$', duration=2000)
        self.add_balloon_talk(spawn_id=703, msg='$52010027_QD__MAIN__27$', duration=2000, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[701,702,703,704,705,706]):
            return 연출_잠시쉬기_01(self.ctx)


class 연출_잠시쉬기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출_페리온영웅등장(self.ctx)


class 연출_페리온영웅등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2001, type='trigger', achieve='Windvalley')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_loop(spawn_id=501, sequence_name='Attack_Idle_A', duration=16000.0)
        self.set_scene_skip(state=페리온으로, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출_페리온영웅등장_보스대사(self.ctx)


class 연출_페리온영웅등장_보스대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__28$', duration=3000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__29$', duration=3000)
        self.destroy_monster(spawn_ids=[601])
        self.destroy_monster(spawn_ids=[602])
        self.destroy_monster(spawn_ids=[603])
        self.destroy_monster(spawn_ids=[604])
        self.destroy_monster(spawn_ids=[605])
        self.destroy_monster(spawn_ids=[606])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 연출_페리온영웅등장_보스대사_02(self.ctx)


class 연출_페리온영웅등장_보스대사_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004,4015], return_view=False)
        self.add_balloon_talk(spawn_id=501, msg='$52010027_QD__MAIN__30$', duration=2000)
        self.add_cinematic_talk(npc_id=11003388, msg='$52010027_QD__MAIN__31$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010027_QD__MAIN__32$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 연출_페리온영웅등장_보스대사_03(self.ctx)


class 연출_페리온영웅등장_보스대사_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.add_balloon_talk(spawn_id=501, msg='$52010027_QD__MAIN__33$', duration=2000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__34$', duration=3000)
        self.spawn_monster(spawn_ids=[201]) # 에바고르: 11003391
        self.spawn_monster(spawn_ids=[101]) # 시끄러운 주먹: 11003388

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 연출_페리온영웅등장_02(self.ctx)


class 연출_페리온영웅등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.select_camera_path(path_ids=[4015,4006], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.show_caption(type='VerticalCaption', title='$52010027_QD__MAIN__35$', desc='$52010027_QD__MAIN__36$', align=Align.Center | Align.Left, duration=3000, scale=2.0)
        self.add_cinematic_talk(npc_id=11003388, msg='$52010027_QD__MAIN__37$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출_페리온영웅등장_03(self.ctx)


class 연출_페리온영웅등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003388, msg='$52010027_QD__MAIN__38$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010027_QD__MAIN__39$', duration=3000)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3002')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 연출_페리온영웅등장_04(self.ctx)


class 연출_페리온영웅등장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__40$', duration=3000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010027_QD__MAIN__41$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출_페리온영웅등장_05(self.ctx)


class 연출_페리온영웅등장_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        self.destroy_monster(spawn_ids=[501])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출_페리온영웅과대화(self.ctx)


class 연출_페리온영웅과대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Bore_B', duration=3000.0)
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Attack_Idle_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=11003388, msg='$52010027_QD__MAIN__42$', duration=3500)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010027_QD__MAIN__43$', duration=2000)
        self.add_cinematic_talk(npc_id=11003388, msg='$52010027_QD__MAIN__44$', duration=3500)
        self.move_user(map_id=52010027, portal_id=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 연출_페리온영웅과대화_02(self.ctx)


class 연출_페리온영웅과대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=201, emotion_name='Trigger_NotAgree')
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=29000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN__45$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출_페리온영웅과대화_03(self.ctx)


class 연출_페리온영웅과대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.face_emotion(spawn_id=201, emotion_name='Trigger_NotAgree')
        self.add_cinematic_talk(npc_id=11003391, msg='$52010027_QD__MAIN__46$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3000.0)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003388, msg='$52010027_QD__MAIN__47$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 연출_페리온영웅과대화_04(self.ctx)


class 연출_페리온영웅과대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=29000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN__48$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010027_QD__MAIN__49$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출_페리온영웅과대화_05(self.ctx)


class 연출_페리온영웅과대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=15000.0)
        self.face_emotion(spawn_id=201, emotion_name='Trigger_Sad')
        self.add_cinematic_talk(npc_id=11003388, msg='$52010027_QD__MAIN__50$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010027_QD__MAIN__51$', duration=3000)
        self.add_cinematic_talk(npc_id=11003388, msg='$52010027_QD__MAIN__52$', duration=2000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010027_QD__MAIN__53$', duration=2000)
        self.add_cinematic_talk(npc_id=11003388, msg='$52010027_QD__MAIN__54$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return 연출_페리온영웅과대화_05_1(self.ctx)


class 연출_페리온영웅과대화_05_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 페리온으로(self.ctx)


class 페리온으로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_portal(portal_id=6003, visible=True, enable=True, minimap_visible=True)
        self.move_user(map_id=52010027, portal_id=6004)
        self.destroy_monster(spawn_ids=[201]) # 에바고르: 11003391
        self.destroy_monster(spawn_ids=[101]) # 시끄러운 주먹: 11003388

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 페리온으로02(self.ctx)


class 페리온으로02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 페리온으로03(self.ctx)


class 페리온으로03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$52010027_QD__MAIN__55$', arg3='3000', arg4='0')


initial_state = idle
