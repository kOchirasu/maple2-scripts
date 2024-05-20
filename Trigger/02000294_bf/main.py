""" trigger/02000294_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, minimap_visible=True)
        self.destroy_monster(spawn_ids=[3001])
        self.destroy_monster(spawn_ids=[3002])
        self.destroy_monster(spawn_ids=[3003])
        self.destroy_monster(spawn_ids=[3004])
        self.destroy_monster(spawn_ids=[3005])
        self.destroy_monster(spawn_ids=[3006])
        self.destroy_monster(spawn_ids=[3007])
        self.destroy_monster(spawn_ids=[3008])
        self.destroy_monster(spawn_ids=[3009])
        self.destroy_monster(spawn_ids=[3010])
        self.destroy_monster(spawn_ids=[3011])
        self.destroy_monster(spawn_ids=[3012])
        self.destroy_monster(spawn_ids=[3013])
        self.destroy_monster(spawn_ids=[3014])
        self.destroy_monster(spawn_ids=[3015])
        self.destroy_monster(spawn_ids=[3016])
        self.destroy_monster(spawn_ids=[3017])
        self.destroy_monster(spawn_ids=[3100]) # Boss
        self.destroy_monster(spawn_ids=[3101])
        self.destroy_monster(spawn_ids=[3102])
        self.destroy_monster(spawn_ids=[3103])
        self.destroy_monster(spawn_ids=[3104])
        self.destroy_monster(spawn_ids=[10000]) # Actor
        self.set_agent(trigger_ids=[133])
        self.set_agent(trigger_ids=[134])
        self.set_agent(trigger_ids=[135])
        self.set_agent(trigger_ids=[136])
        self.set_agent(trigger_ids=[137])
        self.set_agent(trigger_ids=[138])
        self.set_agent(trigger_ids=[139])
        self.set_agent(trigger_ids=[140])
        self.set_agent(trigger_ids=[141])
        self.set_agent(trigger_ids=[142])
        self.set_agent(trigger_ids=[143])
        self.set_agent(trigger_ids=[144])
        self.set_agent(trigger_ids=[145])
        self.set_agent(trigger_ids=[146])
        self.set_agent(trigger_ids=[147])
        self.set_agent(trigger_ids=[148])
        self.set_agent(trigger_ids=[149])
        self.set_agent(trigger_ids=[150])
        self.set_agent(trigger_ids=[151])
        self.set_agent(trigger_ids=[152])
        self.set_agent(trigger_ids=[153])
        self.set_agent(trigger_ids=[154])
        self.set_agent(trigger_ids=[155])
        self.set_agent(trigger_ids=[156])
        self.set_agent(trigger_ids=[157])
        self.set_actor(trigger_id=900, visible=True, initial_sequence='Closed') # Door
        self.set_mesh(trigger_ids=[101,102], visible=True) # ExitFenceBarrier
        self.set_mesh(trigger_ids=[103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132], visible=True) # Brige
        self.set_mesh(trigger_ids=[25000,25001,25002,25003,25004,25005,25006,25007,25008,25009,25010,25011,25012,25013,25014,25015,25016,25017], visible=True) # Fence
        self.set_mesh(trigger_ids=[300], visible=True) # InvisibleEnterBarrier
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314], visible=True) # CubeEnterBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[10000], auto_target=False)
        self.select_camera(trigger_id=600)
        self.set_skip(state=GateOpen01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcMonologue01(self.ctx)


class NpcMonologue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=10000, patrol_name='MS2PatrolData_10000')
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__0$', time=2)
        self.set_skip(state=GateOpen01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcMonologue02(self.ctx)


class NpcMonologue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=10000, patrol_name='MS2PatrolData_10001')
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__1$', time=2)
        self.set_skip(state=GateOpen01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GateOpen01(self.ctx)


class GateOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_actor(trigger_id=900, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[300]) # InvisibleEnterBarrier
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GateOpen02(self.ctx)


class GateOpen02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=10000, patrol_name='MS2PatrolData_10002')
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__2$', time=3)
        self.set_actor(trigger_id=900, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314], start_delay=1000, interval=500, fade=5.0) # CubeEnterBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Battle01(self.ctx)


class Battle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002941, text_id=20002941) # 용광로 괴수를 처치하세요!
        self.spawn_monster(spawn_ids=[3001], auto_target=False)
        self.spawn_monster(spawn_ids=[3002], auto_target=False)
        self.spawn_monster(spawn_ids=[3003], auto_target=False)
        self.spawn_monster(spawn_ids=[3004], auto_target=False)
        self.spawn_monster(spawn_ids=[3005], auto_target=False)
        self.spawn_monster(spawn_ids=[3006], auto_target=False)
        self.spawn_monster(spawn_ids=[3007], auto_target=False)
        self.spawn_monster(spawn_ids=[3008], auto_target=False)
        self.spawn_monster(spawn_ids=[3009], auto_target=False)
        self.spawn_monster(spawn_ids=[3010], auto_target=False)
        self.spawn_monster(spawn_ids=[3011], auto_target=False)
        self.spawn_monster(spawn_ids=[3012], auto_target=False)
        self.spawn_monster(spawn_ids=[3013], auto_target=False)
        self.spawn_monster(spawn_ids=[3014], auto_target=False)
        self.spawn_monster(spawn_ids=[3015], auto_target=False)
        self.spawn_monster(spawn_ids=[3016], auto_target=False)
        self.spawn_monster(spawn_ids=[3017], auto_target=False)
        self.spawn_monster(spawn_ids=[3100], auto_target=False) # Boss

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Battle02(self.ctx)


class Battle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999992, key='Battle_01', value=1)
        self.spawn_monster(spawn_ids=[3101])
        self.spawn_monster(spawn_ids=[3102])
        self.spawn_monster(spawn_ids=[3103])
        self.spawn_monster(spawn_ids=[3104])
        self.hide_guide_summary(entity_id=20002941)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3100]):
            return Battle03(self.ctx)


class Battle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[133], visible=True)
        self.set_agent(trigger_ids=[134], visible=True)
        self.set_agent(trigger_ids=[135], visible=True)
        self.set_agent(trigger_ids=[136], visible=True)
        self.set_agent(trigger_ids=[137], visible=True)
        self.set_agent(trigger_ids=[138], visible=True)
        self.set_agent(trigger_ids=[139], visible=True)
        self.set_agent(trigger_ids=[140], visible=True)
        self.set_agent(trigger_ids=[141], visible=True)
        self.set_agent(trigger_ids=[142], visible=True)
        self.set_agent(trigger_ids=[143], visible=True)
        self.set_agent(trigger_ids=[144], visible=True)
        self.set_agent(trigger_ids=[145], visible=True)
        self.set_agent(trigger_ids=[146], visible=True)
        self.set_agent(trigger_ids=[147], visible=True)
        self.set_agent(trigger_ids=[148], visible=True)
        self.set_agent(trigger_ids=[149], visible=True)
        self.set_agent(trigger_ids=[150], visible=True)
        self.set_agent(trigger_ids=[151], visible=True)
        self.set_agent(trigger_ids=[152], visible=True)
        self.set_agent(trigger_ids=[153], visible=True)
        self.set_agent(trigger_ids=[154], visible=True)
        self.set_agent(trigger_ids=[155], visible=True)
        self.set_agent(trigger_ids=[156], visible=True)
        self.set_agent(trigger_ids=[157], visible=True)
        self.destroy_monster(spawn_ids=[3001])
        self.destroy_monster(spawn_ids=[3002])
        self.destroy_monster(spawn_ids=[3003])
        self.destroy_monster(spawn_ids=[3004])
        self.destroy_monster(spawn_ids=[3005])
        self.destroy_monster(spawn_ids=[3006])
        self.destroy_monster(spawn_ids=[3007])
        self.destroy_monster(spawn_ids=[3008])
        self.destroy_monster(spawn_ids=[3009])
        self.destroy_monster(spawn_ids=[3010])
        self.destroy_monster(spawn_ids=[3011])
        self.destroy_monster(spawn_ids=[3012])
        self.destroy_monster(spawn_ids=[3013])
        self.destroy_monster(spawn_ids=[3014])
        self.destroy_monster(spawn_ids=[3015])
        self.destroy_monster(spawn_ids=[3016])
        self.destroy_monster(spawn_ids=[3017])
        self.destroy_monster(spawn_ids=[3018])
        self.destroy_monster(spawn_ids=[3101])
        self.destroy_monster(spawn_ids=[3102])
        self.destroy_monster(spawn_ids=[3103])
        self.destroy_monster(spawn_ids=[3104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BattleEnd01(self.ctx)


class BattleEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[137])
        self.set_agent(trigger_ids=[138])
        self.set_agent(trigger_ids=[152])
        self.set_agent(trigger_ids=[153])
        self.move_npc(spawn_id=10000, patrol_name='MS2PatrolData_10003')
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__3$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BattleEnd02(self.ctx)


class BattleEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__4$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BattleEnd03(self.ctx)


class BattleEnd03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=10000, patrol_name='MS2PatrolData_10004')
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__5$', time=3)
        self.set_mesh(trigger_ids=[101,102], fade=5.0)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BattleEnd04(self.ctx)


class BattleEnd04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002942, text_id=20002942)
        self.set_dialogue(type=1, spawn_id=10000, script='$02000294_BF__MAIN__6$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002942)
        self.destroy_monster(spawn_ids=[3001])
        self.destroy_monster(spawn_ids=[3002])
        self.destroy_monster(spawn_ids=[3003])
        self.destroy_monster(spawn_ids=[3004])
        self.destroy_monster(spawn_ids=[3005])
        self.destroy_monster(spawn_ids=[3006])
        self.destroy_monster(spawn_ids=[3007])
        self.destroy_monster(spawn_ids=[3008])
        self.destroy_monster(spawn_ids=[3009])
        self.destroy_monster(spawn_ids=[3010])
        self.destroy_monster(spawn_ids=[3011])
        self.destroy_monster(spawn_ids=[3012])
        self.destroy_monster(spawn_ids=[3013])
        self.destroy_monster(spawn_ids=[3014])
        self.destroy_monster(spawn_ids=[3015])
        self.destroy_monster(spawn_ids=[3016])
        self.destroy_monster(spawn_ids=[3017])


initial_state = 대기
