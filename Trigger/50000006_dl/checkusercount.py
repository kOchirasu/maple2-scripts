""" trigger/50000006_dl/checkusercount.xml """
import trigger_api


class CheckUserCount(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='DungeonRoomOpened', value=0)
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Interaction_vrmachine_A01_off')
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Interaction_vrmachine_A01_off')
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Interaction_vrmachine_A01_off')

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
        self.set_user_value(trigger_id=3, key='machineon', value=1)
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return DungeonStart01(self.ctx)


class DungeonStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='GuildRaid_Laboratory_DungeonOpen_01')
        self.show_guide_summary(entity_id=25100206, text_id=25100206, duration=3000)
        self.set_actor(trigger_id=4002, initial_sequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonRoomOpened') == 1:
            return DungeonStart02(self.ctx)


class DungeonStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2, key='machineon', value=1)
        self.set_user_value(trigger_id=4, key='machineon', value=1)
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Interaction_vrmachine_A01_on')
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return DungeonStart03(self.ctx)


class DungeonStart03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4001, initial_sequence='Interaction_vrmachine_A01_on')
        self.set_actor(trigger_id=4003, initial_sequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DungeonStart04(self.ctx)


class DungeonStart04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='GuildRaid_Laboratory_DungeonOpen_01')
        self.show_guide_summary(entity_id=25100206, text_id=25100206, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DungeonStart04(self.ctx)


# 던전 로비에서 생성할 던전 인원수가 부족하면 대기
class WaitDungeon01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25100204, text_id=25100204, duration=3000)

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
        self.show_guide_summary(entity_id=25100205, text_id=25100205, duration=3000)

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
        self.show_guide_summary(entity_id=25100204, text_id=25100204, duration=3000)

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
        self.show_guide_summary(entity_id=25100205, text_id=25100205, duration=3000)

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
        self.show_guide_summary(entity_id=25100204, text_id=25100204, duration=3000)

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
        self.show_guide_summary(entity_id=25100205, text_id=25100205, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return DungeonStart(self.ctx)


initial_state = CheckUserCount
