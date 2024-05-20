""" trigger/02000254_bf/elite.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[801])
        self.set_ladder(trigger_ids=[802])
        self.set_ladder(trigger_ids=[803])
        self.set_ladder(trigger_ids=[804])
        self.set_ladder(trigger_ids=[805])
        self.set_ladder(trigger_ids=[806])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[903]):
            return 딜레이1(self.ctx)


class 딜레이1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 탄2(self.ctx)
        if self.monster_dead(spawn_ids=[106]):
            return 클리어딜레이(self.ctx)


class 탄2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[103])
        self.spawn_monster(spawn_ids=[104])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 탄3(self.ctx)
        if self.monster_dead(spawn_ids=[106]):
            return 클리어딜레이(self.ctx)


class 탄3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104])
        self.spawn_monster(spawn_ids=[105])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 탄4(self.ctx)
        if self.monster_dead(spawn_ids=[106]):
            return 클리어딜레이(self.ctx)


class 탄4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[104])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 탄5(self.ctx)
        if self.monster_dead(spawn_ids=[106]):
            return 클리어딜레이(self.ctx)


class 탄5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104])
        self.spawn_monster(spawn_ids=[103])
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 탄2(self.ctx)
        if self.monster_dead(spawn_ids=[106]):
            return 클리어딜레이(self.ctx)


class 클리어딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 클리어(self.ctx)


class 클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 클리어2(self.ctx)


class 클리어2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=14)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000254_BF__ELITE__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 클리어3(self.ctx)


class 클리어3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])
        self.destroy_monster(spawn_ids=[105])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # self.set_event_ui(type=7, arg2='$02000254_BF__ELITE__1$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 사다리생성(self.ctx)


class 사다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[801], visible=True, enable=True)
        self.set_ladder(trigger_ids=[802], visible=True, enable=True)
        self.set_ladder(trigger_ids=[803], visible=True, enable=True)
        self.set_ladder(trigger_ids=[804], visible=True, enable=True)
        self.set_ladder(trigger_ids=[805], visible=True, enable=True)
        self.set_ladder(trigger_ids=[806], visible=True, enable=True)
        self.dungeon_clear()
        self.hide_guide_summary(entity_id=20002524)


initial_state = 시작대기중
