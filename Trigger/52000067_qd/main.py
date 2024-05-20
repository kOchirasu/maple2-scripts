""" trigger/52000067_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_time_scale(start_scale=1.0, end_scale=1.0)
        self.reset_camera()
        self.set_interact_object(trigger_ids=[10001073], state=2)
        self.set_effect(trigger_ids=[7005]) # mask_black
        self.set_effect(trigger_ids=[7001])
        # self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_effect(trigger_ids=[7010]) # 다크 포탈
        self.set_effect(trigger_ids=[7011]) # 다크 포탈
        self.set_effect(trigger_ids=[7012]) # 다크 포탈
        self.set_effect(trigger_ids=[7013]) # 다크 포탈
        self.set_effect(trigger_ids=[7014]) # 다크 포탈
        self.set_effect(trigger_ids=[7015]) # 다크 포탈
        self.set_effect(trigger_ids=[7016]) # 다크 포탈
        self.set_effect(trigger_ids=[7110]) # 다크 포탈 폭발
        self.set_effect(trigger_ids=[7111]) # 다크 포탈 폭발
        self.set_effect(trigger_ids=[7112]) # 다크 포탈 폭발
        self.set_effect(trigger_ids=[7113]) # 다크 포탈 폭발
        self.set_effect(trigger_ids=[7114]) # 다크 포탈 폭발
        self.set_effect(trigger_ids=[7115]) # 다크 포탈 폭발
        self.set_effect(trigger_ids=[7116]) # 다크 포탈 폭발
        self.set_effect(trigger_ids=[7301]) # 다크 포탈 생성음
        self.set_effect(trigger_ids=[7302]) # 다크 포탈 생성음
        self.set_effect(trigger_ids=[7303]) # 다크 포탈 생성음
        self.set_effect(trigger_ids=[7304]) # 다크 포탈 생성음
        self.set_effect(trigger_ids=[7305]) # 로봇 랜딩음
        self.set_effect(trigger_ids=[7306]) # 데블린 워리어 등장음
        self.set_effect(trigger_ids=[7307]) # 수리 음
        self.set_effect(trigger_ids=[7308]) # 로봇 스파크 음
        self.set_effect(trigger_ids=[7309]) # 로봇 움직임 음
        self.set_effect(trigger_ids=[7310]) # 로봇 탑승 음
        self.set_effect(trigger_ids=[7117]) # 감전
        self.set_actor(trigger_id=4999, initial_sequence='Regen_A')
        self.set_actor(trigger_id=4001, initial_sequence='Attack_02_H')
        self.set_actor(trigger_id=4002, initial_sequence='Dead_Idle_A')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=52000067, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.wait_tick(wait_tick=3000):
            return fadein(self.ctx)
        """
        if self.count_users(box_id=702) >= 1:
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[7005], visible=True) # mask_black
        self.set_cinematic_ui(type=9, script='$52000067_QD__MAIN__0$')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7005]) # mask_black
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.remove_buff(box_id=702, skill_id=99910070)
        self.spawn_monster(spawn_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119]) # 다크윈드
        self.spawn_monster(spawn_ids=[501,502,503,504,505,506,507,508,509,510,511,512,513,514]) # 침략자
        self.spawn_monster(spawn_ids=[551,552,553,554,555])
        self.spawn_monster(spawn_ids=[520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536])
        self.spawn_monster(spawn_ids=[121,121,123], auto_target=False) # 블랙윈드 대원
        self.spawn_monster(spawn_ids=[752,753,754], auto_target=False) # 보디가드
        self.move_user_path(patrol_name='MS2PatrolData_1002')
        self.select_camera_path(path_ids=[8001,8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return portal_01(self.ctx)


class portal_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7301], visible=True) # 다크 포탈 생성음
        self.set_effect(trigger_ids=[7010], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return portal_02(self.ctx)


class portal_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7302], visible=True) # 다크 포탈 생성음
        self.set_effect(trigger_ids=[7016], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return portal_03(self.ctx)


class portal_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7303], visible=True) # 다크 포탈 생성음
        self.set_effect(trigger_ids=[7013], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return portal_04(self.ctx)


class portal_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7304], visible=True) # 다크 포탈 생성음
        self.set_effect(trigger_ids=[7012], visible=True) # 다크 포탈
        self.set_effect(trigger_ids=[7014], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return portal_05(self.ctx)


class portal_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7015], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return portal_06(self.ctx)


class portal_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7011], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_03a(self.ctx)


class scene_03a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_03b(self.ctx)


class scene_03b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1003')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_03c(self.ctx)


class scene_03c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2002')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_03c_02(self.ctx)


