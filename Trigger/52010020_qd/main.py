""" trigger/52010020_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001])
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=4)
        self.spawn_monster(spawn_ids=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return Event_Ready(self.ctx)


class Event_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2001')
        self.set_dialogue(type=1, spawn_id=102, script='$52010020_QD__MAIN__0$', time=5)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2002')
        self.set_dialogue(type=1, spawn_id=101, script='$52010020_QD__MAIN__1$', time=5)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001], visible=True)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2004')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2001')
        self.move_user(map_id=52010020, portal_id=1, box_id=701)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_portal(portal_id=1)
        self.spawn_monster(spawn_ids=[103])
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2003')
        self.select_camera_path(path_ids=[8001,8002], return_view=False) # 사이드뷰 카메라
        # self.select_camera(trigger_id=8001)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001502, script='$52010020_QD__MAIN__2$', time=4)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2001')
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_05(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=4)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return end(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=701, type='trigger', achieve='luanDialogue')
        self.select_camera(trigger_id=8001, enable=False)
        self.move_user(map_id=52010019, portal_id=2, box_id=701)


class end(trigger_api.Trigger):
    pass


initial_state = idle
