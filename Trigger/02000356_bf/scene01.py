""" trigger/02000356_bf/scene01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])
        self.set_effect(trigger_ids=[401])
        self.set_effect(trigger_ids=[601]) # 벨라 음성
        self.set_effect(trigger_ids=[602]) # 벨라 음성
        self.set_effect(trigger_ids=[603]) # 벨라 음성
        self.set_effect(trigger_ids=[604]) # 벨라 음성
        self.set_effect(trigger_ids=[605]) # 벨라 음성
        self.set_effect(trigger_ids=[606]) # 레논 음성
        self.set_effect(trigger_ids=[607]) # 알론 음성
        self.set_effect(trigger_ids=[608]) # 알론 음성
        self.set_effect(trigger_ids=[609]) # 알론 음성

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SetSkillA') == 1:
            return 연출시작딜레이(self.ctx)


class 연출시작딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 데보라크대사(self.ctx)


class 데보라크대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_dialogue(type=2, spawn_id=23000007, script='$02000213_BF__SCENE01__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 레논등장(self.ctx)


class 레논등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[203])
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 레논대사1(self.ctx)


class 레논대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_effect(trigger_ids=[606], visible=True) # 2.33
        self.set_dialogue(type=2, spawn_id=11000064, script='$02000213_BF__SCENE01__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라등장(self.ctx)


class 벨라등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202])
        self.set_effect(trigger_ids=[401], visible=True)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사1(self.ctx)


class 벨라대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[401])
        self.set_timer(timer_id='1', seconds=4)
        self.set_effect(trigger_ids=[601], visible=True) # 3.40
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000213_BF__SCENE01__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사2(self.ctx)


class 벨라대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.set_effect(trigger_ids=[602], visible=True) # 2.54
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000213_BF__SCENE01__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 알론등장(self.ctx)


class 알론등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[204])
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 알론대사1(self.ctx)


class 알론대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)
        self.set_effect(trigger_ids=[607], visible=True) # 3.68
        self.set_dialogue(type=2, spawn_id=11000076, script='$02000213_BF__SCENE01__4$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사3(self.ctx)


class 벨라대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)
        self.set_effect(trigger_ids=[603], visible=True) # 4.10
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000213_BF__SCENE01__5$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사4(self.ctx)


class 벨라대사4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)
        self.set_effect(trigger_ids=[604], visible=True) # 3.38
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000213_BF__SCENE01__6$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사5(self.ctx)


class 벨라대사5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_effect(trigger_ids=[605], visible=True) # 2.10
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000213_BF__SCENE01__7$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라사라짐이펙트(self.ctx)


class 벨라사라짐이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_effect(trigger_ids=[407], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라사라짐(self.ctx)


class 벨라사라짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(path_ids=[302])
        self.destroy_monster(spawn_ids=[202])
        self.destroy_monster(spawn_ids=[203])
        self.destroy_monster(spawn_ids=[204])
        self.spawn_monster(spawn_ids=[205])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 알론대사2(self.ctx)


class 알론대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)
        self.set_effect(trigger_ids=[608], visible=True) # 3.27
        self.set_dialogue(type=1, spawn_id=205, script='$02000213_BF__SCENE01__8$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 알론대사3(self.ctx)


class 알론대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)
        self.set_effect(trigger_ids=[609], visible=True) # 3.33
        self.set_dialogue(type=1, spawn_id=205, script='$02000213_BF__SCENE01__9$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301, enable=False)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    pass


initial_state = 시작대기중
