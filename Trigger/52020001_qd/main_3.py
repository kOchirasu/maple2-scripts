""" trigger/52020001_qd/main_3.xml """
import trigger_api


class 차감지2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[3]):
            return 잠시기다림_1(self.ctx)


class 잠시기다림_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 타이머시작(self.ctx)


class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='102', seconds=180, start_delay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 몬스터출현_5(self.ctx)


class 몬스터출현_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[6100003], auto_target=False)
        self.spawn_monster(spawn_ids=[6000018], auto_target=False)
        self.spawn_monster(spawn_ids=[6000019], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터체력50(self.ctx)
        if self.time_expired(timer_id='102'):
            return 실패(self.ctx)


class 몬스터체력50(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=6000018, is_relative=True) <= 50 or self.npc_hp(spawn_id=6000019, is_relative=True) <= 50:
            return 생성_2(self.ctx)
        if self.time_expired(timer_id='102'):
            return 실패(self.ctx)


class 생성_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[6000018], skill_id=49286001, level=1)
        self.add_buff(box_ids=[6000019], skill_id=49286001, level=1)
        self.reset_timer(timer_id='102')
        self.set_interact_object(trigger_ids=[10002003], state=1)
        self.set_event_ui(type=1, arg2='아크레온이 거대해지며 모든공격을 튕겨내기 시작했습니다.', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 작동_2(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=921, key='respawn', value=1)


class 작동_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002003], state=0):
            return 연출시작_2(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=921, key='respawn_end', value=2)


class 연출시작_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[6100003])
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.visible_my_pc(is_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 폭발_2(self.ctx)


class 폭발_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return 맵폭발연출_1(self.ctx)


class 맵폭발연출_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10041], visible=True)
        self.set_skill(trigger_ids=[6005], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return 카메라연출(self.ctx)


class 카메라연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000008], return_view=False)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.destroy_monster(spawn_ids=[6000018])
        self.destroy_monster(spawn_ids=[6000019])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return pc소환_2(self.ctx)


class pc소환_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.move_user(map_id=52020001, portal_id=13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 맵폭발연출_2(self.ctx)


class 맵폭발연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10042], visible=True)
        self.set_skill(trigger_ids=[6006], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return 카메라리셋(self.ctx)


class 카메라리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=17, visible=True, enable=True)
        self.reset_camera(interpolation_time=0.8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10090], visible=True)
        self.set_effect(trigger_ids=[10091], visible=True)
        self.set_effect(trigger_ids=[10092], visible=True)
        self.set_mesh(trigger_ids=[80000], visible=True)
        self.destroy_monster(spawn_ids=[-1])
        self.set_event_ui(type=1, arg2='미션에 실패하였습니다. 다시 재도전 해보세요.', arg3='4000')
        self.move_user(map_id=52020001, portal_id=99)
        self.set_portal(portal_id=14, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            pass


class 끝(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            pass


initial_state = 차감지2
