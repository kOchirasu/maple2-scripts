""" trigger/52000149_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,111,112])
        self.set_effect(trigger_ids=[6001,6002], visible=True)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Sit_Down_A', duration=100000000.0) # 아시모프
        self.set_npc_emotion_loop(spawn_id=112, sequence_name='Event_02_Idle', duration=100000000.0) # 아노스
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001633], quest_states=[2]):
            return 빈집(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001633], quest_states=[1]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001632], quest_states=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001632], quest_states=[2]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001632], quest_states=[1]):
            return 전경_연출준비(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001631], quest_states=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001631], quest_states=[2]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001631], quest_states=[1]):
            return 기본상태(self.ctx)


class 기본상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001632], quest_states=[1]):
            return 전경_연출준비(self.ctx)


class 전경_연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000149, portal_id=10)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 전경_연출시작(self.ctx)


class 전경_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000,8010], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_pc')
        self.set_scene_skip(state=아노스아파_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라_아노스줌인(self.ctx)


class 카메라_아노스줌인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.add_cinematic_talk(npc_id=11003436, msg='$52000149_QD__MAIN__0$', duration=3000)
        self.set_skip(state=아노스아파_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라_아노스줌인01(self.ctx)


class 카메라_아노스줌인01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라_케이틀린01(self.ctx)


class 카메라_케이틀린01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002,8004], return_view=False)
        self.add_cinematic_talk(npc_id=11003436, msg='$52000149_QD__MAIN__1$', duration=3000)
        self.set_skip(state=아노스아파_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라_케이틀린0102(self.ctx)


class 카메라_케이틀린0102(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라_케이틀린02(self.ctx)


class 카메라_케이틀린02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Idle_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=11003436, msg='$52000149_QD__MAIN__2$', duration=3000)
        self.add_balloon_talk(spawn_id=102, msg='$52000149_QD__MAIN__3$', duration=3000)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_katelyn')
        self.set_skip(state=아노스아파_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 호르헤이동(self.ctx)


class 호르헤이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Jorge')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 빈집(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111,112])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 연출종료(self.ctx)


class 아노스아파_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52000149, portal_id=11)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Jorge')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='AnosReturns')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
