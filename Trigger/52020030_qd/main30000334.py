""" trigger/52020030_qd/main30000334.xml """
import trigger_api


"""
탑 입장
크란츠 - 101
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[30000334], quest_states=[1]):
            return 연출시작(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[30000334], quest_states=[2]):
            return 크란츠습격04_01(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4023,4020], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52020030, portal_id=6001) # 천공의탑 문앞

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 유저걸어감(self.ctx)


class 유저걸어감(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user_path(patrol_name='MS2PatrolData_3001')
        self.add_cinematic_talk(npc_id=0, msg='천공의 심장을 손에 넣었으니 티어스 코어를 완벽히 다시 만들 순 없을거야.', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='지금쯤 수호군은 도착했을까...', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='빨리 라딘에게 돌아가야겠어.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 바라보는크란츠(self.ctx)


class 바라보는크란츠(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 바라보는크란츠_01(self.ctx)


class 바라보는크란츠_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4027,4014], return_view=False)
        self.add_cinematic_talk(npc_id=11003761, msg='...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 바라보는크란츠_02(self.ctx)


class 바라보는크란츠_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4014], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_C')
        self.add_cinematic_talk(npc_id=11003761, msg='후우... 말을 안 듣는군.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 바라보는크란츠_03(self.ctx)


class 바라보는크란츠_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4024], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 잠시암전(self.ctx)


class 잠시암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4016,4015], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 크란츠습격전(self.ctx)


class 크란츠습격전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크란츠습격(self.ctx)


class 크란츠습격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.add_cinematic_talk(npc_id=11003761, msg='... 봐 주는건, 여기까지야.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크란츠습격01(self.ctx)


class 크란츠습격01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=300, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npc_id=0, msg='커헉!', duration=1500)
        self.move_user(map_id=52020030, portal_id=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 크란츠습격02(self.ctx)


class 크란츠습격02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=300, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[5006], visible=True)
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Stun_A', duration=20000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크란츠습격03(self.ctx)


class 크란츠습격03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4025], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='으으... 넌...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 크란츠습격03_01(self.ctx)


class 크란츠습격03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4026], return_view=False)
        self.add_cinematic_talk(npc_id=11003761, msg='빨리 이곳에서 나가라니깐, 정~말 말을 안 듣는 인간이군.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크란츠습격03_01_01(self.ctx)


class 크란츠습격03_01_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4028], return_view=False)
        self.add_cinematic_talk(npc_id=11003761, msg='이런 귀중한 크리티아스의 보물을 당신과 같은 외지인에게 넘길 순 없어.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크란츠습격03_02(self.ctx)


class 크란츠습격03_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4025], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='잠깐... 이건 오해야. 난 이오네 왕녀를 위해서...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 크란츠습격03_03(self.ctx)


class 크란츠습격03_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4029], return_view=False)
        self.add_cinematic_talk(npc_id=11003761, msg='... 천공의 심장은 내가 가져가겠다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 크란츠습격04(self.ctx)


class 크란츠습격04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[5006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크란츠습격04_01(self.ctx)


class 크란츠습격04_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111], auto_target=False) # 퀘스트용 크란츠

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크란츠습격05(self.ctx)


class 크란츠습격05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=0.5)
        self.destroy_monster(spawn_ids=[106])
        self.set_achievement(trigger_id=2001, type='trigger', achieve='AttackSomeone')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
