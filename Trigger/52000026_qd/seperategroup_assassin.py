""" trigger/52000026_qd/seperategroup_assassin.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=10000) # TriaAttack
        self.set_effect(trigger_ids=[5000]) # LeftDoorOpen
        self.set_effect(trigger_ids=[5001]) # LeftDoorClose
        self.set_effect(trigger_ids=[5002]) # RightDoorOpen
        self.set_effect(trigger_ids=[5003]) # RightDoorClose
        self.set_effect(trigger_ids=[5004]) # blastjump
        # Asimov Voice 00000553 / everytime
        self.set_effect(trigger_ids=[6001])
        # Asimov Voice 00001338 / everytime
        self.set_effect(trigger_ids=[6002])
        # Asimov Voice 00001339 / everytime
        self.set_effect(trigger_ids=[6003])
        # Asimov Voice 00001340 / everytime
        self.set_effect(trigger_ids=[6004])
        # Asimov Voice 00001341 / in case RuneBlader, Berserker, Priest, Wizard
        self.set_effect(trigger_ids=[6005])
        # Asimov Voice 00001342 / in case RuneBlader, Wizard
        self.set_effect(trigger_ids=[6006])
        # Asimov Voice 00000561 / in case Berserker
        self.set_effect(trigger_ids=[6007])
        # Ishura Voice 00001291 / only RB
        self.set_effect(trigger_ids=[6101])
        # Ishura Voice 00001292 / everytime
        self.set_effect(trigger_ids=[6102])
        # Ishura Voice 00001293 / only RB
        self.set_effect(trigger_ids=[6103])
        # Ishura Voice 00001155 / in case Assassin, Berserker, Heavygunner, Knight, Priest, Ranger, Thief, Wizard
        self.set_effect(trigger_ids=[6104])
        # Ishura Voice 00001159 / in case Assassin, Berserker, Heavygunner, Knight, Priest, Ranger, Thief, Wizard
        self.set_effect(trigger_ids=[6105])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10003010], quest_states=[1], job_code=80):
            # 퀘스트 진행 중 상태
            return 연출준비01(self.ctx)


class 연출준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출준비02(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 연출준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 유저이동01(self.ctx)


class 유저이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3001)
        self.move_user_path(patrol_name='MS2PatrolData_2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 차입장01_1(self.ctx)


class 차입장01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,201])
        self.set_effect(trigger_ids=[5000], visible=True) # LeftDoorOpen
        self.move_user_path(patrol_name='MS2PatrolData_2001')
        self.select_camera(trigger_id=3002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차입장02_1(self.ctx)


class 차입장02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # LeftDoorClose
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        self.select_camera_path(path_ids=[3003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차입장03_1(self.ctx)


class 차입장03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000601, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__0$', time=3)
        self.set_skip(state=차입장01_2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차입장01_2(self.ctx)


class 차입장01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[5002], visible=True) # RightDoorOpen
        self.select_camera(trigger_id=3100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차입장02_2(self.ctx)


class 차입장02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301])
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_301')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_202')
        self.move_user_path(patrol_name='MS2PatrolData_2002')
        self.set_effect(trigger_ids=[5003], visible=True) # RightDoorClose

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차입장03_2(self.ctx)


class 차입장03_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401])
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_401')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차입장04_2(self.ctx)


class 차입장04_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6104], visible=True) # 음성 코드 00001155
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__1$', time=4) # 음성 코드 00001155
        self.set_skip(state=차입장05_2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차입장05_2(self.ctx)


class 차입장05_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[6101]) # Ishura Voice 00001291
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_302')
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_402')
        self.move_user_path(patrol_name='MS2PatrolData_2003')
        self.select_camera(trigger_id=3101)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차입장01_3(self.ctx)


class 차입장01_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # RightDoorOpen
        self.spawn_monster(spawn_ids=[501])
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_501')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차입장02_3(self.ctx)


class 차입장02_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[601])
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData_601')
        self.set_effect(trigger_ids=[5003], visible=True) # RightDoorClose

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차입장03_3(self.ctx)


class 차입장03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3102)
        self.set_effect(trigger_ids=[6001], visible=True) # Asimov Voice 00000553
        self.set_dialogue(type=2, spawn_id=11000031, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__2$', time=7) # 음성 코드 00000553
        self.set_skip(state=차입장01_4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 차입장01_4(self.ctx)


class 차입장01_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[6001]) # Asimov Voice 00000553
        self.select_camera(trigger_id=3200)
        self.set_effect(trigger_ids=[5002], visible=True) # RightDoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차입장02_4(self.ctx)


class 차입장02_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3210)
        self.spawn_monster(spawn_ids=[701])
        self.move_npc(spawn_id=701, patrol_name='MS2PatrolData_701')
        self.set_effect(trigger_ids=[5003], visible=True) # RightDoorClose

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차입장03_4(self.ctx)


class 차입장03_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001581, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__3$', time=4)
        self.set_skip(state=차입장04_4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차입장04_4(self.ctx)


class 차입장04_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=3201)
        self.spawn_monster(spawn_ids=[801])
        self.move_npc(spawn_id=801, patrol_name='MS2PatrolData_801')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차입장05_4(self.ctx)


class 차입장05_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__4$', time=4)
        self.set_skip(state=차입장06_4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차입장06_4(self.ctx)


class 차입장06_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차입장01_5(self.ctx)


class 차입장01_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004], visible=True) # blastjump

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차입장02_5(self.ctx)


class 차입장02_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=701, patrol_name='MS2PatrolData_702')
        self.select_camera(trigger_id=3300)
        self.spawn_monster(spawn_ids=[901])
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차입장03_5(self.ctx)


class 차입장03_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001583, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__5$', time=3)
        self.set_skip(state=차입장04_5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차입장04_5(self.ctx)


class 차입장04_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=3301)
        self.spawn_monster(spawn_ids=[1001])
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차입장05_5(self.ctx)


class 차입장05_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001584, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__6$', time=3)
        self.set_skip(state=차입장06_5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 차입장06_5(self.ctx)


class 차입장06_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차입장07_2(self.ctx)


class 차입장07_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001584, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__7$', time=4)
        self.set_skip(state=차입장08_5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차입장08_5(self.ctx)


class 차입장08_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=3302)
        self.spawn_monster(spawn_ids=[1101])
        self.move_npc(spawn_id=1101, patrol_name='MS2PatrolData_1101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차입장09_5(self.ctx)


class 차입장09_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000015, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__8$', time=4)
        self.set_skip(state=차입장10_5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차입장10_5(self.ctx)


class 차입장10_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[5002], visible=True) # RightDoorOpen
        self.select_camera(trigger_id=3303)
        self.spawn_monster(spawn_ids=[1201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 차입장11_5(self.ctx)


class 차입장11_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True) # RightDoorClose
        self.move_npc(spawn_id=1201, patrol_name='MS2PatrolData_1201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 차입장12_5(self.ctx)


class 차입장12_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001586, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__9$', time=3)
        self.set_skip(state=차입장13_5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차입장13_5(self.ctx)


class 차입장13_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=3304)
        self.move_npc(spawn_id=801, patrol_name='MS2PatrolData_802')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차입장14_5(self.ctx)


class 차입장14_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__10$', time=3)
        self.set_skip(state=입장완료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 입장완료01(self.ctx)


class 입장완료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_sound(trigger_id=10000, enable=True) # TriaAttack
        self.select_camera_path(path_ids=[3400,3401,3402,3403], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 정렬01(self.ctx)


class 정렬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002], visible=True) # Asimov Voice 00001338
        self.set_dialogue(type=2, spawn_id=11000031, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__11$', time=5) # 음성 코드 00001338
        self.set_skip(state=정렬02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 정렬02(self.ctx)


class 정렬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_502')
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData_602')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 정렬03(self.ctx)


class 정렬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1002')
        self.move_npc(spawn_id=1201, patrol_name='MS2PatrolData_1202')
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_902')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 정렬04(self.ctx)


class 정렬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2004')
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_303')
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_403')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 정렬05(self.ctx)


class 정렬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_103')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_203')
        self.move_npc(spawn_id=1101, patrol_name='MS2PatrolData_1102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 정렬06(self.ctx)


class 정렬06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002]) # Asimov Voice 00001338
        self.move_npc(spawn_id=701, patrol_name='MS2PatrolData_703')
        self.move_npc(spawn_id=801, patrol_name='MS2PatrolData_803')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 본론01(self.ctx)


class 본론01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003], visible=True) # Asimov Voice 00001339
        self.set_dialogue(type=2, spawn_id=11000031, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__12$', time=10) # 음성 코드 00001339
        self.set_skip(state=본론02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 본론02(self.ctx)


class 본론02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 본론03(self.ctx)


class 본론03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003]) # Asimov Voice 00001339
        self.set_effect(trigger_ids=[6004], visible=True) # Asimov Voice 00001340
        self.set_dialogue(type=2, spawn_id=11000031, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__13$', time=6) # 음성 코드 00001340
        self.set_skip(state=본론04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 본론04(self.ctx)


class 본론04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[6004]) # Asimov Voice 00001340
        self.select_camera(trigger_id=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 본론05(self.ctx)


class 본론05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_304')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 본론06(self.ctx)


class 본론06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2005')
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_404')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 본론07(self.ctx)


class 본론07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6102], visible=True) # Ishura Voice 00001292
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__14$', time=5) # 음성 코드 00001292
        self.set_skip(state=영상01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 영상01(self.ctx)


class 영상01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_effect(trigger_ids=[6102]) # Ishura Voice 00001292

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 영상02(self.ctx)


class 영상02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Royal_IshuraRemember.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상03(self.ctx)


class 영상03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 영상04(self.ctx)


class 영상04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 정리01(self.ctx)


class 정리01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3600)
        self.set_effect(trigger_ids=[6105], visible=True) # 음성 코드 00001159
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__15$', time=6)
        self.set_skip(state=정리02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 정리02(self.ctx)


class 정리02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_effect(trigger_ids=[6103]) # Ishura Voice 00001293

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 반대01(self.ctx)


class 반대01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__16$', time=4)
        self.set_skip(state=반대02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 반대02(self.ctx)


class 반대02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=3601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 반대03(self.ctx)


class 반대03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001586, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__17$', time=4)
        self.set_skip(state=반대04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 반대04(self.ctx)


class 반대04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.move_npc(spawn_id=1201, patrol_name='MS2PatrolData_1203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 반대05(self.ctx)


class 반대05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3602)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 반대06(self.ctx)


class 반대06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001584, script='$52000026_QD__SEPERATEGROUP_ASSASSIN__18$', time=4)
        self.set_skip(state=반대07)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 반대07(self.ctx)


class 반대07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1003')
        self.select_camera(trigger_id=3603)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 반대09(self.ctx)


"""
class 반대08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3604)
        self.set_dialogue(type=2, spawn_id=11000015, script='상황은 알겠지만 확실치도 않은 일에 무조건 병력을 지원하는 것은… 흠…\\n생각을 좀 해 봐야겠군요. 연락드리죠.', time=4)
        self.set_skip(state=반대09)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 반대09(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()
"""

class 반대09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1101, patrol_name='MS2PatrolData_1103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 반대10(self.ctx)


class 반대10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_903')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료01(self.ctx)


class 연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3801)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출종료02(self.ctx)


class 연출종료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[1201,1001])
        self.destroy_monster(spawn_ids=[1101,901])
        self.select_camera(trigger_id=3801, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 업적발생(self.ctx)


class 업적발생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9001, type='trigger', achieve='SeperateGroup')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 강제퇴장(self.ctx)


class 강제퇴장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000001, portal_id=17, box_id=9001)

    def on_exit(self) -> None:
        self.set_sound(trigger_id=10000) # TriaAttack


initial_state = 대기
