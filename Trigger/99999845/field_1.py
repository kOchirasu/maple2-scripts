""" trigger/99999845/field_1.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000304], state=2)
        self.set_interact_object(trigger_ids=[12000305], state=2)
        self.set_interact_object(trigger_ids=[12000306], state=2)
        # self.set_visible_breakable_object(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])
        # self.set_visible_breakable_object(trigger_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
        # self.set_visible_breakable_object(trigger_ids=[1021,1022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block') == 1:
            self.set_user_value(trigger_id=900002, key='Block', value=0)
            return Block_1(self.ctx)
        if self.user_value(key='Block') == 2:
            self.set_user_value(trigger_id=900002, key='Block', value=0)
            return Block_2(self.ctx)
        if self.user_value(key='Block') == 3:
            self.set_user_value(trigger_id=900002, key='Block', value=0)
            return Block_3(self.ctx)


class Block_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1104]):
            self.set_visible_breakable_object(trigger_ids=[1004], visible=True)
            self.set_interact_object(trigger_ids=[12000304], state=1)
            self.spawn_monster(spawn_ids=[1107], auto_target=False)
            self.spawn_monster(spawn_ids=[1108], auto_target=False)
            self.spawn_monster(spawn_ids=[1109], auto_target=False)
            return CableOn_04(self.ctx)


class Block_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1105]):
            self.set_visible_breakable_object(trigger_ids=[1005], visible=True)
            self.set_interact_object(trigger_ids=[12000305], state=1)
            self.spawn_monster(spawn_ids=[1107], auto_target=False)
            self.spawn_monster(spawn_ids=[1108], auto_target=False)
            self.spawn_monster(spawn_ids=[1109], auto_target=False)
            return CableOn_05(self.ctx)


class Block_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1106]):
            self.set_visible_breakable_object(trigger_ids=[1006], visible=True)
            self.set_interact_object(trigger_ids=[12000306], state=1)
            self.spawn_monster(spawn_ids=[1107], auto_target=False)
            self.spawn_monster(spawn_ids=[1108], auto_target=False)
            self.spawn_monster(spawn_ids=[1109], auto_target=False)
            return CableOn_06(self.ctx)


class CableOn_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000304], state=0):
            self.set_interact_object(trigger_ids=[12000304], state=2)
            self.move_user_to_pos(pos=Vector3(-12687.7676,-1071.39685,2530))
            return CableDelay_04(self.ctx)


class CableOn_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000305], state=0):
            self.set_interact_object(trigger_ids=[12000305], state=2)
            self.move_user_to_pos(pos=Vector3(-11673.0137,-6377.65674,1639))
            return CableDelay_05(self.ctx)


class CableOn_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000306], state=0):
            self.set_interact_object(trigger_ids=[12000306], state=2)
            self.move_user_to_pos(pos=Vector3(-11221.6494,6215.7334,433))
            return CableDelay_06(self.ctx)


class CableDelay_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1004], enable=True)
            return CableOff_04(self.ctx)


class CableDelay_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1005], enable=True)
            return CableOff_05(self.ctx)


class CableDelay_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1006], enable=True)
            return CableOff_06(self.ctx)


class CableOff_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-9825,-1425,1350))
            self.set_user_value(trigger_id=900003, key='Block', value=1)
            return End_01(self.ctx)


class CableOff_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-9375,-9225,150))
            self.set_user_value(trigger_id=900003, key='Block', value=2)
            return End_01(self.ctx)


class CableOff_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-8475,7275,2700))
            self.set_user_value(trigger_id=900003, key='Block', value=3)
            return End_01(self.ctx)


class End_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # self.set_visible_breakable_object(trigger_ids=[1004])
            # self.set_visible_breakable_object(trigger_ids=[1005])
            # self.set_visible_breakable_object(trigger_ids=[1006])
            return 대기(self.ctx)


initial_state = 대기
