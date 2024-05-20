""" trigger/52000035_qd/epilogue4movie.xml """
import trigger_api


# 퀘스트를 완료하지 못했을때 케어
class 한라봉에이드검사1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[6000], quest_ids=[50001677], quest_states=[2]):
            # 챕터6 에필로그 [50001677 허락되지 않은 일] 미완료 시
            return ReturnMapReadyEP6(self.ctx)
        if not self.quest_user_detected(box_ids=[6000], quest_ids=[50001677], quest_states=[2]):
            # 챕터6 에필로그 [50001677 허락되지 않은 일] 미완료 시
            return 한라봉에이드검사2(self.ctx)


class 한라봉에이드검사2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[5000], quest_ids=[50001625], quest_states=[2]):
            # 챕터5 에필로그 [50001625 엇갈리는 마음] 미완료 시
            return ReturnMapReadyEP5(self.ctx)
        if not self.quest_user_detected(box_ids=[5000], quest_ids=[50001625], quest_states=[2]):
            # 챕터5 에필로그 [50001625 엇갈리는 마음] 미완료 시
            return 한라봉에이드검사3(self.ctx)


class 한라봉에이드검사3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[4000], quest_ids=[50001613], quest_states=[2]):
            # 챕터4 에필로그 [50001613 푸른 희망의 빛] 미완료 시
            return ReturnMapReadyEP4(self.ctx)
        if not self.quest_user_detected(box_ids=[4000], quest_ids=[50001613], quest_states=[2]):
            # 챕터4 에필로그 [50001613 푸른 희망의 빛] 미완료 시
            return StartCheckEP6(self.ctx)


# 보내줄 맵 검사 EP6
class ReturnMapReadyEP6(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return ReturnMapReadyEP6_1(self.ctx)


class ReturnMapReadyEP6_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE4MOVIE__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ReturnMapReadyEP6_2(self.ctx)


class ReturnMapReadyEP6_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000154, portal_id=1)


# 보내줄 맵 검사 EP5
class ReturnMapReadyEP5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return ReturnMapReadyEP5_1(self.ctx)


class ReturnMapReadyEP5_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE4MOVIE__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ReturnMapReadyEP5_2(self.ctx)


class ReturnMapReadyEP5_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000065, portal_id=1)


# 보내줄 맵 검사 EP4
class ReturnMapReadyEP4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return ReturnMapReadyEP4_1(self.ctx)


class ReturnMapReadyEP4_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE4MOVIE__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ReturnMapReadyEP4_2(self.ctx)


class ReturnMapReadyEP4_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000001, portal_id=1)


# 연출 분기 검사
class StartCheckEP6(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[6000], quest_ids=[50001677], quest_states=[3]):
            # 챕터6 에필로그 [50001677 허락되지 않은 일] 완료 시
            return 번으로보내는스테이트3(self.ctx)
        if not self.quest_user_detected(box_ids=[6000], quest_ids=[50001677], quest_states=[3]):
            return StartCheckEP5(self.ctx)


class StartCheckEP5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[5000], quest_ids=[50001625], quest_states=[3]):
            # 챕터5 에필로그 [50001625 엇갈리는 마음] 완료 시
            return 번으로보내는스테이트2(self.ctx)
        if not self.quest_user_detected(box_ids=[5000], quest_ids=[50001625], quest_states=[3]):
            return StartCheckEP4(self.ctx)


class StartCheckEP4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[4000], quest_ids=[50001613], quest_states=[3]):
            # 챕터4 에필로그 [50001613 푸른 희망의 빛] 완료 시
            return LoadingDelayA0(self.ctx)


class 번으로보내는스테이트2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2, key='50001625', value=1)


class 번으로보내는스테이트3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3, key='50001677', value=1)


# 챕터4 에필로그 [50001613 푸른 희망의 빛] 완료 시 연출시작
class LoadingDelayA0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Quit, action='exit')
        self.set_onetime_effect(id=11100104, enable=True, path='BG/Common/Sound/Eff_AMB_DarkCorridor_01.xml') # 어둠의 회랑 환경음
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[900], auto_target=False) # 검은 마법사
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 11001957
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 투르카
        self.spawn_monster(spawn_ids=[300], auto_target=False) # 마드리아

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LoadingDelayA1(self.ctx)


