""" trigger/52010070_qd/52010070.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2001], job_code=0):
            return 엔피씨스폰(self.ctx)


class 엔피씨스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 유페리아
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 이슈라
        self.spawn_monster(spawn_ids=[103], auto_target=False) # 렌듀비앙
        self.spawn_monster(spawn_ids=[107], auto_target=False) # 라네모네
        self.spawn_monster(spawn_ids=[109], auto_target=False) # 홀슈타트
        self.set_effect(trigger_ids=[5001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100800], quest_states=[2]):
            return 룬블즈_일어남(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100790], quest_states=[2]):
            return 룬블즈_일어남(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100790], quest_states=[3]):
            return 룬블즈_일어남(self.ctx)


class 룬블즈_일어남(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_cinematic_ui(type=1)
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.move_user(map_id=52010070, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 룬블즈_일어남_02(self.ctx)


class 룬블즈_일어남_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 룬블즈_일어남_03(self.ctx)


class 룬블즈_일어남_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=109, sequence_name='Attack_Idle_A', duration=4000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 룬블즈_일어남_04(self.ctx)


class 룬블즈_일어남_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.set_npc_emotion_loop(spawn_id=107, sequence_name='Bore_A', duration=4000.0)
        self.set_npc_emotion_loop(spawn_id=109, sequence_name='Attack_01_A', duration=4000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 룬블즈_일어남_04_01(self.ctx)


class 룬블즈_일어남_04_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=0.1, end_scale=0.5, duration=5.0, interpolator=1)
        self.set_npc_emotion_loop(spawn_id=109, sequence_name='Attack_Idle_A', duration=4000.0)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 룬블즈_일어남_05(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 룬블즈_일어남_05(self.ctx)


class 룬블즈_일어남_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 룬블즈_일어남_07(self.ctx)


class 룬블즈_일어남_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False) # 유페리아
        self.spawn_monster(spawn_ids=[105], auto_target=False) # 이슈라
        self.spawn_monster(spawn_ids=[106], auto_target=False) # 렌듀비앙
        self.destroy_monster(spawn_ids=[101], arg2=False)
        self.destroy_monster(spawn_ids=[102], arg2=False)
        self.destroy_monster(spawn_ids=[103], arg2=False)
        self.set_effect(trigger_ids=[5001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 룬블즈_일어남_08(self.ctx)


class 룬블즈_일어남_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 룬블즈_일어남_09(self.ctx)


class 룬블즈_일어남_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 룬블즈_일어남_09_01(self.ctx)


class 룬블즈_일어남_09_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 룬블즈_일어남_10(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=30, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 룬블즈_일어남_10(self.ctx)


class 룬블즈_일어남_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100790], quest_states=[3]):
            return 홀슈타트로바꾸기(self.ctx)


class 홀슈타트로바꾸기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.destroy_monster(spawn_ids=[109], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100800], quest_states=[2]):
            return 에레브흑화(self.ctx)


class 에레브흑화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Skip_3, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에레브흑화_02(self.ctx)


class 에레브흑화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에레브흑화_03(self.ctx)


class 에레브흑화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에레브흑화_04(self.ctx)


class 에레브흑화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52010070, portal_id=6001)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_3001')
        self.add_cinematic_talk(npc_id=11004128, align=Align.Left, illust_id='Ishura_normal', msg='$52010070_QD__52010070__0$', duration=4000)
        self.add_cinematic_talk(npc_id=11004191, align=Align.Left, illust_id='11004022', msg='$52010070_QD__52010070__1$', duration=4000)
        self.add_cinematic_talk(npc_id=11004128, align=Align.Left, illust_id='Ishura_normal', msg='$52010070_QD__52010070__2$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return 에레브흑화_05(self.ctx)


class 에레브흑화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='ProphecyofFall.swf', movie_id=1)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 에레브흑화_06(self.ctx)
        if self.wait_tick(wait_tick=85000):
            return 에레브흑화_06(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에레브흑화_06(self.ctx)


class 에레브흑화_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100800], quest_states=[3]):
            return 이동시키기(self.ctx)


class 이동시키기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010072, portal_id=1)


initial_state = wait_01
