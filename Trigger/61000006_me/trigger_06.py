""" trigger/61000006_me/trigger_06.xml """
import trigger_api


class 시간표등록(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # timeEvent.xml의 시작 시간 참조
        pass

    def on_tick(self) -> trigger_api.Trigger:
        return 시간표확인(self.ctx)


class 시간표확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000226], state=1)
        self.set_interact_object(trigger_ids=[10000227], state=1)
        self.set_interact_object(trigger_ids=[10000228], state=1)
        self.set_interact_object(trigger_ids=[10000229], state=1)
        self.set_interact_object(trigger_ids=[10000230], state=1)
        self.set_interact_object(trigger_ids=[10000231], state=1)
        self.set_effect(trigger_ids=[711])
        self.set_effect(trigger_ids=[712])
        self.set_effect(trigger_ids=[713])
        self.set_effect(trigger_ids=[714])
        self.set_effect(trigger_ids=[715])
        self.set_effect(trigger_ids=[716])
        self.set_effect(trigger_ids=[717])
        self.set_effect(trigger_ids=[718])
        self.set_effect(trigger_ids=[719])
        self.set_effect(trigger_ids=[720])
        self.set_effect(trigger_ids=[721])
        self.set_effect(trigger_ids=[722])
        self.set_skill(trigger_ids=[811])
        self.set_skill(trigger_ids=[812])
        self.set_skill(trigger_ids=[813])
        self.set_skill(trigger_ids=[814])
        self.set_skill(trigger_ids=[815])
        self.set_skill(trigger_ids=[816])
        self.set_skill(trigger_ids=[817])
        self.set_skill(trigger_ids=[818])
        self.set_skill(trigger_ids=[819])
        self.set_skill(trigger_ids=[820])
        self.set_skill(trigger_ids=[821])
        self.set_skill(trigger_ids=[822])
        self.set_skill(trigger_ids=[823])
        self.set_skill(trigger_ids=[824])
        self.set_skill(trigger_ids=[825])
        self.set_skill(trigger_ids=[826])
        self.set_skill(trigger_ids=[827])
        self.set_skill(trigger_ids=[828])
        self.set_skill(trigger_ids=[911])
        self.set_skill(trigger_ids=[912])
        self.set_skill(trigger_ids=[913])
        self.set_skill(trigger_ids=[914])
        self.set_skill(trigger_ids=[915])
        self.set_skill(trigger_ids=[916])
        self.set_skill(trigger_ids=[917])
        self.set_skill(trigger_ids=[918])
        self.set_skill(trigger_ids=[919])
        self.set_skill(trigger_ids=[920])
        self.set_skill(trigger_ids=[921])
        self.set_skill(trigger_ids=[922])
        self.set_skill(trigger_ids=[923])
        self.set_skill(trigger_ids=[924])
        self.set_skill(trigger_ids=[925])
        self.set_skill(trigger_ids=[926])
        self.set_skill(trigger_ids=[927])
        self.set_skill(trigger_ids=[928])

    def on_tick(self) -> trigger_api.Trigger:
        return 어나운스0(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_state(id=1, states=[미로패턴01,미로패턴02,미로패턴03])
        self.set_state(id=2, states=[점프패턴01,점프패턴02])
        self.set_timer(timer_id='89', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='89'):
            return 레버(self.ctx)


class 레버(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_state(id=1, states=[미로패턴01,미로패턴02,미로패턴03])
        self.set_state(id=2, states=[점프패턴01,점프패턴02])
        self.set_mesh(trigger_ids=[527,528,529], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 패턴결정(self.ctx)


class 패턴결정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.use_state(id=1, randomize=True)
        self.use_state(id=2, randomize=True)
        self.set_timer(timer_id='12', seconds=240)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 시간표확인(self.ctx)


class 미로패턴01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[527])


class 미로패턴02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[528])


class 미로패턴03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[529])


