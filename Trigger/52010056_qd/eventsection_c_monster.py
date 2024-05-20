""" trigger/52010056_qd/eventsection_c_monster.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2003]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401], auto_target=False) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[402], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[403], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[404], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[405], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[406], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[407], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[408], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[409], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[410], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[411], auto_target=False) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[412], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[413], auto_target=False) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[414], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[415], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[416], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[417], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[418], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[419], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[420], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[421], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[422], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[423], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[424], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[425], auto_target=False) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[426], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[427], auto_target=False) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[428], auto_target=False) # 화이트 크림슨: 29000385


initial_state = Idle
