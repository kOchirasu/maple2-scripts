""" trigger/52100105_qd/52100105_01.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50101020], quest_states=[2]):
            return wait_03(self.ctx)
        if self.quest_user_detected(box_ids=[2002], quest_ids=[50101030], quest_states=[3]):
            return 장치가동_04(self.ctx)


"""
class wait_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=9, script='투르카가 클라디아의 블루 라펜타 에너지를 빼앗으려 하는 연출이 나올 예정입니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출끝(self.ctx)
"""

class wait_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카_클라디아(self.ctx)


class 투르카_클라디아(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 클라디아
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 투르카
        self.spawn_monster(spawn_ids=[103], auto_target=False) # 검은 군단 병사
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.visible_my_pc(is_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 투르카_클라디아_02(self.ctx)


class 투르카_클라디아_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[4001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카_클라디아_03(self.ctx)


class 투르카_클라디아_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002], return_view=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_normal', align=Align.Right, msg='$52100105_QD__52100105_01__0$', duration=4000)
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_normal', align=Align.Right, msg='$52100105_QD__52100105_01__1$', duration=4000)
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_normal', align=Align.Right, msg='$52100105_QD__52100105_01__2$', duration=4000)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 투르카_클라디아_04(self.ctx)


class 투르카_클라디아_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.add_cinematic_talk(npc_id=11004392, illust_id='cladia_normal', align=Align.Left, msg='$52100105_QD__52100105_01__3$', duration=3500)
        self.add_cinematic_talk(npc_id=11004392, illust_id='cladia_normal', align=Align.Left, msg='$52100105_QD__52100105_01__4$', duration=3500)
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_normal', align=Align.Right, msg='$52100105_QD__52100105_01__5$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return 투르카_클라디아_05(self.ctx)


class 투르카_클라디아_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_normal', align=Align.Left, msg='$52100105_QD__52100105_01__6$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 장치가동_01(self.ctx)


class 장치가동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.set_npc_rotation(spawn_id=102, rotation=270.0)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_normal', align=Align.Left, msg='$52100105_QD__52100105_01__7$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 장치가동_01_02(self.ctx)


class 장치가동_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 장치가동_01_03(self.ctx)


class 장치가동_01_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 장치가동_02(self.ctx)


class 장치가동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.select_camera_path(path_ids=[4006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 장치가동_02_01(self.ctx)


class 장치가동_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=102, rotation=360.0)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Quest_Attack_A', duration=5000.0) # 클라디아
        self.add_cinematic_talk(npc_id=11004392, illust_id='cladia_normal', align=Align.Right, msg='$52100105_QD__52100105_01__8$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 장치가동_03(self.ctx)


class 장치가동_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4008], return_view=False)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Quest_Effect_A', duration=12000.0) # 클라디아
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 장치가동_04(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 정리(self.ctx)


class 장치가동_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 정리(self.ctx)


class 정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])
        self.destroy_monster(spawn_ids=[105])
        self.destroy_monster(spawn_ids=[106])
        self.destroy_monster(spawn_ids=[107])
        self.visible_my_pc(is_visible=True)
        self.move_user(map_id=52100110, portal_id=1)


initial_state = wait_01
