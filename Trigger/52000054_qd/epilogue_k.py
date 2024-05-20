""" trigger/52000054_qd/epilogue_k.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50001745], quest_states=[3]):
            # 챕터8 에필로그 [10002274 끝이 아닌 끝] 완료 시
            return CameraEffect0(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50001745], quest_states=[2]):
            return ReturnMapReady0(self.ctx)


class ReturnMapReady0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ReturnMapReady(self.ctx)


class ReturnMapReady(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=9, script='$52000054_QD__EPILOGUE_K__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ReturnMap(self.ctx)


class ReturnMap(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000025, portal_id=2)


class CameraEffect0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Quit, action='exit')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[1000], auto_target=False) # 카트반

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraEffect1(self.ctx)


class CameraEffect1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[100,101], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return CameraEffect2(self.ctx)


class CameraEffect2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml') # 페이드 끈다

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CityWarfareTalk1(self.ctx)


class CityWarfareTalk1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=11100105, enable=True, path='BG/Common/Sound/Eff_AMB_BlackMoon_Abyss_01.xml') # 어둠의 회랑 환경음
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml') # 페이드 끈다
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[200], return_view=False)
        self.set_onetime_effect(id=1883, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001883.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__1$', time=7)
        self.set_skip(state=CityWarfareTalk2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return CityWarfareTalk2(self.ctx)


class CityWarfareTalk2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk3(self.ctx)


class CityWarfareTalk3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1884, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001884.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__2$', time=5)
        self.set_skip(state=CityWarfareTalk4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk4(self.ctx)


class CityWarfareTalk4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk5(self.ctx)


class CityWarfareTalk5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2000], auto_target=False) # 투르카
        self.move_npc(spawn_id=2000, patrol_name='MS2PatrolData_Turka') # 투르카 이동
        self.select_camera_path(path_ids=[300,301], return_view=False)
        self.set_onetime_effect(id=1943, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001943.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__3$', time=11)
        self.set_skip(state=CityWarfareTalk6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return CityWarfareTalk6(self.ctx)


class CityWarfareTalk6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk7(self.ctx)


class CityWarfareTalk7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[202], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=1000, sequence_name='Sit_Down_HeadUP')
        self.set_onetime_effect(id=1885, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001885.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__4$', time=5)
        self.set_skip(state=CityWarfareTalk8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk8(self.ctx)


class CityWarfareTalk8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk9(self.ctx)


class CityWarfareTalk9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1886, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001886.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__5$', time=5)
        self.set_skip(state=CityWarfareTalk10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk10(self.ctx)


class CityWarfareTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk11(self.ctx)


class CityWarfareTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[400,401], return_view=False)
        self.set_onetime_effect(id=1944, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001944.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__6$', time=13)
        self.set_skip(state=CityWarfareTalk12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return CityWarfareTalk12(self.ctx)


class CityWarfareTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk13(self.ctx)


class CityWarfareTalk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1945, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001945.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__7$', time=8)
        self.set_skip(state=CityWarfareTalk14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return CityWarfareTalk14(self.ctx)


class CityWarfareTalk14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk15(self.ctx)


class CityWarfareTalk15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[204,205], return_view=False)
        self.set_onetime_effect(id=1887, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001887.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__8$', time=5)
        self.set_skip(state=CityWarfareTalk16)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk16(self.ctx)


class CityWarfareTalk16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk17(self.ctx)


class CityWarfareTalk17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[402], return_view=False)
        self.set_onetime_effect(id=1946, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001946.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__9$', time=12)
        self.set_skip(state=CityWarfareTalk18)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return CityWarfareTalk18(self.ctx)


class CityWarfareTalk18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk19(self.ctx)


class CityWarfareTalk19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[204], return_view=False)
        self.set_onetime_effect(id=1888, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001888.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__10$', time=5)
        self.set_skip(state=CityWarfareTalk20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk20(self.ctx)


class CityWarfareTalk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk21(self.ctx)


class CityWarfareTalk21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[500,501], return_view=False)
        self.set_onetime_effect(id=1947, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001947.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__11$', time=10)
        self.set_skip(state=CityWarfareTalk22)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return CityWarfareTalk22(self.ctx)


class CityWarfareTalk22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk23(self.ctx)


class CityWarfareTalk23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[200], return_view=False)
        self.set_onetime_effect(id=1889, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001889.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__12$', time=5)
        self.set_skip(state=CityWarfareTalk24)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk24(self.ctx)


class CityWarfareTalk24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk25(self.ctx)


class CityWarfareTalk25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[403], return_view=False)
        self.set_onetime_effect(id=1948, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001948.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__13$', time=8)
        self.set_skip(state=CityWarfareTalk26)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return CityWarfareTalk26(self.ctx)


class CityWarfareTalk26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk27(self.ctx)


class CityWarfareTalk27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__14$', time=5)
        self.set_skip(state=CityWarfareTalk28)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk28(self.ctx)


class CityWarfareTalk28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk29(self.ctx)


class CityWarfareTalk29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[200], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__29$', time=5)
        self.set_skip(state=CityWarfareTalk30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk30(self.ctx)


class CityWarfareTalk30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk31(self.ctx)


class CityWarfareTalk31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[404], return_view=False)
        self.set_onetime_effect(id=1949, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001949.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__15$', time=11)
        self.set_skip(state=CityWarfareTalk32)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return CityWarfareTalk32(self.ctx)


class CityWarfareTalk32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk33(self.ctx)


class CityWarfareTalk33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[408,409], return_view=False)
        self.set_onetime_effect(id=1950, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001950.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__16$', time=8)
        self.set_skip(state=CityWarfareTalk34)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return CityWarfareTalk34(self.ctx)


class CityWarfareTalk34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk35(self.ctx)


class CityWarfareTalk35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1890, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001890.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__17$', time=5)
        self.set_skip(state=CityWarfareTalk36)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk36(self.ctx)


class CityWarfareTalk36(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk37(self.ctx)


class CityWarfareTalk37(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[502,503], return_view=False)
        self.set_onetime_effect(id=1951, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001951.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__18$', time=7)
        self.set_skip(state=CityWarfareTalk38)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return CityWarfareTalk38(self.ctx)


class CityWarfareTalk38(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk39(self.ctx)


class CityWarfareTalk39(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1952, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001952.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__19$', time=7)
        self.set_skip(state=CityWarfareTalk40)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return CityWarfareTalk40(self.ctx)


class CityWarfareTalk40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk41(self.ctx)


class CityWarfareTalk41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[402], return_view=False)
        self.set_onetime_effect(id=1953, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001953.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__20$', time=6)
        self.set_skip(state=CityWarfareTalk42)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return CityWarfareTalk42(self.ctx)


class CityWarfareTalk42(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk43(self.ctx)


class CityWarfareTalk43(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[504,505], return_view=False)
        self.set_onetime_effect(id=1891, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001891.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__21$', time=7)
        self.set_skip(state=CityWarfareTalk44)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return CityWarfareTalk44(self.ctx)


class CityWarfareTalk44(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk45(self.ctx)


class CityWarfareTalk45(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[405,406], return_view=False)
        self.set_onetime_effect(id=1954, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001954.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__22$', time=13)
        self.set_skip(state=CityWarfareTalk46)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return CityWarfareTalk46(self.ctx)


class CityWarfareTalk46(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk47(self.ctx)


class CityWarfareTalk47(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[206,207], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=1000, sequence_name='Sit_Down_HeadUP')
        self.set_onetime_effect(id=1892, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001892.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__23$', time=5)
        self.set_skip(state=CityWarfareTalk48)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk48(self.ctx)


class CityWarfareTalk48(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk49(self.ctx)


class CityWarfareTalk49(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[410,411], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=2000, sequence_name='Bore_B')
        self.set_onetime_effect(id=1955, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001955.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__24$', time=10)
        self.set_skip(state=CityWarfareTalk50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return CityWarfareTalk50(self.ctx)


class CityWarfareTalk50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk51(self.ctx)


class CityWarfareTalk51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1956, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001956.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__25$', time=6)
        self.set_skip(state=CityWarfareTalk52)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return CityWarfareTalk52(self.ctx)


class CityWarfareTalk52(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk53(self.ctx)


class CityWarfareTalk53(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[500,501], return_view=False)
        self.set_onetime_effect(id=1957, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001957.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__26$', time=10)
        self.set_skip(state=CityWarfareTalk54)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return CityWarfareTalk54(self.ctx)


class CityWarfareTalk54(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk55(self.ctx)


class CityWarfareTalk55(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[402], return_view=False)
        self.set_onetime_effect(id=1958, enable=True, path='BG/Common/Sound/Eff_Sound_52000054_Turka_00001958.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000054_QD__EPILOGUE_K__27$', time=12)
        self.set_skip(state=CityWarfareTalk56)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return CityWarfareTalk56(self.ctx)


class CityWarfareTalk56(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk57(self.ctx)


class CityWarfareTalk57(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[202,203], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=1000, sequence_name='Sit_Down_HeadUP')
        self.set_onetime_effect(id=1893, enable=True, path='BG/Common/Sound/Eff_Sound_52000055_Katvan_00001893.xml')
        self.set_dialogue(type=2, spawn_id=11001958, script='$52000054_QD__EPILOGUE_K__28$', time=5)
        self.set_skip(state=CityWarfareTalk58)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk58(self.ctx)


class CityWarfareTalk58(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CityWarfareTalk59(self.ctx)


class CityWarfareTalk59(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CityWarfareTalk60(self.ctx)


class CityWarfareTalk60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2000025, portal_id=2)


initial_state = start
