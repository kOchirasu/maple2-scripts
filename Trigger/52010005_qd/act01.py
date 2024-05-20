""" trigger/52010005_qd/act01.xml """
import trigger_api


class 퀘스트조건01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.set_interact_object(trigger_ids=[10000872], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002820], quest_states=[2]):
            # 1st Quest
            return Q1_마샤르교체01(self.ctx)


# 1st Quest
class Q1_마샤르교체01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Q1_딜레이01(self.ctx)


class Q1_딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return Q1_미카등장(self.ctx)


class Q1_미카등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2010')

    def on_tick(self) -> trigger_api.Trigger:
        return Q1_마샤르이동01(self.ctx)


class Q1_마샤르이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_1020')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8001, spawn_ids=[102]):
            return Q1_마샤르대화01(self.ctx)


class Q1_마샤르대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$52010005_QD__ACT01__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8002, spawn_ids=[102]):
            return Q1_마샤르대화02(self.ctx)


class Q1_마샤르대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=3)
        self.set_dialogue(type=1, spawn_id=102, script='$52010005_QD__ACT01__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return Q1_카메라연출01(self.ctx)


class Q1_카메라연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=3)
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.select_camera(trigger_id=1001)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return Q1_카메라연출02(self.ctx)


class Q1_카메라연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=5)
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010005_QD__ACT01__2$', time=4)
        self.set_skip(state=Q1_카메라연출03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return Q1_카메라연출03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Q1_카메라연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='7', seconds=1)
        self.select_camera(trigger_id=1001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return Q1_마샤르교체02(self.ctx)


class Q1_마샤르교체02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104])
        self.spawn_monster(spawn_ids=[103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002821], quest_states=[2]):
            # 2nd Quest
            return Q1_퇴장(self.ctx)


class Q1_퇴장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[101])


initial_state = 퀘스트조건01
