""" trigger/02000368_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100], visible=True)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147])
        self.set_interact_object(trigger_ids=[10000999], state=0)
        self.set_portal(portal_id=10)
        self.set_portal(portal_id=20)
        self.set_portal(portal_id=30)
        self.set_portal(portal_id=40)
        self.set_portal(portal_id=50)
        self.set_portal(portal_id=60)
        self.set_portal(portal_id=70)
        self.set_portal(portal_id=80)
        self.set_portal(portal_id=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1001]):
            return 전투감지(self.ctx)
        if self.user_detected(box_ids=[1002]):
            return 전투감지(self.ctx)


class 전투감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,111,201,211,301,311,401,411,501,511,601,611]):
            return 전투감지2(self.ctx)


class 전투감지2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102,202,302,402,502,602]):
            return 포털개방(self.ctx)


class 포털개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000999], state=1)
        self.set_portal(portal_id=10, visible=True, enable=True)
        self.set_portal(portal_id=20, visible=True, enable=True)
        self.set_portal(portal_id=30, visible=True, enable=True)
        self.set_portal(portal_id=40, visible=True, enable=True)
        self.set_portal(portal_id=50, visible=True, enable=True)
        self.set_portal(portal_id=60, visible=True, enable=True)
        self.set_portal(portal_id=70, visible=True, enable=True)
        self.set_portal(portal_id=80, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000999], state=0):
            return 다리생성(self.ctx)


class 다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3002,3003,3004,3005])
        self.set_mesh(trigger_ids=[3100])
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147], visible=True, interval=10)
        self.set_portal(portal_id=100, visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
