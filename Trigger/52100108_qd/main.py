""" trigger/52100108_qd/main.xml """
import trigger_api
from System.Numerics import Vector3


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000360], quest_states=[1]):
            return wait_01(self.ctx)


class wait_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(trigger_ids=[6000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wait_03(self.ctx)


class wait_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52100108, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 들어왔다(self.ctx)


class 들어왔다(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[4001,4002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 들어왔다_02(self.ctx)


class 들어왔다_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006,4005], return_view=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52100108_QD__MAIN__0$', duration=3000)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 들어왔다_03(self.ctx)


class 들어왔다_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004,4003], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52100108_QD__MAIN__1$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 제어기기(self.ctx)


class 제어기기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52100108_QD__MAIN__2$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52100108_QD__MAIN__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 들킴(self.ctx)


class 들킴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(232,92,53))
        self.set_directional_light(diffuse_color=Vector3(41,21,18), specular_color=Vector3(130,130,130))
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_effect(trigger_ids=[6000], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=204, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=206, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=207, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=208, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.add_cinematic_talk(npc_id=0, msg='$52100108_QD__MAIN__4$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 들킴_02(self.ctx)


class 들킴_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.add_cinematic_talk(npc_id=25022107, msg='$52100108_QD__MAIN__5$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52100108_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 들킴_03(self.ctx)


class 들킴_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52100108_QD__MAIN__7$', duration=3000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 정리_01(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_effect(trigger_ids=[6000])
        self.set_effect(trigger_ids=[6000], visible=True)
        self.set_ambient_light(primary=Vector3(232,92,53))
        self.set_directional_light(diffuse_color=Vector3(41,21,18), specular_color=Vector3(130,130,130))
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=204, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=206, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=207, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=208, visible=True, initial_sequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 정리_02(self.ctx)


class 정리_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 정리_02(self.ctx)


class 정리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 밝아짐(self.ctx)


class 밝아짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 경보끝_01(self.ctx)


class 경보끝_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000])
        self.set_ambient_light(primary=Vector3(131,160,209))
        self.set_directional_light(diffuse_color=Vector3(134,160,143), specular_color=Vector3(130,130,130))
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=204, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=206, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=207, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=208, visible=True, initial_sequence='sf_quest_light_A01_Off')


initial_state = Ready
