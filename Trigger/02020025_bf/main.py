""" trigger/02020025_bf/main.xml """
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
        self.destroy_monster(spawn_ids=[-1])
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=3)
        self.set_user_value(trigger_id=99990004, key='Timer', value=0) # <일반 5분 타이머>
        self.set_user_value(trigger_id=99990006, key='SpecialTimer', value=0) # <3분내 클리어 특별 타이머>
        self.set_user_value(trigger_id=99990002, key='battlesetting', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.move_user(map_id=2020025, portal_id=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라_캡션(self.ctx)


class 카메라_캡션(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[5001,5002])
        self.show_caption(type='VerticalCaption', title='$02020025_BF__main__3$', desc='$02020025_BF__main__4$', align=Align.centerLeft, duration=5000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 유저연출(self.ctx)


class 유저연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202])
        self.set_dialogue(type=1, script='$02020025_BF__main__5$', time=5)
        self.select_camera(trigger_id=503)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_콘대르설명1(self.ctx)


class 카메라_콘대르설명1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Talk_B', duration=18430.0)
        self.add_cinematic_talk(npc_id=24110001, msg='$02020025_BF__main__0$', duration=4000, align=Align.left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 유저연출_2(self.ctx)


class 유저연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$02020025_BF__main__6$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 유저연출_3(self.ctx)


class 유저연출_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=504)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라_콘대르설명2(self.ctx)


class 카메라_콘대르설명2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=24110001, illust_id='Conder_normal', msg='$02020025_BF__main__1$', duration=4000, align=Align.left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_콘대르설명3(self.ctx)


class 카메라_콘대르설명3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=24110001, illust_id='Conder_normal', msg='$02020025_BF__main__2$', duration=4000, align=Align.left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_콘대르설명4(self.ctx)


class 카메라_콘대르설명4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=24110001, illust_id='Conder_normal', msg='$02020025_BF__main__7$', duration=4000, align=Align.left)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0.1)
        self.destroy_monster(spawn_ids=[202])

    def on_tick(self) -> trigger_api.Trigger:
        return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=False, delay=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=902, spawn_ids=[201]) and self.wait_tick(wait_tick=2000):
            return 전투_진행(self.ctx)


class 전투_진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9001])
        self.set_agent(trigger_ids=[9002])
        self.set_agent(trigger_ids=[9003])
        self.set_agent(trigger_ids=[9004])
        self.set_agent(trigger_ids=[9005])
        self.set_agent(trigger_ids=[9006])
        self.set_agent(trigger_ids=[9007])
        self.set_agent(trigger_ids=[9008])
        self.set_user_value(trigger_id=99990002, key='battlesetting', value=1)
        # self.set_user_value(trigger_id=99990004, key='Timer', value=1)
        # self.set_user_value(trigger_id=99990002, key='SpecialTimer', value=1)
        # self.set_user_value(trigger_id=99990006, key='SpecialTimer', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End') == 1:
            return 랭크체크대사(self.ctx)


class 랭크체크대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_first_user_mission_score() >= 1500:
            self.side_npc_talk(npc_id=24110001, illust='Conder_normal', duration=5000, script='$02020025_BF__main__8$', voice='ko/Npc/00002146')
            return 던전종료_A랭크이상(self.ctx)
        if self.dungeon_first_user_mission_score() < 1500:
            self.side_npc_talk(npc_id=24110001, illust='Conder_smile', duration=5000, script='$02020025_BF__main__9$', voice='ko/Npc/00002145')
            return 던전종료_A랭크미만(self.ctx)


class 던전종료_A랭크이상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])
        self.dungeon_clear()


class 던전종료_A랭크미만(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])
        self.dungeon_fail()


initial_state = 입장
