""" trigger/52100002_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100060], quest_states=[1]):
            # 50100060 퀘스트 진행 중 상태!
            return 룸체크(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100060], quest_states=[2]):
            # 50100060 퀘스트 완료 가능 상태!
            return 퀘스트완료가능이거나완료1(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50100060], quest_states=[3]):
            # 50100060 퀘스트 완료 상태!
            return 퀘스트완료가능이거나완료1(self.ctx)


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 던전시작(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트던전시작(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002,2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[2001]):
            self.set_effect(trigger_ids=[601], visible=True)
            return 사망체크(self.ctx)
        if self.monster_dead(spawn_ids=[2001,2002]):
            return 사망딜레이(self.ctx)


class 사망체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001,2002]):
            return 사망딜레이(self.ctx)


class 사망딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001,2002]):
            return 암전대기(self.ctx)


class 퀘스트던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002,2101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[2101]):
            self.set_effect(trigger_ids=[601], visible=True)
            return 퀘스트사망체크(self.ctx)
        if self.monster_dead(spawn_ids=[2101,2102]):
            return 퀘스트사망딜레이(self.ctx)


class 퀘스트사망체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2101,2102]):
            return 퀘스트사망딜레이(self.ctx)


class 퀘스트사망딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 퀘스트종료체크(self.ctx)


class 퀘스트종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2101,2102]):
            return 암전대기(self.ctx)


class 암전대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 종료연출대기(self.ctx)


class 종료연출대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.move_user(map_id=52100002, portal_id=2)
        self.destroy_monster(spawn_ids=[1001,1002,2001,2002,2101,2102])
        self.spawn_monster(spawn_ids=[1098,1099], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawn_id=1098, sequence_name='Dead_B', duration=3000000.0)
        self.set_npc_emotion_loop(spawn_id=1099, sequence_name='Dead_B', duration=3000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료연출(self.ctx)


class 종료연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=연출종료)
        self.add_cinematic_talk(npc_id=11003889, illust_id='Firis_normal', msg='$02000392_BF__MAIN__0$', align=Align.Left, duration=4000)
        self.add_cinematic_talk(npc_id=11003888, illust_id='Celine_normal', msg='$02000392_BF__MAIN__1$', align=Align.Right, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return PC대사(self.ctx)


class PC대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$02000392_BF__MAIN__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC대사2(self.ctx)


class PC대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$02000392_BF__MAIN__10$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 자매교체(self.ctx)


class 자매교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1098,1099])
        self.spawn_monster(spawn_ids=[1096,1097], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 자매대화(self.ctx)


class 자매대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 자매대화01(self.ctx)


class 자매대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003889, illust_id='Firis_normal', msg='$02000392_BF__MAIN__3$', align=Align.Left, duration=4000)
        self.add_cinematic_talk(npc_id=11003888, illust_id='Celine_normal', msg='$02000392_BF__MAIN__4$', align=Align.Right, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 자매대화02(self.ctx)


class 자매대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003889, illust_id='Firis_normal', msg='$02000392_BF__MAIN__5$', align=Align.Left, duration=5000)
        self.set_dialogue(type=1, spawn_id=1097, script='$02000392_BF__MAIN__6$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 자매대화03(self.ctx)


class 자매대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003888, illust_id='Celine_normal', msg='$02000392_BF__MAIN__11$', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC대사3(self.ctx)


class PC대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$02000392_BF__MAIN__12$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 자매대화04(self.ctx)


class 자매대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003888, illust_id='Celine_normal', msg='$02000392_BF__MAIN__7$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 자매대화05(self.ctx)


class 자매대화05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003888, illust_id='Celine_normal', msg='$02000392_BF__MAIN__8$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 자매대화06(self.ctx)


class 자매대화06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003888, illust_id='Celine_normal', msg='$02000392_BF__MAIN__9$', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[1098,1099])
        self.destroy_monster(spawn_ids=[1096,1097])
        self.spawn_monster(spawn_ids=[1096,1097], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # self.select_camera(trigger_id=302, enable=False)
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 룸체크2(self.ctx)


class 퀘스트완료가능이거나완료1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1096,1097], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 룸체크2(self.ctx)


class 룸체크2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 던전완료(self.ctx)
        if not self.is_dungeon_room():
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            return 종료(self.ctx)


class 던전완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_achievement(trigger_id=199, type='trigger', achieve='ClearSirenSisters')
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
