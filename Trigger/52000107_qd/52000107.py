""" trigger/52000107_qd/52000107.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_portal(portal_id=1)
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
        self.set_effect(trigger_ids=[5323]) # 경로 안내
        self.set_effect(trigger_ids=[5324]) # 경로 안내
        self.set_effect(trigger_ids=[5325]) # 경로 안내
        self.set_effect(trigger_ids=[5326]) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10010]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000107, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='common\\JobIntro_HeavyGunner.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 에델슈타인전경씬01(self.ctx)
        if self.wait_tick(wait_tick=42000):
            return 에델슈타인전경씬01(self.ctx)


class 에델슈타인전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1000,1001], return_view=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8500):
            return 에델슈타인전경씬01_B(self.ctx)


class 에델슈타인전경씬01_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에델슈타인전경씬02(self.ctx)


class 에델슈타인전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1002,1003,1004,1005], return_view=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에델슈타인전경씬03(self.ctx)


class 에델슈타인전경씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000107_QD__52000107__0$', desc='$52000107_QD__52000107__1$', align=Align.Bottom | Align.Left, duration=7000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에델슈타인전경씬04(self.ctx)


class 에델슈타인전경씬04(trigger_api.Trigger):
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
        self.set_effect(trigger_ids=[5323], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5324], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5325], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5326], visible=True) # 경로 안내
        self.add_balloon_talk(msg='$52000107_QD__52000107__2$', duration=6000, delay_tick=1000)
        self.show_guide_summary(entity_id=25201071, text_id=25201071, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10011]):
            return 아이샤등장씬01(self.ctx)


# ########################씬2 아이샤 등장########################
class 아이샤등장씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[2000], auto_target=False) # 아이샤등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아이샤등장씬02(self.ctx)


class 아이샤등장씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=2000, patrol_name='MS2PatrolData_Ayesha_go')
        self.select_camera_path(path_ids=[1006,1007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아이샤등장씬04(self.ctx)


class 아이샤등장씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003291, illust_id='Ayesha_normal', msg='$52000107_QD__52000107__3$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000970, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000970.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 아이샤등장씬05(self.ctx)


class 아이샤등장씬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=200, emotion_name='hello_Cait')
        self.show_caption(type='NameCaption', title='$52000107_QD__52000107__4$', desc='$52000107_QD__52000107__5$', align=Align.Center, offset_rate_x=-0.15, offset_rate_y=0.15, duration=10000, scale=2.0)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 아이샤등장씬06(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아이샤등장씬06(self.ctx)


class 아이샤등장씬06(trigger_api.Trigger):
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
        self.set_effect(trigger_ids=[5323]) # 경로 안내
        self.set_effect(trigger_ids=[5324]) # 경로 안내
        self.set_effect(trigger_ids=[5325]) # 경로 안내
        self.set_effect(trigger_ids=[5326]) # 경로 안내
        self.face_emotion(spawn_id=200)
        self.show_guide_summary(entity_id=25201071, text_id=25201071, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10011], quest_ids=[20002296], quest_states=[2]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 아이샤와떠남01(self.ctx)


# ########################씬3 아이샤와pc, 퓨전코어 연구실로########################
class 아이샤와떠남01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=2000, msg='$52000107_QD__52000107__6$', duration=6000, delay_tick=1000)
        self.set_onetime_effect(id=3000971, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000971.xml')
        self.move_npc(spawn_id=2000, patrol_name='MS2PatrolData_Ayesga_out')
        self.show_guide_summary(entity_id=25201072, text_id=25201072, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=10012, spawn_ids=[2000]):
            return 아이샤와떠남02(self.ctx)


class 아이샤와떠남02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.destroy_monster(spawn_ids=[2000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9003, spawn_ids=[202]):
            return None # Missing State: 아이샤와떠남03


initial_state = Wait
