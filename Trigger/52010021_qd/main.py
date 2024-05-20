""" trigger/52010021_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001])
        self.spawn_monster(spawn_ids=[101,102,103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002540], quest_states=[3]):
            return Event_01_Idle(self.ctx)


class Event_01_Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52010021, portal_id=3, box_id=701)
        self.set_timer(timer_id='2', seconds=2)
        self.set_effect(trigger_ids=[7001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.spawn_monster(spawn_ids=[104])
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2002')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2004')
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2003')
        self.select_camera(trigger_id=8001)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Event_05(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(trigger_id=8001)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010021_QD__MAIN__0$', time=4)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return Ending(self.ctx)


class Ending(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001,8002], return_view=False) # 사이드뷰 카메라
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2012')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2014')
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2013')
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return out(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=4)


class out(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return end(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=9, script='$52010021_QD__MAIN__1$', arg3=True)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return real_end2(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=9, script='$52010021_QD__MAIN__2$', arg3=True)
        self.play_system_sound_in_box(sound='System_Laugh_01')


class real_end2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return real_end3(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=9, script='$52010021_QD__MAIN__3$', arg3=True)


class real_end3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return real_end4(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_Burp_01')


class real_end4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return real_end(self.ctx)


class real_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='mikaEpilogueEnd')
        self.move_user(map_id=2010002, portal_id=1, box_id=701)


initial_state = idle
