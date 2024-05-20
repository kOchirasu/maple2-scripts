""" trigger/52020040_qd/52020040.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import Align


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2001]):
            return wait_02(self.ctx)


class wait_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(trigger_ids=[6000])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wait_03(self.ctx)


class wait_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52020040, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 크리티아스로(self.ctx)


class 크리티아스로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[4001,4002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 크리티아스로_02(self.ctx)


class 크리티아스로_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003,4004,4005], return_view=False)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_B', duration=100000000000.0)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_normal', align=Align.Left, msg='$52020040_QD__52020040__0$', duration=3000)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_smile', align=Align.Right, msg='$52020040_QD__52020040__1$', duration=3000)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_normal', align=Align.Left, msg='$52020040_QD__52020040__2$', duration=3000)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 크리티아스로_02_01(self.ctx)


class 크리티아스로_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.show_caption(type='HorizonCaption', title='$52020040_QD__52020040__3$', align=Align.Bottom | Align.Left, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 크리티아스로_03(self.ctx)


class 크리티아스로_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.add_cinematic_talk(npc_id=11004436, illust_id='Schatten_smile', align=Align.Left, msg='$52020040_QD__52020040__4$', duration=3000)
        self.add_cinematic_talk(npc_id=11004438, illust_id='Mason_closeEye', align=Align.Right, msg='$52020040_QD__52020040__5$', duration=3000)
        self.add_cinematic_talk(npc_id=11004435, illust_id='Conder_smile', align=Align.Left, msg='$52020040_QD__52020040__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 크리티아스로_04(self.ctx)


class 크리티아스로_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(232,92,53))
        self.set_directional_light(diffuse_color=Vector3(41,21,18), specular_color=Vector3(130,130,130))
        self.add_cinematic_talk(npc_id=11004435, illust_id='Conder_normal', align=Align.Left, msg='$52020040_QD__52020040__7$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 경보(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000], visible=True)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=204, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=206, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=207, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=208, visible=True, initial_sequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 경보_01(self.ctx)


class 경보_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_surprise', align=Align.Left, msg='$52020040_QD__52020040__8$', duration=2500)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_surprise', align=Align.Left, msg='$52020040_QD__52020040__9$', duration=2800)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_normal', align=Align.Right, msg='$52020040_QD__52020040__10$', duration=2800)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_surprise', align=Align.Left, msg='$52020040_QD__52020040__11$', duration=2800)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_normal', align=Align.Right, msg='$52020040_QD__52020040__12$', duration=2400)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_surprise', align=Align.Left, msg='$52020040_QD__52020040__13$', duration=2800)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_mad', align=Align.Right, msg='$52020040_QD__52020040__14$', duration=2800)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_surprise', align=Align.Left, msg='$52020040_QD__52020040__15$', duration=2400)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=21300):
            return 경보_02(self.ctx)


class 경보_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009,4010], return_view=False)
        self.set_effect(trigger_ids=[6000])
        self.add_cinematic_talk(npc_id=11004440, msg='$52020040_QD__52020040__16$', duration=3000)
        self.add_cinematic_talk(npc_id=11004440, msg='$52020040_QD__52020040__17$', duration=5000)
        self.add_cinematic_talk(npc_id=11004440, msg='$52020040_QD__52020040__18$', duration=2600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10200):
            return 경보끝_01(self.ctx)


class 경보끝_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
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
        self.add_cinematic_talk(npc_id=11004435, illust_id='Conder_normal', align=Align.Right, msg='$52020040_QD__52020040__19$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 경보끝_02_01(self.ctx)


class 경보끝_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 경보끝_02_02(self.ctx)


class 경보끝_02_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 경보끝_02(self.ctx)


class 경보끝_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4012], return_view=False)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_surprise', align=Align.Left, msg='$52020040_QD__52020040__20$', duration=2800)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_surprise', align=Align.Left, msg='$52020040_QD__52020040__21$', duration=2800)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_surprise', align=Align.Left, msg='$52020040_QD__52020040__22$', duration=3000)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_normal', align=Align.Right, msg='$52020040_QD__52020040__23$', duration=3000)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_normal', align=Align.Right, msg='$52020040_QD__52020040__24$', duration=3000)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_surprise', align=Align.Left, msg='$52020040_QD__52020040__25$', duration=3000)
        self.add_cinematic_talk(npc_id=11004435, illust_id='Conder_normal', align=Align.Right, msg='$52020040_QD__52020040__26$', duration=3000)
        self.add_cinematic_talk(npc_id=11004436, illust_id='Schatten_surprise', align=Align.Left, msg='$52020040_QD__52020040__27$', duration=3000)
        self.add_cinematic_talk(npc_id=11004435, illust_id='Conder_normal', align=Align.Right, msg='$52020040_QD__52020040__28$', duration=2500)
        self.add_cinematic_talk(npc_id=11004438, illust_id='Mason_normal', align=Align.Left, msg='$52020040_QD__52020040__29$', duration=3000)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_normal', align=Align.Right, msg='$52020040_QD__52020040__30$', duration=2500)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_normal', align=Align.Right, msg='$52020040_QD__52020040__31$', duration=3000)
        self.add_cinematic_talk(npc_id=11004438, illust_id='Mason_normal', align=Align.Left, msg='$52020040_QD__52020040__32$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52020040_QD__52020040__33$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=37800):
            return 경보끝_03(self.ctx)


class 경보끝_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011,4013], return_view=False)
        # self.set_pc_emotion_loop(sequence_name='Talk_A', duration=10000000000000.0)
        self.add_cinematic_talk(npc_id=11004438, illust_id='Mason_normal', msg='$52020040_QD__52020040__34$', align=Align.Left, duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52020040_QD__52020040__35$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52020040_QD__52020040__36$', duration=3000)
        self.add_cinematic_talk(npc_id=11004436, illust_id='Schatten_surprise', align=Align.Left, msg='$52020040_QD__52020040__37$', duration=3500)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_normal', align=Align.Right, msg='$52020040_QD__52020040__38$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52020040_QD__52020040__39$', duration=3000)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_closeEye', align=Align.Left, msg='$52020040_QD__52020040__40$', duration=2800)
        self.add_cinematic_talk(npc_id=11004437, illust_id='Neirin_normal', align=Align.Right, msg='$52020040_QD__52020040__41$', duration=3000)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_closeEye', align=Align.Left, msg='$52020040_QD__52020040__42$', duration=3000)
        self.add_cinematic_talk(npc_id=11004434, illust_id='Bliche_normal', align=Align.Left, msg='$52020040_QD__52020040__43$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52020040_QD__52020040__44$', duration=3000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=33200):
            return 이동(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이동_02(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이동_02(self.ctx)


class 이동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2020029, portal_id=2)


initial_state = wait_01
