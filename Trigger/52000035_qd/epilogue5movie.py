""" trigger/52000035_qd/epilogue5movie.xml """
import trigger_api


class start01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='50001625') == 1:
            return start02(self.ctx)


class start02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[5000], quest_ids=[50001625], quest_states=[3]):
            return LoadingDelayB0(self.ctx)
        if not self.quest_user_detected(box_ids=[5000], quest_ids=[50001625], quest_states=[3]):
            return ReturnMapReady0(self.ctx)


class ReturnMapReady0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return ReturnMapReady(self.ctx)


class ReturnMapReady(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE5MOVIE__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ReturnMap(self.ctx)


class ReturnMap(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000065, portal_id=1)


# 챕터5 에필로그 [50001625 엇갈리는 마음]완료 시 연출맵으로 이동
class LoadingDelayB0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Quit, action='exit')
        self.set_onetime_effect(id=11100104, enable=True, path='BG/Common/Sound/Eff_AMB_DarkCorridor_01.xml') # 어둠의 회랑 환경음
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 11001957
        self.spawn_monster(spawn_ids=[5400], auto_target=False) # 로그스1
        self.spawn_monster(spawn_ids=[5401], auto_target=False) # 로그스2
        self.spawn_monster(spawn_ids=[5200], auto_target=False) # 투르카
        self.spawn_monster(spawn_ids=[5300], auto_target=False) # 벨라

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return CameraEffect1(self.ctx)


