""" trigger/02000347_bf/fire.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050])
        self.set_skill(trigger_ids=[7001])
        self.set_skill(trigger_ids=[7002])
        self.set_skill(trigger_ids=[7003])
        self.set_skill(trigger_ids=[7004])
        self.set_skill(trigger_ids=[7005])
        self.set_skill(trigger_ids=[7006])
        self.set_skill(trigger_ids=[7007])
        self.set_skill(trigger_ids=[7008])
        self.set_skill(trigger_ids=[7009])
        self.set_skill(trigger_ids=[7010])
        self.set_skill(trigger_ids=[7011])
        self.set_skill(trigger_ids=[7012])
        self.set_skill(trigger_ids=[7013])
        self.set_skill(trigger_ids=[7014])
        self.set_skill(trigger_ids=[7015])
        self.set_skill(trigger_ids=[7016])
        self.set_skill(trigger_ids=[7017])
        self.set_skill(trigger_ids=[7018])
        self.set_skill(trigger_ids=[7019])
        self.set_skill(trigger_ids=[7020])
        self.set_skill(trigger_ids=[7021])
        self.set_skill(trigger_ids=[7022])
        self.set_skill(trigger_ids=[7023])
        self.set_skill(trigger_ids=[7024])
        self.set_skill(trigger_ids=[7025])
        self.set_skill(trigger_ids=[7026])
        self.set_skill(trigger_ids=[7027])
        self.set_skill(trigger_ids=[7028])
        self.set_skill(trigger_ids=[7029])
        self.set_skill(trigger_ids=[7030])
        self.set_skill(trigger_ids=[7031])
        self.set_skill(trigger_ids=[7032])
        self.set_skill(trigger_ids=[7033])
        self.set_skill(trigger_ids=[7034])
        self.set_skill(trigger_ids=[7035])
        self.set_skill(trigger_ids=[7036])
        self.set_skill(trigger_ids=[7037])
        self.set_skill(trigger_ids=[7038])
        self.set_skill(trigger_ids=[7039])
        self.set_skill(trigger_ids=[7040])
        self.set_skill(trigger_ids=[7041])
        self.set_skill(trigger_ids=[7042])
        self.set_skill(trigger_ids=[7043])
        self.set_skill(trigger_ids=[7044])
        self.set_skill(trigger_ids=[7045])
        self.set_skill(trigger_ids=[7046])
        self.set_skill(trigger_ids=[7047])
        self.set_skill(trigger_ids=[7048])
        self.set_skill(trigger_ids=[7049])
        self.set_skill(trigger_ids=[7050])
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[606])
        self.set_effect(trigger_ids=[607])
        self.set_effect(trigger_ids=[608])
        self.set_effect(trigger_ids=[609])
        self.set_effect(trigger_ids=[610])
        self.set_effect(trigger_ids=[611])
        self.set_effect(trigger_ids=[612])
        self.set_effect(trigger_ids=[613])
        self.set_effect(trigger_ids=[614])
        self.set_effect(trigger_ids=[615])
        self.set_effect(trigger_ids=[616])
        self.set_effect(trigger_ids=[617])
        self.set_effect(trigger_ids=[618])
        self.set_effect(trigger_ids=[619])
        self.set_effect(trigger_ids=[620])
        self.set_effect(trigger_ids=[621])
        self.set_effect(trigger_ids=[622])
        self.set_effect(trigger_ids=[623])
        self.set_effect(trigger_ids=[624])
        self.set_effect(trigger_ids=[625])
        self.set_effect(trigger_ids=[626])
        self.set_effect(trigger_ids=[627])
        self.set_effect(trigger_ids=[628])
        self.set_effect(trigger_ids=[629])
        self.set_effect(trigger_ids=[630])
        self.set_effect(trigger_ids=[631])
        self.set_effect(trigger_ids=[632])
        self.set_effect(trigger_ids=[633])
        self.set_effect(trigger_ids=[634])
        self.set_effect(trigger_ids=[635])
        self.set_effect(trigger_ids=[636])
        self.set_effect(trigger_ids=[637])
        self.set_effect(trigger_ids=[638])
        self.set_effect(trigger_ids=[639])
        self.set_effect(trigger_ids=[640])
        self.set_effect(trigger_ids=[641])
        self.set_effect(trigger_ids=[642])
        self.set_effect(trigger_ids=[643])
        self.set_effect(trigger_ids=[644])
        self.set_effect(trigger_ids=[645])
        self.set_effect(trigger_ids=[646])
        self.set_effect(trigger_ids=[647])
        self.set_effect(trigger_ids=[648])
        self.set_effect(trigger_ids=[649])
        self.set_effect(trigger_ids=[650])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[60002]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050], interval=2)
        self.set_skill(trigger_ids=[7001])
        self.set_skill(trigger_ids=[7002])
        self.set_skill(trigger_ids=[7003])
        self.set_skill(trigger_ids=[7004])
        self.set_skill(trigger_ids=[7005])
        self.set_skill(trigger_ids=[7006])
        self.set_skill(trigger_ids=[7007])
        self.set_skill(trigger_ids=[7008])
        self.set_skill(trigger_ids=[7009])
        self.set_skill(trigger_ids=[7010])
        self.set_skill(trigger_ids=[7011])
        self.set_skill(trigger_ids=[7012])
        self.set_skill(trigger_ids=[7013])
        self.set_skill(trigger_ids=[7014])
        self.set_skill(trigger_ids=[7015])
        self.set_skill(trigger_ids=[7016])
        self.set_skill(trigger_ids=[7017])
        self.set_skill(trigger_ids=[7018])
        self.set_skill(trigger_ids=[7019])
        self.set_skill(trigger_ids=[7020])
        self.set_skill(trigger_ids=[7021])
        self.set_skill(trigger_ids=[7022])
        self.set_skill(trigger_ids=[7023])
        self.set_skill(trigger_ids=[7024])
        self.set_skill(trigger_ids=[7025])
        self.set_skill(trigger_ids=[7026])
        self.set_skill(trigger_ids=[7027])
        self.set_skill(trigger_ids=[7028])
        self.set_skill(trigger_ids=[7029])
        self.set_skill(trigger_ids=[7030])
        self.set_skill(trigger_ids=[7031])
        self.set_skill(trigger_ids=[7032])
        self.set_skill(trigger_ids=[7033])
        self.set_skill(trigger_ids=[7034])
        self.set_skill(trigger_ids=[7035])
        self.set_skill(trigger_ids=[7036])
        self.set_skill(trigger_ids=[7037])
        self.set_skill(trigger_ids=[7038])
        self.set_skill(trigger_ids=[7039])
        self.set_skill(trigger_ids=[7040])
        self.set_skill(trigger_ids=[7041])
        self.set_skill(trigger_ids=[7042])
        self.set_skill(trigger_ids=[7043])
        self.set_skill(trigger_ids=[7044])
        self.set_skill(trigger_ids=[7045])
        self.set_skill(trigger_ids=[7046])
        self.set_skill(trigger_ids=[7047])
        self.set_skill(trigger_ids=[7048])
        self.set_skill(trigger_ids=[7049])
        self.set_skill(trigger_ids=[7050])
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[606])
        self.set_effect(trigger_ids=[607])
        self.set_effect(trigger_ids=[608])
        self.set_effect(trigger_ids=[609])
        self.set_effect(trigger_ids=[610])
        self.set_effect(trigger_ids=[611])
        self.set_effect(trigger_ids=[612])
        self.set_effect(trigger_ids=[613])
        self.set_effect(trigger_ids=[614])
        self.set_effect(trigger_ids=[615])
        self.set_effect(trigger_ids=[616])
        self.set_effect(trigger_ids=[617])
        self.set_effect(trigger_ids=[618])
        self.set_effect(trigger_ids=[619])
        self.set_effect(trigger_ids=[620])
        self.set_effect(trigger_ids=[621])
        self.set_effect(trigger_ids=[622])
        self.set_effect(trigger_ids=[623])
        self.set_effect(trigger_ids=[624])
        self.set_effect(trigger_ids=[625])
        self.set_effect(trigger_ids=[626])
        self.set_effect(trigger_ids=[627])
        self.set_effect(trigger_ids=[628])
        self.set_effect(trigger_ids=[629])
        self.set_effect(trigger_ids=[630])
        self.set_effect(trigger_ids=[631])
        self.set_effect(trigger_ids=[632])
        self.set_effect(trigger_ids=[633])
        self.set_effect(trigger_ids=[634])
        self.set_effect(trigger_ids=[635])
        self.set_effect(trigger_ids=[636])
        self.set_effect(trigger_ids=[637])
        self.set_effect(trigger_ids=[638])
        self.set_effect(trigger_ids=[639])
        self.set_effect(trigger_ids=[640])
        self.set_effect(trigger_ids=[641])
        self.set_effect(trigger_ids=[642])
        self.set_effect(trigger_ids=[643])
        self.set_effect(trigger_ids=[644])
        self.set_effect(trigger_ids=[645])
        self.set_effect(trigger_ids=[646])
        self.set_effect(trigger_ids=[647])
        self.set_effect(trigger_ids=[648])
        self.set_effect(trigger_ids=[649])
        self.set_effect(trigger_ids=[650])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 랜덤스킬작동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=2.0):
            return 번생성1(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성2(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성3(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성4(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성5(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성6(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성7(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성8(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성9(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성10(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성11(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성12(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성13(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성14(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성15(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성16(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성17(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성18(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성19(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성20(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성21(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성22(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성23(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성24(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성25(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성26(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성27(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성28(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성29(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성30(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성31(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성32(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성33(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성34(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성35(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성36(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성37(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성38(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성39(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성40(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성41(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성42(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성43(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성44(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성45(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성46(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성47(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성48(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성49(self.ctx)
        if self.random_condition(weight=2.0):
            return 번생성50(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)


class 번생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7001], enable=True)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_mesh(trigger_ids=[3001], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7002], enable=True)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_mesh(trigger_ids=[3002], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7003], enable=True)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_mesh(trigger_ids=[3003], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7004], enable=True)
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_mesh(trigger_ids=[3004], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7005], enable=True)
        self.set_effect(trigger_ids=[605], visible=True)
        self.set_mesh(trigger_ids=[3005], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7006], enable=True)
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_mesh(trigger_ids=[3006], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7007], enable=True)
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_mesh(trigger_ids=[3007], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7008], enable=True)
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_mesh(trigger_ids=[3008], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7009], enable=True)
        self.set_effect(trigger_ids=[609], visible=True)
        self.set_mesh(trigger_ids=[3009], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7010], enable=True)
        self.set_effect(trigger_ids=[610], visible=True)
        self.set_mesh(trigger_ids=[3010], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7011], enable=True)
        self.set_effect(trigger_ids=[611], visible=True)
        self.set_mesh(trigger_ids=[3011], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7012], enable=True)
        self.set_effect(trigger_ids=[612], visible=True)
        self.set_mesh(trigger_ids=[3012], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7013], enable=True)
        self.set_effect(trigger_ids=[613], visible=True)
        self.set_mesh(trigger_ids=[3013], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7014], enable=True)
        self.set_effect(trigger_ids=[614], visible=True)
        self.set_mesh(trigger_ids=[3014], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7015], enable=True)
        self.set_effect(trigger_ids=[615], visible=True)
        self.set_mesh(trigger_ids=[3015], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7016], enable=True)
        self.set_effect(trigger_ids=[616], visible=True)
        self.set_mesh(trigger_ids=[3016], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7017], enable=True)
        self.set_effect(trigger_ids=[617], visible=True)
        self.set_mesh(trigger_ids=[3017], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7018], enable=True)
        self.set_effect(trigger_ids=[618], visible=True)
        self.set_mesh(trigger_ids=[3018], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7019], enable=True)
        self.set_effect(trigger_ids=[619], visible=True)
        self.set_mesh(trigger_ids=[3019], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7020], enable=True)
        self.set_effect(trigger_ids=[620], visible=True)
        self.set_mesh(trigger_ids=[3020], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7021], enable=True)
        self.set_effect(trigger_ids=[621], visible=True)
        self.set_mesh(trigger_ids=[3021], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7022], enable=True)
        self.set_effect(trigger_ids=[622], visible=True)
        self.set_mesh(trigger_ids=[3022], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7023], enable=True)
        self.set_effect(trigger_ids=[623], visible=True)
        self.set_mesh(trigger_ids=[3023], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7024], enable=True)
        self.set_effect(trigger_ids=[624], visible=True)
        self.set_mesh(trigger_ids=[3024], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7025], enable=True)
        self.set_effect(trigger_ids=[625], visible=True)
        self.set_mesh(trigger_ids=[3025], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7026], enable=True)
        self.set_effect(trigger_ids=[626], visible=True)
        self.set_mesh(trigger_ids=[3026], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7027], enable=True)
        self.set_effect(trigger_ids=[627], visible=True)
        self.set_mesh(trigger_ids=[3027], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7028], enable=True)
        self.set_effect(trigger_ids=[628], visible=True)
        self.set_mesh(trigger_ids=[3028], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7029], enable=True)
        self.set_effect(trigger_ids=[629], visible=True)
        self.set_mesh(trigger_ids=[3029], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7030], enable=True)
        self.set_effect(trigger_ids=[630], visible=True)
        self.set_mesh(trigger_ids=[3030], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7031], enable=True)
        self.set_effect(trigger_ids=[631], visible=True)
        self.set_mesh(trigger_ids=[3031], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7032], enable=True)
        self.set_effect(trigger_ids=[632], visible=True)
        self.set_mesh(trigger_ids=[3032], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7033], enable=True)
        self.set_effect(trigger_ids=[633], visible=True)
        self.set_mesh(trigger_ids=[3033], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7034], enable=True)
        self.set_effect(trigger_ids=[634], visible=True)
        self.set_mesh(trigger_ids=[3034], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7035], enable=True)
        self.set_effect(trigger_ids=[635], visible=True)
        self.set_mesh(trigger_ids=[3035], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성36(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7036], enable=True)
        self.set_effect(trigger_ids=[636], visible=True)
        self.set_mesh(trigger_ids=[3036], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성37(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7037], enable=True)
        self.set_effect(trigger_ids=[637], visible=True)
        self.set_mesh(trigger_ids=[3037], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성38(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7038], enable=True)
        self.set_effect(trigger_ids=[638], visible=True)
        self.set_mesh(trigger_ids=[3038], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성39(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7039], enable=True)
        self.set_effect(trigger_ids=[639], visible=True)
        self.set_mesh(trigger_ids=[3039], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7040], enable=True)
        self.set_effect(trigger_ids=[640], visible=True)
        self.set_mesh(trigger_ids=[3040], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7041], enable=True)
        self.set_effect(trigger_ids=[641], visible=True)
        self.set_mesh(trigger_ids=[3041], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성42(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7042], enable=True)
        self.set_effect(trigger_ids=[642], visible=True)
        self.set_mesh(trigger_ids=[3042], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성43(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7043], enable=True)
        self.set_effect(trigger_ids=[643], visible=True)
        self.set_mesh(trigger_ids=[3043], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성44(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7044], enable=True)
        self.set_effect(trigger_ids=[644], visible=True)
        self.set_mesh(trigger_ids=[3044], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성45(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7045], enable=True)
        self.set_effect(trigger_ids=[645], visible=True)
        self.set_mesh(trigger_ids=[3045], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성46(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7046], enable=True)
        self.set_effect(trigger_ids=[646], visible=True)
        self.set_mesh(trigger_ids=[3046], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성47(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7047], enable=True)
        self.set_effect(trigger_ids=[647], visible=True)
        self.set_mesh(trigger_ids=[3047], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성48(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7048], enable=True)
        self.set_effect(trigger_ids=[648], visible=True)
        self.set_mesh(trigger_ids=[3048], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성49(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7049], enable=True)
        self.set_effect(trigger_ids=[649], visible=True)
        self.set_mesh(trigger_ids=[3049], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 번생성50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7050], enable=True)
        self.set_effect(trigger_ids=[650], visible=True)
        self.set_mesh(trigger_ids=[3050], visible=True, interval=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 랜덤스킬작동(self.ctx)
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7001])
        self.set_skill(trigger_ids=[7002])
        self.set_skill(trigger_ids=[7003])
        self.set_skill(trigger_ids=[7004])
        self.set_skill(trigger_ids=[7005])
        self.set_skill(trigger_ids=[7006])
        self.set_skill(trigger_ids=[7007])
        self.set_skill(trigger_ids=[7008])
        self.set_skill(trigger_ids=[7009])
        self.set_skill(trigger_ids=[7010])
        self.set_skill(trigger_ids=[7011])
        self.set_skill(trigger_ids=[7012])
        self.set_skill(trigger_ids=[7013])
        self.set_skill(trigger_ids=[7014])
        self.set_skill(trigger_ids=[7015])
        self.set_skill(trigger_ids=[7016])
        self.set_skill(trigger_ids=[7017])
        self.set_skill(trigger_ids=[7018])
        self.set_skill(trigger_ids=[7019])
        self.set_skill(trigger_ids=[7020])
        self.set_skill(trigger_ids=[7021])
        self.set_skill(trigger_ids=[7022])
        self.set_skill(trigger_ids=[7023])
        self.set_skill(trigger_ids=[7024])
        self.set_skill(trigger_ids=[7025])
        self.set_skill(trigger_ids=[7026])
        self.set_skill(trigger_ids=[7027])
        self.set_skill(trigger_ids=[7028])
        self.set_skill(trigger_ids=[7029])
        self.set_skill(trigger_ids=[7030])
        self.set_skill(trigger_ids=[7031])
        self.set_skill(trigger_ids=[7032])
        self.set_skill(trigger_ids=[7033])
        self.set_skill(trigger_ids=[7034])
        self.set_skill(trigger_ids=[7035])
        self.set_skill(trigger_ids=[7036])
        self.set_skill(trigger_ids=[7037])
        self.set_skill(trigger_ids=[7038])
        self.set_skill(trigger_ids=[7039])
        self.set_skill(trigger_ids=[7040])
        self.set_skill(trigger_ids=[7041])
        self.set_skill(trigger_ids=[7042])
        self.set_skill(trigger_ids=[7043])
        self.set_skill(trigger_ids=[7044])
        self.set_skill(trigger_ids=[7045])
        self.set_skill(trigger_ids=[7046])
        self.set_skill(trigger_ids=[7047])
        self.set_skill(trigger_ids=[7048])
        self.set_skill(trigger_ids=[7049])
        self.set_skill(trigger_ids=[7050])
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[606])
        self.set_effect(trigger_ids=[607])
        self.set_effect(trigger_ids=[608])
        self.set_effect(trigger_ids=[609])
        self.set_effect(trigger_ids=[610])
        self.set_effect(trigger_ids=[611])
        self.set_effect(trigger_ids=[612])
        self.set_effect(trigger_ids=[613])
        self.set_effect(trigger_ids=[614])
        self.set_effect(trigger_ids=[615])
        self.set_effect(trigger_ids=[616])
        self.set_effect(trigger_ids=[617])
        self.set_effect(trigger_ids=[618])
        self.set_effect(trigger_ids=[619])
        self.set_effect(trigger_ids=[620])
        self.set_effect(trigger_ids=[621])
        self.set_effect(trigger_ids=[622])
        self.set_effect(trigger_ids=[623])
        self.set_effect(trigger_ids=[624])
        self.set_effect(trigger_ids=[625])
        self.set_effect(trigger_ids=[626])
        self.set_effect(trigger_ids=[627])
        self.set_effect(trigger_ids=[628])
        self.set_effect(trigger_ids=[629])
        self.set_effect(trigger_ids=[630])
        self.set_effect(trigger_ids=[631])
        self.set_effect(trigger_ids=[632])
        self.set_effect(trigger_ids=[633])
        self.set_effect(trigger_ids=[634])
        self.set_effect(trigger_ids=[635])
        self.set_effect(trigger_ids=[636])
        self.set_effect(trigger_ids=[637])
        self.set_effect(trigger_ids=[638])
        self.set_effect(trigger_ids=[639])
        self.set_effect(trigger_ids=[640])
        self.set_effect(trigger_ids=[641])
        self.set_effect(trigger_ids=[642])
        self.set_effect(trigger_ids=[643])
        self.set_effect(trigger_ids=[644])
        self.set_effect(trigger_ids=[645])
        self.set_effect(trigger_ids=[646])
        self.set_effect(trigger_ids=[647])
        self.set_effect(trigger_ids=[648])
        self.set_effect(trigger_ids=[649])
        self.set_effect(trigger_ids=[650])


initial_state = 대기
