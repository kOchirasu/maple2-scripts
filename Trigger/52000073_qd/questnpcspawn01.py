""" trigger/52000073_qd/questnpcspawn01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 카트반

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002667], quest_states=[3]): # 조사대원
            return NpcRemove01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002667], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002667], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002666], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002666], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002666], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002665], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002665], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002665], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002664], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002664], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002664], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002663], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002663], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002663], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002662], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002662], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002662], quest_states=[1]):
            return NpcChange01(self.ctx)


class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[201], auto_target=False)


class NpcRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])


initial_state = Wait