class CameraEffect1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2100280, enable=True, path='BG/Common/Sound/Eff_System_Chapter5_Armour_Footsteps_Long_01.xml')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_EP4_DarkLord') # 11001957 이동
        self.move_npc(spawn_id=5400, patrol_name='MS2PatrolData_RoguesEnd_B') # 로그스 이동
        self.move_npc(spawn_id=5401, patrol_name='MS2PatrolData_RoguesEnd_A') # 로그스 이동
        self.select_camera_path(path_ids=[51000,51001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            return CameraEffect2(self.ctx)


class CameraEffect2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Epilogue5Talk1(self.ctx)


class Epilogue5Talk1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[52000,52001], return_view=False)
        self.set_onetime_effect(id=1920, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001920.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__1$', time=7)
        self.set_skip(state=Epilogue5Talk2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue5Talk2(self.ctx)


class Epilogue5Talk2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk3(self.ctx)


class Epilogue5Talk3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[52002,52003], return_view=False)
        self.set_onetime_effect(id=1921, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001921.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__2$', time=12)
        self.set_skip(state=Epilogue5Talk4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return Epilogue5Talk4(self.ctx)


class Epilogue5Talk4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk5(self.ctx)


class Epilogue5Talk5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[53007], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_EP4_DarkToTurka') # 11001957,투르카 노려봄!
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE5MOVIE__3$', time=5)
        self.set_skip(state=Epilogue5Talk6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk6(self.ctx)


class Epilogue5Talk6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2100275, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk7(self.ctx)


class Epilogue5Talk7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[52004], return_view=False)
        self.set_onetime_effect(id=1922, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001922.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__4$', time=7)
        self.set_skip(state=Epilogue5Talk8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue5Talk8(self.ctx)


class Epilogue5Talk8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk9(self.ctx)


class Epilogue5Talk9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_TurkaToDark') # 투르카,11001957 노려봄!
        self.select_camera_path(path_ids=[2102,2103], return_view=False)
        self.set_onetime_effect(id=1923, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001923.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__5$', time=8)
        self.set_skip(state=Epilogue5Talk10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Epilogue5Talk10(self.ctx)


class Epilogue5Talk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk11(self.ctx)


class Epilogue5Talk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[53001,53002], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_threatTurka') # 11001957,투르카 협박하러감
        self.set_onetime_effect(id=2100281, enable=True, path='BG/Common/Sound/Eff_System_Chapter5_Armor_Footsteps_Short_01.xml')
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE5MOVIE__6$', time=5)
        self.set_skip(state=Epilogue5Talk12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk12(self.ctx)


class Epilogue5Talk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk13(self.ctx)


class Epilogue5Talk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[53003,53004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE5MOVIE__7$', time=5)
        self.set_skip(state=Epilogue5Talk14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk14(self.ctx)


class Epilogue5Talk14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk16(self.ctx)


class Epilogue5Talk16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[53005,53006], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE5MOVIE__8$', time=5)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Bore_A')
        self.set_skip(state=Epilogue5Talk17)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk17(self.ctx)


class Epilogue5Talk17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=2100275, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk18(self.ctx)


class Epilogue5Talk18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[52005], return_view=False)
        self.set_onetime_effect(id=1924, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001924.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__9$', time=7)
        self.set_skip(state=Epilogue5Talk19)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue5Talk19(self.ctx)


class Epilogue5Talk19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.move_npc(spawn_id=5200, patrol_name='MS2PatrolData_TurkaReturn') # 11001957,투르카 원복
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk20(self.ctx)


class Epilogue5Talk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[53008,53009], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_EP4_DarkToTurka') # 11001957,투르카 노려봄!
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE5MOVIE__10$', time=5)
        self.set_skip(state=Epilogue5Talk21)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk21(self.ctx)


class Epilogue5Talk21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=2100275, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk22(self.ctx)


class Epilogue5Talk22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[51002,51003], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_darkReturn') # 11001957,투르카 원복
        self.set_onetime_effect(id=1925, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001925.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__11$', time=6)
        self.set_skip(state=Epilogue5Talk23)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Epilogue5Talk23(self.ctx)


class Epilogue5Talk23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk24(self.ctx)


class Epilogue5Talk24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1926, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001926.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__12$', time=5)
        self.set_skip(state=Epilogue5Talk25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk25(self.ctx)


class Epilogue5Talk25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk27(self.ctx)


class Epilogue5Talk27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.select_camera_path(path_ids=[53010], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE5MOVIE__32$', time=5)
        self.set_skip(state=Epilogue5Talk28)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk28(self.ctx)


class Epilogue5Talk28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2100275, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk29(self.ctx)


class Epilogue5Talk29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[52006,52007], return_view=False)
        self.set_onetime_effect(id=1927, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001927.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__13$', time=10)
        self.set_skip(state=Epilogue5Talk30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Epilogue5Talk30(self.ctx)


class Epilogue5Talk30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk31(self.ctx)


class Epilogue5Talk31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1928, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001928.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__14$', time=10)
        self.set_skip(state=Epilogue5Talk32)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Epilogue5Talk32(self.ctx)


class Epilogue5Talk32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk33(self.ctx)


class Epilogue5Talk33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[51004,51005], return_view=False)
        self.set_onetime_effect(id=1929, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001929.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__15$', time=7)
        self.set_skip(state=Epilogue5Talk34)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue5Talk34(self.ctx)


class Epilogue5Talk34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk35(self.ctx)


class Epilogue5Talk35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1930, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001930.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__16$', time=12)
        self.set_skip(state=Epilogue5Talk36)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return Epilogue5Talk36(self.ctx)


class Epilogue5Talk36(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk37(self.ctx)


class Epilogue5Talk37(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.select_camera_path(path_ids=[53011,53012], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE5MOVIE__17$', time=5)
        self.set_skip(state=Epilogue5Talk38)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk38(self.ctx)


class Epilogue5Talk38(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk39(self.ctx)


class Epilogue5Talk39(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_EP4_DarkToTurka') # 11001957,투르카 노려봄!
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE5MOVIE__18$', time=5)
        self.set_skip(state=Epilogue5Talk40)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk40(self.ctx)


class Epilogue5Talk40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2100275, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk41(self.ctx)


class Epilogue5Talk41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1300], return_view=False)
        self.set_onetime_effect(id=1931, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001931.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__19$', time=7)
        self.set_skip(state=Epilogue5Talk42)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue5Talk42(self.ctx)


class Epilogue5Talk42(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk43(self.ctx)


class Epilogue5Talk43(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_darkReturn') # 11001957,투르카 원복
        self.select_camera_path(path_ids=[1400], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=5300, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE5MOVIE__20$', time=5)
        self.set_skip(state=Epilogue5Talk44)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk44(self.ctx)


class Epilogue5Talk44(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk45(self.ctx)


class Epilogue5Talk45(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1300], return_view=False)
        self.set_onetime_effect(id=1932, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001932.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__21$', time=7)
        self.set_skip(state=Epilogue5Talk46)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue5Talk46(self.ctx)


class Epilogue5Talk46(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk47(self.ctx)


class Epilogue5Talk47(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[54000], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE5MOVIE__22$', time=5)
        self.set_skip(state=Epilogue5Talk48)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk48(self.ctx)


class Epilogue5Talk48(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk49(self.ctx)


class Epilogue5Talk49(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[52008], return_view=False)
        self.set_onetime_effect(id=1933, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001933.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__23$', time=5)
        self.set_skip(state=Epilogue5Talk50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk50(self.ctx)


class Epilogue5Talk50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk51(self.ctx)


class Epilogue5Talk51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[51006,51007], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE5MOVIE__24$', time=5)
        self.set_skip(state=Epilogue5Talk52)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk52(self.ctx)


class Epilogue5Talk52(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk53(self.ctx)


class Epilogue5Talk53(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1934, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001934.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE5MOVIE__25$', time=8)
        self.set_skip(state=Epilogue5Talk54)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Epilogue5Talk54(self.ctx)


class Epilogue5Talk54(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk55(self.ctx)


class Epilogue5Talk55(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2100275, enable=True, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.select_camera_path(path_ids=[53013,53014], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE5MOVIE__26$', time=5)
        self.set_skip(state=Epilogue5Talk56)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Epilogue5Talk56(self.ctx)


class Epilogue5Talk56(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2100275, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk57(self.ctx)


class Epilogue5Talk57(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1400], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE5MOVIE__27$', time=5)
        self.set_skip(state=Epilogue5Talk58)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk58(self.ctx)


class Epilogue5Talk58(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.move_npc(spawn_id=5300, patrol_name='MS2PatrolData_bellaOUT') # 벨라 퇴장
        self.set_onetime_effect(id=2100282, enable=True, path='BG/Common/Sound/Eff_System_Chapter5_Bella_Foosteps_01.xml')
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk59(self.ctx)


class Epilogue5Talk59(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[55001,55002], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE5MOVIE__28$', time=5)
        self.set_skip(state=Epilogue5Talk60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk60(self.ctx)


class Epilogue5Talk60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk61(self.ctx)


class Epilogue5Talk61(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[55003,55004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE5MOVIE__29$', time=5)
        self.set_skip(state=Epilogue5Talk62)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk62(self.ctx)


class Epilogue5Talk62(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk63(self.ctx)


class Epilogue5Talk63(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=10, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[55005,55006], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE5MOVIE__30$', time=5)
        self.set_skip(state=Epilogue5Talk64)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Epilogue5Talk64(self.ctx)


class Epilogue5Talk64(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_onetime_effect(id=2100282, path='BG/Common/Sound/Eff_System_Chapter5_Bella_Foosteps_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk65(self.ctx)


class Epilogue5Talk65(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[55007], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE5MOVIE__31$', time=5)
        self.set_skip(state=Epilogue5Talk66)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk66(self.ctx)


class Epilogue5Talk66(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue5Talk67(self.ctx)


class Epilogue5Talk67(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue5Talk68(self.ctx)


class Epilogue5Talk68(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2000065, portal_id=1)


initial_state = start01
