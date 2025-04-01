""" trigger/02000481_bf/01_enter.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001]) # Invisible_TireSpawn
        self.set_mesh(trigger_ids=[3002,3003,3004,3006,3007,3008]) # Invisible_MobSpawn
        self.set_mesh(trigger_ids=[3005,3008], visible=True) # Invisible_BehindBarrier
        # Invisible_BarrierGrating
        self.set_mesh(trigger_ids=[3100], visible=True)
        self.destroy_monster(spawn_ids=[102,202]) # Npc_Battle
        self.destroy_monster(spawn_ids=[300,301]) # TirePendulum
        self.destroy_monster(spawn_ids=[900,901,910,911,912,913,920,921,922]) # TirePendulum
        self.spawn_monster(spawn_ids=[101,201], auto_target=False) # Npc_Actor
        self.set_mesh(trigger_ids=[3202,3203], visible=True) # Grating_Top
        self.set_mesh(trigger_ids=[3200,3201]) # Grating_Opened
        self.set_mesh(trigger_ids=[3300,3301,3302,3303], visible=True) # Grating_Closed
        self.set_breakable(trigger_ids=[4000,4001,4002,4003]) # Grating
        self.set_visible_breakable_object(trigger_ids=[4000,4001,4002,4003]) # Grating
        self.set_interact_object(trigger_ids=[10002025], state=0) # Lever

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='start') == 1:
            return DungeonStart(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[300,301]) # TirePendulum

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcTalk01(self.ctx)


# 연출 시작
class NpcTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000119, script='$02000481_BF__01_ENTER__0$', time=4) # 프레이
        self.set_skip(state=NpcTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return NpcTalk01Skip(self.ctx)


class NpcTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return NpcTalk02(self.ctx)


class NpcTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000015, script='$02000481_BF__01_ENTER__1$', time=5) # 오스칼
        self.set_skip(state=NpcTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return NpcTalk02Skip(self.ctx)


class NpcTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NpcMonologue01(self.ctx)


class NpcMonologue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000481_BF__01_ENTER__2$', time=2) # 프레이
        self.set_dialogue(type=1, spawn_id=201, script='$02000481_BF__01_ENTER__3$', time=2) # 오스칼
        self.set_user_value(trigger_id=2, key='MobSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcChange01(self.ctx)


class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=101)
        self.remove_balloon_talk(spawn_id=201)
        self.destroy_monster(spawn_ids=[101,201]) # Npc_Actor
        self.spawn_monster(spawn_ids=[102,202], auto_target=False) # Npc_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NpcMonologue02(self.ctx)


class NpcMonologue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000481_BF__01_ENTER__4$', time=3) # 프레이
        self.set_dialogue(type=1, spawn_id=202, script='$02000481_BF__01_ENTER__5$', time=2, arg5=1) # 오스칼
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039501, text_id=20039501, duration=4000) # 가이드 : 레버 당기기
        self.set_interact_object(trigger_ids=[10002025], state=1) # Lever

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002025], state=0):
            return GratingOpen01(self.ctx)


class GratingOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039502, text_id=20039502, duration=4000) # 가이드 : 지하도 안쪽으로 이동하기
        self.set_mesh(trigger_ids=[3300,3301,3302,3303], start_delay=500) # Grating_Closed
        self.set_breakable(trigger_ids=[4000,4001,4002,4003], enable=True) # Grating
        self.set_visible_breakable_object(trigger_ids=[4000,4001,4002,4003], visible=True) # Grating

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return GratingOpen02(self.ctx)


class GratingOpen02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[910], auto_target=False)
        # Invisible_BarrierGrating
        self.set_mesh(trigger_ids=[3100])
        self.set_mesh(trigger_ids=[3200,3201], visible=True) # Grating_Opened

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GratingOpen03(self.ctx)


class GratingOpen03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000,4001,4002,4003]) # Grating
        self.set_visible_breakable_object(trigger_ids=[4000,4001,4002,4003]) # Grating
        self.spawn_monster(spawn_ids=[911,912,913], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return MobSpawn_Hallway01(self.ctx)


class MobSpawn_Hallway01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039503, text_id=20039503, duration=4000) # 가이드 : 타이어에 매달려 넘어가기
        self.spawn_monster(spawn_ids=[920], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            return MobSpawn_Hallway02(self.ctx)


class MobSpawn_Hallway02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[921,922], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039504, text_id=20039504, duration=4000) # 가이드 : 사다리를 타고 위로 올라가기


initial_state = Wait
