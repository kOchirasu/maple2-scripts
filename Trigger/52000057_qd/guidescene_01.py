""" trigger/52000057_qd/guidescene_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000611], quest_states=[2]):
            return 오필리아리젠(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000611], quest_states=[1]):
            return 오필리아리젠(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000610], quest_states=[3]):
            return 오필리아리젠상시(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000610], quest_states=[2]):
            return 오필리아리젠상시(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000610], quest_states=[1]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 말풍선대사01(self.ctx)


class 말풍선대사01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=198, spawn_ids=[1001]):
            return 시네마틱대사01(self.ctx)


class 시네마틱대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001871, script='$52000057_QD__GUIDESCENE_01__0$', time=2)
        self.set_dialogue(type=2, spawn_id=11001871, script='$52000057_QD__GUIDESCENE_01__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 연퀘감지(self.ctx)


class 연퀘감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000611], quest_states=[1]):
            return 오필리아대사연출01(self.ctx)


class 오필리아리젠(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 오필리아대사연출01(self.ctx)


class 오필리아대사연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001871, script='$52000057_QD__GUIDESCENE_01__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return SendSignalToGuide01(self.ctx)


# 트리거 To가이드
class SendSignalToGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guide_event(event_id=60660)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 종료(self.ctx)


class 오필리아리젠상시(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000611], quest_states=[1]):
            return 오필리아대사연출01(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
