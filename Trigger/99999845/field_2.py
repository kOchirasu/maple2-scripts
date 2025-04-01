""" trigger/99999845/field_2.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000307], state=2)
        self.set_interact_object(trigger_ids=[12000308], state=2)
        self.set_interact_object(trigger_ids=[12000309], state=2)
        self.set_interact_object(trigger_ids=[12000310], state=2)
        self.set_interact_object(trigger_ids=[12000311], state=2)
        self.set_interact_object(trigger_ids=[12000312], state=2)
        # self.set_visible_breakable_object(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])
        # self.set_visible_breakable_object(trigger_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
        # self.set_visible_breakable_object(trigger_ids=[1021,1022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block') == 1:
            self.set_user_value(trigger_id=900003, key='Block', value=0)
            return Block_1(self.ctx)
        if self.user_value(key='Block') == 2:
            self.set_user_value(trigger_id=900003, key='Block', value=0)
            return Block_2(self.ctx)
        if self.user_value(key='Block') == 3:
            self.set_user_value(trigger_id=900003, key='Block', value=0)
            return Block_3(self.ctx)


class Block_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1107]):
            self.set_visible_breakable_object(trigger_ids=[1007], visible=True)
            self.set_visible_breakable_object(trigger_ids=[1008], visible=True)
            self.set_interact_object(trigger_ids=[12000307], state=1)
            self.set_interact_object(trigger_ids=[12000308], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            return CableOn_07_08(self.ctx)


class Block_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1108]):
            self.set_visible_breakable_object(trigger_ids=[1009], visible=True)
            self.set_visible_breakable_object(trigger_ids=[1010], visible=True)
            self.set_interact_object(trigger_ids=[12000309], state=1)
            self.set_interact_object(trigger_ids=[12000310], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            return CableOn_09_10(self.ctx)


class Block_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1109]):
            self.set_visible_breakable_object(trigger_ids=[1011], visible=True)
            self.set_visible_breakable_object(trigger_ids=[1012], visible=True)
            self.set_interact_object(trigger_ids=[12000311], state=1)
            self.set_interact_object(trigger_ids=[12000312], state=1)
            self.spawn_monster(spawn_ids=[1110], auto_target=False)
            self.spawn_monster(spawn_ids=[1111], auto_target=False)
            self.spawn_monster(spawn_ids=[1112], auto_target=False)
            self.spawn_monster(spawn_ids=[1113], auto_target=False)
            return CableOn_11_12(self.ctx)


class CableOn_07_08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000307], state=0):
            self.set_interact_object(trigger_ids=[12000307], state=2)
            self.set_interact_object(trigger_ids=[12000308], state=2)
            self.move_user_to_pos(pos=Vector3(-8476.297,-3480.99072,1343))
            return CableDelay_07(self.ctx)
        if self.object_interacted(interact_ids=[12000308], state=0):
            self.set_interact_object(trigger_ids=[12000307], state=2)
            self.set_interact_object(trigger_ids=[12000308], state=2)
            self.move_user_to_pos(pos=Vector3(-6726.70264,-377.953552,1343))
            return CableDelay_08(self.ctx)


class CableOn_09_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000309], state=0):
            self.set_interact_object(trigger_ids=[12000309], state=2)
            self.set_interact_object(trigger_ids=[12000310], state=2)
            self.move_user_to_pos(pos=Vector3(-8321.446,-7475.03271,135))
            return CableDelay_09(self.ctx)
        if self.object_interacted(interact_ids=[12000310], state=0):
            self.set_interact_object(trigger_ids=[12000309], state=2)
            self.set_interact_object(trigger_ids=[12000310], state=2)
            self.move_user_to_pos(pos=Vector3(-6576.207,-9063.119,135))
            return CableDelay_10(self.ctx)


class CableOn_11_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000311], state=0):
            self.set_interact_object(trigger_ids=[12000311], state=2)
            self.set_interact_object(trigger_ids=[12000312], state=2)
            self.move_user_to_pos(pos=Vector3(-7723.194,5673.29346,2690))
            return CableDelay_11(self.ctx)
        if self.object_interacted(interact_ids=[12000312], state=0):
            self.set_interact_object(trigger_ids=[12000311], state=2)
            self.set_interact_object(trigger_ids=[12000312], state=2)
            self.move_user_to_pos(pos=Vector3(-6276.41748,8028.68164,2690))
            return CableDelay_12(self.ctx)


class CableDelay_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1007], enable=True)
            return CableOff_07(self.ctx)


class CableDelay_08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1008], enable=True)
            return CableOff_08(self.ctx)


class CableDelay_09(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1009], enable=True)
            return CableOff_09(self.ctx)


class CableDelay_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1010], enable=True)
            return CableOff_10(self.ctx)


class CableDelay_11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1011], enable=True)
            return CableOff_11(self.ctx)


class CableDelay_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1012], enable=True)
            return CableOff_12(self.ctx)


class CableOff_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-5025,-4125,150))
            self.set_user_value(trigger_id=900004, key='Block', value=2)
            return End_02(self.ctx)


class CableOff_08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-4575,3075,1500))
            self.set_user_value(trigger_id=900004, key='Block', value=1)
            return End_02(self.ctx)


class CableOff_09(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-3525,-6075,150))
            self.set_user_value(trigger_id=900004, key='Block', value=2)
            return End_02(self.ctx)


class CableOff_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-1875,-8775,2700))
            self.set_user_value(trigger_id=900004, key='Block', value=3)
            return End_02(self.ctx)


class CableOff_11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-4575,5025,1550))
            self.set_user_value(trigger_id=900004, key='Block', value=1)
            return End_02(self.ctx)


class CableOff_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-2025,8025,1600))
            self.set_user_value(trigger_id=900004, key='Block', value=4)
            return End_02(self.ctx)


class End_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # self.set_visible_breakable_object(trigger_ids=[1007])
            # self.set_visible_breakable_object(trigger_ids=[1008])
            # self.set_visible_breakable_object(trigger_ids=[1009])
            # self.set_visible_breakable_object(trigger_ids=[1010])
            # self.set_visible_breakable_object(trigger_ids=[1011])
            # self.set_visible_breakable_object(trigger_ids=[1012])
            return 대기(self.ctx)


initial_state = 대기
