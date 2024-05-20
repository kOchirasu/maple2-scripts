""" trigger/52000085_qd/50001538.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100280], quest_states=[1]):
            # 50100280 퀘스트 진행 중 상태!
            return 대기(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100280], quest_states=[2]):
            # 50100280 퀘스트 완료 가능 상태!
            return 던전종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100280], quest_states=[3]):
            # 50100280 퀘스트 완료 상태!
            return 던전종료(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_mesh(trigger_ids=[3000,3001], visible=True)
        self.spawn_monster(spawn_ids=[1001,1002,1003], auto_target=False)
        self.set_portal(portal_id=91)
        self.remove_buff(box_id=199, skill_id=70000115)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=2000)
        self.set_npc_emotion_loop(spawn_id=1001, sequence_name='Attack_Idle_A', duration=1000000000000.0)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=1000000000000.0)
        self.set_skip(state=연출종료)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=300)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트루카대사01(self.ctx)


class 트루카대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1003, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__0$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 트루카대사02(self.ctx)


class 트루카대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__1$', align=Align.Left, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 에르다대사01(self.ctx)


class 에르다대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002A')
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000085_QD__50001538__2$', align=Align.Right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에르다대사02(self.ctx)


class 에르다대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003A')
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000085_QD__50001538__3$', align=Align.Right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 트루카대사03(self.ctx)


class 트루카대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)
        self.set_npc_emotion_sequence(spawn_id=1003, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__4$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 트루카대사04(self.ctx)


class 트루카대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__5$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에르다대사03(self.ctx)


class 에르다대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000085_QD__50001538__6$', align=Align.Right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트루카대사05(self.ctx)


class 트루카대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__7$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 트루카대사06(self.ctx)


class 트루카대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__8$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 트루카대사07(self.ctx)


class 트루카대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__9$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에르다대사04(self.ctx)


class 에르다대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000085_QD__50001538__10$', align=Align.Right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 설눈이이동01(self.ctx)


class 설눈이이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304)
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 설눈이대사01(self.ctx)


class 설눈이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=1001, sequence_name='Attack_Idle_A', duration=1000000000000.0)
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000085_QD__50001538__11$', align=Align.Right, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 트루카대사08(self.ctx)


class 트루카대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003B')
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__12$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트루카대사09(self.ctx)


class 트루카대사09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__13$', align=Align.Left, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 홀슈타트등장(self.ctx)


class 홀슈타트등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=306)
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 홀슈타트대사01(self.ctx)


class 홀슈타트대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=307)
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000085_QD__50001538__14$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 트루카대사10(self.ctx)


class 트루카대사10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=308)
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__15$', align=Align.Right, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 홀슈타트대사02(self.ctx)


class 홀슈타트대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=310)
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000085_QD__50001538__16$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 트루카대사11(self.ctx)


class 트루카대사11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=308)
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__17$', align=Align.Right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 트루카대사12(self.ctx)


class 트루카대사12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=309)
        self.add_cinematic_talk(npc_id=11003071, illust_id='11003762', msg='$52000085_QD__50001538__18$', align=Align.Right, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 포털이펙트(self.ctx)


class 포털이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1003, sequence_name='Bore_A')
        self.set_effect(trigger_ids=[601], visible=True)
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52000085_QD__50001538__19$', align=Align.Left, duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return NPC합체(self.ctx)


class NPC합체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1099')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1099')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=600):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1003,1004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 포털삭제(self.ctx)


class 포털삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 설눈이이동02(self.ctx)


class 설눈이이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=311)
        self.move_user_path(patrol_name='MS2PatrolData_PC')
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 설눈이대사02(self.ctx)


class 설눈이대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000085_QD__50001538__20$', align=Align.Right, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에르다방향전환(self.ctx)


class 에르다방향전환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에르다대사05(self.ctx)


class 에르다대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=312)
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000085_QD__50001538__21$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 설눈이대사03(self.ctx)


class 설눈이대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000085_QD__50001538__22$', align=Align.Right, duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에르다대사06(self.ctx)


class 에르다대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=1002, sequence_name='Attack_Idle_A', duration=1000000000000.0)
        self.select_camera(trigger_id=313)
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000085_QD__50001538__23$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[1001,1002,1003,1004])
        self.spawn_monster(spawn_ids=[2001,2002])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.move_user(map_id=52000085, portal_id=99)
        self.add_buff(box_ids=[199], skill_id=70000115, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7500):
            self.spawn_monster(spawn_ids=[2003,2004,2005], auto_target=False)
            return 에르다사망대기(self.ctx)


class 에르다사망대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2002]):
            return 에르다사망딜레이(self.ctx)


class 에르다사망딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2003,2004,2005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000085, portal_id=98)
        self.destroy_monster(spawn_ids=[2001,2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 종료연출시작(self.ctx)


class 종료연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=종료연출종료)
        self.spawn_monster(spawn_ids=[1005,1006], auto_target=False)
        self.select_camera(trigger_id=314)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에르다대사07(self.ctx)


class 에르다대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000085_QD__50001538__24$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 설눈이대사04(self.ctx)


class 설눈이대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000085_QD__50001538__25$', align=Align.Right, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 에르다공중부양준비(self.ctx)


class 에르다공중부양준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=315)
        self.set_npc_emotion_loop(spawn_id=1006, sequence_name='Attack_Idle_A', duration=1000000000000.0)
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000085_QD__50001538__26$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에르다공중부양(self.ctx)


class 에르다공중부양(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.move_npc(spawn_id=1006, patrol_name='MS2PatrolData_1006')
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000085_QD__50001538__27$', align=Align.Right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 얼림(self.ctx)


class 얼림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=1005, sequence_name='Stun_A', duration=1000000000000.0)
        self.set_pc_emotion_loop(sequence_name='StunFrozen_A', duration=25000.0)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[603], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 에르다공중부양중(self.ctx)


class 에르다공중부양중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=316)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return PC말풍선대사01(self.ctx)


class PC말풍선대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1006])
        self.select_camera(trigger_id=317)
        self.set_dialogue(type=1, script='$52000085_QD__50001538__28$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 설눈이말풍선대사01(self.ctx)


class 설눈이말풍선대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.set_dialogue(type=1, spawn_id=1005, script='$52000085_QD__50001538__29$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선대사02(self.ctx)


class PC말풍선대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=318)
        self.set_dialogue(type=1, script='$52000085_QD__50001538__30$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 설만이이동01(self.ctx)


class 설만이이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1007, script='$52000085_QD__50001538__31$', time=5)
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1007A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 설눈이인사(self.ctx)


class 설눈이인사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603])
        self.set_npc_emotion_loop(spawn_id=1005, sequence_name='Idle_A', duration=1000000000000.0)
        self.set_dialogue(type=1, spawn_id=1005, script='$52000085_QD__50001538__32$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 설만이이동02(self.ctx)


class 설만이이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005A')
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1007B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선대사03(self.ctx)


class PC말풍선대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602])
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=1000.0)
        self.move_user_path(patrol_name='MS2PatrolData_PC2')
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1007C')
        self.set_dialogue(type=1, script='$52000085_QD__50001538__33$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 설만이대사01(self.ctx)


class 설만이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=종료연출종료)
        self.select_camera(trigger_id=319)
        self.add_cinematic_talk(npc_id=11003073, illust_id='11000404', msg='$52000085_QD__50001538__34$', align=Align.Right, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 설눈이대사05(self.ctx)


class 설눈이대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000085_QD__50001538__35$', align=Align.Left, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 설만이대사02(self.ctx)


class 설만이대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003073, illust_id='11000404', msg='$52000085_QD__50001538__36$', align=Align.Right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 설눈이대사06(self.ctx)


class 설눈이대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000085_QD__50001538__37$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 설눈이대사07(self.ctx)


class 설눈이대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000085_QD__50001538__38$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 종료연출종료(self.ctx)


class 종료연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_npc_emotion_loop(spawn_id=1005, sequence_name='Idle_A', duration=1000000000000.0)
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=1000.0)
        self.destroy_monster(spawn_ids=[1005,1006,1007])
        self.set_achievement(trigger_id=199, type='trigger', achieve='snowqueenerda')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 던전종료(self.ctx)


class 던전종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1008,1009], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_portal(portal_id=91, visible=True, enable=True, minimap_visible=True)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 퀘스트체크
