""" trigger/52000030_qd/main_r.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101], job_code=50):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Nutaman_intro.swf', movie_id=1)
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 이슈라대사01(self.ctx)


class 이슈라대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000030_QD__MAIN_R__0$', time=3)
        self.set_dialogue(type=2, spawn_id=11000015, script='$52000030_QD__MAIN_R__1$', time=3)
        self.set_skip(state=NPC_단체_이동)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return NPC_단체_이동(self.ctx)


class NPC_단체_이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001')
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005')
        self.move_npc(spawn_id=1006, patrol_name='MS2PatrolData_1006')
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1007')
        self.move_npc(spawn_id=1008, patrol_name='MS2PatrolData_1008')
        self.move_npc(spawn_id=1009, patrol_name='MS2PatrolData_1009')
        self.move_npc(spawn_id=1010, patrol_name='MS2PatrolData_1010')
        self.move_npc(spawn_id=1011, patrol_name='MS2PatrolData_1011')
        self.move_npc(spawn_id=1012, patrol_name='MS2PatrolData_1001')
        self.move_npc(spawn_id=1013, patrol_name='MS2PatrolData_1002')
        self.move_npc(spawn_id=1014, patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014]):
            return 전투판으로이동(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014])
        self.spawn_monster(spawn_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,2001,2002], auto_target=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 전투판으로이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301, enable=False)
        self.move_user(map_id=52000030, portal_id=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2002]):
            return 차전투2(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[2001])


class 차전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2003,2004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2003]):
            return 이슈라대사02(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[2004])


class 이슈라대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000015, script='$52000030_QD__MAIN_R__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 차전투3(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 차전투3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2005]):
            return 이슈라대사03(self.ctx)


class 이슈라대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000030_QD__MAIN_R__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            self.move_user(map_id=52000031)
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
