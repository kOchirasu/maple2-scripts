""" trigger/50000013_dl/checkusercount.xml """
import trigger_api


class CheckUserCount(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 충족되면
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 부족하면
            return WaitDungeon01(self.ctx)


# 던전 최대 인원수가 충족되면
class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.show_guide_summary(entity_id=25100203, text_id=25100203)


# 던전 로비에서 생성할 던전 인원수가 부족하면 대기
class WaitDungeon01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25100201, text_id=25100201, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return WaitDungeon02(self.ctx)


class WaitDungeon02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 충족되면
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 부족하면
            return WaitDungeon03(self.ctx)


class WaitDungeon03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25100202, text_id=25100202, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return WaitDungeon04(self.ctx)


class WaitDungeon04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 충족되면
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 부족하면
            return WaitDungeon05(self.ctx)


class WaitDungeon05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25100201, text_id=25100201, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return WaitDungeon06(self.ctx)


class WaitDungeon06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 충족되면
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 부족하면
            return WaitDungeon07(self.ctx)


class WaitDungeon07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25100202, text_id=25100202, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return WaitDungeon08(self.ctx)


class WaitDungeon08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 충족되면
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 부족하면
            return WaitDungeon09(self.ctx)


class WaitDungeon09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25100201, text_id=25100201, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return WaitDungeon10(self.ctx)


class WaitDungeon10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 충족되면
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            # 던전 로비에서 생성할 던전 인원수가 부족하면
            return WaitDungeon11(self.ctx)


class WaitDungeon11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25100202, text_id=25100202, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DungeonStart(self.ctx)


initial_state = CheckUserCount
