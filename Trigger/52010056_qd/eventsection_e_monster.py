""" trigger/52010056_qd/eventsection_e_monster.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5501])
        self.set_effect(trigger_ids=[5502])
        self.set_effect(trigger_ids=[5503])
        self.set_effect(trigger_ids=[5504])
        self.set_effect(trigger_ids=[5505])
        self.set_effect(trigger_ids=[5506])
        self.set_effect(trigger_ids=[5507])
        self.set_effect(trigger_ids=[5508])
        self.set_effect(trigger_ids=[5509])
        self.set_effect(trigger_ids=[5510])
        self.set_effect(trigger_ids=[5511])
        self.set_effect(trigger_ids=[5512])
        self.set_effect(trigger_ids=[5513])
        self.set_effect(trigger_ids=[5514])
        self.set_effect(trigger_ids=[5515])
        self.set_effect(trigger_ids=[5516])
        self.set_effect(trigger_ids=[5517])
        self.set_effect(trigger_ids=[5518])
        self.set_effect(trigger_ids=[5519])
        self.set_effect(trigger_ids=[5520])
        self.set_effect(trigger_ids=[5521])
        self.set_effect(trigger_ids=[5522])
        self.set_effect(trigger_ids=[5523])
        self.set_effect(trigger_ids=[5524])
        self.set_effect(trigger_ids=[5525])
        self.set_effect(trigger_ids=[5526])
        self.set_effect(trigger_ids=[5527])
        self.set_effect(trigger_ids=[5528])
        self.set_effect(trigger_ids=[5529])
        self.set_effect(trigger_ids=[5530])
        self.set_effect(trigger_ids=[5531])
        self.set_effect(trigger_ids=[5532])
        self.set_effect(trigger_ids=[5533])
        self.set_effect(trigger_ids=[5534])
        self.set_effect(trigger_ids=[5535])
        self.set_effect(trigger_ids=[5536])
        self.set_effect(trigger_ids=[5537])
        self.set_effect(trigger_ids=[5538])
        self.set_effect(trigger_ids=[5539])
        self.set_effect(trigger_ids=[5540])
        self.set_effect(trigger_ids=[5541])
        self.set_effect(trigger_ids=[5542])
        self.set_effect(trigger_ids=[5543])
        self.set_effect(trigger_ids=[5544])
        self.set_effect(trigger_ids=[5545])
        self.set_effect(trigger_ids=[5546])
        self.set_effect(trigger_ids=[5547])
        self.set_effect(trigger_ids=[5548])
        self.set_effect(trigger_ids=[5549])
        self.set_mesh(trigger_ids=[9001,9002,9003,9004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2009], quest_ids=[91000053], quest_states=[2]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[601]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[602]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[603]) # 크림슨 발록: 29000387
        self.spawn_monster(spawn_ids=[604]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[605]) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[606]) # 크림슨 스피어: 29000386

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크림슨발록_지시(self.ctx)


class 크림슨발록_지시(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=603, msg='$52010056_QD__EventSection_E_Monster__0$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 크림슨스피어_대답(self.ctx)


class 크림슨스피어_대답(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=601, msg='$52010056_QD__EventSection_E_Monster__1$', duration=1500)
        self.add_balloon_talk(spawn_id=602, msg='$52010056_QD__EventSection_E_Monster__1$', duration=1500)
        self.add_balloon_talk(spawn_id=604, msg='$52010056_QD__EventSection_E_Monster__1$', duration=1500)
        self.add_balloon_talk(spawn_id=605, msg='$52010056_QD__EventSection_E_Monster__1$', duration=1500)
        self.add_balloon_talk(spawn_id=606, msg='$52010056_QD__EventSection_E_Monster__1$', duration=1500)
        self.set_mesh(trigger_ids=[9002,9003,9004], visible=True)
        self.set_effect(trigger_ids=[5501], visible=True)
        self.set_effect(trigger_ids=[5502], visible=True)
        self.set_effect(trigger_ids=[5503], visible=True)
        self.set_effect(trigger_ids=[5504], visible=True)
        self.set_effect(trigger_ids=[5505], visible=True)
        self.set_effect(trigger_ids=[5506], visible=True)
        self.set_effect(trigger_ids=[5507], visible=True)
        self.set_effect(trigger_ids=[5508], visible=True)
        self.set_effect(trigger_ids=[5509], visible=True)
        self.set_effect(trigger_ids=[5510], visible=True)
        self.set_effect(trigger_ids=[5511], visible=True)
        self.set_effect(trigger_ids=[5512], visible=True)
        self.set_effect(trigger_ids=[5513], visible=True)
        self.set_effect(trigger_ids=[5514], visible=True)
        self.set_effect(trigger_ids=[5515], visible=True)
        self.set_effect(trigger_ids=[5516], visible=True)
        self.set_effect(trigger_ids=[5517], visible=True)
        self.set_effect(trigger_ids=[5518], visible=True)
        self.set_effect(trigger_ids=[5519], visible=True)
        self.set_effect(trigger_ids=[5520], visible=True)
        self.set_effect(trigger_ids=[5521], visible=True)
        self.set_effect(trigger_ids=[5522], visible=True)
        self.set_effect(trigger_ids=[5523], visible=True)
        self.set_effect(trigger_ids=[5524], visible=True)
        self.set_effect(trigger_ids=[5525], visible=True)
        self.set_effect(trigger_ids=[5526], visible=True)
        self.set_effect(trigger_ids=[5527], visible=True)
        self.set_effect(trigger_ids=[5528], visible=True)
        self.set_effect(trigger_ids=[5529], visible=True)
        self.set_effect(trigger_ids=[5530], visible=True)
        self.set_effect(trigger_ids=[5531], visible=True)
        self.set_effect(trigger_ids=[5532], visible=True)
        self.set_effect(trigger_ids=[5533], visible=True)
        self.set_effect(trigger_ids=[5534], visible=True)
        self.set_effect(trigger_ids=[5535], visible=True)
        self.set_effect(trigger_ids=[5536], visible=True)
        self.set_effect(trigger_ids=[5537], visible=True)
        self.set_effect(trigger_ids=[5538], visible=True)
        self.set_effect(trigger_ids=[5539], visible=True)
        self.set_effect(trigger_ids=[5540], visible=True)
        self.set_effect(trigger_ids=[5541], visible=True)
        self.set_effect(trigger_ids=[5542], visible=True)
        self.set_effect(trigger_ids=[5543], visible=True)
        self.set_effect(trigger_ids=[5544], visible=True)
        self.set_effect(trigger_ids=[5545], visible=True)
        self.set_effect(trigger_ids=[5546], visible=True)
        self.set_effect(trigger_ids=[5547], visible=True)
        self.set_effect(trigger_ids=[5548], visible=True)
        self.set_effect(trigger_ids=[5549], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[601,602,603,604,605]):
            return MeshOff(self.ctx)


class MeshOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5501])
        self.set_effect(trigger_ids=[5502])
        self.set_effect(trigger_ids=[5503])
        self.set_effect(trigger_ids=[5504])
        self.set_effect(trigger_ids=[5505])
        self.set_effect(trigger_ids=[5506])
        self.set_effect(trigger_ids=[5507])
        self.set_effect(trigger_ids=[5508])
        self.set_effect(trigger_ids=[5509])
        self.set_effect(trigger_ids=[5510])
        self.set_effect(trigger_ids=[5511])
        self.set_effect(trigger_ids=[5512])
        self.set_effect(trigger_ids=[5513])
        self.set_effect(trigger_ids=[5514])
        self.set_effect(trigger_ids=[5515])
        self.set_effect(trigger_ids=[5516])
        self.set_effect(trigger_ids=[5517])
        self.set_effect(trigger_ids=[5518])
        self.set_effect(trigger_ids=[5519])
        self.set_effect(trigger_ids=[5520])
        self.set_effect(trigger_ids=[5521])
        self.set_effect(trigger_ids=[5522])
        self.set_effect(trigger_ids=[5523])
        self.set_effect(trigger_ids=[5524])
        self.set_effect(trigger_ids=[5525])
        self.set_effect(trigger_ids=[5526])
        self.set_effect(trigger_ids=[5527])
        self.set_effect(trigger_ids=[5528])
        self.set_effect(trigger_ids=[5529])
        self.set_effect(trigger_ids=[5530])
        self.set_effect(trigger_ids=[5531])
        self.set_effect(trigger_ids=[5532])
        self.set_effect(trigger_ids=[5533])
        self.set_effect(trigger_ids=[5534])
        self.set_effect(trigger_ids=[5535])
        self.set_effect(trigger_ids=[5536])
        self.set_effect(trigger_ids=[5537])
        self.set_effect(trigger_ids=[5538])
        self.set_effect(trigger_ids=[5539])
        self.set_effect(trigger_ids=[5540])
        self.set_effect(trigger_ids=[5541])
        self.set_effect(trigger_ids=[5542])
        self.set_effect(trigger_ids=[5543])
        self.set_effect(trigger_ids=[5544])
        self.set_effect(trigger_ids=[5545])
        self.set_effect(trigger_ids=[5546])
        self.set_effect(trigger_ids=[5547])
        self.set_effect(trigger_ids=[5548])
        self.set_effect(trigger_ids=[5549])
        self.set_mesh(trigger_ids=[9001,9002,9003,9004])


initial_state = Idle
