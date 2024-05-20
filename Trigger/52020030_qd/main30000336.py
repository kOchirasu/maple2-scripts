""" trigger/52020030_qd/main30000336.xml """
import trigger_api


# 투르카와 전투
class 체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2003], quest_ids=[30000336], quest_states=[2]):
            return 체크2(self.ctx)


class 체크2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(is_visible=False)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.set_scene_skip(state=세번째연출대화진행05, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세번째연출대화진행_01(self.ctx)


class 세번째연출대화진행_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003756, msg='...계획이 틀어졌군.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세번째연출대화진행(self.ctx)


class 세번째연출대화진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4017], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003753, msg='... 왔나.\\n바보같은 행동을 했더군.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세번째연출대화진행02(self.ctx)


class 세번째연출대화진행02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4022], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=108, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003756, msg='... 할말 없어.\\n그래서, 이제 어쩔 셈이지?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 세번째연출대화진행03(self.ctx)


class 세번째연출대화진행03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4017], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='훗. 바보같이.\\n이제 흑성회가 움직이긴 어렵겠군.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세번째연출대화진행03_01(self.ctx)


class 세번째연출대화진행03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4040], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='또 다른 계획을 준비해야겠어.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 세번째연출대화진행04(self.ctx)


class 세번째연출대화진행04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4022], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=108, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003753, msg='그 새로운 계획, 흑성회에도 당연히 전달해 주겠지?\\n기대할께.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 세번째연출대화진행05(self.ctx)


class 세번째연출대화진행05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세번째연출대화진행06(self.ctx)


class 세번째연출대화진행06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.visible_my_pc(is_visible=True)
        self.move_user(map_id=2020017, portal_id=4)


initial_state = 체크
