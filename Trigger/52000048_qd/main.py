""" trigger/52000048_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], auto_target=False)
        self.spawn_monster(spawn_ids=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110], auto_target=False)
        self.spawn_monster(spawn_ids=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], auto_target=False)
        self.spawn_monster(spawn_ids=[2001])
        self.set_mesh(trigger_ids=[3000], visible=True)
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.move_npc(spawn_id=1101, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1102, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1103, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1104, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1105, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1106, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1107, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1108, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1109, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1110, patrol_name='MS2PatrolData_A')
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_B')
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_B')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_B')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_B')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_B')
        self.move_npc(spawn_id=1006, patrol_name='MS2PatrolData_B')
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_B')
        self.move_npc(spawn_id=1008, patrol_name='MS2PatrolData_B')
        self.move_npc(spawn_id=1009, patrol_name='MS2PatrolData_B')
        self.move_npc(spawn_id=1010, patrol_name='MS2PatrolData_B')
        self.move_npc(spawn_id=1201, patrol_name='MS2PatrolData_C')
        self.move_npc(spawn_id=1202, patrol_name='MS2PatrolData_C')
        self.move_npc(spawn_id=1203, patrol_name='MS2PatrolData_C')
        self.move_npc(spawn_id=1204, patrol_name='MS2PatrolData_C')
        self.move_npc(spawn_id=1205, patrol_name='MS2PatrolData_C')
        self.move_npc(spawn_id=1206, patrol_name='MS2PatrolData_C')
        self.move_npc(spawn_id=1207, patrol_name='MS2PatrolData_C')
        self.move_npc(spawn_id=1208, patrol_name='MS2PatrolData_C')
        self.move_npc(spawn_id=1209, patrol_name='MS2PatrolData_C')
        self.move_npc(spawn_id=1210, patrol_name='MS2PatrolData_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 칸두라이동(self.ctx)


class 칸두라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_K1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            self.set_npc_emotion_sequence(spawn_id=2001, sequence_name='Attack_01_A')
            return 칸두라이동2(self.ctx)


class 칸두라이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], fade=5.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_K2')
            return 카메라이동대기(self.ctx)


class 카메라이동대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 카메라이동2(self.ctx)


class 카메라이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 라오즈등장(self.ctx)


class 라오즈등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.spawn_monster(spawn_ids=[2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return PC말풍선(self.ctx)


class PC말풍선(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC')
        self.set_dialogue(type=1, script='$52000048_QD__MAIN__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 라오즈대사01(self.ctx)


class 라오즈대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001768, script='$52000048_QD__MAIN__1$', time=3)
        self.set_skip(state=라오즈대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라오즈대사02(self.ctx)


class 라오즈대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 라오즈대사02(self.ctx)


class 라오즈대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001768, script='$52000048_QD__MAIN__2$', time=6)
        self.set_skip(state=라오즈대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 라오즈대사03(self.ctx)


class 라오즈대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 라오즈대사03(self.ctx)


class 라오즈대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304)
        self.set_dialogue(type=2, spawn_id=11001768, script='$52000048_QD__MAIN__3$', time=6)
        self.set_skip(state=라오즈대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 퀘스트완료(self.ctx)


class 라오즈대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 퀘스트완료(self.ctx)


class 퀘스트완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=101, type='trigger', achieve='MessageThroughAnimar')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304, enable=False)
        self.move_user(map_id=52000050, portal_id=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
