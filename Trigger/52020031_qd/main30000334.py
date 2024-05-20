""" trigger/52020031_qd/main30000334.xml """
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
        if self.quest_user_detected(box_ids=[2001], quest_ids=[30000334], quest_states=[1]):
            return 세번째전투끝나고(self.ctx)


class 세번째전투끝나고(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세번째전투끝나고1(self.ctx)


class 세번째전투끝나고1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.spawn_monster(spawn_ids=[101], auto_target=False)
        # self.set_npc_emotion_loop(spawn_id=101, sequence_name='Sit_Down_A', duration=12000.0) # 쓰러져있는 연출용 하렌
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 세번째전투끝나고2(self.ctx)


class 세번째전투끝나고2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020031, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 세번째전투끝나고2_2(self.ctx)


class 세번째전투끝나고2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[5001], visible=True)
        self.face_emotion(emotion_name='defaultBattle')
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=5000.0)
        self.add_cinematic_talk(npc_id=0, msg='역시 너희 흑성회는 믿을 만한 사람들이 아니었군.\\n천공의 심장은 내가 가져가겠어.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 세번째전투끝나고3(self.ctx)


class 세번째전투끝나고3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.set_effect(trigger_ids=[5001])
        self.add_cinematic_talk(npc_id=11003756, msg='크윽...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세번째전투끝나고3_01(self.ctx)


class 세번째전투끝나고3_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 세번째전투끝나고4(self.ctx)


class 세번째전투끝나고4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='오늘 있었던 일은, 라딘에게도 전하겠어.', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='흑성회와의 동맹은 여기까지야.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 천공의탑으로이동(self.ctx)


class 천공의탑으로이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52020030, portal_id=6001)


initial_state = idle
