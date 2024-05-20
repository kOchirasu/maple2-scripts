""" trigger/52000083_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


"""
class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001536], quest_states=[1]):
            return 연출대기(self.ctx)
"""

class 연출출력체크50001536(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001536], quest_states=[1]):
            return 연출시작(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50100260], quest_states=[1]):
            return 연출시작(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001536], quest_states=[1]):
            return 조건체크01(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50100260], quest_states=[1]):
            return 조건체크01(self.ctx)


class 조건체크01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001536], quest_states=[2]):
            return 연출이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50100260], quest_states=[2]):
            return 연출이후(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001536], quest_states=[2]):
            return 조건체크02(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50100260], quest_states=[2]):
            return 조건체크02(self.ctx)


class 조건체크02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001536], quest_states=[3]):
            return 조건체크03(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001536], quest_states=[3]):
            return 전투종료후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50100260], quest_states=[3]):
            return 조건체크03(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50100260], quest_states=[3]):
            return 조건체크03(self.ctx)


class 조건체크03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001537], quest_states=[1]):
            return 연출이후(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001537], quest_states=[1]):
            return 연출이후(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50100270], quest_states=[1]):
            return 연출이후(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50100270], quest_states=[1]):
            return 연출이후(self.ctx)


"""
class 조건체크04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001537], quest_states=[2]):
            return 연출이후(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001537], quest_states=[2]):
            return 빈방(self.ctx)
"""

class 연출이후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 전투종료후(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 연출종료(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False) # 스턴당한 디나
        # self.set_npc_emotion_loop(spawn_id=1001, sequence_name='Stun_A')
        self.spawn_monster(spawn_ids=[1011], auto_target=False) # 싸우고 있는 의문의 검사
        self.spawn_monster(spawn_ids=[1021], auto_target=False) # 연출용 어둠의 세력 몬스터 스폰포인트 1
        self.spawn_monster(spawn_ids=[1022], auto_target=False) # 연출용 어둠의 세력 몬스터 스폰포인트 2
        self.spawn_monster(spawn_ids=[1023], auto_target=False) # 연출용 어둠의 세력 몬스터 스폰포인트 3
        self.spawn_monster(spawn_ids=[1024], auto_target=False) # 연출용 어둠의 세력 몬스터 스폰포인트 4
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 몬스터처치(self.ctx)


class 몬스터처치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1021,1022,1023,1024]):
            return 경로이동01(self.ctx)


class 경로이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrol_name='MS2PatrolData_PC_01')
        self.move_npc(spawn_id=1011, patrol_name='MS2PatrolData_blader_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 경로이동02(self.ctx)


class 경로이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.destroy_monster(spawn_ids=[1011])
            self.spawn_monster(spawn_ids=[1012], auto_target=False)
            return PC말풍선01(self.ctx)


class PC말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000083_QD__MAIN__0$', time=3)
        # self.set_npc_emotion_loop(spawn_id=1012, sequence_name='Idle_A', duration=30000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사시네마틱대사(self.ctx)


class 검사시네마틱대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000083_QD__MAIN__1$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PC말풍선02(self.ctx)


class PC말풍선02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000083_QD__MAIN__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PC말풍선03(self.ctx)


class PC말풍선03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000083_QD__MAIN__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 디나말풍선01(self.ctx)


class 디나말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1001, script='$52000083_QD__MAIN__4$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 디나기상(self.ctx)


class 디나기상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=1001, sequence_name='Idle_A', duration=69000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화01(self.ctx)


class 검사대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001,8002], return_view=False)
        self.set_npc_emotion_loop(spawn_id=1012, sequence_name='Talk_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000083_QD__MAIN__5$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 디나대화01(self.ctx)


class 디나대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003065, script='$52000083_QD__MAIN__6$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화02(self.ctx)


class 검사대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000083_QD__MAIN__7$', align=Align.Left, duration=3000)
        self.set_npc_emotion_loop(spawn_id=1012, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 디나대화02(self.ctx)


class 디나대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003065, script='$52000083_QD__MAIN__8$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화03(self.ctx)


class 검사대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000083_QD__MAIN__9$', align=Align.Left, duration=3000)
        self.set_npc_emotion_loop(spawn_id=1012, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 디나대화03(self.ctx)


class 디나대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003065, script='$52000083_QD__MAIN__10$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 디나대화04(self.ctx)


class 디나대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003065, script='$52000083_QD__MAIN__11$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 디나대화05(self.ctx)


class 디나대화05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003065, script='$52000083_QD__MAIN__12$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 디나대화05To1(self.ctx)


class 디나대화05To1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003065, script='$52000083_QD__MAIN__13$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화04(self.ctx)


class 검사대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000083_QD__MAIN__14$', align=Align.Left, duration=3000)
        self.set_npc_emotion_loop(spawn_id=1012, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 디나대화06(self.ctx)


class 디나대화06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003065, script='$52000083_QD__MAIN__15$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사대화06(self.ctx)


class 검사대화06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000083_QD__MAIN__16$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시점이동(self.ctx)


class 시점이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_npc_emotion_loop(spawn_id=1012, sequence_name='Bore_B', duration=2000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 검사퇴장01(self.ctx)


class 검사퇴장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1012, patrol_name='MS2PatrolData_blader_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return PC따라감(self.ctx)


class PC따라감(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC_03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return PC말풍선04(self.ctx)


class PC말풍선04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000083_QD__MAIN__17$', time=3)
        self.set_pc_emotion_loop(sequence_name='Talk_B', duration=2500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선05(self.ctx)


class PC말풍선05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000083_QD__MAIN__18$', time=3)
        self.set_pc_emotion_loop(sequence_name='Talk_B', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사시네마틱대사02(self.ctx)


class 검사시네마틱대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000083_QD__MAIN__19$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사말풍선03(self.ctx)


class 검사말풍선03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000083_QD__MAIN__20$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 검사퇴장02(self.ctx)


class 검사퇴장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.move_npc(spawn_id=1012, patrol_name='MS2PatrolData_blader_03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[1012])
        self.destroy_monster(spawn_ids=[1001])
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='meetarcaneblader2nd')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
