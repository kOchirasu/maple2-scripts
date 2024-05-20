""" trigger/02000243_bf/trigger_01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[705,706], visible=True)
        self.set_mesh(trigger_ids=[711,712])
        self.destroy_monster(spawn_ids=[601])
        self.set_effect(trigger_ids=[2004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=201) >= 1:
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[711,712], visible=True)
        self.spawn_monster(spawn_ids=[601], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601]):
            return 통과딜레이(self.ctx)


class 통과딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=999, type='trigger', achieve='GoldenTower2nd')
        self.set_achievement(trigger_id=999, type='trigger', achieve='ClearGoldentowerfirst')
        self.dungeon_clear()
        self.set_timer(timer_id='3', seconds=3)
        self.set_mesh(trigger_ids=[705,706])
        self.set_mesh(trigger_ids=[711,712])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2004], visible=True)
        self.set_timer(timer_id='1', seconds=180)


initial_state = 대기
