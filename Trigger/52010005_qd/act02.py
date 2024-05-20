""" trigger/52010005_qd/act02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            self.set_interact_object(trigger_ids=[10000872], state=0)
            return 퀘스트조건02(self.ctx)


class 퀘스트조건02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002821], quest_states=[2]):
            # 2nd Quest
            return Q2_미카등장01(self.ctx)


# 2nd Quest
class Q2_미카등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return Q2_딜레이01(self.ctx)


class Q2_딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=2)
        self.select_camera(trigger_id=3001)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return Q2_미카대화01(self.ctx)


class Q2_미카대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=3)
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010005_QD__ACT02__0$', time=3)
        self.set_skip(state=Q2_미카대화02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return Q2_미카대화02대기(self.ctx)


class Q2_미카대화02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Q2_미카대화02(self.ctx)


class Q2_미카대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='13', seconds=3)
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010005_QD__ACT02__1$', time=3)
        self.set_skip(state=Q2_미카대화종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='13'):
            return Q2_미카대화종료(self.ctx)


class Q2_미카대화종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.select_camera(trigger_id=3001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
