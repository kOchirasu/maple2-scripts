""" trigger/52100103_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[700])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작체크(self.ctx)


"""
class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100960], quest_states=[3]):
            return 마를레네생성준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100960], quest_states=[2]):
            return 연출시작체크(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100960], quest_states=[1]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100950], quest_states=[3]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100950], quest_states=[2]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100950], quest_states=[1]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100940], quest_states=[3]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100940], quest_states=[2]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100940], quest_states=[1]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100930], quest_states=[3]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100930], quest_states=[2]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100930], quest_states=[1]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100920], quest_states=[3]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100920], quest_states=[2]):
            return 퀘스트용NPC소환준비(self.ctx)
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100920], quest_states=[1]):
            return 퀘스트용NPC소환(self.ctx)
"""

"""
class 퀘스트용NPC소환준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1], arg2=False)
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[700])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트용NPC소환(self.ctx)
"""

"""
class 퀘스트용NPC소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1], auto_target=False)
        self.spawn_monster(spawn_ids=[2], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작체크(self.ctx)
"""

class 연출시작체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10000], quest_ids=[50100960], quest_states=[2]):
            return 연출시작준비(self.ctx)


class 연출시작준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1], arg2=False)
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[700])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출NPC소환(self.ctx)


class 연출NPC소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52100103, portal_id=3)
        self.spawn_monster(spawn_ids=[1000], auto_target=False)
        self.spawn_monster(spawn_ids=[2000], auto_target=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시작암전1(self.ctx)


class 시작암전1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52100103, portal_id=3)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=엔딩암전, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 클라디아대사1(self.ctx)


class 클라디아대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        self.select_camera_path(path_ids=[1000,1001], return_view=False)
        self.set_npc_emotion_loop(spawn_id=2000, sequence_name='Bore_A', duration=1333.0)
        self.add_cinematic_talk(npc_id=11004419, msg='$52100103_QD__MAIN__0$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마를레네대사1(self.ctx)


class 마를레네대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        self.set_npc_emotion_loop(spawn_id=1000, sequence_name='Talk_A', duration=1333.0)
        self.add_cinematic_talk(npc_id=11004395, msg='$52100103_QD__MAIN__1$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 카메라흔들기(self.ctx)


class 카메라흔들기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[700], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마를레네대사2(self.ctx)


class 마를레네대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[3], auto_target=False)
        self.spawn_monster(spawn_ids=[200], auto_target=False)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.spawn_monster(spawn_ids=[203], auto_target=False)
        self.set_npc_rotation(spawn_id=1000, rotation=-45.0)
        self.set_npc_rotation(spawn_id=2000, rotation=45.0)
        self.add_cinematic_talk(npc_id=11004395, msg='$52100103_QD__MAIN__2$', duration=2000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11004419, msg='$52100103_QD__MAIN__3$', duration=2000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=3, sequence_name='Bore_A', duration=1333.0)
        self.select_camera(trigger_id=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카대사1(self.ctx)


class 투르카대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='PatrolData_PC_01')
        self.add_cinematic_talk(npc_id=11004430, msg='$52100103_QD__MAIN__4$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC돌아보기(self.ctx)


class PC돌아보기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 포탈오픈(self.ctx)


class 포탈오픈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.select_camera(trigger_id=1002)
        self.spawn_monster(spawn_ids=[300], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC대사(self.ctx)


class PC대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004395, msg='$52100103_QD__MAIN__5$', duration=3000, align=Align.Left)
        self.move_user(map_id=52100103, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카이동1(self.ctx)


class 투르카이동1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=300, patrol_name='PatrolData_Turka_1')
        self.move_npc(spawn_id=200, patrol_name='PatrolData_200_1')
        self.move_npc(spawn_id=201, patrol_name='PatrolData_201_1')
        self.move_npc(spawn_id=202, patrol_name='PatrolData_202_1')
        self.move_npc(spawn_id=203, patrol_name='PatrolData_203_1')
        self.select_camera(trigger_id=1003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC이동(self.ctx)


class PC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1000], arg2=False)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.add_cinematic_talk(npc_id=11004430, msg='$52100103_QD__MAIN__6$', duration=3000, align=Align.Left)
        self.move_npc(spawn_id=1001, patrol_name='PatrolData_1001_1')
        self.move_npc(spawn_id=300, patrol_name='PatrolData_Turka_2')
        self.move_npc(spawn_id=200, patrol_name='PatrolData_200_2')
        self.move_npc(spawn_id=201, patrol_name='PatrolData_201_2')
        self.move_npc(spawn_id=202, patrol_name='PatrolData_202_2')
        self.move_npc(spawn_id=203, patrol_name='PatrolData_203_2')
        self.move_user_path(patrol_name='PatrolData_PC_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC말풍선대사(self.ctx)


class PC말풍선대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52100103_QD__MAIN__7$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PC공격자세(self.ctx)


class PC공격자세(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=30000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카대사협박1(self.ctx)


class 투르카대사협박1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=202, rotation=45.0)
        self.set_npc_rotation(spawn_id=201, rotation=-45.0)
        self.set_npc_rotation(spawn_id=200, rotation=15.0)
        self.set_npc_rotation(spawn_id=203, rotation=-15.0)
        self.add_cinematic_talk(npc_id=11004430, msg='$52100103_QD__MAIN__8$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=300, sequence_name='Bore_A', duration=1333.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마를레네협박(self.ctx)


class 마를레네협박(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004395, msg='$52100103_QD__MAIN__9$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=1001, sequence_name='Talk_A', duration=1333.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카대사협박2(self.ctx)


class 투르카대사협박2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004430, msg='$52100103_QD__MAIN__10$', duration=6000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11004395, msg='$52100103_QD__MAIN__11$', duration=2000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11004430, msg='$52100103_QD__MAIN__12$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=300, sequence_name='Bore_A', duration=1333.0)
        self.destroy_monster(spawn_ids=[2000], arg2=False)
        self.spawn_monster(spawn_ids=[2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클라디아대사(self.ctx)


class 클라디아대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2001, patrol_name='PatrolData_2001_1')
        self.add_cinematic_talk(npc_id=11004385, msg='$52100103_QD__MAIN__13$', duration=2000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11004385, msg='$52100103_QD__MAIN__14$', duration=3500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 마를레네대사(self.ctx)


class 마를레네대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004395, msg='$52100103_QD__MAIN__15$', duration=2000, align=Align.Left)
        self.set_npc_rotation(spawn_id=1001, rotation=45.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클라디아마를레네바라보기(self.ctx)


class 클라디아마를레네바라보기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=2001, rotation=-90.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클라디아대사2(self.ctx)


class 클라디아대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=2001, sequence_name='Talk_A', duration=1333.0)
        self.add_cinematic_talk(npc_id=11004385, msg='$52100103_QD__MAIN__16$', duration=4000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11004395, msg='$52100103_QD__MAIN__17$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카대사3(self.ctx)


class 투르카대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004430, msg='$52100103_QD__MAIN__18$', duration=3000, align=Align.Left)
        self.set_npc_emotion_loop(spawn_id=300, sequence_name='Bore_A', duration=1333.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클라디아퇴장(self.ctx)


class 클라디아퇴장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.select_camera(trigger_id=1004)
        self.move_npc(spawn_id=2001, patrol_name='PatrolData_2001_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 부하퇴장(self.ctx)


class 부하퇴장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=200, patrol_name='PatrolData_200_3')
        self.move_npc(spawn_id=201, patrol_name='PatrolData_201_3')
        self.move_npc(spawn_id=202, patrol_name='PatrolData_202_3')
        self.move_npc(spawn_id=203, patrol_name='PatrolData_203_3')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카퇴장(self.ctx)


class 투르카퇴장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=300, patrol_name='PatrolData_Turka_3')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마를레네엔딩대사(self.ctx)


class 마를레네엔딩대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1005,1006], return_view=False)
        self.add_cinematic_talk(npc_id=11004395, msg='$52100103_QD__MAIN__19$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 엔딩암전(self.ctx)


class 엔딩암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터정리(self.ctx)


class 몬스터정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 상황정리(self.ctx)


class 상황정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52100109, portal_id=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.set_onetime_effect(id=101, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마를레네생성준비(self.ctx)


class 마를레네생성준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마를레네생성(self.ctx)


class 마를레네생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[700])
        self.spawn_monster(spawn_ids=[1], auto_target=False)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: State


initial_state = Ready
