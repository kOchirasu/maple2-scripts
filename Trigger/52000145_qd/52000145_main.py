""" trigger/52000145_qd/52000145_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002711], quest_states=[3]):
            return 퀘스트2완료_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002711], quest_states=[2]):
            return 퀘스트2진행_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002711], quest_states=[1]):
            return 퀘스트2시작_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002710], quest_states=[3]):
            return 퀘스트1완료가능_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002710], quest_states=[2]):
            return 퀘스트1진행_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002710], quest_states=[1]):
            return 퀘스트1수락_02(self.ctx)
        if self.user_detected(box_ids=[701]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 영상재생_01(self.ctx)


class 영상재생_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='common\\JobIntro_Ranger.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 독백_01(self.ctx)
        if self.wait_tick(wait_tick=45000):
            return 독백_01(self.ctx)


class 독백_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000145_QD__52000145_MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작_01(self.ctx)


class 시작_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # self.set_cinematic_ui(type=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시작_02(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=2)


class 시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000145, portal_id=99)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 하스터숙면_01(self.ctx)


class 하스터숙면_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000145_QD__52000145_MAIN__1$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 하스터숙면_02(self.ctx)


class 하스터숙면_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000145_QD__52000145_MAIN__2$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 하스터숙면_03(self.ctx)


class 하스터숙면_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 하스터숙면_04(self.ctx)


class 하스터숙면_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=퀘스트1수락_01, action='nextState')
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000145_QD__52000145_MAIN__3$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 하스터숙면_05(self.ctx)


class 하스터숙면_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003189, msg='$52000145_QD__52000145_MAIN__4$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 하스터숙면_06(self.ctx)


class 하스터숙면_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(emotion_name='Think_A')
        self.add_cinematic_talk(npc_id=0, msg='$52000145_QD__52000145_MAIN__5$', duration=3000, align=Align.Right)
        # self.add_cinematic_talk(npc_id=0, msg='$52000145_QD__52000145_MAIN__6$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 퀘스트1수락_01(self.ctx)


class 퀘스트1수락_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 퀘스트1수락_02(self.ctx)


class 퀘스트1수락_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=25201456, text_id=25201456)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701,702], quest_ids=[40002710], quest_states=[1]):
            return 퀘스트1진행_00(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25201456)


class 퀘스트1진행_00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트1진행_01(self.ctx)


class 퀘스트1진행_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25201451, text_id=25201451)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701,702], quest_ids=[40002710], quest_states=[2]):
            return 퀘스트1완료가능_00(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25201451)


class 퀘스트1완료가능_00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트1완료가능_01(self.ctx)


class 퀘스트1완료가능_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25201452, text_id=25201452)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701,702], quest_ids=[40002710], quest_states=[3]):
            return 퀘스트1완료_01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25201452)


class 퀘스트1완료_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트2시작_01(self.ctx)


class 퀘스트2시작_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25201453, text_id=25201453)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701,702], quest_ids=[40002711], quest_states=[1]):
            return 퀘스트2진행_00(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25201453)


class 퀘스트2진행_00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트2진행_01(self.ctx)


class 퀘스트2진행_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25201454, text_id=25201454)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701,703], quest_ids=[40002711], quest_states=[2]):
            return 퀘스트2완료가능_00(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25201454)


class 퀘스트2완료가능_00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트2완료가능_01(self.ctx)


class 퀘스트2완료가능_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25201455, text_id=25201455)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701,702], quest_ids=[40002711], quest_states=[3]):
            return 퀘스트2완료_01(self.ctx)


class 퀘스트2완료_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25201455)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트2완료_02(self.ctx)


class 퀘스트2완료_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.move_user(map_id=52000145, portal_id=99)
        self.spawn_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 오스칼등장_01(self.ctx)


class 오스칼등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Troubled_A'])
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 오스칼등장_02(self.ctx)


class 오스칼등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Suprise_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 오스칼등장_03(self.ctx)


class 오스칼등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=마무리, action='exit')
        self.face_emotion(emotion_name='Think_A')
        self.add_cinematic_talk(npc_id=0, msg='$52000145_QD__52000145_MAIN__7$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오스칼등장_04(self.ctx)


class 오스칼등장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003189, msg='$52000145_QD__52000145_MAIN__8$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오스칼등장_05(self.ctx)


class 오스칼등장_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000145_QD__52000145_MAIN__9$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=0, msg='$52000145_QD__52000145_MAIN__10$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 오스칼등장_06(self.ctx)


class 오스칼등장_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003189, msg='$52000145_QD__52000145_MAIN__11$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5485):
            return 오스칼등장_07(self.ctx)


class 오스칼등장_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 오스칼등장_08(self.ctx)


class 오스칼등장_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000145_QD__52000145_MAIN__12$', duration=3000, align=Align.Left)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Sit_Down_A', duration=70000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 오스칼등장_08_1(self.ctx)


class 오스칼등장_08_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003189, msg='$52000145_QD__52000145_MAIN__13$', duration=2500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 오스칼등장_09(self.ctx)


class 오스칼등장_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 오스칼등장_10(self.ctx)


class 오스칼등장_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003189, msg='$52000145_QD__52000145_MAIN__14$', duration=4000, illust_id='Hastur_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 오스칼등장_11(self.ctx)


class 오스칼등장_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000145_QD__52000145_MAIN__15$', duration=3000, illust_id='Oskhal_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 오스칼등장_12(self.ctx)


class 오스칼등장_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003189, msg='$52000145_QD__52000145_MAIN__16$', duration=3500, illust_id='Hastur_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 오스칼등장_13(self.ctx)


class 오스칼등장_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000145_QD__52000145_MAIN__17$', duration=2500, illust_id='Oskhal_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003380, msg='$52000145_QD__52000145_MAIN__18$', duration=3500, illust_id='Oskhal_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003380, msg='$52000145_QD__52000145_MAIN__19$', duration=3000, illust_id='Oskhal_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9500):
            return 오스칼등장_14(self.ctx)


class 오스칼등장_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003189, msg='$52000145_QD__52000145_MAIN__20$', duration=3000, illust_id='Hastur_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 오스칼등장_15(self.ctx)


class 오스칼등장_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000145_QD__52000145_MAIN__21$', duration=3500, illust_id='Oskhal_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5172):
            return 오스칼등장_16(self.ctx)


class 오스칼등장_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003189, msg='$52000145_QD__52000145_MAIN__22$', duration=3000, illust_id='Hastur_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 오스칼등장_17(self.ctx)


class 오스칼등장_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000145_QD__52000145_MAIN__23$', duration=2500, illust_id='Oskhal_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003380, msg='$52000145_QD__52000145_MAIN__24$', duration=3500, illust_id='Oskhal_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003380, msg='$52000145_QD__52000145_MAIN__25$', duration=2500, illust_id='Oskhal_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9742):
            return 오스칼등장_18(self.ctx)


class 오스칼등장_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003189, msg='$52000145_QD__52000145_MAIN__26$', duration=3000, illust_id='Hastur_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 오스칼등장_19(self.ctx)


class 오스칼등장_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003380, msg='$52000145_QD__52000145_MAIN__27$', duration=3000, illust_id='Oskhal_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3631):
            return 오스칼등장_20(self.ctx)


class 오스칼등장_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003189, msg='$52000145_QD__52000145_MAIN__28$', duration=3500, illust_id='Hastur_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 오스칼등장_21(self.ctx)


class 오스칼등장_21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion()
        self.add_cinematic_talk(npc_id=0, msg='$52000145_QD__52000145_MAIN__29$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000146, portal_id=1)


initial_state = 준비
