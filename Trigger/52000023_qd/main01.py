""" trigger/52000023_qd/main01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # 종이문서 발견 사운드 이펙트
        self.set_effect(trigger_ids=[6001]) # Ishura Voice 00001274
        self.set_effect(trigger_ids=[6002]) # Ishura Voice 00001275
        self.set_effect(trigger_ids=[6003]) # Ishura Voice 00001276
        self.set_effect(trigger_ids=[6004]) # Ishura Voice 00001277
        self.set_effect(trigger_ids=[6005]) # Ishura Voice 00001278
        self.set_effect(trigger_ids=[6006]) # Ishura Voice 00001279
        self.set_effect(trigger_ids=[6007]) # Ishura Voice 00001280
        self.set_effect(trigger_ids=[6008]) # Ishura Voice 00001281
        self.set_effect(trigger_ids=[6009]) # Ishura Voice 00001282
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8100])
        self.set_agent(trigger_ids=[8101])
        self.set_agent(trigger_ids=[8102])
        self.set_agent(trigger_ids=[8103])
        self.set_agent(trigger_ids=[8104])
        self.set_agent(trigger_ids=[8105])
        self.set_agent(trigger_ids=[8106])
        self.set_agent(trigger_ids=[8107])
        self.set_agent(trigger_ids=[8108])
        self.set_agent(trigger_ids=[8109])
        self.set_mesh(trigger_ids=[3000])
        self.set_interact_object(trigger_ids=[10000617], state=0)
        self.set_interact_object(trigger_ids=[10000618], state=0)
        self.set_interact_object(trigger_ids=[10000619], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[20002230], quest_states=[1]):
            # 퀘스트 진행 중 상태
            return 연출준비(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8100], visible=True)
        self.set_agent(trigger_ids=[8101], visible=True)
        self.set_agent(trigger_ids=[8102], visible=True)
        self.set_agent(trigger_ids=[8103], visible=True)
        self.set_agent(trigger_ids=[8104], visible=True)
        self.set_agent(trigger_ids=[8105], visible=True)
        self.set_agent(trigger_ids=[8106], visible=True)
        self.set_agent(trigger_ids=[8107], visible=True)
        self.set_agent(trigger_ids=[8108], visible=True)
        self.set_agent(trigger_ids=[8109], visible=True)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[901,902,903,904,905,906,907,908,909,910], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 유저이동01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 유저이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 유저이동02(self.ctx)


class 유저이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_100')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 유저이동03(self.ctx)


class 유저이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[601,602], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투준비01(self.ctx)


class 전투준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True) # Ishura Voice 00001274
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000023_QD__MAIN01__0$', time=6) # 음성코드 	00001274
        self.set_skip(state=전투준비02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 전투준비02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 전투준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001]) # Ishura Voice 00001274
        self.set_effect(trigger_ids=[6002], visible=True) # Ishura Voice 00001275
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000023_QD__MAIN01__1$', time=4) # 음성코드 	00001275
        self.set_skip(state=전투시작)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투시작(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=603, enable=False)
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8100])
        self.set_agent(trigger_ids=[8101])
        self.set_agent(trigger_ids=[8102])
        self.set_agent(trigger_ids=[8103])
        self.set_agent(trigger_ids=[8104])
        self.set_agent(trigger_ids=[8105])
        self.set_agent(trigger_ids=[8106])
        self.set_agent(trigger_ids=[8107])
        self.set_agent(trigger_ids=[8108])
        self.set_agent(trigger_ids=[8109])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903,904,905,906,907,908,909,910]):
            return 대화준비01(self.ctx)


class 대화준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002]) # Ishura Voice 00001275
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대화준비02(self.ctx)


class 대화준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_200')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return 대화준비03(self.ctx)


class 대화준비03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이슈라대화01(self.ctx)


class 이슈라대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003], visible=True) # Ishura Voice 00001276
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000023_QD__MAIN01__2$', time=8) # 음성코드 	00001276
        self.set_skip(state=이슈라대화02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 이슈라대화02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 이슈라대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003]) # Ishura Voice 00001276
        self.set_effect(trigger_ids=[6004], visible=True) # Ishura Voice 00001277
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000023_QD__MAIN01__3$', time=8) # 음성코드 	00001277
        self.set_skip(state=이슈라대화03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 이슈라대화03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 이슈라대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6004]) # Ishura Voice 00001277
        self.set_effect(trigger_ids=[6005], visible=True) # Ishura Voice 00001278
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000023_QD__MAIN01__4$', time=7) # 음성코드 	00001278
        self.set_skip(state=이슈라대화04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 이슈라대화04(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 이슈라대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6005]) # Ishura Voice 00001278
        self.set_effect(trigger_ids=[6006], visible=True) # Ishura Voice 00001279
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000023_QD__MAIN01__5$', time=6) # 음성코드 	00001279
        self.set_skip(state=수색준비)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 수색준비(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 수색준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6006]) # Ishura Voice 00001279
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.set_interact_object(trigger_ids=[10000617], state=1)
        self.set_interact_object(trigger_ids=[10000618], state=1)
        self.set_interact_object(trigger_ids=[10000619], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 수색시작(self.ctx)


class 수색시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=25200231, text_id=25200231)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000617], state=0):
            return 수색종료01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[5001], visible=True) # 종이문서 발견 사운드 이펙트
        self.set_mesh(trigger_ids=[3000], visible=True)


class 수색종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000618], state=0)
        self.set_interact_object(trigger_ids=[10000619], state=0)
        self.hide_guide_summary(entity_id=25200231)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 수색종료02(self.ctx)


class 수색종료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_104')
        self.set_effect(trigger_ids=[6007], visible=True) # Ishura Voice 00001280
        self.set_dialogue(type=1, spawn_id=103, script='$52000023_QD__MAIN01__6$', time=3) # 음성코드 	00001280

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 정리준비01(self.ctx)


class 정리준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_102')
        self.select_camera(trigger_id=604)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9003, spawn_ids=[103]):
            return 정리준비02(self.ctx)


class 정리준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6007]) # Ishura Voice 00001280

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 정리대화01(self.ctx)


class 정리대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6008], visible=True) # Ishura Voice 00001281
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000023_QD__MAIN01__7$', time=9) # 음성코드 	00001281
        self.set_skip(state=정리대화02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 정리대화02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 정리대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6008]) # Ishura Voice 00001281
        self.set_effect(trigger_ids=[6009], visible=True) # Ishura Voice 00001282
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000023_QD__MAIN01__8$', time=5) # 음성코드 	00001282
        self.set_skip(state=퇴장준비)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 퇴장준비(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 퇴장준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=604, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 퇴장중(self.ctx)


class 퇴장중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9900, type='trigger', achieve='MeetAgain_Ishura')
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9004, spawn_ids=[103]):
            return 퇴장완료(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[103])


class 퇴장완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6009]) # Ishura Voice 00001282


initial_state = 대기
