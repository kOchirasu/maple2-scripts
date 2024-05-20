""" trigger/52000070_qd/trap01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000]) # SlidingBoard
        self.set_visible_breakable_object(trigger_ids=[4000]) # SlidingBoard
        self.set_mesh(trigger_ids=[3100]) # WallforMinimap
        self.set_mesh(trigger_ids=[4100]) # BoardOpened
        self.set_mesh(trigger_ids=[4200], visible=True) # BoardClosed
        self.set_actor(trigger_id=3000, visible=True, initial_sequence='Closed') # Door
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[6000]) # LargeGear_SlidingBoard
        self.set_effect(trigger_ids=[6100]) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002677], quest_states=[1]):
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCEnter01(self.ctx)


class PCEnter01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCEnter02(self.ctx)


class PCEnter02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)
        self.set_mesh(trigger_ids=[4200], start_delay=100, fade=3.0) # BoardClosed
        self.set_breakable(trigger_ids=[4000], enable=True) # SlidingBoard
        self.set_visible_breakable_object(trigger_ids=[4000], visible=True) # SlidingBoard
        self.set_effect(trigger_ids=[6000], visible=True) # LargeGear_SlidingBoard

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BoardSlide01(self.ctx)


class BoardSlide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3000, visible=True, initial_sequence='Opened') # Door
        # soundeffect 추가
        self.set_effect(trigger_ids=[6100], visible=True) # DoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BoardSlide02(self.ctx)


class BoardSlide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4100], visible=True, start_delay=800, fade=3.0) # BoardOpened

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EnemyNpcWalkIn01(self.ctx)


class EnemyNpcWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000]) # LargeGear_SlidingBoard
        self.set_breakable(trigger_ids=[4000]) # SlidingBoard
        self.set_visible_breakable_object(trigger_ids=[4000]) # SlidingBoard
        self.move_user_path(patrol_name='MS2PatrolData_1000')
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EnemyNpcWalkIn02(self.ctx)


class EnemyNpcWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=602)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EnemyNpcWalkIn03(self.ctx)


class EnemyNpcWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EnemyNpcWalkIn04(self.ctx)


class EnemyNpcWalkIn04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_104')
        self.select_camera(trigger_id=603)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EnemyNpcTalk01(self.ctx)


class EnemyNpcTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001963, script='$52000070_QD__TRAP01__0$', time=5) # 카트반의 첩자
        self.set_skip(state=EnemyNpcTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EnemyNpcTalk01Skip(self.ctx)


class EnemyNpcTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return EnemyNpcTalk02(self.ctx)


class EnemyNpcTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001963, script='$52000070_QD__TRAP01__1$', time=5) # 카트반의 첩자
        self.set_skip(state=EnemyNpcTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EnemyNpcTalk02Skip(self.ctx)


class EnemyNpcTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return EnemyMobChange01(self.ctx)


class EnemyMobChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=1.0)
        self.destroy_monster(spawn_ids=[101,102,103,104])
        self.spawn_monster(spawn_ids=[901,902,903,904], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903,904]):
            return BattleEnd01(self.ctx)


class BattleEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCPositionFix01(self.ctx)


class PCPositionFix01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=604)
        self.move_user(map_id=52000070, portal_id=10, box_id=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCPositionFix02(self.ctx)


class PCPositionFix02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FriendNpcWalkIn01(self.ctx)


class FriendNpcWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201,202,203,204], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_202')
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_203')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FriendNpcWalkIn02(self.ctx)


class FriendNpcWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1001')
        self.select_camera(trigger_id=605)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FriendNpcTalk01(self.ctx)


class FriendNpcTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001964, script='$52000070_QD__TRAP01__2$', time=4) # 험플스 대원
        self.set_skip(state=FriendNpcTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FriendNpcTalk01Skip(self.ctx)


class FriendNpcTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return FriendNpcTalk02(self.ctx)


class FriendNpcTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        self.set_dialogue(type=2, spawn_id=11001964, script='$52000070_QD__TRAP01__3$', time=4) # 험플스 대원
        self.set_skip(state=FriendNpcTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FriendNpcTalk02Skip(self.ctx)


class FriendNpcTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return WayOpen01(self.ctx)


class WayOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_211')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_212')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return WayOpen02(self.ctx)


class WayOpen02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_213')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_214')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return WayOpen03(self.ctx)


class WayOpen03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=201, script='$52000070_QD__TRAP01__4$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return QuestCom(self.ctx)


class QuestCom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9900, type='trigger', achieve='remnantssweeping')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002677], quest_states=[2]):
            return MoveToComplete(self.ctx)


class MoveToComplete(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.move_user(map_id=2000208, portal_id=1)


initial_state = Wait
