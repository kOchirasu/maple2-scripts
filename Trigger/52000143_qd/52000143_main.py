""" trigger/52000143_qd/52000143_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_mesh(trigger_ids=[4003,4004,4005,4006], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return 잠시대기(self.ctx)


class 잠시대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.add_buff(box_ids=[701], skill_id=70000124, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 한번더대기(self.ctx)


class 한번더대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 로베와대화_01(self.ctx)


class 로베와대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=로베와전투_01, action='nextState')
        self.add_cinematic_talk(npc_id=0, msg='$52000143_QD__52000143_MAIN__0$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 로베와대화_02(self.ctx)


class 로베와대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000143_QD__52000143_MAIN__1$', duration=3500, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 로베와대화_03(self.ctx)


class 로베와대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000143_QD__52000143_MAIN__2$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 로베와대화_04(self.ctx)


class 로베와대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000143_QD__52000143_MAIN__3$', duration=2500, illust_id='Robe_normal', align=Align.Right)
        self.add_cinematic_talk(npc_id=11003401, msg='$52000143_QD__52000143_MAIN__4$', duration=3000, illust_id='Robe_normal', align=Align.Right)
        self.add_cinematic_talk(npc_id=11003401, msg='$52000143_QD__52000143_MAIN__5$', duration=2500, illust_id='Robe_normal', align=Align.Right)
        self.add_cinematic_talk(npc_id=11003401, msg='$52000143_QD__52000143_MAIN__6$', duration=3000, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 로베와대화_05(self.ctx)


class 로베와대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000143_QD__52000143_MAIN__7$', duration=3500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 로베와대화_06(self.ctx)


class 로베와대화_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000143_QD__52000143_MAIN__8$', duration=1000, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 로베와대화_07(self.ctx)


class 로베와대화_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 로베와전투_01(self.ctx)


class 로베와전투_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 로베와전투_02(self.ctx)


class 로베와전투_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 로베와전투_03(self.ctx)


class 로베와전투_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=25201431, text_id=25201431)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return 로베와전투_04(self.ctx)


class 로베와전투_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entity_id=25201431)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 로베와전투_05(self.ctx)


class 로베와전투_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__9$', duration=2500, align=Align.Center)
        self.move_user(map_id=52000143, portal_id=99)
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 알론등장_01(self.ctx)


class 알론등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 알론등장_02(self.ctx)


class 알론등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_2002')
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_2003')
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 자대화_03_3(self.ctx)


class 자대화_03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002,8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 자대화_04_3(self.ctx)


class 자대화_04_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=마무리_01, action='nextState')
        self.add_cinematic_talk(npc_id=11003401, msg='$52000143_QD__52000143_MAIN__10$', duration=2500, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 자대화_05_3(self.ctx)


class 자대화_05_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__11$', duration=3000, illust_id='Alon_normal', align=Align.Center)
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__12$', duration=2500, illust_id='Alon_normal', align=Align.Center)
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__13$', duration=3000, illust_id='Alon_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 자대화_06_3(self.ctx)


class 자대화_06_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000143_QD__52000143_MAIN__14$', duration=3500, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 자대화_07_3(self.ctx)


class 자대화_07_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__15$', duration=3000, illust_id='Alon_normal', align=Align.Center)
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__16$', duration=3000, illust_id='Alon_normal', align=Align.Center)
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__17$', duration=3000, illust_id='Alon_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 자대화_08_3(self.ctx)


class 자대화_08_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003401, msg='$52000143_QD__52000143_MAIN__18$', duration=2500, illust_id='Robe_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 자대화_09_3(self.ctx)


class 자대화_09_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000143_QD__52000143_MAIN__19$', duration=2500, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 자대화_10_3(self.ctx)


class 자대화_10_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__20$', duration=3000, illust_id='Alon_normal', align=Align.Center)
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__21$', duration=2500, illust_id='Alon_normal', align=Align.Center)
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__22$', duration=3000, illust_id='Alon_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 자대화_10_1_3(self.ctx)


class 자대화_10_1_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 자대화_10_2_3(self.ctx)


class 자대화_10_2_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000143_QD__52000143_MAIN__23$', duration=2500, align=Align.Left)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_2006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 자대화_11_3(self.ctx)


class 자대화_11_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_2005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 자대화_11_1_3(self.ctx)


class 자대화_11_1_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000143_QD__52000143_MAIN__28$', duration=3000, align=Align.Left)
        self.set_pc_emotion_sequence(sequence_names=['Knight_Bore_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 자대화_12_3(self.ctx)


class 자대화_12_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__24$', duration=5500, illust_id='Alon_normal', align=Align.Right)
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__25$', duration=5500, illust_id='Alon_normal', align=Align.Right)
        self.add_cinematic_talk(npc_id=11003404, msg='$52000143_QD__52000143_MAIN__26$', duration=5000, illust_id='Alon_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=17000):
            return 마무리_01(self.ctx)


class 마무리_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마무리_02(self.ctx)


class 마무리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52000143_QD__52000143_MAIN__27$')
        self.remove_buff(box_id=701, skill_id=70000124)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000144, portal_id=1)


initial_state = 준비
