""" trigger/80000014_bonus/train.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3123,3124,3125,3126,3127,3128,3129])
        self.set_mesh(trigger_ids=[3121], visible=True)
        self.set_mesh(trigger_ids=[3122], visible=True)
        self.set_mesh(trigger_ids=[3701,3702,3703])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[120]):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1200], auto_target=False)
        self.set_mesh(trigger_ids=[3122], start_delay=500)
        self.add_buff(box_ids=[1200], skill_id=60170051, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 삼(self.ctx)


class 삼(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3703], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이(self.ctx)


class 이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3703])
        self.set_mesh(trigger_ids=[3702], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 일(self.ctx)


class 일(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3702])
        self.set_mesh(trigger_ids=[3701], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 출발(self.ctx)


class 출발(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3701])
        self.move_npc(spawn_id=1200, patrol_name='MS2PatrolData1200A')
        self.create_item(spawn_ids=[9020,9021,9022,9023,9024,9025], arg5=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=121, spawn_ids=[1200]):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.destroy_monster(spawn_ids=[1200])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
