""" trigger/52000033_qd/audiencewithereb_02.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[60100010], quest_states=[1]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000033, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return pcmove(self.ctx)


class pcmove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1) # 보험용
        self.set_cinematic_ui(type=3) # 보험용
        self.move_user_path(patrol_name='MS2PatrolData_1004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ErebTalk_01(self.ctx)


class ErebTalk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[700], return_view=False) # 에레브 얼굴로 클로즈업
        self.add_cinematic_talk(npc_id=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__0$', duration=5000)
        self.set_scene_skip(state=end, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ErebTalk_02(self.ctx)


class ErebTalk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[901], return_view=False) # 에레브 얼굴로 클로즈업
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__1$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Erebintroduce(self.ctx)


class Erebintroduce(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(scale=2.3, type='NameCaption', title='$52000033_QD__AUDIENCEWITHEREB_02__18$', desc='$52000033_QD__AUDIENCEWITHEREB_02__19$', align=Align.Center | Align.Left, offset_rate_x=-0.15, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ErebTalk_03(self.ctx)


class ErebTalk_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__2$', duration=3000)
        self.add_cinematic_talk(npc_id=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Kaltalk_01(self.ctx)


class Kaltalk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001665, msg='$52000033_QD__AUDIENCEWITHEREB_02__4$', duration=3000, illust_id='Karl_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Kaltalk_02(self.ctx)


class Kaltalk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[902], return_view=False) # 칼 얼굴로 클로즈업
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11001665, msg='$52000033_QD__AUDIENCEWITHEREB_02__5$', duration=3000)
        self.add_cinematic_talk(npc_id=11001665, msg='$52000033_QD__AUDIENCEWITHEREB_02__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return kaltroduce(self.ctx)


class kaltroduce(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(scale=2.3, type='NameCaption', title='$52000033_QD__AUDIENCEWITHEREB_02__20$', desc='$52000033_QD__AUDIENCEWITHEREB_02__21$', align=Align.Center | Align.Left, offset_rate_x=-0.15, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return talk_01(self.ctx)


class talk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[601], return_view=False) # 뒷 뷰
        self.add_cinematic_talk(npc_id=11001663, illust_id='Ereb_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__7$', duration=1000, align=Align.Left) # 에레브
        self.add_cinematic_talk(npc_id=11001665, illust_id='Karl_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__8$', duration=3000, align=Align.Right) # 칼

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return talk_02(self.ctx)


class talk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001666, illust_id='Fray_serious', msg='$52000033_QD__AUDIENCEWITHEREB_02__9$', duration=3000, delay_tick=3, align=Align.Center)
        self.add_cinematic_talk(npc_id=11001663, illust_id='Ereb_closeEye', msg='$52000033_QD__AUDIENCEWITHEREB_02__10$', duration=1000, align=Align.Left) # 에레브
        self.add_cinematic_talk(npc_id=11001665, illust_id='Karl_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__11$', duration=1000, align=Align.Right) # 칼

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6649):
            return talk_03(self.ctx)


class talk_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001666, illust_id='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__12$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11001666, illust_id='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__13$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return talk_04(self.ctx)


class talk_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001666, illust_id='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__14$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11001666, illust_id='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__15$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return talk_05(self.ctx)


class talk_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001663, illust_id='Ereb_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__16$', duration=3000, align=Align.Left) # 에레브
        self.add_cinematic_talk(npc_id=11001665, illust_id='Karl_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__17$', duration=3000, delay_tick=3, align=Align.Right) # 칼
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9001, type='trigger', achieve='AudienceWithEreb')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[60100010], quest_states=[1]):
            return end(self.ctx)


initial_state = idle
