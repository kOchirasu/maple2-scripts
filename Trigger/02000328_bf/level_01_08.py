""" trigger/02000328_bf/level_01_08.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[5108])
        # self.spawn_monster(spawn_ids=[10008])
        self.set_mesh(trigger_ids=[31801,31802,31803,31804,31805,31806,31807,31808,31809,31810,31811,31812,31813,31814,31815,31816,31817,31818,31819,31820,31821,31822])
        self.set_mesh(trigger_ids=[41801], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10006]):
            # self.set_cube(trigger_ids=[5108], is_visible=True)
            self.set_mesh(trigger_ids=[31801,31802,31803,31804,31805,31806,31807,31808,31809,31810,31811,31812,31813,31814,31815,31816,31817,31818,31819,31820,31821,31822], visible=True, interval=200, fade=2.0)
            self.set_mesh(trigger_ids=[41801])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
