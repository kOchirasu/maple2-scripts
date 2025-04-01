""" trigger/02000376_bf/10_patrol.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PatrolStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PatrolStart') == 1:
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcChange01(self.ctx)


class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[100,200])
        self.spawn_monster(spawn_ids=[101,201], auto_target=False) # 스크립트 잡담을 가지고 있는 NPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9301, spawn_ids=[101]):
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9302, spawn_ids=[101]):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_102')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9303, spawn_ids=[101]):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_103')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9304, spawn_ids=[101]):
            return Patrol04(self.ctx)


class Patrol04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_104')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9305, spawn_ids=[101]):
            return Patrol05Air(self.ctx)


class Patrol05Air(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=201, script='$02000376_BF__10_PATROL__0$', time=2) # 준타
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_105')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NpcChange02(self.ctx)


class NpcChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,201])
        self.spawn_monster(spawn_ids=[102,202], auto_target=False) # 연출용
        self.remove_balloon_talk(spawn_id=201)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='PatrolEnd', value=1)


initial_state = Wait
