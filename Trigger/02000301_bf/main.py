""" trigger/02000301_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000585], state=0)
        self.set_interact_object(trigger_ids=[11000004], state=2)
        self.set_interact_object(trigger_ids=[13000006], state=2)
        self.set_effect(trigger_ids=[604])
        self.spawn_monster(spawn_ids=[1007,1008], auto_target=False)
        self.spawn_monster(spawn_ids=[2099], auto_target=False)
        self.set_mesh(trigger_ids=[4998,4999], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 연출시작딜레이(self.ctx)


class 연출시작딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.set_timer(timer_id='3', seconds=3)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 트리스탄01(self.ctx)


class 트리스탄01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=2, spawn_id=11000252, script='$02000301_BF__MAIN__0$', time=4)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        return 몬스터전투(self.ctx)


class 몬스터전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[1007,1008]):
            return 골두스이동(self.ctx)


class 골두스이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2099, patrol_name='MS2PatrolData_2098')
        self.set_dialogue(type=1, spawn_id=2099, script='$02000301_BF__MAIN__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1007,1008]):
            return 또다른연출시작(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[4998,4999])


class 또다른연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='1', seconds=1)
        self.set_skip(state=또다른연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 골두스마무리(self.ctx)


class 골두스마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=2, spawn_id=11000252, script='$02000301_BF__MAIN__2$', time=4)
        self.set_skip(state=또다른연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 또다른연출종료(self.ctx)


class 또다른연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        # self.set_interact_object(trigger_ids=[13000006], state=1)
        # self.create_item(spawn_ids=[9001], trigger_id=199)
        return 이동대기(self.ctx)


class 이동대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000585], state=1)
        self.show_guide_summary(entity_id=20002999, text_id=20002999)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.move_npc(spawn_id=2099, patrol_name='MS2PatrolData_2099')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000585], state=0):
            self.hide_guide_summary(entity_id=20002999)
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_timer(timer_id='4', seconds=4)
        self.show_count_ui(text='$02000301_BF__MAIN__4$', stage=1, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            self.move_user(map_id=2000299, portal_id=2, box_id=199)
            return 이동대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
