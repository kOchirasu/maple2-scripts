""" trigger/52000043_qd/50001452.xml """
import trigger_api


class 선행퀘스트체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001017], state=2)
        self.set_interact_object(trigger_ids=[10001018], state=2)
        self.set_interact_object(trigger_ids=[10001019], state=2)
        self.set_interact_object(trigger_ids=[10001020], state=2)
        self.set_interact_object(trigger_ids=[10001021], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001451], quest_states=[3]):
            self.destroy_monster(spawn_ids=[1001,2001])
            return 시작조건(self.ctx)


class 시작조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001452], quest_states=[1]):
            return 연출시작(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001452], quest_states=[2]):
            self.destroy_monster(spawn_ids=[1003,2003])
            return NPC만배치(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001452], quest_states=[3]):
            self.destroy_monster(spawn_ids=[1003,2003])
            return NPC만배치(self.ctx)


class NPC만배치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001,2001])
        self.spawn_monster(spawn_ids=[1003,2003], auto_target=False)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001454], quest_states=[2]):
            self.destroy_monster(spawn_ids=[1003,2003])
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001454], quest_states=[3]):
            self.destroy_monster(spawn_ids=[1003,2003])
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001,2001])
        self.spawn_monster(spawn_ids=[1002,2002], auto_target=False)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], visible=True)
        self.select_camera(trigger_id=304)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPC이동01(self.ctx)


class NPC이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002A')
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2002A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=101, spawn_ids=[2002]):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002B')
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2002B')
        self.set_interact_object(trigger_ids=[10001017], state=1)
        self.set_interact_object(trigger_ids=[10001018], state=1)
        self.set_interact_object(trigger_ids=[10001019], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001019], state=0):
            return 부서짐연출(self.ctx)


class 부서짐연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001017], state=2)
        self.set_interact_object(trigger_ids=[10001018], state=2)
        self.set_interact_object(trigger_ids=[10001020], state=1)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017], interval=200, fade=2.0)
        self.select_camera(trigger_id=306)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=향로반응대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 향로반응대기(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(trigger_id=306, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 향로반응대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001452], quest_states=[2]):
            return NPC이동02(self.ctx)


class NPC이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002C')
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2002C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[1002]):
            return NPC교체01(self.ctx)


class NPC교체01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1002])
        self.spawn_monster(spawn_ids=[1003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=103, spawn_ids=[2002]):
            return NPC교체02(self.ctx)


class NPC교체02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2002])
        self.spawn_monster(spawn_ids=[2003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 선행퀘스트체크
