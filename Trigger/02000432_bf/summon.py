""" trigger/02000432_bf/summon.xml """
import trigger_api


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 소환(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=죽음대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 죽음대기(self.ctx)


class 죽음대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 셀린사망(self.ctx)
        if self.monster_dead(spawn_ids=[2002]):
            return 피리스사망(self.ctx)


class 셀린사망(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2002, script='$02000432_BF__SUMMON__1$', time=4)
        self.add_buff(box_ids=[2002], skill_id=40500011, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2002]):
            self.set_achievement(trigger_id=199, type='trigger', achieve='SirenDualKill')
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 피리스사망(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_achievement(trigger_id=199, type='trigger', achieve='BigSisterFirst')
        self.set_dialogue(type=1, spawn_id=2001, script='$02000432_BF__SUMMON__0$', time=4)
        self.add_buff(box_ids=[2001], skill_id=40500011, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            self.set_achievement(trigger_id=199, type='trigger', achieve='SirenDualKill')
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 룸체크
