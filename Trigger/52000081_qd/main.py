""" trigger/52000081_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001532], quest_states=[1]):
            # 50001532 퀘스트 진행 중 상태!
            return 연출01시작(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50100230], quest_states=[1]):
            # 50100230 퀘스트 진행 중 상태!
            return 연출01시작(self.ctx)


class 연출01시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.move_user_path(patrol_name='MS2PatrolData_PC_01')
            return PC말풍선01(self.ctx)


class PC말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000081_QD__MAIN__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC말풍선02(self.ctx)


class PC말풍선02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000081_QD__MAIN__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선03(self.ctx)


class PC말풍선03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000081_QD__MAIN__2$', time=1)
        self.set_pc_emotion_loop(sequence_name='Push_A', duration=10000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 감옥이펙트(self.ctx)


class 감옥이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몹소환(self.ctx)


class 몹소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000081_QD__MAIN__3$', time=2)
        self.set_pc_emotion_loop(sequence_name='Push_A', duration=15000.0)
        self.spawn_monster(spawn_ids=[1001,1003,1004], auto_target=False) # 연출용 어둠의 세력 몬스터

    def on_tick(self) -> trigger_api.Trigger:
        if not self.monster_dead(spawn_ids=[1001,1003,1004]):
            return 검사등장(self.ctx)
        if self.monster_dead(spawn_ids=[1001,1003,1004]):
            return PC구출01(self.ctx)


class 검사등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False) # 연출용 의문의 검사
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_NPC_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1001]):
            return PC구출01(self.ctx)
        if self.wait_tick(wait_tick=15000):
            return 예비용00(self.ctx)


class 예비용00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001,1003,1004])
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_NPC_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC구출01(self.ctx)


class PC구출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_NPC_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC구출02(self.ctx)


class PC구출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_NPC_02_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC구출03(self.ctx)


class PC구출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=1002, sequence_name='Attack_01_D', duration=2000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC구출04(self.ctx)


class PC구출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=10000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화01(self.ctx)


class 검사대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=1002, sequence_name='Bore_A', duration=1500.0)
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000081_QD__MAIN__4$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화02(self.ctx)


class 검사대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000081_QD__MAIN__5$', align=Align.Left, duration=3000)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_NPC_03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return PC말풍선04(self.ctx)


class PC말풍선04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004,8005], return_view=False)
        self.set_dialogue(type=1, script='$52000081_QD__MAIN__6$', time=3)
        self.move_user_path(patrol_name='MS2PatrolData_PC_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선05(self.ctx)


class PC말풍선05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000081_QD__MAIN__7$', time=3)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_NPC_04')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화03(self.ctx)


class 검사대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000081_QD__MAIN__17$', align=Align.Left, duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC말풍선06(self.ctx)


class PC말풍선06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000081_QD__MAIN__8$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선07(self.ctx)


class PC말풍선07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000081_QD__MAIN__9$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선08(self.ctx)


class PC말풍선08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000081_QD__MAIN__10$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화04(self.ctx)


class 검사대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000081_QD__MAIN__11$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화05(self.ctx)


class 검사대화05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000081_QD__MAIN__12$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화06(self.ctx)


class 검사대화06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000081_QD__MAIN__13$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사퇴장01(self.ctx)


class 검사퇴장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_NPC_05')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 검사대화07(self.ctx)


class 검사대화07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000081_QD__MAIN__14$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화08(self.ctx)


class 검사대화08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000081_QD__MAIN__15$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화09(self.ctx)


class 검사대화09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000081_QD__MAIN__16$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사퇴장02(self.ctx)


class 검사퇴장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_NPC_06')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1002])
        self.set_achievement(trigger_id=9000, type='trigger', achieve='meetarcaneblader1st')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
