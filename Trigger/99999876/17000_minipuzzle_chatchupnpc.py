""" trigger/99999876/17000_minipuzzle_chatchupnpc.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='ChangeNpc', value=0) # 17101 몬스터 AI에서 받는 신호
        self.destroy_monster(spawn_ids=[17101,17102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return SettingDelay(self.ctx)


class SettingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Setting(self.ctx)


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[17101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ChangeNpc') == 1:
            # 17101 몬스터 AI에서 받는 신호
            return ChatchUpNpc(self.ctx)


class ChatchUpNpc(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # UI 표시 안함 / NPC AI에서 스폰시킨 InteractObject 의 LifeTime
        self.set_timer(timer_id='1', seconds=30, auto_remove=True)
        # 동일 맵에 스포너가 있으면 대상 npc의 위치를 보정해서 교체되는 npc를 스폰 시켜줌
        self.change_monster(from_spawn_id=17101, to_spawn_id=17102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return ChatchUpNpc_Quit(self.ctx)


class ChatchUpNpc_Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='1')
        self.destroy_monster(spawn_ids=[17101,17102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Wait(self.ctx)


initial_state = Wait
