""" trigger/02000303_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3005])
        self.set_interact_object(trigger_ids=[13000008], state=2)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_interact_object(trigger_ids=[10000585], state=0)
        self.set_interact_object(trigger_ids=[10000575,10000576,10000577,10000578], state=1)
        self.spawn_monster(spawn_ids=[2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 연출시작딜레이(self.ctx)


class 연출시작딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=2, spawn_id=11000145, script='$02000303_BF__MAIN__0$', time=4)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007], auto_target=False)
        self.show_guide_summary(entity_id=20003031, text_id=20003031, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000575,10000576,10000577,10000578], state=0):
            return 또다른연출시작(self.ctx)


class 또다른연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.set_skip(state=또다른연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 연출이펙트(self.ctx)


class 연출이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3005], visible=True, fade=2.0)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_skip(state=또다른연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 카메라이동2(self.ctx)


class 카메라이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.set_skip(state=또다른연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return NPC대사(self.ctx)


class NPC대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001_A')
        self.set_dialogue(type=2, spawn_id=11000145, script='$02000303_BF__MAIN__1$', time=4)
        self.set_skip(state=또다른연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 또다른연출종료(self.ctx)


class 또다른연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2001])
        self.select_camera(trigger_id=302, enable=False)
        self.set_mesh(trigger_ids=[3005], visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        # self.set_interact_object(trigger_ids=[13000008], state=1)
        # self.create_item(spawn_ids=[9001], trigger_id=101)
        return 이동대기(self.ctx)


class 이동대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000585], state=1)
        self.show_guide_summary(entity_id=20002999, text_id=20002999)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000585], state=0):
            self.hide_guide_summary(entity_id=20002999)
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_timer(timer_id='4', seconds=4)
        self.show_count_ui(text='$02000303_BF__MAIN__3$', stage=1, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            self.move_user(map_id=2000299, portal_id=2, box_id=101)
            return 이동대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
