""" trigger/02000035_in/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[3]):
            return 기본(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[2]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[1]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001605], quest_states=[3]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001605], quest_states=[2]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001605], quest_states=[1]):
            return npc스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001604], quest_states=[3]):
            return npc스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001604], quest_states=[2]):
            return npc스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001604], quest_states=[1]):
            return 기본(self.ctx)


class 기본(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class npc스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001605], quest_states=[1]):
            return 연출준비(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001605], quest_states=[1]):
            return NPC스폰조건01(self.ctx)


class NPC스폰조건01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001605], quest_states=[2]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001605], quest_states=[1]):
            return 연출준비(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001604], quest_states=[3]):
            return NPC스폰조건02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001604], quest_states=[2]):
            return NPC스폰조건02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001604], quest_states=[1]):
            return 기본(self.ctx)


class NPC스폰조건02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001605], quest_states=[2]):
            return 탈주이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001605], quest_states=[1]):
            return 연출준비(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001604], quest_states=[3]):
            return NPC스폰조건01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001604], quest_states=[2]):
            return NPC스폰조건01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001604], quest_states=[1]):
            return 기본(self.ctx)


class 탈주이후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102,103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 연출준비00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출준비(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000035, portal_id=10)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=케이틀린슬픔_스킵완료, action='nextState') # setsceneskip set
        # setsceneskip set
        # setsceneskip set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 언쟁시작(self.ctx)


class 언쟁시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003264, script='$02000035_IN__MAIN__0$', time=4)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8150):
            return 케이틀린대사01(self.ctx)


class 케이틀린대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003262, script='$02000035_IN__MAIN__1$', time=4)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3000.0)
        self.set_skip(state=케이틀린대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6400):
            return 앤대사01(self.ctx)


class 케이틀린대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 앤대사01(self.ctx)


class 앤대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003264, script='$02000035_IN__MAIN__2$', time=5)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=앤대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5328):
            return 케이틀린대사02(self.ctx)


class 앤대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 케이틀린대사02(self.ctx)


class 케이틀린대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003262, script='$02000035_IN__MAIN__3$', time=3)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3000.0)
        self.set_skip(state=케이틀린대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9404):
            return 호르헤대사01(self.ctx)


class 케이틀린대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 호르헤대사01(self.ctx)


class 호르헤대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003263, script='$02000035_IN__MAIN__4$', time=4)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=3000.0)
        self.set_skip(state=호르헤대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 케이틀린대사03(self.ctx)


class 호르헤대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 케이틀린대사03(self.ctx)


class 케이틀린대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003262, script='$02000035_IN__MAIN__5$', time=5)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=케이틀린대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9404):
            return 앤대사02(self.ctx)


class 케이틀린대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 앤대사02(self.ctx)


class 앤대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003264, script='$02000035_IN__MAIN__9$', time=3)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='ChatUp_A', duration=2000.0)
        self.set_skip(state=앤대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 호르헤대사02(self.ctx)


class 앤대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 호르헤대사02(self.ctx)


class 호르헤대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003263, script='$02000035_IN__MAIN__10$', time=2)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='ChatUp_A', duration=2000.0)
        self.set_skip(state=호르헤대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 케이틀린대사04(self.ctx)


class 호르헤대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 케이틀린대사04(self.ctx)


class 케이틀린대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003262, script='$02000035_IN__MAIN__6$', time=4)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=케이틀린대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4780):
            return 케이틀린탈주01(self.ctx)


class 케이틀린대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 케이틀린탈주01(self.ctx)


class 케이틀린탈주01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_100_wayout')
        self.move_user_path(patrol_name='MS2PatrolData_PC01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 케이틀린탈주02(self.ctx)


class 케이틀린탈주02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003262, script='$02000035_IN__MAIN__7$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 케이틀린탈주03(self.ctx)


class 케이틀린탈주03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101_wayout')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC멈칫(self.ctx)


class PC멈칫(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$02000035_IN__MAIN__11$', time=2)
        # self.set_pc_emotion_loop(sequence_name='Talk_A', duration=1000.0)
        self.destroy_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 앤대사03(self.ctx)


class 앤대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003264, script='$02000035_IN__MAIN__8$', time=3)
        # self.set_npc_emotion_loop(spawn_id=103, sequence_name='ChatUp_A', duration=3000.0)
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='ChatUp_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4022):
            return 연출종료(self.ctx)


class 케이틀린슬픔_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[101])
        self.move_user_path(patrol_name='MS2PatrolData_PC01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9000, type='trigger', achieve='KatelyninGrief')
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
