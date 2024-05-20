""" trigger/52000195_qd/52000195.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003407], quest_states=[1]):
            # 여제의 꿈 퀘스트 진행 유저
            return CameraEffect01(self.ctx)
        if not self.quest_user_detected(box_ids=[2001], quest_ids=[10003407], quest_states=[1]):
            # 여제의 꿈 퀘스트 진행 유저가 아니면 이동
            return 이동(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[204]) # 에레브
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000195, portal_id=5001)
        self.select_camera_path(path_ids=[4003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52000195_QD__52000195__0$', align=Align.Bottom | Align.Left, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CameraEffect03_4(self.ctx)


class CameraEffect03_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_5(self.ctx)


class CameraEffect03_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.destroy_monster(spawn_ids=[204])
        self.visible_my_pc(is_visible=True) # 유저 투명 처리 품
        self.set_visible_ui(ui_names=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'])
        self.add_buff(box_ids=[2001], skill_id=99910402, level=1, is_player=False) # 에레브 변신
        self.add_buff(box_ids=[2001], skill_id=99910402, level=1, is_player=False, is_skill_set=False) # 에레브 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_6(self.ctx)


class CameraEffect03_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_7(self.ctx)


class CameraEffect03_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000195_QD__52000195__1$', align=Align.Left, illust_id='Ereb_surprise', duration=3000)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000195_QD__52000195__2$', align=Align.Left, illust_id='Ereb_serious', duration=3000)
        self.add_cinematic_talk(npc_id=11001302, msg='$52000195_QD__52000195__3$', align=Align.Left, illust_id='Ereb_serious', duration=3000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return CameraEffect03_8(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.destroy_monster(spawn_ids=[204])
        self.visible_my_pc(is_visible=True) # 유저 투명 처리 품
        self.set_visible_ui(ui_names=['MessengerBrowser','GroupMessengerBrowser','HighlightGameMenu'])
        self.add_buff(box_ids=[2001], skill_id=99910402, level=1, is_player=False) # 에레브 변신
        self.add_buff(box_ids=[2001], skill_id=99910402, level=1, is_player=False, is_skill_set=False) # 에레브 변신

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_8(self.ctx)


class CameraEffect03_8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2002]):
            return 과거장면_01(self.ctx)


class 과거장면_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 과거장면_02(self.ctx)


class 과거장면_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.spawn_monster(spawn_ids=[201]) # 바론
        self.spawn_monster(spawn_ids=[202]) # 칼
        self.spawn_monster(spawn_ids=[203]) # 에레브
        self.remove_buff(box_id=2002, skill_id=99910402)
        self.visible_my_pc(is_visible=False) # 유저 투명 처리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 과거장면_03(self.ctx)


class 과거장면_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 과거장면_05(self.ctx)


class 과거장면_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000195_QD__52000195__4$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 과거장면_06(self.ctx)


class 과거장면_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Talk_A', duration=8000.0)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000195_QD__52000195__5$', align=Align.Right, illust_id='Karl_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000195_QD__52000195__6$', align=Align.Right, illust_id='Karl_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 과거장면_07(self.ctx)


class 과거장면_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000195_QD__52000195__7$', align=Align.Right, illust_id='Baron_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 과거장면_08(self.ctx)


class 과거장면_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 과거장면_08_1(self.ctx)


class 과거장면_08_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000195_QD__52000195__8$', align=Align.Right, illust_id='Karl_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 과거장면_08_2(self.ctx)


class 과거장면_08_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202])
        self.select_camera_path(path_ids=[4009], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 과거장면_09(self.ctx)


class 과거장면_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11004785, msg='$52000195_QD__52000195__9$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 과거장면_10(self.ctx)


class 과거장면_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11004785, msg='$52000195_QD__52000195__10$', illust_id='Ereb_surprise', duration=4000)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000195_QD__52000195__11$', illust_id='Ereb_surprise', duration=4000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 업적달성(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 업적달성(self.ctx)


class 업적달성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2002, achieve='DreamofEreb')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000193, portal_id=5001)


initial_state = start
