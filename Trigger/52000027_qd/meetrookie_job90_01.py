""" trigger/52000027_qd/meetrookie_job90_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8100], visible=True)
        self.set_agent(trigger_ids=[8101], visible=True)
        self.set_agent(trigger_ids=[8102], visible=True)
        self.set_agent(trigger_ids=[8103], visible=True)
        self.set_agent(trigger_ids=[8104], visible=True)
        self.set_agent(trigger_ids=[8200], visible=True)
        self.set_agent(trigger_ids=[8201], visible=True)
        self.set_agent(trigger_ids=[8202], visible=True)
        self.set_agent(trigger_ids=[8203], visible=True)
        self.set_agent(trigger_ids=[8204], visible=True)
        self.set_agent(trigger_ids=[8205], visible=True)
        self.spawn_monster(spawn_ids=[901,902,903,911,912], auto_target=False)
        self.set_ladder(trigger_ids=[4000], fade=2)
        self.set_ladder(trigger_ids=[4001], fade=2)
        self.set_mesh(trigger_ids=[8900,8901,8902,8903], visible=True)
        self.set_mesh(trigger_ids=[8001], visible=True)
        self.set_mesh(trigger_ids=[8002], visible=True)
        self.set_mesh(trigger_ids=[8003], visible=True)
        self.set_actor(trigger_id=7000, visible=True, initial_sequence='Closed') # door
        self.set_actor(trigger_id=7001, visible=True, initial_sequence='Closed') # door
        self.set_actor(trigger_id=7100, visible=True, initial_sequence='Closed') # floor
        self.set_actor(trigger_id=7101, visible=True, initial_sequence='Closed') # floor
        self.set_actor(trigger_id=7102, visible=True, initial_sequence='Closed') # floor
        self.set_actor(trigger_id=7103, visible=True, initial_sequence='Closed') # floor
        self.set_actor(trigger_id=7200, visible=True, initial_sequence='Down_Idle_A') # blackeyeman
        self.set_actor(trigger_id=7201, visible=True, initial_sequence='Idle_A') # mafia
        self.set_actor(trigger_id=7202, visible=True, initial_sequence='Idle_A') # mafia
        self.set_actor(trigger_id=7203, visible=True, initial_sequence='Idle_A') # mafia
        self.set_actor(trigger_id=7204, initial_sequence='Down_Idle_B') # runebladerscout
        self.set_actor(trigger_id=7300, visible=True, initial_sequence='Closed') # lever
        self.set_breakable(trigger_ids=[6201,6202,6203])
        self.set_visible_breakable_object(trigger_ids=[6201,6202,6203])
        self.set_mesh(trigger_ids=[8500], visible=True) # goldsafebox
        self.set_interact_object(trigger_ids=[10000420], state=0) # goldsafebox
        self.set_effect(trigger_ids=[6100]) # LeverHear
        self.set_effect(trigger_ids=[6200]) # MetalDoor
        self.set_effect(trigger_ids=[6300]) # MetalDoor
        self.set_effect(trigger_ids=[6400]) # GroundDoor
        self.set_effect(trigger_ids=[6401]) # GroundDoor
        self.set_effect(trigger_ids=[6500]) # FallDownScream

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[20002243], quest_states=[1], job_code=90):
            # 퀘스트 진행 중 상태
            return 차전투대기1(self.ctx)


class 차전투대기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25200271, text_id=25200271)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차전투중1(self.ctx)


class 차전투중1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903]):
            return 차전투종료1(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25200271)


class 차전투종료1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 루키등장01(self.ctx)


class 루키등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 루키등장02(self.ctx)


class 루키등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1011')
        self.set_dialogue(type=2, spawn_id=11001610, script='$52000027_QD__MEETROOKIE01__0$', time=3)
        self.set_skip(state=루키등장03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 루키등장03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 루키등장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001584, script='$52000027_QD__MEETROOKIE01__1$', time=3)
        self.set_skip(state=사다리생성01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 사다리생성01(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 사다리생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 사다리생성02(self.ctx)


class 사다리생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8001])
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1012')
        self.select_camera_path(path_ids=[600,601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 사다리생성03(self.ctx)


class 사다리생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=7300, visible=True, initial_sequence='Opened') # lever
        self.set_effect(trigger_ids=[6100], visible=True) # LeverHear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 사다리생성04(self.ctx)


class 사다리생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[4000], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[4001], visible=True, enable=True, fade=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 사다리생성05(self.ctx)


class 사다리생성05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 루키이동01(self.ctx)


class 루키이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$52000027_QD__MEETROOKIE01__2$', time=3, arg5=1)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1013')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 루키이동02(self.ctx)


class 루키이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_dialogue(type=1, spawn_id=102, script='$52000027_QD__MEETROOKIE01__3$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 루키이동03(self.ctx)


class 루키이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=7000, visible=True, initial_sequence='Opened') # door
        self.set_effect(trigger_ids=[6200], visible=True) # MetalDoor
        self.set_mesh(trigger_ids=[8002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 루키이동04(self.ctx)


class 루키이동04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8100])
        self.set_agent(trigger_ids=[8101])
        self.set_agent(trigger_ids=[8102])
        self.set_agent(trigger_ids=[8103])
        self.set_agent(trigger_ids=[8104])
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_1014')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차전투시작2(self.ctx)


class 차전투시작2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[911,912]):
            return 루키이동10(self.ctx)


class 루키이동10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_1015')
        self.set_dialogue(type=1, spawn_id=102, script='$52000027_QD__MEETROOKIE01__4$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9101, spawn_ids=[102]):
            return 루키이동11(self.ctx)


class 루키이동11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return 상황연출01(self.ctx)


class 상황연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001610, script='$52000027_QD__MEETROOKIE01__5$', time=3)
        self.select_camera(trigger_id=700)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 상황연출02(self.ctx)


class 상황연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701)
        self.set_skip(state=상황연출03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 상황연출03(self.ctx)


class 상황연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=702)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 상황연출04(self.ctx)


class 상황연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 루키경고01(self.ctx)


class 루키경고01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001584, script='$52000027_QD__MEETROOKIE01__6$', time=3)
        self.set_skip(state=루키경고02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 루키경고02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 루키경고02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 루키경고03(self.ctx)


class 루키경고03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001610, script='$52000027_QD__MEETROOKIE01__7$', time=5)
        self.set_skip(state=루키경고04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 루키경고04(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 루키경고04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=701, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 레버찾기01(self.ctx)


class 레버찾기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='TrapOpen', value=0)
        self.set_dialogue(type=1, spawn_id=102, script='$52000027_QD__MEETROOKIE01__8$', time=3, arg5=1)
        self.show_guide_summary(entity_id=25200272, text_id=25200272)
        self.set_user_value(trigger_id=2, key='SetLever', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 레버찾기02(self.ctx)


class 레버찾기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrapOpen') == 1:
            return 함정연출01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=25200272)


class 함정연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001610, script='$52000027_QD__MEETROOKIE01__9$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 함정연출02(self.ctx)


class 함정연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 함정연출03(self.ctx)


class 함정연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[6201,6202,6203], enable=True)
        self.set_visible_breakable_object(trigger_ids=[6201,6202,6203], visible=True)
        self.set_effect(trigger_ids=[6500], visible=True) # FallDownScream
        self.set_actor(trigger_id=7201, initial_sequence='Idle_A') # mafia
        self.set_actor(trigger_id=7202, initial_sequence='Idle_A') # mafia
        self.set_actor(trigger_id=7203, initial_sequence='Idle_A') # mafia
        self.set_actor(trigger_id=7100, visible=True, initial_sequence='Opened') # floor
        self.set_actor(trigger_id=7101, visible=True, initial_sequence='Opened') # floor
        self.set_actor(trigger_id=7102, visible=True, initial_sequence='Opened') # floor
        self.set_actor(trigger_id=7103, visible=True, initial_sequence='Opened') # floor
        self.set_mesh(trigger_ids=[8900,8901,8902,8903])
        self.set_effect(trigger_ids=[6400], visible=True) # GroundDoor
        self.set_effect(trigger_ids=[6401], visible=True) # GroundDoor

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 함정연출04(self.ctx)


class 함정연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=800, enable=False)
        self.set_visible_breakable_object(trigger_ids=[6201,6202,6203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 루키이동20(self.ctx)


class 루키이동20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25200273, text_id=25200273, duration=4000)
        self.set_actor(trigger_id=7001, visible=True, initial_sequence='Opened') # door
        self.set_effect(trigger_ids=[6300], visible=True) # MetalDoor
        self.set_mesh(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8200])
        self.set_agent(trigger_ids=[8201])
        self.set_agent(trigger_ids=[8202])
        self.set_agent(trigger_ids=[8203])
        self.set_agent(trigger_ids=[8204])
        self.set_agent(trigger_ids=[8205])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9004]):
            return 루키이동21(self.ctx)


class 루키이동21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$52000027_QD__MEETROOKIE01__10$', time=3, arg5=1)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_1017')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 루키이동22(self.ctx)


class 루키이동22(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9102, spawn_ids=[102]):
            return 루키이동23(self.ctx)


class 루키이동23(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            return 루키미션01(self.ctx)


class 루키미션01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=801)

    def on_tick(self) -> trigger_api.Trigger:
        return 루키미션02(self.ctx)


class 루키미션02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001584, script='$52000027_QD__MEETROOKIE01__11$', time=3)
        self.set_skip(state=루키미션03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 루키미션03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 루키미션03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001584, script='$52000027_QD__MEETROOKIE01__12$', time=4)
        self.set_mesh(trigger_ids=[8500], start_delay=100) # goldsafebox
        self.set_interact_object(trigger_ids=[10000420], state=1) # goldsafebox
        self.set_skip(state=루키미션04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 루키미션04(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 루키미션04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=801, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 미션완료01(self.ctx)


class 미션완료01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[20002243], quest_states=[2]):
            # 퀘스트 완료 가능 상태
            return 미션완료02(self.ctx)


class 미션완료02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 유저퇴장(self.ctx)


class 유저퇴장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000100, portal_id=9, box_id=9900)


initial_state = 대기
