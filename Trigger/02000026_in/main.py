""" trigger/02000026_in/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102])
        self.set_mesh(trigger_ids=[4001,4002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001568], quest_states=[3]):
            return 조건체크01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001568], quest_states=[2]):
            return 아노스있음01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001568], quest_states=[1]):
            return 아노스만남연출대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001567], quest_states=[3]):
            return 대기조건01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001567], quest_states=[2]):
            return 대기조건01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001567], quest_states=[1]):
            return 기본상태(self.ctx)


class 대기조건01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001568], quest_states=[1]):
            return 아노스만남연출시작(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001568], quest_states=[1]):
            return start(self.ctx)


class 조건체크01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001569], quest_states=[1]):
            return 아노스있음01(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001569], quest_states=[1]):
            return 조건체크02(self.ctx)


class 조건체크02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001573], quest_states=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001568,50001569,50001570,50001571,50001572,50001573], quest_states=[2]):
            return 아노스있음01(self.ctx)


class 기본상태(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return start(self.ctx)


class 아노스있음01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_mesh(trigger_ids=[4001,4002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 아노스만남연출대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_mesh(trigger_ids=[4001,4002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            self.move_user_path(patrol_name='MS2PatrolData_PC_00')
            return 아노스만남연출시작(self.ctx)


class 아노스만남연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8000], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 아노스등장(self.ctx)


class 아노스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_00')
        self.set_dialogue(type=2, spawn_id=11003313, script='$02000026_IN__MAIN__0$', time=4)
        self.set_scene_skip(state=아노스만남_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아노스이동01(self.ctx)


class 아노스이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_01')
        self.set_dialogue(type=2, spawn_id=11003313, script='$02000026_IN__MAIN__1$', time=3)
        # self.set_skip(state=아노스만남_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3239):
            return 아노스이동02(self.ctx)


class 아노스이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Anos_02')
        # self.set_skip(state=아노스만남_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아노스이동03(self.ctx)


class 아노스이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003313, script='$02000026_IN__MAIN__2$', time=3)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='ChatUp_A')
        # self.set_skip(state=아노스만남_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4623):
            return 아노스대사01(self.ctx)


class 아노스대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003313, script='$02000026_IN__MAIN__3$', time=4)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=아노스대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라이동_라딘01(self.ctx)


class 아노스대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 카메라이동_라딘01(self.ctx)


class 카메라이동_라딘01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라딘대사01(self.ctx)


class 라딘대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000264, script='$02000026_IN__MAIN__4$', time=3)
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Bore_A')
        self.set_skip(state=라딘대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4623):
            return 아노스대사02(self.ctx)


class 라딘대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사02(self.ctx)


class 아노스대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=4000.0)
        self.set_dialogue(type=2, spawn_id=11003313, script='$02000026_IN__MAIN__5$', time=4)
        self.set_skip(state=아노스대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4519):
            return 라딘대사02(self.ctx)


class 아노스대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 라딘대사02(self.ctx)


class 라딘대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='ChatUP_A')
        # self.set_npc_emotion_loop(spawn_id=103, sequence_name='ChatUP_A', duration=4000.0)
        self.set_dialogue(type=2, spawn_id=11000264, script='$02000026_IN__MAIN__6$', time=4)
        self.set_skip(state=라딘대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4780):
            return 카메라이동_아노스01(self.ctx)


class 라딘대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 카메라이동_아노스01(self.ctx)


class 카메라이동_아노스01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아노스대사03(self.ctx)


class 아노스대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='ChatUp_A')
        # self.set_npc_emotion_loop(spawn_id=102, sequence_name='ChatUp_A', duration=3000.0)
        self.set_dialogue(type=2, spawn_id=11003313, script='$02000026_IN__MAIN__7$', time=3)
        self.set_skip(state=아노스대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6817):
            return 아노스대사04(self.ctx)


class 아노스대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사04(self.ctx)


class 아노스대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003313, script='$02000026_IN__MAIN__8$', time=3)
        self.move_user_path(patrol_name='MS2PatrolData_PC_01')
        self.set_skip(state=아노스대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라딘대사03(self.ctx)


class 아노스대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 라딘대사03(self.ctx)


class 라딘대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=4000.0)
        self.set_dialogue(type=2, spawn_id=11000264, script='$02000026_IN__MAIN__9$', time=4)
        self.set_skip(state=라딘대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return PC안녕(self.ctx)


class 라딘대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC안녕(self.ctx)


class PC안녕(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Hello_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사05(self.ctx)


class 아노스대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=3000.0)
        self.set_dialogue(type=2, spawn_id=11003313, script='$02000026_IN__MAIN__10$', time=3)
        self.set_skip(state=아노스대사05_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3343):
            return 아노스대사06(self.ctx)


class 아노스대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아노스대사06(self.ctx)


class 아노스대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Idle_A', duration=3000.0)
        self.set_dialogue(type=2, spawn_id=11003313, script='$02000026_IN__MAIN__11$', time=3)
        self.show_caption(type='NameCaption', title='$02000026_IN__MAIN__12$', desc='$02000026_IN__MAIN__13$', align=Align.Center | Align.Left, offset_rate_x=0.05, offset_rate_y=0.15, duration=5000, scale=2.0)
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출종료(self.ctx)


class 아노스만남_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[101,102])
        self.spawn_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='MeetAnos')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
