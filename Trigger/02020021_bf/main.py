""" trigger/02020021_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9001], visible=True)
        self.set_agent(trigger_ids=[9002], visible=True)
        self.set_agent(trigger_ids=[9003], visible=True)
        self.set_agent(trigger_ids=[9004], visible=True)
        self.set_agent(trigger_ids=[9005], visible=True)
        self.set_agent(trigger_ids=[9006], visible=True)
        self.set_agent(trigger_ids=[9007], visible=True)
        self.set_agent(trigger_ids=[9008], visible=True)
        self.set_user_value(trigger_id=99990002, key='battlesetting', value=0)
        self.set_user_value(trigger_id=99990003, key='Timer', value=0)
        self.set_user_value(trigger_id=99990004, key='SpecialTimer', value=0)
        self.set_user_value(trigger_id=99990002, key='SpecialTimer', value=0)
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라_캡션(self.ctx)


class 카메라_캡션(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[501,502], return_view=False)
        self.show_caption(type='VerticalCaption', title='$02020021_BF__main__3$', desc='$02020021_BF__main__4$', align=Align.centerLeft, duration=4000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_샤텐대사1(self.ctx)


class 카메라_샤텐대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[503,504], return_view=False)
        self.add_cinematic_talk(npc_id=23200085, illust_id='Schatten_normal', msg='$02020021_BF__main__0$', duration=4000, align=Align.left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_샤텐대사2(self.ctx)


class 카메라_샤텐대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=23200085, illust_id='Schatten_normal', msg='$02020021_BF__main__1$', duration=4000, align=Align.left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_샤텐대사3(self.ctx)


class 카메라_샤텐대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[505,506], return_view=False)
        self.add_cinematic_talk(npc_id=23200085, illust_id='Schatten_normal', msg='$02020021_BF__main__2$', duration=4000, align=Align.left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_샤텐대사4(self.ctx)


class 카메라_샤텐대사4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[507,508], return_view=False)
        self.add_cinematic_talk(npc_id=23200085, illust_id='Schatten_normal', msg='$02020021_BF__main__5$', duration=4000, align=Align.left)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0.1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=901, spawn_ids=[201]) and self.wait_tick(wait_tick=2000):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9001])
        self.set_agent(trigger_ids=[9002])
        self.set_agent(trigger_ids=[9003])
        self.set_agent(trigger_ids=[9004])
        self.set_agent(trigger_ids=[9005])
        self.set_agent(trigger_ids=[9006])
        self.set_agent(trigger_ids=[9007])
        self.set_agent(trigger_ids=[9008])
        self.set_ai_extra_data(key='Start', value=1)
        self.side_npc_talk(npc_id=23200085, illust='Schatten_smile', duration=5000, script='$02020021_BF__main__6$', voice='ko/Npc/00002248')
        self.set_user_value(trigger_id=99990002, key='battlesetting', value=1)
        # self.set_user_value(trigger_id=99990003, key='Timer', value=1)
        # self.set_user_value(trigger_id=99990004, key='SpecialTimer', value=1)
        # self.set_user_value(trigger_id=99990002, key='SpecialTimer', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End') == 1:
            return 랭크체크대사(self.ctx)


class 랭크체크대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_first_user_mission_score() >= 1500:
            self.side_npc_talk(npc_id=23200085, illust='Schatten_smile', duration=5000, script='$02020021_BF__main__7$', voice='ko/Npc/00002082')
            return 던전종료_A랭크이상(self.ctx)
        if self.dungeon_first_user_mission_score() < 1500:
            self.side_npc_talk(npc_id=23200085, illust='Schatten_serious', duration=5000, script='$02020021_BF__main__8$', voice='ko/Npc/00002081')
            return 던전종료_A랭크미만(self.ctx)


class 던전종료_A랭크이상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()


class 던전종료_A랭크미만(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_fail()


initial_state = 입장
