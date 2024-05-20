""" trigger/52010006_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.set_mesh(trigger_ids=[3001])
        self.set_mesh(trigger_ids=[3002,3003,3004,3005], visible=True)
        self.set_mesh(trigger_ids=[3006,3007,3008,3009])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 미카등장(self.ctx)


class 미카등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 미카대사01(self.ctx)


class 미카대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010006_QD__MAIN__0$', time=4)
        self.set_scene_skip(state=미카대사02_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 미카대사02(self.ctx)


class 미카대사02_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 미카대사02(self.ctx)


class 미카대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010006_QD__MAIN__10$', time=4)
        self.set_scene_skip(state=몬스터생성_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 몬스터생성(self.ctx)


class 몬스터생성_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001_A')
        self.spawn_monster(spawn_ids=[2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 미카이동(self.ctx)


class 미카이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=104, spawn_ids=[1001]):
            return 미카교체(self.ctx)


class 미카교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001])
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1001_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[1007]):
            return 사슬(self.ctx)


class 사슬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.set_mesh(trigger_ids=[3001], visible=True, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 카보대사01(self.ctx)


class 카보대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001319, script='$52010006_QD__MAIN__1$', time=5)
        self.set_scene_skip(state=카보대사02_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카보대사02(self.ctx)


class 카보대사02_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 카보대사02(self.ctx)


class 카보대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001319, script='$52010006_QD__MAIN__2$', time=5)
        self.set_scene_skip(state=미카친구들소환_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 미카친구들소환(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 미카친구들소환_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 미카친구들소환(self.ctx)


class 미카친구들소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.spawn_monster(spawn_ids=[1003,1004,1005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 스타츠대사01(self.ctx)


class 스타츠대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_A')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004_A')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_A')
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010006_QD__MAIN__3$', time=2)
        self.set_scene_skip(state=둔바대사01_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 둔바대사01(self.ctx)


class 둔바대사01_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 둔바대사01(self.ctx)


class 둔바대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001217, script='$52010006_QD__MAIN__11$', time=2)
        self.set_scene_skip(state=타라대사01_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 타라대사01(self.ctx)


class 타라대사01_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 타라대사01(self.ctx)


class 타라대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001218, script='$52010006_QD__MAIN__12$', time=3)
        self.set_scene_skip(state=카보대사03_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카보대사03(self.ctx)


class 카보대사03_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 카보대사03(self.ctx)


class 카보대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_A')
        self.set_dialogue(type=2, spawn_id=11001319, script='$52010006_QD__MAIN__4$', time=5)
        self.set_scene_skip(state=카보소환_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카보소환(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 카보소환_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 카보소환(self.ctx)


class 카보소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[1002])
        self.spawn_monster(spawn_ids=[2002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 카보대사04(self.ctx)


class 카보대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2002])
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001319, script='$52010006_QD__MAIN__5$', time=5)
        self.set_scene_skip(state=카보대사05_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 카보대사05(self.ctx)


class 카보대사05_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 카보대사05(self.ctx)


class 카보대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001319, script='$52010006_QD__MAIN__6$', time=5)
        self.move_npc(spawn_id=1006, patrol_name='MS2PatrolData_1002_B')
        self.set_scene_skip(state=사슬해제_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.destroy_monster(spawn_ids=[1006])
            return 사슬해제(self.ctx)


class 사슬해제_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 사슬해제(self.ctx)


class 사슬해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_B')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004_B')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_B')
        self.set_mesh(trigger_ids=[3001], fade=3.0)
        self.set_mesh(trigger_ids=[3002,3003,3004,3005])
        self.set_mesh(trigger_ids=[3006,3007,3008,3009], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1001_D')
            return 스타츠대사02(self.ctx)


class 스타츠대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010006_QD__MAIN__7$', time=5)
        self.set_scene_skip(state=스타츠대사03_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 스타츠대사03(self.ctx)


class 스타츠대사03_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 스타츠대사03(self.ctx)


class 스타츠대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010006_QD__MAIN__8$', time=5)
        self.set_scene_skip(state=스타츠대사04_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 스타츠대사04(self.ctx)


class 스타츠대사04_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 스타츠대사04(self.ctx)


class 스타츠대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010006_QD__MAIN__9$', time=5)
        self.set_scene_skip(state=업적이벤트발생_0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return 업적이벤트발생(self.ctx)


class 업적이벤트발생_0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 업적이벤트발생(self.ctx)


class 업적이벤트발생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_achievement(trigger_id=103, type='trigger', achieve='RescueMika')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2010030, portal_id=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
