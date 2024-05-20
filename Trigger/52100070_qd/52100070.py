""" trigger/52100070_qd/52100070.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=400)
        self.set_effect(trigger_ids=[5000])
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5006])
        self.set_effect(trigger_ids=[5007])
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1000]):
            return narration01(self.ctx)


class narration01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=9, script='$52100070_QD__52100070__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 암전1(self.ctx)


class 암전1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return Camera_Move_01(self.ctx)


class Camera_Move_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[400,401], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52100070_QD__52100070__1$', desc='$52100070_QD__52100070__2$', align=Align.Bottom | Align.Left, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=연출끝)
        self.spawn_monster(spawn_ids=[101,102,103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 전경카메라1(self.ctx)


class 전경카메라1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600)
        self.select_camera_path(path_ids=[600,601], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 퐈이야(self.ctx)


class 퐈이야(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_effect(trigger_ids=[5004], visible=True)
        self.set_effect(trigger_ids=[5007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 이슈라카메라1(self.ctx)


class 이슈라카메라1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[402,403], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이슈라카메라2(self.ctx)


class 이슈라카메라2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500)
        self.select_camera_path(path_ids=[500,501], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이슈라카메라3(self.ctx)


class 이슈라카메라3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=404, enable=False)
        self.select_camera_path(path_ids=[404,405], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이슈라카메라4(self.ctx)


class 이슈라카메라4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=406, enable=False)
        self.select_camera_path(path_ids=[406,407], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 렌듀비앙이동1(self.ctx)


class 렌듀비앙이동1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=0.5, end_scale=0.5, duration=50.0, interpolator=1)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_11003867')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 유페리아이동1(self.ctx)


class 유페리아이동1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_11003868')
        self.set_effect(trigger_ids=[5000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 이슈라이동1(self.ctx)


class 이슈라이동1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5005], visible=True)
        self.set_effect(trigger_ids=[5006], visible=True)
        self.set_time_scale(enable=True, start_scale=0.3, end_scale=0.3, duration=50.0, interpolator=1)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_11003866')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000])
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5006])
        self.set_effect(trigger_ids=[5007])
        self.set_time_scale(start_scale=0.5, end_scale=0.5, duration=50.0, interpolator=1)
        self.destroy_monster(spawn_ids=[101,102,103], arg2=False)
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.visible_my_pc(is_visible=True)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52010068, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Ready(self.ctx)


initial_state = Ready
