""" trigger/02000074_in/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4000])
        self.destroy_monster(spawn_ids=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001592], quest_states=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001592], quest_states=[2]):
            return 쪽지스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001592], quest_states=[1]):
            return 쪽지스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001591], quest_states=[3]):
            return 쪽지스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001591], quest_states=[2]):
            return 쪽지스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001589], quest_states=[2]):
            return 케이틀린스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001589], quest_states=[1]):
            return 케이틀린스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001588], quest_states=[3]):
            return 케이틀린스폰(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001588], quest_states=[2]): # 
            return 케이틀린스폰(self.ctx)


class 케이틀린스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 연출용 어둠의 세력 몬스터

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9000]):
            return start(self.ctx)


class 쪽지스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_mesh(trigger_ids=[4000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9000]):
            return start(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
