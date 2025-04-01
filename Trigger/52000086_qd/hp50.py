""" trigger/52000086_qd/hp50.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 퀘스트체크50100300_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100300], quest_states=[3]):
            # 어둠에 물든 서리왕 퀘스트 완료 상태!
            return 던전종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100300], quest_states=[2]):
            # 어둠에 물든 서리왕 퀘스트 완료 가능 상태!
            return 던전종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100300], quest_states=[1]):
            # 어둠에 물든 서리왕 퀘스트 진행 중 상태!
            return 대기(self.ctx)


class 퀘스트체크50100310_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100310], quest_states=[3]):
            # 어둠에 물든 서리왕 퀘스트 완료 상태!
            return 던전종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100310], quest_states=[2]):
            # 어둠에 물든 서리왕 퀘스트 완료 가능 상태!
            return 던전종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100310], quest_states=[1]):
            # 어둠에 물든 서리왕 퀘스트 진행 중 상태!
            return 대기(self.ctx)


class 퀘스트체크50100311_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100311], quest_states=[3]):
            # 어둠에 물든 서리왕 퀘스트 완료 상태!
            return 던전종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100311], quest_states=[2]):
            # 어둠에 물든 서리왕 퀘스트 완료 가능 상태!
            return 던전종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100311], quest_states=[1]):
            # 어둠에 물든 서리왕 퀘스트 진행 중 상태!
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000])
        self.set_visible_breakable_object(trigger_ids=[4000])
        self.set_portal(portal_id=91)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='hp50') == 1:
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[1007,1008], auto_target=False)
        self.move_user(map_id=52000086, portal_id=30)
        self.select_camera(trigger_id=313)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에르다등장(self.ctx)


class 에르다등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=연출종료)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera(trigger_id=314)
        self.move_npc(spawn_id=1008, patrol_name='MS2PatrolData_1008A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에르다대사01(self.ctx)


class 에르다대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003069, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__0$', align=Align.right, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 비에른대사01(self.ctx)


class 비에른대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=315)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__1$', align=Align.left, duration=3000)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__2$', align=Align.left, duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에르다대사02(self.ctx)


class 에르다대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=316)
        self.visible_my_pc(is_visible=False) # 캐릭터 숨김
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__3$', align=Align.right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 비에른대사02(self.ctx)


class 비에른대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__4$', align=Align.left, duration=4000)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__5$', align=Align.left, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 비에른접근(self.ctx)


class 비에른접근(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1006B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에르다대사03(self.ctx)


class 에르다대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True) # 캐릭터 보임
        self.select_camera(trigger_id=317)
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__6$', align=Align.right, duration=4000)
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__7$', align=Align.right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 비에른대사03(self.ctx)


class 비에른대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=318)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__8$', align=Align.left, duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에르다대사04(self.ctx)


class 에르다대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=317)
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__9$', align=Align.right, duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 비에른대사04(self.ctx)


class 비에른대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=312)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__10$', align=Align.right, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 비에른대사05(self.ctx)


class 비에른대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=318)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__11$', align=Align.left, duration=4000)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__12$', align=Align.left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 에르다대사05(self.ctx)


class 에르다대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=317)
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__13$', align=Align.right, duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에르다대사06(self.ctx)


class 에르다대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1008])
        self.set_visible_breakable_object(trigger_ids=[4000], visible=True)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__14$', align=Align.left, duration=2000)
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__15$', align=Align.right, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 에르다대사07(self.ctx)


class 에르다대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=319)
        self.spawn_monster(spawn_ids=[1009], auto_target=False)
        self.set_visible_breakable_object(trigger_ids=[4000])
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__16$', align=Align.right, duration=3000)
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__17$', align=Align.right, duration=5000)
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__18$', align=Align.right, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return 에르다이동(self.ctx)


class 에르다이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1009, patrol_name='MS2PatrolData_1009A')
        self.select_camera(trigger_id=320)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에르다대사08(self.ctx)


class 에르다대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1007A')
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__19$', align=Align.right, duration=4000)
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__20$', align=Align.right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.visible_my_pc(is_visible=True) # 캐릭터 숨김
        self.set_ai_extra_data(key='getBack', value=1)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[1007,1008,1009])
        self.spawn_monster(spawn_ids=[2098], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.add_buff(box_ids=[199], skill_id=70000115, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 비에른사망대기(self.ctx)


class 비에른사망대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 사망연출대기(self.ctx)


class 사망연출대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 사망연출시작(self.ctx)


class 사망연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000086, portal_id=40)
        self.destroy_monster(spawn_ids=[2099])
        self.destroy_monster(spawn_ids=[2098])
        self.spawn_monster(spawn_ids=[1101,1102], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=1102, sequence_name='Stun_A', duration=1000000000000.0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 에드다이동02(self.ctx)


class 에드다이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=사망연출종료)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera(trigger_id=321)
        self.move_npc(spawn_id=1101, patrol_name='MS2PatrolData_1101A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에르다대사10(self.ctx)


class 에르다대사10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__21$', align=Align.right, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 비에른대사10(self.ctx)


class 비에른대사10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=322)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__22$', align=Align.left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에르다대사11(self.ctx)


class 에르다대사11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__23$', align=Align.right, duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 비에른대사11(self.ctx)


class 비에른대사11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=323)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__24$', align=Align.left, duration=4000)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__25$', align=Align.left, duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 비에른대사12(self.ctx)


class 비에른대사12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__26$', align=Align.left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에르다대사12(self.ctx)


class 에르다대사12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__27$', align=Align.right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 비에른대사13(self.ctx)


class 비에른대사13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=322)
        self.set_npc_emotion_loop(spawn_id=1102, sequence_name='Idle_A', duration=1000000000000.0)
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__28$', align=Align.left, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 비에른대사14(self.ctx)


class 비에른대사14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=324)
        self.move_npc(spawn_id=1102, patrol_name='MS2PatrolData_1102A')
        self.add_cinematic_talk(npc_id=11003075, illust_id='SnowKing_normal', msg='$52000086_QD__HP50__29$', align=Align.left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에드다이동03(self.ctx)


class 에드다이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=325)
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__30$', align=Align.right, duration=3000)
        # self.move_npc(spawn_id=1101, patrol_name='MS2PatrolData_1101B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC말풍선대사(self.ctx)


class PC말풍선대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000086_QD__HP50__31$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 에르다대사13(self.ctx)


class 에르다대사13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__32$', align=Align.right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에르다대사13To1(self.ctx)


class 에르다대사13To1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003074, illust_id='SnowQueen_normal', msg='$52000086_QD__HP50__33$', align=Align.right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에르다대사14(self.ctx)


class 에르다대사14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=321)
        # self.set_dialogue(type=2, spawn_id=11003074, script='미안하지만 지금은… 생각을 좀 정리하고 싶으니 혼자 있게 해 다오. 부탁이다.', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에드다마저이동(self.ctx)


class 에드다마저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # self.move_npc(spawn_id=1101, patrol_name='MS2PatrolData_1101C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 사망연출종료(self.ctx)


class 사망연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[1101,1102])
        self.spawn_monster(spawn_ids=[10000,10001,10002])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.set_achievement(trigger_id=199, type='trigger', achieve='snowkingbjorn')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 던전종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_portal(portal_id=91)
        self.move_user(map_id=52000086, portal_id=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 던전종료1(self.ctx)


class 던전종료1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3102])
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3102])
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3103])
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3104])
        self.set_breakable(trigger_ids=[4000])
        self.set_visible_breakable_object(trigger_ids=[4000])
        self.move_user(map_id=52000086, portal_id=30)
        self.destroy_monster(spawn_ids=[1101,1102])
        self.spawn_monster(spawn_ids=[10000,10001,10002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 퀘스트체크50100300_2
