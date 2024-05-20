""" trigger/52000097_qd/main.xml """
import trigger_api


"""
class test(trigger_api.Trigger):
    pass
"""

class main(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000097, portal_id=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[101,102,201], auto_target=False) # 배우 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[8001,8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003,8004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003084, script='$52000097_QD__MAIN__0$', time=5)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8005], return_view=False)
        self.select_camera_path(path_ids=[8006], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003085, script='$52000097_QD__MAIN__1$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003086, script='$52000097_QD__MAIN__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003086, script='$52000097_QD__MAIN__3$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Talk_A'])
        self.set_dialogue(type=1, script='$52000097_QD__MAIN__4$', time=3)
        self.set_dialogue(type=1, script='$52000097_QD__MAIN__5$', time=3, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8008], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003086, script='$52000097_QD__MAIN__6$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003086, script='$52000097_QD__MAIN__7$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_09(self.ctx)


class scene_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000097_QD__MAIN__8$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_10(self.ctx)


class scene_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003086, script='$52000097_QD__MAIN__9$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return scene_11(self.ctx)


class scene_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Attack_01_E')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_12_ready(self.ctx)


class scene_12_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8009], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Failure_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_12(self.ctx)


class scene_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='ProphecyofFall.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return scene_13(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


class scene_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2002')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2001')
        self.set_dialogue(type=1, spawn_id=102, script='$52000097_QD__MAIN__10$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=101, script='$52000097_QD__MAIN__11$', time=2)
        self.select_camera_path(path_ids=[8008], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Failure_Idle_A'])
        self.set_dialogue(type=2, spawn_id=11003086, script='$52000097_QD__MAIN__12$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_14(self.ctx)


class scene_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.set_dialogue(type=1, script='$52000097_QD__MAIN__13$', time=3, arg5=1)
        self.move_user_path(patrol_name='MS2PatrolData_2003')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_15(self.ctx)


class scene_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Talk_A'])
        self.set_dialogue(type=1, script='$52000097_QD__MAIN__14$', time=4)
        self.set_dialogue(type=1, script='$52000097_QD__MAIN__15$', time=4, arg5=4)
        self.set_dialogue(type=1, script='$52000097_QD__MAIN__16$', time=4, arg5=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return scene_16(self.ctx)


class scene_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003086, script='$52000097_QD__MAIN__17$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_17(self.ctx)


class scene_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003086, script='$52000097_QD__MAIN__18$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_18(self.ctx)


class scene_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003086, script='$52000097_QD__MAIN__19$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_19(self.ctx)


class scene_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_20(self.ctx)


class scene_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8011], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2006')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_21(self.ctx)


class scene_21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])
        self.set_dialogue(type=2, spawn_id=11003085, script='$52000097_QD__MAIN__20$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_22(self.ctx)


class scene_22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003084, script='$52000097_QD__MAIN__21$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_23(self.ctx)


class scene_23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2008')
        self.move_user_path(patrol_name='MS2PatrolData_2009')
        self.set_dialogue(type=2, spawn_id=11003084, script='$52000097_QD__MAIN__22$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_24(self.ctx)


class scene_24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003085, script='$52000097_QD__MAIN__23$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_25(self.ctx)


class scene_25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000097_QD__MAIN__24$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scene_26(self.ctx)


class scene_26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # self.set_achievement(trigger_id=701, type='trigger', achieve='meetalbanos')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000068, portal_id=1)


initial_state = test
