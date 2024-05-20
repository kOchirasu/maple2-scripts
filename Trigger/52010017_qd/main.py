""" trigger/52010017_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[401])
        self.set_ladder(trigger_ids=[402])
        self.set_ladder(trigger_ids=[403])
        self.set_ladder(trigger_ids=[404])
        self.set_ladder(trigger_ids=[405])
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.set_mesh(trigger_ids=[3001], visible=True)
        self.set_mesh(trigger_ids=[3002])
        self.set_mesh(trigger_ids=[3003], visible=True)
        self.set_mesh(trigger_ids=[3004])
        self.set_mesh(trigger_ids=[3005], visible=True)
        self.set_mesh(trigger_ids=[3006])
        self.set_mesh(trigger_ids=[3007], visible=True)
        self.set_mesh(trigger_ids=[3008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[102], quest_ids=[10002851], quest_states=[1]):
            self.spawn_monster(spawn_ids=[1002], auto_target=False)
            self.spawn_monster(spawn_ids=[1003], auto_target=False)
            self.spawn_monster(spawn_ids=[1004], auto_target=False)
            self.spawn_monster(spawn_ids=[2001])
            return 카메라연출01(self.ctx)


class 카메라연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 미카대사01(self.ctx)


class 미카대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001])
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005')
        self.set_ladder(trigger_ids=[401], visible=True, enable=True)
        self.set_ladder(trigger_ids=[402], visible=True, enable=True)
        self.set_ladder(trigger_ids=[403], visible=True, enable=True)
        self.set_ladder(trigger_ids=[404], visible=True, enable=True)
        self.set_ladder(trigger_ids=[405], visible=True, enable=True)
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010017_QD__MAIN__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 체크포인트01(self.ctx)


class 체크포인트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            self.spawn_monster(spawn_ids=[2002])
            return 카메라연출02(self.ctx)


class 카메라연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 미카대사02(self.ctx)


class 미카대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010017_QD__MAIN__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.select_camera(trigger_id=302, enable=False)
            return 체크포인트02(self.ctx)


class 체크포인트02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_A')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_A')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004_A')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2002]):
            return 미키이동01(self.ctx)


class 미키이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_A2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=103, spawn_ids=[1005]):
            return 오브젝트01(self.ctx)


class 오브젝트01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_mesh(trigger_ids=[3001])
            self.set_mesh(trigger_ids=[3002], visible=True)
            return 카메라연출03(self.ctx)


class 카메라연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 타라대사01(self.ctx)


class 타라대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001218, script='$52010017_QD__MAIN__2$', time=2)
        self.select_camera(trigger_id=303)
        self.spawn_monster(spawn_ids=[2003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 체크포인트03(self.ctx)


class 체크포인트03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=303, enable=False)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_B')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_B')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004_B')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2003]):
            return 미키이동02(self.ctx)


class 미키이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_B2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=104, spawn_ids=[1005]):
            return 오브젝트02(self.ctx)


class 오브젝트02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_mesh(trigger_ids=[3003])
            self.set_mesh(trigger_ids=[3004], visible=True)
            return 카메라연출04(self.ctx)


class 카메라연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 둔바대사01(self.ctx)


class 둔바대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304)
        self.set_dialogue(type=2, spawn_id=11001217, script='$52010017_QD__MAIN__3$', time=2)
        self.spawn_monster(spawn_ids=[2004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 체크포인트04(self.ctx)


class 체크포인트04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=304, enable=False)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_C')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_C')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004_C')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2004]):
            return 미키이동03(self.ctx)


class 미키이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_C2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=105, spawn_ids=[1005]):
            return 오브젝트03(self.ctx)


class 오브젝트03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_mesh(trigger_ids=[3005])
            self.set_mesh(trigger_ids=[3006], visible=True)
            return 카메라연출05(self.ctx)


class 카메라연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 스타츠대사01(self.ctx)


class 스타츠대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010017_QD__MAIN__4$', time=2)
        self.spawn_monster(spawn_ids=[2005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 체크포인트05(self.ctx)


class 체크포인트05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=305, enable=False)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_D')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_D')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004_D')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2005]):
            return 미키이동04(self.ctx)


class 미키이동04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_D2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=106, spawn_ids=[1005]):
            return 오브젝트04(self.ctx)


class 오브젝트04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_mesh(trigger_ids=[3007])
            self.set_mesh(trigger_ids=[3008], visible=True)
            return 카메라연출06(self.ctx)


class 카메라연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_D3')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 미카대사03(self.ctx)


class 미카대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010017_QD__MAIN__5$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 미카대사04(self.ctx)


class 미카대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010017_QD__MAIN__6$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 이동대기(self.ctx)


class 이동대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=110, type='trigger', achieve='Getalllamestone')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.move_user(map_id=2010034, portal_id=3, box_id=110)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
