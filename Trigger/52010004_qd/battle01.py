""" trigger/52010004_qd/battle01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[10000])
        self.set_agent(trigger_ids=[10001])
        self.set_agent(trigger_ids=[10002])
        self.set_agent(trigger_ids=[10003])
        self.spawn_monster(spawn_ids=[101], auto_target=False) # Quest
        self.set_mesh(trigger_ids=[7000,7001,7002,7003]) # BattleZone

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002800], quest_states=[2]):
            return 둔바교체01(self.ctx)


class 둔바교체01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_mesh(trigger_ids=[7000,7001,7002,7003], visible=True) # BattleZone
        self.destroy_monster(spawn_ids=[101]) # Quest
        self.spawn_monster(spawn_ids=[102], auto_target=False) # Act

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 둔바연출준비01(self.ctx)


class 둔바연출준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.select_camera(trigger_id=601)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 둔바대화01(self.ctx)


class 둔바대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=2)
        self.set_dialogue(type=2, spawn_id=11001217, script='$52010004_QD__BATTLE01__0$', time=2)
        self.set_skip(state=둔바대화02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 둔바대화02대기(self.ctx)


class 둔바대화02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 둔바대화02(self.ctx)


class 둔바대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=2)
        self.set_dialogue(type=2, spawn_id=11001217, script='$52010004_QD__BATTLE01__1$', time=2)
        self.set_skip(state=둔바대화03대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 둔바대화03대기(self.ctx)


class 둔바대화03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 둔바대화03(self.ctx)


class 둔바대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=2)
        self.set_dialogue(type=2, spawn_id=11001217, script='$52010004_QD__BATTLE01__2$', time=2)
        self.set_skip(state=둔바연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 둔바연출종료01(self.ctx)


class 둔바연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_timer(timer_id='13', seconds=1)
        self.select_camera(trigger_id=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='13'):
            return 전투준비01(self.ctx)


class 전투준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=1)
        self.set_agent(trigger_ids=[10000], visible=True)
        self.set_agent(trigger_ids=[10001], visible=True)
        self.set_agent(trigger_ids=[10002], visible=True)
        self.set_agent(trigger_ids=[10003], visible=True)
        self.destroy_monster(spawn_ids=[102]) # Act
        self.spawn_monster(spawn_ids=[201]) # Monster

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 전투중01(self.ctx)


class 전투중01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010004, portal_id=50, box_id=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201]):
            return 둔바교체대기02(self.ctx)


class 둔바교체대기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[7000,7001,7002,7003]) # BattleZone
        self.set_timer(timer_id='30', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 둔바교체02(self.ctx)


class 둔바교체02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201]) # Monster
        self.spawn_monster(spawn_ids=[101], auto_target=False) # Quest


initial_state = 대기
