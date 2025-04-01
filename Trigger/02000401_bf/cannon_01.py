""" trigger/02000401_bf/cannon_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[691])
        self.set_mesh(trigger_ids=[3901], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cannon01') == 1:
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2901])
        self.add_buff(box_ids=[2901], skill_id=40444001, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2901]):
            self.set_effect(trigger_ids=[691], visible=True)
            self.set_mesh(trigger_ids=[3901], fade=5.0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
