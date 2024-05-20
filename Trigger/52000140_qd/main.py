""" trigger/52000140_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[5001])
        self.set_cinematic_ui(type=0) # 유저 이동 하게
        self.set_cinematic_ui(type=2) # UI 숨기기 초기화
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return 카메라연출_01(self.ctx)


class 카메라연출_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.set_cinematic_ui(type=1) # 유저 이동 못 하게
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라연출_02(self.ctx)


class 카메라연출_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라연출_04(self.ctx)


"""
class 카메라연출_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라연출_04(self.ctx)
"""

class 카메라연출_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 카메라연출_05(self.ctx)


class 카메라연출_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8002], return_view=False)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 삼자대화_01(self.ctx)

    def on_exit(self) -> None:
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2002')


class 삼자대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=투르카소멸_01, action='nextState')
        self.add_cinematic_talk(npc_id=0, msg='$52000140_QD__MAIN__0$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 삼자대화_02(self.ctx)


class 삼자대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000140_QD__MAIN__1$', duration=3000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 삼자대화_03(self.ctx)


class 삼자대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003329, msg='$52000140_QD__MAIN__2$', duration=2500, align=Align.Right)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2003')
        self.add_cinematic_talk(npc_id=11003329, msg='$52000140_QD__MAIN__3$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5300):
            return 투르카소멸_01(self.ctx)


class 투르카소멸_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_effect(trigger_ids=[5001], visible=True)
        self.destroy_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 투르카소멸_02(self.ctx)


class 투르카소멸_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=2) # UI 숨기기 초기화
        self.set_cinematic_ui(type=0) # 유저 이동 가능하게
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[105])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 어둠의졸개_01(self.ctx)


class 어둠의졸개_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103,104])
        self.show_guide_summary(entity_id=25201401, text_id=25201401)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103,104]):
            return 졸개퇴치완료_01(self.ctx)


class 졸개퇴치완료_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entity_id=25201401)
        self.set_cinematic_ui(type=1) # 유저 이동 못하게
        self.set_cinematic_ui(type=3) # 상하 레터박스

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 졸개퇴치완료_02(self.ctx)


class 졸개퇴치완료_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000140, portal_id=99)
        self.destroy_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2002')
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 졸개퇴치완료_03(self.ctx)


class 졸개퇴치완료_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 알론과대화_01(self.ctx)


class 알론과대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=투르카와전투_01, action='nextState')
        self.add_cinematic_talk(npc_id=0, msg='$52000140_QD__MAIN__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 알론과대화_02(self.ctx)


class 알론과대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000140_QD__MAIN__5$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 알론과대화_03(self.ctx)


class 알론과대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000140_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 알론과대화_04(self.ctx)


class 알론과대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000140_QD__MAIN__7$', duration=2500, align=Align.Right)
        self.add_cinematic_talk(npc_id=11003328, msg='$52000140_QD__MAIN__8$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5300):
            return 알론과대화_05(self.ctx)


class 알론과대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000140_QD__MAIN__9$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 알론과대화_06(self.ctx)

    def on_exit(self) -> None:
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2003')


class 알론과대화_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000140_QD__MAIN__10$', duration=2000, align=Align.Right)
        self.move_user_path(patrol_name='MS2PatrolData_2008')
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2300):
            return 알론과대화_07(self.ctx)


class 알론과대화_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003,8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2200):
            return 차삼자대화_01_2(self.ctx)


class 차삼자대화_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003329, msg='$52000140_QD__MAIN__11$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차삼자대화_02_2(self.ctx)


class 차삼자대화_02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000140_QD__MAIN__12$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차삼자대화_03_2(self.ctx)


class 차삼자대화_03_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003329, msg='$52000140_QD__MAIN__13$', duration=2500, align=Align.Right)
        self.add_cinematic_talk(npc_id=11003329, msg='$52000140_QD__MAIN__14$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5200):
            return 차삼자대화_04_2(self.ctx)


class 차삼자대화_04_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000140_QD__MAIN__15$', duration=2500, align=Align.Center)
        self.add_cinematic_talk(npc_id=11003328, msg='$52000140_QD__MAIN__16$', duration=2500, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5200):
            return 차삼자대화_05_2(self.ctx)


class 차삼자대화_05_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003329, msg='$52000140_QD__MAIN__17$', duration=2500, align=Align.Right)
        self.add_cinematic_talk(npc_id=11003329, msg='$52000140_QD__MAIN__18$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5300):
            return 차삼자대화_06_2(self.ctx)


class 차삼자대화_06_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000140_QD__MAIN__19$', duration=2500, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차삼자대화_07_2(self.ctx)


class 차삼자대화_07_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003329, msg='$52000140_QD__MAIN__20$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차삼자대화_08_2(self.ctx)


class 차삼자대화_08_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003328, msg='$52000140_QD__MAIN__21$', duration=2000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2300):
            return 투르카와전투_01(self.ctx)


class 투르카와전투_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0) # 유저 이동 가능하게
        self.set_cinematic_ui(type=2) # UI 숨기기 초기화
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[106])
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[105])
        self.show_guide_summary(entity_id=25201402, text_id=25201402)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 투르카와전투_02(self.ctx)


class 투르카와전투_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.hide_guide_summary(entity_id=25201402)
        self.move_user(map_id=52000140, portal_id=99)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카와전투_03(self.ctx)


class 투르카와전투_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.destroy_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.destroy_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.move_user_path(patrol_name='MS2PatrolData_2008')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차삼자대화_01_3(self.ctx)


class 차삼자대화_01_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003329, msg='$52000140_QD__MAIN__22$', duration=2500, align=Align.Right)
        self.add_cinematic_talk(npc_id=11003329, msg='$52000140_QD__MAIN__23$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5300):
            return 차삼자대화_02_3(self.ctx)


class 차삼자대화_02_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000140_QD__MAIN__24$', duration=2000)
        self.move_user_path(patrol_name='MS2PatrolData_2005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2200):
            return 차삼자대화_03_3(self.ctx)


class 차삼자대화_03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)
        self.add_cinematic_talk(npc_id=11003328, msg='$52000140_QD__MAIN__25$', duration=2000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2200):
            return 투르카퇴장_01(self.ctx)


class 투르카퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007], return_view=False)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.destroy_monster(spawn_ids=[102])
        # self.set_pc_emotion_sequence(sequence_names=['Priest_Sanctuary_A'])
        self.set_pc_emotion_sequence(sequence_names=['Priest_Skill_Divine_Protection_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return 투르카퇴장_02(self.ctx)


class 투르카퇴장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=10000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC의부상_01(self.ctx)


class PC의부상_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=10000.0)
        self.set_effect(trigger_ids=[5001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC의부상_02(self.ctx)


class PC의부상_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8004,8005], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PC의부상_03(self.ctx)


class PC의부상_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000141, portal_id=1)


initial_state = 준비
