""" trigger/52010064_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 트리스탄

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000073], quest_states=[3]):
            return 돌아가(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000073], quest_states=[2]):
            return CameraEffect01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000073], quest_states=[1]):
            return CameraEffect01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[91000072], quest_states=[3]):
            return 돌아가(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[91000073], quest_states=[1]):
            return 돌아가(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=quit01, action='nextState') # setsceneskip 1 set
        # setsceneskip set
        # setsceneskip set
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='flyingtristan') # 퀘스트 완료 업적

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[8000], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 트리스탄대사01(self.ctx)


class 트리스탄대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010], return_view=False)
        self.add_cinematic_talk(npc_id=11003842, illust_id='Tristan_normal', msg='$52010064_QD__main__0$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄대사02(self.ctx)


class 트리스탄대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003842, illust_id='Tristan_normal', msg='$52010064_QD__main__1$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄대사03(self.ctx)


class 트리스탄대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.add_cinematic_talk(npc_id=11003842, illust_id='Tristan_normal', msg='$52010064_QD__main__2$', duration=3000, align=Align.Right)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Tristan_walking')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄대사04(self.ctx)


class 트리스탄대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003842, illust_id='Tristan_normal', msg='$52010064_QD__main__3$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄대사05(self.ctx)


class 트리스탄대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.add_cinematic_talk(npc_id=11003842, illust_id='Tristan_normal', msg='$52010064_QD__main__4$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리스탄대사06(self.ctx)


class 트리스탄대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003842, illust_id='Tristan_normal', msg='$52010064_QD__main__5$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마무리줌아웃(self.ctx)


class 마무리줌아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_cinematic_ui(type=0)
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return quit01(self.ctx)


class quit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return quit03(self.ctx)


class quit03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.move_user(map_id=52010052, portal_id=1) # 작전실로 자동 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return quit03(self.ctx)


class 돌아가(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010052, portal_id=1) # 작전실로 자동 이동
        self.visible_my_pc(is_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return 돌아가(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
