""" trigger/52010032_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


"""
치유의 숲 : 52010032
들어오자마자 앉아있는 상태 연출
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202]) # 퀘스트 나메드: 11000039
        self.set_effect(trigger_ids=[5001]) # 나메드 치유 시전 이펙트
        self.set_effect(trigger_ids=[5002]) # 붉은 늑대의 심장 치유 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003090], quest_states=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.move_user(map_id=52010032, portal_id=7001)
        self.spawn_monster(spawn_ids=[201]) # 나메드:

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 치유의식_01(self.ctx)


class 치유의식_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN__0$', duration=3000, illust_id='0', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 치유의식_02(self.ctx)


class 치유의식_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_3001')
        self.move_user_path(patrol_name='MS2PatrolData_3002')
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN__1$', duration=3000, illust_id='0', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 치유의식_03(self.ctx)


class 치유의식_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_B')
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Cry_A'])
        self.add_cinematic_talk(npc_id=11003389, msg='$52010032_QD__MAIN__2$', duration=3000, illust_id='0', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 치유의식_04(self.ctx)


class 치유의식_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 치유의식_05(self.ctx)


class 치유의식_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003390, msg='$52010032_QD__MAIN__3$', duration=3000, illust_id='0', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return None # Missing State: 의식종료_01


class 의식종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: 의식종료_02


class 의식종료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
