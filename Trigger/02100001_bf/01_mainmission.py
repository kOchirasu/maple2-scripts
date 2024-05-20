""" trigger/02100001_bf/01_mainmission.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align

#include dungeon_common/checkuser10_guildraid.py
from dungeon_common.checkuser10_guildraid import *


# 아프렐라 오지
class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='10000') # Red
        self.set_interact_object(trigger_ids=[10001234], state=1) # Blue
        self.set_interact_object(trigger_ids=[10001235], state=1) # Grey
        self.set_interact_object(trigger_ids=[10001236], state=1) # Green
        self.set_interact_object(trigger_ids=[10001237], state=1) # Yellow
        self.set_interact_object(trigger_ids=[10001238], state=1) # 주민NPC
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108]) # 입구 포탈
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True) # 출구 포탈 Cage
        self.set_portal(portal_id=2) # 출구 포탈
        self.set_portal(portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102,103,104,105,106,107,108], auto_target=False) # 주민NPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 임시 테스트용 데이터 세팅 가능 지점 CheckUser10_GuildRaid / DungeonStart / DoorOpen / TimmerStart
            return CheckUser10_GuildRaid(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=903)
        self.set_cinematic_intro()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ShowCaption01(self.ctx)


# 설명문 출력
class ShowCaption01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_intro(text='$02100001_BF__01_MAINMISSION__0$')
        self.set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return ShowCaption01Skip(self.ctx)


class ShowCaption01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ShowCaption02(self.ctx)


class ShowCaption02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_intro(text='$02100001_BF__01_MAINMISSION__1$')
        self.set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return ShowCaption02Skip(self.ctx)


class ShowCaption02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return CloseCaptionSetting(self.ctx)


class CloseCaptionSetting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.close_cinematic()
        self.select_camera(trigger_id=903, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DoorOpen(self.ctx)


class DoorOpen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99, key='CageDoorOpen', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TalkStart(self.ctx)


class TalkStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CinematicTalk01(self.ctx)


class CinematicTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003512, msg='$02100001_BF__01_MAINMISSION__2$', duration=5000, align=Align.Center, illust_id='0')
        self.set_skip(state=CinematicTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CinematicTalk01Skip(self.ctx)


class CinematicTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CinematicTalk02(self.ctx)


class CinematicTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003512, msg='$02100001_BF__01_MAINMISSION__3$', duration=5000, align=Align.Center, illust_id='0')
        self.set_skip(state=CinematicTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CinematicTalk02Skip(self.ctx)


class CinematicTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return TalkEnd(self.ctx)


class TalkEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=900, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return TimmerStart(self.ctx)


class TimmerStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99, key='MissionStart', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01') # 제한 시간 5분
        self.set_timer(timer_id='10000', seconds=300, start_delay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        """
        all_of:  Red
        all_of:  Blue
        all_of:  Grey
        all_of:  Green
        all_of:  Yellow
        """
        if self.object_interacted(interact_ids=[10001234], state=0) and self.object_interacted(interact_ids=[10001235], state=0) and self.object_interacted(interact_ids=[10001236], state=0) and self.object_interacted(interact_ids=[10001237], state=0) and self.object_interacted(interact_ids=[10001238], state=0):
            return MissionComplete(self.ctx)
        if self.time_expired(timer_id='10000'):
            return MissionFail(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=5, key='GiveBuffSlowly', value=2)


class MissionFail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='10000')
        self.set_portal(portal_id=1) # 입구 포탈
        self.set_event_ui(type=5, arg2='$02100001_BF__01_MAINMISSION__4$', arg3='3000')
        self.set_interact_object(trigger_ids=[10001234], state=2) # Red
        self.set_interact_object(trigger_ids=[10001235], state=2) # Blue
        self.set_interact_object(trigger_ids=[10001236], state=2) # Grey
        self.set_interact_object(trigger_ids=[10001237], state=2) # Green
        self.set_interact_object(trigger_ids=[10001238], state=2) # Yellow

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MoveToCage(self.ctx)


class MoveToCage(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2100001, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BadEndingStart(self.ctx)


# BadEnding 연출
class BadEndingStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=901)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BadEndingTalk01(self.ctx)


class BadEndingTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003517, msg='$02100001_BF__01_MAINMISSION__5$', duration=5000, align=Align.Center, illust_id='0')
        self.set_skip(state=BadEndingTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return BadEndingTalk01Skip(self.ctx)


class BadEndingTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return BadEndingEnd(self.ctx)


class BadEndingEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=901, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DungeonFail(self.ctx)


# 던전 실패 선언
class DungeonFail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_fail()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BadEndingPortalOn(self.ctx)


class BadEndingPortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True) # 출구 포탈 Cage

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class MissionComplete(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='10000')
        self.set_portal(portal_id=1) # 입구 포탈
        self.set_achievement(trigger_id=9902, type='trigger', achieve='Find02100001')
        self.set_achievement(trigger_id=9902, type='trigger', achieve='guildraid_clear_1') # CN 스탬프 이벤트 전용
        self.set_event_ui(type=7, arg2='$02100001_BF__01_MAINMISSION__6$', arg3='3000')
        self.set_user_value(trigger_id=99, key='MissionComplete', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return HappyEndingStart(self.ctx)


# HappyEnding 연출
class HappyEndingStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=902)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return HappyEndingTalk01(self.ctx)


class HappyEndingTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003512, msg='$02100001_BF__01_MAINMISSION__7$', duration=5000, align=Align.Center, illust_id='0')
        self.set_skip(state=HappyEndingTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return HappyEndingTalk01Skip(self.ctx)


class HappyEndingTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return HappyEndingEnd(self.ctx)


class HappyEndingEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=902, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DungeonSuccess(self.ctx)


# 던전 클리어 선언
class DungeonSuccess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return HappyEndingPortalOn(self.ctx)


class HappyEndingPortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True) # 출구 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
