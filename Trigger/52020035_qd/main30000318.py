""" trigger/52020035_qd/main30000318.xml """
import trigger_api


# 퀘스트 수락 후 연출 시작
class idle3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[703], quest_ids=[30000318], quest_states=[2]):
            return 연출시작3(self.ctx)


# 라딘과 대화 시작
class 연출시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=8, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출시작3_1(self.ctx)


class 연출시작3_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(is_visible=False)
        self.destroy_monster(spawn_ids=[117])
        self.destroy_monster(spawn_ids=[118])
        self.destroy_monster(spawn_ids=[119])
        self.destroy_monster(spawn_ids=[120])
        self.destroy_monster(spawn_ids=[121])
        self.spawn_monster(spawn_ids=[110], auto_target=False) # 연출라딘
        self.spawn_monster(spawn_ids=[117], auto_target=False) # 연출웨이홍
        self.spawn_monster(spawn_ids=[118], auto_target=False) # 연출브리드민
        self.spawn_monster(spawn_ids=[119], auto_target=False) # 연출바사라첸
        self.spawn_monster(spawn_ids=[120], auto_target=False) # 연출하렌
        self.spawn_monster(spawn_ids=[121], auto_target=False) # 연출카일
        self.select_camera_path(path_ids=[4026], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 뒷이야기(self.ctx)


class 뒷이야기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=8, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003754, msg='크크큭... 착한 연기 잘 하는군. 라딘.', duration=3000)
        self.set_scene_skip(state=끝, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 뒷이야기01(self.ctx)


class 뒷이야기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4028], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 뒷이야기01(self.ctx)


class 뒷이야기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4030], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=119, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003756, msg='훗. 생각보다 잘 넘어간 것 같군요.', duration=3000)
        self.add_cinematic_talk(npc_id=11003759, msg='쳇, 복잡하게 만들지 말고 그냥 죽어버리면 되잖아?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 뒷이야기02(self.ctx)


class 뒷이야기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4026], return_view=False)
        self.add_cinematic_talk(npc_id=11003754, msg='하렌. 그럼 우리도 다음 작전을 이야기 해 볼까.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 뒷이야기02_1(self.ctx)


class 뒷이야기02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4031], return_view=False)
        self.move_npc(spawn_id=119, patrol_name='MS2PatrolData_3008')
        self.add_cinematic_talk(npc_id=11003756, msg='...후훗.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=9, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=9, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.visible_my_pc(is_visible=True)
        self.move_user(map_id=2020012, portal_id=1)
        self.destroy_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[112])
        self.destroy_monster(spawn_ids=[113])
        self.destroy_monster(spawn_ids=[114])
        self.destroy_monster(spawn_ids=[115])


initial_state = idle3
