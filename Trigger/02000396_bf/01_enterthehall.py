""" trigger/02000396_bf/01_enterthehall.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004]) # DoorOpen
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='Closed') # Upstairs
        self.set_ladder(trigger_ids=[511]) # Ladder_Enter
        self.set_ladder(trigger_ids=[512]) # Ladder_Enter
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006], visible=True) # Invisible_AlwaysOn
        self.set_mesh(trigger_ids=[3007], visible=True) # Invisible_DoorOpen
        self.destroy_monster(spawn_ids=[101,102]) # Npc
        self.destroy_monster(spawn_ids=[901,902,903]) # Mob_Actor
        self.set_agent(trigger_ids=[8006,8007,8008,8009], visible=True)
        self.set_user_value(key='MobClear', value=0)
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BlackeyeApp01(self.ctx)


class BlackeyeApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[101], auto_target=False) # Npc_Actor

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BlackeyeApp02(self.ctx)


class BlackeyeApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')
        self.set_dialogue(type=1, spawn_id=101, script='$02000396_BF__01_ENTERTHEHALL__0$', time=3, arg5=1)
        self.set_skip(state=BlackeyeApp02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return BlackeyeApp02Skip(self.ctx)


class BlackeyeApp02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=101)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return BlackeyeApp03(self.ctx)


class BlackeyeApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000396_BF__01_ENTERTHEHALL__1$', time=3)
        self.set_skip(state=BlackeyeApp03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BlackeyeApp03Skip(self.ctx)


class BlackeyeApp03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=101)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return EnemyApp01(self.ctx)


class EnemyApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601)
        self.set_user_value(trigger_id=2, key='MobSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EnemyApp02(self.ctx)


class EnemyApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[901,902,903], auto_target=False) # Mob_Actor
        self.set_dialogue(type=1, spawn_id=901, script='$02000396_BF__01_ENTERTHEHALL__2$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=902, script='$02000396_BF__01_ENTERTHEHALL__3$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=903, script='$02000396_BF__01_ENTERTHEHALL__4$', time=2, arg5=1)
        self.set_skip(state=EnemyApp03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return EnemyApp03Skip(self.ctx)


class EnemyApp03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=901)
        self.remove_balloon_talk(spawn_id=902)
        self.remove_balloon_talk(spawn_id=903)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return EnemyApp03(self.ctx)


class EnemyApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_104')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BlackeyeAction01(self.ctx)


class BlackeyeAction01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000006, script='$02000396_BF__01_ENTERTHEHALL__5$', time=5) # 블랙아이
        self.set_skip(state=BlackeyeAction01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return BlackeyeAction01Skip(self.ctx)


class BlackeyeAction01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BlackeyeAction02(self.ctx)


class BlackeyeAction02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101]) # Npc_Actor
        self.spawn_monster(spawn_ids=[102], auto_target=False) # Npc_Battle
        self.set_dialogue(type=1, spawn_id=102, script='$02000396_BF__01_ENTERTHEHALL__6$', time=3, arg5=1)
        self.set_ladder(trigger_ids=[511], visible=True, enable=True, fade=1) # Ladder_Enter
        self.set_ladder(trigger_ids=[512], visible=True, enable=True, fade=1) # Ladder_Enter
        self.set_user_value(trigger_id=2, key='MobAttack', value=1)
        self.set_user_value(trigger_id=10, key='TrapOn', value=1)
        self.set_user_value(trigger_id=11, key='TrapOn', value=1)
        self.set_user_value(trigger_id=12, key='TrapOn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return BlackeyeAction03(self.ctx)


class BlackeyeAction03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039601, text_id=20039601, duration=3000) # 가이드 : 레버를 당겨 트랩을 발동시키기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobClear') == 1:
            return MoveToUpstairs01(self.ctx)


class MoveToUpstairs01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8006,8007,8008,8009])
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_102')
        self.set_effect(trigger_ids=[5004], visible=True) # DoorOpen
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='Opened') # Upstairs
        self.set_mesh(trigger_ids=[3007]) # Invisible_DoorOpen
        self.set_user_value(trigger_id=3, key='EnableLadder', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return MoveToUpstairs02(self.ctx)


class MoveToUpstairs02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000006, script='$02000396_BF__01_ENTERTHEHALL__7$', time=5) # 블랙아이
        self.set_skip(state=MoveToUpstairs02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return MoveToUpstairs02Skip(self.ctx)


class MoveToUpstairs02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039602, text_id=20039602, duration=3000) # 가이드 : 계단을 통해 2층으로 올라가기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return FindWayOut01(self.ctx)


class FindWayOut01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui_script(type=BannerType.Text, script='$02000396_BF__01_ENTERTHEHALL__8$', duration=4000, box_ids=['0'])
        self.set_user_value(trigger_id=4, key='SearchStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9100, spawn_ids=[102]):
            return NpcMonologueRandom(self.ctx)


class NpcMonologueRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return NpcMonologue01(self.ctx)
        if self.random_condition(weight=25.0):
            return NpcMonologue02(self.ctx)
        if self.random_condition(weight=25.0):
            return NpcMonologue03(self.ctx)
        if self.random_condition(weight=25.0):
            return NpcMonologue04(self.ctx)


class NpcMonologue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000396_BF__01_ENTERTHEHALL__9$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return NpcMonologueRandom(self.ctx)
        if self.user_value(key='FindWay') == 1:
            return NpcLeave01(self.ctx)


class NpcMonologue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000396_BF__01_ENTERTHEHALL__10$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return NpcMonologueRandom(self.ctx)
        if self.user_value(key='FindWay') == 1:
            return NpcLeave01(self.ctx)


class NpcMonologue03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000396_BF__01_ENTERTHEHALL__11$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return NpcMonologueRandom(self.ctx)
        if self.user_value(key='FindWay') == 1:
            return NpcLeave01(self.ctx)


class NpcMonologue04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000396_BF__01_ENTERTHEHALL__12$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return NpcMonologueRandom(self.ctx)
        if self.user_value(key='FindWay') == 1:
            return NpcLeave01(self.ctx)


class NpcLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=102)
        self.destroy_monster(spawn_ids=[102]) # Npc


initial_state = Wait
