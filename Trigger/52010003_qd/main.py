""" trigger/52010003_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.set_actor(trigger_id=2001, initial_sequence='Sit_Down_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002802], quest_states=[1]):
            return Event_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002836], quest_states=[1]):
            return B_Event_01(self.ctx)


class B_Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=2001, visible=True, initial_sequence='Sit_Down_A')
        self.select_camera(trigger_id=8001)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[103,104,105,106])
        self.set_timer(timer_id='4', seconds=4)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_1004')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_1005')
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_1006')
        # self.set_skip(state=Event_02_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return B_Event_02_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class B_Event_02_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return B_Event_02(self.ctx)


class B_Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010003_QD__MAIN__13$', time=5) # 에레브
        self.set_skip(state=B_Event_03_IDLE)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return B_Event_03_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class B_Event_03_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return B_Event_03(self.ctx)


class B_Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010003_QD__MAIN__14$', time=5) # 스타츠
        self.set_skip(state=B_Event_04_IDLE)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return B_Event_04_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class B_Event_04_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return B_Event_04(self.ctx)


class B_Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010003_QD__MAIN__15$', time=5) # 에레브
        self.set_skip(state=B_Event_05_IDLE)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return B_Event_05_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class B_Event_05_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return B_Event_05(self.ctx)


class B_Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001218, script='$52010003_QD__MAIN__16$', time=5) # 타라
        self.set_skip(state=B_Event_06_IDLE)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return B_Event_06_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class B_Event_06_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return B_Event_06(self.ctx)


class B_Event_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001217, script='$52010003_QD__MAIN__17$', time=5) # 둔바
        self.set_skip(state=B_Event_07_IDLE)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return B_Event_07_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class B_Event_07_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return B_Event_07(self.ctx)


class B_Event_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010003_QD__MAIN__18$', time=5) # 에레브
        self.set_skip(state=B_Event_08_IDLE)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return B_Event_08_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()
        self.select_camera(trigger_id=8001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.set_achievement(trigger_id=701, type='trigger', achieve='Hope_Lumieragon') # Hope_Lumieragon


class B_Event_08_IDLE(trigger_api.Trigger):
    pass


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8001)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[102])
        self.set_timer(timer_id='4', seconds=4)
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010003_QD__MAIN__0$', time=4)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_1002')
        self.set_skip(state=Event_02_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Event_02_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_02_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010003_QD__MAIN__1$', time=5)
        self.set_skip(state=Event_03_IDLE)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return Event_03_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_03_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010003_QD__MAIN__2$', time=4)
        self.set_skip(state=Event_04_IDLE)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Event_04_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_04_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010003_QD__MAIN__3$', time=4)
        self.set_timer(timer_id='4', seconds=4)
        self.set_skip(state=Event_05_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Event_05_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_05_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010003_QD__MAIN__4$', time=4)
        self.set_timer(timer_id='4', seconds=4)
        self.set_skip(state=Event_06_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Event_06_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_06_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Event_06(self.ctx)


class Event_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010003_QD__MAIN__5$', time=5)
        self.set_timer(timer_id='5', seconds=5)
        self.set_skip(state=Event_07_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return Event_07_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_07_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Event_07(self.ctx)


class Event_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010003_QD__MAIN__6$', time=4)
        self.set_timer(timer_id='3', seconds=3)
        self.set_skip(state=Event_08_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_08_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_08_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Event_08(self.ctx)


class Event_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010003_QD__MAIN__7$', time=4)
        self.set_timer(timer_id='4', seconds=4)
        self.set_skip(state=Event_09_IDLE)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Event_09_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_09_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Event_09(self.ctx)


class Event_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010003_QD__MAIN__8$', time=3)
        self.set_timer(timer_id='3', seconds=3)
        self.set_skip(state=Event_10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_10(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010003_QD__MAIN__9$', time=4)
        self.set_timer(timer_id='4', seconds=4)
        self.set_skip() # Missing State: Event_11

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return PlayMovie_01(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class PlayMovie_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='DestinyofMika.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return PlayMovie_02(self.ctx)


class PlayMovie_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='45', seconds=4)
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010003_QD__MAIN__10$', time=4)
        self.set_skip(state=Event_12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='45'):
            return Event_12(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010003_QD__MAIN__11$', time=3)
        self.set_timer(timer_id='3', seconds=3)
        self.set_skip(state=Event_13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_13(self.ctx)


class Event_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010003_QD__MAIN__12$', time=4)
        self.set_timer(timer_id='4', seconds=4)
        self.set_skip(state=Event_14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Event_14(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.select_camera(trigger_id=8001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class Event_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='MikaDestiny') # MikaDestiny
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[102]):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])


initial_state = idle
