""" trigger/52000047_qd/action01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 미션 성공 사운드 이펙트
        self.set_effect(trigger_ids=[5100]) # DoorOpen
        self.set_effect(trigger_ids=[5101]) # DoorClose
        self.set_effect(trigger_ids=[5200]) # Dust
        self.set_effect(trigger_ids=[5201]) # Dust
        self.set_effect(trigger_ids=[5202]) # Dust
        self.set_effect(trigger_ids=[5203]) # Dust
        self.set_effect(trigger_ids=[5204]) # Dust
        self.set_effect(trigger_ids=[5205]) # Dust
        self.set_effect(trigger_ids=[5206]) # Dust
        self.set_effect(trigger_ids=[5207]) # Dust
        self.set_effect(trigger_ids=[5208]) # Dust
        self.set_effect(trigger_ids=[5209]) # Dust
        self.set_effect(trigger_ids=[5210]) # Dust
        self.set_effect(trigger_ids=[5220]) # SandFlow
        self.set_effect(trigger_ids=[5221]) # SandFlow
        self.set_effect(trigger_ids=[5300]) # RockFall
        self.set_skill(trigger_ids=[7000]) # PCKnockBack
        self.set_skill(trigger_ids=[7001]) # PCKnockBack
        self.set_skill(trigger_ids=[7002]) # CubeBreak
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021]) # BrokenCube  Visible OFF
        self.set_mesh(trigger_ids=[3100]) # Barrier Visible OFF
        self.set_user_value(key='VasaraTired', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[10003044], quest_states=[2]):
            # 인내의 한계 퀘스트 수락한 상태
            return Quit(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[10003044], quest_states=[1]):
            # 인내의 한계 퀘스트 수락한 상태
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[10003043], quest_states=[3]):
            # 꺾을 수 없는 의지 퀘스트 완료 상태
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[10003043], quest_states=[2]):
            # 꺾을 수 없는 의지 퀘스트 완료 가능 상태
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[10003043], quest_states=[1]):
            # 꺾을 수 없는 의지 퀘스트 수락한 상태
            return LoadingDelay02(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


# 첫 번째 퀘스트 완료 가능, 완료 상태
class QuestOnGoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,201,530,531,532,533,534,535,536,537,538,539], auto_target=False)
        self.move_user(map_id=52000047, portal_id=3, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestOnGoing02(self.ctx)


class QuestOnGoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NextQuestStart01(self.ctx)


# 최초 입장
class LoadingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500)
        self.spawn_monster(spawn_ids=[500,501,502,503,504,505,506,507,508,509], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCWalkIn01(self.ctx)


class PCWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=501)
        self.move_user_path(patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCWalkIn02(self.ctx)


class PCWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=500, sequence_name='Talk_A', duration=6000.0)
        self.set_npc_emotion_sequence(spawn_id=507, sequence_name='Bore_A')
        self.set_npc_emotion_sequence(spawn_id=501, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCWalkIn03(self.ctx)


class PCWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=502, sequence_name='Talk_A', duration=6000.0)
        self.set_npc_emotion_loop(spawn_id=509, sequence_name='Talk_A', duration=6000.0)
        self.set_npc_emotion_sequence(spawn_id=503, sequence_name='Bore_A')
        self.select_camera(trigger_id=502)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPCNotice01(self.ctx)


class NPCNotice01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=509, patrol_name='MS2PatrolData_509')
        self.set_dialogue(type=1, spawn_id=509, script='$52000047_QD__ACTION01__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPCNotice02(self.ctx)


class NPCNotice02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=500, patrol_name='MS2PatrolData_500')
        self.move_npc(spawn_id=507, patrol_name='MS2PatrolData_507')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPCNotice03(self.ctx)


class NPCNotice03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=504, patrol_name='MS2PatrolData_504')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPCNotice04(self.ctx)


class NPCNotice04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=508, patrol_name='MS2PatrolData_508')
        self.set_dialogue(type=1, spawn_id=504, script='$52000047_QD__ACTION01__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NPCNotice05(self.ctx)


class NPCNotice05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_501')
        self.move_npc(spawn_id=506, patrol_name='MS2PatrolData_506')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPCNotice06(self.ctx)


class NPCNotice06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=502, patrol_name='MS2PatrolData_502')
        self.move_npc(spawn_id=505, patrol_name='MS2PatrolData_505')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPCNotice07(self.ctx)


class NPCNotice07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=503, patrol_name='MS2PatrolData_503')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MafiaReadyToFight01(self.ctx)


class MafiaReadyToFight01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=505, script='$52000047_QD__ACTION01__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MafiaReadyToFight02(self.ctx)


class MafiaReadyToFight02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=503)
        self.set_pc_emotion_sequence(sequence_names=['Striker_Bore_A'])
        self.set_dialogue(type=1, script='$52000047_QD__ACTION01__3$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MafiaReadyToFight03(self.ctx)


class MafiaReadyToFight03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=504)
        self.change_monster(from_spawn_id=500, to_spawn_id=900)
        self.change_monster(from_spawn_id=501, to_spawn_id=901)
        self.change_monster(from_spawn_id=502, to_spawn_id=902)
        self.change_monster(from_spawn_id=503, to_spawn_id=903)
        self.change_monster(from_spawn_id=504, to_spawn_id=904)
        self.change_monster(from_spawn_id=505, to_spawn_id=905)
        self.change_monster(from_spawn_id=506, to_spawn_id=906)
        self.change_monster(from_spawn_id=507, to_spawn_id=907)
        self.change_monster(from_spawn_id=508, to_spawn_id=908)
        self.change_monster(from_spawn_id=509, to_spawn_id=909)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return MafiaReadyToFight04(self.ctx)


class MafiaReadyToFight04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=504, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return MafiaFightStart01(self.ctx)


class MafiaFightStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=25200471, text_id=25200471) # 가이드 : 흑성회 조직원들 모두 쓰러트리기

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900,901,902,903,904,905,906,907,908,909]):
            return MafiaFightEnd01(self.ctx)


class MafiaFightEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # 미션 성공 사운드 이펙트
        self.hide_guide_summary(entity_id=25200471)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return WeihongWalkIn01(self.ctx)


# 웨이홍 바사라첸 입장
class WeihongWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[5100], visible=True) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return WeihongWalkIn02(self.ctx)


class WeihongWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[100], auto_target=False) # 웨이 홍
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_100')
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return WeihongWalkIn03(self.ctx)


class WeihongWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 바사라 첸
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_200')
        self.set_effect(trigger_ids=[5101], visible=True) # DoorClose
        self.move_user(map_id=52000047, portal_id=2, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return WeihongTalk01(self.ctx)


class WeihongTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)
        self.set_dialogue(type=2, spawn_id=11000251, script='$52000047_QD__ACTION01__4$', time=4) # 웨이 홍
        self.set_skip(state=WeihongTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return WeihongTalk01Skip(self.ctx)


class WeihongTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_user_value(trigger_id=500, key='NpcRemove', value=1)
        self.set_user_value(trigger_id=501, key='NpcRemove', value=1)
        self.set_user_value(trigger_id=502, key='NpcRemove', value=1)
        self.set_user_value(trigger_id=503, key='NpcRemove', value=1)
        self.set_user_value(trigger_id=504, key='NpcRemove', value=1)
        self.set_user_value(trigger_id=505, key='NpcRemove', value=1)
        self.set_user_value(trigger_id=506, key='NpcRemove', value=1)
        self.set_user_value(trigger_id=507, key='NpcRemove', value=1)
        self.set_user_value(trigger_id=508, key='NpcRemove', value=1)
        self.set_user_value(trigger_id=509, key='NpcRemove', value=1)
        self.spawn_monster(spawn_ids=[520,521,522,523,524,525,526,527,528,529], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return WeihongTalk02(self.ctx)


class WeihongTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000251, script='$52000047_QD__ACTION01__5$', time=4) # 웨이 홍
        self.set_skip(state=WeihongTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return WeihongTalk02Skip(self.ctx)


class WeihongTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=602)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MeetAgainWeihong01(self.ctx)


class MeetAgainWeihong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=520, patrol_name='MS2PatrolData_520')
        self.move_npc(spawn_id=521, patrol_name='MS2PatrolData_521')
        self.move_npc(spawn_id=522, patrol_name='MS2PatrolData_522')
        self.move_npc(spawn_id=523, patrol_name='MS2PatrolData_523')
        self.move_npc(spawn_id=524, patrol_name='MS2PatrolData_524')
        self.move_npc(spawn_id=525, patrol_name='MS2PatrolData_525')
        self.move_npc(spawn_id=526, patrol_name='MS2PatrolData_526')
        self.move_npc(spawn_id=527, patrol_name='MS2PatrolData_527')
        self.move_npc(spawn_id=528, patrol_name='MS2PatrolData_528')
        self.move_npc(spawn_id=529, patrol_name='MS2PatrolData_529')
        self.set_dialogue(type=1, spawn_id=520, script='$52000047_QD__ACTION01__6$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MeetAgainWeihong02(self.ctx)


class MeetAgainWeihong02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=527, script='$52000047_QD__ACTION01__7$', time=2)
        self.set_dialogue(type=1, spawn_id=529, script='$52000047_QD__ACTION01__8$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MeetAgainWeihong03(self.ctx)


class MeetAgainWeihong03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1001')
        self.set_dialogue(type=1, script='$52000047_QD__ACTION01__9$', time=4, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MeetAgainWeihong04(self.ctx)


class MeetAgainWeihong04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_101')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return MeetAgainWeihong05(self.ctx)


class MeetAgainWeihong05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=602, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MeetAgainWeihong06(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[100,200,520,521,522,523,524,525,526,527,528,529])
        self.spawn_monster(spawn_ids=[101,201,530,531,532,533,534,535,536,537,538,539], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class MeetAgainWeihong06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9900, type='trigger', achieve='MeetAgainWeihong')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NextQuestStart01(self.ctx)


# 다음 퀘스트 시작
class NextQuestStart01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[10003044], quest_states=[1]):
            # 인내의 한계 퀘스트 수락한 상태
            return PositionArrange01(self.ctx)


class PositionArrange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PositionArrange02(self.ctx)


class PositionArrange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=700)
        self.move_user(map_id=52000047, portal_id=3, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PositionArrange03(self.ctx)


class PositionArrange03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return WeihongStepBack01(self.ctx)


class WeihongStepBack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52000047_QD__ACTION01__10$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return WeihongStepBack02(self.ctx)


class WeihongStepBack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')
        self.set_dialogue(type=1, spawn_id=101, script='$52000047_QD__ACTION01__11$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PCTryToAttackWeihong01(self.ctx)


class PCTryToAttackWeihong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=710)
        self.set_pc_emotion_loop(sequence_name='Knuckle_Attack_Idle_A', duration=1734.0)
        self.set_dialogue(type=1, script='$52000047_QD__ACTION01__12$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return PCTryToAttackWeihong02(self.ctx)


class PCTryToAttackWeihong02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=711)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return PCTryToAttackWeihong03(self.ctx)


class PCTryToAttackWeihong03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return VasaraPush01(self.ctx)


class VasaraPush01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_202')
        self.set_dialogue(type=1, spawn_id=201, script='$52000047_QD__ACTION01__20$', time=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return VasaraPush02(self.ctx)


class VasaraPush02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Attack_01_H')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return VasaraPush03(self.ctx)


class VasaraPush03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7000], enable=True) # PCKnockBack

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return VasaraPush04(self.ctx)


class VasaraPush04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Push_A', duration=1500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SceneChange01(self.ctx)


class SceneChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SceneChange02(self.ctx)


class SceneChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=720)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SceneChange03(self.ctx)


class SceneChange03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return VasaraTalk01(self.ctx)


class VasaraTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_203')
        self.set_dialogue(type=1, script='$52000047_QD__ACTION01__13$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return VasaraTalk02(self.ctx)


class VasaraTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=201, script='$52000047_QD__ACTION01__14$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return VasaraTalk03(self.ctx)


class VasaraTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000047_QD__ACTION01__15$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return VasaraBattle01(self.ctx)


class VasaraBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=720, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return VasaraBattle02(self.ctx)


class VasaraBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=25200472, text_id=25200472) # 가이드 : 바사라 첸 쓰러트리기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='VasaraTired') == 1:
            return VasaraBattle03(self.ctx)


class VasaraBattle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # 미션 성공 사운드 이펙트
        self.hide_guide_summary(entity_id=25200472)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return VasaraTired01(self.ctx)


class VasaraTired01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return VasaraTired02(self.ctx)


class VasaraTired02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=720)
        self.move_user(map_id=52000047, portal_id=4, box_id=9900)
        self.destroy_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return VasaraTired03(self.ctx)


class VasaraTired03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=203, sequence_name='Down_Idle_A', duration=9000.0)
        self.set_pc_emotion_loop(sequence_name='Knuckle_Attack_Idle_A', duration=9537.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return VasaraTired04(self.ctx)


class VasaraTired04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=600):
            return VasaraTired05(self.ctx)


class VasaraTired05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=203, script='$52000047_QD__ACTION01__21$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return WeihongOrder01(self.ctx)


class WeihongOrder01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=730)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return WeihongOrder02(self.ctx)


class WeihongOrder02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000251, script='$52000047_QD__ACTION01__16$', time=5) # 웨이 홍
        self.set_skip(state=WeihongOrder02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return WeihongOrder02Skip(self.ctx)


class WeihongOrder02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return MafiaMove01(self.ctx)


class MafiaMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=731)
        self.move_npc(spawn_id=530, patrol_name='MS2PatrolData_530')
        self.move_npc(spawn_id=535, patrol_name='MS2PatrolData_535')
        self.move_npc(spawn_id=534, patrol_name='MS2PatrolData_534')
        self.move_npc(spawn_id=537, patrol_name='MS2PatrolData_537')
        self.move_npc(spawn_id=532, patrol_name='MS2PatrolData_532')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return MafiaMove02(self.ctx)


class MafiaMove02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=531, patrol_name='MS2PatrolData_531')
        self.move_npc(spawn_id=533, patrol_name='MS2PatrolData_533')
        self.move_npc(spawn_id=536, patrol_name='MS2PatrolData_536')
        self.move_npc(spawn_id=538, patrol_name='MS2PatrolData_538')
        self.move_npc(spawn_id=539, patrol_name='MS2PatrolData_539')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return VasaraTalk10(self.ctx)


class VasaraTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_204')
        self.set_dialogue(type=2, spawn_id=11001547, script='$52000047_QD__ACTION01__17$', time=5) # 바사라 첸
        self.set_skip(state=VasaraTalk10Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return VasaraTalk10Skip(self.ctx)


class VasaraTalk10Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return VasaraPushAgain01(self.ctx)


class VasaraPushAgain01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return VasaraPushAgain02(self.ctx)


class VasaraPushAgain02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Attack_02_G,Attack_03_G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return VasaraPushAgain03(self.ctx)


class VasaraPushAgain03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7001], enable=True) # PCKnockBack

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return VasaraPushAgain04(self.ctx)


class VasaraPushAgain04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Push_A', duration=6000.0)
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Attack_01_I,Attack_Idle_A,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return VasaraLastAttack01(self.ctx)


class VasaraLastAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7002], enable=True) # CubeBreak
        self.set_effect(trigger_ids=[5300], visible=True) # RockFall

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return VasaraLastAttack02(self.ctx)


class VasaraLastAttack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5220], visible=True) # SandFlow
        self.set_random_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021], visible=True, start_delay=22, interval=50, fade=80) # Rock Visible  ON
        self.set_effect(trigger_ids=[5200], visible=True) # Dust
        self.set_effect(trigger_ids=[5201], visible=True) # Dust
        self.set_effect(trigger_ids=[5202], visible=True) # Dust
        self.set_effect(trigger_ids=[5203], visible=True) # Dust
        self.set_effect(trigger_ids=[5204], visible=True) # Dust
        self.set_effect(trigger_ids=[5205], visible=True) # Dust
        self.set_effect(trigger_ids=[5206], visible=True) # Dust
        self.set_effect(trigger_ids=[5207], visible=True) # Dust
        self.set_effect(trigger_ids=[5208], visible=True) # Dust
        self.set_effect(trigger_ids=[5209], visible=True) # Dust
        self.set_effect(trigger_ids=[5210], visible=True) # Dust

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return VasaraLastAttack03(self.ctx)


class VasaraLastAttack03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5221], visible=True) # SandFlow
        self.select_camera(trigger_id=731)
        self.set_mesh(trigger_ids=[3100], visible=True) # Barrier Visible OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return VasaraTalk20(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[5220], visible=True) # SandFlow


class VasaraTalk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001547, script='$52000047_QD__ACTION01__18$', time=5) # 바사라 첸
        self.set_skip(state=VasaraTalk20Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return VasaraTalk20Skip(self.ctx)


class VasaraTalk20Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return VasaraTalk21(self.ctx)


class VasaraTalk21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001547, script='$52000047_QD__ACTION01__19$', time=5) # 바사라 첸
        self.set_skip(state=VasaraTalk21Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return VasaraTalk21Skip(self.ctx)


class VasaraTalk21Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=731, enable=False)
        self.set_effect(trigger_ids=[5221], visible=True) # SandFlow

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FriendOfVasara01(self.ctx)


class FriendOfVasara01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5220], visible=True) # SandFlow
        self.set_achievement(trigger_id=9900, type='trigger', achieve='FriendOfVasara')
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5221], visible=True) # SandFlow
        self.move_user(map_id=2000138, portal_id=105, box_id=9900)


initial_state = Wait
