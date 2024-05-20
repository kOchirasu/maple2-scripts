""" trigger/52000200_qd/52000200.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2001]):
            return CameraEffect01(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_quest_accept(quest_id=10003419) # 퀘스트 강제 수락
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[101]) # 바론
        self.spawn_monster(spawn_ids=[102]) # 칼
        self.spawn_monster(spawn_ids=[103]) # 에레브

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect02_02(self.ctx)


class CameraEffect02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000200_QD__52000200__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 여제알현(self.ctx)


class 여제알현(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__1$', illust_id='Ereb_normal', align=Align.Left, duration=4000)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__2$', align=Align.Right, illust_id='Karl_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__3$', illust_id='Ereb_normal', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 여제알현_02(self.ctx)


class 여제알현_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004,4005], return_view=False)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__4$', align=Align.Right, illust_id='Karl_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__5$', illust_id='Ereb_normal', align=Align.Left, duration=4500)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__6$', illust_id='Ereb_normal', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11500):
            return 여제알현_03(self.ctx)


class 여제알현_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__7$', align=Align.Right, illust_id='Karl_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__8$', align=Align.Right, illust_id='Karl_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__9$', illust_id='Ereb_surprise', align=Align.Left, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return 여제알현_04(self.ctx)


class 여제알현_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3002')
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 여제알현_05(self.ctx)


class 여제알현_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004782, msg='$52000200_QD__52000200__10$', align=Align.Left, illust_id='Ruana_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__11$', align=Align.Left, illust_id='Ereb_surprise', duration=4000)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__12$', align=Align.Right, illust_id='Karl_normal', duration=4500)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__13$', align=Align.Right, illust_id='Karl_normal', duration=4500)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__14$', align=Align.Left, illust_id='Ereb_surprise', duration=3000)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__15$', align=Align.Right, illust_id='Karl_normal', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=25000):
            return 여제알현_06(self.ctx)


class 여제알현_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007,4008], return_view=False)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__16$', align=Align.Left, illust_id='Ereb_surprise', duration=4500)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__17$', align=Align.Right, illust_id='Karl_normal', duration=2800)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__18$', align=Align.Right, illust_id='Karl_normal', duration=4500)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__19$', align=Align.Left, illust_id='Ereb_surprise', duration=4000)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__20$', align=Align.Left, illust_id='Ereb_closeEye', duration=4000)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000200_QD__52000200__21$', align=Align.Left, illust_id='Ereb_closeEye', duration=4000)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__22$', align=Align.Right, illust_id='Karl_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=27800):
            return 음모(self.ctx)


class 음모(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 음모_02(self.ctx)


class 음모_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000200_QD__52000200__23$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 음모_03(self.ctx)


class 음모_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11001975, msg='$52000200_QD__52000200__24$', align=Align.Left, duration=4500)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__25$', align=Align.Right, illust_id='Karl_normal', duration=2800)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__26$', align=Align.Right, illust_id='Karl_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__27$', align=Align.Right, illust_id='Karl_normal', duration=3000)
        self.add_cinematic_talk(npc_id=11000264, msg='$52000200_QD__52000200__28$', align=Align.Left, illust_id='Radin_normal', duration=4500)
        self.add_cinematic_talk(npc_id=11000264, msg='$52000200_QD__52000200__29$', align=Align.Left, illust_id='Radin_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004778, msg='$52000200_QD__52000200__30$', align=Align.Right, illust_id='Karl_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11000264, msg='$52000200_QD__52000200__31$', align=Align.Left, illust_id='Radin_normal', duration=4000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=29000):
            return 이동(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True) # 유저 투명 처리
        self.move_user(map_id=52000190, portal_id=5001)


initial_state = start
