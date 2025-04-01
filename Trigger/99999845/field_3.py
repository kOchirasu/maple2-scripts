""" trigger/99999845/field_3.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000313], state=2)
        self.set_interact_object(trigger_ids=[12000314], state=2)
        self.set_interact_object(trigger_ids=[12000315], state=2)
        self.set_interact_object(trigger_ids=[12000316], state=2)
        self.set_interact_object(trigger_ids=[12000317], state=2)
        self.set_interact_object(trigger_ids=[12000318], state=2)
        # self.set_visible_breakable_object(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])
        # self.set_visible_breakable_object(trigger_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
        # self.set_visible_breakable_object(trigger_ids=[1021,1022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block') == 1:
            self.set_user_value(trigger_id=900004, key='Block', value=0)
            return Block_1(self.ctx)
        if self.user_value(key='Block') == 2:
            self.set_user_value(trigger_id=900004, key='Block', value=0)
            return Block_2(self.ctx)
        if self.user_value(key='Block') == 3:
            self.set_user_value(trigger_id=900004, key='Block', value=0)
            return Block_3(self.ctx)
        if self.user_value(key='Block') == 4:
            self.set_user_value(trigger_id=900004, key='Block', value=0)
            return Block_4(self.ctx)


class Block_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1110]):
            self.set_visible_breakable_object(trigger_ids=[1013], visible=True)
            self.set_interact_object(trigger_ids=[12000313], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            return CableOn_13(self.ctx)


class Block_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1111]):
            self.set_visible_breakable_object(trigger_ids=[1014], visible=True)
            self.set_visible_breakable_object(trigger_ids=[1015], visible=True)
            self.set_interact_object(trigger_ids=[12000314], state=1)
            self.set_interact_object(trigger_ids=[12000315], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            return CableOn_14_15(self.ctx)


class Block_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1112]):
            self.set_visible_breakable_object(trigger_ids=[1016], visible=True)
            self.set_visible_breakable_object(trigger_ids=[1017], visible=True)
            self.set_interact_object(trigger_ids=[12000316], state=1)
            self.set_interact_object(trigger_ids=[12000317], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            return CableOn_16_17(self.ctx)


class Block_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1113]):
            self.set_visible_breakable_object(trigger_ids=[1018], visible=True)
            self.set_interact_object(trigger_ids=[12000318], state=1)
            self.spawn_monster(spawn_ids=[1114], auto_target=False)
            self.spawn_monster(spawn_ids=[1115], auto_target=False)
            self.spawn_monster(spawn_ids=[1116], auto_target=False)
            return CableOn_18(self.ctx)


class CableOn_13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000313], state=0):
            self.set_interact_object(trigger_ids=[12000313], state=2)
            self.move_user_to_pos(pos=Vector3(-2514.072,3816.40259,1500))
            return CableDelay_13(self.ctx)


class CableOn_14_15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000314], state=0):
            self.set_interact_object(trigger_ids=[12000314], state=2)
            self.set_interact_object(trigger_ids=[12000315], state=2)
            self.move_user_to_pos(pos=Vector3(-3524.431,-1479.53162,137))
            return CableDelay_14(self.ctx)
        if self.object_interacted(interact_ids=[12000315], state=0):
            self.set_interact_object(trigger_ids=[12000314], state=2)
            self.set_interact_object(trigger_ids=[12000315], state=2)
            self.move_user_to_pos(pos=Vector3(-1478.22412,-4127.897,137))
            return CableDelay_15(self.ctx)


class CableOn_16_17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000316], state=0):
            self.set_interact_object(trigger_ids=[12000316], state=2)
            self.set_interact_object(trigger_ids=[12000317], state=2)
            self.move_user_to_pos(pos=Vector3(-848.5522,-7473.63,2690))
            return CableDelay_16(self.ctx)
        if self.object_interacted(interact_ids=[12000317], state=0):
            self.set_interact_object(trigger_ids=[12000316], state=2)
            self.set_interact_object(trigger_ids=[12000317], state=2)
            self.move_user_to_pos(pos=Vector3(1372.17615,-8612.513,2690))
            return CableDelay_17(self.ctx)


class CableOn_18(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000318], state=0):
            self.set_interact_object(trigger_ids=[12000318], state=2)
            self.move_user_to_pos(pos=Vector3(-840.132935,6427.83936,1640))
            return CableDelay_18(self.ctx)


class CableDelay_13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1013], enable=True)
            return CableOff_13(self.ctx)


class CableDelay_14(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1014], enable=True)
            return CableOff_14(self.ctx)


class CableDelay_15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1015], enable=True)
            return CableOff_15(self.ctx)


class CableDelay_16(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1016], enable=True)
            return CableOff_16(self.ctx)


class CableDelay_17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1017], enable=True)
            return CableOff_17(self.ctx)


class CableDelay_18(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1018], enable=True)
            return CableOff_18(self.ctx)


class CableOff_13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(525,1425,300))
            self.set_user_value(trigger_id=900005, key='Block', value=1)
            return End_03(self.ctx)


class CableOff_14(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-375,-75,300))
            self.set_user_value(trigger_id=900005, key='Block', value=1)
            return End_03(self.ctx)


class CableOff_15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(3375,-5475,1500))
            self.set_user_value(trigger_id=900005, key='Block', value=2)
            return End_03(self.ctx)


class CableOff_16(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(525,-1575,300))
            self.set_user_value(trigger_id=900005, key='Block', value=1)
            return End_03(self.ctx)


class CableOff_17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(3975,-5925,1500))
            self.set_user_value(trigger_id=900005, key='Block', value=2)
            return End_03(self.ctx)


class CableOff_18(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(2475,4575,2550))
            self.set_user_value(trigger_id=900005, key='Block', value=3)
            return End_03(self.ctx)


class End_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # self.set_visible_breakable_object(trigger_ids=[1013])
            # self.set_visible_breakable_object(trigger_ids=[1014])
            # self.set_visible_breakable_object(trigger_ids=[1015])
            # self.set_visible_breakable_object(trigger_ids=[1016])
            # self.set_visible_breakable_object(trigger_ids=[1017])
            # self.set_visible_breakable_object(trigger_ids=[1018])
            return 대기(self.ctx)


initial_state = 대기