class LoadingDelayA1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_EP4_DarkLord') # 11001957 이동
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_EP4_Turka') # 투르카 이동
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_EP4_Madria') # 마드리아 이동
        self.move_npc(spawn_id=400, patrol_name='MS2PatrolData_EP4_bella') # 마드리아 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffectA0(self.ctx)


class CameraEffectA0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 페이드 켠다
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_EP4_DarkLord') # 11001957 이동
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_EP4_Turka') # 투르카 이동
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_EP4_Madria') # 마드리아 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraEffectA1(self.ctx)


class CameraEffectA1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000035_QD__EPILOGUE4MOVIE__3$')
        self.select_camera_path(path_ids=[1000,1001,1002,1003,1004,1005,1006,1007,1008,1009], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffectA2(self.ctx)


class CameraEffectA2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml') # 페이드 끈다
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return CameraEffect1100(self.ctx)


class CameraEffect1100(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraEffect1101(self.ctx)


class CameraEffect1101(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2100276, enable=True, path='BG/Common/Sound/Eff_System_Chapter4_ZoomIn_01.xml')
        self.select_camera_path(path_ids=[1100,1101,1104], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return CameraEffect_1103(self.ctx)


class CameraEffect_1103(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraEffect_1104(self.ctx)


class CameraEffect_1104(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_onetime_effect(id=2100277, enable=True, path='BG/Common/Sound/Eff_System_Chapter4_DarkWizard_Appear_01.xml')
        self.select_camera_path(path_ids=[1103,1102,1105], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=900, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraEffect_1105(self.ctx)


class CameraEffect_1105(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.1, duration=2.5, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CameraEffect_1106(self.ctx)


class CameraEffect_1106(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CameraEffectA3(self.ctx)


class CameraEffectA3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.select_camera_path(path_ids=[1200,1201], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE4MOVIE__4$', time=7)
        self.set_skip(state=Epilogue4Talk1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue4Talk1(self.ctx)


class Epilogue4Talk1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk2(self.ctx)


class Epilogue4Talk2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1300], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE4MOVIE__5$', time=5)
        self.set_skip(state=Epilogue4Talk3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk3(self.ctx)


class Epilogue4Talk3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk4(self.ctx)


class Epilogue4Talk4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE4MOVIE__6$', time=5)
        self.set_skip(state=Epilogue4Talk5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk5(self.ctx)


class Epilogue4Talk5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk6(self.ctx)


class Epilogue4Talk6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1915, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001915.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE4MOVIE__7$', time=6)
        self.set_skip(state=Epilogue4Talk7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Epilogue4Talk7(self.ctx)


class Epilogue4Talk7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk8(self.ctx)


class Epilogue4Talk8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2100,2101], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_EP4_DarkToTurka') # 11001957,투르카 노려봄!
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE4MOVIE__8$', time=5)
        self.set_skip(state=Epilogue4Talk9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk9(self.ctx)


class Epilogue4Talk9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk10(self.ctx)


class Epilogue4Talk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE4MOVIE__9$', time=5)
        self.set_skip(state=Epilogue4Talk11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk11(self.ctx)


class Epilogue4Talk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk12(self.ctx)


class Epilogue4Talk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE4MOVIE__10$', time=5)
        self.set_skip(state=Epilogue4Talk12B)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk12B(self.ctx)


class Epilogue4Talk12B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk12C(self.ctx)


class Epilogue4Talk12C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_TurkaToDark') # 투르카,11001957 노려봄!
        self.select_camera_path(path_ids=[2102,2103], return_view=False)
        self.set_onetime_effect(id=1916, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001916.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE4MOVIE__11$', time=13)
        self.set_skip(state=Epilogue4Talk13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return Epilogue4Talk13(self.ctx)


class Epilogue4Talk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return DM_AttScene01(self.ctx)


# 검은마법사 화남!
class DM_AttScene01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000,2001], return_view=False)
        self.set_onetime_effect(id=2100278, enable=True, path='BG/Common/Sound/Eff_System_Chapter4_DarkWizard_Attack_01.xml')
        self.set_npc_emotion_sequence(spawn_id=900, sequence_name='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DM_AttScene02(self.ctx)


class DM_AttScene02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.1, duration=2.5, interpolator=2) # 2초간 느려지기 시작
        self.set_onetime_effect(id=1917, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001917.xml')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_darkReturn') # 11001957,투르카 원복
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_TurkaReturn') # 11001957,투르카 원복

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DM_AttScene03(self.ctx)


class DM_AttScene03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Damg_A')
        self.set_npc_emotion_sequence(spawn_id=200, sequence_name='Damg_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return DM_AttScene04(self.ctx)


class DM_AttScene04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2002,2003], return_view=False)
        self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.1, duration=2.5, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Epilogue4Talk14(self.ctx)


class Epilogue4Talk14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1501], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000035_QD__EPILOGUE4MOVIE__12$', time=5)
        self.set_skip(state=Epilogue4Talk15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk15(self.ctx)


class Epilogue4Talk15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk16(self.ctx)


class Epilogue4Talk16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1200], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE4MOVIE__38$', time=5)
        self.set_skip(state=Epilogue4Talk17)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Epilogue4Talk17(self.ctx)


class Epilogue4Talk17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk18(self.ctx)


class Epilogue4Talk18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1300], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE4MOVIE__13$', time=5)
        self.set_skip(state=Epilogue4Talk19)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Epilogue4Talk19(self.ctx)


class Epilogue4Talk19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk20(self.ctx)


class Epilogue4Talk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1500], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000035_QD__EPILOGUE4MOVIE__14$', time=5)
        self.set_skip(state=Epilogue4Talk21)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk21(self.ctx)


class Epilogue4Talk21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk22(self.ctx)


class Epilogue4Talk22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3000,3001], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000035_QD__EPILOGUE4MOVIE__15$', time=5)
        self.set_skip(state=Epilogue4Talk23)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk23(self.ctx)


class Epilogue4Talk23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk24(self.ctx)


class Epilogue4Talk24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000035_QD__EPILOGUE4MOVIE__16$', time=5)
        self.set_skip(state=Epilogue4Talk25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk25(self.ctx)


class Epilogue4Talk25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk26(self.ctx)


class Epilogue4Talk26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000035_QD__EPILOGUE4MOVIE__17$', time=5)
        self.set_skip(state=Epilogue4Talk27)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk27(self.ctx)


class Epilogue4Talk27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk27A(self.ctx)


class Epilogue4Talk27A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1203], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE4MOVIE__39$', time=5)
        self.set_skip(state=Epilogue4Talk27B)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk27B(self.ctx)


class Epilogue4Talk27B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk28(self.ctx)


class Epilogue4Talk28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1502,1504], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000035_QD__EPILOGUE4MOVIE__18$', time=5)
        self.set_skip(state=Epilogue4Talk29)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk29(self.ctx)


class Epilogue4Talk29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk30(self.ctx)


class Epilogue4Talk30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1400,1406], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000035_QD__EPILOGUE4MOVIE__19$', time=8)
        self.set_onetime_effect(id=1978, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_01_00001978.xml')
        self.set_skip(state=Epilogue4Talk31)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Epilogue4Talk31(self.ctx)


class Epilogue4Talk31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk32(self.ctx)


class Epilogue4Talk32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1401], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000035_QD__EPILOGUE4MOVIE__20$', time=6)
        self.set_onetime_effect(id=1979, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_02_00001979.xml')
        self.set_skip(state=Epilogue4Talk33)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Epilogue4Talk33(self.ctx)


class Epilogue4Talk33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk34(self.ctx)


class Epilogue4Talk34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1505,1506], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000035_QD__EPILOGUE4MOVIE__21$', time=5)
        self.set_skip(state=Epilogue4Talk35)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk35(self.ctx)


class Epilogue4Talk35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk36(self.ctx)


class Epilogue4Talk36(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2100279, enable=True, path='BG/Common/Sound/Eff_System_Chapter4_ZoomOut_01.xml')
        self.select_camera_path(path_ids=[1403], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000035_QD__EPILOGUE4MOVIE__22$', time=5)
        self.set_onetime_effect(id=1980, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_03_00001980.xml')
        self.set_skip(state=Epilogue4Talk37)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk37(self.ctx)


class Epilogue4Talk37(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk38(self.ctx)


class Epilogue4Talk38(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1500,1503], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000035_QD__EPILOGUE4MOVIE__23$', time=5)
        self.set_skip(state=Epilogue4Talk39)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk39(self.ctx)


class Epilogue4Talk39(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk40(self.ctx)


class Epilogue4Talk40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1407], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000035_QD__EPILOGUE4MOVIE__24$', time=7)
        self.set_onetime_effect(id=1981, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_04_00001981.xml')
        self.set_skip(state=Epilogue4Talk41)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue4Talk41(self.ctx)


class Epilogue4Talk41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk42(self.ctx)


class Epilogue4Talk42(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1401], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000035_QD__EPILOGUE4MOVIE__25$', time=5)
        self.set_skip(state=Epilogue4Talk43)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk43(self.ctx)


class Epilogue4Talk43(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk44(self.ctx)


class Epilogue4Talk44(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1402], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000035_QD__EPILOGUE4MOVIE__26$', time=5)
        self.set_skip(state=Epilogue4Talk45)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk45(self.ctx)


class Epilogue4Talk45(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk46(self.ctx)


class Epilogue4Talk46(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1404], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000035_QD__EPILOGUE4MOVIE__27$', time=5)
        self.set_onetime_effect(id=1982, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_05_00001982.xml')
        self.set_skip(state=Epilogue4Talk47)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk47(self.ctx)


class Epilogue4Talk47(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk48(self.ctx)


class Epilogue4Talk48(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1200,1201], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE4MOVIE__28$', time=5)
        self.set_skip(state=Epilogue4Talk49)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk49(self.ctx)


class Epilogue4Talk49(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk50(self.ctx)


class Epilogue4Talk50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE4MOVIE__29$', time=5)
        self.set_skip(state=Epilogue4Talk51)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk51(self.ctx)


class Epilogue4Talk51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk52(self.ctx)


class Epilogue4Talk52(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_MadToDark') # 마드리아, 11001957 노려봄!
        self.select_camera_path(path_ids=[1405], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000035_QD__EPILOGUE4MOVIE__30$', time=5)
        self.set_onetime_effect(id=1983, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter4_End_06_00001983.xml')
        self.set_skip(state=Epilogue4Talk53)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk53(self.ctx)


class Epilogue4Talk53(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk54(self.ctx)


class Epilogue4Talk54(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1202], return_view=False)
        self.move_npc(spawn_id=300, patrol_name='MS2PatrolData_madriaReturn') # 마드리아, 재자리
        self.set_dialogue(type=2, spawn_id=11001957, script='$52000035_QD__EPILOGUE4MOVIE__31$', time=5)
        self.set_skip(state=Epilogue4Talk55)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk55(self.ctx)


class Epilogue4Talk55(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk56(self.ctx)


class Epilogue4Talk56(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1100,1101,1104], return_view=False)
        self.set_onetime_effect(id=1918, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001918.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE4MOVIE__32$', time=12)
        self.set_skip(state=Epilogue4Talk58)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return Epilogue4Talk58(self.ctx)


class Epilogue4Talk58(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk59(self.ctx)


class Epilogue4Talk59(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[400], auto_target=False) # 벨라
        self.move_npc(spawn_id=400, patrol_name='MS2PatrolData_EP4_bella_go') # 벨라, 나서기
        self.select_camera_path(path_ids=[1600,1601], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE4MOVIE__33$', time=5)
        self.set_skip(state=Epilogue4Talk60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Epilogue4Talk60(self.ctx)


class Epilogue4Talk60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk61(self.ctx)


class Epilogue4Talk61(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1300,1301], return_view=False)
        self.set_onetime_effect(id=1919, enable=True, path='BG/Common/Sound/Eff_Sound_52000035_Turka_00001919.xml')
        self.set_dialogue(type=2, spawn_id=11001956, script='$52000035_QD__EPILOGUE4MOVIE__34$', time=8)
        self.set_skip(state=Epilogue4Talk62)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Epilogue4Talk62(self.ctx)


class Epilogue4Talk62(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk63(self.ctx)


class Epilogue4Talk63(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1602], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE4MOVIE__35$', time=5)
        self.set_skip(state=Epilogue4Talk64)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk64(self.ctx)


class Epilogue4Talk64(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk65(self.ctx)


class Epilogue4Talk65(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1603,1604], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE4MOVIE__36$', time=5)
        self.set_skip(state=Epilogue4Talk66)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk66(self.ctx)


class Epilogue4Talk66(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk67(self.ctx)


class Epilogue4Talk67(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1605,1606], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001852, script='$52000035_QD__EPILOGUE4MOVIE__37$', time=5)
        self.set_skip(state=Epilogue4Talk68)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue4Talk68(self.ctx)


class Epilogue4Talk68(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue4Talk69(self.ctx)


class Epilogue4Talk69(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Epilogue4Talk70(self.ctx)


class Epilogue4Talk70(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2000001, portal_id=2)


initial_state = 한라봉에이드검사1
