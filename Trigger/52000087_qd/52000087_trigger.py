""" trigger/52000087_qd/52000087_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10)
        self.set_effect(trigger_ids=[600])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[22651], quest_ids=[20002266], quest_states=[3]):
            return 용무없는유저는아웃(self.ctx)
        if self.quest_user_detected(box_ids=[22651], quest_ids=[10002781], quest_states=[1]):
            return 카르카르시작(self.ctx)
        if self.quest_user_detected(box_ids=[22651], quest_ids=[20002265], quest_states=[3]):
            return 완료연출01_20002265(self.ctx)


# 카르카르 연출, 메이플연합 회담씬
class 카르카르시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 진행(self.ctx)


class 진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에레브_1(self.ctx)


class 에레브_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000087_QD__52000087_TRIGGER__0$', time=3)
        self.set_skip(state=에레브_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에레브_1skip(self.ctx)


class 에레브_1skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 에레브_2(self.ctx)


class 에레브_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000087_QD__52000087_TRIGGER__1$', time=5)
        self.set_skip(state=에레브_2skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에레브_2skip(self.ctx)


class 에레브_2skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 에레브_3(self.ctx)


class 에레브_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000087_QD__52000087_TRIGGER__2$', time=5)
        self.set_skip(state=에레브_3skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에레브_3skip(self.ctx)


class 에레브_3skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 블랙아이_1(self.ctx)


class 블랙아이_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000006, script='$52000087_QD__52000087_TRIGGER__3$', time=3)
        self.set_skip(state=블랙아이_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 블랙아이_1skip(self.ctx)


class 블랙아이_1skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 블랙아이_1a(self.ctx)


class 블랙아이_1a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000006, script='$52000087_QD__52000087_TRIGGER__4$', time=5)
        self.set_skip(state=블랙아이_1askip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 블랙아이_1askip(self.ctx)


class 블랙아이_1askip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 프레이_1(self.ctx)


class 프레이_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000119, script='$52000087_QD__52000087_TRIGGER__5$', time=5)
        self.set_skip(state=프레이_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 프레이_1skip(self.ctx)


class 프레이_1skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 구르는천둥_1(self.ctx)


class 구르는천둥_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001581, script='$52000087_QD__52000087_TRIGGER__6$', time=3)
        self.set_skip(state=구르는천둥_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 구르는천둥_1skip(self.ctx)


class 구르는천둥_1skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 알론_1(self.ctx)


class 알론_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000087_QD__52000087_TRIGGER__7$', time=3)
        self.set_skip(state=알론_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 알론_1skip(self.ctx)


class 알론_1skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 오스칼_1(self.ctx)


class 오스칼_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000015, script='$52000087_QD__52000087_TRIGGER__8$', time=5)
        self.set_skip(state=오스칼_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 오스칼_1skip(self.ctx)


class 오스칼_1skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 블랙아이_2(self.ctx)


class 블랙아이_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000006, script='$52000087_QD__52000087_TRIGGER__9$', time=5)
        self.set_skip(state=블랙아이_2skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 블랙아이_2skip(self.ctx)


class 블랙아이_2skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 블랙아이_2a(self.ctx)


class 블랙아이_2a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000006, script='$52000087_QD__52000087_TRIGGER__10$', time=5)
        self.set_skip(state=블랙아이_2askip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 블랙아이_2askip(self.ctx)


class 블랙아이_2askip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 블랙아이_3(self.ctx)


class 블랙아이_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000006, script='$52000087_QD__52000087_TRIGGER__11$', time=5)
        self.set_skip(state=블랙아이_3skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 블랙아이_3skip(self.ctx)


class 블랙아이_3skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 알론_2(self.ctx)


class 알론_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000087_QD__52000087_TRIGGER__12$', time=3)
        self.set_skip(state=알론_2skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 알론_2skip(self.ctx)


class 알론_2skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 에레브_4(self.ctx)


class 에레브_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000087_QD__52000087_TRIGGER__13$', time=5)
        self.set_skip(state=에레브_4skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에레브_4skip(self.ctx)


class 에레브_4skip(trigger_api.Trigger):
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
        self.widget_action(type='SceneMovie', func='Clear')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_scene_movie(file_name='lumieragonhistory.swf', movie_id=1)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 알론_3(self.ctx)


class 알론_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000087_QD__52000087_TRIGGER__14$', time=5)
        self.set_skip(state=알론_3skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 알론_3skip(self.ctx)


class 알론_3skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 알론_4(self.ctx)


class 알론_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000087_QD__52000087_TRIGGER__15$', time=5)
        self.set_skip(state=알론_4skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 알론_4skip(self.ctx)


class 알론_4skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 알론_4a(self.ctx)


class 알론_4a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000087_QD__52000087_TRIGGER__16$', time=5)
        self.set_skip(state=알론_4askip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 알론_4askip(self.ctx)


class 알론_4askip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 알론_5(self.ctx)


class 알론_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000087_QD__52000087_TRIGGER__17$', time=5)
        self.set_skip(state=알론_5skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 알론_5skip(self.ctx)


class 알론_5skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 에레브_5(self.ctx)


class 에레브_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000087_QD__52000087_TRIGGER__18$', time=5)
        self.set_skip(state=에레브_5skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에레브_5skip(self.ctx)


class 에레브_5skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 에레브_6(self.ctx)


class 에레브_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000087_QD__52000087_TRIGGER__19$', time=5)
        self.set_skip(state=에레브_6skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에레브_6skip(self.ctx)


class 에레브_6skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칼_1(self.ctx)


class 칼_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000074, script='$52000087_QD__52000087_TRIGGER__20$', time=5)
        self.set_skip(state=칼_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 칼_1skip(self.ctx)


class 칼_1skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 에레브_7(self.ctx)


class 에레브_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000087_QD__52000087_TRIGGER__21$', time=5)
        self.set_skip(state=에레브_7skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에레브_7skip(self.ctx)


class 에레브_7skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 에레브_8(self.ctx)


class 에레브_8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000087_QD__52000087_TRIGGER__22$', time=5)
        self.set_skip(state=에레브_8skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에레브_8skip(self.ctx)


class 에레브_8skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=22651, type='trigger', achieve='Lumieragon_History')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


# 챕터10 [20002265 새로운 실마리]완료 시 연출, 오르데가 포탈타고 나타남
class 완료연출01_20002265(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user(map_id=52000087, portal_id=10)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 완료연출02_20002265(self.ctx)


class 완료연출02_20002265(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[2002,2003,2004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 완료연출03_20002265(self.ctx)


class 완료연출03_20002265(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.spawn_monster(spawn_ids=[1003], auto_target=False) # 오르데
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_Start') # 오르데 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 완료연출04_20002265(self.ctx)


class 완료연출04_20002265(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=1003, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 완료연출04_b20002265(self.ctx)


class 완료연출04_b20002265(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003087, script='$52000087_QD__52000087_TRIGGER__23$', time=3) # 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료연출04_c20002265(self.ctx)


class 완료연출04_c20002265(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1003, sequence_name='ChatUp_A')
        self.set_dialogue(type=2, spawn_id=11003087, script='$52000087_QD__52000087_TRIGGER__24$', time=3) # 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료연출05_20002265(self.ctx)


class 완료연출05_20002265(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=2.0)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_Orde') # 오르데 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[22651], quest_ids=[20002266], quest_states=[3]):
            return 완료연출01_20002266(self.ctx)


"""
챕터10 [20002265 새로운 실마리]완료 시 연출 종료, 오르데가 포탈타고 나타남
챕터10 [20002266 취향입니다, 존중해주시죠]완료 시 연출, 오르데와 PC가 포탈열고 사라짐
"""
class 완료연출01_난입20002266(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1003], auto_target=False) # 오르데

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 완료연출01_20002266(self.ctx)


class 완료연출01_20002266(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000087, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 완료연출02_20002266(self.ctx)


class 완료연출02_20002266(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[2005,2006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 완료연출03_20002266(self.ctx)


class 완료연출03_20002266(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003087, script='$52000087_QD__52000087_TRIGGER__25$', time=3) # 대사
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_OrdeOut') # 에레브 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료연출04_20002266(self.ctx)


class 완료연출04_20002266(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=500, visible=True, enable=True, minimap_visible=True)
        self.set_effect(trigger_ids=[601], visible=True)
        self.destroy_monster(spawn_ids=[1003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료연출05_20002266(self.ctx)


class 완료연출05_20002266(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)


class 용무없는유저는아웃(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[22651], quest_ids=[20002285], quest_states=[3]):
            return 챕터10에필로그연출01(self.ctx)


# 챕터10 에필로그 연출
class 챕터10에필로그연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user(map_id=52000087, portal_id=10)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 챕터10에필로그연출02(self.ctx)


class 챕터10에필로그연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__26$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출03(self.ctx)


class 챕터10에필로그연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__27$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출05(self.ctx)


class 챕터10에필로그연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__28$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출05b(self.ctx)


class 챕터10에필로그연출05b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출06(self.ctx)


class 챕터10에필로그연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=90000, enable=True) # 마드리아 고조 브금
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000087_QD__52000087_TRIGGER__29$', time=6)
        self.set_onetime_effect(id=2007, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_01_00002007.xml')
        self.set_skip(state=챕터10에필로그연출06스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 챕터10에필로그연출06스킵(self.ctx)


class 챕터10에필로그연출06스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출07(self.ctx)


class 챕터10에필로그연출07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000087_QD__52000087_TRIGGER__30$', time=6)
        self.set_onetime_effect(id=2008, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_02_00002008.xml')
        self.set_skip(state=챕터10에필로그연출07스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 챕터10에필로그연출07스킵(self.ctx)


class 챕터10에필로그연출07스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출08(self.ctx)


class 챕터10에필로그연출08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000087_QD__52000087_TRIGGER__31$', time=9)
        self.set_onetime_effect(id=2009, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_03_00002009.xml')
        self.set_skip(state=챕터10에필로그연출08스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 챕터10에필로그연출08스킵(self.ctx)


class 챕터10에필로그연출08스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출09(self.ctx)


class 챕터10에필로그연출09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__32$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 챕터10에필로그연출10(self.ctx)


class 챕터10에필로그연출10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000087_QD__52000087_TRIGGER__33$', time=5)
        self.set_onetime_effect(id=2010, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_04_00002010.xml')
        self.set_skip(state=챕터10에필로그연출10스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 챕터10에필로그연출10스킵(self.ctx)


class 챕터10에필로그연출10스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출11(self.ctx)


class 챕터10에필로그연출11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000087_QD__52000087_TRIGGER__34$', time=5)
        self.set_onetime_effect(id=2011, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_05_00002011.xml')
        self.set_skip(state=챕터10에필로그연출11스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 챕터10에필로그연출11스킵(self.ctx)


class 챕터10에필로그연출11스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출12(self.ctx)


class 챕터10에필로그연출12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__35$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출13(self.ctx)


class 챕터10에필로그연출13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__36$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출13_b(self.ctx)


class 챕터10에필로그연출13_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000087_QD__52000087_TRIGGER__37$', time=5)
        self.set_onetime_effect(id=2012, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_06_00002012.xml')
        self.set_skip(state=챕터10에필로그연출13b스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 챕터10에필로그연출13b스킵(self.ctx)


class 챕터10에필로그연출13b스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출14(self.ctx)


class 챕터10에필로그연출14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000087_QD__52000087_TRIGGER__38$', time=5)
        self.set_onetime_effect(id=2013, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_07_00002013.xml')
        self.set_skip(state=챕터10에필로그연출14스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출14스킵(self.ctx)


class 챕터10에필로그연출14스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출15(self.ctx)


class 챕터10에필로그연출15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000087_QD__52000087_TRIGGER__39$', time=6)
        self.set_onetime_effect(id=2014, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_08_00002014.xml')
        self.set_skip(state=챕터10에필로그연출15스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 챕터10에필로그연출15스킵(self.ctx)


class 챕터10에필로그연출15스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출16(self.ctx)


class 챕터10에필로그연출16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000087_QD__52000087_TRIGGER__40$', time=5)
        self.set_onetime_effect(id=2015, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_09_00002015.xml')
        self.set_skip(state=챕터10에필로그연출16스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 챕터10에필로그연출16스킵(self.ctx)


class 챕터10에필로그연출16스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 챕터10에필로그연출17(self.ctx)


class 챕터10에필로그연출17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 챕터10에필로그연출18(self.ctx)


class 챕터10에필로그연출18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__41$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출18b(self.ctx)


class 챕터10에필로그연출18b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__42$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출19(self.ctx)


class 챕터10에필로그연출19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__43$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출20(self.ctx)


class 챕터10에필로그연출20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__44$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출21(self.ctx)


class 챕터10에필로그연출21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__45$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 챕터10에필로그연출22(self.ctx)


class 챕터10에필로그연출22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2000025, portal_id=2)


initial_state = 대기
