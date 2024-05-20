""" trigger/52000032_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, initial_sequence='Idle_A')
        self.set_mesh(trigger_ids=[3001,3002,3003])
        self.set_mesh(trigger_ids=[3004])
        self.set_mesh(trigger_ids=[3005], visible=True)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[606])
        self.set_effect(trigger_ids=[607])
        self.set_effect(trigger_ids=[608])
        self.set_effect(trigger_ids=[609])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,2001], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 홀슈타트변신(self.ctx)


class 홀슈타트변신(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2001])
        self.spawn_monster(spawn_ids=[2002], auto_target=False)
        self.set_effect(trigger_ids=[601])
        # self.set_mesh(trigger_ids=[3001,3002,3003], fade=2.0)
        self.set_effect(trigger_ids=[605], visible=True)
        self.add_buff(box_ids=[2002], skill_id=71000005, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 유페리아대사01(self.ctx)


class 유페리아대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Idle_A')
        self.select_camera(trigger_id=3022)
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_dialogue(type=2, spawn_id=11001564, script='$52000032_QD__MAIN__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 유페리아돌진(self.ctx)


class 유페리아돌진(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 카메라전환(self.ctx)


class 카메라전환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 이슈라돌진(self.ctx)


class 이슈라돌진(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603], visible=True)
        self.select_camera(trigger_id=3033)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=550):
            return 홀슈타트어택(self.ctx)


class 홀슈타트어택(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2002_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            self.set_effect(trigger_ids=[604], visible=True)
            self.set_effect(trigger_ids=[602], visible=True)
            return 화면전환대기(self.ctx)


class 화면전환대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            self.destroy_monster(spawn_ids=[1001,1003])
            return 홀슈타트대사01(self.ctx)


class 홀슈타트대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3034)
        self.set_dialogue(type=2, spawn_id=11001231, script='$52000032_QD__MAIN__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 홀슈타트이동(self.ctx)


class 홀슈타트이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2002_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[2002]):
            return 홀슈타트소멸(self.ctx)


class 홀슈타트소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1101,1102], auto_target=False)
        self.destroy_monster(spawn_ids=[2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, initial_sequence='Idle_A')
        self.spawn_monster(spawn_ids=[2099], auto_target=False)
        # self.select_camera(trigger_id=304)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101], job_code=1):
            return 투입대사10(self.ctx)
        if self.user_detected(box_ids=[101], job_code=10):
            return 투입대사10(self.ctx)
        if self.user_detected(box_ids=[101], job_code=20):
            return 투입대사20(self.ctx)
        if self.user_detected(box_ids=[101], job_code=30):
            return 투입대사30(self.ctx)
        if self.user_detected(box_ids=[101], job_code=40):
            return 투입대사40(self.ctx)
        if self.user_detected(box_ids=[101], job_code=50):
            return 투입대사50(self.ctx)
        if self.user_detected(box_ids=[101], job_code=60):
            return 투입대사60(self.ctx)
        if self.user_detected(box_ids=[101], job_code=70):
            return 투입대사70(self.ctx)
        if self.user_detected(box_ids=[101], job_code=80):
            return 투입대사80(self.ctx)
        if self.user_detected(box_ids=[101], job_code=90):
            return 투입대사90(self.ctx)


class 투입대사10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__2$', time=2)
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000032_QD__MAIN__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__4$', time=2)
        self.set_dialogue(type=2, spawn_id=11001581, script='$52000032_QD__MAIN__5$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__6$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 투입대사30_1(self.ctx)


class 투입대사30_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_dialogue(type=2, spawn_id=11000032, script='$52000032_QD__MAIN__7$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 누타만전투(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__8$', time=2)
        self.set_dialogue(type=2, spawn_id=11001578, script='$52000032_QD__MAIN__9$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__10$', time=2)
        self.set_dialogue(type=2, spawn_id=11000015, script='$52000032_QD__MAIN__11$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__12$', time=2)
        self.set_dialogue(type=2, spawn_id=11001583, script='$52000032_QD__MAIN__13$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사70(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__14$', time=2)
        self.set_dialogue(type=2, spawn_id=11001586, script='$52000032_QD__MAIN__15$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사80(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__16$', time=2)
        self.set_dialogue(type=2, spawn_id=11001584, script='$52000032_QD__MAIN__17$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사90(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__18$', time=2)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__19$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 누타만전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 누타만전투종료(self.ctx)


class 누타만전투종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=305)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 렌듀비앙대사01(self.ctx)


class 렌듀비앙대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1103,1104], auto_target=False)
        self.select_camera(trigger_id=304)
        self.set_dialogue(type=2, spawn_id=11001575, script='$52000032_QD__MAIN__20$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 유페리아대사_흐느낌(self.ctx)


class 유페리아대사_흐느낌(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_dialogue(type=2, spawn_id=11001576, script='$52000032_QD__MAIN__21$', time=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8500):
            return 아노스대사01(self.ctx)


class 아노스대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[609], visible=True)
        self.set_dialogue(type=2, spawn_id=11000032, script='$52000032_QD__MAIN__22$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 렌듀비앙대사02(self.ctx)


class 렌듀비앙대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000032_QD__MAIN__23$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 렌듀비앙이동(self.ctx)


class 렌듀비앙이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1103, patrol_name='MS2PatrolData_1103_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 렌듀비앙캐스팅(self.ctx)


class 렌듀비앙캐스팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[1103], skill_id=71000004, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3004], visible=True, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=199, type='trigger', achieve='ClearNutaman')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2000023, portal_id=100)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
