""" trigger/02020020_bf/02020020_battle.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='battlesetting') == 1:
            return 전투_1라운드세팅(self.ctx)


class 전투_1라운드세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=24100101, illust='Neirin_normal', duration=5000, script='$02020020_BF__02020020_battle__0$')
        # self.side_npc_talk(npc_id=24100101, illust='Neirin_normal', duration=5000, script='$02020020_BF__02020020_battle__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_1라운드시작(self.ctx)


class 전투_1라운드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102]):
            return 전투_1라운드종료(self.ctx)


class 전투_1라운드종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_2라운드세팅(self.ctx)


class 전투_2라운드세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=24100101, illust='Neirin_normal', duration=5000, script='$02020020_BF__02020020_battle__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_2라운드시작(self.ctx)


class 전투_2라운드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103]):
            return 전투_2라운드종료(self.ctx)


class 전투_2라운드종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 전투_종료(self.ctx)


class 전투_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='battlesetting', value=2)
        self.side_npc_talk(npc_id=24100101, illust='Neirin_normal', duration=5000, script='$02020020_BF__02020020_battle__3$')


initial_state = 대기
