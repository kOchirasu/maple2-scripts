""" trigger/52000040_qd/main_02.xml """
import trigger_api


# 출연진 : 라오즈(401 : 11001760)
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4)
        self.set_portal(portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[1]):
            return end(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[2]):
            return end(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[3]):
            return end(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003052], quest_states=[3]):
            return start_05(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003052], quest_states=[2]):
            return start_05(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003052], quest_states=[1]):
            self.set_effect(trigger_ids=[6002], visible=True)
            self.spawn_monster(spawn_ids=[401], auto_target=False)
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=401, script='$52000040_QD__MAIN_02__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=401, script='$52000040_QD__MAIN_02__1$', time=2)
        self.set_dialogue(type=1, spawn_id=401, script='$52000040_QD__MAIN_02__2$', time=2, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_4001') # 연출용 라오즈 이동
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=702, spawn_ids=[401]):
            return npc_exit_01(self.ctx)


class npc_exit_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001], visible=True)
        self.destroy_monster(spawn_ids=[401])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='FollowingLaoz') # 퀘스트 목표 체크용 업적이벤트 발생
        self.spawn_monster(spawn_ids=[501], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[1]):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[501])
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4, visible=True)


initial_state = ready
