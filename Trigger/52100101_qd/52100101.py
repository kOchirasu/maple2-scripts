""" trigger/52100101_qd/52100101.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2001]):
            return wait_02(self.ctx)


class wait_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001]) # 정리
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])
        self.destroy_monster(spawn_ids=[105])
        self.destroy_monster(spawn_ids=[106])
        self.destroy_monster(spawn_ids=[107])
        self.destroy_monster(spawn_ids=[108])
        self.destroy_monster(spawn_ids=[109])
        self.destroy_monster(spawn_ids=[110])
        self.destroy_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[112])
        self.destroy_monster(spawn_ids=[113])
        self.destroy_monster(spawn_ids=[114]) # 다시생성
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Dead_A')
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Dead_B')
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Dead_A')
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Dead_B')
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.set_npc_emotion_sequence(spawn_id=105, sequence_name='Dead_A')
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.set_npc_emotion_sequence(spawn_id=106, sequence_name='Dead_B')
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.set_npc_emotion_sequence(spawn_id=107, sequence_name='Dead_B')
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.set_npc_emotion_sequence(spawn_id=108, sequence_name='Dead_A')
        self.spawn_monster(spawn_ids=[114], auto_target=False) # 클라디아
        self.set_npc_emotion_loop(spawn_id=114, sequence_name='Sit_Down_A', duration=10000000000.0) # 클라디아

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[50100860], quest_states=[2]):
            return wait_01_02(self.ctx)
        if self.quest_user_detected(box_ids=[2002], quest_ids=[50100870], quest_states=[3]):
            return wait_01_03(self.ctx)


class wait_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wait_01_02_003(self.ctx)


class wait_01_02_003(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52100101, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구릉도착(self.ctx)


class 구릉도착(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 구릉도착_01_2(self.ctx)


class 구릉도착_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4002,4003], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3001')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 구릉도착_02(self.ctx)


class 구릉도착_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__0$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 검은군단들(self.ctx)


class 검은군단들(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False) # 미사일포트 조금 더 적게
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__1$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 검은군단들2(self.ctx)


class 검은군단들2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005,4007], return_view=False) # 시간 계산 다시
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__2$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 검은군단들3(self.ctx)


class 검은군단들3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 정리_01(self.ctx)


class 정리_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 정리_02(self.ctx)


class 정리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 밝아짐(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 밝아짐(self.ctx)


class 밝아짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2002], quest_ids=[50100870], quest_states=[3]):
            return wait_01_03(self.ctx)


class wait_01_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wait_01_04(self.ctx)


class wait_01_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52100101, portal_id=3)
        self.spawn_monster(spawn_ids=[109], auto_target=False) # 장교
        self.spawn_monster(spawn_ids=[110], auto_target=False) # 병사
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.spawn_monster(spawn_ids=[113], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클라디아바라봄(self.ctx)


class 클라디아바라봄(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클라디아바라봄_02(self.ctx)


class 클라디아바라봄_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__4$', duration=3000)
        self.add_cinematic_talk(npc_id=11004422, msg='$52100101_QD__52100101__5$', duration=3000)
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 게오르크_04(self.ctx)


class 게오르크_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011,4013], return_view=False) # 바로 오는 것으로
        self.move_npc(spawn_id=109, patrol_name='MS2PatrolData_3002')
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_3003')
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_3004')
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_3005')
        self.move_npc(spawn_id=113, patrol_name='MS2PatrolData_3006')
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 게오르크_04_02(self.ctx)


class 게오르크_04_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004422, msg='$52100101_QD__52100101__7$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 게오르크_05(self.ctx)


class 게오르크_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__8$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 게오르크_06(self.ctx)


class 게오르크_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4014], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3007')
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__9$', duration=4000)
        self.add_cinematic_talk(npc_id=11004422, msg='$52100101_QD__52100101__10$', duration=4000)
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__11$', duration=4500)
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__12$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16500):
            return 게오르크_07(self.ctx)


class 게오르크_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004422, msg='$52100101_QD__52100101__13$', duration=4500)
        self.add_cinematic_talk(npc_id=11004422, msg='$52100101_QD__52100101__14$', duration=4500)
        self.add_cinematic_talk(npc_id=0, msg='$52100101_QD__52100101__15$', duration=4500)
        self.add_cinematic_talk(npc_id=11004422, msg='$52100101_QD__52100101__16$', duration=4000)
        self.add_cinematic_talk(npc_id=11004422, msg='$52100101_QD__52100101__17$', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=22000):
            return 잠시후(self.ctx)


class 잠시후(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 잠시후_2(self.ctx)


class 잠시후_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52100101_QD__52100101__18$')
        self.select_camera_path(path_ids=[4015], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 잠시후_3(self.ctx)


class 잠시후_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[109]) # 장교
        self.destroy_monster(spawn_ids=[110]) # 병사
        self.destroy_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[112])
        self.destroy_monster(spawn_ids=[113])
        self.destroy_monster(spawn_ids=[114])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(is_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 잠시후_4(self.ctx)


class 잠시후_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 잠시후_5(self.ctx)


class 잠시후_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4016], return_view=False)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.add_cinematic_talk(npc_id=11004421, msg='$52100101_QD__52100101__19$', duration=3000)
        self.add_cinematic_talk(npc_id=11004421, msg='$52100101_QD__52100101__20$', duration=3000)
        self.add_cinematic_talk(npc_id=11004421, msg='$52100101_QD__52100101__21$', duration=3000)
        self.add_cinematic_talk(npc_id=11004421, msg='$52100101_QD__52100101__22$', duration=3000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 이동(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이동_02(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이동_02(self.ctx)


class 이동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.move_user(map_id=2020029, portal_id=3)


initial_state = wait_01
