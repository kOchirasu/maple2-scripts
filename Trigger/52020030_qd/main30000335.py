""" trigger/52020030_qd/main30000335.xml """
import trigger_api


# 투르카와 전투
class 입장1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5007])
        self.set_effect(trigger_ids=[5006])
        self.set_onetime_effect(id=300, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=301, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2003], quest_ids=[30000335], quest_states=[1]):
            return 투르카이오네연출시작(self.ctx)


class 투르카이오네연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.destroy_monster(spawn_ids=[111]) # 퀘스트용 크란츠 삭제
        self.select_camera_path(path_ids=[4011], return_view=False)
        self.move_user(map_id=52020030, portal_id=6004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카이오네연출시작_02(self.ctx)


class 투르카이오네연출시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 투르카의등장(self.ctx)


class 투르카의등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4031], return_view=False)
        self.add_cinematic_talk(npc_id=11003762, msg='천공의 심장을 손에 넣었군.', duration=3000)
        self.set_scene_skip(action='exit') # Missing State: 공명준비

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카의등장_01(self.ctx)


class 투르카의등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11003762, msg='이리 가져와라. 크란츠.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카의등장02(self.ctx)


class 투르카의등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4019], return_view=False)
        self.add_cinematic_talk(npc_id=11003761, msg='어디서 감히 명령이지?', duration=3000)
        self.add_cinematic_talk(npc_id=11003761, msg='나에게 명령을 내릴 수 있는 자는 오직 이오네 왕녀님 뿐이다.', duration=3000)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Quest_Frustration_A', duration=9500.0)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=12000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 투르카의등장03(self.ctx)


class 투르카의등장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4018], return_view=False)
        self.add_cinematic_talk(npc_id=11003760, msg='크란츠... 지금은 이 자의 말을 듣도록 해.', duration=3000)
        self.add_cinematic_talk(npc_id=11003760, msg='천공의 심장을 이리로.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 투르카의등장04(self.ctx)


class 투르카의등장04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4019], return_view=False)
        self.add_cinematic_talk(npc_id=11003761, msg='... 넵. 왕녀님', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 반대하는플레이어(self.ctx)


class 반대하는플레이어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4025], return_view=False)
        self.face_emotion(emotion_name='defaultBattle')
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=0, msg='천공의 심장을 넘기면 안돼!\\n투르카가 티마이온을!!!', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 반대하는플레이어02(self.ctx)


class 반대하는플레이어02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4019,4035], return_view=False)
        self.add_cinematic_talk(npc_id=11003761, msg='어쩔 수 없어.\\n모든 것은 왕녀님을 위해...', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 반대하는플레이어03(self.ctx)


class 반대하는플레이어03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4036], return_view=False)
        self.move_npc(spawn_id=109, patrol_name='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 반대하는플레이어04(self.ctx)


class 반대하는플레이어04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4025], return_view=False)
        self.face_emotion(emotion_name='defaultBattle')
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=0, msg='안돼!!!', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크란츠이동(self.ctx)


class 크란츠이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[105], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크란츠이동_02(self.ctx)


class 크란츠이동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4037], return_view=False)
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_3005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 크란츠이동_03(self.ctx)


