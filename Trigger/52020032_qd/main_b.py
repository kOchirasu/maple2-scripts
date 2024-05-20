""" trigger/52020032_qd/main_b.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_actor(trigger_id=8002, initial_sequence='Idle_A')
        self.set_actor(trigger_id=8003, initial_sequence='Idle_A')
        self.set_actor(trigger_id=8004, initial_sequence='Idle_A')
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200165], quest_states=[1]):
            return Npc_Set(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200165], quest_states=[2]):
            return Npc_Set(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200165], quest_states=[3]):
            return Npc_All_Del(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200160], quest_states=[1]):
            return Event_A_Ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200160], quest_states=[2]):
            return Npc_Set(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200160], quest_states=[3]):
            return Npc_Set(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200150], quest_states=[2]):
            return Event_A_Ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200150], quest_states=[3]):
            return Event_A_Ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200155], quest_states=[1]):
            return Event_A_Ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200155], quest_states=[2]):
            return Event_A_Ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200155], quest_states=[3]):
            return Event_A_Ready(self.ctx)


class Event_A_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401]) # 미카엘
        self.set_actor(trigger_id=8002, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=8003, visible=True, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200160], quest_states=[1]):
            return Event_C_01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200150], quest_states=[3]):
            return Event_A_01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200155], quest_states=[1]):
            return Event_B_01(self.ctx)


class Event_A_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=8003, initial_sequence='Idle_A')
        self.set_actor(trigger_id=8004, visible=True, initial_sequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200155], quest_states=[1]):
            return Event_B_01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200160], quest_states=[1]):
            return Event_C_01(self.ctx)


class Event_B_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return Event_B_02(self.ctx)


class Event_B_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020016)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200160], quest_states=[1]):
            return Event_C_01(self.ctx)


class Event_C_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_actor(trigger_id=8002, visible=True, initial_sequence='Idle_A')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Event_C_Skip_01, action='Exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Event_C_02(self.ctx)


class Event_C_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020032, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return Event_C_03(self.ctx)


class Event_C_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=90000.0)
        self.add_cinematic_talk(npc_id=11003620, msg='그럼 편안한 죽음 되시길.', duration=2800, illust_id='Michael_normal', align=Align.Center)
        self.destroy_monster(spawn_ids=[401])
        self.set_actor(trigger_id=8002, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_C_04(self.ctx)


class Event_C_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_balloon_talk(msg='......', duration=1800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_C_05(self.ctx)


class Event_C_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_C_06(self.ctx)


class Event_C_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003622, msg='$npcName:11003620$놈!', duration=2800, illust_id='Turka_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_C_07(self.ctx)


class Event_C_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True)
        self.spawn_monster(spawn_ids=[501]) # 투르카
        self.add_cinematic_talk(npc_id=11003622, msg='감히 날 배신하다니!', duration=2800, illust_id='Turka_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_C_08(self.ctx)


class Event_C_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003622, msg='배신의 대가는 톡톡히 치르게 해주겠다.', illust_id='Turka_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_C_09(self.ctx)


class Event_C_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003622, msg='.......', duration=1800, illust_id='0', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_C_10(self.ctx)


class Event_C_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003622, msg='이렇게 된 이상 그 계획을 빨리 진행해야겠군.', duration=2800, illust_id='0', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_C_11(self.ctx)


class Event_C_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Event_C_12(self.ctx)


class Event_C_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True)
        self.destroy_monster(spawn_ids=[501])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_C_13(self.ctx)


class Event_C_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_C_14(self.ctx)


class Event_C_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='......', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_C_15(self.ctx)


class Event_C_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_actor(trigger_id=8003, initial_sequence='Idle_A')
        self.set_actor(trigger_id=8004, initial_sequence='Idle_A')
        self.spawn_monster(spawn_ids=[402]) # 엘레나
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=3000.0)
        self.reset_camera(interpolation_time=2.0)
        self.set_achievement(trigger_id=2001, type='trigger', achieve='Eavesdrop')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_C_Exit(self.ctx)


class Event_C_Skip_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_C_Skip_02(self.ctx)


class Event_C_Skip_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=3000.0)
        self.destroy_monster(spawn_ids=[401]) # 미카엘
        self.destroy_monster(spawn_ids=[501]) # 투르카
        self.spawn_monster(spawn_ids=[402]) # 엘레나
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_actor(trigger_id=8002, initial_sequence='Idle_A')
        self.set_actor(trigger_id=8003, initial_sequence='Idle_A')
        self.set_actor(trigger_id=8004, initial_sequence='Idle_A')
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.reset_camera(interpolation_time=2.0)
        self.set_achievement(trigger_id=2001, type='trigger', achieve='Eavesdrop')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_C_Exit(self.ctx)


class Event_C_Exit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


class Npc_Set(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[402]) # 엘레나
        self.destroy_monster(spawn_ids=[401])
        self.destroy_monster(spawn_ids=[501])


class Npc_All_Del(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[401])
        self.destroy_monster(spawn_ids=[402])
        self.destroy_monster(spawn_ids=[501])


initial_state = Idle
