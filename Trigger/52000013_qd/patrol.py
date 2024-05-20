""" trigger/52000013_qd/patrol.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_actor(trigger_id=6000, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 어린벨라등장(self.ctx)


class 어린벨라등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=1)
        self.spawn_monster(spawn_ids=[5000], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 어린벨라패트롤01(self.ctx)


class 어린벨라패트롤01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=5000, patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9001, spawn_ids=[5000]):
            return 어린벨라대화01(self.ctx)


class 어린벨라대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=3)
        self.set_dialogue(type=1, spawn_id=5000, script='$52000013_QD__MAIN__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 어린벨라패트롤02(self.ctx)


class 어린벨라패트롤02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=5000, patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9002, spawn_ids=[5000]):
            return 어린벨라대화02(self.ctx)


class 어린벨라대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=3)
        self.set_dialogue(type=1, spawn_id=5000, script='$52000013_QD__MAIN__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 어린벨라패트롤03(self.ctx)


class 어린벨라패트롤03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=5000, patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9003, spawn_ids=[5000]):
            return 카메라연출01(self.ctx)


class 카메라연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='12', seconds=6)
        self.select_camera_path(path_ids=[901], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9004, spawn_ids=[5000]):
            return 카메라연출02(self.ctx)


class 카메라연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='13', seconds=12)
        self.set_actor(trigger_id=6000, visible=True, initial_sequence='Idle_A')
        self.select_camera_path(path_ids=[902,903], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='13'):
            return 화면끄기(self.ctx)


class 화면끄기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='14', seconds=2)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 어린벨라소멸(self.ctx)


class 어린벨라소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=1)
        self.destroy_monster(spawn_ids=[5000])
        self.set_actor(trigger_id=6000, initial_sequence='Idle_A')
        self.spawn_monster(spawn_ids=[6001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 벨라연출01(self.ctx)


class 벨라연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='16', seconds=8)
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=6001, patrol_name='MS2PatrolData_2001')
        self.select_camera_path(path_ids=[904,905], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='16'):
            return 벨라연출종료(self.ctx)


class 벨라연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='17', seconds=8)
        self.select_camera(trigger_id=905, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='17'):
            return 이동딜레이(self.ctx)


class 이동딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10000], quest_ids=[10002611], quest_states=[3]):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='19', seconds=10)
        self.move_user(map_id=3009017, portal_id=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='19'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=10)
        self.destroy_monster(spawn_ids=[6001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 대기(self.ctx)


initial_state = 대기
