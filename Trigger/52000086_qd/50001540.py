""" trigger/52000086_qd/50001540.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 퀘스트체크50100300_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100300], quest_states=[3]):
            # 어둠에 물든 서리왕 퀘스트 완료 상태!
            return None # Missing State: 던전종료
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100300], quest_states=[2]):
            # 어둠에 물든 서리왕 퀘스트 완료 가능 상태!
            return None # Missing State: 던전종료
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100300], quest_states=[1]):
            # 어둠에 물든 서리왕 퀘스트 진행 중 상태!
            return 대기(self.ctx)


class 퀘스트체크50100310_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100310], quest_states=[3]):
            # 녹아내린 얼음 퀘스트 완료 상태!
            return None # Missing State: 던전종료
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100310], quest_states=[2]):
            # 녹아내린 얼음 퀘스트 완료 가능 상태!
            return None # Missing State: 던전종료
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100310], quest_states=[1]):
            # 녹아내린 얼음 퀘스트 진행 중 상태!
            return 대기(self.ctx)


class 퀘스트체크50100311_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100311], quest_states=[3]):
            # 그리고 남겨진 자들… 퀘스트 완료 상태!
            return None # Missing State: 던전종료
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100311], quest_states=[2]):
            # 그리고 남겨진 자들… 퀘스트 완료 가능 상태!
            return None # Missing State: 던전종료
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100311], quest_states=[1]):
            # 그리고 남겨진 자들… 퀘스트 진행 중 상태!
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Closed') # IronDoor_Stage02
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Closed') # IronDoor_Stage03
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='Closed') # IronDoor_Stage04
        self.set_actor(trigger_id=4005, visible=True, initial_sequence='Closed') # IronDoor_Stage05
        self.select_camera(trigger_id=300)
        self.set_mesh(trigger_ids=[3005,3006,3007,3008,3009,3010,3011,3012], visible=True)
        self.set_mesh(trigger_ids=[3102,3103,3104,3105], visible=True)
        self.set_mesh(trigger_ids=[3160,3161,3162,3163,3164])
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=True)
        self.spawn_monster(spawn_ids=[1001,1002,1003], auto_target=False)
        self.remove_buff(box_id=199, skill_id=70000115)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000086, portal_id=99)
        self.set_skip(state=연출종료)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 에르다대사01(self.ctx)


class 에르다대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000086_QD__50001540__0$', align=Align.Right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에르다대사02(self.ctx)


class 에르다대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000086_QD__50001540__1$', align=Align.Right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 설눈이대사01(self.ctx)


class 설눈이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000086_QD__50001540__2$', align=Align.Right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 비에른대사01(self.ctx)


class 비에른대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__50001540__3$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 설눈이대사02(self.ctx)


class 설눈이대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001A')
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000086_QD__50001540__4$', align=Align.Right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 비에른방향전환(self.ctx)


class 비에른방향전환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000086_QD__50001540__5$', align=Align.Right, duration=2000)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 비에른공격(self.ctx)


class 비에른공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=306)
        self.set_npc_emotion_sequence(spawn_id=1003, sequence_name='Attack_01_D')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000086_QD__50001540__6$', align=Align.Right, duration=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 설눈이스턴(self.ctx)


class 설눈이스턴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_npc_emotion_loop(spawn_id=1001, sequence_name='Stun_A', duration=1000000000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에르다대사03(self.ctx)


class 에르다대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000086_QD__50001540__7$', align=Align.Right, duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 비에른대사02(self.ctx)


class 비에른대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=307)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__50001540__8$', align=Align.Left, duration=4000)
        self.add_cinematic_talk(npc_id=11003068, illust_id='Seolnunyi_normal', msg='$52000086_QD__50001540__9$', align=Align.Right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 비에른대사03(self.ctx)


class 비에른대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=308)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003B')
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__50001540__10$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에르다대사04(self.ctx)


class 에르다대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=309)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002A')
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000086_QD__50001540__11$', align=Align.Right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에르다대사05(self.ctx)


class 에르다대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=310)
        self.set_npc_emotion_loop(spawn_id=1002, sequence_name='AttackReady_01_A', duration=1000000000000.0)
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000086_QD__50001540__12$', align=Align.Right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[1001,1002,1003])
        self.spawn_monster(spawn_ids=[1004,1005], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=1004, sequence_name='Stun_A', duration=1000000000000.0)
        self.set_npc_emotion_loop(spawn_id=1005, sequence_name='AttackReady_01_A', duration=1000000000000.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.add_buff(box_ids=[199], skill_id=70000115, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차게이트1(self.ctx)


class 차게이트1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.show_guide_summary(entity_id=25200861, text_id=25200861, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 차게이트2(self.ctx)


class 차게이트2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2002], auto_target=False)
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2002]):
            return 차게이트3(self.ctx)


class 차게이트3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2003], auto_target=False)
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2003]):
            return 차게이트4(self.ctx)


class 차게이트4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2004], auto_target=False)
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2004]):
            return 감지대기(self.ctx)


class 감지대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.set_actor(trigger_id=4005, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3105])
        self.show_guide_summary(entity_id=25200862, text_id=25200862, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 차연출시작2(self.ctx)


class 차연출시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=차연출종료2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=311)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 비에른대사04(self.ctx)


class 비에른대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__50001540__13$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 비에른대사05(self.ctx)


class 비에른대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=312)
        self.move_npc(spawn_id=1006, patrol_name='MS2PatrolData_1006A')
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__50001540__14$', align=Align.Left, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 차연출종료2(self.ctx)


class 차연출종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_portal(portal_id=91)
        self.destroy_monster(spawn_ids=[1006])
        self.spawn_monster(spawn_ids=[2099], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.add_buff(box_ids=[199], skill_id=70000115, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 퀘스트체크50100300_1
