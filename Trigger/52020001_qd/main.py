""" trigger/52020001_qd/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[40001])
        self.set_skill(trigger_ids=[6001])
        self.set_interact_object(trigger_ids=[10002001], state=2)
        self.set_interact_object(trigger_ids=[10002002], state=2)
        self.set_interact_object(trigger_ids=[10002003], state=2)
        self.spawn_monster(spawn_ids=[6000020], auto_target=False)
        self.set_effect(trigger_ids=[10090])
        self.set_effect(trigger_ids=[10091])
        self.set_effect(trigger_ids=[10092])
        self.set_mesh(trigger_ids=[80000])
        self.set_portal(portal_id=14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[5]):
            return 인트로(self.ctx)


class 인트로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 인트로_카메라(self.ctx)


class 인트로_카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=2000012)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 인트로_폭발_1(self.ctx)


class 인트로_폭발_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10011], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 인트로_폭발_2(self.ctx)


class 인트로_폭발_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10012], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 인트로_폭발_3(self.ctx)


class 인트로_폭발_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10013], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 인트로_폭발_4(self.ctx)


class 인트로_폭발_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10014], visible=True)
        self.set_skill(trigger_ids=[6001], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1200):
            return 인트로_종료(self.ctx)


class 인트로_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.select_camera(trigger_id=2000012, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 알림(self.ctx)


class 알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='시간이 얼마 없습니다.\\n폭격을 일삼는 에고웨폰들을 처치하며 크리티아스로 침투하세요.', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 감지(self.ctx)


class 감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1]):
            return 타이머시작(self.ctx)


class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='100', seconds=180, start_delay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 몬스터출현_1(self.ctx)


"""
class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 대기_2(self.ctx)
"""

"""
class 대기_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=2000004)
        self.set_dialogue(type=2, script='저 녀석의 공격을 조심해야 겠어...', time=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대기_초기화(self.ctx)
"""

"""
class 대기_초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.select_camera(trigger_id=2000004, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 알림(self.ctx)
"""

class 몬스터출현_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[40001], enable=True)
        self.spawn_monster(spawn_ids=[6000001], auto_target=False)
        self.spawn_monster(spawn_ids=[6000002], auto_target=False)
        self.spawn_monster(spawn_ids=[6000003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터사망_1(self.ctx)
        if self.time_expired(timer_id='100'):
            return 실패(self.ctx)

    def on_exit(self) -> None:
        self.set_dialogue(type=1, script='서둘러야 해!', time=3)


class 몬스터사망_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[6000001]) and self.monster_dead(spawn_ids=[6000002]) and self.monster_dead(spawn_ids=[6000003]):
            return 몬스터출현_2(self.ctx)
        if self.time_expired(timer_id='100'):
            return 실패(self.ctx)


class 몬스터출현_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[6000004], auto_target=False)
        self.spawn_monster(spawn_ids=[6000005], auto_target=False)
        self.spawn_monster(spawn_ids=[6000006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터사망_2(self.ctx)
        if self.time_expired(timer_id='100'):
            return 실패(self.ctx)


class 몬스터사망_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[6000004]) and self.monster_dead(spawn_ids=[6000005]) and self.monster_dead(spawn_ids=[6000006]):
            return 스위치생성연출(self.ctx)
        if self.time_expired(timer_id='100'):
            return 실패(self.ctx)


class 스위치생성연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='100')
        self.destroy_monster(spawn_ids=[6100001])
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 스위치생성연출_카메라(self.ctx)


class 스위치생성연출_카메라(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=2000003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 생성_1(self.ctx)


class 생성_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002001], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 스위치생성연출_카메라_초기화(self.ctx)


class 스위치생성연출_카메라_초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.select_camera(trigger_id=2000003, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 작동(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[6100001], auto_target=False)
        self.set_dialogue(type=1, script='저 스위치를 한번 작동시켜 볼까?', time=3)


class 작동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002001], state=0):
            return 연출시작_1(self.ctx)


class 연출시작_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[6100001])
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.visible_my_pc(is_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 발사_카메라연출_1(self.ctx)


class 발사_카메라연출_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=2000001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 폭발배경연출_1(self.ctx)


class 폭발배경연출_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10028], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 폭발배경연출_2(self.ctx)


class 폭발배경연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10029], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 폭발_1(self.ctx)


class 폭발_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 날라감_1(self.ctx)


class 날라감_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.select_camera_path(path_ids=[2000002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return pc소환(self.ctx)


class pc소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.move_user(map_id=52020001, portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 폭발배경연출_3(self.ctx)


class 폭발배경연출_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10023], visible=True)
        self.set_skill(trigger_ids=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return 폭발배경연출_4(self.ctx)


class 폭발배경연출_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10024], visible=True)
        self.set_skill(trigger_ids=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 폭발배경연출_5(self.ctx)


class 폭발배경연출_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10025], visible=True)
        self.set_skill(trigger_ids=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=400):
            return 맵폭발연출_1(self.ctx)


class 맵폭발연출_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10021], visible=True)
        self.set_skill(trigger_ids=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 맵폭발연출_2(self.ctx)


class 폭발배경연출_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10026], visible=True)
        self.set_skill(trigger_ids=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 폭발배경연출_7(self.ctx)


class 폭발배경연출_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10027], visible=True)
        self.set_skill(trigger_ids=[6002], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 맵폭발연출_2(self.ctx)


class 맵폭발연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[10022], visible=True)
        self.set_skill(trigger_ids=[6003], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 카메라리셋(self.ctx)


class 카메라리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=15, visible=True, enable=True)
        self.reset_camera(interpolation_time=0.5)

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


initial_state = 시작
