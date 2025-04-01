""" trigger/02020300_bf/bombcontrol.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='RandomBombEnd', value=0)
        self.start_combine_spawn(group_id=[516])
        self.start_combine_spawn(group_id=[517])
        self.start_combine_spawn(group_id=[518])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RandomBomb') == 1:
            return 포탑생성_1(self.ctx)


class 포탑생성_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[152]) # 몬스터 등장
        self.start_combine_spawn(group_id=[518], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[152]):
            return 포탑생성_2(self.ctx)


class 포탑생성_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[516], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 포탑생성_3(self.ctx)


class 포탑생성_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[517], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[151,152,153,154,155,156,157,158,159]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='RandomBombEnd', value=1)
        self.start_combine_spawn(group_id=[516])
        self.start_combine_spawn(group_id=[517])
        self.start_combine_spawn(group_id=[518])


initial_state = 대기
