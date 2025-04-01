""" trigger/52100300_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align, BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990002, key='Spawn', value=0)
        self.set_user_value(trigger_id=99990003, key='RandomBomb', value=0)
        self.set_user_value(trigger_id=99990004, key='Laser', value=0)
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=3)
        self.set_interact_object(trigger_ids=[10002185], state=0) # 엘리베이터 발판
        self.enable_spawn_point_pc(spawn_id=100, is_enable=True) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawn_id=101)
        self.enable_spawn_point_pc(spawn_id=102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 연출시작(self.ctx)


# 연출시작
class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52100300, portal_id=5001)
        self.spawn_monster(spawn_ids=[351])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작_2(self.ctx)


class 연출시작_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[4004,4005], return_view=False)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2900):
            return 연출시작_2_02(self.ctx)


class 연출시작_2_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006,4007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출시작_2_03(self.ctx)


class 연출시작_2_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작_3(self.ctx)


class 연출시작_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4001,4002], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52100300_QD__MAIN__12$', align=Align.bottomLeft, duration=3000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출시작_4(self.ctx)


class 연출시작_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52100300_QD__MAIN__13$', duration=3500)
        self.add_cinematic_talk(npc_id=11004682, illust_id='11004022', align=Align.right, msg='$52100300_QD__MAIN__14$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출시작_5(self.ctx)


class 연출시작_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=351, patrol_name='MS2PatrolData_3001')
        self.add_cinematic_talk(npc_id=11004682, illust_id='11004022', align=Align.right, msg='$52100300_QD__MAIN__15$', duration=3500)
        self.add_cinematic_talk(npc_id=0, msg='$52100300_QD__MAIN__16$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출시작_6(self.ctx)


class 연출시작_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[351], arg2=False)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작_7(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[351])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작_7(self.ctx)


class 연출시작_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            self.set_event_ui_script(type=BannerType.Text, script='$52100300_QD__MAIN__0$', duration=5000)
            self.spawn_monster(spawn_ids=[101,102,103], auto_target=False)
            return 추가대사_01(self.ctx)


# 연출끝

"""
class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            self.set_event_ui_script(type=BannerType.Text, script='$52100300_QD__MAIN__0$', duration=5000)
            self.spawn_monster(spawn_ids=[101,102,103], auto_target=False)
            return 추가대사_01(self.ctx)
"""

class 추가대사_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.set_user_value(trigger_id=99990004, key='Laser', value=1)
            self.side_npc_talk(npc_id=29500101, illust='ArcheonBlack_Normal', script='$52100300_QD__MAIN__1$', duration=5000)
            return 추가대사_02(self.ctx)


class 추가대사_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103]):
            self.side_npc_talk(npc_id=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__2$', duration=5000)
            return 추가대사_03(self.ctx)


class 추가대사_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', script='$52100300_QD__MAIN__3$', duration=5000)
            return 엘리베이터_체크(self.ctx)


class 엘리베이터_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.side_npc_talk(npc_id=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__4$', duration=5000)
            return 엘리베이터_스위치(self.ctx)


class 엘리베이터_스위치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002185], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002185], state=0):
            return 엘리베이터_활성화(self.ctx)


class 엘리베이터_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[5001], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[903]):
            return 아르케온_탑승_가이드(self.ctx)


class 아르케온_탑승_가이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$52100300_QD__MAIN__5$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[711]):
            return 레이저_패턴_시작(self.ctx)


class 레이저_패턴_시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[904]):
            return 갈림길_전투(self.ctx)


class 갈림길_전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201,202,203,204], auto_target=False)
        self.set_actor(trigger_id=9001, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_end')
        self.set_mesh(trigger_ids=[1001], visible=True)
        self.enable_spawn_point_pc(spawn_id=100) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawn_id=101, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[905]):
            return 짜투리_전투(self.ctx)


class 짜투리_전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301,302,303,304], auto_target=False)
        self.set_mesh(trigger_ids=[2001,2002,2003,2004], visible=True)
        self.set_mesh(trigger_ids=[30000,30010,30020,30030], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[911]):
            return 웨이브_시작(self.ctx)


class 웨이브_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=29000170, illust='ArcaneBlader_unfair', script='$52100300_QD__MAIN__6$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 추가대사_04(self.ctx)


class 추가대사_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990002, key='Spawn', value=1)
        self.set_mesh(trigger_ids=[2001,2002,2003,2004])
        self.set_mesh(trigger_ids=[30000,30010,30020,30030])
        self.side_npc_talk(npc_id=29500101, illust='ArcheonBlack_Normal', script='$52100300_QD__MAIN__7$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnRoomEnd') == 1:
            self.set_actor(trigger_id=9001, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_start')
            return 길열림(self.ctx)


class 길열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1001])
        self.set_mesh(trigger_ids=[2001,2002,2003,2004], visible=True)
        self.set_mesh(trigger_ids=[30000,30010,30020,30030], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[921]):
            return 지뢰방_시작(self.ctx)


class 지뢰방_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=100) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawn_id=101)
        self.enable_spawn_point_pc(spawn_id=102, is_enable=True)
        self.set_actor(trigger_id=9002, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_end')
        self.set_actor(trigger_id=9003, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_end')
        self.set_actor(trigger_id=9004, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_end')
        self.set_mesh(trigger_ids=[5001])
        self.set_mesh(trigger_ids=[3001,3002,3003], visible=True)
        self.set_user_value(trigger_id=99990003, key='RandomBomb', value=1)
        self.side_npc_talk(npc_id=29500101, illust='ArcheonBlack_Normal', script='$52100300_QD__MAIN__8$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 추가대사_05(self.ctx)


class 추가대사_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__9$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 추가대사_06(self.ctx)


class 추가대사_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', script='$52100300_QD__MAIN__10$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RandomBombEnd') == 1:
            self.set_user_value(trigger_id=99990004, key='Laser', value=0)
            return 보스전(self.ctx)


class 보스전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__11$', duration=5000)
        self.set_actor(trigger_id=9002, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_start')
        self.set_mesh(trigger_ids=[3001])
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
