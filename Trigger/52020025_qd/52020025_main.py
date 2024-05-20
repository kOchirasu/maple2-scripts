""" trigger/52020025_qd/52020025_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1001], visible=True)
        self.set_agent(trigger_ids=[9001], visible=True)
        self.set_agent(trigger_ids=[9002], visible=True)
        self.set_agent(trigger_ids=[9003], visible=True)
        self.set_agent(trigger_ids=[9004], visible=True)
        self.set_agent(trigger_ids=[9005], visible=True)
        self.set_agent(trigger_ids=[9006], visible=True)
        self.set_agent(trigger_ids=[9007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='으아아악!!!', time=2)
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_mesh(trigger_ids=[1001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라_PC(self.ctx)


class 카메라_PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라_보스등장(self.ctx)


class 카메라_보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_Bossmove')
        self.set_npc_rotation(spawn_id=0, rotation=180.0)
        self.set_dialogue(type=1, script='응??', time=2)
        self.select_camera(trigger_id=502)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라_PC도망준비(self.ctx)


class 카메라_PC도망준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=0, rotation=180.0)
        self.set_dialogue(type=1, script='튀자!!', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.reset_camera(interpolation_time=0.1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_agent(trigger_ids=[9001])
        self.set_agent(trigger_ids=[9002])
        self.set_agent(trigger_ids=[9003])
        self.set_agent(trigger_ids=[9004])
        self.set_agent(trigger_ids=[9005])
        self.set_agent(trigger_ids=[9006])
        self.set_agent(trigger_ids=[9007])

    def on_tick(self) -> trigger_api.Trigger:
        return 달리기시작(self.ctx)


class 달리기시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_local_camera(camera_id=511, enable=True)
        self.move_user_path(patrol_name='MS2PatrolData_PCrun')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_Bossrun')
        self.set_event_ui(type=1, arg2='무서운 몬스터로부터 도망치세요', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            return 탈출성공(self.ctx)


class 탈출성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.set_onetime_effect(id=1, enable=True, path='BG\\Common\\ScreenMask\\Eff_CameraMasking_white.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2020008, portal_id=6001)


initial_state = 감지
