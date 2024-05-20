""" trigger/52000124_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100105,60100106,60100107,60100108,60100109,60100110], quest_states=[2]):
            return ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100110], quest_states=[3]):
            return delnpc(self.ctx)


# 준비
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202]) # 연출용 카트반 (11003195)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return camera(self.ctx)


class camera(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4001, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_01(self.ctx)


# 이벤트 씬 시작
class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4002], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003195, msg='$52000124_QD__MAIN__0$', duration=2000, align=Align.Right)
        self.set_scene_skip(state=scene_07, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003195, msg='$52000124_QD__MAIN__1$', duration=2000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.add_cinematic_talk(npc_id=11000069, msg='$52000124_QD__MAIN__2$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_3001')
        self.add_cinematic_talk(npc_id=11003195, msg='$52000124_QD__MAIN__3$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Sit_down_A', duration=1000000000000.0)
        self.add_cinematic_talk(npc_id=11000069, msg='$52000124_QD__MAIN__4$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.add_cinematic_talk(npc_id=11003195, msg='$52000124_QD__MAIN__5$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201]) # 카트반(11003196)
        self.destroy_monster(spawn_ids=[202]) # 연출용 카트반(11003195)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100110], quest_states=[2]):
            return warptalk(self.ctx)


class warptalk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=201, msg='$52000124_QD__MAIN__6$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return warp(self.ctx)


class warp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000073, portal_id=4)


# delnpc
class delnpc(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201,202])


initial_state = idle
