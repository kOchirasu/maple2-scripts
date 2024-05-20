""" trigger/52000138_qd/main.xml """
import trigger_api
from System.Numerics import Vector3


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7101, enable=True)
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4005, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4006, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4007, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4008, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4009, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4010, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=4011, visible=True, initial_sequence='Closed') # 사이렌 종료
        self.set_actor(trigger_id=1001, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1002, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1003, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1004, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1005, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1006, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1007, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1008, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1009, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1010, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1011, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1012, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1013, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1014, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1015, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1016, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1017, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1018, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1019, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1020, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1021, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1022, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1023, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1024, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1025, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1026, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1027, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=1028, visible=True, initial_sequence='sf_quest_light_A01_Off')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG\\weather\\Eff_monochrome_03.xml')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/Sound/Eff_ Object_Train_alert.xml')
        self.set_ambient_light(primary=Vector3(0,0,0))
        self.set_ambient_light(primary=Vector3(1,1,1))
        self.add_buff(box_ids=[701], skill_id=99910230, level=1, is_player=False) # 레논 변신
        self.add_buff(box_ids=[701], skill_id=99910230, level=1, is_player=False, is_skill_set=False) # 레논 변신
        # 다크윈드 대원 101번 소환
        # self.spawn_monster(spawn_ids=[101,102,103,104,105,122])
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return act1_wave1(self.ctx)


class act1_wave1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$52000138_QD__MAIN__0$', arg3='3000', arg4='0') # 1구역 사이렌 시작
        self.set_actor(trigger_id=1001, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1002, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1003, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1004, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1009, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1010, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1025, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1026, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1027, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1028, visible=True, initial_sequence='sf_quest_light_A01_On') # 다크윈드 대원 101번 대사
        self.set_dialogue(type=1, spawn_id=101, script='$52000138_QD__MAIN__1$', time=3)
        self.set_sound(trigger_id=10000, enable=True)
        self.set_sound(trigger_id=7002, enable=True)
        # self.set_dialogue(type=1, spawn_id=122, script='레논! 사실이 아니지? 네가 그럴리가 없잖아!', time=4, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1):
            return act1_wave2(self.ctx)

    def on_exit(self) -> None:
        # self.set_effect(trigger_ids=[7001], visible=True)
        # self.destroy_monster(spawn_ids=[122])
        pass


class act1_wave2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 다크윈드 대원 102,104번 소환
        # self.set_actor(trigger_id=4001, visible=True, initial_sequence='Opened')
        # self.set_actor(trigger_id=4002, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1):
            return act1_wave2_move(self.ctx)


