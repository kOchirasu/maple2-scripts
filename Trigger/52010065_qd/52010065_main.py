""" trigger/52010065_qd/52010065_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class PC체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            self.visible_my_pc(is_visible=False)
            return 준비_01(self.ctx)


class 준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.visible_my_pc(is_visible=True) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.set_visible_ui(ui_names=['UpperHudDialog','MessengerBrowser','ExpBar','GroupMessengerBrowser','QuestGuideDialog','MinimapDialog','AdPushDialog','SnowmanEventDialog'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 준비_02(self.ctx)


class 준비_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_visible_ui(ui_names=['MessengerBrowser','GroupMessengerBrowser'])
        self.add_buff(box_ids=[701], skill_id=99910320, level=1, is_player=False) # 검마 변신
        self.add_buff(box_ids=[701], skill_id=99910320, level=1, is_player=False, is_skill_set=False) # 검마 변신
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 발록
        self.set_mesh(trigger_ids=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[91000076], quest_states=[3]):
            return 퀘스트완료_02(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[91000076], quest_states=[2]):
            return 검마등장_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[91000076], quest_states=[1]):
            return 검마등장_01(self.ctx)


class 검마등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 검마등장_02(self.ctx)


class 검마등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 검마등장_03(self.ctx)


class 검마등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 벨라등장_01(self.ctx)


class 벨라등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 저멀리발록_01(self.ctx)


class 저멀리발록_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 저멀리발록_02(self.ctx)


class 저멀리발록_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.set_scene_skip(state=스킵1_01, action='nextState')
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 발록검마인사_01(self.ctx)


class 발록검마인사_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003819, msg='$52010065_QD__52010065_main__0$', duration=3000, illust_id='balrog_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 발록검마인사_02(self.ctx)


class 발록검마인사_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001811, msg='$52010065_QD__52010065_main__1$', duration=3000, illust_id='BlackWizard_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 발록검마인사_03(self.ctx)


class 발록검마인사_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003819, msg='$52010065_QD__52010065_main__2$', duration=3000, illust_id='balrog_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 다리끊기_01(self.ctx)


class 다리끊기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다리끊기_02(self.ctx)


class 다리끊기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4003,4006,4010])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=50):
            return 다리끊기_03(self.ctx)


class 다리끊기_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4004,4005,4014])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=50):
            return 다리끊기_04(self.ctx)


class 다리끊기_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4007,4013,4018])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=50):
            return 다리끊기_05(self.ctx)


class 다리끊기_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4009,4015,4022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=50):
            return 다리끊기_06(self.ctx)


class 다리끊기_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4008,4012,4017])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=50):
            return 다리끊기_07(self.ctx)


class 다리끊기_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4011,4016,4023])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=50):
            return 다리끊기_08(self.ctx)


class 다리끊기_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4019,4021,4024])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=50):
            return 다리끊기_09(self.ctx)


class 다리끊기_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4020,4025])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 비웃는검마_01(self.ctx)


class 비웃는검마_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 비웃는검마_02(self.ctx)


class 비웃는검마_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001811, msg='$52010065_QD__52010065_main__3$', duration=3000, illust_id='BlackWizard_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 비웃는검마_03(self.ctx)


class 비웃는검마_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003820, msg='$52010065_QD__52010065_main__4$', duration=3000, illust_id='Bella_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11001811, msg='$52010065_QD__52010065_main__5$', duration=3000, illust_id='BlackWizard_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 용암건너기_01(self.ctx)


class 스킵1_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025])

    def on_tick(self) -> trigger_api.Trigger:
        return 용암건너기_01(self.ctx)


class 용암건너기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.reset_camera(interpolation_time=1.0)
        self.set_mesh(trigger_ids=[4026], visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 용암건너기_02(self.ctx)


class 용암건너기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25210651, text_id=25210651)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return 용암건너기완료_01(self.ctx)


class 용암건너기완료_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 용암건너기완료_02(self.ctx)


class 용암건너기완료_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010065, portal_id=11)
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 퀘스트완료_01(self.ctx)


class 퀘스트완료_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.hide_guide_summary(entity_id=25210651)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[91000076], quest_states=[3]):
            return 퀘스트완료_02(self.ctx)


class 퀘스트완료_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 검마퇴장_01(self.ctx)


class 검마퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006], return_view=False)
        self.visible_my_pc(is_visible=False)
        self.destroy_monster(spawn_ids=[103])
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.destroy_monster(spawn_ids=[104])
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 검마퇴장_02(self.ctx)


class 검마퇴장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=마무리, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 검마퇴장_03(self.ctx)


class 검마퇴장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 검마퇴장_04(self.ctx)


class 검마퇴장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006,8007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 검마퇴장_05(self.ctx)


class 검마퇴장_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007,8008], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 검마퇴장_06(self.ctx)


class 검마퇴장_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001811, msg='$52010065_QD__52010065_main__6$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11001811, msg='$52010065_QD__52010065_main__7$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010061, portal_id=1)


initial_state = PC체크
