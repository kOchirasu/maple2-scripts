""" trigger/52000101_qd/52000101.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_portal(portal_id=1000)
        self.set_effect(trigger_ids=[5304]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5305]) # 화살표 안내 사운드 이펙트
        self.set_effect(trigger_ids=[5306]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5307]) # 목표 바닥 지점01 NPC
        self.set_effect(trigger_ids=[5308]) # 목표 바닥 지점03 포탈
        self.set_effect(trigger_ids=[5309]) # 화살표01 NPC
        self.set_effect(trigger_ids=[5310]) # 경로 안내
        self.set_effect(trigger_ids=[5311]) # 경로 안내
        self.set_effect(trigger_ids=[5312]) # 경로 안내
        self.set_effect(trigger_ids=[5313]) # 경로 안내
        self.set_effect(trigger_ids=[5314]) # 경로 안내
        self.set_effect(trigger_ids=[5315]) # 경로 안내
        self.set_effect(trigger_ids=[5316]) # 경로 안내
        self.set_effect(trigger_ids=[5317]) # 경로 안내
        self.set_effect(trigger_ids=[5318]) # 경로 안내
        self.set_effect(trigger_ids=[5319]) # 경로 안내
        self.set_effect(trigger_ids=[5320]) # 경로 안내
        self.set_effect(trigger_ids=[5321]) # 경로 안내
        self.set_effect(trigger_ids=[5322]) # 경로 안내
        self.move_user(map_id=52000101, portal_id=1010)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[4000]):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='common\\JobIntro_Wizard.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 엘리니아전경씬01(self.ctx)
        if self.wait_tick(wait_tick=62000):
            return 엘리니아전경씬01(self.ctx)


class 엘리니아전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1100,1101], return_view=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 엘리니아전경씬02(self.ctx)


class 엘리니아전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000101_QD__52000101__0$', desc='$52000101_QD__52000101__1$', align=Align.Bottom | Align.Left, duration=10000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 엘리니아전경씬03(self.ctx)


class 엘리니아전경씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.set_effect(trigger_ids=[5304], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5305], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5306], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5307], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5308], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5309], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5310], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5311], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5312], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5313], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5314], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5315], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5316], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5317], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5318], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5319], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5320], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5321], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5322], visible=True) # 경로 안내
        self.add_balloon_talk(msg='$52000101_QD__52000101__2$', duration=6000, delay_tick=1000)
        self.show_guide_summary(entity_id=25201011, text_id=25201011, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[4001]):
            return 케이틀린등장씬01(self.ctx)


# ########################씬2 케이틀린 등장########################
class 케이틀린등장씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 케이틀린

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 케이틀린등장씬02(self.ctx)


class 케이틀린등장씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_caitCome')
        self.select_camera_path(path_ids=[1002,1003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 케이틀린등장씬03(self.ctx)


class 케이틀린등장씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1004,1005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 케이틀린등장씬04_b(self.ctx)


class 케이틀린등장씬04_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=200, sequence_name='Bore_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 케이틀린등장씬04(self.ctx)


class 케이틀린등장씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='NameCaption', title='$52000101_QD__52000101__3$', desc='$52000101_QD__52000101__4$', align=Align.Center, offset_rate_x=-0.15, offset_rate_y=0.15, duration=10000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 케이틀린등장씬04_1(self.ctx)


class 케이틀린등장씬04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 케이틀린등장씬05(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_caitCome')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 케이틀린등장씬05(self.ctx)


class 케이틀린등장씬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.set_effect(trigger_ids=[5304]) # 경로 안내
        self.set_effect(trigger_ids=[5305]) # 경로 안내
        self.set_effect(trigger_ids=[5306]) # 경로 안내
        self.set_effect(trigger_ids=[5307]) # 경로 안내
        self.set_effect(trigger_ids=[5308]) # 경로 안내
        self.set_effect(trigger_ids=[5309]) # 경로 안내
        self.set_effect(trigger_ids=[5310]) # 경로 안내
        self.set_effect(trigger_ids=[5311]) # 경로 안내
        self.set_effect(trigger_ids=[5312]) # 경로 안내
        self.set_effect(trigger_ids=[5313]) # 경로 안내
        self.set_effect(trigger_ids=[5314]) # 경로 안내
        self.set_effect(trigger_ids=[5315]) # 경로 안내
        self.set_effect(trigger_ids=[5316]) # 경로 안내
        self.set_effect(trigger_ids=[5317]) # 경로 안내
        self.set_effect(trigger_ids=[5318]) # 경로 안내
        self.set_effect(trigger_ids=[5319]) # 경로 안내
        self.set_effect(trigger_ids=[5320]) # 경로 안내
        self.set_effect(trigger_ids=[5321]) # 경로 안내
        self.set_effect(trigger_ids=[5322]) # 경로 안내
        self.face_emotion(spawn_id=200)
        self.show_guide_summary(entity_id=25201012, text_id=25201012, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[4001], quest_ids=[20002286], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 케이틀린화남01(self.ctx)
        if self.quest_user_detected(box_ids=[4001], quest_ids=[20002286], quest_states=[2]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 케이틀린화남01(self.ctx)


# ########################씬3 케이틀린과 대화퀘스트 이후########################
class 케이틀린화남01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=케이틀린화남06, action='exit')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000101, portal_id=1011)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 케이틀린화남02(self.ctx)


class 케이틀린화남02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npc_id=0, msg='$52000101_QD__52000101__5$', duration=4000, align=Align.Right)
        self.select_camera_path(path_ids=[1006,1007], return_view=False)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_caitTurn') # 마드리아 이동
        self.move_user_path(patrol_name='MS2PatrolData_PC_Run')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 케이틀린화남03(self.ctx)


class 케이틀린화남03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003146, msg='$52000101_QD__52000101__6$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000946, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000946.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 케이틀린화남04(self.ctx)


class 케이틀린화남04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=200, emotion_name='UpSet')
        self.select_camera_path(path_ids=[1008,1009], return_view=False)
        self.add_cinematic_talk(npc_id=11003146, msg='$52000101_QD__52000101__7$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000947, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000947.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 케이틀린화남05(self.ctx)


class 케이틀린화남05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1200], return_view=False)
        self.add_cinematic_talk(npc_id=11003146, msg='$52000101_QD__52000101__8$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000948, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000948.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 케이틀린화남05_1(self.ctx)


class 케이틀린화남05_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 케이틀린화남06(self.ctx)


class 케이틀린화남06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=52000100, portal_id=1)


initial_state = Wait
