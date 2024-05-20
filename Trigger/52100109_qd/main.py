""" trigger/52100109_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[91000980], quest_states=[1]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52100109, portal_id=2)
        self.visible_my_pc(is_visible=False)
        self.spawn_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103])
        self.select_camera_path(path_ids=[4001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 삼자대면(self.ctx)


class 삼자대면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005,4002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 삼자대면_02(self.ctx)


class 삼자대면_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=5000.0)
        self.add_cinematic_talk(npc_id=11004614, msg='$52100109_QD__MAIN__0$', align=Align.Left, illust_id='Eone_normal', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 삼자대면_02_01(self.ctx)


class 삼자대면_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=8500.0)
        self.add_cinematic_talk(npc_id=11004616, msg='$52100109_QD__MAIN__1$', align=Align.Right, illust_id='Bliche_closeEye', duration=4500)
        self.add_cinematic_talk(npc_id=11004616, msg='$52100109_QD__MAIN__2$', align=Align.Right, illust_id='Bliche_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8500):
            return 삼자대면_02_02(self.ctx)


class 삼자대면_02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=9000.0)
        self.add_cinematic_talk(npc_id=11004614, msg='$52100109_QD__MAIN__3$', align=Align.Left, illust_id='Eone_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004614, msg='$52100109_QD__MAIN__4$', align=Align.Left, illust_id='Eone_serious', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 삼자대면_02_03(self.ctx)


class 삼자대면_02_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=5200.0)
        self.add_cinematic_talk(npc_id=11004616, msg='$52100109_QD__MAIN__5$', align=Align.Right, illust_id='Bliche_normal', duration=2000)
        self.add_cinematic_talk(npc_id=11004616, msg='$52100109_QD__MAIN__6$', align=Align.Right, illust_id='Bliche_normal', duration=3200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5200):
            return 삼자대면_02_04(self.ctx)


class 삼자대면_02_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3200.0)
        self.add_cinematic_talk(npc_id=11004614, msg='$52100109_QD__MAIN__7$', align=Align.Left, illust_id='Eone_closeEye', duration=3200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3200):
            return 삼자대면_03(self.ctx)


class 삼자대면_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=19000.0)
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.add_cinematic_talk(npc_id=11004615, msg='$52100109_QD__MAIN__8$', align=Align.Left, illust_id='siman_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 삼자대면_03_00(self.ctx)


class 삼자대면_03_00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.add_cinematic_talk(npc_id=11004615, msg='$52100109_QD__MAIN__9$', align=Align.Left, illust_id='siman_normal', duration=5000)
        self.add_cinematic_talk(npc_id=11004615, msg='$52100109_QD__MAIN__10$', align=Align.Left, illust_id='siman_normal', duration=5000)
        self.add_cinematic_talk(npc_id=11004615, msg='$52100109_QD__MAIN__11$', align=Align.Left, illust_id='siman_normal', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 삼자대면_03_01(self.ctx)


class 삼자대면_03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=5000.0)
        self.add_cinematic_talk(npc_id=11004614, msg='$52100109_QD__MAIN__12$', align=Align.Left, illust_id='Eone_serious', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 삼자대면_03_02(self.ctx)


class 삼자대면_03_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=4500.0)
        self.add_cinematic_talk(npc_id=11004616, msg='$52100109_QD__MAIN__13$', align=Align.Right, illust_id='Bliche_closeEye', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 삼자대면_03_03(self.ctx)


class 삼자대면_03_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=8500.0)
        self.add_cinematic_talk(npc_id=11004614, msg='$52100109_QD__MAIN__14$', align=Align.Left, illust_id='Eone_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004614, msg='$52100109_QD__MAIN__15$', align=Align.Left, illust_id='Eone_closeEye', duration=4500)
        self.add_cinematic_talk(npc_id=11004616, msg='$52100109_QD__MAIN__16$', align=Align.Right, illust_id='Bliche_closeEye', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11300):
            return 삼자대면_03_04(self.ctx)


class 삼자대면_03_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=4500.0)
        self.add_cinematic_talk(npc_id=11004616, msg='$52100109_QD__MAIN__17$', align=Align.Right, illust_id='Bliche_normal', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 삼자대면_04(self.ctx)


class 삼자대면_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3200.0)
        self.add_cinematic_talk(npc_id=11004614, msg='$52100109_QD__MAIN__18$', align=Align.Left, illust_id='Eone_normal', duration=3200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3200):
            return 삼자대면_04_01(self.ctx)


class 삼자대면_04_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=4500.0)
        self.add_cinematic_talk(npc_id=11004616, msg='$52100109_QD__MAIN__19$', align=Align.Right, illust_id='Bliche_normal', duration=4500)
        self.add_cinematic_talk(npc_id=11004615, msg='$52100109_QD__MAIN__20$', align=Align.Left, illust_id='siman_normal', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 삼자대면_04_02(self.ctx)


class 삼자대면_04_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=8000.0)
        self.add_cinematic_talk(npc_id=11004614, msg='$52100109_QD__MAIN__21$', align=Align.Left, illust_id='Eone_smile', duration=4000)
        self.add_cinematic_talk(npc_id=11004615, msg='$52100109_QD__MAIN__22$', align=Align.Right, illust_id='siman_normal', duration=4000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 삼자대면끝(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 정리(self.ctx)


class 삼자대면끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 정리(self.ctx)


class 정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.visible_my_pc(is_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 정리_02(self.ctx)


class 정리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=2001, achieve='Georg')


initial_state = Wait
