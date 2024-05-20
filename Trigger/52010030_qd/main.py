""" trigger/52010030_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


"""
시련의 동굴 : 52010030
에바고르 좌절씬
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_portal(portal_id=1)
        self.set_effect(trigger_ids=[5001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2001]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.spawn_monster(spawn_ids=[101]) # 에바고르: 11003391

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에바고르_독백_01(self.ctx)


class 에바고르_독백_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Down_Idle_A', duration=200000.0) # 에바고르 좌절모션
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__0$')
        self.set_scene_skip(state=종료, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에바고르_독백_02(self.ctx)


class 에바고르_독백_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에바고르_독백_02_01(self.ctx)


class 에바고르_독백_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__2$', arg3=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에바고르_독백_03(self.ctx)


class 에바고르_독백_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__3$', arg3=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에바고르_독백_04(self.ctx)


class 에바고르_독백_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에바고르_좌절_01(self.ctx)


class 에바고르_좌절_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4004,4001], return_view=False) # 에바고르 정면
        self.add_cinematic_talk(npc_id=11003391, msg='$52010030_QD__MAIN__5$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에바고르_좌절_02(self.ctx)


class 에바고르_좌절_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003470, msg='$52010030_QD__MAIN__6$', duration=2000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003470, msg='$52010030_QD__MAIN__7$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에바고르_좌절_03(self.ctx)


class 에바고르_좌절_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Attack_Idle_A', duration=200000.0) # 에바고르 좌절모션
        self.add_cinematic_talk(npc_id=11003391, msg='$52010030_QD__MAIN__8$', duration=2000, align=Align.Left)
        self.select_camera_path(path_ids=[4002], return_view=False) # 에바고르 얼굴 돌림

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 뮤테라피온_등장_01(self.ctx)


class 뮤테라피온_등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        # self.spawn_monster(spawn_ids=[201])
        self.add_cinematic_talk(npc_id=11003470, msg='$52010030_QD__MAIN__9$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 뮤테라피온_등장_02(self.ctx)


class 뮤테라피온_등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.select_camera_path(path_ids=[2002,4003], return_view=False) # 뮤테라 피온 줌인
        self.add_cinematic_talk(npc_id=11003470, msg='$52010030_QD__MAIN__10$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 잠시뒤(self.ctx)


class 잠시뒤(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52010030_QD__MAIN__11$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 잠시뒤_1(self.ctx)


class 잠시뒤_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000146, portal_id=3)


initial_state = idle
