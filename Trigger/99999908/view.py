""" trigger/99999908/view.xml """
import trigger_api


# 에디셔널 이펙트를 계속 걸어줌
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return buff_01(self.ctx)


class buff_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=99910221, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return buff_02(self.ctx)


class buff_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=99910221, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return buff_03(self.ctx)


class buff_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=99910221, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return buff_04(self.ctx)


class buff_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=99910221, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return buff_05(self.ctx)


class buff_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120])
        self.spawn_npc_range(range_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120], random_pick_count=3, score=100)
        self.add_buff(box_ids=[701], skill_id=99910221, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return idle(self.ctx)


initial_state = idle
