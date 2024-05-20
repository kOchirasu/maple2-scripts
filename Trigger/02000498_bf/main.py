""" trigger/02000498_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[500], visible=True)
        self.set_effect(trigger_ids=[501], visible=True)
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[610])
        self.set_effect(trigger_ids=[6010])
        self.set_effect(trigger_ids=[6011])
        self.set_effect(trigger_ids=[6012])
        self.set_effect(trigger_ids=[6013])
        self.set_effect(trigger_ids=[6015])
        self.set_effect(trigger_ids=[6016])
        self.set_effect(trigger_ids=[6017])
        self.set_effect(trigger_ids=[6018])
        self.set_effect(trigger_ids=[6019])
        self.set_effect(trigger_ids=[6020])
        self.set_effect(trigger_ids=[6021])
        self.set_effect(trigger_ids=[6022])
        self.set_effect(trigger_ids=[6023])
        self.set_effect(trigger_ids=[6024])
        self.set_effect(trigger_ids=[6025])
        self.set_effect(trigger_ids=[6026])
        self.set_effect(trigger_ids=[6027])
        self.set_effect(trigger_ids=[6028])
        self.set_effect(trigger_ids=[6029])
        self.set_effect(trigger_ids=[6030])
        self.set_effect(trigger_ids=[6031])
        self.set_effect(trigger_ids=[6032])
        self.set_effect(trigger_ids=[6110])
        self.set_effect(trigger_ids=[6111])
        self.set_effect(trigger_ids=[6112])
        self.set_effect(trigger_ids=[6113])
        self.set_effect(trigger_ids=[6101])
        self.set_skill(trigger_ids=[701])
        self.set_skill(trigger_ids=[702])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024], visible=True)
        self.set_mesh(trigger_ids=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012], visible=True)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100009]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[100009], skill_id=70000102, level=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100001]):
            return 시작연출(self.ctx)


class 시작연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6011], visible=True)
        self.set_effect(trigger_ids=[6012], visible=True)
        self.set_event_ui(type=1, arg2='다크스크림의 새로운 차원의 틈으로 진입 했습니다.', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100002]):
            return 시작연출_2(self.ctx)


class 시작연출_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6013], visible=True)
        self.set_effect(trigger_ids=[6010], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100003]):
            return 시작연출_3(self.ctx)


class 시작연출_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6023], visible=True)
        self.set_effect(trigger_ids=[6022], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100004]):
            return 시작연출_4(self.ctx)


class 시작연출_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6021], visible=True)
        self.set_effect(trigger_ids=[6024], visible=True)
        self.set_event_ui(type=1, arg2='더 가까이 다가가십시오.', arg3='3000')
        self.set_effect(trigger_ids=[500])
        self.set_effect(trigger_ids=[501])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100005]):
            return 시작연출_5(self.ctx)


class 시작연출_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6028], visible=True)
        self.set_effect(trigger_ids=[6027], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100006]):
            return 시작연출_6(self.ctx)


class 시작연출_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6025], visible=True)
        self.set_effect(trigger_ids=[6026], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100007]):
            return 시작연출_7(self.ctx)


class 시작연출_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6032], visible=True)
        self.set_effect(trigger_ids=[6029], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100008]):
            return 시작연출_8(self.ctx)


class 시작연출_8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6031], visible=True)
        self.set_effect(trigger_ids=[6030], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
