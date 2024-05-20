""" trigger/52000014_qd/meteo_7700.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[7700,7701,7702,7703,7704,7705,7706,7707,7708,7709])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 랜덤생성01(self.ctx)


class 랜덤생성01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 패턴01생성01(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴02생성01(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴03생성01(self.ctx)
        if self.random_condition(weight=25.0):
            return 패턴04생성01(self.ctx)


# 패턴01
class 패턴01생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_mesh(trigger_ids=[7700], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 패턴01낙하01(self.ctx)


class 패턴01낙하01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=1)
        self.set_mesh(trigger_ids=[7700], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 패턴01생성02(self.ctx)


class 패턴01생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=1)
        self.set_mesh(trigger_ids=[7702], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 패턴01낙하02(self.ctx)


class 패턴01낙하02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=1)
        self.set_mesh(trigger_ids=[7702], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 패턴01생성03(self.ctx)


class 패턴01생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=1)
        self.set_mesh(trigger_ids=[7707], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 패턴01낙하03(self.ctx)


class 패턴01낙하03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=1)
        self.set_mesh(trigger_ids=[7707], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 딜레이랜덤01(self.ctx)


# 패턴02
class 패턴02생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=1)
        self.set_mesh(trigger_ids=[7702], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 패턴02낙하01(self.ctx)


class 패턴02낙하01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=1)
        self.set_mesh(trigger_ids=[7702], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 패턴02생성02(self.ctx)


class 패턴02생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='13', seconds=1)
        self.set_mesh(trigger_ids=[7704], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='13'):
            return 패턴02낙하02(self.ctx)


class 패턴02낙하02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='14', seconds=1)
        self.set_mesh(trigger_ids=[7704], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 패턴02생성03(self.ctx)


class 패턴02생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=1)
        self.set_mesh(trigger_ids=[7708], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 패턴02낙하03(self.ctx)


class 패턴02낙하03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='16', seconds=1)
        self.set_mesh(trigger_ids=[7708], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='16'):
            return 딜레이랜덤01(self.ctx)


# 패턴03
class 패턴03생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='21', seconds=1)
        self.set_mesh(trigger_ids=[7709], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='21'):
            return 패턴03낙하01(self.ctx)


class 패턴03낙하01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='22', seconds=1)
        self.set_mesh(trigger_ids=[7709], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='22'):
            return 패턴03생성02(self.ctx)


class 패턴03생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='23', seconds=1)
        self.set_mesh(trigger_ids=[7706], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='23'):
            return 패턴03낙하02(self.ctx)


class 패턴03낙하02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='24', seconds=1)
        self.set_mesh(trigger_ids=[7706], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='24'):
            return 패턴03생성03(self.ctx)


class 패턴03생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='25', seconds=1)
        self.set_mesh(trigger_ids=[7703], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='25'):
            return 패턴03낙하03(self.ctx)


class 패턴03낙하03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='26', seconds=1)
        self.set_mesh(trigger_ids=[7703], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='26'):
            return 패턴03생성04(self.ctx)


class 패턴03생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='27', seconds=1)
        self.set_mesh(trigger_ids=[7708], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='27'):
            return 패턴03낙하04(self.ctx)


class 패턴03낙하04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='28', seconds=1)
        self.set_mesh(trigger_ids=[7708], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='28'):
            return 딜레이랜덤01(self.ctx)


# 패턴04
class 패턴04생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='31', seconds=1)
        self.set_mesh(trigger_ids=[7701], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='31'):
            return 패턴04낙하01(self.ctx)


class 패턴04낙하01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='32', seconds=1)
        self.set_mesh(trigger_ids=[7701], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='32'):
            return 패턴04생성02(self.ctx)


class 패턴04생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='33', seconds=1)
        self.set_mesh(trigger_ids=[7705], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='33'):
            return 패턴04낙하02(self.ctx)


class 패턴04낙하02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='34', seconds=1)
        self.set_mesh(trigger_ids=[7705], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='34'):
            return 패턴04생성03(self.ctx)


class 패턴04생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='35', seconds=1)
        self.set_mesh(trigger_ids=[7708], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='35'):
            return 패턴04낙하03(self.ctx)


class 패턴04낙하03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='36', seconds=1)
        self.set_mesh(trigger_ids=[7708], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='36'):
            return 패턴04생성04(self.ctx)


class 패턴04생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='37', seconds=1)
        self.set_mesh(trigger_ids=[7709], visible=True, fade=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='37'):
            return 패턴04낙하04(self.ctx)


class 패턴04낙하04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='38', seconds=1)
        self.set_mesh(trigger_ids=[7709], fade=500.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='38'):
            return 딜레이랜덤01(self.ctx)


class 딜레이랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return 딜레이01(self.ctx)
        if self.random_condition(weight=25.0):
            return 딜레이02(self.ctx)
        if self.random_condition(weight=25.0):
            return 딜레이03(self.ctx)
        if self.random_condition(weight=25.0):
            return 딜레이04(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='100', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='100'):
            return 초기화(self.ctx)


class 딜레이02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='101', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='101'):
            return 초기화(self.ctx)


class 딜레이03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='102', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='102'):
            return 초기화(self.ctx)


class 딜레이04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='103', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='103'):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='200', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='200'):
            return 랜덤생성01(self.ctx)


initial_state = 대기
