""" trigger/02000397_bf/03_usingbomb.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5100,5101,5102,5103]) # DownArrowBomb
        self.set_effect(trigger_ids=[5200,5201,5202,5203]) # TargetBoxGuide
        self.destroy_monster(spawn_ids=[910,911]) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[910,911], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ArrowGuideOn(self.ctx)


class ArrowGuideOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 폭탄을 들어서 가로막힌 벽을 향해 던지기
        self.show_guide_summary(entity_id=20039703, text_id=20039703, duration=4000)
        self.set_effect(trigger_ids=[5100,5101,5102,5103], visible=True) # DownArrowBomb
        self.set_effect(trigger_ids=[5200,5201,5202,5203], visible=True) # TargetBoxGuide

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9201]):
            # 무기고 탈출
            return ArrowGuideOff(self.ctx)


class ArrowGuideOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5100,5101,5102,5103]) # DownArrowBomb
        self.set_effect(trigger_ids=[5200,5201,5202,5203]) # TargetBoxGuide


initial_state = Wait
