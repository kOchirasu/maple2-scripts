""" trigger/dungeon_common/checkuser10_guildraid.xml """
import trigger_api


class CheckUser10_GuildRaid(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30, start_delay=1) # 최대 30초 대기

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9900) >= 10:
            return MaxCount10_Start(self.ctx)
        if self.count_users(box_id=9900) < 10:
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9900) >= 10:
            # 10명이면 바로 시작
            return MaxCount10_Start(self.ctx)
        if self.time_expired(timer_id='1'):
            return MaxCount10_Start(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 최대 30초 대기 타이머 초기화
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        return DungeonStart(self.ctx)


