""" trigger/52000029_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[606])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,2001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 구르는천둥대사01(self.ctx)


class 구르는천둥대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001581, script='$52000029_QD__MAIN__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 유페리아대사01(self.ctx)


class 유페리아대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_dialogue(type=2, spawn_id=11001564, script='$52000029_QD__MAIN__1$', time=2)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.select_camera(trigger_id=3022)
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001_A')
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPC이동2(self.ctx)


class NPC이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_A')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004_A')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPC이동3(self.ctx)


class NPC이동3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1006, patrol_name='MS2PatrolData_1006_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이펙트연출(self.ctx)


class 이펙트연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[2001], skill_id=71000003, level=1, is_skill_set=False)
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 이슈라이동01(self.ctx)


class 이슈라이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 이슈라대사01(self.ctx)


class 이슈라대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000029_QD__MAIN__2$', time=2) # 음성 코드 00001296

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 홀슈타트방향전환(self.ctx)


class 홀슈타트방향전환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 홀슈타트대사01(self.ctx)


class 홀슈타트대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=2, spawn_id=11001231, script='$52000029_QD__MAIN__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 홀슈타트도망(self.ctx)


class 홀슈타트도망(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=3055)
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001_B')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이슈라추격(self.ctx)


class 이슈라추격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001,1002,1004,1005,1006])
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)
        self.spawn_monster(spawn_ids=[1009], auto_target=False)
        self.spawn_monster(spawn_ids=[1010], auto_target=False)
        self.spawn_monster(spawn_ids=[1011], auto_target=False)
        self.spawn_monster(spawn_ids=[1101], auto_target=False)
        self.spawn_monster(spawn_ids=[1102], auto_target=False)
        self.spawn_monster(spawn_ids=[1104], auto_target=False)
        self.spawn_monster(spawn_ids=[1105], auto_target=False)
        self.spawn_monster(spawn_ids=[1106], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NPC집결(self.ctx)


class NPC집결(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=306)
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1007_B')
        self.move_npc(spawn_id=1008, patrol_name='MS2PatrolData_1008_B')
        self.move_npc(spawn_id=1009, patrol_name='MS2PatrolData_1009_B')
        self.move_npc(spawn_id=1010, patrol_name='MS2PatrolData_1010_B')
        self.move_npc(spawn_id=1011, patrol_name='MS2PatrolData_1011_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 렌듀비앙대사01(self.ctx)


class 렌듀비앙대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000029_QD__MAIN__4$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스대사01(self.ctx)


class 아노스대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=307)
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_dialogue(type=2, spawn_id=11000032, script='$52000029_QD__MAIN__5$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 제나대사01(self.ctx)


class 제나대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001583, script='$52000029_QD__MAIN__6$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 유페리아대사02(self.ctx)


class 유페리아대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[609], visible=True)
        self.set_dialogue(type=2, spawn_id=11001564, script='$52000029_QD__MAIN__7$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 이슈라대사02(self.ctx)


class 이슈라대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=308)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000029_QD__MAIN__8$', time=2) # 음성 코드 00001297

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 이슈라대사03(self.ctx)


class 이슈라대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000029_QD__MAIN__9$', time=11) # 음성 코드 00001298

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11500):
            return 이슈라대사04(self.ctx)


class 이슈라대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=306)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_D')
        self.set_effect(trigger_ids=[605], visible=True)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000029_QD__MAIN__10$', time=6) # 음성 코드 00001299

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 렌듀비앙대사02(self.ctx)


class 렌듀비앙대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000029_QD__MAIN__11$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 렌듀비앙이동(self.ctx)


class 렌듀비앙이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1007_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 렌듀비앙캐스팅(self.ctx)


class 렌듀비앙캐스팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[1007], skill_id=71000004, level=1, is_skill_set=False)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_C')
        self.select_camera(trigger_id=309)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 이슈라대사05(self.ctx)


class 이슈라대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000029_QD__MAIN__12$', time=3) # 음성 코드 00001300

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.move_user(map_id=52000030)
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
