""" trigger/52000115_qd/52000115.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class START(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 대기01(self.ctx)


class 대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[9001])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=True) # 큐브하나씩부셔지는연출
        self.set_breakable(trigger_ids=[3000])
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대기02(self.ctx)


class 대기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='exit')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 검은마법사등장
        self.select_camera_path(path_ids=[2000,2001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            return camera01(self.ctx)


class camera01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2002,2003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return camera02(self.ctx)


class camera02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2004,2005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return camera03(self.ctx)


class camera03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2006,2007], return_view=False)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_BlackMage') # 마드리아 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return camera05(self.ctx)


class camera05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2008,2009], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera06(self.ctx)


class camera06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2010,2011], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return camera08(self.ctx)


class camera07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2012,2013], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera08(self.ctx)


class camera08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2014,2015], return_view=False)
        self.destroy_monster(spawn_ids=[200])
        self.spawn_monster(spawn_ids=[203], auto_target=False) # 검은마법사등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return camera08b(self.ctx)


class camera08b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2016,2017], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        return camera09_b(self.ctx)


class camera09_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return camera09(self.ctx)


class camera09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2018], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return camera10(self.ctx)


class camera10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2020,2019], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return camera10_b(self.ctx)


class camera10_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1400):
            return camera11(self.ctx)


class camera11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_blackfast.xml')
        self.set_effect(trigger_ids=[9001], visible=True)
        self.select_camera_path(path_ids=[2022,2023], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return camera12(self.ctx)


# 오오오오오오오 쉐도우게이트강림 오오오오오오오
class camera12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_background(dds='SW_BG_Iceage_C.dds')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return camera13(self.ctx)


class camera13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.select_camera_path(path_ids=[2024,2025], return_view=False)
        self.set_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], interval=500, fade=1000.0) # 큐브하나씩부셔지는연출
        self.set_mesh(trigger_ids=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], interval=800, fade=1000.0) # 큐브하나씩부셔지는연출
        self.set_breakable(trigger_ids=[3000], enable=True)
        self.spawn_monster(spawn_ids=[204], auto_target=False) # 검은마법사등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return camera14b(self.ctx)


class camera14b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=True, interval=500, fade=1000.0) # 큐브하나씩부셔지는연출
        self.set_mesh(trigger_ids=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=True, interval=800, fade=1000.0) # 큐브하나씩부셔지는연출

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return camera14c(self.ctx)


class camera14c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], interval=500, fade=1000.0) # 큐브하나씩부셔지는연출
        self.set_mesh(trigger_ids=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], interval=800, fade=1000.0) # 큐브하나씩부셔지는연출
        self.select_camera_path(path_ids=[2026,2027], return_view=False)
        self.destroy_monster(spawn_ids=[204])
        self.spawn_monster(spawn_ids=[205], auto_target=False) # 검은마법사등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return camera15(self.ctx)


class camera15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=True, interval=500, fade=1000.0) # 큐브하나씩부셔지는연출
        self.set_mesh(trigger_ids=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=True, interval=800, fade=1000.0) # 큐브하나씩부셔지는연출
        self.select_camera_path(path_ids=[2028,2029,2030,2031], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return camera16(self.ctx)


class camera16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], interval=500, fade=1000.0) # 큐브하나씩부셔지는연출
        self.set_mesh(trigger_ids=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], interval=800, fade=1000.0) # 큐브하나씩부셔지는연출
        self.select_camera_path(path_ids=[2032,2033], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return camera17(self.ctx)


class camera17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return camera18(self.ctx)


class camera18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001811, msg='$52000115_QD__52000115__0$', duration=6000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return camera19(self.ctx)


class camera19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit01(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199], job_code=10):
            # 나이트
            return 기본종료(self.ctx)
        if self.user_detected(box_ids=[199], job_code=20):
            # 버서커
            return 버서커리스항구01(self.ctx)
        if self.user_detected(box_ids=[199], job_code=30):
            # 위자드
            return 트라이아도서관01(self.ctx)
        if self.user_detected(box_ids=[199], job_code=40):
            # 프리스트
            self.move_user(map_id=52000139, portal_id=1)
        if self.user_detected(box_ids=[199], job_code=50):
            # 레인저
            return 기본종료(self.ctx)
        if self.user_detected(box_ids=[199], job_code=60):
            # 헤비거너
            return 기본종료(self.ctx)
        if self.user_detected(box_ids=[199], job_code=70):
            # 시프
            return 기본종료(self.ctx)
        if self.user_detected(box_ids=[199], job_code=80):
            # 어쌔신
            return 기본종료(self.ctx)
        if self.user_detected(box_ids=[199], job_code=90):
            # 나이트
            return 기본종료(self.ctx)


class 트라이아도서관01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000115_QD__52000115__1$', desc='$52000115_QD__52000115__2$', align=Align.Bottom | Align.Left, duration=10000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트라이아도서관02(self.ctx)


class 트라이아도서관02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000031, portal_id=1)


class 버서커리스항구01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52000115_QD__52000115__3$', desc='$52000115_QD__52000115__4$', align=Align.Bottom | Align.Left, duration=10000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 버서커리스항구02(self.ctx)


class 버서커리스항구02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000062, portal_id=13)


class 기본종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000062, portal_id=1)


initial_state = START
