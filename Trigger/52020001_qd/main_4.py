""" trigger/52020001_qd/main_4.xml """
import trigger_api


class 차감지2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002010], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[4]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 카메리이동(self.ctx)


class 카메리이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000010], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 탈것등장(self.ctx)


class 탈것등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[7001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 폭발_1(self.ctx)


class 폭발_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10052], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 폭발_2(self.ctx)


class 폭발_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10053], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 폭발_3(self.ctx)


class 폭발_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10054], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 맵폭발연출(self.ctx)


class 맵폭발연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10051], visible=True)
        self.set_skill(trigger_ids=[6007], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4400):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000010])
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 오브젝트반응(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[6100004], auto_target=False)


class 오브젝트반응(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='좋아! 이 녀석을 타고 돌격해야겠어!!', time=3)
        self.set_interact_object(trigger_ids=[10002010], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 오브젝트반응_2(self.ctx)


class 오브젝트반응_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002010], state=0):
            return 오브젝트반응_3(self.ctx)


class 오브젝트반응_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002010], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 카메라연출(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[7001], arg2=False)


class 카메라연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[2000009], return_view=False)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 알림(self.ctx)


class 알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='출력이 부족해 크리티아스로 진입할 수 없습니다.', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 알림_2(self.ctx)


class 알림_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='적들을 처치하면 에너지를 충전할 수 있습니다.\\n제한시간 내에 100%충전해, 크리티아스로 진입하세요!', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 타이머시작(self.ctx)


class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='110', seconds=360, start_delay=1, interval=1, v_offset=80)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[6000030], auto_target=False)
        self.spawn_monster(spawn_ids=[6000031], auto_target=False)
        self.spawn_monster(spawn_ids=[6000032], auto_target=False)
        self.spawn_monster(spawn_ids=[6000033], auto_target=False)
        self.spawn_monster(spawn_ids=[6000034], auto_target=False)
        self.set_user_value(trigger_id=909, key='respawn', value=1)
        self.set_user_value(trigger_id=910, key='respawn', value=1)
        self.set_user_value(trigger_id=911, key='respawn', value=1)
        self.set_user_value(trigger_id=912, key='respawn', value=1)
        self.set_user_value(trigger_id=913, key='respawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='110'):
            return 실패(self.ctx)


"""
class 몬스터전멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[6000030,6000031,6000032,6000033,6000034]):
            return 몬스터생성(self.ctx)
        if self.time_expired(timer_id='110'):
            return 실패(self.ctx)
"""

class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2000009])
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


initial_state = 차감지2
