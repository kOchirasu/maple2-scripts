""" trigger/52000104_qd/52000104.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_portal(portal_id=2)
        self.spawn_monster(spawn_ids=[205], auto_target=False) # 리에나플라워등장
        self.set_effect(trigger_ids=[5300]) # 경로 안내
        self.set_effect(trigger_ids=[5301]) # 경로 안내
        self.set_effect(trigger_ids=[5302]) # 경로 안내
        self.set_effect(trigger_ids=[5303]) # 경로 안내
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
        self.set_effect(trigger_ids=[5400]) # 경로 안내
        self.set_effect(trigger_ids=[5401]) # 경로 안내
        self.set_effect(trigger_ids=[5402]) # 경로 안내
        self.set_effect(trigger_ids=[5403]) # 경로 안내
        self.set_effect(trigger_ids=[5404]) # 경로 안내
        self.set_effect(trigger_ids=[5405]) # 경로 안내
        self.set_effect(trigger_ids=[5406]) # 경로 안내
        self.set_effect(trigger_ids=[5407]) # 경로 안내
        self.set_effect(trigger_ids=[5408]) # 경로 안내
        self.set_effect(trigger_ids=[5409]) # 경로 안내
        self.set_effect(trigger_ids=[5410]) # 경로 안내
        self.set_effect(trigger_ids=[5411]) # 경로 안내
        self.set_effect(trigger_ids=[5412]) # 경로 안내
        self.set_effect(trigger_ids=[5413]) # 경로 안내
        self.set_effect(trigger_ids=[5414]) # 경로 안내
        self.set_effect(trigger_ids=[5415]) # 경로 안내
        self.set_effect(trigger_ids=[5416]) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10011]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000104, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='common\\JobIntro_Berserker.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 리엔전경씬01(self.ctx)
        if self.wait_tick(wait_tick=75000):
            return 리엔전경씬01(self.ctx)


class 리엔전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1000,1001], return_view=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 리엔전경씬01_B(self.ctx)


class 리엔전경씬01_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 리엔전경씬02(self.ctx)


class 리엔전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1002,1003], return_view=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 리엔전경씬03(self.ctx)


class 리엔전경씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000104_QD__52000104__0$', desc='$52000104_QD__52000104__1$', align=Align.Bottom | Align.Left, duration=7000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 리엔전경씬04(self.ctx)


class 리엔전경씬04(trigger_api.Trigger):
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
        self.set_effect(trigger_ids=[5300], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5301], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5302], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5303], visible=True) # 경로 안내
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
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.add_balloon_talk(msg='$52000104_QD__52000104__2$', duration=6000, delay_tick=1000)
        self.show_guide_summary(entity_id=25201041, text_id=25201041, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10012]):
            return 리린과대화01(self.ctx)


# ########################씬2 리린 등장########################
class 리린과대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.move_user(map_id=52000104, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 리린과대화02(self.ctx)


class 리린과대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Ririn_Go')
        self.select_camera_path(path_ids=[1004,1005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 리린과대화03(self.ctx)


class 리린과대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1006,1007], return_view=False)
        self.face_emotion(spawn_id=200, emotion_name='hello_Cait')
        self.show_caption(type='NameCaption', title='$52000104_QD__52000104__3$', desc='$52000104_QD__52000104__4$', align=Align.Center, offset_rate_x=-0.15, offset_rate_y=0.15, duration=10000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 리린과대화04(self.ctx)


class 리린과대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 리린과대화05(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolation_time=1.0)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 리린과대화05(self.ctx)


class 리린과대화05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.set_effect(trigger_ids=[5300]) # 경로 안내
        self.set_effect(trigger_ids=[5301]) # 경로 안내
        self.set_effect(trigger_ids=[5302]) # 경로 안내
        self.set_effect(trigger_ids=[5303]) # 경로 안내
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
        self.face_emotion(spawn_id=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002316], quest_states=[1]):
            return 꽃가꾸기퀘스트01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002317], quest_states=[1]):
            return 꽃섬멸퀘스트01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002317], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 할아버지등장씬01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002319], quest_states=[1]):
            return 할아버지등장씬01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002319], quest_states=[2]):
            return 할아버지등장씬01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002319], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 할아버지등장씬01(self.ctx)


class 꽃가꾸기퀘스트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25201042, text_id=25201042, duration=10000)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Ririn_Go2') # 마드리아 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002317], quest_states=[1]):
            return 꽃섬멸퀘스트01(self.ctx)


# ########################씬3 꽃 섬멸 퀘스트########################
class 꽃섬멸퀘스트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1006,1007], return_view=False)
        self.set_cinematic_ui(type=1)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Ririn_Go2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 꽃섬멸퀘스트02(self.ctx)


class 꽃섬멸퀘스트02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1006,1007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 꽃섬멸퀘스트03(self.ctx)


class 꽃섬멸퀘스트03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.spawn_monster(spawn_ids=[200,201,202,203,204], auto_target=False)
        self.set_sound(trigger_id=9000, enable=True) # 코믹한 상황 브금
        self.add_balloon_talk(msg='$52000104_QD__52000104__5$', duration=6000, delay_tick=1000)
        self.show_guide_summary(entity_id=25201043, text_id=25201043, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002317], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 할아버지등장씬01(self.ctx)


# ########################씬4 할아버지 등장########################
class 할아버지등장씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=9000) # 코믹한 상황 브금
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 할아버지등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 할아버지등장씬02(self.ctx)


class 할아버지등장씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_3, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_ten_go')
        self.select_camera_path(path_ids=[1008,1009], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 할아버지등장씬03(self.ctx)


class 할아버지등장씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003175, illust_id='Ten_normal', msg='$52000104_QD__52000104__6$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 할아버지등장씬04(self.ctx)


class 할아버지등장씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='NameCaption', title='$52000104_QD__52000104__7$', desc='$52000104_QD__52000104__8$', align=Align.Center, offset_rate_x=-0.15, offset_rate_y=0.15, duration=10000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 할아버지등장씬04_1(self.ctx)


class 할아버지등장씬04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 할아버지등장씬05(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolation_time=1.0)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_ten_go')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 할아버지등장씬05(self.ctx)


class 할아버지등장씬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_ririn_move') # 마드리아 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002319], quest_states=[1]):
            return 대검바라보기01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002319], quest_states=[2]):
            return 대검바라보기01(self.ctx)
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002319], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 수련장으로이동01(self.ctx)


# ########################씬5 대검 바라보기########################
class 대검바라보기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Ririn_Go3') # 리린 이동
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_ten_go2') # 텐 이동
        self.show_guide_summary(entity_id=25201044, text_id=25201044, duration=10000)
        self.set_effect(trigger_ids=[5400], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5401], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5402], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5403], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5404], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5405], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5406], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5407], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5408], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5409], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5410], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5411], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5412], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5413], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5414], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5415], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5416], visible=True) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002319], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 수련장으로이동01(self.ctx)


class 수련장으로이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5400]) # 경로 안내
        self.set_effect(trigger_ids=[5401]) # 경로 안내
        self.set_effect(trigger_ids=[5402]) # 경로 안내
        self.set_effect(trigger_ids=[5403]) # 경로 안내
        self.set_effect(trigger_ids=[5404]) # 경로 안내
        self.set_effect(trigger_ids=[5405]) # 경로 안내
        self.set_effect(trigger_ids=[5406]) # 경로 안내
        self.set_effect(trigger_ids=[5407]) # 경로 안내
        self.set_effect(trigger_ids=[5408]) # 경로 안내
        self.set_effect(trigger_ids=[5409]) # 경로 안내
        self.set_effect(trigger_ids=[5410]) # 경로 안내
        self.set_effect(trigger_ids=[5411]) # 경로 안내
        self.set_effect(trigger_ids=[5412]) # 경로 안내
        self.set_effect(trigger_ids=[5413]) # 경로 안내
        self.set_effect(trigger_ids=[5414]) # 경로 안내
        self.set_effect(trigger_ids=[5415]) # 경로 안내
        self.set_effect(trigger_ids=[5416]) # 경로 안내
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Ririn_Go') # 리린 이동
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_ten_exit') # 텐 이동
        self.add_balloon_talk(msg='$52000104_QD__52000104__9$', duration=6000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=101, msg='$52000104_QD__52000104__10$', duration=6000, delay_tick=2500)
        self.show_guide_summary(entity_id=25201045, text_id=25201045, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=10013, spawn_ids=[102]):
            return 수련장으로이동02(self.ctx)


class 수련장으로이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.destroy_monster(spawn_ids=[102])


initial_state = Wait