class act1_wave2_move(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1구역 좌우측 문 개방
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Opened')
        self.set_dialogue(type=1, spawn_id=102, script='$52000138_QD__MAIN__2$', time=3, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return act1_wave2_1(self.ctx)


class act1_wave2_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 다크윈드 대원 102,104번 소환
        # self.set_actor(trigger_id=4001, visible=True, initial_sequence='Opened')
        # self.set_actor(trigger_id=4002, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1):
            return act1_wave2_move_1(self.ctx)


class act1_wave2_move_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1구역 좌우측 문 개방
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Opened')
        self.set_dialogue(type=1, spawn_id=104, script='$52000138_QD__MAIN__3$', time=3, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return act1_wave3(self.ctx)


class act1_wave3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 다크윈드 대원 103,105번 소환
        self.spawn_monster(spawn_ids=[103,105])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return act1_wave3_move(self.ctx)


class act1_wave3_move(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=105, script='$52000138_QD__MAIN__4$', time=3, arg5=3) # 1구역 중앙 문 개방
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Opened')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return ready_1(self.ctx)


class ready_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.spawn_monster(spawn_ids=[106,107,108,109,110,111,112,123])
        self.spawn_monster(spawn_ids=[110,111])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return act2_wave1(self.ctx)


class act2_wave1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 2구역 사이렌 시작
        self.set_actor(trigger_id=1005, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1006, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1007, visible=True, initial_sequence='sf_quest_light_A01_Of')
        self.set_actor(trigger_id=1008, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1011, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1012, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1011, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1012, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1023, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1024, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_dialogue(type=1, spawn_id=110, script='$52000138_QD__MAIN__5$', time=2)
        self.set_dialogue(type=1, spawn_id=111, script='$52000138_QD__MAIN__6$', time=3, arg5=1)
        # self.set_dialogue(type=1, spawn_id=123, script='아니라고 말해줘! 아니라고 말해달라고!', time=4, arg5=3) # 블랙아이 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1):
            return act2_wave2(self.ctx)

    def on_exit(self) -> None:
        # self.destroy_monster(spawn_ids=[123])
        pass


class act2_wave2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 2구역 좌측 문 개방
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='Opened') # 다크윈드 대원 106,107번 소환
        self.spawn_monster(spawn_ids=[106,107])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1):
            return act2_wave2_move(self.ctx)


class act2_wave2_move(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=106, script='$52000138_QD__MAIN__7$', time=3, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return act2_wave3(self.ctx)


class act2_wave3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 2구역 우측 문 개방
        self.set_actor(trigger_id=4005, visible=True, initial_sequence='Opened') # 다크윈드 대원 108,109번 소환
        self.spawn_monster(spawn_ids=[108,109])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return act2_wave3_move(self.ctx)


class act2_wave3_move(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 2구역 중앙 문 개방
        self.set_actor(trigger_id=4006, visible=True, initial_sequence='Opened')
        self.set_dialogue(type=1, spawn_id=109, script='$52000138_QD__MAIN__8$', time=3, arg5=3)
        self.spawn_monster(spawn_ids=[112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return act2_wave3_move_1(self.ctx)


class act2_wave3_move_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=112, script='$52000138_QD__MAIN__9$', time=3, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703]):
            return ready_2(self.ctx)


class ready_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[113])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1):
            return act3_wave1_move(self.ctx)


class act3_wave1_move(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 3구역 사이렌 시작
        self.set_actor(trigger_id=1013, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1014, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1015, visible=True, initial_sequence='sf_quest_light_A01_Of')
        self.set_actor(trigger_id=1016, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1017, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1018, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1019, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1020, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1021, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=1022, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_dialogue(type=1, spawn_id=113, script='$52000138_QD__MAIN__10$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1):
            return act3_wave2_1(self.ctx)

    def on_exit(self) -> None:
        # self.destroy_monster(spawn_ids=[124])
        pass


class act3_wave2_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[114,115,120,121])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return act3_wave2_2(self.ctx)


class act3_wave2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=114, script='$52000138_QD__MAIN__11$', time=2, arg5=2)
        self.spawn_monster(spawn_ids=[116,117,118,119])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return act3_wave2_move(self.ctx)


class act3_wave2_move(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=116, script='$52000138_QD__MAIN__12$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123]):
            return escape(self.ctx)


class escape(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[122])
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_scene_skip(state=endready, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return plot(self.ctx)


class plot(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=7102, enable=True)
        self.set_dialogue(type=1, spawn_id=122, script='$52000138_QD__MAIN__13$', time=3, arg5=4)
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return scheme1(self.ctx)


class scheme1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=122, script='$52000138_QD__MAIN__14$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scheme2(self.ctx)


class scheme2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=122, script='$52000138_QD__MAIN__15$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scheme3(self.ctx)


class scheme3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=122, script='$52000138_QD__MAIN__16$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return scheme4(self.ctx)

    def on_exit(self) -> None:
        self.select_camera_path(path_ids=[8002], return_view=False)


class scheme4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=122, sequence_name='Talk_A', duration=1500.0)
        self.set_dialogue(type=1, spawn_id=122, script='$52000138_QD__MAIN__17$', time=5)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return endready(self.ctx)


class endready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='windead')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='windead')
        self.move_user(map_id=2000153, portal_id=2)


initial_state = idle
