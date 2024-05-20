""" trigger/02000349_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001])
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=204, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=206, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=207, visible=True, initial_sequence='Idle_A')
        self.set_interact_object(trigger_ids=[10000806], state=2)
        self.set_interact_object(trigger_ids=[10000806], state=2)
        self.set_interact_object(trigger_ids=[10000807], state=2)
        self.set_interact_object(trigger_ids=[10000808], state=2)
        self.set_interact_object(trigger_ids=[10000809], state=2)
        self.set_interact_object(trigger_ids=[10000810], state=2)
        self.set_interact_object(trigger_ids=[10000811], state=2)
        self.set_interact_object(trigger_ids=[10000812], state=2)
        self.set_interact_object(trigger_ids=[13000014], state=2)
        self.set_mesh(trigger_ids=[39101,39102,39103,39104,39105,39106], visible=True)
        self.set_mesh(trigger_ids=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], visible=True)
        self.set_mesh(trigger_ids=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716])
        self.set_effect(trigger_ids=[600]) # fog 500
        self.set_effect(trigger_ids=[601]) # fog 1000
        self.set_effect(trigger_ids=[602]) # fog 1500
        self.set_effect(trigger_ids=[6101])
        self.set_effect(trigger_ids=[6102])
        self.set_effect(trigger_ids=[6103])
        self.set_effect(trigger_ids=[6104])
        self.set_effect(trigger_ids=[6105])
        self.set_effect(trigger_ids=[6106])
        self.set_effect(trigger_ids=[6107])
        self.set_effect(trigger_ids=[6108])
        self.set_effect(trigger_ids=[6201])
        self.set_effect(trigger_ids=[6202])
        self.set_effect(trigger_ids=[6203])
        self.set_effect(trigger_ids=[6204])
        self.set_effect(trigger_ids=[6205])
        self.set_skill(trigger_ids=[701])
        self.set_skill(trigger_ids=[702])
        self.set_skill(trigger_ids=[703])
        self.set_skill(trigger_ids=[704])
        self.set_portal(portal_id=2)
        self.set_agent(trigger_ids=[901], visible=True)
        self.set_agent(trigger_ids=[902], visible=True)
        self.set_agent(trigger_ids=[903], visible=True)
        self.set_agent(trigger_ids=[904], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='KatvanIntroMovie.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 진행01벽제거(self.ctx)


class 진행01벽제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, initial_sequence='Idle_A')
        self.set_interact_object(trigger_ids=[10000806], state=1)
        self.show_guide_summary(entity_id=20003492, text_id=20003492)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000806], state=0):
            self.hide_guide_summary(entity_id=20003492)
            self.set_mesh(trigger_ids=[39101])
            return 진행01몬스터(self.ctx)


class 진행01몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002,1003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1101]):
            return 진행01오브젝트(self.ctx)


class 진행01오브젝트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003496, text_id=20003496)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(trigger_id=202, initial_sequence='Idle_A')
        self.set_interact_object(trigger_ids=[10000807], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000807], state=0):
            self.hide_guide_summary(entity_id=20003496)
            return 진행02몬스터(self.ctx)


class 진행02몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[39102])
        self.spawn_monster(spawn_ids=[1004,1005,1006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1102]):
            return 진행02오브젝트(self.ctx)


class 진행02오브젝트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003497, text_id=20003497)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(trigger_id=203, initial_sequence='Idle_A')
        self.set_interact_object(trigger_ids=[10000808], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000808], state=0):
            self.hide_guide_summary(entity_id=20003497)
            return 진행03몬스터(self.ctx)


class 진행03몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[39103])
        self.spawn_monster(spawn_ids=[1007,1008,1009], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1103]):
            return 진행04오브젝트(self.ctx)


class 진행04오브젝트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003498, text_id=20003498)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(trigger_id=204, initial_sequence='Idle_A')
        self.set_interact_object(trigger_ids=[10000809], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000809], state=0):
            self.hide_guide_summary(entity_id=20003498)
            return 진행04몬스터(self.ctx)


class 진행04몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[39104])
        self.spawn_monster(spawn_ids=[1010,1011,1012], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1104]):
            return 진행05오브젝트(self.ctx)


class 진행05오브젝트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003499, text_id=20003499)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(trigger_id=205, initial_sequence='Idle_A')
        self.set_interact_object(trigger_ids=[10000810], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000810], state=0):
            self.hide_guide_summary(entity_id=20003499)
            return 진행05몬스터(self.ctx)


class 진행05몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[39105])
        self.spawn_monster(spawn_ids=[1013,1014,1015], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1105]):
            return 진행06오브젝트(self.ctx)


class 진행06오브젝트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003500, text_id=20003500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(trigger_id=206, initial_sequence='Idle_A')
        self.set_interact_object(trigger_ids=[10000811], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000811], state=0):
            self.set_achievement(trigger_id=100, type='trigger', achieve='rescue_boroboro')
            self.hide_guide_summary(entity_id=20003500)
            return 진행06몬스터(self.ctx)


class 진행06몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[39106])
        self.spawn_monster(spawn_ids=[1016,1017,1018,1019,1020])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1106]):
            return 레논오브젝트(self.ctx)


class 레논오브젝트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003495, text_id=20003495)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_actor(trigger_id=207, initial_sequence='Idle_A')
        self.set_interact_object(trigger_ids=[10000812], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000812], state=0):
            self.destroy_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
            self.hide_guide_summary(entity_id=20003495)
            return 레논구출(self.ctx)


class 레논구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.set_skip(state=레논구출종료)
        self.destroy_monster(spawn_ids=[2001])
        self.spawn_monster(spawn_ids=[2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 레논대사01(self.ctx)


class 레논대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6101], visible=True)
        self.set_dialogue(type=2, spawn_id=11000064, script='$02000349_BF__MAIN__3$', time=3)
        self.set_skip(state=레논구출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 레논대사02(self.ctx)


class 레논대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6102], visible=True)
        self.set_dialogue(type=2, spawn_id=11000064, script='$02000349_BF__MAIN__4$', time=3)
        self.set_skip(state=레논구출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 레논구출종료(self.ctx)


class 레논구출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.create_item(spawn_ids=[9001], trigger_id=100)
        # self.set_interact_object(trigger_ids=[13000014], state=1)
        self.select_camera_path(path_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        return 진행07(self.ctx)


class 진행07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=301, enable=False)
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData2002_AB')
        self.show_guide_summary(entity_id=20003501, text_id=20003501, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=127, spawn_ids=[2002]):
            return 진행07몬스터(self.ctx)


class 진행07몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1021])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1021]):
            return 진행08(self.ctx)


class 진행08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData2002_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=128, spawn_ids=[2002]):
            self.set_skill(trigger_ids=[701], enable=True)
            self.set_effect(trigger_ids=[6201], visible=True)
            self.destroy_monster(spawn_ids=[2002])
            self.spawn_monster(spawn_ids=[2003])
            return 진행09(self.ctx)


class 진행09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData2002_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[129]):
            return 진행09몬스터(self.ctx)


class 진행09몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2003, patrol_name='MS2PatrolData2003_A')
        self.spawn_monster(spawn_ids=[1022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1022]):
            return 진행10(self.ctx)


class 진행10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2003, patrol_name='MS2PatrolData2003_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=130, spawn_ids=[2003]):
            self.set_skill(trigger_ids=[702], enable=True)
            self.set_effect(trigger_ids=[6202], visible=True)
            self.destroy_monster(spawn_ids=[2003])
            self.spawn_monster(spawn_ids=[2004])
            return 진행11(self.ctx)


class 진행11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[131]):
            return 진행11몬스터(self.ctx)


class 진행11몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2004, patrol_name='MS2PatrolData2004_A')
        self.spawn_monster(spawn_ids=[1023])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1023]):
            return 진행12(self.ctx)


class 진행12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2004, patrol_name='MS2PatrolData2004_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=132, spawn_ids=[2004]):
            self.set_skill(trigger_ids=[703], enable=True)
            self.set_effect(trigger_ids=[6203], visible=True)
            self.destroy_monster(spawn_ids=[2004])
            self.spawn_monster(spawn_ids=[2005])
            return 진행13(self.ctx)


class 진행13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[133]):
            return 진행13몬스터(self.ctx)


class 진행13몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2005, patrol_name='MS2PatrolData2005_A')
        self.spawn_monster(spawn_ids=[1024])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1024]):
            return 진행14(self.ctx)


class 진행14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2005, patrol_name='MS2PatrolData2005_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=134, spawn_ids=[2005]):
            self.set_skill(trigger_ids=[704], enable=True)
            self.set_effect(trigger_ids=[6204], visible=True)
            self.destroy_monster(spawn_ids=[2005])
            self.spawn_monster(spawn_ids=[2007])
            return 진행15(self.ctx)


class 진행15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[135]):
            return 카트반연출딜레이(self.ctx)


class 카트반연출딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1099], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카드반연출시작(self.ctx)


class 카드반연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=302)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카드반대사01(self.ctx)


class 카드반대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000349_BF__MAIN__5$', time=3)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카드반대사02(self.ctx)


class 카드반대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000349_BF__MAIN__6$', time=4)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 레논대사05(self.ctx)


class 레논대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)
        self.set_dialogue(type=2, spawn_id=11000064, script='$02000349_BF__MAIN__7$', time=4)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카드반대사03(self.ctx)


class 카드반대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000349_BF__MAIN__8$', time=6)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 카드반대사04(self.ctx)


class 카드반대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000349_BF__MAIN__9$', time=8)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 카드반대사05(self.ctx)


class 카드반대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.spawn_monster(spawn_ids=[1025,1026], auto_target=False)
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000349_BF__MAIN__10$', time=7)
        self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 카드반연출종료(self.ctx)


class 카드반연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003502, text_id=20003502, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.destroy_monster(spawn_ids=[1025,1026])
        self.destroy_monster(spawn_ids=[1099])
        self.set_agent(trigger_ids=[901])
        self.set_agent(trigger_ids=[902])
        self.set_agent(trigger_ids=[903])
        self.set_agent(trigger_ids=[904])
        self.destroy_monster(spawn_ids=[2007])
        self.spawn_monster(spawn_ids=[2006])
        self.select_camera_path(path_ids=[302])

    def on_tick(self) -> trigger_api.Trigger:
        return 진행16(self.ctx)


class 진행16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=302, enable=False)
        self.select_camera(trigger_id=303, enable=False)
        self.move_npc(spawn_id=2006, patrol_name='MS2PatrolData2006_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=136, spawn_ids=[2006]):
            return 진행17(self.ctx)


class 진행17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1025,1026], auto_target=False)
        self.spawn_monster(spawn_ids=[1099], auto_target=False)
        self.set_agent(trigger_ids=[901], visible=True)
        self.set_agent(trigger_ids=[902], visible=True)
        self.set_agent(trigger_ids=[903], visible=True)
        self.set_agent(trigger_ids=[904], visible=True)
        self.set_mesh(trigger_ids=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], interval=200, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1099]):
            return 던전종료연출딜레이(self.ctx)


class 던전종료연출딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2006])
        self.spawn_monster(spawn_ids=[2008])
        self.destroy_monster(spawn_ids=[1025,1026])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 던전종료연출종료(self.ctx)


class 던전종료연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2008, script='$02000349_BF__MAIN__11$', time=3)
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2008, script='$02000349_BF__MAIN__13$', time=4)
        self.move_npc(spawn_id=2008, patrol_name='MS2PatrolData2008_A')
        self.set_effect(trigger_ids=[6205], visible=True)
        # self.show_guide_summary(entity_id=20003493, text_id=20003493)
        self.set_mesh(trigger_ids=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=True)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.destroy_monster(spawn_ids=[2008])
            self.hide_guide_summary(entity_id=20003493)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
