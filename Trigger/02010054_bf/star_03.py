""" trigger/02010054_bf/star_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000861], state=2)
        self.set_effect(trigger_ids=[606])
        self.set_mesh(trigger_ids=[3310,3311,3312,3313])
        self.set_mesh(trigger_ids=[3126], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3310,3311,3312,3313], visible=True, interval=500, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3126], fade=5.0)
        self.set_mesh(trigger_ids=[3310,3311,3312,3313], interval=900, fade=3.0)
        self.set_effect(trigger_ids=[606], visible=True)
        self.spawn_monster(spawn_ids=[2005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2005]):
            self.set_interact_object(trigger_ids=[10000861], state=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
