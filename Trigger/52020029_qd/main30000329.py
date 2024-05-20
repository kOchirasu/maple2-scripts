""" trigger/52020029_qd/main30000329.xml """
import trigger_api


# 진리의 문 입장
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[30000329], quest_states=[2]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작_02(self.ctx)


class 연출시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52020029, portal_id=6001)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 진리의문입장(self.ctx)


class 진리의문입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3001')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3002')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_3003')
        self.add_cinematic_talk(npc_id=11003755, msg='후. 이제서야 이곳에 들어오게 되는 군요.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 진리의문입장_02(self.ctx)


class 진리의문입장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003755, msg='덕분에 정말 큰 도움 받았습니다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 진리의문입장_03(self.ctx)


class 진리의문입장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(emotion_name='defaultBattle')
        self.add_cinematic_talk(npc_id=0, msg='저건...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 진리의문유례(self.ctx)


class 진리의문유례(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.add_cinematic_talk(npc_id=11003755, msg='아아. 저 두개의 큰 화면. 저것이 바로 진리의 문입니다.', duration=3000)
        self.add_cinematic_talk(npc_id=11003755, msg='듣기론 세상의 모든 정보를 찾을 수 있는 기계라더군요.', duration=3000)
        self.set_scene_skip(state=마무리, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 감탄(self.ctx)


class 감탄(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11003717, msg='아아... 저것을 직접 만져볼 수 있다니 황홀하군!', duration=3000)
        self.add_cinematic_talk(npc_id=11003755, msg='자, 시간이 없으니 빨리 원하는 정보를 검색해 보죠.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 마무리(self.ctx)


class 마무리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마무리2(self.ctx)


class 마무리2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020029, portal_id=6002)
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마무리3(self.ctx)


class 마무리3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
