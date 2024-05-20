""" trigger/52000033_qd/audiencewithereb_03.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[60100245], quest_states=[2]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=end, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return pcmove(self.ctx)


class pcmove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return ErebTalk_01(self.ctx)


class ErebTalk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[700], return_view=False) # 에레브 얼굴로 클로즈업
        self.add_cinematic_talk(npc_id=11001663, illust_id='Ereb_normal', msg='$52000033_QD__AUDIENCEWITHEREB_03__0$', duration=3000, align=Align.Left) # 에레브

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ErebTalk_02(self.ctx)


class ErebTalk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[901], return_view=False) # 에레브 얼굴로 클로즈업
        self.add_cinematic_talk(npc_id=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_03__1$', duration=3000, align=Align.Left) # 에레브

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ErebTalk_03(self.ctx)


class ErebTalk_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[601], return_view=False) # 뒷 뷰

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return story_01(self.ctx)


class story_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000033_QD__AUDIENCEWITHEREB_03__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return story_02(self.ctx)


class story_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000033_QD__AUDIENCEWITHEREB_03__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return story_03(self.ctx)


class story_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000033_QD__AUDIENCEWITHEREB_03__4$')
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData_1005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ErebTalk_04(self.ctx)


class ErebTalk_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001663, illust_id='Ereb_surprise', msg='$52000033_QD__AUDIENCEWITHEREB_03__5$', duration=3000, align=Align.Left) # 에레브

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ErebTalk_05(self.ctx)


class ErebTalk_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001, enable=True)
        self.add_cinematic_talk(npc_id=11001663, illust_id='Ereb_closeEye', msg='$52000033_QD__AUDIENCEWITHEREB_03__6$', duration=3000, align=Align.Left) # 에레브
        self.add_balloon_talk(spawn_id=401, msg='$52000033_QD__AUDIENCEWITHEREB_03__7$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ErebTalk_06(self.ctx)


class ErebTalk_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001663, illust_id='Ereb_serious', msg='$52000033_QD__AUDIENCEWITHEREB_03__8$', duration=3000, align=Align.Left) # 에레브
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData_1006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ErebTalk_07(self.ctx)


class ErebTalk_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001663, illust_id='Ereb_closeEye', msg='$52000033_QD__AUDIENCEWITHEREB_03__9$', duration=3000, align=Align.Left) # 에레브
        self.destroy_monster(spawn_ids=[601])
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[601])
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
