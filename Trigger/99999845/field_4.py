""" trigger/99999845/field_4.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000319], state=2)
        self.set_interact_object(trigger_ids=[12000320], state=2)
        self.set_interact_object(trigger_ids=[12000321], state=2)
        # self.set_visible_breakable_object(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])
        # self.set_visible_breakable_object(trigger_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
        # self.set_visible_breakable_object(trigger_ids=[1021,1022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block') == 1:
            self.set_user_value(trigger_id=900005, key='Block', value=0)
            return Block_1(self.ctx)
        if self.user_value(key='Block') == 2:
            self.set_user_value(trigger_id=900005, key='Block', value=0)
            return Block_2(self.ctx)
        if self.user_value(key='Block') == 3:
            self.set_user_value(trigger_id=900005, key='Block', value=0)
            return Block_3(self.ctx)


class Block_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1114]):
            self.set_visible_breakable_object(trigger_ids=[1019], visible=True)
            self.set_interact_object(trigger_ids=[12000319], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            return CableOn_19(self.ctx)


class Block_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1115]):
            self.set_visible_breakable_object(trigger_ids=[1020], visible=True)
            self.set_interact_object(trigger_ids=[12000320], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            return CableOn_20(self.ctx)


class Block_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1116]):
            self.set_visible_breakable_object(trigger_ids=[1021], visible=True)
            self.set_interact_object(trigger_ids=[12000321], state=1)
            self.spawn_monster(spawn_ids=[1117], auto_target=False)
            return CableOn_21(self.ctx)


class CableOn_19(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000319], state=0):
            self.set_interact_object(trigger_ids=[12000319], state=2)
            self.move_user_to_pos(pos=Vector3(1974.56885,372.1966,289))
            return CableDelay_19(self.ctx)


class CableOn_20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000320], state=0):
            self.set_interact_object(trigger_ids=[12000320], state=2)
            self.move_user_to_pos(pos=Vector3(3971.3916,-4325.10742,1492))
            return CableDelay_20(self.ctx)


class CableOn_21(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000321], state=0):
            self.set_interact_object(trigger_ids=[12000321], state=2)
            self.move_user_to_pos(pos=Vector3(3528.33643,2824.1394,2528))
            return CableDelay_21(self.ctx)


class CableDelay_19(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1019], enable=True)
            return CableOff_19(self.ctx)


class CableDelay_20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1020], enable=True)
            return CableOff_20(self.ctx)


class CableDelay_21(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1021], enable=True)
            return CableOff_21(self.ctx)


class CableOff_19(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(6675,75,1650))
            self.set_user_value(trigger_id=900006, key='Block', value=1)
            return End_04(self.ctx)


class CableOff_20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(6675,-1125,1650))
            self.set_user_value(trigger_id=900006, key='Block', value=1)
            return End_04(self.ctx)


class CableOff_21(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(6675,1275,1650))
            self.set_user_value(trigger_id=900006, key='Block', value=1)
            return End_04(self.ctx)


class End_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # self.set_visible_breakable_object(trigger_ids=[1019])
            # self.set_visible_breakable_object(trigger_ids=[1020])
            # self.set_visible_breakable_object(trigger_ids=[1021])
            return 대기(self.ctx)


initial_state = 대기
