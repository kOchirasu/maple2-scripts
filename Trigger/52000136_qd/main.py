""" trigger/52000136_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601,602])
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001604], quest_states=[1]):
            return 기본(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001603], quest_states=[3]):
            return 기본(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001603], quest_states=[2]):
            return 연출시작(self.ctx)


class 기본(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 첫진입(self.ctx)


class 첫진입(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000136_QD__MAIN__0$', duration=3000, align=Align.Left)
        self.set_scene_skip(state=불안한케이틀린_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전경스케치01(self.ctx)


class 전경스케치01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_skip(state=불안한케이틀린_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 전경스케치02(self.ctx)


class 전경스케치02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.move_user(map_id=52000136, portal_id=10)
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 케이틀린발견01(self.ctx)


class 케이틀린발견01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='Patrol_101_katelyn_wander')
        self.add_balloon_talk(spawn_id=101, msg='$52000136_QD__MAIN__1$', duration=1000)
        self.add_balloon_talk(spawn_id=101, msg='$52000136_QD__MAIN__2$', duration=1000, delay_tick=500)
        self.add_balloon_talk(spawn_id=101, msg='$52000136_QD__MAIN__3$', duration=1000, delay_tick=500)
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 케이틀린발견02(self.ctx)


class 케이틀린발견02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000136_QD__MAIN__4$', duration=3000, align=Align.Left)
        self.move_user_path(patrol_name='MS2PatrolData_PC')
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 케이틀린발견03(self.ctx)


class 케이틀린발견03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.add_balloon_talk(spawn_id=101, msg='$52000136_QD__MAIN__5$', duration=3000, delay_tick=500)
        self.move_npc(spawn_id=101, patrol_name='Patrol_101_katelyn_run')
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 케이틀린대사01(self.ctx)


class 케이틀린대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003261, script='$52000136_QD__MAIN__6$', time=3)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4300.0)
        self.set_skip(state=불안한케이틀린_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC대사01(self.ctx)


"""
class 케이틀린대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC대사01(self.ctx)
"""

class PC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000136_QD__MAIN__7$', duration=3000, align=Align.Left)
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 케이틀린대사02(self.ctx)


class 케이틀린대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003261, script='$52000136_QD__MAIN__8$', time=3)
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 문줌인(self.ctx)


class 문줌인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010,8011], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 불안한케이틀린_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010,8011], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52000136, portal_id=11)
        self.move_npc(spawn_id=101, patrol_name='Patrol_101_katelyn_run') # 케이틀린 위치로

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
