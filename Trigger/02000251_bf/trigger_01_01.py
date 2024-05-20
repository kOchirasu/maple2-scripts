""" trigger/02000251_bf/trigger_01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[705,706], visible=True)
        self.set_mesh(trigger_ids=[711,712])
        self.destroy_monster(spawn_ids=[601,602,603,604])
        self.set_effect(trigger_ids=[3004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=201) >= 1:
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[711,712], visible=True)
        self.spawn_monster(spawn_ids=[601,602,603,604], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,602,603,604]):
            return 통과딜레이(self.ctx)


class 통과딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        # self.set_event_ui(type=7, arg2='$02000251_BF__TRIGGER_01_01__0$', arg3='3000', arg4='0')
        self.set_achievement(trigger_id=1000, type='trigger', achieve='goldenTower')
        # self.create_item(spawn_ids=[9001], trigger_id=998)
        self.dungeon_clear()
        self.set_mesh(trigger_ids=[705,706])
        self.set_mesh(trigger_ids=[711,712])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[3004], visible=True)


initial_state = 대기
