""" trigger/52020001_qd/main_5.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[4]):
            return 기다림(self.ctx)


class 기다림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition_open_boss_gauge(max_gauge_point=300, title='출력 에너지')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 체력조건_1(self.ctx)


class 체력조건_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 150:
            return 알림_1(self.ctx)


class 알림_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='에너지가 50%충전 되었습니다.', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 체력조건_2(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[6000041], auto_target=False)
        self.spawn_monster(spawn_ids=[6000042], auto_target=False)
        self.add_buff(box_ids=[6000041], skill_id=49286001, level=1)
        self.add_buff(box_ids=[6000042], skill_id=49286001, level=1)


class 체력조건_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 300:
            return 알림_5(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(type='trigger', achieve='EscapeToKritias')


class 알림_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='에너지가 100%충전 되었습니다.', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 알림_6(self.ctx)


class 알림_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='곧 최대 출력으로 돌진 합니다.', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마지막_연출(self.ctx)


class 마지막_연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(path_ids=[2000009], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 캐릭터숨기기(self.ctx)


class 캐릭터숨기기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False)
        self.spawn_monster(spawn_ids=[7002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마지막_연출_2(self.ctx)


class 마지막_연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return AI연출(self.ctx)


class AI연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.select_camera_path(path_ids=[2000013], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return AI연출_2(self.ctx)


class AI연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, script='준비완료! 크리티아스로 돌진!', time=3)
        self.set_ai_extra_data(key='wing', value=1, box_id=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='wing', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 끝_2(self.ctx)


class 끝_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 맵이동(self.ctx)


class 맵이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2020001, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


initial_state = 시작
