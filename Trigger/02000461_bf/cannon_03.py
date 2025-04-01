""" trigger/02000461_bf/cannon_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[693])
        self.set_effect(trigger_ids=[793])
        self.set_mesh(trigger_ids=[3903], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cannon03') == 1:
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2903])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2903]):
            self.set_effect(trigger_ids=[693], visible=True)
            self.set_mesh(trigger_ids=[3903], fade=5.0)
            return 보스전_대기(self.ctx)


class 보스전_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Bosscannon03') == 1:
            return 보스전용_생성(self.ctx)


class 보스전용_생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[693])
        self.set_effect(trigger_ids=[793], visible=True)
        self.set_mesh(trigger_ids=[3903], visible=True)
        self.spawn_monster(spawn_ids=[2903])
        self.add_buff(box_ids=[2099], skill_id=70002081, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2903]):
            self.set_effect(trigger_ids=[693], visible=True)
            self.set_effect(trigger_ids=[793])
            self.set_mesh(trigger_ids=[3903], fade=5.0)
            self.add_buff(box_ids=[2099], skill_id=70002082, level=1, is_skill_set=False)
            self.add_buff(box_ids=[2903], skill_id=40444001, level=1, is_skill_set=False)
            return 보스전용_재생성대기(self.ctx)
        if self.user_value(key='DungeonClear') == 1:
            return 종료(self.ctx)


class 보스전용_재생성대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=90000):
            return 보스전용_생성(self.ctx)
        if self.user_value(key='DungeonClear') == 1:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[693])
        self.set_effect(trigger_ids=[793])
        self.set_mesh(trigger_ids=[3903], visible=True)
        self.destroy_monster(spawn_ids=[2903])


initial_state = 대기
