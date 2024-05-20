""" trigger/52020031_qd/main30000333.xml """
import trigger_api


"""
제단 입장
예상치 못한 인물 하렌(11003747) - spawnpoint : 1 
한순간의 방심 하렌(11003749) - spawnpoint : 2
연출용 하렌(11003756) - spawnpoint : 101
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[30000333], quest_states=[1]):
            return 두번째연출준비(self.ctx)


class 두번째연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 두번째연출준비_01(self.ctx)


class 두번째연출준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[102]) # 퀘스트용 하렌
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.select_camera_path(path_ids=[4003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째연출준비_02(self.ctx)


class 두번째연출준비_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020031, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째연출(self.ctx)


class 두번째연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=0, msg='천공의 심장을 돌려줘.', duration=3000)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3200):
            return 두번째연출_01(self.ctx)


class 두번째연출_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 두번째연출_02(self.ctx)


class 두번째연출_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003756, msg='곱게 가져갈 수 있을 거라고 생각해?', duration=3000)
        self.add_cinematic_talk(npc_id=11003756, msg='꿈도 야무지다니까... 호호호', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 두번째연출_03(self.ctx)


class 두번째연출_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4012], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째연출전투준비_01(self.ctx)


class 두번째연출전투준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 두번째연출전투준비(self.ctx)


class 두번째연출전투준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=2) # UI 숨기기 초기화
        self.set_cinematic_ui(type=0) # 유저 이동 가능하게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 두번째연출전투준비1(self.ctx)


class 두번째연출전투준비1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[601], auto_target=False) # 몬스터 하렌
        self.set_event_ui(type=1, arg2='하렌을 처치하세요!', arg3='2000', arg4='0')
        self.add_balloon_talk(spawn_id=601, msg='숨통을 끊어주마.', duration=3000, delay_tick=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601]):
            return 두번째연출전투종료1(self.ctx)


class 두번째연출전투종료1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=0.5)
        self.move_user(map_id=52020031, portal_id=6001)
        self.destroy_monster(spawn_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째연출전투종료2(self.ctx)


class 두번째연출전투종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
