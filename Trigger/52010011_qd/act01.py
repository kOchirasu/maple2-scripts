""" trigger/52010011_qd/act01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.set_effect(trigger_ids=[5000]) # 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 퀘스트시작(self.ctx)


class 퀘스트시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002811], quest_states=[2]):
            # Quest
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 진행(self.ctx)


class 진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010011, portal_id=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대사_01_테모로(self.ctx)


class 대사_01_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__0$', time=5)
        self.set_skip(state=대사_01_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_01_테모로skip(self.ctx)


class 대사_01_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_02_테모로(self.ctx)


class 대사_02_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__1$', time=5)
        self.set_skip(state=대사_02_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_02_테모로skip(self.ctx)


class 대사_02_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_03_PC(self.ctx)


class 대사_03_PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52010011_QD__ACT01__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대사_04_테모로(self.ctx)


class 대사_04_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__3$', time=5)
        self.set_skip(state=대사_04_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_04_테모로skip(self.ctx)


class 대사_04_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_05_테모로(self.ctx)


class 대사_05_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__4$', time=5)
        self.set_skip(state=대사_05_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_05_테모로skip(self.ctx)


class 대사_05_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_06_PC(self.ctx)


class 대사_06_PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52010011_QD__ACT01__5$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대사_07_테모로(self.ctx)


class 대사_07_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__6$', time=5)
        self.set_skip(state=대사_07_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_07_테모로skip(self.ctx)


class 대사_07_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_08_테모로(self.ctx)


class 대사_08_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__7$', time=5)
        self.set_skip(state=대사_08_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_08_테모로skip(self.ctx)


class 대사_08_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_09_PC(self.ctx)


class 대사_09_PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52010011_QD__ACT01__8$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대사_10_테모로(self.ctx)


class 대사_10_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__9$', time=5)
        self.set_skip(state=대사_10_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_10_테모로skip(self.ctx)


class 대사_10_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_11_테모로(self.ctx)


class 대사_11_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__10$', time=5)
        self.set_skip(state=대사_11_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_11_테모로skip(self.ctx)


class 대사_11_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_12_PC(self.ctx)


class 대사_12_PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52010011_QD__ACT01__11$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_13_테모로(self.ctx)


class 대사_13_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__12$', time=5)
        self.set_skip(state=대사_13_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_13_테모로skip(self.ctx)


class 대사_13_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 영상준비(self.ctx)


class 영상준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_timer(timer_id='21', seconds=2)
        self.select_camera_path(path_ids=[601,602], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='21'):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='common\\KarKarIntro.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 대사_14_PC(self.ctx)
        if self.wait_tick(wait_tick=18000):
            return 대사_14_PC(self.ctx)


class 대사_14_PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=1, script='$52010011_QD__ACT01__13$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대사_15_테모로(self.ctx)


class 대사_15_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__14$', time=5)
        self.set_skip(state=대사_15_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_15_테모로skip(self.ctx)


class 대사_15_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_16_테모로(self.ctx)


class 대사_16_테모로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001314, script='$52010011_QD__ACT01__15$', time=5)
        self.set_skip(state=대사_16_테모로skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_16_테모로skip(self.ctx)


class 대사_16_테모로skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.spawn_monster(spawn_ids=[1001])
        self.set_skip(state=대사_17_덴덴)

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_17_덴덴(self.ctx)


class 대사_17_덴덴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_2001')
        self.set_dialogue(type=2, spawn_id=11001313, script='$52010011_QD__ACT01__16$', time=5)
        self.set_skip(state=대사_17_덴덴skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대사_17_덴덴skip(self.ctx)


class 대사_17_덴덴skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_18_PC(self.ctx)


class 대사_18_PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52010011_QD__ACT01__17$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대사_19_덴덴(self.ctx)


class 대사_19_덴덴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001313, script='$52010011_QD__ACT01__18$', time=4)
        self.set_skip(state=대사_19_덴덴skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대사_19_덴덴skip(self.ctx)


class 대사_19_덴덴skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 대사_20_PC(self.ctx)


class 대사_20_PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52010011_QD__ACT01__19$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대사_21_덴덴(self.ctx)


class 대사_21_덴덴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001313, script='$52010011_QD__ACT01__20$', time=3)
        self.set_skip(state=대사_21_덴덴skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대사_21_덴덴skip(self.ctx)


class 대사_21_덴덴skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
