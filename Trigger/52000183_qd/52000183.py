""" trigger/52000183_qd/52000183.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[500], auto_target=False)
        self.spawn_monster(spawn_ids=[501], auto_target=False)
        self.spawn_monster(spawn_ids=[502], auto_target=False)
        self.spawn_monster(spawn_ids=[503], auto_target=False)
        self.spawn_monster(spawn_ids=[504], auto_target=False)
        self.spawn_monster(spawn_ids=[505], auto_target=False)
        self.spawn_monster(spawn_ids=[506], auto_target=False)
        self.spawn_monster(spawn_ids=[507], auto_target=False)
        self.spawn_monster(spawn_ids=[508], auto_target=False)
        self.spawn_monster(spawn_ids=[509], auto_target=False)
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='jobChange_priest.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 전경씬01(self.ctx)
        if self.wait_tick(wait_tick=8000):
            return 전경씬01(self.ctx)


class 전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000183, portal_id=80)
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=30, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.select_camera_path(path_ids=[4000,4001,4002], return_view=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전경씬02_b(self.ctx)


class 전경씬02_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Priest_HeavensPray3_A'])
        self.set_npc_emotion_loop(spawn_id=500, sequence_name='Bore_A', duration=8000.0)
        self.set_npc_emotion_loop(spawn_id=501, sequence_name='Idle_A', duration=8000.0)
        self.set_npc_emotion_loop(spawn_id=502, sequence_name='Idle_A', duration=8000.0)
        self.set_npc_emotion_loop(spawn_id=503, sequence_name='Bore_A', duration=8000.0)
        self.set_npc_emotion_loop(spawn_id=504, sequence_name='Idle_A', duration=8000.0)
        self.set_npc_emotion_loop(spawn_id=505, sequence_name='Bore_A', duration=8000.0)
        self.set_npc_emotion_loop(spawn_id=506, sequence_name='Idle_A', duration=8000.0)
        self.set_npc_emotion_loop(spawn_id=507, sequence_name='Bore_A', duration=8000.0)

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
        self.move_npc(spawn_id=502, patrol_name='MS2PatrolData_502')
        self.move_npc(spawn_id=503, patrol_name='MS2PatrolData_503')
        self.move_npc(spawn_id=505, patrol_name='MS2PatrolData_505')
        self.move_npc(spawn_id=506, patrol_name='MS2PatrolData_506')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.show_guide_summary(entity_id=52001831, text_id=52001831, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002341], quest_states=[3]):
            return 전직이펙트_01(self.ctx)


class 전직이펙트_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전직이펙트_02(self.ctx)


class 전직이펙트_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002342], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 가브란트퇴장01(self.ctx)


# ########################전원 퇴장########################
class 가브란트퇴장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=509, patrol_name='MS2PatrolData_gabExit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9002, spawn_ids=[509]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[509])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002343], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 전원퇴장01(self.ctx)


class 전원퇴장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전원퇴장01_b(self.ctx)


class 전원퇴장01_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000183, portal_id=81)
        self.destroy_monster(spawn_ids=[500])
        self.destroy_monster(spawn_ids=[501])
        self.destroy_monster(spawn_ids=[502])
        self.destroy_monster(spawn_ids=[502])
        self.destroy_monster(spawn_ids=[503])
        self.destroy_monster(spawn_ids=[504])
        self.destroy_monster(spawn_ids=[505])
        self.destroy_monster(spawn_ids=[506])
        self.destroy_monster(spawn_ids=[507])
        self.destroy_monster(spawn_ids=[508])
        self.destroy_monster(spawn_ids=[509])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전원퇴장02(self.ctx)


class 전원퇴장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.show_guide_summary(entity_id=52001832, text_id=52001832, duration=10000)
        self.spawn_monster(spawn_ids=[510], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002345], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return 프론티아재단으로01(self.ctx)


# ########################퀘스트 종료########################
class 프론티아재단으로01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 프론티아재단으로02(self.ctx)


class 프론티아재단으로02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000186, portal_id=1)


initial_state = Wait
