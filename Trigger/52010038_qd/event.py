""" trigger/52010038_qd/event.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)
        self.set_agent(trigger_ids=[8009], visible=True)
        self.set_agent(trigger_ids=[8010], visible=True)
        self.set_agent(trigger_ids=[8011], visible=True)
        self.set_agent(trigger_ids=[8012], visible=True)
        self.set_agent(trigger_ids=[8013], visible=True)
        self.set_skill(trigger_ids=[710])
        self.set_skill(trigger_ids=[711])
        self.set_effect(trigger_ids=[6110])
        self.set_effect(trigger_ids=[6111])
        self.set_effect(trigger_ids=[6298])
        self.set_actor(trigger_id=220)
        self.set_actor(trigger_id=221)
        self.set_actor(trigger_id=222)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EventStart') == 1:
            return 이벤트조건(self.ctx)


class 이벤트조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6298], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 이벤트시작(self.ctx)


class 이벤트시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1200], auto_target=False)
        self.destroy_monster(spawn_ids=[1201])
        self.set_dialogue(type=1, spawn_id=1200, script='$52010038_QD__EVENT__0$', time=2)
        self.move_npc(spawn_id=1200, patrol_name='MS2PatrolData_1200')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=104, spawn_ids=[1200]):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[710], enable=True)
        self.set_effect(trigger_ids=[6110], visible=True)
        self.spawn_monster(spawn_ids=[2012,2013,2014,2015])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 감지대기(self.ctx)


class 감지대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])
        self.set_agent(trigger_ids=[8013])
        self.set_dialogue(type=1, spawn_id=1200, script='$52010038_QD__EVENT__2$', time=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[105]):
            return 폭발시퀀스시작(self.ctx)


class 폭발시퀀스시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=220, visible=True, initial_sequence='Regen_A')
        self.set_actor(trigger_id=221, visible=True, initial_sequence='Regen_A')
        self.set_actor(trigger_id=222, visible=True, initial_sequence='Regen_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 폭발딜레이(self.ctx)


class 폭발딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=220, visible=True, initial_sequence='Attack_01_A')
        self.set_actor(trigger_id=221, visible=True, initial_sequence='Attack_01_A')
        self.set_actor(trigger_id=222, visible=True, initial_sequence='Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 폭발(self.ctx)


class 폭발(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=220, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=221, visible=True, initial_sequence='Attack_02_A')
        self.set_actor(trigger_id=222, visible=True, initial_sequence='Attack_02_A')
        self.set_skill(trigger_ids=[711], enable=True)
        self.set_effect(trigger_ids=[6298])
        self.set_effect(trigger_ids=[6111], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            return 폭탄숨김(self.ctx)


class 폭탄숨김(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=220)
        self.set_actor(trigger_id=221)
        self.set_actor(trigger_id=222)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1300):
            return 점수(self.ctx)


class 점수(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[4010], auto_target=False)
        self.spawn_monster(spawn_ids=[4030], auto_target=False)
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=5000, script='$52010038_QD__event__4$', voice='ko/Npc/00002105')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
