""" trigger/52010033_qd/main_quest10003078.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 페리온 병원 : 52010033
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003078], quest_states=[2]):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.visible_my_pc(is_visible=False)
        self.move_user(map_id=52010033, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 티나감사(self.ctx)


class 티나감사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=나메드들어옴02, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4002], return_view=False)
        self.add_cinematic_talk(npc_id=11003420, msg='$52010033_QD__MAIN_QUEST10003078__0$', duration=4000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010033_QD__MAIN_QUEST10003078__1$', duration=3000)
        self.add_cinematic_talk(npc_id=11003420, msg='$52010033_QD__MAIN_QUEST10003078__2$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 나메드들어옴(self.ctx)


class 나메드들어옴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[201]) # 나메드:
        self.select_camera_path(path_ids=[4002,4001], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.show_caption(type='VerticalCaption', title='$52010033_QD__MAIN_QUEST10003078__3$', desc='$52010033_QD__MAIN_QUEST10003078__4$', align=Align.Center | Align.Left, duration=5000, scale=2.0)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010033_QD__MAIN_QUEST10003078__5$', duration=5000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010033_QD__MAIN_QUEST10003078__6$', duration=4500)
        self.add_cinematic_talk(npc_id=11003420, msg='$52010033_QD__MAIN_QUEST10003078__7$', duration=2000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010033_QD__MAIN_QUEST10003078__8$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010033_QD__MAIN_QUEST10003078__9$', duration=2000)
        self.add_cinematic_talk(npc_id=11003389, msg='$52010033_QD__MAIN_QUEST10003078__10$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=22000):
            return 나메드들어옴_1(self.ctx)


class 나메드들어옴_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 나메드들어옴02(self.ctx)


class 나메드들어옴02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010032, portal_id=1)


initial_state = idle
