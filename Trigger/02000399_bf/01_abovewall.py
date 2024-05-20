""" trigger/02000399_bf/01_abovewall.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # InvisibleMesh_forTransparancy
        self.set_mesh(trigger_ids=[3000], visible=True)
        self.set_portal(portal_id=2)
        self.set_interact_object(trigger_ids=[10001150], state=0) # LeverForLadder01
        self.set_interact_object(trigger_ids=[10001151], state=0) # LeverForRope
        self.set_interact_object(trigger_ids=[10001152], state=0) # LeverForLadder02
        self.destroy_monster(spawn_ids=[901,902,903]) # Mob
        self.destroy_monster(spawn_ids=[910,911,912,920,921,922,930,931,932,940,941,942]) # Mob
        self.set_ladder(trigger_ids=[510]) # Ladder01
        self.set_ladder(trigger_ids=[511]) # Ladder01
        self.set_ladder(trigger_ids=[512]) # Ladder01
        self.set_ladder(trigger_ids=[513]) # Ladder01
        self.set_ladder(trigger_ids=[514]) # Ladder01
        self.set_ladder(trigger_ids=[520]) # Ladder02
        self.set_ladder(trigger_ids=[521]) # Ladder02
        self.set_ladder(trigger_ids=[522]) # Ladder02
        self.set_ladder(trigger_ids=[523]) # Ladder02
        self.set_ladder(trigger_ids=[524]) # Ladder02
        self.set_ladder(trigger_ids=[525]) # Ladder02
        self.set_ladder(trigger_ids=[526]) # Ladder02
        self.set_ladder(trigger_ids=[527]) # Ladder02
        self.set_ladder(trigger_ids=[528]) # Ladder02
        self.set_rope(trigger_id=530) # Rope
        self.set_rope(trigger_id=531) # Rope
        self.set_rope(trigger_id=532) # Rope
        self.set_rope(trigger_id=533) # Rope
        self.set_rope(trigger_id=534) # Rope
        self.set_rope(trigger_id=535) # Rope
        self.set_rope(trigger_id=536) # Rope
        self.set_rope(trigger_id=537) # Rope
        self.set_rope(trigger_id=538) # Rope
        self.set_rope(trigger_id=539) # Rope

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GuideToMove(self.ctx)


class GuideToMove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 성벽을 따라 다음 탑으로 이동하세요.
        self.show_guide_summary(entity_id=20039901, text_id=20039901, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            # 계단 진입
            return MobActorSpawn(self.ctx)


class MobActorSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901,902,903], auto_target=False) # Mob
        self.set_dialogue(type=1, spawn_id=901, script='$02000399_BF__01_ABOVEWALL__0$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=902, script='$02000399_BF__01_ABOVEWALL__1$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=903, script='$02000399_BF__01_ABOVEWALL__2$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Battle01Start(self.ctx)


class Battle01Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[930,931,932], auto_target=False) # Mob
        self.set_interact_object(trigger_ids=[10001150], state=1) # LeverForLadder01

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001150], state=0):
            return Battle02Start(self.ctx)


class Battle02Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039902, text_id=20039902, duration=3000) # 가이드 : 사다리를 타고 위로 올라가세요.
        self.set_ladder(trigger_ids=[510], visible=True, enable=True, fade=2) # Ladder01
        self.set_ladder(trigger_ids=[511], visible=True, enable=True, fade=2) # Ladder01
        self.set_ladder(trigger_ids=[512], visible=True, enable=True, fade=2) # Ladder01
        self.set_ladder(trigger_ids=[513], visible=True, enable=True, fade=2) # Ladder01
        self.set_ladder(trigger_ids=[514], visible=True, enable=True, fade=2) # Ladder01
        self.set_ladder(trigger_ids=[520], visible=True, enable=True, fade=2) # Ladder02
        self.spawn_monster(spawn_ids=[910,911,912], auto_target=False) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            return Battle03Start(self.ctx)


class Battle03Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2, key='TireSpawn', value=1)
        self.spawn_monster(spawn_ids=[920,921,922], auto_target=False) # Mob
        self.set_interact_object(trigger_ids=[10001151], state=1) # LeverForRope

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001151], state=0):
            return RopeOn(self.ctx)


class RopeOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_rope(trigger_id=530, visible=True, enable=True, fade=2) # Rope
        self.set_rope(trigger_id=531, visible=True, enable=True, fade=2) # Rope
        self.set_rope(trigger_id=532, visible=True, enable=True, fade=2) # Rope
        self.set_rope(trigger_id=533, visible=True, enable=True, fade=2) # Rope
        self.set_rope(trigger_id=534, visible=True, enable=True, fade=2) # Rope
        self.set_rope(trigger_id=535, visible=True, enable=True, fade=2) # Rope
        self.set_rope(trigger_id=536, visible=True, enable=True, fade=2) # Rope
        self.set_rope(trigger_id=537, visible=True, enable=True, fade=2) # Rope
        self.set_rope(trigger_id=538, visible=True, enable=True, fade=2) # Rope
        self.set_rope(trigger_id=539, visible=True, enable=True, fade=2) # Rope
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 로프를 타고 탑 위층으로 올라가세요.
        self.show_guide_summary(entity_id=20039906, text_id=20039906)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            # 탑 위층 진입
            return Battle04Start(self.ctx)


class Battle04Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20039906)
        self.spawn_monster(spawn_ids=[940,941,942], auto_target=False) # Mob
        self.set_interact_object(trigger_ids=[10001152], state=1) # LeverForLadder02

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001152], state=0):
            return PortalOn(self.ctx)


class PortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[520], visible=True, enable=True, fade=2) # Ladder02
        self.set_ladder(trigger_ids=[521], visible=True, enable=True, fade=2) # Ladder02
        self.set_ladder(trigger_ids=[522], visible=True, enable=True, fade=2) # Ladder02
        self.set_ladder(trigger_ids=[523], visible=True, enable=True, fade=2) # Ladder02
        self.set_ladder(trigger_ids=[524], visible=True, enable=True, fade=2) # Ladder02
        self.set_ladder(trigger_ids=[525], visible=True, enable=True, fade=2) # Ladder02
        self.set_ladder(trigger_ids=[526], visible=True, enable=True, fade=2) # Ladder02
        self.set_ladder(trigger_ids=[527], visible=True, enable=True, fade=2) # Ladder02
        self.set_ladder(trigger_ids=[528], visible=True, enable=True, fade=2) # Ladder02
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039804, text_id=20039804, duration=5000) # 가이드 : 사다리를 타고 위로 올라가세요.
        self.set_portal(portal_id=2, enable=True)


initial_state = Wait