class 점프패턴01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[711], visible=True)
        self.set_effect(trigger_ids=[712])
        self.set_effect(trigger_ids=[713])
        self.set_effect(trigger_ids=[714], visible=True)
        self.set_effect(trigger_ids=[715])
        self.set_effect(trigger_ids=[716], visible=True)
        self.set_effect(trigger_ids=[717], visible=True)
        self.set_effect(trigger_ids=[718])
        self.set_effect(trigger_ids=[719], visible=True)
        self.set_effect(trigger_ids=[720])
        self.set_effect(trigger_ids=[721])
        self.set_effect(trigger_ids=[722], visible=True)
        self.set_skill(trigger_ids=[811], enable=True)
        self.set_skill(trigger_ids=[812], enable=True)
        self.set_skill(trigger_ids=[813], enable=True)
        self.set_skill(trigger_ids=[814])
        self.set_skill(trigger_ids=[815])
        self.set_skill(trigger_ids=[816])
        self.set_skill(trigger_ids=[817])
        self.set_skill(trigger_ids=[818])
        self.set_skill(trigger_ids=[819])
        self.set_skill(trigger_ids=[820], enable=True)
        self.set_skill(trigger_ids=[821], enable=True)
        self.set_skill(trigger_ids=[822], enable=True)
        self.set_skill(trigger_ids=[823], enable=True)
        self.set_skill(trigger_ids=[824], enable=True)
        self.set_skill(trigger_ids=[825], enable=True)
        self.set_skill(trigger_ids=[826])
        self.set_skill(trigger_ids=[827])
        self.set_skill(trigger_ids=[828])
        self.set_skill(trigger_ids=[911])
        self.set_skill(trigger_ids=[912])
        self.set_skill(trigger_ids=[913])
        self.set_skill(trigger_ids=[914], enable=True)
        self.set_skill(trigger_ids=[915], enable=True)
        self.set_skill(trigger_ids=[916], enable=True)
        self.set_skill(trigger_ids=[917], enable=True)
        self.set_skill(trigger_ids=[918], enable=True)
        self.set_skill(trigger_ids=[919], enable=True)
        self.set_skill(trigger_ids=[920])
        self.set_skill(trigger_ids=[921])
        self.set_skill(trigger_ids=[922])
        self.set_skill(trigger_ids=[923])
        self.set_skill(trigger_ids=[924])
        self.set_skill(trigger_ids=[925])
        self.set_skill(trigger_ids=[926], enable=True)
        self.set_skill(trigger_ids=[927], enable=True)
        self.set_skill(trigger_ids=[928], enable=True)


class 점프패턴02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[711])
        self.set_effect(trigger_ids=[712], visible=True)
        self.set_effect(trigger_ids=[713], visible=True)
        self.set_effect(trigger_ids=[714])
        self.set_effect(trigger_ids=[715])
        self.set_effect(trigger_ids=[716], visible=True)
        self.set_effect(trigger_ids=[717], visible=True)
        self.set_effect(trigger_ids=[718])
        self.set_effect(trigger_ids=[719], visible=True)
        self.set_effect(trigger_ids=[720])
        self.set_effect(trigger_ids=[721])
        self.set_effect(trigger_ids=[722], visible=True)
        self.set_skill(trigger_ids=[811])
        self.set_skill(trigger_ids=[812])
        self.set_skill(trigger_ids=[813])
        self.set_skill(trigger_ids=[814], enable=True)
        self.set_skill(trigger_ids=[815], enable=True)
        self.set_skill(trigger_ids=[816], enable=True)
        self.set_skill(trigger_ids=[817])
        self.set_skill(trigger_ids=[818])
        self.set_skill(trigger_ids=[819])
        self.set_skill(trigger_ids=[820], enable=True)
        self.set_skill(trigger_ids=[821], enable=True)
        self.set_skill(trigger_ids=[822], enable=True)
        self.set_skill(trigger_ids=[823], enable=True)
        self.set_skill(trigger_ids=[824], enable=True)
        self.set_skill(trigger_ids=[825], enable=True)
        self.set_skill(trigger_ids=[826])
        self.set_skill(trigger_ids=[827])
        self.set_skill(trigger_ids=[828])
        self.set_skill(trigger_ids=[911], enable=True)
        self.set_skill(trigger_ids=[912], enable=True)
        self.set_skill(trigger_ids=[913], enable=True)
        self.set_skill(trigger_ids=[914])
        self.set_skill(trigger_ids=[915])
        self.set_skill(trigger_ids=[916])
        self.set_skill(trigger_ids=[917], enable=True)
        self.set_skill(trigger_ids=[918], enable=True)
        self.set_skill(trigger_ids=[919], enable=True)
        self.set_skill(trigger_ids=[920])
        self.set_skill(trigger_ids=[921])
        self.set_skill(trigger_ids=[922])
        self.set_skill(trigger_ids=[923])
        self.set_skill(trigger_ids=[924])
        self.set_skill(trigger_ids=[925])
        self.set_skill(trigger_ids=[926], enable=True)
        self.set_skill(trigger_ids=[927], enable=True)
        self.set_skill(trigger_ids=[928], enable=True)


initial_state = 시간표등록
