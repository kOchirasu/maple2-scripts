""" trigger/02010055_bf/scene01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[699])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 바르칸트대사(self.ctx)


class 바르칸트대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.set_effect(trigger_ids=[699], visible=True)
        self.set_dialogue(type=2, spawn_id=23000068, script='$02010055_BF__SCENE01__0$', time=4)
        self.set_skip(state=바르칸트대사2스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 바르칸트대사2(self.ctx)


class 바르칸트대사2스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 바르칸트대사2(self.ctx)


class 바르칸트대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.set_effect(trigger_ids=[699], visible=True)
        self.set_dialogue(type=2, spawn_id=23000068, script='$02010055_BF__SCENE01__1$', time=4)
        self.set_skip(state=종료준비)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 종료(self.ctx)


class 종료준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 시작대기중
