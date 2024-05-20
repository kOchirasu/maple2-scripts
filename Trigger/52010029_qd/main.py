""" trigger/52010029_qd/main.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import Align


"""
치유의 숲 : 52010026
들어오자마자 앉아있는 상태 연출
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2001]):
            return black(self.ctx)


class black(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[4002], return_view=False)
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.show_caption(type='VerticalCaption', title='$52010029_QD__MAIN__0$', desc='$52010029_QD__MAIN__1$', align=Align.Center | Align.Right, duration=3000, scale=2.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__2$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__3$', duration=3000)
        self.select_camera_path(path_ids=[4018,4003,4002,4019], return_view=False)
        self.move_user(map_id=52010029, portal_id=6006)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 시작_원경을보여주자_02(self.ctx)


class 시작_원경을보여주자_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4016], return_view=False)
        self.spawn_monster(spawn_ids=[406])
        self.spawn_monster(spawn_ids=[407])
        self.spawn_monster(spawn_ids=[405])
        self.spawn_monster(spawn_ids=[408])
        self.spawn_monster(spawn_ids=[409])
        self.spawn_monster(spawn_ids=[410])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 시작_원경을보았으니이제시작하자(self.ctx)


class 시작_원경을보았으니이제시작하자(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrol_name='MS2PatrolData_3006')
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__4$', duration=2000)
        self.add_balloon_talk(msg='$52010029_QD__MAIN__5$', duration=2000, delay_tick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차전투시작_몬스터스폰1(self.ctx)


class 차전투시작_몬스터스폰1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4015], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__6$', duration=3000)
        self.add_balloon_talk(spawn_id=406, msg='$52010029_QD__MAIN__7$', duration=2000)
        self.add_balloon_talk(spawn_id=407, msg='$52010029_QD__MAIN__8$', duration=2000)
        self.set_npc_emotion_sequence(spawn_id=405, sequence_name='Attack_01_A')
        self.set_npc_emotion_sequence(spawn_id=408, sequence_name='Attack_01_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차전투시작_몬스터스폰_02_1(self.ctx)


class 차전투시작_몬스터스폰_02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4016], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=10000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__9$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__10$', duration=3000)
        self.destroy_monster(spawn_ids=[405])
        self.destroy_monster(spawn_ids=[406])
        self.destroy_monster(spawn_ids=[407])
        self.destroy_monster(spawn_ids=[408])
        self.destroy_monster(spawn_ids=[409])
        self.destroy_monster(spawn_ids=[410])
        self.spawn_monster(spawn_ids=[501])
        self.spawn_monster(spawn_ids=[401])
        self.spawn_monster(spawn_ids=[402])
        self.spawn_monster(spawn_ids=[403])
        self.spawn_monster(spawn_ids=[404])
        self.spawn_monster(spawn_ids=[703])
        self.set_npc_emotion_loop(spawn_id=501, sequence_name='Stun_A', duration=16000000.0)
        self.set_npc_emotion_loop(spawn_id=703, sequence_name='Stun_A', duration=16000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 차전투시작_몬스터스폰_black1(self.ctx)


class 차전투시작_몬스터스폰_black1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52010029_QD__MAIN__11$', desc='$52010029_QD__MAIN__12$', align=Align.Center | Align.Left, duration=3000, scale=2.0)
        self.add_cinematic_talk(npc_id=11003392, msg='$52010029_QD__MAIN__13$', duration=3000)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_ambient_light(primary=Vector3(128,128,128))
        self.add_balloon_talk(spawn_id=401, msg='$52010029_QD__MAIN__14$', duration=3000)
        self.add_balloon_talk(spawn_id=402, msg='$52010029_QD__MAIN__15$', duration=3500)
        self.add_cinematic_talk(npc_id=11003392, msg='$52010029_QD__MAIN__16$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 시작_괴롭힘당하는바야르_02(self.ctx)


class 시작_괴롭힘당하는바야르_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__17$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=703, sequence_name='Stun_A', duration=16000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작_괴롭힘당하는바야르_02_01(self.ctx)


class 시작_괴롭힘당하는바야르_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003397, msg='$52010029_QD__MAIN__18$', duration=4000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__19$', duration=4000)
        self.spawn_monster(spawn_ids=[701])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 시작_괴롭힘당하는바야르_03(self.ctx)


class 시작_괴롭힘당하는바야르_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.move_npc(spawn_id=701, patrol_name='MS2PatrolData_3001')
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__20$', duration=3000)
        self.show_caption(type='VerticalCaption', title='$52010029_QD__MAIN__21$', desc='$52010029_QD__MAIN__22$', align=Align.Center | Align.Left, duration=3000, scale=2.0)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__23$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 시작_괴롭힘당하는바야르_03_01(self.ctx)


class 시작_괴롭힘당하는바야르_03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawn_id=701, sequence_name='Attack_01_D')
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__24$', duration=4000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__25$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 시작_괴롭힘당하는바야르_04(self.ctx)


class 시작_괴롭힘당하는바야르_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.set_npc_emotion_loop(spawn_id=703, sequence_name='Down_Idle_A', duration=16000000.0)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__26$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작_괴롭힘당하는바야르_05(self.ctx)


class 시작_괴롭힘당하는바야르_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4016], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__27$', duration=3000)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=3500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차전투시작_01_1(self.ctx)


