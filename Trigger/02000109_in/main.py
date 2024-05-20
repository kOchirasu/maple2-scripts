""" trigger/02000109_in/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4001,4002,4003,4004], visible=True)
        self.set_mesh(trigger_ids=[4011])
        self.destroy_monster(spawn_ids=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001608], quest_states=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001608], quest_states=[2]):
            return 일기장스폰_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001608], quest_states=[1]):
            return 일기장스폰_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[3]):
            return 일기장스폰_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[2]):
            return 일기장스폰_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[1]):
            return 벽삭제(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[3]):
            return npc스폰_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[2]):
            return npc스폰_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[1]):
            return 종료(self.ctx)


class 퀘스트진행체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001608], quest_states=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001608], quest_states=[2]):
            return None # Missing State: 일기장스폰
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001608], quest_states=[1]):
            return None # Missing State: 일기장스폰
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[3]):
            return None # Missing State: 일기장스폰
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[2]):
            return 일기장스폰_대기(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[1]):
            return 벽삭제(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[3]):
            return npc스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[2]):
            return npc스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[1]):
            return 종료(self.ctx)


class npc스폰_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[1]):
            return 벽삭제(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[1]):
            return 퀘스트진행체크(self.ctx)


class npc스폰(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[1]):
            return 벽삭제(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[1]):
            return 퀘스트진행체크(self.ctx)


class 벽삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4001,4002,4003,4004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[2]):
            return 일기장스폰_대기(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[2]):
            return 퀘스트진행체크(self.ctx)


class 일기장스폰_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_mesh(trigger_ids=[4011], visible=True)
        self.set_mesh(trigger_ids=[4001,4002,4003,4004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[3]):
            return 종료(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[3]):
            return 일기장스폰01(self.ctx)


class 일기장스폰01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4011], visible=True)
        self.set_mesh(trigger_ids=[4001,4002,4003,4004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[2]):
            return 일기장스폰02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[3]):
            return 일기장없어짐(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[3]):
            return 일기장스폰02(self.ctx)


class 일기장스폰02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4011], visible=True)
        self.set_mesh(trigger_ids=[4001,4002,4003,4004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[2]):
            return 일기장스폰01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001606], quest_states=[3]):
            return 일기장없어짐(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[3]):
            return 일기장스폰01(self.ctx)


class 일기장없어짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.set_mesh(trigger_ids=[4011])
        self.set_mesh(trigger_ids=[4001,4002,4003,4004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[2]):
            return 일기장스폰_대기(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001607], quest_states=[2]):
            return 퀘스트진행체크(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
