""" trigger/02000177_bf/wait.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_max_user_count() == 4:
            # 던전 최대 인원수가 4이면
            return MaxCount04_Wait01(self.ctx)
        if self.dungeon_max_user_count() == 3:
            # 던전 최대 인원수가 3이면
            return MaxCount03_Wait01(self.ctx)
        if self.dungeon_max_user_count() == 2:
            # 던전 최대 인원수가 2이면
            return MaxCount02_Wait01(self.ctx)
        if self.dungeon_max_user_count() == 1:
            # 던전 최대 인원수가 1이면
            return MaxCount01_Wait01(self.ctx)


# 던전 최대 인원수가 4이면
class MaxCount04_Wait01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 4:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return MaxCount04_Wait02(self.ctx)


class MaxCount04_Wait02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 4:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return MaxCount04_Wait03(self.ctx)


class MaxCount04_Wait03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 4:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return MaxCount04_Wait04(self.ctx)


class MaxCount04_Wait04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 4:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return DungeonStart(self.ctx)


# 던전 최대 인원수가 3이면
class MaxCount03_Wait01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 3:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return MaxCount03_Wait02(self.ctx)


class MaxCount03_Wait02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 3:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return MaxCount03_Wait03(self.ctx)


class MaxCount03_Wait03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 3:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return MaxCount03_Wait04(self.ctx)


class MaxCount03_Wait04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 3:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return DungeonStart(self.ctx)


# 던전 최대 인원수가 2이면
class MaxCount02_Wait01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 2:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return MaxCount02_Wait02(self.ctx)


class MaxCount02_Wait02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 2:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return MaxCount02_Wait03(self.ctx)


class MaxCount02_Wait03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 2:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return MaxCount02_Wait04(self.ctx)


class MaxCount02_Wait04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=40012, text_id=40012, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 2:
            return DungeonStart(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return DungeonStart(self.ctx)


# 던전 최대 인원수가 1이면 바로 시작
class MaxCount01_Wait01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DungeonStart(self.ctx)


initial_state = Wait
