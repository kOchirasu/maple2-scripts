""" trigger/52000056_qd/50001460.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[606])
        self.set_effect(trigger_ids=[607])
        self.set_effect(trigger_ids=[608])
        self.set_effect(trigger_ids=[609])
        self.set_effect(trigger_ids=[610])
        self.set_effect(trigger_ids=[611])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008], visible=True)
        self.set_gravity(gravity=-9.8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103,104,105,106]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000056, portal_id=3)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC말풍선01(self.ctx)


class PC말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000056_QD__50001460__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 낙하준비(self.ctx)


class 낙하준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008], interval=200, fade=2.0)
        self.set_gravity(gravity=-37.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 낙하시작(self.ctx)


class 낙하시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 낙하종료(self.ctx)


class 낙하종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC말풍선02(self.ctx)


class PC말풍선02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000056_QD__50001460__1$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PC말풍선03(self.ctx)


class PC말풍선03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000056_QD__50001460__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_effect(trigger_ids=[601], visible=True)
            self.set_effect(trigger_ids=[602], visible=True)
            self.set_effect(trigger_ids=[603], visible=True)
            self.set_effect(trigger_ids=[604], visible=True)
            self.set_effect(trigger_ids=[605], visible=True)
            self.set_effect(trigger_ids=[606], visible=True)
            self.set_effect(trigger_ids=[607], visible=True)
            self.set_effect(trigger_ids=[608], visible=True)
            self.set_effect(trigger_ids=[609], visible=True)
            self.set_effect(trigger_ids=[610], visible=True)
            self.set_effect(trigger_ids=[611], visible=True)
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            self.set_gravity(gravity=-9.8)
            return 이펙트종료대기(self.ctx)


class 이펙트종료대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            self.set_effect(trigger_ids=[601])
            self.set_effect(trigger_ids=[602])
            self.set_effect(trigger_ids=[603])
            self.set_effect(trigger_ids=[604])
            self.set_effect(trigger_ids=[605])
            self.set_effect(trigger_ids=[606])
            self.set_effect(trigger_ids=[607])
            self.set_effect(trigger_ids=[608])
            self.set_effect(trigger_ids=[609])
            self.set_effect(trigger_ids=[610])
            self.set_effect(trigger_ids=[611])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
