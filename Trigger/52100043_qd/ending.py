""" trigger/52100043_qd/ending.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Ending_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[720]):
            return Ending_Camera_1(self.ctx)


class Ending_Camera_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=500, enable=False)
        self.select_camera_path(path_ids=[500,501], return_view=False)
        self.set_effect(trigger_ids=[5000])
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])
        self.set_mesh(trigger_ids=[4993])
        self.set_mesh(trigger_ids=[4994])
        self.set_mesh(trigger_ids=[4995])
        self.set_mesh(trigger_ids=[4996])
        self.set_mesh(trigger_ids=[4997])
        self.set_mesh(trigger_ids=[4998])
        self.set_mesh(trigger_ids=[4999])
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[600,601,602], auto_target=False)
        self.set_mesh(trigger_ids=[4993], visible=True)
        self.set_mesh(trigger_ids=[4994], visible=True)
        self.set_mesh(trigger_ids=[4995], visible=True)
        self.set_mesh(trigger_ids=[4996], visible=True)
        self.set_mesh(trigger_ids=[4997], visible=True)
        self.set_mesh(trigger_ids=[4998], visible=True)
        self.set_mesh(trigger_ids=[4999], visible=True)
        self.visible_my_pc(is_visible=True)
        self.move_npc(spawn_id=600, patrol_name='MS2PatrolData0')
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData1')
        self.move_npc(spawn_id=602, patrol_name='MS2PatrolData2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Ending_Talk_1(self.ctx)


class Ending_Talk_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=narration01)
        self.select_camera(trigger_id=1000)
        self.set_npc_emotion_sequence(spawn_id=602, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11001566, illust_id='11001566', msg='$52100043_QD__ENDING__0$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Ending_Talk_2(self.ctx)


class Ending_Talk_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=1001)
        self.set_npc_emotion_sequence(spawn_id=601, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11001567, illust_id='11001567', msg='$52100043_QD__ENDING__1$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Ending_Talk_3(self.ctx)


class Ending_Talk_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=1002)
        self.set_npc_emotion_sequence(spawn_id=600, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11001568, illust_id='11001568', msg='$52100043_QD__ENDING__2$', duration=5000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Shake_Camera(self.ctx)


class Shake_Camera(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True)
        self.select_camera_path(path_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4006,4007,4008,4006,4007,4005,4006,4007,4008,4006,4007,4008,4006,4007,4008,4006,4007,4008,4008,4006,4007,4008,4006,4007,4008,4006,4007,4008])
        self.add_cinematic_talk(npc_id=11001567, illust_id='11001567', msg='$52100043_QD__ENDING__3$', duration=2000, align=Align.Left)
        self.destroy_monster(spawn_ids=[601,602], arg2=False)
        self.spawn_monster(spawn_ids=[701,702], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Ending_Talk_4(self.ctx)


class Ending_Talk_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[701,702], arg2=False)
        self.destroy_monster(spawn_ids=[601,602])
        self.set_effect(trigger_ids=[5000], visible=True)
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_effect(trigger_ids=[5004], visible=True)
        self.set_effect(trigger_ids=[5005], visible=True)
        self.add_cinematic_talk(npc_id=11001566, illust_id='11001566', msg='$52100043_QD__ENDING__4$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Ending_Talk_5(self.ctx)


class Ending_Talk_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7000,7001], return_view=False)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.add_cinematic_talk(npc_id=11001568, illust_id='11001568', msg='$52100043_QD__ENDING__5$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return del6000(self.ctx)


class del6000(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_blackfast.xml')
        self.destroy_monster(spawn_ids=[600])
        self.spawn_monster(spawn_ids=[700], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return Ending_Talk_6(self.ctx)


class Ending_Talk_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_blackfast.xml')
        self.select_camera(trigger_id=6000)
        self.move_npc(spawn_id=700, patrol_name='MS2PatrolData4')
        self.add_cinematic_talk(npc_id=11001568, illust_id='11001568', msg='$52100043_QD__ENDING__6$', duration=3000, align=Align.Left)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_time_scale(enable=True, start_scale=0.8, end_scale=0.03, duration=3.0, interpolator=1)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_effect(trigger_ids=[5006], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Ending_Talk_7(self.ctx)


class Ending_Talk_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        self.select_camera_path(path_ids=[3000,3001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return narration01(self.ctx)


class narration01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[-1])
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return narration02(self.ctx)


class narration02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=Map_Warf)
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return narration03(self.ctx)


class narration03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__9$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return narration04(self.ctx)


class narration04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__10$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return narration05(self.ctx)


class narration05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__11$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return narration06(self.ctx)


class narration06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52100043_QD__ENDING__12$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Map_Warf(self.ctx)


class Map_Warf(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[-1])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.move_user(map_id=52010068, portal_id=1)


initial_state = Ending_Ready
