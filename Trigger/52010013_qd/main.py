""" trigger/52010013_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002797], quest_states=[1]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8001)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[104])
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=2, spawn_id=11001217, script='$52010013_QD__MAIN__0$', time=3)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_02_IDLE(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_02_IDLE(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8002)
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010013_QD__MAIN__1$', time=5)
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
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010013_QD__MAIN__2$', time=4)
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
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010013_QD__MAIN__3$', time=4)
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
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010013_QD__MAIN__4$', time=4)
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
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010013_QD__MAIN__5$', time=5)
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
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010013_QD__MAIN__6$', time=4)
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
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010013_QD__MAIN__7$', time=4)
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
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010013_QD__MAIN__8$', time=3)
        self.set_timer(timer_id='3', seconds=3)
        self.set_skip(state=Event_10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_10(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Event_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010013_QD__MAIN__9$', time=4)
        self.set_timer(timer_id='4', seconds=4)
        self.set_skip(state=End)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return End(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.select_camera(trigger_id=8001, enable=False)
        self.select_camera(trigger_id=8002, enable=False)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='DragonMika')
        self.move_user(map_id=2010002, portal_id=13, box_id=701)


initial_state = idle
