""" trigger/02000006_ad/01_followallice.xml """
import trigger_api


class 대기00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[51,52,53,54])
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118])
        self.set_effect(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218])
        self.set_ladder(trigger_ids=[151])
        self.set_ladder(trigger_ids=[152])
        self.set_ladder(trigger_ids=[153])
        self.set_ladder(trigger_ids=[154])
        self.set_ladder(trigger_ids=[155])
        self.set_ladder(trigger_ids=[156])
        self.set_effect(trigger_ids=[219,220,221,222,223,224])
        self.set_interact_object(trigger_ids=[10000449], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000449], state=0):
            return 대기01(self.ctx)


class 대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[51])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[51]):
            return 발판생성01(self.ctx)


class 몬스터수명설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기01(self.ctx)


class 발판생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101], visible=True)
        self.set_effect(trigger_ids=[201], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성02(self.ctx)


class 발판생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[102], visible=True)
        self.set_effect(trigger_ids=[202], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성03(self.ctx)


class 발판생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[103], visible=True)
        self.set_effect(trigger_ids=[203], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성04(self.ctx)


class 발판생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[104], visible=True)
        self.set_effect(trigger_ids=[204], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성05(self.ctx)


class 발판생성05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[105], visible=True)
        self.set_effect(trigger_ids=[205], visible=True)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기02(self.ctx)


class 대기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[52])
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118])
        self.set_effect(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218])
        self.set_timer(timer_id='2', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[52]):
            return 발판생성06(self.ctx)
        if self.time_expired(timer_id='2'):
            return 대기00(self.ctx)


class 발판생성06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[106], visible=True)
        self.set_effect(trigger_ids=[206], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성07(self.ctx)


class 발판생성07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[107], visible=True)
        self.set_effect(trigger_ids=[207], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성08(self.ctx)


class 발판생성08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[108], visible=True)
        self.set_effect(trigger_ids=[208], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성09(self.ctx)


class 발판생성09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[109], visible=True)
        self.set_effect(trigger_ids=[209], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성10(self.ctx)


class 발판생성10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[110], visible=True)
        self.set_effect(trigger_ids=[210], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성11(self.ctx)


class 발판생성11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[111], visible=True)
        self.set_effect(trigger_ids=[211], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성12(self.ctx)


class 발판생성12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], visible=True)
        self.set_effect(trigger_ids=[212], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성13(self.ctx)


class 발판생성13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], visible=True)
        self.set_effect(trigger_ids=[213], visible=True)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기03(self.ctx)


class 대기03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[53])
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118])
        self.set_effect(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218])
        self.set_timer(timer_id='2', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[53]):
            return 발판생성14(self.ctx)
        if self.time_expired(timer_id='2'):
            return 대기00(self.ctx)


class 발판생성14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], visible=True)
        self.set_effect(trigger_ids=[214], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성15(self.ctx)


class 발판생성15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], visible=True)
        self.set_effect(trigger_ids=[215], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성16(self.ctx)


class 발판생성16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[116], visible=True)
        self.set_effect(trigger_ids=[216], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성17(self.ctx)


class 발판생성17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[117], visible=True)
        self.set_effect(trigger_ids=[217], visible=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발판생성18(self.ctx)


class 발판생성18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[118], visible=True)
        self.set_effect(trigger_ids=[218], visible=True)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기04(self.ctx)


class 대기04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[54])
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118])
        self.set_effect(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218])
        self.set_timer(timer_id='2', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[54]):
            return 사다리등장(self.ctx)
        if self.time_expired(timer_id='2'):
            return 대기00(self.ctx)


class 사다리등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[151], visible=True, enable=True)
        self.set_ladder(trigger_ids=[152], visible=True, enable=True)
        self.set_ladder(trigger_ids=[153], visible=True, enable=True)
        self.set_ladder(trigger_ids=[154], visible=True, enable=True)
        self.set_ladder(trigger_ids=[155], visible=True, enable=True)
        self.set_ladder(trigger_ids=[156], visible=True, enable=True)
        self.set_effect(trigger_ids=[219,220,221,222,223,224], visible=True)
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기00(self.ctx)


initial_state = 대기00
