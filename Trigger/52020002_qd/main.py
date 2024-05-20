""" trigger/52020002_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4001,4002], visible=True)
        self.destroy_monster(spawn_ids=[120,121])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001779], quest_states=[3]):
            return 진행이후_기본(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001775,50001776,50001777,50001778,50001779], quest_states=[1,2]):
            return 제이든보고연출_완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001774], quest_states=[3]):
            return 제이든보고연출_완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001774], quest_states=[2]):
            return 제이든보고연출_완료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001774], quest_states=[1]):
            return 제이든보고연출_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001773], quest_states=[3]):
            return 기본(self.ctx)


class 기본(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 진행이후_기본(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4001,4002])
        self.destroy_monster(spawn_ids=[120,121])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 제이든보고연출_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[120], auto_target=False)
        self.set_mesh(trigger_ids=[4001,4002])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출준비(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020002, portal_id=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(is_visible=False) # 유저 투명 처리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_scene_skip(state=제이든보고_스킵완료, action='nextState') # setsceneskip set
        # setsceneskip set
        # setsceneskip set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 제이든등장(self.ctx)


class 제이든등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003540, illust_id='Jaiden_normal', msg='안녕하세요? 제가 나타났습니다.\\n연출은 제작 중이니 기다려 주세요.', duration=3000)
        self.set_npc_emotion_loop(spawn_id=120, sequence_name='Talk_A', duration=3000.0)
        self.set_skip(state=skip01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 제이든보고_스킵완료(self.ctx)


class skip01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 제이든보고_스킵완료(self.ctx)


"""
class 케이틀린탈주01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_100_wayout')
        self.move_user_path(patrol_name='MS2PatrolData_PC01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 케이틀린탈주02(self.ctx)
"""

"""
class 케이틀린탈주02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003262, script='$02000035_IN__MAIN__7$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 케이틀린탈주03(self.ctx)
"""

"""
class 케이틀린탈주03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101_wayout')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC멈칫(self.ctx)
"""

"""
class PC멈칫(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$02000035_IN__MAIN__11$', time=2)
        self.destroy_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 앤대사03(self.ctx)
"""

"""
class 앤대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003264, script='$02000035_IN__MAIN__8$', time=3)
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='ChatUp_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4022):
            return 연출종료(self.ctx)
"""

class 제이든보고_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[120])
        self.spawn_monster(spawn_ids=[121], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9000, type='trigger', achieve='JaidenReportstoRadin')
        self.reset_camera(interpolation_time=2.0)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.visible_my_pc(is_visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 제이든보고연출_완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[120])
        self.spawn_monster(spawn_ids=[121], auto_target=False)
        self.set_mesh(trigger_ids=[4001,4002])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
