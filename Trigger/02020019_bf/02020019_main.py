""" trigger/02020019_bf/02020019_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.move_user(map_id=2020019, portal_id=1)
        self.set_user_value(trigger_id=99990002, key='battlesetting', value=0)
        self.set_user_value(trigger_id=99990004, key='Timer', value=0)
        self.set_user_value(trigger_id=99990005, key='SpecialTimer', value=0)
        self.set_user_value(trigger_id=99990002, key='SpecialTimer', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.move_user(map_id=2020019, portal_id=1)
        self.spawn_monster(spawn_ids=[101,102,103], auto_target=False) # <네이린과 대포 스폰(아군)>
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라_캡션(self.ctx)


class 카메라_캡션(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[501,502], return_view=False)
        self.show_caption(type='VerticalCaption', title='$02020019_BF__02020019_main__3$', desc='$02020019_BF__02020019_main__4$', align=Align.centerLeft, duration=4000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_네이린설명1(self.ctx)


class 카메라_네이린설명1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=503)
        self.add_cinematic_talk(npc_id=24100001, illust_id='Neirin_normal', msg='$02020019_BF__02020019_main__0$', duration=4000, align=Align.left)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=6300.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_네이린설명2(self.ctx)


class 카메라_네이린설명2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=24100001, illust_id='Neirin_normal', msg='$02020019_BF__02020019_main__1$', duration=4000, align=Align.left)
        # self.add_cinematic_talk(npc_id=24100001, illust_id='Neirin_normal', msg='$02020019_BF__02020019_main__2$', duration=4000, align=Align.left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_네이린설명3(self.ctx)


class 카메라_네이린설명3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=24100001, illust_id='Neirin_normal', msg='$02020019_BF__02020019_main__5$', duration=4000, align=Align.left)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0.1)

    def on_tick(self) -> trigger_api.Trigger:
        return 전투_대기(self.ctx)


class 전투_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 전투_진행(self.ctx)


class 전투_진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990002, key='battlesetting', value=1)
        # self.set_user_value(trigger_id=99990004, key='Timer', value=1)
        # self.set_user_value(trigger_id=99990005, key='SpecialTimer', value=1)
        # self.set_user_value(trigger_id=99990002, key='SpecialTimer', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End') >= 1:
            return 랭크체크대사(self.ctx)


class 랭크체크대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_first_user_mission_score() >= 1500:
            self.side_npc_talk(npc_id=24100001, illust='Neirin_surprise', duration=5000, script='$02020019_BF__02020019_main__6$', voice='ko/Npc/00002125')
            return 던전종료_A랭크이상(self.ctx)
        if self.dungeon_first_user_mission_score() < 1500:
            self.side_npc_talk(npc_id=24100001, illust='Neirin_smile', duration=5000, script='$02020019_BF__02020019_main__7$', voice='ko/Npc/00002124')
            return 던전종료_A랭크미만(self.ctx)


class 던전종료_A랭크이상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()


class 던전종료_A랭크미만(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_fail()


initial_state = 입장
