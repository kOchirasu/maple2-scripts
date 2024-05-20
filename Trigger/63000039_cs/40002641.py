""" trigger/63000039_cs/40002641.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_off')
        self.set_mesh(trigger_ids=[3000,3001,3002], visible=True)
        self.set_mesh(trigger_ids=[3003,3004,3005])
        self.set_interact_object(trigger_ids=[10001025], state=0)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002641], quest_states=[1]):
            return NPC말풍선(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002641], quest_states=[2]):
            return 유저이동(self.ctx)


class NPC말풍선(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_dialogue(type=1, spawn_id=1002, script='$63000039_CS__40002641__0$', time=4)
            self.set_dialogue(type=1, spawn_id=1005, script='$63000039_CS__40002641__1$', time=4, arg5=2)
            return 오브젝트반응대기(self.ctx)


class 오브젝트반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001025], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001025], state=0):
            self.set_mesh(trigger_ids=[3000,3001,3002])
            self.set_mesh(trigger_ids=[3003,3004,3005], visible=True)
            return NPC를이동(self.ctx)


class NPC를이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001')
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return PC이동(self.ctx)


class PC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, visible=True, initial_sequence='sf_fi_funct_darkdoor_A01_on')
        self.move_user_path(patrol_name='MS2PatrolData_PC')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return PC말풍선(self.ctx)


class PC말풍선(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.set_dialogue(type=1, script='$63000039_CS__40002641__2$', time=4)
        self.set_achievement(trigger_id=199, type='trigger', achieve='SaveBackstreetPeople')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 유저이동조건(self.ctx)


class 유저이동조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[40002641], quest_states=[2]):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302, enable=False)
        self.move_user(map_id=2000275, portal_id=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
