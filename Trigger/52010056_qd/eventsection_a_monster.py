""" trigger/52010056_qd/eventsection_a_monster.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2002]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=201, msg='$52010056_QD__EventSection_A_Monster__0$', duration=2800)
        self.spawn_monster(spawn_ids=[201]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[202]) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[203]) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[204]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[205]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[206]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[207]) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[208]) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[209]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[210]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[211]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[212]) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[213]) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[214]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[215]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[216]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[217]) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[218]) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[219]) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[220]) # 화이트 크림슨: 29000385


initial_state = Idle
