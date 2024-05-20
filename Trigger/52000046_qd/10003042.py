""" trigger/52000046_qd/10003042.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002,2002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[10003042], quest_states=[2]):
            return 연출시작(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[2002])
        self.spawn_monster(spawn_ids=[2001], auto_target=False)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.add_buff(box_ids=[199], skill_id=70000095, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 자베스대사01(self.ctx)


class 자베스대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000046_QD__10003042__0$', time=3)
        self.set_skip(state=자베스대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 브라보대사01(self.ctx)


class 자베스대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 브라보대사01(self.ctx)


class 브라보대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000046_QD__10003042__1$', time=3)
        self.set_skip(state=브라보대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 제이시대사01(self.ctx)


class 브라보대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 제이시대사01(self.ctx)


class 제이시대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000515, script='$52000046_QD__10003042__2$', time=5)
        self.set_skip(state=제이시대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출종료(self.ctx)


class 제이시대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2001])
        self.spawn_monster(spawn_ids=[2002], auto_target=False)
        self.add_buff(box_ids=[199], skill_id=70000096, level=1)
        self.move_user(map_id=52000046, portal_id=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10):
            self.move_user_path(patrol_name='MS2PatrolData_9000')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
