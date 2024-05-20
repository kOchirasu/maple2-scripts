""" trigger/52010067_qd/main.xml """
import trigger_api


class 연출01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            self.visible_my_pc(is_visible=False) # 유저 투명 처리
            self.set_cinematic_ui(type=1)
            self.set_effect(trigger_ids=[9010])
            return 연출브릿지(self.ctx)


class 연출브릿지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[700], quest_ids=[20002290], quest_states=[2]):
            # 몬스터 처치 수업을 다 끝내면 케이틀린 등장
            return 조준씬01(self.ctx)
        if self.quest_user_detected(box_ids=[700], quest_ids=[20002290], quest_states=[3]):
            # 몬스터 처치 수업을 다 끝내면 케이틀린 등장
            return 피격씬01(self.ctx)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@포신정렬씬@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class 조준씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 인페르녹

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출02_b(self.ctx)


class 연출02_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1300):
            return 연출02_c(self.ctx)


class 연출02_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000,2001,2002,2003,2004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5300):
            return 연출03(self.ctx)


class 연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2005,2006,2007,2008,2009,2010,2011], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3200):
            return 연출04(self.ctx)


class 연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2012], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출05(self.ctx)


class 연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return quit(self.ctx)


class quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000422, portal_id=3)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@피격씬@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class 피격씬01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 피격씬01_a(self.ctx)


class 피격씬01_a(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1300):
            return 피격씬02(self.ctx)


class 피격씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[9010], visible=True)
        self.select_camera_path(path_ids=[3004,3005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 피격씬03_a(self.ctx)


class 피격씬03_a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3000,3001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3900):
            return 피격씬03(self.ctx)


class 피격씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3002,3003], return_view=False)
        self.set_time_scale(enable=True, start_scale=0.1, end_scale=0.1, duration=3.5, interpolator=1) # 2초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3600):
            return 피격씬04(self.ctx)


class 피격씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return quit02(self.ctx)


class quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000422, portal_id=3)


initial_state = 연출01
