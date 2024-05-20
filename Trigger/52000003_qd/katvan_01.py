""" trigger/52000003_qd/katvan_01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[100], quest_ids=[50001743], quest_states=[1]):
            return 카트반생성(self.ctx)


class 카트반생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102]) # 카트반

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작딜레이(self.ctx)


class 연출시작딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=101)
        self.set_timer(timer_id='1', seconds=1)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 대화시작(self.ctx)


class 대화시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True) # 2.33
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000003_QD__KATVAN_01__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카트반대사1(self.ctx)


class 카트반대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603], visible=True) # 2.33
        self.set_dialogue(type=2, spawn_id=11001024, script='$52000003_QD__KATVAN_01__1$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카트반대사2(self.ctx)


class 카트반대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True) # 2.33
        self.set_dialogue(type=2, spawn_id=11001024, script='$52000003_QD__KATVAN_01__2$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 레논대사1(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[102])


class 레논대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True) # 2.33
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000003_QD__KATVAN_01__3$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라원위치(self.ctx)


class 카메라원위치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=0.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라원위치_1(self.ctx)


class 카메라원위치_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 끝(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolation_time=0.5)
        self.destroy_monster(spawn_ids=[102]) # 카트반

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=100, type='trigger', achieve='Katvan')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 시작대기중
