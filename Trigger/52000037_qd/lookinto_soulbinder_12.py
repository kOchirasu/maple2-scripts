""" trigger/52000037_qd/lookinto_soulbinder_12.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, initial_sequence='Dead_A') # NelfActor
        self.set_portal(portal_id=2)
        self.set_interact_object(trigger_ids=[10000175], state=0) # Bag

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[60100065], quest_states=[2], job_code=110):
            return 연출01조건(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[60100065], quest_states=[3], job_code=110):
            return NPC만배치(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class NPC만배치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Dead_A') # NelfActor
        self.spawn_monster(spawn_ids=[101], auto_target=False) # NelfDummyNPC
        self.set_interact_object(trigger_ids=[10000175], state=1) # Bag

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 연출01조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Dead_A') # NelfActor
        self.spawn_monster(spawn_ids=[101], auto_target=False) # NelfDummyNPC
        self.set_interact_object(trigger_ids=[10000175], state=1) # Bag

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9300], quest_ids=[60100065], quest_states=[2], job_code=110):
            return 연출01시작(self.ctx)


class 연출01시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000037, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.move_user_path(patrol_name='MS2PatrolData_PC1101A')
            return PC말풍선01(self.ctx)


class PC말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__LOOKINTO_SOULBINDER_12__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC말풍선02(self.ctx)


class PC말풍선02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__LOOKINTO_SOULBINDER_12__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선03(self.ctx)


class PC말풍선03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__LOOKINTO_SOULBINDER_12__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선04(self.ctx)


class PC말풍선04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__LOOKINTO_SOULBINDER_12__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선05(self.ctx)


class PC말풍선05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__LOOKINTO_SOULBINDER_12__4$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 강제이동02조건(self.ctx)


class 강제이동02조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9301], quest_ids=[60100065], quest_states=[2], job_code=110):
            return PC말풍선07(self.ctx)


class PC말풍선07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__LOOKINTO_SOULBINDER_12__5$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 강제이동02(self.ctx)


class 강제이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC1101B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9302], quest_ids=[60100065], quest_states=[2], job_code=110):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Wait
