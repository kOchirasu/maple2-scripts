""" trigger/52000055_qd/darkwindmovie.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 카트반
        self.spawn_monster(spawn_ids=[104], auto_target=False) # 다크윈드 에반
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 다크윈드 대원
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 다크윈드 대원
        self.spawn_monster(spawn_ids=[202], auto_target=False) # 다크윈드 대원
        self.spawn_monster(spawn_ids=[203], auto_target=False) # 다크윈드 대원
        self.spawn_monster(spawn_ids=[204], auto_target=False) # 다크윈드 대원
        self.spawn_monster(spawn_ids=[205], auto_target=False) # 다크윈드 대원

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100235], quest_states=[1]):
            return start(self.ctx)


# [10001393 커닝시티 시가전 ] 완료 시
class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=6002)
        self.set_onetime_effect(id=11100101, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_ComputerRoom_01.xml')
        self.move_user(map_id=52000055, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return CameraEffect01(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera(trigger_id=101)
        self.move_user_path(patrol_name='MS2PatrolData_PC')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Katvan') # 카트반 이동
        self.set_scene_skip(state=Quit, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect4(self.ctx)


class CameraEffect4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return CameraEffect5(self.ctx)


class CameraEffect5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 페이드 아웃

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraEffect6(self.ctx)


class CameraEffect6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 페이드 인
        self.select_camera(trigger_id=103)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect7(self.ctx)


class CameraEffect7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7500):
            return CameraEffect8(self.ctx)


class CameraEffect8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[119,120])
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraEffect9(self.ctx)


class CameraEffect9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=11100102, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_SystemWarningAlarm_01.xml')
        self.set_onetime_effect(id=2100267, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_ComputerSignal_01.xml')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=100, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_AI_00001876.xml')
        self.set_dialogue(type=2, spawn_id=11001896, script='$52000055_QD__DARKWINDMOVIE__0$', time=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return CityWarfareTalk2(self.ctx)


class CityWarfareTalk2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=11100102, path='BG/Common/Sound/Eff_Object_CityWar_SystemWarningAlarm_01.xml')
        self.select_camera_path(path_ids=[106,128]) # 카트반 캠

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk3(self.ctx)


class CityWarfareTalk3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001878.xml')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000055_QD__DARKWINDMOVIE__1$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return CityWarfareTalk4(self.ctx)


class CityWarfareTalk4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.select_camera_path(path_ids=[105,127]) # 대원 캠

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk5(self.ctx)


class CityWarfareTalk5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3500148, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_KeyboardTyping_01.xml')
        self.set_dialogue(type=2, spawn_id=11000259, script='$52000055_QD__DARKWINDMOVIE__2$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return CityWarfareTalk6(self.ctx)


class CityWarfareTalk6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.select_camera_path(path_ids=[107,129]) # 대원 캠

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk7(self.ctx)


class CityWarfareTalk7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000259, script='$52000055_QD__DARKWINDMOVIE__3$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return CityWarfareTalk8(self.ctx)


class CityWarfareTalk8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.select_camera_path(path_ids=[109,110,111])

    def on_tick(self) -> trigger_api.Trigger:
        return CameraEffect109(self.ctx)


class CameraEffect109(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=11100103, enable=True, path='BG/Common/Sound/Eff_Object_CityWar_SystemErrorAlarm_01.xml')
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_AI_00001877.xml')
        self.set_dialogue(type=2, spawn_id=11001896, script='$52000055_QD__DARKWINDMOVIE__4$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return CityWarfareTalk10(self.ctx)


class CityWarfareTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=11100103, path='BG/Common/Sound/Eff_Object_CityWar_SystemErrorAlarm_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk11(self.ctx)


class CityWarfareTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=105) # 대원 캠
        self.set_dialogue(type=2, spawn_id=11000259, script='$52000055_QD__DARKWINDMOVIE__5$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk12(self.ctx)


class CityWarfareTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CameraEffect13(self.ctx)


class CameraEffect13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=112)
        self.select_camera_path(path_ids=[112,113]) # 카트반 캠
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001879.xml')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000055_QD__DARKWINDMOVIE__6$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return CityWarfareTalk14(self.ctx)


class CityWarfareTalk14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk15(self.ctx)


class CityWarfareTalk15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=114)
        self.select_camera_path(path_ids=[114,115])
        self.set_dialogue(type=2, spawn_id=11000259, script='$52000055_QD__DARKWINDMOVIE__7$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk16(self.ctx)


class CityWarfareTalk16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk17(self.ctx)


class CityWarfareTalk17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000215, script='$52000055_QD__DARKWINDMOVIE__8$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return CityWarfareTalk18(self.ctx)


class CityWarfareTalk18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.select_camera_path(path_ids=[117,118])

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk19(self.ctx)


class CityWarfareTalk19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=104, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001880.xml')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000055_QD__DARKWINDMOVIE__9$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return CityWarfareTalk20(self.ctx)


class CityWarfareTalk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=115, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001964.xml')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000055_QD__DARKWINDMOVIE__10$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CityWarfareTalk20b(self.ctx)


class CityWarfareTalk20b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk21(self.ctx)


class CityWarfareTalk21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=118)
        self.select_camera_path(path_ids=[121,122]) # 카트반 캠

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CityWarfareTalk22(self.ctx)


class CityWarfareTalk22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk23(self.ctx)


class CityWarfareTalk23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=105, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001881.xml')
        self.select_camera(trigger_id=122) # 카트반 캠
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000055_QD__DARKWINDMOVIE__11$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk24(self.ctx)


class CityWarfareTalk24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk25(self.ctx)


class CityWarfareTalk25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[125,126]) # 대원 캠
        self.set_dialogue(type=2, spawn_id=11000215, script='$52000055_QD__DARKWINDMOVIE__12$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk26(self.ctx)


class CityWarfareTalk26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk27(self.ctx)


class CityWarfareTalk27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=106, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001882.xml')
        self.select_camera_path(path_ids=[123,124]) # 카트반 캠
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000055_QD__DARKWINDMOVIE__13$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk28(self.ctx)


class CityWarfareTalk28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk29(self.ctx)


class CityWarfareTalk29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=6002, visible=True, enable=True, minimap_visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.move_user(map_id=52000067, portal_id=1)


initial_state = Ready
