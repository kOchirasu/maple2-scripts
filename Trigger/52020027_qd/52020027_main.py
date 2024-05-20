""" trigger/52020027_qd/52020027_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990002, key='Boss', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 연출감지(self.ctx)


class 연출감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.move_user(map_id=52020027, portal_id=2)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Sit_Down_A', duration=5000.0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라_세리하대사1(self.ctx)


class 카메라_세리하대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=22000114, script='대체 어딨는거지?', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라_세리하대사2(self.ctx)


class 카메라_세리하대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=502)
        self.set_npc_rotation(spawn_id=101, rotation=180.0)
        self.set_dialogue(type=2, spawn_id=22000114, script='여기까지 쫓아왔어?', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_세리하대사3(self.ctx)


class 카메라_세리하대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=22000114, script='이제 결판을 내자!!', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.reset_camera(interpolation_time=0.1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 보스전시작(self.ctx)


class 보스전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111])
        self.set_user_value(trigger_id=99990002, key='Boss', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111]):
            return 보스전종료(self.ctx)


class 보스전종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_achievement(trigger_id=904, achieve='KritiasScrimmage')
        self.set_event_ui(type=1, arg2='연출들어갈 예정입니다', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2020006, portal_id=6001)


initial_state = 감지
