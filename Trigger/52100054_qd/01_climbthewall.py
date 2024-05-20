""" trigger/52100054_qd/01_climbthewall.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[5100,5101,5102,5103,5104,5105,5106]) # ArrowGuide01
        self.set_effect(trigger_ids=[5200,5201,5202,5203]) # DownArrowBomb
        self.set_effect(trigger_ids=[5300,5301,5302,5303,5304]) # ArrowGuide02
        self.set_effect(trigger_ids=[5400,5401,5402]) # ArrowGuide03
        self.set_effect(trigger_ids=[5500,5501,5502,5503,5504]) # ArrowGuide04
        self.set_ladder(trigger_ids=[510]) # Ladder01
        self.set_ladder(trigger_ids=[511]) # Ladder01
        self.set_ladder(trigger_ids=[512]) # Ladder01
        self.set_ladder(trigger_ids=[513]) # Ladder01
        self.set_ladder(trigger_ids=[514]) # Ladder01
        self.set_ladder(trigger_ids=[515]) # Ladder01
        self.set_ladder(trigger_ids=[516]) # Ladder01
        self.set_ladder(trigger_ids=[517]) # Ladder01
        self.set_ladder(trigger_ids=[518]) # Ladder01
        self.set_ladder(trigger_ids=[519]) # Ladder01
        self.set_ladder(trigger_ids=[520]) # Ladder01
        self.set_ladder(trigger_ids=[521]) # Ladder01
        self.set_ladder(trigger_ids=[522]) # Ladder01
        self.set_ladder(trigger_ids=[530]) # Ladder02
        self.set_ladder(trigger_ids=[531]) # Ladder02
        self.set_ladder(trigger_ids=[532]) # Ladder02
        self.set_ladder(trigger_ids=[533]) # Ladder02
        self.set_ladder(trigger_ids=[534]) # Ladder02
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008], visible=True) # Invisible_AlwaysOn
        self.set_interact_object(trigger_ids=[10002083], state=1) # Lever
        self.set_interact_object(trigger_ids=[10002084], state=1) # Lever
        self.destroy_monster(spawn_ids=[901,902,903,910,911,912,913,920,921,922,923,930,931,932,933,934]) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FirstArrowGuide01(self.ctx)


class FirstArrowGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039801, text_id=20039801, duration=4000) # 가이드 : 벽을 타고 올라가기
        self.set_effect(trigger_ids=[5100,5101,5102,5103,5104,5105,5106], visible=True) # ArrowGuide01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            # 테라스 도착
            return TerraceMobAttack01(self.ctx)


class TerraceMobAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[901,902,903], auto_target=False) # Mob_Actor
        self.set_dialogue(type=1, spawn_id=901, script='$52100054_QD__01_CLIMBTHEWALL__0$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=902, script='$52100054_QD__01_CLIMBTHEWALL__0$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=903, script='$52100054_QD__01_CLIMBTHEWALL__0$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TerraceMobAttack02(self.ctx)


class TerraceMobAttack02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[910,911,912,913], auto_target=False)
        self.set_effect(trigger_ids=[5500,5501,5502,5503,5504], visible=True) # ArrowGuide04

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LiftUpBombGuide01(self.ctx)


class LiftUpBombGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 폭탄을 들어서 가로막힌 벽을 향해 던지기
        self.show_guide_summary(entity_id=20039802, text_id=20039802, duration=4000)
        self.set_effect(trigger_ids=[5200,5201,5202,5203], visible=True) # DownArrowBomb

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9150]):
            # 테라스 너머 중간 벽
            return SecondArrowGuide01(self.ctx)


class SecondArrowGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5500,5501,5502,5503,5504]) # ArrowGuide04
        self.set_effect(trigger_ids=[5300,5301,5302,5303,5304], visible=True) # ArrowGuide02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9200]):
            # 탑 아래층 도착
            return TowerUnderMobAttack01(self.ctx)


class TowerUnderMobAttack01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039803, text_id=20039803, duration=3000) # 가이드 : 레버를 당기기
        self.spawn_monster(spawn_ids=[920,921,922,923], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002083], state=0):
            return LadderOnToTowerUp01(self.ctx)


class LadderOnToTowerUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039804, text_id=20039804, duration=3000) # 가이드 : 사다리를 타고 위로 올라가기
        self.set_ladder(trigger_ids=[510], visible=True, enable=True, fade=1) # Ladder01
        self.set_ladder(trigger_ids=[511], visible=True, enable=True, fade=2) # Ladder01
        self.set_ladder(trigger_ids=[512], visible=True, enable=True, fade=3) # Ladder01
        self.set_ladder(trigger_ids=[513], visible=True, enable=True, fade=4) # Ladder01
        self.set_ladder(trigger_ids=[514], visible=True, enable=True, fade=5) # Ladder01
        self.set_ladder(trigger_ids=[515], visible=True, enable=True, fade=6) # Ladder01
        self.set_ladder(trigger_ids=[516], visible=True, enable=True, fade=7) # Ladder01
        self.set_ladder(trigger_ids=[517], visible=True, enable=True, fade=8) # Ladder01
        self.set_ladder(trigger_ids=[518], visible=True, enable=True, fade=9) # Ladder01
        self.set_ladder(trigger_ids=[519], visible=True, enable=True, fade=10) # Ladder01
        self.set_ladder(trigger_ids=[520], visible=True, enable=True, fade=11) # Ladder01
        self.set_ladder(trigger_ids=[521], visible=True, enable=True, fade=12) # Ladder01
        self.set_ladder(trigger_ids=[522], visible=True, enable=True, fade=13) # Ladder01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9300]):
            return GuideMoveToBridge01(self.ctx)


class GuideMoveToBridge01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5400,5401,5402], visible=True) # ArrowGuide03
        self.spawn_monster(spawn_ids=[930,931,932,933,934], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9400]):
            # 다리 끝 도착
            return GuidePullTheLever01(self.ctx)


class GuidePullTheLever01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039803, text_id=20039803, duration=3000) # 가이드 : 레버를 당기기

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002084], state=0):
            return LadderOnToNextMap01(self.ctx)


class LadderOnToNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, enable=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20039804, text_id=20039804, duration=3000) # 가이드 : 사다리를 타고 위로 올라가기
        self.set_ladder(trigger_ids=[530], visible=True, enable=True, fade=1) # Ladder02
        self.set_ladder(trigger_ids=[531], visible=True, enable=True, fade=2) # Ladder02
        self.set_ladder(trigger_ids=[532], visible=True, enable=True, fade=3) # Ladder02
        self.set_ladder(trigger_ids=[533], visible=True, enable=True, fade=4) # Ladder02
        self.set_ladder(trigger_ids=[534], visible=True, enable=True, fade=5) # Ladder02


initial_state = Wait
