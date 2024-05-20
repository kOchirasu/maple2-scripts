""" trigger/52020026_qd/52020026_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018])
        self.set_agent(trigger_ids=[9001], visible=True)
        self.set_agent(trigger_ids=[9002], visible=True)
        self.set_agent(trigger_ids=[9003], visible=True)
        self.set_agent(trigger_ids=[9004], visible=True)
        self.set_agent(trigger_ids=[9005], visible=True)
        self.set_agent(trigger_ids=[9006], visible=True)
        self.set_agent(trigger_ids=[9007], visible=True)
        self.set_agent(trigger_ids=[9008], visible=True)
        self.set_agent(trigger_ids=[9009], visible=True)
        self.set_agent(trigger_ids=[9010], visible=True)
        self.set_agent(trigger_ids=[9011], visible=True)
        self.set_agent(trigger_ids=[9012], visible=True)
        self.set_agent(trigger_ids=[9013], visible=True)
        self.set_agent(trigger_ids=[9014], visible=True)
        self.set_agent(trigger_ids=[9015], visible=True)
        self.set_agent(trigger_ids=[9016], visible=True)
        self.set_agent(trigger_ids=[9017], visible=True)
        self.set_agent(trigger_ids=[9018], visible=True)
        self.set_agent(trigger_ids=[9019], visible=True)
        self.set_agent(trigger_ids=[9020], visible=True)
        self.set_agent(trigger_ids=[9021], visible=True)
        self.set_agent(trigger_ids=[9022], visible=True)
        self.set_agent(trigger_ids=[9023], visible=True)
        self.set_agent(trigger_ids=[9024], visible=True)
        self.set_agent(trigger_ids=[9025], visible=True)
        self.set_agent(trigger_ids=[9026], visible=True)
        self.set_agent(trigger_ids=[9027], visible=True)
        self.set_agent(trigger_ids=[9028], visible=True)
        self.set_agent(trigger_ids=[9029], visible=True)
        self.set_agent(trigger_ids=[9030], visible=True)
        self.set_agent(trigger_ids=[9031], visible=True)
        self.set_agent(trigger_ids=[9032], visible=True)
        self.set_interact_object(trigger_ids=[10001320], state=2)
        self.set_interact_object(trigger_ids=[10001321], state=2)
        self.set_interact_object(trigger_ids=[10001322], state=2)
        self.set_interact_object(trigger_ids=[10001323], state=2)
        self.set_interact_object(trigger_ids=[10001324], state=2)
        self.set_interact_object(trigger_ids=[10001325], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[901]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 층1(self.ctx)


class 층1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 층레버활성1(self.ctx)


class 층레버활성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='레버를 작동시켜 계단을 완성하세요.', arg3='5000')
        self.set_interact_object(trigger_ids=[10001320], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001320], state=0):
            return 층2(self.ctx)


class 층2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_mesh(trigger_ids=[1001,1002,1003], visible=True, interval=500, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102]):
            return 층레버활성2(self.ctx)


class 층레버활성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001321], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001321], state=0):
            return 층3(self.ctx)


class 층3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.set_mesh(trigger_ids=[1004,1005,1006], visible=True, interval=500, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103,104]):
            return 층레버활성3(self.ctx)


class 층레버활성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001322], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001322], state=0):
            return 층4(self.ctx)


class 층4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.set_mesh(trigger_ids=[1007,1008,1009], visible=True, interval=500, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[105,106]):
            return 층레버활성4(self.ctx)


class 층레버활성4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001323], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001323], state=0):
            return 층5(self.ctx)


class 층5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.set_mesh(trigger_ids=[1010,1011,1012], visible=True, interval=500, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[906]):
            return 층_벽부수기5(self.ctx)


class 층_벽부수기5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9001])
        self.set_agent(trigger_ids=[9002])
        self.set_agent(trigger_ids=[9003])
        self.set_agent(trigger_ids=[9004])
        self.set_agent(trigger_ids=[9005])
        self.set_agent(trigger_ids=[9006])
        self.set_agent(trigger_ids=[9007])
        self.set_agent(trigger_ids=[9008])
        self.set_agent(trigger_ids=[9009])
        self.set_agent(trigger_ids=[9010])
        self.set_agent(trigger_ids=[9011])
        self.set_agent(trigger_ids=[9012])
        self.set_agent(trigger_ids=[9013])
        self.set_agent(trigger_ids=[9014])
        self.set_agent(trigger_ids=[9015])
        self.set_agent(trigger_ids=[9016])
        self.spawn_monster(spawn_ids=[108])
        self.set_skill(trigger_ids=[1], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[107,108]):
            return 층레버활성5(self.ctx)


class 층레버활성5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001324], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001324], state=0):
            return 층6(self.ctx)


class 층6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.set_mesh(trigger_ids=[1013,1014,1015], visible=True, interval=500, fade=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[907]):
            return 층_벽부수기6(self.ctx)


class 층_벽부수기6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9017])
        self.set_agent(trigger_ids=[9018])
        self.set_agent(trigger_ids=[9019])
        self.set_agent(trigger_ids=[9020])
        self.set_agent(trigger_ids=[9021])
        self.set_agent(trigger_ids=[9022])
        self.set_agent(trigger_ids=[9023])
        self.set_agent(trigger_ids=[9024])
        self.set_agent(trigger_ids=[9025])
        self.set_agent(trigger_ids=[9026])
        self.set_agent(trigger_ids=[9027])
        self.set_agent(trigger_ids=[9028])
        self.set_agent(trigger_ids=[9029])
        self.set_agent(trigger_ids=[9030])
        self.set_agent(trigger_ids=[9031])
        self.set_agent(trigger_ids=[9032])
        self.spawn_monster(spawn_ids=[111])
        self.set_skill(trigger_ids=[2], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[109,110,111]):
            return 층레버활성6(self.ctx)


class 층레버활성6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001325], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001325], state=0):
            return 포탈활성화(self.ctx)


class 포탈활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1016,1017,1018], visible=True, interval=500, fade=3.0)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 감지