class 크란츠이동_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=11003760, msg='수고했어요, 크란츠.', duration=3000)
        self.add_cinematic_talk(npc_id=11003761, msg='왕녀님의 말씀이라면...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 공명준비이오네(self.ctx)


class 공명준비이오네(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4031], return_view=False)
        self.add_cinematic_talk(npc_id=11003762, msg='자, 그럼 이오네.\\n파멸의 날개에 천공의 심장을 공명시켜라.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공명준비이오네_02(self.ctx)


class 공명준비이오네_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4018], return_view=False)
        self.add_cinematic_talk(npc_id=11003760, msg='알았어.\\n바로 시작하도록 하지.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공명준비이오네03(self.ctx)


class 공명준비이오네03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Quest_Spell_A')
        self.add_cinematic_talk(npc_id=11003760, msg='파멸의 날개여, 마법의 힘을 받아들여라.', duration=3000)
        self.set_effect(trigger_ids=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공명준비이오네04(self.ctx)


class 공명준비이오네04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4034], return_view=False)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Quest_Resonance_A', duration=1200000000.0)
        self.set_effect(trigger_ids=[5004], visible=True)
        self.set_effect(trigger_ids=[5007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 투르카공격준비(self.ctx)


class 투르카공격준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4031], return_view=False)
        self.add_cinematic_talk(npc_id=11003762, msg='크하하.', duration=3000)
        self.add_cinematic_talk(npc_id=11003762, msg='계획대로 되어가는군.', duration=3000)
        self.add_cinematic_talk(npc_id=11003762, msg='자 그럼... 이제 방해꾼을 처리해 보도록 할까.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 투르카공격준비_1(self.ctx)


class 투르카공격준비_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.destroy_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카공격준비01(self.ctx)


class 투르카공격준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4021], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Attack_02_C')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=300, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npc_id=11003762, msg='너 따위는 내가 직접 나설 것도 없지.\\n이 곳에서 영원히 잠들어라.', duration=3000)
        self.add_cinematic_talk(npc_id=11003762, msg='나와라. 어둠의 그림자들이여...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 투르카공격준비03(self.ctx)


class 투르카공격준비03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=400, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.select_camera_path(path_ids=[4032,4033], return_view=False)
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Bore_A', duration=100000.0)
        self.spawn_monster(spawn_ids=[501])
        self.spawn_monster(spawn_ids=[502])
        self.spawn_monster(spawn_ids=[503])
        self.spawn_monster(spawn_ids=[504])
        self.spawn_monster(spawn_ids=[505])
        self.spawn_monster(spawn_ids=[506])
        self.spawn_monster(spawn_ids=[507])
        self.spawn_monster(spawn_ids=[508])
        self.spawn_monster(spawn_ids=[509])
        self.spawn_monster(spawn_ids=[510])
        self.spawn_monster(spawn_ids=[511])
        self.spawn_monster(spawn_ids=[512])
        self.spawn_monster(spawn_ids=[513])
        self.spawn_monster(spawn_ids=[514])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카공격준비04(self.ctx)


class 투르카공격준비04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카공격준비05(self.ctx)


class 투르카공격준비05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020030, portal_id=6005)
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=300, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='투르카의 부하들을 처치하세요.', arg3='2000', arg4='0')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.destroy_monster(spawn_ids=[104])
        self.reset_camera()
        self.set_effect(trigger_ids=[5003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[501,502,503,504,505,506,507,508,509,510,511,512,513,514]):
            return 공명완료(self.ctx)


class 공명완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[5001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공명완료02(self.ctx)


class 공명완료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011], return_view=False)
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Bore_A', duration=100000.0)
        self.add_cinematic_talk(npc_id=11003760, msg='공명이 완료 되었어.\\n다음 재료를 찾으러 이동 해야해.', duration=3000)
        self.add_cinematic_talk(npc_id=11003762, msg='후후. 빠르군.', duration=3000)
        self.set_effect(trigger_ids=[5004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 공명완료02_01(self.ctx)


class 공명완료02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4039], return_view=False)
        self.add_cinematic_talk(npc_id=11003761, msg='왕녀님, 몸음 괜찮으신 겁니까. \\n혹시 무리라도 하신건...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 공명완료02_02(self.ctx)


class 공명완료02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4018], return_view=False)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=11003760, msg='난 괜찮아 크란츠. ', duration=3000)
        self.add_cinematic_talk(npc_id=11003760, msg='투르카, 어서 다음 재료의 장소로 이동을.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 공명완료02_03(self.ctx)


class 공명완료02_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011], return_view=False)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Bore_A', duration=100000.0)
        self.add_cinematic_talk(npc_id=11003762, msg='자, 그럼 이동해볼까.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 공명완료03(self.ctx)


class 공명완료03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[110])
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_effect(trigger_ids=[5005], visible=True)
        self.move_user(map_id=52020030, portal_id=6005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공명완료03_01(self.ctx)


class 공명완료03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4038], return_view=False)
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.face_emotion(emotion_name='defaultBattle')
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=8000.0)
        self.add_cinematic_talk(npc_id=0, msg='이럴수가...', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='이오네 왕녀가 투르카와 손을 잡다니...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 공명완료04(self.ctx)


class 공명완료04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4017], return_view=False)
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_3002')
        self.add_cinematic_talk(npc_id=11003753, msg='자네... 무사했군....', duration=3000)
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 공명완료05(self.ctx)


class 공명완료05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=0.5)
        self.set_achievement(trigger_id=2003, type='trigger', achieve='SkyTower')
        self.destroy_monster(spawn_ids=[107])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 입장1
