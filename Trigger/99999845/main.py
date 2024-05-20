""" trigger/99999845/main.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000301], state=2)
        self.set_interact_object(trigger_ids=[12000302], state=2)
        self.set_interact_object(trigger_ids=[12000303], state=2)
        self.set_interact_object(trigger_ids=[12000304], state=2)
        self.set_interact_object(trigger_ids=[12000305], state=2)
        self.set_interact_object(trigger_ids=[12000306], state=2)
        self.set_interact_object(trigger_ids=[12000307], state=2)
        self.set_interact_object(trigger_ids=[12000308], state=2)
        self.set_interact_object(trigger_ids=[12000309], state=2)
        self.set_interact_object(trigger_ids=[12000310], state=2)
        self.set_interact_object(trigger_ids=[12000311], state=2)
        self.set_interact_object(trigger_ids=[12000312], state=2)
        self.set_interact_object(trigger_ids=[12000313], state=2)
        self.set_interact_object(trigger_ids=[12000314], state=2)
        self.set_interact_object(trigger_ids=[12000315], state=2)
        self.set_interact_object(trigger_ids=[12000316], state=2)
        self.set_interact_object(trigger_ids=[12000317], state=2)
        self.set_interact_object(trigger_ids=[12000318], state=2)
        self.set_interact_object(trigger_ids=[12000319], state=2)
        self.set_interact_object(trigger_ids=[12000320], state=2)
        self.set_interact_object(trigger_ids=[12000321], state=2)
        self.set_interact_object(trigger_ids=[12000322], state=2)
        self.set_mesh(trigger_ids=[1001], visible=True)
        self.set_mesh(trigger_ids=[1002], visible=True)
        self.set_mesh(trigger_ids=[1003], visible=True)
        self.set_mesh(trigger_ids=[1004], visible=True)
        self.set_mesh(trigger_ids=[1005], visible=True)
        self.set_mesh(trigger_ids=[1006], visible=True)
        self.set_mesh(trigger_ids=[2001], visible=True)
        self.set_mesh(trigger_ids=[2002], visible=True)
        self.set_mesh(trigger_ids=[2003], visible=True)
        self.set_mesh(trigger_ids=[2004], visible=True)
        self.set_mesh(trigger_ids=[2005], visible=True)
        self.set_mesh(trigger_ids=[2006], visible=True)
        self.set_mesh(trigger_ids=[2007], visible=True)
        self.set_mesh(trigger_ids=[2008], visible=True)
        self.set_mesh(trigger_ids=[3001], visible=True)
        self.set_mesh(trigger_ids=[3002], visible=True)
        self.set_mesh(trigger_ids=[3003], visible=True)
        self.set_mesh(trigger_ids=[3004], visible=True)
        self.set_mesh(trigger_ids=[3005], visible=True)
        self.set_mesh(trigger_ids=[3006], visible=True)
        self.set_visible_breakable_object(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010])
        self.set_visible_breakable_object(trigger_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020])
        self.set_visible_breakable_object(trigger_ids=[1021,1022])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[900]):
            # self.spawn_monster(spawn_ids=[1001], auto_target=False)
            # self.spawn_monster(spawn_ids=[1002], auto_target=False)
            return LineStart(self.ctx)


class LineStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1101], auto_target=False)
        self.spawn_monster(spawn_ids=[1102], auto_target=False)
        self.spawn_monster(spawn_ids=[1103], auto_target=False)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], auto_target=False)
        self.spawn_monster(spawn_ids=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1101,1103]):
            self.set_mesh(trigger_ids=[1001])
            self.set_mesh(trigger_ids=[1002])
            self.set_mesh(trigger_ids=[1003])
            self.set_mesh(trigger_ids=[1004])
            self.set_mesh(trigger_ids=[1005])
            self.set_mesh(trigger_ids=[1006])
            self.set_mesh(trigger_ids=[2001])
            self.set_mesh(trigger_ids=[2002])
            self.set_mesh(trigger_ids=[2003])
            self.set_mesh(trigger_ids=[2004])
            self.set_mesh(trigger_ids=[2005])
            self.set_mesh(trigger_ids=[2006])
            self.set_mesh(trigger_ids=[2007])
            self.set_mesh(trigger_ids=[2008])
            self.set_mesh(trigger_ids=[3001])
            self.set_mesh(trigger_ids=[3002])
            self.set_mesh(trigger_ids=[3003])
            self.set_mesh(trigger_ids=[3004])
            self.set_mesh(trigger_ids=[3005])
            self.set_mesh(trigger_ids=[3006])
            self.set_visible_breakable_object(trigger_ids=[1001,1002,1003], visible=True)
            self.set_interact_object(trigger_ids=[12000301], state=1)
            self.set_interact_object(trigger_ids=[12000302], state=1)
            self.set_interact_object(trigger_ids=[12000303], state=1)
            self.spawn_monster(spawn_ids=[1104], auto_target=False)
            self.spawn_monster(spawn_ids=[1105], auto_target=False)
            self.spawn_monster(spawn_ids=[1106], auto_target=False)
            return CableOn_01(self.ctx)


class CableOn_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000302], state=0):
            self.set_interact_object(trigger_ids=[12000301], state=2)
            self.set_interact_object(trigger_ids=[12000302], state=2)
            self.set_interact_object(trigger_ids=[12000303], state=2)
            self.move_user_to_pos(pos=Vector3(-15571.11,75.2856445,3600))
            # self.set_mesh(trigger_ids=[2000], visible=True)
            # self.set_mesh(trigger_ids=[2001], visible=True)
            # self.set_mesh(trigger_ids=[2002], visible=True)
            # self.set_mesh(trigger_ids=[2003], visible=True)
            # self.set_mesh(trigger_ids=[2004], visible=True)
            # self.set_mesh(trigger_ids=[2005], visible=True)
            # self.set_mesh(trigger_ids=[2006], visible=True)
            # self.set_mesh(trigger_ids=[2007], visible=True)
            # self.set_mesh(trigger_ids=[2008], visible=True)
            # self.set_mesh(trigger_ids=[2009], visible=True)
            return CableDelay_01_1(self.ctx)
        if self.object_interacted(interact_ids=[12000303], state=0):
            self.set_interact_object(trigger_ids=[12000301], state=2)
            self.set_interact_object(trigger_ids=[12000302], state=2)
            self.set_interact_object(trigger_ids=[12000303], state=2)
            self.move_user_to_pos(pos=Vector3(-15571.11,-1561.813,3600))
            # self.set_mesh(trigger_ids=[3001], visible=True)
            # self.set_mesh(trigger_ids=[3002], visible=True)
            # self.set_mesh(trigger_ids=[3003], visible=True)
            # self.set_mesh(trigger_ids=[3004], visible=True)
            # self.set_mesh(trigger_ids=[3005], visible=True)
            # self.set_mesh(trigger_ids=[3006], visible=True)
            return CableDelay_01_2(self.ctx)
        if self.object_interacted(interact_ids=[12000301], state=0):
            self.set_interact_object(trigger_ids=[12000301], state=2)
            self.set_interact_object(trigger_ids=[12000302], state=2)
            self.set_interact_object(trigger_ids=[12000303], state=2)
            self.move_user_to_pos(pos=Vector3(-15571.11,1730.293,3600))
            # self.set_mesh(trigger_ids=[1001], visible=True)
            # self.set_mesh(trigger_ids=[1002], visible=True)
            # self.set_mesh(trigger_ids=[1003], visible=True)
            # self.set_mesh(trigger_ids=[1004], visible=True)
            # self.set_mesh(trigger_ids=[1005], visible=True)
            # self.set_mesh(trigger_ids=[1006], visible=True)
            return CableDelay_01_3(self.ctx)


class CableDelay_01_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1002], enable=True)
            return CableOff_01(self.ctx)


class CableDelay_01_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1003], enable=True)
            return CableOff_02(self.ctx)


class CableDelay_01_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_breakable(trigger_ids=[1001], enable=True)
            return CableOff_03(self.ctx)


class CableOff_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-13125,75,2550))
            self.set_user_value(trigger_id=900002, key='Block', value=1)
            return End_01(self.ctx)


class CableOff_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-13275,-5025,1650))
            self.set_user_value(trigger_id=900002, key='Block', value=2)
            return End_01(self.ctx)


class CableOff_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            # self.move_user_to_pos(pos=Vector3(-12925,5025,550))
            self.set_user_value(trigger_id=900002, key='Block', value=3)
            return End_01(self.ctx)


class End_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # self.set_visible_breakable_object(trigger_ids=[1001])
            # self.set_visible_breakable_object(trigger_ids=[1002])
            # # <transition state="대기"/>
            self.set_visible_breakable_object(trigger_ids=[1003])
            pass


initial_state = 대기
