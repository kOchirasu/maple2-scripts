""" trigger/52000113_qd/52000113.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class START(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10011]):
            return 대기01(self.ctx)


class 대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Quit02, action='exit')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.spawn_npc_range(range_ids=[202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221])
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 쉐도우클로
        self.set_cinematic_ui(type=1)
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_203') # 로그스들 이동
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_204') # 로그스들 이동
        self.move_npc(spawn_id=215, patrol_name='MS2PatrolData_215') # 로그스들 이동
        self.move_npc(spawn_id=216, patrol_name='MS2PatrolData_216') # 로그스들 이동
        self.move_npc(spawn_id=217, patrol_name='MS2PatrolData_217') # 로그스들 이동
        self.move_npc(spawn_id=219, patrol_name='MS2PatrolData_219') # 로그스들 이동
        self.move_npc(spawn_id=220, patrol_name='MS2PatrolData_220') # 로그스들 이동
        self.move_npc(spawn_id=221, patrol_name='MS2PatrolData_221') # 로그스들 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera01(self.ctx)


class camera01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[1000,1001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera02(self.ctx)


class camera02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1002,1003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera03(self.ctx)


class camera03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1004,1005], return_view=False)
        self.move_npc(spawn_id=208, patrol_name='MS2PatrolData_Rogues_come') # 로그스들 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera04(self.ctx)


class camera04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1006,1007], return_view=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003338, illust_id='0', msg='$52000113_QD__52000113__0$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera05(self.ctx)


class camera05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1008,1009], return_view=False)
        self.add_cinematic_talk(npc_id=11003185, illust_id='0', msg='$52000113_QD__52000113__1$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera06(self.ctx)


class camera06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1010], return_view=False)
        self.add_cinematic_talk(npc_id=11003185, illust_id='0', msg='$52000113_QD__52000113__2$', duration=4000, align=Align.Right)
        self.move_npc(spawn_id=208, patrol_name='MS2PatrolData_Rogues_out') # 로그스들 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera07(self.ctx)


class camera07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[1011,1012], return_view=False)
        self.add_cinematic_talk(npc_id=11003185, illust_id='0', msg='$52000113_QD__52000113__3$', duration=5000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera08(self.ctx)


class camera08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003185, illust_id='0', msg='$52000113_QD__52000113__4$', duration=5000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit01_1(self.ctx)


class Quit01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user(map_id=2000062, portal_id=13)


initial_state = START