class 차전투시작_01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차전투시작_02_1(self.ctx)


class 차전투시작_02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_local_camera(camera_id=4014, enable=True)
        self.spawn_monster(spawn_ids=[605]) # 악당Mob_1
        self.spawn_monster(spawn_ids=[606]) # 악당Mob_2
        self.spawn_monster(spawn_ids=[607]) # 악당Mob_3
        self.spawn_monster(spawn_ids=[608]) # 악당Mob_4
        self.spawn_monster(spawn_ids=[613]) # 악당Mob_5
        self.spawn_monster(spawn_ids=[614]) # 악당Mob_6
        self.destroy_monster(spawn_ids=[701])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차전투시작_02_1_1(self.ctx)


class 차전투시작_02_1_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차전투시작_03_1(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_local_camera(camera_id=4014, enable=True)
        self.destroy_monster(spawn_ids=[405])
        self.destroy_monster(spawn_ids=[406])
        self.destroy_monster(spawn_ids=[407])
        self.destroy_monster(spawn_ids=[408])
        self.destroy_monster(spawn_ids=[409])
        self.destroy_monster(spawn_ids=[410])
        self.destroy_monster(spawn_ids=[605]) # 악당Mob_1
        self.destroy_monster(spawn_ids=[606]) # 악당Mob_2
        self.destroy_monster(spawn_ids=[607]) # 악당Mob_3
        self.destroy_monster(spawn_ids=[608]) # 악당Mob_4
        self.destroy_monster(spawn_ids=[613]) # 악당Mob_5
        self.destroy_monster(spawn_ids=[614]) # 악당Mob_6
        self.spawn_monster(spawn_ids=[501])
        self.spawn_monster(spawn_ids=[401])
        self.spawn_monster(spawn_ids=[402])
        self.spawn_monster(spawn_ids=[403])
        self.spawn_monster(spawn_ids=[404])
        self.spawn_monster(spawn_ids=[703])
        self.spawn_monster(spawn_ids=[605]) # 악당Mob_1
        self.spawn_monster(spawn_ids=[606]) # 악당Mob_2
        self.spawn_monster(spawn_ids=[607]) # 악당Mob_3
        self.spawn_monster(spawn_ids=[608]) # 악당Mob_4
        self.spawn_monster(spawn_ids=[613]) # 악당Mob_5
        self.spawn_monster(spawn_ids=[614]) # 악당Mob_6
        self.destroy_monster(spawn_ids=[701])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차전투시작_03_1(self.ctx)


class 차전투시작_03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=605, msg='$52010029_QD__MAIN__28$', duration=2000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=606, msg='$52010029_QD__MAIN__29$', duration=2000, delay_tick=1500)
        self.set_npc_emotion_loop(spawn_id=501, sequence_name='Stun_A', duration=16000000.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=1, arg2='$52010029_QD__MAIN__30$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[605,606,607,608,613,614]):
            return 차전투시작_01_2(self.ctx)


class 차전투시작_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[702])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[701])
        self.destroy_monster(spawn_ids=[605])
        self.destroy_monster(spawn_ids=[606])
        self.destroy_monster(spawn_ids=[607])
        self.destroy_monster(spawn_ids=[608])
        self.destroy_monster(spawn_ids=[613])
        self.destroy_monster(spawn_ids=[614])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차전투시작_02_2(self.ctx)


class 차전투시작_02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52010029, portal_id=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차전투시작_02_01_2(self.ctx)


class 차전투시작_02_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=4014)
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.move_user_path(patrol_name='MS2PatrolData_3002')
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__31$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차전투시작_02_01_01_2(self.ctx)


class 차전투시작_02_01_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_loop(spawn_id=703, sequence_name='Stun_A', duration=16000000.0)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__32$', duration=3000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__33$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 차전투시작_02_02_2(self.ctx)


