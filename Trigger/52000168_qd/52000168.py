""" trigger/52000168_qd/52000168.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401], auto_target=False) # 바사라첸
        self.spawn_monster(spawn_ids=[402], auto_target=False) # 바사라첸
        self.spawn_monster(spawn_ids=[403], auto_target=False) # 바사라첸
        self.spawn_monster(spawn_ids=[404], auto_target=False) # 바사라첸
        self.spawn_monster(spawn_ids=[405], auto_target=False) # 바사라첸
        self.spawn_monster(spawn_ids=[406], auto_target=False) # 바사라첸
        self.move_user(map_id=52000168, portal_id=80)
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='jobChange_RBlader.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 전경씬01(self.ctx)
        if self.wait_tick(wait_tick=8000):
            return 전경씬01(self.ctx)


class 전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_pc_emotion_loop(sequence_name='Push_A', duration=10000.0, arg3=True)
        self.set_npc_emotion_loop(spawn_id=402, sequence_name='Attack_Idle_A', duration=1000000.0)
        self.set_npc_emotion_loop(spawn_id=403, sequence_name='Dead_A', duration=800000.0)
        self.set_npc_emotion_loop(spawn_id=404, sequence_name='Dead_A', duration=800000.0)
        self.set_npc_emotion_loop(spawn_id=405, sequence_name='Dead_A', duration=800000.0)
        self.set_npc_emotion_loop(spawn_id=406, sequence_name='Dead_A', duration=800000.0)
        self.select_camera_path(path_ids=[4000,4001,4003], return_view=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 전경씬02(self.ctx)


class 전경씬02(trigger_api.Trigger):
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
        self.show_guide_summary(entity_id=52001681, text_id=52001681, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002373], quest_states=[3]):
            return 전직이펙트_01(self.ctx)


class 전직이펙트_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전직이펙트_02(self.ctx)


class 전직이펙트_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[402])
        self.destroy_monster(spawn_ids=[403])
        self.destroy_monster(spawn_ids=[404])
        self.destroy_monster(spawn_ids=[405])
        self.destroy_monster(spawn_ids=[406])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전직이펙트_03(self.ctx)


class 전직이펙트_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit03(self.ctx)


# ########################퀘스트 종료########################
class Quit03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[402])
        self.destroy_monster(spawn_ids=[403])
        self.destroy_monster(spawn_ids=[404])
        self.destroy_monster(spawn_ids=[405])
        self.destroy_monster(spawn_ids=[406])
        self.spawn_monster(spawn_ids=[500], auto_target=False)
        self.spawn_monster(spawn_ids=[501], auto_target=False)
        self.spawn_monster(spawn_ids=[502], auto_target=False)
        self.move_npc(spawn_id=500, patrol_name='MS2PatrolData_500')
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_501')
        self.move_npc(spawn_id=502, patrol_name='MS2PatrolData_502')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002374], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 칼리브요새로01(self.ctx)


class 칼리브요새로01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 칼리브요새로02(self.ctx)


class 칼리브요새로02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000169, portal_id=1)


initial_state = Wait
