""" trigger/52000098_qd/ep10movie.xml """
import trigger_api


class 연출시작검사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10000], quest_ids=[20002266], quest_states=[3]):
            # 챕터6 에필로그 [10002353 허락되지 않은 일] 미완료 시
            return LoadingDelayB0(self.ctx)


class LoadingDelayB0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=11100104, enable=True, path='BG/Common/Sound/Eff_AMB_DarkCorridor_01.xml') # 어둠의 회랑 환경음
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        # self.set_cinematic_ui(type=9, script='현 시각, 검은달 심연 성채')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[2000], auto_target=False) # 검은마법사
        self.spawn_monster(spawn_ids=[2001], auto_target=False) # 마드리아

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraEffect1(self.ctx)


class CameraEffect1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_madria') # 마드리아 이동
        self.select_camera_path(path_ids=[3000,3001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            return CameraEffect2(self.ctx)


class CameraEffect2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Epilogue10Talk1(self.ctx)


class Epilogue10Talk1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[3004,3005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue10Talk3(self.ctx)


class Epilogue10Talk3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[3002,3003], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000098_QD__EP10MOVIE__0$', time=12)
        self.set_skip(state=Epilogue10Talk4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return Epilogue10Talk4(self.ctx)


class Epilogue10Talk4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk5(self.ctx)


class Epilogue10Talk5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3006,3007], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000098_QD__EP10MOVIE__1$', time=9)
        self.set_onetime_effect(id=1998, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_Start_01_00001998.xml')
        self.set_skip(state=Epilogue10Talk6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return Epilogue10Talk6(self.ctx)


class Epilogue10Talk6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk7(self.ctx)


class Epilogue10Talk7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000098_QD__EP10MOVIE__2$', time=9)
        self.set_onetime_effect(id=1999, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_Start_02_00001999.xml')
        self.set_skip(state=Epilogue10Talk8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return Epilogue10Talk8(self.ctx)


class Epilogue10Talk8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk9(self.ctx)


class Epilogue10Talk9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3008,3009], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000098_QD__EP10MOVIE__15$', time=4)
        self.set_skip(state=Epilogue10Talk10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Epilogue10Talk10(self.ctx)


class Epilogue10Talk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk11(self.ctx)


class Epilogue10Talk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3010,3011], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000098_QD__EP10MOVIE__3$', time=6)
        self.set_onetime_effect(id=2000, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_Start_03_00002000.xml')
        self.set_skip(state=Epilogue10Talk12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Epilogue10Talk12(self.ctx)


class Epilogue10Talk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk13(self.ctx)


class Epilogue10Talk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3012,3013], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000098_QD__EP10MOVIE__4$', time=5)
        self.set_skip(state=Epilogue10Talk14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue10Talk14(self.ctx)


class Epilogue10Talk14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk16(self.ctx)


class Epilogue10Talk16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[53005,53006], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000098_QD__EP10MOVIE__5$', time=5)
        self.set_skip(state=Epilogue10Talk17)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue10Talk17(self.ctx)


class Epilogue10Talk17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=2100275, path='BG/Common/Sound/Eff_System_DarkLord_Breathing.xml') # 11001957 호흡기
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk18(self.ctx)


class Epilogue10Talk18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3014], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000098_QD__EP10MOVIE__6$', time=7)
        self.set_skip(state=Epilogue10Talk19)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue10Talk19(self.ctx)


class Epilogue10Talk19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk20(self.ctx)


class Epilogue10Talk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3015], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000098_QD__EP10MOVIE__7$', time=5)
        self.set_skip(state=Epilogue10Talk21)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue10Talk21(self.ctx)


class Epilogue10Talk21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk22(self.ctx)


class Epilogue10Talk22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3016,3017], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000098_QD__EP10MOVIE__8$', time=6)
        self.set_skip(state=Epilogue10Talk23)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue10Talk23(self.ctx)


class Epilogue10Talk23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk24(self.ctx)


class Epilogue10Talk24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3018], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000098_QD__EP10MOVIE__9$', time=5)
        self.set_onetime_effect(id=2001, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_Start_04_00002001.xml')
        self.set_skip(state=Epilogue10Talk25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue10Talk25(self.ctx)


class Epilogue10Talk25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk27(self.ctx)


class Epilogue10Talk27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3019,3020], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000098_QD__EP10MOVIE__10$', time=5)
        self.set_skip(state=Epilogue10Talk28)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Epilogue10Talk28(self.ctx)


class Epilogue10Talk28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk29(self.ctx)


class Epilogue10Talk29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3021,3022], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000098_QD__EP10MOVIE__11$', time=10)
        self.set_skip(state=Epilogue10Talk30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Epilogue10Talk30(self.ctx)


class Epilogue10Talk30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk31(self.ctx)


class Epilogue10Talk31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3023,3024], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000098_QD__EP10MOVIE__12$', time=10)
        self.set_skip(state=Epilogue10Talk32)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue10Talk32(self.ctx)


class Epilogue10Talk32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk33(self.ctx)


class Epilogue10Talk33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3025,3026], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001955, script='$52000098_QD__EP10MOVIE__13$', time=7)
        self.set_skip(state=Epilogue10Talk34)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Epilogue10Talk34(self.ctx)


class Epilogue10Talk34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Epilogue10Talk35(self.ctx)


class Epilogue10Talk35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3027,3028], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001851, script='$52000098_QD__EP10MOVIE__14$', time=12)
        self.set_skip(state=Epilogue10Talk36)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Epilogue10Talk36(self.ctx)


class Epilogue10Talk36(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2000175, portal_id=1)


initial_state = 연출시작검사
