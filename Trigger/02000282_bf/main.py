""" trigger/02000282_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000424], state=0)
        self.set_interact_object(trigger_ids=[10000425], state=0)
        self.set_interact_object(trigger_ids=[10000426], state=0)
        self.set_interact_object(trigger_ids=[10000433], state=2)
        self.set_interact_object(trigger_ids=[10000434], state=2)
        self.set_interact_object(trigger_ids=[10000435], state=2)
        self.set_ladder(trigger_ids=[341])
        self.set_ladder(trigger_ids=[342])
        self.set_ladder(trigger_ids=[343])
        self.set_ladder(trigger_ids=[351])
        self.set_ladder(trigger_ids=[352])
        self.set_ladder(trigger_ids=[353])
        self.set_ladder(trigger_ids=[361])
        self.set_ladder(trigger_ids=[362])
        self.set_ladder(trigger_ids=[363])
        self.set_portal(portal_id=4)
        self.set_portal(portal_id=5)
        self.set_portal(portal_id=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)
        self.spawn_monster(spawn_ids=[1009], auto_target=False)
        self.spawn_monster(spawn_ids=[1010], auto_target=False)
        self.spawn_monster(spawn_ids=[1011], auto_target=False)
        self.spawn_monster(spawn_ids=[1012], auto_target=False)
        self.spawn_monster(spawn_ids=[1014], auto_target=False)
        self.spawn_monster(spawn_ids=[1015], auto_target=False)
        self.spawn_monster(spawn_ids=[1016], auto_target=False)
        self.spawn_monster(spawn_ids=[1017], auto_target=False)
        self.spawn_monster(spawn_ids=[1018], auto_target=False)
        self.spawn_monster(spawn_ids=[1019], auto_target=False)
        self.spawn_monster(spawn_ids=[1020], auto_target=False)
        self.spawn_monster(spawn_ids=[1021], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return 번생성4(self.ctx)
        if self.random_condition(weight=33.0):
            return 번생성5(self.ctx)
        if self.random_condition(weight=34.0):
            return 번생성6(self.ctx)


class 번생성4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000424], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000424], state=0):
            return 번몬스터4(self.ctx)


class 번몬스터4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2004], auto_target=False)
        self.show_guide_summary(entity_id=20002817, text_id=20002817, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2004]):
            self.show_guide_summary(entity_id=20002812, text_id=20002812, duration=5000)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.set_ladder(trigger_ids=[341], visible=True, enable=True)
            self.set_ladder(trigger_ids=[342], visible=True, enable=True)
            self.set_ladder(trigger_ids=[343], visible=True, enable=True)
            self.set_portal(portal_id=4, enable=True, minimap_visible=True)
            return 소멸대기(self.ctx)


class 번생성5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000425], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000425], state=0):
            return 번몬스터5(self.ctx)


class 번몬스터5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2005], auto_target=False)
        self.show_guide_summary(entity_id=20002817, text_id=20002817, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2005]):
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.show_guide_summary(entity_id=20002812, text_id=20002812, duration=5000)
            self.set_ladder(trigger_ids=[351], visible=True, enable=True)
            self.set_ladder(trigger_ids=[352], visible=True, enable=True)
            self.set_ladder(trigger_ids=[353], visible=True, enable=True)
            self.set_portal(portal_id=5, enable=True, minimap_visible=True)
            return 소멸대기(self.ctx)


class 번생성6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000426], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000426], state=0):
            return 번몬스터6(self.ctx)


class 번몬스터6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2006], auto_target=False)
        self.show_guide_summary(entity_id=20002817, text_id=20002817, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2006]):
            self.show_guide_summary(entity_id=20002812, text_id=20002812, duration=5000)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.set_ladder(trigger_ids=[361], visible=True, enable=True)
            self.set_ladder(trigger_ids=[362], visible=True, enable=True)
            self.set_ladder(trigger_ids=[363], visible=True, enable=True)
            self.set_portal(portal_id=6, enable=True, minimap_visible=True)
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    pass


initial_state = 대기
