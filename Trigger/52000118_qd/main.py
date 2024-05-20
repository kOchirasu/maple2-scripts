""" trigger/52000118_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 넬프의 집 : 60100015
class ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100015], quest_states=[2]):
            return fadeout(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60100015], quest_states=[3]):
            return fadeout_a(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101]) # 수상한 가면: 11003167
        self.set_portal(portal_id=1)
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_scene_skip(state=fadeout_a, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return suspiciousmask(self.ctx)


class suspiciousmask(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4002,4003], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__0$', duration=3000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return dooropen(self.ctx)


class dooropen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)
        self.spawn_monster(spawn_ids=[102]) # 조디: 11003186

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return jordyspawn(self.ctx)


class jordyspawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__1$', duration=3000, illust_id='Jordy_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return jordyin(self.ctx)


class jordyin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__2$', duration=3000)
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__3$', duration=3000, illust_id='Jordy_normal', align=Align.Left)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_3001') # 조디 올라감

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return jordyhello(self.ctx)


class jordyhello(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__4$', duration=1000, illust_id='Jordy_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return huk(self.ctx)


class huk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Sit_Down_A', duration=1000.0)
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__5$', duration=1000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return suspiciousmaskmove(self.ctx)


class suspiciousmaskmove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3002') # 수상한 가면 뒤 돌아봄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return talk_01(self.ctx)


class talk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Attack_Idle_A', duration=10000.0)
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return talk_02(self.ctx)


class talk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__7$', duration=3000, illust_id='Jordy_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__8$', duration=3000, illust_id='Jordy_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return talk_03(self.ctx)


class talk_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__9$', duration=3000, illust_id='Jordy_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__10$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return talk_04(self.ctx)


class talk_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__11$', duration=3000, illust_id='Jordy_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return killyou(self.ctx)


class killyou(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Attack_01_B')
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__12$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return talk_05(self.ctx)


class talk_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__13$', duration=3000, illust_id='Jordy_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return talk_06(self.ctx)


class talk_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7001, enable=True)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__14$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return camera_01(self.ctx)


class camera_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return camera_02(self.ctx)


class camera_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return talk_07(self.ctx)


class talk_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__15$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return talk_08(self.ctx)


class talk_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__16$', duration=3000, illust_id='Jordy_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return talk_09(self.ctx)


class talk_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__18$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return talk_10(self.ctx)


class talk_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__19$', duration=3000, illust_id='Jordy_normal', align=Align.Left)
        self.add_cinematic_talk(npc_id=11003186, msg='$52000118_QD__MAIN__20$', duration=3000, illust_id='Jordy_normal', align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return talk_11(self.ctx)


class talk_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__21$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return talk_12(self.ctx)


class talk_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_3005') # 수상한 가면 내려감
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_3003') # 조디 비켜줌
        self.add_balloon_talk(spawn_id=102, msg='$52000118_QD__MAIN__22$', duration=4000)
        self.add_cinematic_talk(npc_id=11003167, msg='$52000118_QD__MAIN__23$', duration=3000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return fadeout_a(self.ctx)


class fadeout_a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.visible_my_pc(is_visible=True) # 유저 투명 처리 해제
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[104]) # 조디
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return fadein_a(self.ctx)


class fadein_a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$52000118_QD__MAIN__24$', arg3='3000', arg4='0')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = ready
