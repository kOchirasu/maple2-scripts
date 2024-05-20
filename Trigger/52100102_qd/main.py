""" trigger/52100102_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1000]):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50100890], quest_states=[3]):
            return NPC소환(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50100890], quest_states=[2]):
            return 연출끝(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50100890], quest_states=[1]):
            return 연출끝(self.ctx)


class NPC소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.spawn_monster(spawn_ids=[100], auto_target=False)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[200], auto_target=False)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.spawn_monster(spawn_ids=[203], auto_target=False)
        self.spawn_monster(spawn_ids=[204], auto_target=False)
        self.spawn_monster(spawn_ids=[205], auto_target=False)
        self.spawn_monster(spawn_ids=[206], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1000]):
            return narration01(self.ctx)


class narration01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=9, script='$52100102_QD__MAIN__0$')
        self.set_scene_skip(state=연출끝, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return narration02(self.ctx)


class narration02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[1,2], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52100102_QD__MAIN__1$', desc='$52100102_QD__MAIN__2$', align=Align.Bottom | Align.Left, duration=3000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 암전1(self.ctx)


class 암전1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 카메라무브1(self.ctx)


class 카메라무브1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3,4], return_view=False)
        self.move_npc(spawn_id=202, patrol_name='PatrolData_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 위협1(self.ctx)


class 위협1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8)
        self.add_cinematic_talk(npc_id=11004429, msg='$52100102_QD__MAIN__3$', duration=3000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11004429, msg='$52100102_QD__MAIN__4$', duration=4000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Bore_A', duration=1333.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 위협2(self.ctx)


class 위협2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=301, sequence_name='Bore_B', duration=3667.0)
        self.add_cinematic_talk(npc_id=11004426, msg='$52100102_QD__MAIN__5$', duration=4000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카등장(self.ctx)


class 투르카등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[6,7,9], return_view=False)
        self.set_effect(trigger_ids=[600], visible=True)
        self.spawn_monster(spawn_ids=[300], auto_target=False)
        self.add_cinematic_talk(npc_id=11004430, msg='$52100102_QD__MAIN__6$', duration=3000, align=Align.Left)
        self.move_npc(spawn_id=300, patrol_name='PatrolData_Turka_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카대사소개(self.ctx)


class 투르카대사소개(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.show_caption(type='VerticalCaption', title='$52100102_QD__MAIN__7$', desc='$52100102_QD__MAIN__8$', align=Align.Bottom | Align.Left, duration=3000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카대사1(self.ctx)


class 투르카대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=300, sequence_name='Bore_A', duration=5400.0)
        self.add_cinematic_talk(npc_id=11004430, msg='$52100102_QD__MAIN__9$', duration=5000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 검은군단물러서기_1(self.ctx)


class 검은군단물러서기_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])
        self.select_camera(trigger_id=10)
        self.set_npc_rotation(spawn_id=202, rotation=180.0)
        self.add_cinematic_talk(npc_id=11004429, msg='$52100102_QD__MAIN__10$', duration=2000, align=Align.Left)
        self.set_npc_rotation(spawn_id=200, rotation=225.0)
        self.set_npc_rotation(spawn_id=201, rotation=180.0)
        self.set_npc_rotation(spawn_id=205, rotation=225.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 검은군단돌아보기_1(self.ctx)


class 검은군단돌아보기_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=203, rotation=180.0)
        self.set_npc_rotation(spawn_id=204, rotation=135.0)
        self.set_npc_rotation(spawn_id=206, rotation=135.0)
        self.add_cinematic_talk(npc_id=11004430, msg='$52100102_QD__MAIN__11$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 검은군단물러서기_2(self.ctx)


class 검은군단물러서기_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=300, patrol_name='PatrolData_Turka_2')
        self.move_npc(spawn_id=201, patrol_name='PatrolData_back_201')
        self.move_npc(spawn_id=202, patrol_name='PatrolData_back_202')
        self.move_npc(spawn_id=205, patrol_name='PatrolData_back_205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 검은군단물러서기_3(self.ctx)


class 검은군단물러서기_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=200, patrol_name='PatrolData_back_200')
        self.move_npc(spawn_id=204, patrol_name='PatrolData_Back_204')
        self.move_npc(spawn_id=206, patrol_name='PatrolData_back_206')
        self.move_npc(spawn_id=203, patrol_name='PatrolData_back_203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 검은군단소멸시키기(self.ctx)


class 검은군단소멸시키기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[200])
        self.destroy_monster(spawn_ids=[201])
        self.destroy_monster(spawn_ids=[202])
        self.destroy_monster(spawn_ids=[203])
        self.destroy_monster(spawn_ids=[204])
        self.destroy_monster(spawn_ids=[205])
        self.destroy_monster(spawn_ids=[206])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 카메라전환_1(self.ctx)


class 카메라전환_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[300])
        self.spawn_monster(spawn_ids=[301], auto_target=False)
        self.select_camera(trigger_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 투르카이동_1(self.ctx)


class 투르카이동_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=301, patrol_name='PatrolData_Turka_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 게오르크장교대사(self.ctx)


class 게오르크장교대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004426, msg='$52100102_QD__MAIN__12$', duration=5000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 투르카공격1To1(self.ctx)


class 투르카공격1To1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004430, msg='$52100102_QD__MAIN__13$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=301, sequence_name='Bore_B', duration=3667.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카공격1To2(self.ctx)


class 투르카공격1To2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=301, patrol_name='PatrolData_Turka_Attack')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 투르카공격1To3(self.ctx)


class 투르카공격1To3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=301, sequence_name='Attack_01_B', duration=600.0)
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=600):
            return 투르카공격1To4(self.ctx)


class 투르카공격1To4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[11,12], return_view=False)
        self.set_npc_emotion_loop(spawn_id=301, sequence_name='Attack_02_B', duration=1400.0)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Dead_A', duration=1333.0)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Dead_A', duration=1333.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 투르카공격카메라(self.ctx)


class 투르카공격카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[103])
        self.add_cinematic_talk(npc_id=11004425, msg='$52100102_QD__MAIN__14$', duration=1000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 투르카질문_1(self.ctx)


class 투르카질문_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[107])
        self.spawn_monster(spawn_ids=[108])
        self.select_camera(trigger_id=13)
        self.add_cinematic_talk(npc_id=11004426, msg='$52100102_QD__MAIN__15$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 투르카질문_2To1(self.ctx)


class 투르카질문_2To1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=301, sequence_name='Bore_B', duration=3667.0)
        self.add_cinematic_talk(npc_id=11004430, msg='$52100102_QD__MAIN__16$', duration=5000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11004426, msg='$52100102_QD__MAIN__17$', duration=3000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11004430, msg='$52100102_QD__MAIN__18$', duration=5000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 투르카공격2To1(self.ctx)


class 투르카공격2To1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=301, sequence_name='Attack_01_B', duration=600.0)
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=600):
            return 투르카공격2To2(self.ctx)


class 투르카공격2To2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=100, enable=True, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        self.select_camera(trigger_id=14)
        self.set_time_scale(enable=True, start_scale=0.3, end_scale=1.0, duration=30.0, interpolator=1)
        self.set_npc_emotion_loop(spawn_id=301, sequence_name='Attack_02_B', duration=1400.0)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Dead_A', duration=1333.0)
        self.add_cinematic_talk(npc_id=11004426, msg='$52100102_QD__MAIN__19$', duration=1500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 상황정리(self.ctx)


class 상황정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(start_scale=0.3, end_scale=1.0, duration=50.0, interpolator=1)
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[107])
        self.destroy_monster(spawn_ids=[108])
        self.spawn_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[110])
        self.spawn_monster(spawn_ids=[111])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 엔딩카메라1(self.ctx)


class 엔딩카메라1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[301])
        self.spawn_monster(spawn_ids=[302])
        self.set_onetime_effect(id=100, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        self.select_camera_path(path_ids=[15,16], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 투르카엔딩대사_1(self.ctx)


class 투르카엔딩대사_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=17)
        self.move_npc(spawn_id=302, patrol_name='PatrolData_Turka_End_Move')
        self.set_effect(trigger_ids=[604], visible=True)
        self.add_cinematic_talk(npc_id=11004430, msg='$52100102_QD__MAIN__20$', duration=5000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 엔딩암전(self.ctx)


class 엔딩암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1], arg2=False)
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.visible_my_pc(is_visible=True)
        self.set_onetime_effect(id=101, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=2020029, portal_id=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: State


initial_state = Ready
