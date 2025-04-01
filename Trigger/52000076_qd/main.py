""" trigger/52000076_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
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
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=11, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001901.xml')
        self.set_onetime_effect(id=12, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001902.xml')
        self.set_onetime_effect(id=13, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001903.xml')
        self.set_onetime_effect(id=14, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001904.xml')
        self.set_onetime_effect(id=15, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001905.xml')
        self.set_onetime_effect(id=16, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001906.xml')
        self.set_onetime_effect(id=17, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001907.xml')
        self.set_onetime_effect(id=18, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001908.xml')
        self.set_onetime_effect(id=19, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001909.xml')
        self.set_onetime_effect(id=20, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001910.xml')
        self.set_user_value(key='saveEveIntheDark', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return CheckQuestCondition(self.ctx)


class CheckQuestCondition(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[100], quest_ids=[40002688], quest_states=[1]):
            return DungeonReady(self.ctx)
        if self.quest_user_detected(box_ids=[100], quest_ids=[40002688], quest_states=[2]):
            return QuestOnGoing01(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return DungeonReady(self.ctx)


# 다음 맵 이동
class QuestOnGoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000076, portal_id=30, box_id=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return QuestOnGoing02(self.ctx)


class QuestOnGoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=320)
        self.spawn_monster(spawn_ids=[1310,1410], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return QuestOnGoing03(self.ctx)


class QuestOnGoing03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EveTalk30(self.ctx)


# 던전 진행
class DungeonReady(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return DungeonStart(self.ctx)


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
        self.spawn_monster(spawn_ids=[2002], auto_target=False)

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
        self.spawn_monster(spawn_ids=[1021], auto_target=False)

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
            self.spawn_monster(spawn_ids=[2003], auto_target=False)
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
        self.spawn_monster(spawn_ids=[1022], auto_target=False)

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
            self.spawn_monster(spawn_ids=[2004], auto_target=False)
            return 진행11(self.ctx)


class 진행11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[131]):
            return 진행11몬스터(self.ctx)


class 진행11몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2004, patrol_name='MS2PatrolData2004_A')
        self.spawn_monster(spawn_ids=[1023], auto_target=False)

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
            self.spawn_monster(spawn_ids=[2005], auto_target=False)
            return 진행13(self.ctx)


class 진행13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[133]):
            return 진행13몬스터(self.ctx)


class 진행13몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2005, patrol_name='MS2PatrolData2005_A')
        self.spawn_monster(spawn_ids=[1024], auto_target=False)

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
            self.spawn_monster(spawn_ids=[2007], auto_target=False)
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
        self.set_scene_skip(state=카드반연출종료, action='nextState')
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=302)
        # self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카드반대사01(self.ctx)


class 카드반대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000349_BF__MAIN__5$', time=3)
        # self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카드반대사02(self.ctx)


class 카드반대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000349_BF__MAIN__6$', time=4)
        # self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 레논대사05(self.ctx)


class 레논대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)
        self.set_dialogue(type=2, spawn_id=11000064, script='$02000349_BF__MAIN__7$', time=4)
        # self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카드반대사03(self.ctx)


class 카드반대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000349_BF__MAIN__8$', time=6)
        # self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 카드반대사04(self.ctx)


class 카드반대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000349_BF__MAIN__9$', time=8)
        # self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 카드반대사05(self.ctx)


class 카드반대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.spawn_monster(spawn_ids=[1025,1026], auto_target=False)
        self.set_dialogue(type=2, spawn_id=24001705, script='$02000349_BF__MAIN__10$', time=7)
        # self.set_skip(state=카드반연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 카드반연출종료(self.ctx)


class 카드반연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.show_guide_summary(entity_id=20003502, text_id=20003502, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.destroy_monster(spawn_ids=[1025,1026])
        self.destroy_monster(spawn_ids=[1099])
        self.set_agent(trigger_ids=[901])
        self.set_agent(trigger_ids=[902])
        self.set_agent(trigger_ids=[903])
        self.set_agent(trigger_ids=[904])
        self.destroy_monster(spawn_ids=[2007])
        self.spawn_monster(spawn_ids=[2006], auto_target=False)
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
            return BossBattleStart01(self.ctx)


# Boss 전투 개시
class BossBattleStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1025,1026], auto_target=False)
        self.spawn_monster(spawn_ids=[1099], auto_target=False)
        self.set_agent(trigger_ids=[901], visible=True)
        self.set_agent(trigger_ids=[902], visible=True)
        self.set_agent(trigger_ids=[903], visible=True)
        self.set_agent(trigger_ids=[904], visible=True)
        self.set_mesh(trigger_ids=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], interval=200, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='saveEveIntheDark') == 1:
            return BossNpcChange01(self.ctx)
        if self.monster_dead(spawn_ids=[1099]):
            return BossNpcChange01(self.ctx)


class BossNpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_agent(trigger_ids=[901])
        self.set_agent(trigger_ids=[902])
        self.set_agent(trigger_ids=[903])
        self.set_agent(trigger_ids=[904])
        self.set_mesh(trigger_ids=[3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813,3814,3815,3816], visible=True, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BossNpcChange02(self.ctx)


class BossNpcChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1025,1026,1099,2006])
        self.move_user(map_id=52000076, portal_id=20, box_id=100)
        self.spawn_monster(spawn_ids=[1200,1300], auto_target=False)
        self.select_camera(trigger_id=310)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BossNpcChange03(self.ctx)


class BossNpcChange03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawn_id=1200, sequence_name='Attack_Idle_A', duration=15000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BossNpcChange04(self.ctx)


class BossNpcChange04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=311)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return EveEnter01(self.ctx)


class EveEnter01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1400], auto_target=False)
        self.move_npc(spawn_id=1400, patrol_name='MS2PatrolData_1400')
        self.select_camera(trigger_id=312)
        self.set_dialogue(type=1, spawn_id=1400, script='$52000076_QD__MAIN__0$', time=4, arg5=2)
        self.set_scene_skip(state=EvilKatvanLeave04, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return EveEnter02(self.ctx)


class EveEnter02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=313)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EveEnter03(self.ctx)


class EveEnter03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1300, patrol_name='MS2PatrolData_1300')
        self.move_user_path(patrol_name='MS2PatrolData_1000')
        self.set_dialogue(type=1, spawn_id=1300, script='$52000076_QD__MAIN__1$', time=2, arg5=2)
        self.set_dialogue(type=1, script='$52000076_QD__MAIN__2$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return EveEnter04(self.ctx)


class EveEnter04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=11, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001901.xml')
        self.set_dialogue(type=1, spawn_id=1200, script='$52000076_QD__MAIN__3$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EveTalk01(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=11, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001901.xml')


class EveTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=314)
        self.add_cinematic_talk(npc_id=11000523, illust_id='Eve_serious', msg='$52000076_QD__MAIN__4$', duration=5000)
        self.set_npc_emotion_sequence(spawn_id=1400, sequence_name='Talk_A')
        # self.set_skip(state=EveTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EveTalk01Skip(self.ctx)


class EveTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1400, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EveTalk02(self.ctx)


class EveTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000523, illust_id='Eve_serious', msg='$52000076_QD__MAIN__5$', duration=5000)
        self.set_npc_emotion_sequence(spawn_id=1400, sequence_name='Talk_A')
        # self.set_skip(state=EveTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EveTalk02Skip(self.ctx)


class EveTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1400, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LennonTalk01(self.ctx)


class LennonTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000076_QD__MAIN__6$', time=5) # 레논
        self.set_npc_emotion_sequence(spawn_id=1300, sequence_name='Talk_A')
        # self.set_skip(state=LennonTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return LennonTalk01Skip(self.ctx)


class LennonTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1300, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LennonTurnAround01(self.ctx)


class LennonTurnAround01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=315)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LennonTurnAround02(self.ctx)


class LennonTurnAround02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1300, patrol_name='MS2PatrolData_1301')
        self.move_npc(spawn_id=1400, patrol_name='MS2PatrolData_1401')
        self.move_user_path(patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return LennonTalk02(self.ctx)


class LennonTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1300, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000076_QD__MAIN__7$', time=5) # 레논
        # self.set_skip(state=LennonTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LennonTalk02Skip(self.ctx)


class LennonTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1300, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EvilKatvanTalk01(self.ctx)


class EvilKatvanTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=12, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001902.xml')
        self.set_dialogue(type=2, spawn_id=24001705, script='$52000076_QD__MAIN__8$', time=7) # 흑화카트반
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Talk_A')
        # self.set_skip(state=EvilKatvanTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return EvilKatvanTalk01Skip(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=12, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001902.xml')


class EvilKatvanTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return EvilKatvanTalk02(self.ctx)


class EvilKatvanTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=13, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001903.xml')
        self.set_dialogue(type=2, spawn_id=24001705, script='$52000076_QD__MAIN__9$', time=7) # 흑화카트반
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Talk_A')
        # self.set_skip(state=EvilKatvanTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return EvilKatvanTalk02Skip(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=13, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001903.xml')


class EvilKatvanTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return EvilKatvanTalk03(self.ctx)


class EvilKatvanTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=14, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001904.xml')
        self.set_dialogue(type=2, spawn_id=24001705, script='$52000076_QD__MAIN__10$', time=6) # 흑화카트반
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Talk_A')
        # self.set_skip(state=EvilKatvanTalk03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return EvilKatvanTalk03Skip(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=14, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001904.xml')


class EvilKatvanTalk03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return EveWalkFront01(self.ctx)


class EveWalkFront01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Idle_A')
        self.move_npc(spawn_id=1400, patrol_name='MS2PatrolData_1402')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EveTalk10(self.ctx)


class EveTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1400, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11000523, illust_id='Eve_serious', msg='$52000076_QD__MAIN__11$', duration=5000)
        # self.set_skip(state=EveTalk10Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EveTalk10Skip(self.ctx)


class EveTalk10Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EveTalk11(self.ctx)

    def on_exit(self) -> None:
        self.set_npc_emotion_sequence(spawn_id=1400, sequence_name='Idle_A')


class EveTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1400, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11000523, illust_id='Eve_serious', msg='$52000076_QD__MAIN__12$', duration=7000)
        # self.set_skip(state=EveTalk11Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return EveTalk11Skip(self.ctx)


class EveTalk11Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EveTalk12(self.ctx)

    def on_exit(self) -> None:
        self.set_npc_emotion_sequence(spawn_id=1400, sequence_name='Idle_A')


class EveTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1400, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11000523, script='$52000076_QD__MAIN__13$', time=5) # 이브
        # self.set_skip(state=EveTalk12Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EveTalk12Skip(self.ctx)


class EveTalk12Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EvilKatvanTalk10(self.ctx)

    def on_exit(self) -> None:
        self.set_npc_emotion_sequence(spawn_id=1400, sequence_name='Idle_A')


class EvilKatvanTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=15, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001905.xml')
        self.set_dialogue(type=2, spawn_id=24001705, script='$52000076_QD__MAIN__14$', time=6) # 흑화카트반
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Talk_A')
        # self.set_skip(state=EvilKatvanTalk10Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return EvilKatvanTalk10Skip(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=15, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001905.xml')


class EvilKatvanTalk10Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LennonTalk10(self.ctx)


class LennonTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Idle_A')
        self.move_npc(spawn_id=1300, patrol_name='MS2PatrolData_1302')
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000076_QD__MAIN__15$', time=3) # 레논
        # self.set_skip(state=LennonTalk10Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return LennonTalk10Skip(self.ctx)


class LennonTalk10Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State
        self.select_camera(trigger_id=316)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EvilKatvanTalk20(self.ctx)


class EvilKatvanTalk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=16, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001906.xml')
        self.set_dialogue(type=2, spawn_id=24001705, script='$52000076_QD__MAIN__16$', time=5) # 흑화카트반
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Talk_A')
        # self.set_skip(state=EvilKatvanTalk20Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EvilKatvanTalk20Skip(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=16, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001906.xml')


class EvilKatvanTalk20Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EvilKatvanTalk21(self.ctx)

    def on_exit(self) -> None:
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Idle_A')


class EvilKatvanTalk21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=17, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001907.xml')
        self.set_dialogue(type=2, spawn_id=24001705, script='$52000076_QD__MAIN__17$', time=6) # 흑화카트반
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Talk_A')
        # self.set_skip(state=EvilKatvanTalk21Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return EvilKatvanTalk21Skip(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=17, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001907.xml')


class EvilKatvanTalk21Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EvilKatvanTalk22(self.ctx)

    def on_exit(self) -> None:
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Idle_A')


class EvilKatvanTalk22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=18, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001908.xml')
        self.set_dialogue(type=2, spawn_id=24001705, script='$52000076_QD__MAIN__18$', time=5) # 흑화카트반
        # self.set_skip(state=EvilKatvanTalk22Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EvilKatvanTalk22Skip(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=18, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001908.xml')


class EvilKatvanTalk22Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State
        self.select_camera(trigger_id=317)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LennonTalk20(self.ctx)


class LennonTalk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1300, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000076_QD__MAIN__19$', time=4) # 레논
        # self.set_skip(state=LennonTalk20Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LennonTalk20Skip(self.ctx)


class LennonTalk20Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1300, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EvilKatvanTalk30(self.ctx)


class EvilKatvanTalk30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1200, patrol_name='MS2PatrolData_1200')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EvilKatvanTalk31(self.ctx)


class EvilKatvanTalk31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=19, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001909.xml')
        self.set_dialogue(type=2, spawn_id=24001705, script='$52000076_QD__MAIN__20$', time=9) # 흑화카트반
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Talk_A')
        # self.set_skip(state=EvilKatvanTalk31Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return EvilKatvanTalk31Skip(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=19, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001909.xml')


class EvilKatvanTalk31Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EvilKatvanTalk32(self.ctx)


class EvilKatvanTalk32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001910.xml')
        self.set_dialogue(type=2, spawn_id=24001705, script='$52000076_QD__MAIN__21$', time=6) # 흑화카트반
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return EvilKatvanTalk32Skip(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=20, path='BG/Common/Sound/Eff_Sound_52000076_EvilKatvan_DarkRoots_00001910.xml')


class EvilKatvanTalk32Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1200, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EvilKatvanLeave01(self.ctx)


class EvilKatvanLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1200, patrol_name='MS2PatrolData_1201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return EvilKatvanLeave02(self.ctx)


class EvilKatvanLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1200])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return EvilKatvanLeave03(self.ctx)


class EvilKatvanLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1300, patrol_name='MS2PatrolData_1303')
        self.set_dialogue(type=1, spawn_id=1300, script='$52000076_QD__MAIN__22$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EvilKatvanLeave04(self.ctx)


class EvilKatvanLeave04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return PositionArrange01(self.ctx)


class PositionArrange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1200,1300,1400])
        self.move_user(map_id=52000076, portal_id=30, box_id=100)
        self.spawn_monster(spawn_ids=[1310,1410], auto_target=False)
        self.select_camera(trigger_id=320)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PositionArrange02(self.ctx)


class PositionArrange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return LennonTalk30(self.ctx)


class LennonTalk30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=EveTalk31Skip, action='nextState')
        self.set_npc_emotion_sequence(spawn_id=1310, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000076_QD__MAIN__23$', time=5) # 레논
        # self.set_skip(state=LennonTalk30Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LennonTalk30Skip(self.ctx)


class LennonTalk30Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1310, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LennonTalk31(self.ctx)


class LennonTalk31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1310, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000076_QD__MAIN__24$', time=5) # 레논
        # self.set_skip(state=LennonTalk31Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LennonTalk31Skip(self.ctx)


class LennonTalk31Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1310, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EveTalk20(self.ctx)


class EveTalk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1410, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11000523, illust_id='Eve_serious', msg='$52000076_QD__MAIN__25$', duration=6000)
        # self.set_skip(state=EveTalk20Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return EveTalk20Skip(self.ctx)


class EveTalk20Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1410, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EveTalk21(self.ctx)


class EveTalk21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1410, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11000523, illust_id='Eve_serious', msg='$52000076_QD__MAIN__26$', duration=6000)
        # self.set_skip(state=EveTalk21Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return EveTalk21Skip(self.ctx)


class EveTalk21Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1410, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LennonTalk40(self.ctx)


class LennonTalk40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1310, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000076_QD__MAIN__27$', time=6) # 레논
        # self.set_skip(state=LennonTalk40Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return LennonTalk40Skip(self.ctx)


class LennonTalk40Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1310, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EveTalk30(self.ctx)


class EveTalk30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1410, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11000523, illust_id='Eve_serious', msg='$52000076_QD__MAIN__28$', duration=3000)
        # self.set_skip(state=EveTalk30Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EveTalk30Skip(self.ctx)


class EveTalk30Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1410, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State
        self.select_camera(trigger_id=321)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return EveTalk31(self.ctx)


class EveTalk31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000523, illust_id='Eve_serious', msg='$52000076_QD__MAIN__29$', duration=5000)
        # self.set_skip(state=EveTalk31Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EveTalk31Skip(self.ctx)


class EveTalk31Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestComplete01(self.ctx)


class QuestComplete01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=100, type='trigger', achieve='saveEveIntheDark')
        self.set_effect(trigger_ids=[6205], visible=True)
        self.set_mesh(trigger_ids=[3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713,3714,3715,3716], visible=True)
        self.set_portal(portal_id=2, visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestComplete02(self.ctx)


class QuestComplete02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.reset_camera(interpolation_time=1.0)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[100], quest_ids=[40002688], quest_states=[2]):
            return QuestComplete03(self.ctx)


class QuestComplete03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1310, patrol_name='MS2PatrolData_1304')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GotoTria01(self.ctx)


class GotoTria01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1310, script='$52000076_QD__MAIN__30$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GotoTria02(self.ctx)


class GotoTria02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1410, patrol_name='MS2PatrolData_1403')
        self.move_user_path(patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GotoTria03(self.ctx)


class GotoTria03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1310,1410])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GotoTria04(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class GotoTria04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000050, portal_id=1, box_id=100)


initial_state = 대기
