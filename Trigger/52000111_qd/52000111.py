""" trigger/52000111_qd/52000111.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10011]):
            return START(self.ctx)


class START(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8000])
        self.set_effect(trigger_ids=[8001])
        self.set_effect(trigger_ids=[8002])
        self.set_effect(trigger_ids=[8003])
        self.set_effect(trigger_ids=[8004])
        self.set_effect(trigger_ids=[8005])
        self.set_effect(trigger_ids=[8006])
        self.set_effect(trigger_ids=[8007])
        self.set_effect(trigger_ids=[8008])
        self.set_effect(trigger_ids=[8009])
        self.set_effect(trigger_ids=[8010])
        self.set_effect(trigger_ids=[8011])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002315], quest_states=[2]):
            return 어쌔신탈출02(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002313], quest_states=[2]):
            return PC대탈출01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002313], quest_states=[3]):
            return PC대탈출01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002314], quest_states=[2]):
            return PC대탈출01(self.ctx)
        if not self.quest_user_detected(box_ids=[10011], quest_ids=[20002313], quest_states=[2]):
            return Wait(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002312], quest_states=[3]):
            return PC대탈출01(self.ctx)


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.set_effect(trigger_ids=[5300])
        self.set_effect(trigger_ids=[5301])
        self.set_effect(trigger_ids=[5302])
        self.set_effect(trigger_ids=[5303])
        self.set_effect(trigger_ids=[5304])
        self.set_effect(trigger_ids=[5305])
        self.set_effect(trigger_ids=[5306])
        self.set_effect(trigger_ids=[5307])
        self.set_effect(trigger_ids=[5308])
        self.set_effect(trigger_ids=[5309])
        self.set_effect(trigger_ids=[5310])
        self.set_effect(trigger_ids=[5311])
        self.set_effect(trigger_ids=[5312])
        self.set_effect(trigger_ids=[5313])
        self.set_effect(trigger_ids=[5314])
        self.set_effect(trigger_ids=[5315])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10011]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000111, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='common\\JobIntro_Assassin.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 커닝시티전경씬01(self.ctx)
        if self.wait_tick(wait_tick=55000):
            return 커닝시티전경씬01(self.ctx)


class 커닝시티전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.select_camera_path(path_ids=[1000,1001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 커닝시티전경씬01_B(self.ctx)


class 커닝시티전경씬01_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1002,1003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 커닝시티전경씬02(self.ctx)


class 커닝시티전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1004,1005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 커닝시티전경씬03(self.ctx)


class 커닝시티전경씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000111_QD__52000111__0$', desc='$52000111_QD__52000111__1$', align=Align.Bottom | Align.Left, duration=7000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 커닝시티전경씬04(self.ctx)


class 커닝시티전경씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit01_1(self.ctx)


class Quit01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.set_effect(trigger_ids=[5300], visible=True)
        self.set_effect(trigger_ids=[5301], visible=True)
        self.set_effect(trigger_ids=[5302], visible=True)
        self.set_effect(trigger_ids=[5303], visible=True)
        self.set_effect(trigger_ids=[5304], visible=True)
        self.set_effect(trigger_ids=[5305], visible=True)
        self.set_effect(trigger_ids=[5306], visible=True)
        self.set_effect(trigger_ids=[5307], visible=True)
        self.set_effect(trigger_ids=[5308], visible=True)
        self.set_effect(trigger_ids=[5309], visible=True)
        self.set_effect(trigger_ids=[5310], visible=True)
        self.set_effect(trigger_ids=[5311], visible=True)
        self.set_effect(trigger_ids=[5312], visible=True)
        self.set_effect(trigger_ids=[5313], visible=True)
        self.set_effect(trigger_ids=[5314], visible=True)
        self.set_effect(trigger_ids=[5315], visible=True)
        self.add_balloon_talk(msg='$52000111_QD__52000111__2$', duration=6000, delay_tick=1000)
        self.show_guide_summary(entity_id=25201111, text_id=25201111, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10012]):
            return 쉐도우클로등장씬01(self.ctx)


# ########################씬2 쉐도우클로 등장########################
class 쉐도우클로등장씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=9000, enable=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 쉐도우클로등장씬02(self.ctx)


class 쉐도우클로등장씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=2000, patrol_name='MS2PatrolData_pcFront')
        self.add_balloon_talk(msg='$52000111_QD__52000111__3$', duration=6000, delay_tick=1000)
        self.set_pc_emotion_loop(sequence_name='Assassin_Bore_A', duration=25000.0)
        self.select_camera_path(path_ids=[1006,1007], return_view=False)
        self.move_user(map_id=52000111, portal_id=10)
        self.set_effect(trigger_ids=[5300])
        self.set_effect(trigger_ids=[5301])
        self.set_effect(trigger_ids=[5302])
        self.set_effect(trigger_ids=[5303])
        self.set_effect(trigger_ids=[5304])
        self.set_effect(trigger_ids=[5305])
        self.set_effect(trigger_ids=[5306])
        self.set_effect(trigger_ids=[5307])
        self.set_effect(trigger_ids=[5308])
        self.set_effect(trigger_ids=[5309])
        self.set_effect(trigger_ids=[5310])
        self.set_effect(trigger_ids=[5311])
        self.set_effect(trigger_ids=[5312])
        self.set_effect(trigger_ids=[5313])
        self.set_effect(trigger_ids=[5314])
        self.set_effect(trigger_ids=[5315])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 쉐도우클로등장씬04(self.ctx)


class 쉐도우클로등장씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Assassin_Bore_A'])
        self.add_balloon_talk(msg='$52000111_QD__52000111__4$', duration=6000, delay_tick=1000)
        self.select_camera_path(path_ids=[1012,1013], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 쉐도우클로등장씬05(self.ctx)


class 쉐도우클로등장씬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8000], visible=True)
        self.set_effect(trigger_ids=[8001], visible=True)
        self.set_effect(trigger_ids=[8002], visible=True)
        self.set_effect(trigger_ids=[8003], visible=True)
        self.set_effect(trigger_ids=[8004], visible=True)
        self.set_effect(trigger_ids=[8005], visible=True)
        self.set_effect(trigger_ids=[8006], visible=True)
        self.set_effect(trigger_ids=[8007], visible=True)
        self.set_effect(trigger_ids=[8008], visible=True)
        self.set_effect(trigger_ids=[8009], visible=True)
        self.select_camera_path(path_ids=[1014,1015], return_view=False)
        self.spawn_npc_range(range_ids=[202,203,204,205,206,207,208,209,210,211])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 쉐도우클로등장씬06(self.ctx)


class 쉐도우클로등장씬06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8010], visible=True)
        self.spawn_monster(spawn_ids=[200], auto_target=False)
        self.select_camera_path(path_ids=[1016,1017], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 쉐도우클로등장씬07(self.ctx)


class 쉐도우클로등장씬07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=200, sequence_name='Sit_Down_A', duration=4000.0)
        self.select_camera_path(path_ids=[1018,1019], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 쉐도우클로등장씬09(self.ctx)


class 쉐도우클로등장씬09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=200, sequence_name='Bore_A')
        self.select_camera_path(path_ids=[1020,1021], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 쉐도우클로등장씬11(self.ctx)


class 쉐도우클로등장씬11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1022,1023], return_view=False)
        self.show_caption(type='NameCaption', title='$52000111_QD__52000111__5$', desc='$52000111_QD__52000111__6$', align=Align.Center, offset_rate_x=-0.15, offset_rate_y=0.15, duration=10000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 쉐도우클로등장씬11_1(self.ctx)


class 쉐도우클로등장씬11_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 쉐도우클로등장씬12(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=2000, patrol_name='MS2PatrolData_pcFront')
        self.move_user(map_id=52000111, portal_id=10)
        self.set_effect(trigger_ids=[5300])
        self.set_effect(trigger_ids=[5301])
        self.set_effect(trigger_ids=[5302])
        self.set_effect(trigger_ids=[5303])
        self.set_effect(trigger_ids=[5304])
        self.set_effect(trigger_ids=[5305])
        self.set_effect(trigger_ids=[5306])
        self.set_effect(trigger_ids=[5307])
        self.set_effect(trigger_ids=[5308])
        self.set_effect(trigger_ids=[5309])
        self.set_effect(trigger_ids=[5310])
        self.set_effect(trigger_ids=[5311])
        self.set_effect(trigger_ids=[5312])
        self.set_effect(trigger_ids=[5313])
        self.set_effect(trigger_ids=[5314])
        self.set_effect(trigger_ids=[5315])
        self.set_effect(trigger_ids=[8000], visible=True)
        self.set_effect(trigger_ids=[8001], visible=True)
        self.set_effect(trigger_ids=[8002], visible=True)
        self.set_effect(trigger_ids=[8003], visible=True)
        self.set_effect(trigger_ids=[8004], visible=True)
        self.set_effect(trigger_ids=[8005], visible=True)
        self.set_effect(trigger_ids=[8006], visible=True)
        self.set_effect(trigger_ids=[8007], visible=True)
        self.set_effect(trigger_ids=[8008], visible=True)
        self.set_effect(trigger_ids=[8009], visible=True)
        self.spawn_npc_range(range_ids=[202,203,204,205,206,207,208,209,210,211])
        self.destroy_monster(spawn_ids=[200])
        self.spawn_monster(spawn_ids=[200], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 쉐도우클로등장씬12(self.ctx)


class 쉐도우클로등장씬12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(trigger_ids=[8010], visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.set_effect(trigger_ids=[5300])
        self.set_effect(trigger_ids=[5301])
        self.set_effect(trigger_ids=[5302])
        self.set_effect(trigger_ids=[5303])
        self.set_effect(trigger_ids=[5304])
        self.set_effect(trigger_ids=[5305])
        self.set_effect(trigger_ids=[5306])
        self.set_effect(trigger_ids=[5307])
        self.set_effect(trigger_ids=[5308])
        self.set_effect(trigger_ids=[5309])
        self.set_effect(trigger_ids=[5310])
        self.set_effect(trigger_ids=[5312])
        self.set_effect(trigger_ids=[5313])
        self.set_effect(trigger_ids=[5314])
        self.destroy_monster(spawn_ids=[200])
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.show_guide_summary(entity_id=25201112, text_id=25201112, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002306], quest_states=[1]):
            # 퀘스트 20002305 완료 시
            return 쉐도우클로와떠남01(self.ctx)


# ########################씬3 쉐도우클로와pc, 재즈바로########################
class 쉐도우클로와떠남01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.show_guide_summary(entity_id=25201113, text_id=25201113, duration=5000)


# ########################씬4 PC, 대탈출########################
class PC대탈출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=9001, enable=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[300,301,302], auto_target=False)
        self.move_user(map_id=52000111, portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return PC대탈출02(self.ctx)


class PC대탈출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_3, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1008,1009], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Push_A', duration=8000.0)
        self.face_emotion(emotion_name='PC_Pain_86000')
        self.set_npc_emotion_loop(spawn_id=300, sequence_name='Sit_Down_A', duration=17500.0)
        self.set_npc_emotion_loop(spawn_id=301, sequence_name='Sit_Down_A', duration=17500.0)
        self.set_npc_emotion_loop(spawn_id=302, sequence_name='Sit_Down_A', duration=17500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7800):
            return PC대탈출03(self.ctx)


class PC대탈출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC_GO')
        self.select_camera_path(path_ids=[1010,1011], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return PC대탈출03_1(self.ctx)


class PC대탈출03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC대탈출04(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user_path(patrol_name='MS2PatrolData_PC_GO')
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC대탈출04(self.ctx)


class PC대탈출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.add_balloon_talk(msg='$52000111_QD__52000111__7$', duration=6000, delay_tick=1000)
        self.show_guide_summary(entity_id=25201114, text_id=25201114, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002314], quest_states=[3]):
            return 어쌔신탈출01(self.ctx)


# ########################어쌔신 탈출########################
class 어쌔신탈출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 어쌔신탈출02(self.ctx)


class 어쌔신탈출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000113)


initial_state = 입장
