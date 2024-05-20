""" trigger/52020032_qd/main_a.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=8001, initial_sequence='Damg_Idle_B')
        self.set_interact_object(trigger_ids=[10001281], state=0)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200100], quest_states=[3]):
            return Del_Npc(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200095], quest_states=[1]):
            return Ready(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200095], quest_states=[2]):
            return Exit(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200095], quest_states=[3]):
            return Exit(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200100], quest_states=[1]):
            return Exit(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200100], quest_states=[2]):
            return Exit(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=8001, visible=True, initial_sequence='Damg_Idle_B')
        self.spawn_monster(spawn_ids=[102]) # 미카엘
        self.spawn_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[204])
        self.spawn_monster(spawn_ids=[205])
        self.spawn_monster(spawn_ids=[206])
        self.spawn_monster(spawn_ids=[207])
        self.spawn_monster(spawn_ids=[301]) # 폭주 마리오네트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2002], quest_ids=[60200095], quest_states=[1]):
            return Battle_A(self.ctx)


class Battle_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=201, to_spawn_id=601)
        self.change_monster(from_spawn_id=202, to_spawn_id=602)
        self.change_monster(from_spawn_id=203, to_spawn_id=603)
        self.change_monster(from_spawn_id=204, to_spawn_id=604)
        self.change_monster(from_spawn_id=205, to_spawn_id=605)
        self.change_monster(from_spawn_id=206, to_spawn_id=606)
        self.change_monster(from_spawn_id=207, to_spawn_id=607)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,602,603,604,605,606,607]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.set_scene_skip(state=Battle_B, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_3001')
        self.select_camera_path(path_ids=[4004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=301, sequence_name='Attack_01_B')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Battle_B(self.ctx)


class Battle_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0.5)
        self.change_monster(from_spawn_id=301, to_spawn_id=701)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[701]):
            return Event_End(self.ctx)


class Event_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.set_interact_object(trigger_ids=[10001281], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200095], quest_states=[2]):
            return Exit(self.ctx)


class Exit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101]) # 미카엘
        self.set_actor(trigger_id=8001, initial_sequence='Damg_Idle_B')


class Del_Npc(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.set_actor(trigger_id=8001, initial_sequence='Damg_Idle_B')


initial_state = Idle
