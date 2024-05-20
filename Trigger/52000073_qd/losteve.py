""" trigger/52000073_qd/losteve.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


"""
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001681], quest_states=[2]):
            return 대원등장(self.ctx)
"""

class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9900]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001683], quest_states=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001683], quest_states=[2]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001683], quest_states=[1]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001682], quest_states=[3]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001682], quest_states=[2]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001682], quest_states=[1]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001681], quest_states=[3]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001681], quest_states=[2]):
            return 대원등장(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001681], quest_states=[1]):
            return 대원등장(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001680], quest_states=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001680], quest_states=[2]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[50001680], quest_states=[1]):
            return 기본상태(self.ctx)


class 기본상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[401])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9900]):
            return 퀘스트조건체크(self.ctx)


class 대원있음(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return None # Missing State: 종료


class 대원등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[401]) # 윈 스틸던의 시체

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대원대사(self.ctx)


class 대원대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_pcTurn')
        self.select_camera_path(path_ids=[8003,8004], return_view=False)
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_2001')
        self.add_cinematic_talk(npc_id=11003446, illust_id='0', msg='$52000073_QD__LOSTEVE__0$', duration=4000, align=Align.Right) # 호르헤 대사
        self.face_emotion(spawn_id=101, emotion_name='Upset')
        self.set_scene_skip(state=연출종료, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카트반대사(self.ctx)


class 카트반대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000044, illust_id='0', msg='$52000073_QD__LOSTEVE__1$', duration=4000, align=Align.Right) # 호르헤 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return None # Missing State: 종료


initial_state = idle