class 차전투시작_02_02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__34$', duration=3000)
        self.set_npc_emotion_sequence(spawn_id=702, sequence_name='Attack_01_D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차전투시작_02_03_2(self.ctx)


class 차전투시작_02_03_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__35$', duration=3000)
        self.set_npc_emotion_sequence(spawn_id=501, sequence_name='Attack_01_J')
        self.move_user(map_id=52010029, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차전투시작_02_04_2(self.ctx)


class 차전투시작_02_04_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__36$', duration=3000)
        self.set_npc_emotion_sequence(spawn_id=501, sequence_name='Attack_01_E')
        self.set_npc_emotion_sequence(spawn_id=702, sequence_name='Attack_01_E')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차전투시작_03_2(self.ctx)


class 차전투시작_03_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.spawn_monster(spawn_ids=[601])
        self.spawn_monster(spawn_ids=[602])
        self.spawn_monster(spawn_ids=[603])
        self.spawn_monster(spawn_ids=[604])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차전투시작_03_1_2(self.ctx)


class 차전투시작_03_1_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차전투시작_04_2(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52010029, portal_id=6001)
        self.destroy_monster(spawn_ids=[601])
        self.destroy_monster(spawn_ids=[602])
        self.destroy_monster(spawn_ids=[603])
        self.destroy_monster(spawn_ids=[604])
        self.spawn_monster(spawn_ids=[601])
        self.spawn_monster(spawn_ids=[602])
        self.spawn_monster(spawn_ids=[603])
        self.spawn_monster(spawn_ids=[604])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차전투시작_04_2(self.ctx)


class 차전투시작_04_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.set_event_ui(type=1, arg2='$52010029_QD__MAIN__37$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,602,603,604]):
            return 차전투종료2(self.ctx)


class 차전투종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52010029, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차전투종료직후2(self.ctx)


class 차전투종료직후2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[601])
        self.destroy_monster(spawn_ids=[602])
        self.destroy_monster(spawn_ids=[603])
        self.destroy_monster(spawn_ids=[604])
        self.set_scene_skip(state=Skip_3, action='nextState')
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_loop(spawn_id=501, sequence_name='Stun_A', duration=16000000.0)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__38$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차전투종료_01_2(self.ctx)


class 차전투종료_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__39$', duration=3000)
        self.set_npc_emotion_sequence(spawn_id=702, sequence_name='Attack_01_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차전투시작_01_3(self.ctx)


class 차전투시작_01_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[609])
        self.spawn_monster(spawn_ids=[610])
        self.spawn_monster(spawn_ids=[611])
        self.spawn_monster(spawn_ids=[612])
        self.spawn_monster(spawn_ids=[616])
        self.spawn_monster(spawn_ids=[617])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차전투시작_01_1_3(self.ctx)


class 차전투시작_01_1_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차전투시작_02_3(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawn_ids=[609])
        self.destroy_monster(spawn_ids=[610])
        self.destroy_monster(spawn_ids=[611])
        self.destroy_monster(spawn_ids=[612])
        self.destroy_monster(spawn_ids=[616])
        self.destroy_monster(spawn_ids=[617])
        self.spawn_monster(spawn_ids=[609])
        self.spawn_monster(spawn_ids=[610])
        self.spawn_monster(spawn_ids=[611])
        self.spawn_monster(spawn_ids=[612])
        self.spawn_monster(spawn_ids=[616])
        self.spawn_monster(spawn_ids=[617])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차전투시작_02_3(self.ctx)


class 차전투시작_02_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=1, arg2='$52010029_QD__MAIN__40$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[609,610,611,612,616,617]):
            return 차전투시작_02_직후3(self.ctx)


class 차전투시작_02_직후3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52010029, portal_id=6003)
        self.set_scene_skip(state=Skip_4, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차전투시작_01_4(self.ctx)


class 차전투시작_01_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4011], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[609])
        self.destroy_monster(spawn_ids=[610])
        self.destroy_monster(spawn_ids=[611])
        self.destroy_monster(spawn_ids=[612])
        self.destroy_monster(spawn_ids=[616])
        self.destroy_monster(spawn_ids=[617])
        self.move_user_path(patrol_name='MS2PatrolData_3004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차전투시작_02_01_4(self.ctx)


class 차전투시작_02_01_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=5000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__41$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차전투시작_02_4(self.ctx)


class 차전투시작_02_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__42$', duration=4000)
        self.set_npc_emotion_sequence(spawn_id=501, sequence_name='Attack_01_J')
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__43$', duration=3000)
        self.add_cinematic_talk(npc_id=11003392, msg='$52010029_QD__MAIN__44$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__45$', duration=2000)
        self.add_cinematic_talk(npc_id=11003392, msg='$52010029_QD__MAIN__46$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__47$', duration=3000)
        self.set_onetime_effect(id=102, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_sequence(spawn_id=702, sequence_name='Attack_01_G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=18000):
            return 차전투시작_03_4(self.ctx)


class 차전투시작_03_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__48$', duration=4000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__49$', duration=4000)
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__50$', duration=4000)
        self.set_npc_emotion_loop(spawn_id=501, sequence_name='Stun_A', duration=16000000.0)
        self.destroy_monster(spawn_ids=[401])
        self.destroy_monster(spawn_ids=[402])
        self.destroy_monster(spawn_ids=[403])
        self.destroy_monster(spawn_ids=[404])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 차전투시작_04_4(self.ctx)


class 차전투시작_04_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npc_id=11003431, msg='$52010029_QD__MAIN__51$', duration=4000)
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_effect(trigger_ids=[5004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차전투시작_05_4(self.ctx)


class 차전투시작_05_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__52$', duration=2000)
        self.set_effect(trigger_ids=[5003], visible=True)
        self.destroy_monster(spawn_ids=[501])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차전투시작_06_4(self.ctx)


class 차전투시작_06_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=501, sequence_name='Attack_02_E')
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawn_id=703, sequence_name='Down_Idle_A', duration=16000000.0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[702])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차전투시작_07_4(self.ctx)


class 차전투시작_07_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.move_user(map_id=52010029, portal_id=6005)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=6000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__53$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__54$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 차전투시작_08_4(self.ctx)


class 차전투시작_08_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__55$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__56$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 차전투시작_09_4(self.ctx)


class 차전투시작_09_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=3500.0)
        self.set_npc_emotion_loop(spawn_id=703, sequence_name='Attack_Idle_A', duration=16000000.0)
        self.add_balloon_talk(msg='$52010029_QD__MAIN__57$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__58$', duration=4000)
        self.add_balloon_talk(msg='$52010029_QD__MAIN__59$', duration=2000, delay_tick=4000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__60$', duration=4000)
        self.add_balloon_talk(msg='$52010029_QD__MAIN__61$', duration=3000, delay_tick=7000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__62$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__63$', duration=3000)
        self.move_user_path(patrol_name='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            return 차전투시작_09_01_4(self.ctx)


class 차전투시작_09_01_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__64$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__65$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 에바고르전투_01(self.ctx)


class 에바고르전투_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__66$', duration=4000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__67$', duration=2000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__68$', duration=3000)
        self.set_npc_emotion_sequence(spawn_id=703, sequence_name='Attack_02_A')
        self.face_emotion(spawn_id=703, emotion_name='Trigger_Fury')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 에바고르전투_01_1(self.ctx)


class 에바고르전투_01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 에바고르전투_02(self.ctx)


class Skip_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52010029, portal_id=6005)
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.destroy_monster(spawn_ids=[401])
        self.destroy_monster(spawn_ids=[402])
        self.destroy_monster(spawn_ids=[403])
        self.destroy_monster(spawn_ids=[404])
        self.destroy_monster(spawn_ids=[501])
        self.destroy_monster(spawn_ids=[702])
        self.set_onetime_effect(id=7, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 에바고르전투_02(self.ctx)


class 에바고르전투_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.destroy_monster(spawn_ids=[703])
        self.spawn_monster(spawn_ids=[699])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에바고르전투_03(self.ctx)


class 에바고르전투_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=7, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 에바고르전투_04(self.ctx)


class 에바고르전투_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=1, arg2='$52010029_QD__MAIN__69$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[699]):
            return 훈계_01(self.ctx)


class 훈계_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2001, type='trigger', achieve='evagor')
        self.set_onetime_effect(id=8, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[699])
        self.set_scene_skip(state=Warp, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3600):
            return 훈계_02_01(self.ctx)


class 훈계_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4012], return_view=False)
        self.spawn_monster(spawn_ids=[704])
        self.move_user(map_id=52010029, portal_id=6004)
        self.set_npc_emotion_loop(spawn_id=704, sequence_name='Down_Idle_A', duration=16000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 훈계_02_02(self.ctx)


class 훈계_02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=8, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=9000.0)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__70$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__71$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__72$', duration=4000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__73$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__74$', duration=2000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__75$', duration=4000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__76$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__77$', duration=4000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__78$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 훈계_03(self.ctx)


class 훈계_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__79$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__80$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__81$', duration=5000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__82$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__83$', duration=3000)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__84$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=21000):
            return 훈계_04(self.ctx)


class 훈계_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_3005')
        self.add_cinematic_talk(npc_id=0, msg='$52010029_QD__MAIN__85$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 훈계_05(self.ctx)


class 훈계_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4017], return_view=False)
        self.add_cinematic_talk(npc_id=11003391, msg='$52010029_QD__MAIN__86$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 훈계_06(self.ctx)


class 훈계_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Warp(self.ctx)


class Warp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000051, portal_id=21)


initial_state = idle
