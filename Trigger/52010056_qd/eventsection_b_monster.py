""" trigger/52010056_qd/eventsection_b_monster.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2003]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[302]) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[303]) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[304]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[305]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[306]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[307]) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[308]) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[309]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[310]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[311]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[312]) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[313]) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[314]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[315]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[316]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[317]) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[318]) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[319]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[320]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[321]) # 화이트 크림슨: 29000385


initial_state = Idle
