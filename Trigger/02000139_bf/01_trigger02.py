""" trigger/02000139_bf/01_trigger02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[701,702,703,704,705,706,707,708,709,710,711,712])
        self.set_interact_object(trigger_ids=[10000160], state=1)
        self.set_ladder(trigger_ids=[601])
        self.set_ladder(trigger_ids=[602])
        self.set_ladder(trigger_ids=[603])
        self.set_ladder(trigger_ids=[604])
        self.set_ladder(trigger_ids=[605])
        self.set_ladder(trigger_ids=[606])
        self.set_ladder(trigger_ids=[607])
        self.set_ladder(trigger_ids=[608])
        self.set_ladder(trigger_ids=[609])
        self.set_ladder(trigger_ids=[610])
        self.set_ladder(trigger_ids=[611])
        self.set_ladder(trigger_ids=[612])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000160], state=0):
            return 사다리등장(self.ctx)


class 사다리등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[601], visible=True, enable=True)
        self.set_effect(trigger_ids=[701], visible=True)
        self.set_ladder(trigger_ids=[602], visible=True, enable=True)
        self.set_effect(trigger_ids=[702], visible=True)
        self.set_ladder(trigger_ids=[603], visible=True, enable=True)
        self.set_effect(trigger_ids=[703], visible=True)
        self.set_ladder(trigger_ids=[604], visible=True, enable=True)
        self.set_effect(trigger_ids=[704], visible=True)
        self.set_ladder(trigger_ids=[605], visible=True, enable=True)
        self.set_effect(trigger_ids=[705], visible=True)
        self.set_ladder(trigger_ids=[606], visible=True, enable=True)
        self.set_effect(trigger_ids=[706], visible=True)
        self.set_ladder(trigger_ids=[607], visible=True, enable=True)
        self.set_effect(trigger_ids=[707], visible=True)
        self.set_ladder(trigger_ids=[608], visible=True, enable=True)
        self.set_effect(trigger_ids=[708], visible=True)
        self.set_ladder(trigger_ids=[609], visible=True, enable=True)
        self.set_effect(trigger_ids=[709], visible=True)
        self.set_ladder(trigger_ids=[610], visible=True, enable=True)
        self.set_effect(trigger_ids=[710], visible=True)
        self.set_ladder(trigger_ids=[611], visible=True, enable=True)
        self.set_effect(trigger_ids=[711], visible=True)
        self.set_ladder(trigger_ids=[612], visible=True, enable=True)
        self.set_effect(trigger_ids=[713], visible=True)
        self.set_timer(timer_id='4', seconds=18)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 대기(self.ctx)


initial_state = 대기
