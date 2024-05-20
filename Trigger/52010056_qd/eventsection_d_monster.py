""" trigger/52010056_qd/eventsection_d_monster.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2003]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[501], auto_target=False) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[502], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[503], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[504], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[505], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[506], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[507], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[508], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[509], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[510], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[511], auto_target=False) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[512], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[513], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[514], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[515], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[516], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[517], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[518], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[519], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[520], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[521], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[522], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[523], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[524], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[525], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[526], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[527], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[528], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[529], auto_target=False) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[530], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[531], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[532], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[533], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[534], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[535], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[536], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[537], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[538], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[539], auto_target=False) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[540], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[541], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[542], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[543], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[544], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[545], auto_target=False) # 퍼플 크림슨: 29000383


initial_state = Idle