class scene_03c_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7305], visible=True) # 로봇 랜딩음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return scene_03d(self.ctx)


class scene_03d(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000067_QD__MAIN__22$', time=2)
        self.move_user_path(patrol_name='MS2PatrolData_1004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Regen_A')
        self.set_effect(trigger_ids=[7001], visible=True)
        self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.1, duration=2.0, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return scene_05_a(self.ctx)


class scene_05_a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Jump_Damg_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1400):
            return scene_05_b(self.ctx)


class scene_05_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_time_scale(enable=True, start_scale=0.1, end_scale=0.1, duration=1.0) # 1초 정지
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_05_d(self.ctx)


class scene_05_d(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=0.1, end_scale=1.0, duration=1.0, interpolator=2) # 1초 뒤 복원

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(start_scale=1.0, end_scale=1.0, duration=1.0) # 종료
        self.select_camera_path(path_ids=[8005,8006], return_view=False)
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale() # 1초 뒤 복원
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2003')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__4$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8006,8007], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__5$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return scene_09(self.ctx)


class scene_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__6$', time=3)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return fadeout(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.remove_buff(box_id=702, skill_id=99910070)
        self.destroy_monster(spawn_ids=[201])
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,122,123])
        self.destroy_monster(spawn_ids=[501,502,503,504,505,506,507,508,509,510,511,512,513,514])
        self.destroy_monster(spawn_ids=[520,521,522,523,524,525,526,527,528,529,531,532,533,534,535,536,537,538,539])
        self.destroy_monster(spawn_ids=[551,552,553,554,555,556,557,558,559])
        self.destroy_monster(spawn_ids=[751,752,753,754,756,757,758,759,761,762])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Skip_2(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119]) # 다크윈드
        self.spawn_monster(spawn_ids=[501,502,503,504,505,506,507,508,509,510,511,512,513,514]) # 침략자
        self.spawn_monster(spawn_ids=[551,552,553,554,555])
        self.spawn_monster(spawn_ids=[520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536])
        self.spawn_monster(spawn_ids=[121,121,123], auto_target=False) # 블랙윈드 대원
        self.spawn_monster(spawn_ids=[752,753,754], auto_target=False) # 보디가드
        self.move_user_path(patrol_name='MS2PatrolData_1002')
        self.select_camera_path(path_ids=[8001,8002], return_view=False)
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Regen_A')
        self.set_effect(trigger_ids=[7001], visible=True)
        self.set_effect(trigger_ids=[7010], visible=True) # 다크 포탈
        self.set_effect(trigger_ids=[7011], visible=True) # 다크 포탈
        self.set_effect(trigger_ids=[7012], visible=True) # 다크 포탈
        self.set_effect(trigger_ids=[7013], visible=True) # 다크 포탈
        self.set_effect(trigger_ids=[7014], visible=True) # 다크 포탈
        self.set_effect(trigger_ids=[7015], visible=True) # 다크 포탈
        self.set_effect(trigger_ids=[7016], visible=True) # 다크 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2002')
        self.set_effect(trigger_ids=[7005], visible=True) # mask_black
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2003')
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=25200671, text_id=25200671)
        self.set_mesh(trigger_ids=[6004,6005], visible=True, fade=10.0) # 투명 벽
        self.set_dialogue(type=1, spawn_id=201, script='$52000067_QD__MAIN__7$', time=3, arg5=2)
        self.set_interact_object(trigger_ids=[10001073], state=1)
        self.set_actor(trigger_id=4001, initial_sequence='Regen_A')
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[7005]) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001073], state=0):
            return play(self.ctx)


class play(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7310], visible=True) # 로봇 탑승 음
        self.hide_guide_summary(entity_id=25200671)
        self.set_dialogue(type=1, spawn_id=201, script='$52000067_QD__MAIN__8$', time=3)
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005], fade=10.0) # 투명 벽
        self.set_interact_object(trigger_ids=[10001073], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return GuideMission(self.ctx)
        if self.monster_dead(spawn_ids=[801,802,803,804,805,806,807]):
            return boss_event(self.ctx)


class GuideMission(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$52000067_QD__MAIN__9$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[801,802,803,804,805,806,807]):
            return boss_event(self.ctx)


class boss_event(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[7005], visible=True) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return boss_event_02(self.ctx)


class boss_event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000067, portal_id=2)
        self.set_effect(trigger_ids=[7005]) # mask_black
        self.select_camera_path(path_ids=[8008,8009], return_view=False)
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,122,123])
        self.destroy_monster(spawn_ids=[501,502,503,504,505,506,507,508,509,510,511,512,513,514])
        self.destroy_monster(spawn_ids=[520,521,522,523,524,525,526,527,528,529,531,532,533,534,535,536,537,538,539])
        self.destroy_monster(spawn_ids=[551,552,553,554,555,556,557,558,559])
        self.destroy_monster(spawn_ids=[801,802,803,804,805,806,807])
        # self.destroy_monster(spawn_ids=[851,852,853,854,855,856,857,858,859,861,862,863,864,865,866,867])
        self.destroy_monster(spawn_ids=[751,752,753,754,756,757,758,759,761,762])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return boss_event_03(self.ctx)


