""" trigger/52000066_qd/train03.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001]) # DownArrow
        self.set_interact_object(trigger_ids=[10001072], state=1) # TrainLever
        self.set_user_value(key='TrainMove', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TrainMove') == 1:
            return FourthPhaseChase01(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=25200663, text_id=25200663) # 가이드 : 레버를 당겨 보세요.


class FourthPhaseChase01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # DownArrow

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001072], state=0):
            return FourthPhaseChase02(self.ctx)


class FourthPhaseChase02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25200663)
        self.set_effect(trigger_ids=[5001]) # DownArrow
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_200')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GetInTheTrain01(self.ctx)


class GetInTheTrain01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=25200664, text_id=25200664) # 가이드 : 수레에 타세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9700]):
            # HoldTrain
            return GetInTheTrain02(self.ctx)


class GetInTheTrain02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=700, enable=True) # LocalTargetCamera
        self.hide_guide_summary(entity_id=25200664)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=25200665, text_id=25200665, duration=2000) # 가이드 : 출발합니다!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return GetInTheTrain03(self.ctx)


class GetInTheTrain03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return GetInTheTrain04(self.ctx)


class GetInTheTrain04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=700) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthPhaseChase01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[5001], visible=True) # DownArrow
        self.set_interact_object(trigger_ids=[10001072], state=1) # TrainLever


initial_state = Wait
