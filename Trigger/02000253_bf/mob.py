""" trigger/02000253_bf/mob.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002527)
        self.hide_guide_summary(entity_id=20002528)
        self.hide_guide_summary(entity_id=20002529)
        self.hide_guide_summary(entity_id=20002530)
        self.hide_guide_summary(entity_id=20002531)
        self.hide_guide_summary(entity_id=20002532)
        self.set_ladder(trigger_ids=[1701])
        self.set_ladder(trigger_ids=[1702])
        self.set_ladder(trigger_ids=[1703])
        self.set_ladder(trigger_ids=[1704])
        self.set_interact_object(trigger_ids=[13000005], state=2)
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=906) >= 1:
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 몹1(self.ctx)


class 몹1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002527, text_id=20002527)
        self.set_timer(timer_id='1', seconds=15)
        # self.spawn_monster(spawn_ids=[4001])
        # self.spawn_monster(spawn_ids=[4002])
        # self.spawn_monster(spawn_ids=[4003])
        # self.spawn_monster(spawn_ids=[4004])
        # self.spawn_monster(spawn_ids=[4005])
        # self.spawn_monster(spawn_ids=[4006])
        # self.spawn_monster(spawn_ids=[4007])
        # self.spawn_monster(spawn_ids=[4008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 몹2(self.ctx)
        if self.object_interacted(interact_ids=[10001050], state=0):
            return 몹2(self.ctx)
        if self.object_interacted(interact_ids=[10001051], state=0):
            return 몹2(self.ctx)
        if self.object_interacted(interact_ids=[10001052], state=0):
            return 몹2(self.ctx)
        """
        if self.monster_dead(spawn_ids=[4001,4003,4005,4007]):
            return 몹2(self.ctx)
        """
        if self.object_interacted(interact_ids=[10001053], state=0):
            return 몹2(self.ctx)


class 몹2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002528, text_id=20002528)
        self.set_timer(timer_id='1', seconds=20)
        # self.spawn_monster(spawn_ids=[4001])
        self.spawn_monster(spawn_ids=[4002])
        # self.spawn_monster(spawn_ids=[4003])
        self.spawn_monster(spawn_ids=[4004])
        # self.spawn_monster(spawn_ids=[4005])
        # self.spawn_monster(spawn_ids=[4006])
        # self.spawn_monster(spawn_ids=[4007])
        self.spawn_monster(spawn_ids=[4008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4002,4004,4006,4008]):
            return 몹3(self.ctx)


class 몹3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002529, text_id=20002529)
        self.set_timer(timer_id='1', seconds=20)
        self.spawn_monster(spawn_ids=[4001])
        # self.spawn_monster(spawn_ids=[4002])
        self.spawn_monster(spawn_ids=[4003])
        # self.spawn_monster(spawn_ids=[4004])
        # self.spawn_monster(spawn_ids=[4005])
        # self.spawn_monster(spawn_ids=[4006])
        self.spawn_monster(spawn_ids=[4007])
        # self.spawn_monster(spawn_ids=[4008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4001,4003,4005,4007]):
            return 몹4(self.ctx)


class 몹4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002530, text_id=20002530)
        self.set_timer(timer_id='1', seconds=20)
        self.spawn_monster(spawn_ids=[4001])
        self.spawn_monster(spawn_ids=[4002])
        self.spawn_monster(spawn_ids=[4003])
        self.spawn_monster(spawn_ids=[4004])
        # self.spawn_monster(spawn_ids=[4005])
        # self.spawn_monster(spawn_ids=[4006])
        # self.spawn_monster(spawn_ids=[4007])
        # self.spawn_monster(spawn_ids=[4008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4001,4002,4003,4005,4006]):
            return 몹5(self.ctx)


class 몹5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002531, text_id=20002531)
        self.set_timer(timer_id='1', seconds=20)
        # self.spawn_monster(spawn_ids=[4001])
        # self.spawn_monster(spawn_ids=[4002])
        # self.spawn_monster(spawn_ids=[4003])
        # self.spawn_monster(spawn_ids=[4004])
        self.spawn_monster(spawn_ids=[4005])
        self.spawn_monster(spawn_ids=[4006])
        self.spawn_monster(spawn_ids=[4007])
        self.spawn_monster(spawn_ids=[4008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4003,4004,4005,4006,4007,4008]):
            return 몹6(self.ctx)


class 몹6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002532, text_id=20002532)
        self.set_timer(timer_id='1', seconds=20)
        self.spawn_monster(spawn_ids=[4001])
        self.spawn_monster(spawn_ids=[4002])
        self.spawn_monster(spawn_ids=[4003])
        self.spawn_monster(spawn_ids=[4004])
        self.spawn_monster(spawn_ids=[4005])
        # self.spawn_monster(spawn_ids=[4006])
        # self.spawn_monster(spawn_ids=[4007])
        # self.spawn_monster(spawn_ids=[4008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4001,4002,4003,4004,4005,4006]):
            return 몹10(self.ctx)


class 몹7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002533, text_id=20002533)
        self.set_timer(timer_id='1', seconds=20)
        self.spawn_monster(spawn_ids=[4001])
        self.spawn_monster(spawn_ids=[4002])
        self.spawn_monster(spawn_ids=[4003])
        self.spawn_monster(spawn_ids=[4004])
        self.spawn_monster(spawn_ids=[4005])
        self.spawn_monster(spawn_ids=[4006])
        self.spawn_monster(spawn_ids=[4007])
        self.spawn_monster(spawn_ids=[4008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 몹8(self.ctx)


class 몹8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=20)
        self.spawn_monster(spawn_ids=[4001])
        self.spawn_monster(spawn_ids=[4002])
        self.spawn_monster(spawn_ids=[4003])
        self.spawn_monster(spawn_ids=[4004])
        self.spawn_monster(spawn_ids=[4005])
        self.spawn_monster(spawn_ids=[4006])
        self.spawn_monster(spawn_ids=[4007])
        self.spawn_monster(spawn_ids=[4008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 몹9(self.ctx)


class 몹9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=20)
        self.spawn_monster(spawn_ids=[4001])
        self.spawn_monster(spawn_ids=[4002])
        self.spawn_monster(spawn_ids=[4003])
        self.spawn_monster(spawn_ids=[4004])
        self.spawn_monster(spawn_ids=[4005])
        self.spawn_monster(spawn_ids=[4006])
        self.spawn_monster(spawn_ids=[4007])
        self.spawn_monster(spawn_ids=[4008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 몹10(self.ctx)


class 몹10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002533, text_id=20002533)
        self.set_timer(timer_id='1', seconds=20)
        self.spawn_monster(spawn_ids=[4009])
        self.spawn_monster(spawn_ids=[4010])
        self.spawn_monster(spawn_ids=[4011])
        self.spawn_monster(spawn_ids=[4012])
        self.spawn_monster(spawn_ids=[4013])
        self.spawn_monster(spawn_ids=[4014])
        self.spawn_monster(spawn_ids=[4015])
        self.spawn_monster(spawn_ids=[4016])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4009,4010,4011,4012,4013,4014,4015,4016]):
            return 열려(self.ctx)


class 열려(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002524, text_id=20002524)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        # self.set_interact_object(trigger_ids=[13000005], state=1)
        # self.create_item(spawn_ids=[9001], trigger_id=999)
        self.set_ladder(trigger_ids=[1701], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1702], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1703], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1704], visible=True, enable=True, fade=2)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002524)


initial_state = 대기
