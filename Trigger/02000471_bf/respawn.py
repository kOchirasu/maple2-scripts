""" trigger/02000471_bf/respawn.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 1:
            return respawn_timer1(self.ctx)


class respawn_timer1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='respawntimer1', seconds=120, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 2:
            return end(self.ctx)
        if self.time_expired(timer_id='respawntimer1'):
            return respawn1(self.ctx)


class respawn1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='respawntimer1')
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 2:
            return end(self.ctx)
        if not self.monster_dead(spawn_ids=[1999]):
            return respawn_timer2(self.ctx)


class respawn_timer2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='respawntimer2', seconds=120, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 2:
            return end(self.ctx)
        if self.time_expired(timer_id='respawntimer2'):
            return respawn2(self.ctx)


class respawn2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='respawntimer2')
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 2:
            return end(self.ctx)
        if not self.monster_dead(spawn_ids=[1999]):
            return respawn_timer3(self.ctx)


class respawn_timer3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='respawntimer3', seconds=120, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 2:
            return end(self.ctx)
        if self.time_expired(timer_id='respawntimer3'):
            return respawn3(self.ctx)


class respawn3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='respawntimer3')
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 2:
            return end(self.ctx)
        if not self.monster_dead(spawn_ids=[1999]):
            return respawn_timer4(self.ctx)


class respawn_timer4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='respawntimer4', seconds=120, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 2:
            return end(self.ctx)
        if self.time_expired(timer_id='respawntimer4'):
            return respawn4(self.ctx)


class respawn4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='respawntimer4')
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 2:
            return end(self.ctx)
        if not self.monster_dead(spawn_ids=[1999]):
            return respawn_timer5(self.ctx)


class respawn_timer5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='respawntimer5', seconds=120, auto_remove=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 2:
            return end(self.ctx)
        if self.time_expired(timer_id='respawntimer5'):
            return respawn5(self.ctx)


class respawn5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='respawntimer5')
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
