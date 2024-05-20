""" trigger/52000006_qd/tutorial_06_1.xml """
import trigger_api


class 엔터대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 연출세팅(self.ctx)


class 연출세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return PC대사1(self.ctx)


class PC대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_1__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 양등장(self.ctx)


class 양등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_1__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 양이동(self.ctx)


class 양이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)
        self.move_npc(spawn_id=201, patrol_name='PatrolData_Sheep_01')
        self.set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_1__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])
        self.select_camera(trigger_id=302, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 엔터대기중
