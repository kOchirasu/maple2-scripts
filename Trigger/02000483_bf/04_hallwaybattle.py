""" trigger/02000483_bf/04_hallwaybattle.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # InvisibleBarrier_AlwaysOn
        self.set_mesh(trigger_ids=[3800,3900], visible=True)
        self.set_portal(portal_id=20)
        self.set_interact_object(trigger_ids=[10002045], state=0) # Key
        self.destroy_monster(spawn_ids=[901,902,903]) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            # 복도 진입
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901,902,903], auto_target=False) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MobTrapOn01(self.ctx)


class MobTrapOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=901, script='$02000483_BF__04_HALLWAYBATTLE__0$', time=2)
        self.set_dialogue(type=1, spawn_id=902, script='$02000483_BF__04_HALLWAYBATTLE__1$', time=2)
        self.set_dialogue(type=1, spawn_id=903, script='$02000483_BF__04_HALLWAYBATTLE__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MobTrapOn02(self.ctx)


class MobTrapOn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=5, key='MobWave', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039704, text_id=20039704, duration=2000) # 가이드 : 적군이 몰려옵니다!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MobTrapOn03(self.ctx)


class MobTrapOn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=6, key='BlockEnable', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GuideUseKey(self.ctx)


class GuideUseKey(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 다른 방으로 이동할 단서를 찾으세요
        self.show_guide_summary(entity_id=20039705, text_id=20039705)
        self.set_interact_object(trigger_ids=[10002045], state=1) # Key

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002045], state=0):
            return PortalOn(self.ctx)


class PortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20039705)
        self.set_portal(portal_id=20, visible=True, enable=True)


initial_state = Wait
