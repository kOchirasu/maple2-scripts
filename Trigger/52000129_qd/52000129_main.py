""" trigger/52000129_qd/52000129_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103])
        self.spawn_monster(spawn_ids=[104])
        self.set_effect(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002691], quest_states=[1]):
            return 퀘스트진행_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002691], quest_states=[2]):
            return 퀘스트완료가능_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002691], quest_states=[3]):
            return 페이드아웃_01(self.ctx)
        if self.user_detected(box_ids=[701]):
            return 잠시대기(self.ctx)


class 잠시대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라이동_01(self.ctx)


class 카메라이동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 카메라이동_02(self.ctx)


class 카메라이동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000129_QD__52000129_MAIN__0$', desc='$52000129_QD__52000129_MAIN__1$', align=Align.Bottom | Align.Left, duration=4000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 카메라리셋_01(self.ctx)


class 카메라리셋_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 계단타고이동_01(self.ctx)


class 계단타고이동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=25201291, text_id=25201291)
        self.set_effect(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return 퀘스트받기_01(self.ctx)


class 퀘스트받기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201291)
        self.set_effect(trigger_ids=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011])
        self.show_guide_summary(entity_id=25201292, text_id=25201292)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002691], quest_states=[1]):
            return 퀘스트진행_01(self.ctx)


class 퀘스트진행_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201291)
        self.hide_guide_summary(entity_id=25201292)
        self.show_guide_summary(entity_id=25201293, text_id=25201293)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002691], quest_states=[2]):
            return 퀘스트완료가능_01(self.ctx)


class 퀘스트완료가능_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201291)
        self.hide_guide_summary(entity_id=25201292)
        self.hide_guide_summary(entity_id=25201293)
        self.show_guide_summary(entity_id=25201294, text_id=25201294)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[40002691], quest_states=[3]):
            return 페이드아웃_01(self.ctx)


class 페이드아웃_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entity_id=25201291)
        self.hide_guide_summary(entity_id=25201292)
        self.hide_guide_summary(entity_id=25201293)
        self.hide_guide_summary(entity_id=25201294)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 페이드아웃_02(self.ctx)


class 페이드아웃_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000129, portal_id=99)
        self.spawn_monster(spawn_ids=[105])
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 페이드인_01(self.ctx)


class 페이드인_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMaskEff_fadein_1sec.xml')
        self.set_pc_emotion_sequence(sequence_names=['Talk_A'])
        self.set_scene_skip(state=마무리, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 감시_01(self.ctx)


class 감시_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Talk_A'])
        self.set_dialogue(type=1, spawn_id=101, script='$52000129_QD__52000129_MAIN__2$', time=2)
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 감시_02(self.ctx)


class 감시_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002,8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 감시_03(self.ctx)


class 감시_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2002')
        self.set_dialogue(type=1, spawn_id=102, script='$52000129_QD__52000129_MAIN__3$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000130, portal_id=1)


initial_state = 준비
