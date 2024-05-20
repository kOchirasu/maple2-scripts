""" trigger/02000296_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[110]) # Enter
        self.set_ladder(trigger_ids=[111]) # Enter
        self.set_ladder(trigger_ids=[112]) # Enter
        self.set_ladder(trigger_ids=[113]) # Enter
        self.destroy_monster(spawn_ids=[5001]) # Mob
        self.destroy_monster(spawn_ids=[5002]) # Mob
        self.destroy_monster(spawn_ids=[5003]) # Mob
        self.destroy_monster(spawn_ids=[5004]) # Mob
        self.destroy_monster(spawn_ids=[5100]) # Boss
        self.destroy_monster(spawn_ids=[5005]) # Blackeye_Actor01
        self.destroy_monster(spawn_ids=[5006]) # Blackeye_Battle
        self.destroy_monster(spawn_ids=[5007]) # Lennon_Battle
        self.destroy_monster(spawn_ids=[5012]) # Blackeye_Actor02
        self.destroy_monster(spawn_ids=[5013]) # Lennon_Actor
        self.set_effect(trigger_ids=[1000], visible=True)
        self.set_effect(trigger_ids=[4000]) # Intro_Chord
        self.set_mesh(trigger_ids=[1001]) # SoulBead
        self.set_mesh(trigger_ids=[1100], visible=True) # SoulBeadBarrier_AlwaysOn
        self.set_mesh(trigger_ids=[1101], visible=True) # EnterBarrier
        self.set_mesh(trigger_ids=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209], visible=True, interval=100, fade=5.0) # ExitBridge
        self.set_portal(portal_id=2, visible=True, minimap_visible=True)
        self.set_agent(trigger_ids=[1300], visible=True)
        self.set_agent(trigger_ids=[1301], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[5007], auto_target=False) # Lennon_Battle
        self.spawn_monster(spawn_ids=[5005], auto_target=False) # Blackeye_Actor01
        self.spawn_monster(spawn_ids=[5001], auto_target=False)
        self.spawn_monster(spawn_ids=[5002], auto_target=False)
        self.spawn_monster(spawn_ids=[5003], auto_target=False)
        self.spawn_monster(spawn_ids=[5004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LoadingDelay02(self.ctx)


class LoadingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=1, spawn_id=5005, script='$02000296_BF__MAIN__0$', time=3)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return LoadingDelay03(self.ctx)


class LoadingDelay03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=1, spawn_id=5005, script='$02000296_BF__MAIN__1$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return MeetLennon01(self.ctx)


# 레논 전투 중
class MeetLennon01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MeetLennon02(self.ctx)


class MeetLennon02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[5005]) # Blackeye_Actor01
        self.spawn_monster(spawn_ids=[5012], auto_target=False) # Blackeye_Actor02
        self.set_dialogue(type=1, spawn_id=5007, script='$02000296_BF__MAIN__2$', time=3) # Lennon_Battle
        self.set_dialogue(type=1, spawn_id=5007, script='$02000296_BF__MAIN__3$', time=3, arg5=3) # Lennon_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return MeetLennon03(self.ctx)


class MeetLennon03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=600, enable=False)
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LennonLeave01(self.ctx)


class LennonLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=5012, patrol_name='MS2PatrolData_5012')
        self.set_dialogue(type=1, spawn_id=5012, script='$02000296_BF__MAIN__4$', time=3, arg5=1) # Blackeye_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return LennonLeave02(self.ctx)


class LennonLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_agent(trigger_ids=[1300])
        self.set_agent(trigger_ids=[1301])
        self.change_monster(from_spawn_id=5012, to_spawn_id=5006) # Blackeye_Battle
        self.change_monster(from_spawn_id=5007, to_spawn_id=5013) # Lennon_Actor
        self.remove_balloon_talk(spawn_id=5012)
        self.remove_balloon_talk(spawn_id=5007)
        self.set_dialogue(type=1, spawn_id=5013, script='$02000296_BF__MAIN__5$', time=4, arg5=1) # Lennon_Actor
        self.move_npc(spawn_id=5013, patrol_name='MS2PatrolData_5009')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return LennonLeave03(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5005]) # Blackeye_Actor01
        self.spawn_monster(spawn_ids=[5012], auto_target=False) # Blackeye_Actor02
        self.change_monster(from_spawn_id=5012, to_spawn_id=5006) # Blackeye_Battle
        self.change_monster(from_spawn_id=5007, to_spawn_id=5013) # Lennon_Actor

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LennonLeave03(self.ctx)


class LennonLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=601, enable=False)
        self.destroy_monster(spawn_ids=[5013]) # Lennon_Actor
        self.set_mesh(trigger_ids=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209], start_delay=500, interval=100, fade=5.0) # ExitBridge
        self.set_mesh(trigger_ids=[1101]) # EnterBarrier
        self.set_ladder(trigger_ids=[110], visible=True, enable=True) # Enter
        self.set_ladder(trigger_ids=[111], visible=True, enable=True) # Enter
        self.set_ladder(trigger_ids=[112], visible=True, enable=True) # Enter
        self.set_ladder(trigger_ids=[113], visible=True, enable=True) # Enter

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReactSoulBead01(self.ctx)


class ReactSoulBead01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[1300], visible=True)
        self.set_agent(trigger_ids=[1301], visible=True)
        self.play_system_sound_in_box(box_ids=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002961, text_id=20002961) # 영혼의 구슬에 속박된 주민들을 구해주세요
        self.set_dialogue(type=1, spawn_id=5006, script='$02000296_BF__MAIN__6$', time=4) # Blackeye_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ReactSoulBead02(self.ctx)


class ReactSoulBead02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002961)
        self.set_dialogue(type=1, spawn_id=5006, script='$02000296_BF__MAIN__7$', time=4) # Blackeye_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000500,10000501,10000502,10000503], state=0):
            return BossBattle01(self.ctx)


class BossBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[4000], visible=True) # Intro_Chord
        self.set_mesh(trigger_ids=[1001], visible=True, fade=2.0)
        self.set_effect(trigger_ids=[1000])
        self.set_dialogue(type=1, spawn_id=5006, script='$02000296_BF__MAIN__8$', time=3) # Blackeye_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return BossBattle02(self.ctx)


class BossBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[5100]) # Boss

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BossBattle03(self.ctx)


class BossBattle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002963, text_id=20002963, duration=5000) # 악령술사 디툰을 처치하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[5100]):
            return ReadyToMove01(self.ctx)


class ReadyToMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5100,5001,5002,5003,5004])
        self.set_mesh(trigger_ids=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209], visible=True, interval=100, fade=5.0) # ExitBridge
        self.set_agent(trigger_ids=[1300])
        self.set_agent(trigger_ids=[1301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToMove02(self.ctx)


class ReadyToMove02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.move_npc(spawn_id=5006, patrol_name='MS2PatrolData_5009')
        self.set_dialogue(type=1, spawn_id=5006, script='$02000296_BF__MAIN__9$', time=4) # Blackeye_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ReadyToMove03(self.ctx)


class ReadyToMove03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20002962, text_id=20002962, duration=6000) # 다음 층으로 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9002, spawn_ids=[5006]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5006])


initial_state = 대기