class boss_event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7306], visible=True) # 데블린 워리어 등장음
        self.spawn_monster(spawn_ids=[999], delay=5000)
        self.set_scene_skip(state=Skip_3, action='nextState')
        # self.set_actor(trigger_id=4999, initial_sequence='Regen_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return boss_event_04(self.ctx)


class boss_event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010,8011], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=999, sequence_name='AttackReady_A')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return boss_event_05(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return boss_event_05(self.ctx)


class boss_event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8012], return_view=False)
        self.set_effect(trigger_ids=[7005], visible=True) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return boss_event_06(self.ctx)


class boss_event_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(trigger_ids=[7005]) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return boss_event_07(self.ctx)


class boss_event_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[999]):
            return ending_ready(self.ctx)


class ending_ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ending(self.ctx)


class ending(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_4, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[7005], visible=True) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ending_02(self.ctx)


class ending_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[6300,6301,6302,6303,6304,6305,6306,6307,6308,6309,6310])
        self.set_visible_breakable_object(trigger_ids=[6311,6312,6313,6314,6315,6316,6317,6318,6319,6320,6321])
        self.set_visible_breakable_object(trigger_ids=[6322,6323,6324,6325,6326,6327,6328,6329,6330,6331])
        self.remove_buff(box_id=702, skill_id=99910070)
        self.set_cinematic_ui(type=9, script='$52000067_QD__MAIN__10$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ending_02_b(self.ctx)


class ending_02_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[851,852,853,854,855,856,857,858,859,860])
        self.spawn_monster(spawn_ids=[861,862,863,864,865,866,867,868,869,870])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ending_03(self.ctx)


class ending_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7307], visible=True) # 수리 음
        self.set_dialogue(type=1, spawn_id=861, script='$52000067_QD__MAIN__11$', time=2)
        self.set_dialogue(type=1, spawn_id=853, script='$52000067_QD__MAIN__12$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=851, script='$52000067_QD__MAIN__13$', time=3, arg5=3)
        self.set_dialogue(type=1, spawn_id=861, script='$52000067_QD__MAIN__14$', time=3, arg5=4)
        self.set_dialogue(type=1, spawn_id=862, script='$52000067_QD__MAIN__15$', time=3, arg5=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8014,8015], return_view=False)
        self.set_effect(trigger_ids=[7005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return ending_04(self.ctx)


class ending_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7117], visible=True) # 감전 이펙트
        # self.spawn_monster(spawn_ids=[201])
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2003')
        self.move_user(map_id=52000067, portal_id=3)
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Dead_Idle_A')
        self.set_effect(trigger_ids=[7005], visible=True) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ending_05(self.ctx)


class ending_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8016,8017], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ending_06(self.ctx)


class ending_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7308], visible=True) # 로봇 스파크 음
        self.set_effect(trigger_ids=[7005]) # mask_black

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ending_07(self.ctx)


class ending_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__16$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ending_08(self.ctx)


class ending_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__17$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ending_09(self.ctx)


class ending_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8018], return_view=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ending_09_b(self.ctx)


class ending_09_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ending_10(self.ctx)


class ending_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__18$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ending_11(self.ctx)


class ending_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2005')
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__19$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ending_12(self.ctx)


class ending_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__20$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ending_12_b(self.ctx)


class ending_12_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ending_13(self.ctx)


class ending_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ending_14(self.ctx)


class ending_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8019], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ending_15(self.ctx)


class ending_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001897, script='$52000067_QD__MAIN__21$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ending_16(self.ctx)


class ending_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8020], return_view=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_1006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return ending_17(self.ctx)


class ending_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7309], visible=True) # 로봇 움직임 음
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Dead_Damg_A')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ending_18(self.ctx)


class Skip_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_achievement(trigger_id=702, type='trigger', achieve='CityWarfareClear')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return end02(self.ctx)


class ending_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7005], visible=True) # mask_black
        self.set_achievement(trigger_id=702, type='trigger', achieve='CityWarfareClear')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return end01(self.ctx)


class end01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.play_scene_movie(file_name='Aftermath_Madria.swf')
        self.set_scene_skip(state=end02, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return end02(self.ctx)


class end02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000055, portal_id=1)


initial_state = idle
