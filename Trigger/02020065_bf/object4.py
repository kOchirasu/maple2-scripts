""" trigger/02020065_bf/object4.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[714], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_4') == 1:
            return 터렛_활성화(self.ctx)


class 터렛_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[714], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_4') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[714]):
            return 터렛_비활성화(self.ctx)
        if self.monster_dead(spawn_ids=[801]):
            return 종료(self.ctx)


class 터렛_비활성화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_4') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[801]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[714], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_4') == 1:
            return 대기(self.ctx)


initial_state = 대기
