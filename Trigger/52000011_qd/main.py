""" trigger/52000011_qd/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036,7037,7038,7039,7040,7041], enable=True)
        self.set_breakable(trigger_ids=[7101,7102,7103,7104,7105,7106,7107,7108,7109,7110,7111,7112,7113,7114,7115,7116,7117,7118,7119,7120,7121,7122,7123,7124,7125,7126,7127,7128,7129,7130,7131,7132,7133,7134,7135,7136,7137,7138,7139,7140,7141,7142,7143,7144,7145,7146,7147,7148,7149,7150,7151,7152,7153,7154,7155,7156,7157,7158,7159,7160,7161,7162,7163,7164,7165,7166,7167,7168,7169,7170], enable=True)
        self.set_breakable(trigger_ids=[7201,7202,7203,7204,7205,7206,7207,7208,7209,7210,7211,7212,7213,7214,7215,7216,7217,7218,7219,7220,7221,7222,7223,7224,7225,7226,7227,7228,7229,7230,7231,7232,7233,7234,7235,7236,7237,7238,7239,7240,7241,7242,7243,7244,7245,7246,7247,7248,7249,7250,7251,7252,7253,7254,7255,7256,7257,7258,7259,7260,7261,7262,7263,7264,7265,7266,7267,7268,7269,7270], enable=True)
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=204, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=206, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=207, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=208, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3001], visible=True)
        self.set_mesh(trigger_ids=[3002], visible=True)
        self.set_mesh(trigger_ids=[3003], visible=True)
        self.set_mesh(trigger_ids=[3004], visible=True)
        self.set_portal(portal_id=2)
        self.set_agent(trigger_ids=[9001], visible=True)
        self.set_agent(trigger_ids=[9002], visible=True)
        self.set_agent(trigger_ids=[9003], visible=True)
        self.set_agent(trigger_ids=[9004], visible=True)
        self.set_agent(trigger_ids=[9005], visible=True)
        self.set_agent(trigger_ids=[9006], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[101], quest_ids=[10002594], quest_states=[1]):
            return 연출시작딜레이(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 연출시작딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 오스칼01(self.ctx)


class 오스칼01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[302])
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=2, spawn_id=11000015, script='$52000011_QD__MAIN__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 오스칼02(self.ctx)


class 오스칼02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.set_dialogue(type=2, spawn_id=11000015, script='$52000011_QD__MAIN__1$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return NPC교체(self.ctx)


class NPC교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2002], auto_target=False)
        self.destroy_monster(spawn_ids=[2001])
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3001])
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[2002]):
            return 몬스터생성01(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 몬스터생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=202, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[1001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1001]):
            return 몬스터생성02(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 몬스터생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1002]):
            return 문열림02(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 문열림02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9001])
        self.set_agent(trigger_ids=[9002])
        self.set_breakable(trigger_ids=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036,7037,7038,7039,7040,7041])
        self.set_actor(trigger_id=203, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3002])
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=103, spawn_ids=[2002]):
            return 몬스터생성03(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 몬스터생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=204, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[1003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1003]):
            return 몬스터생성04(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 몬스터생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1004]):
            return 문열림03(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 문열림03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9003])
        self.set_agent(trigger_ids=[9004])
        self.set_breakable(trigger_ids=[7101,7102,7103,7104,7105,7106,7107,7108,7109,7110,7111,7112,7113,7114,7115,7116,7117,7118,7119,7120,7121,7122,7123,7124,7125,7126,7127,7128,7129,7130,7131,7132,7133,7134,7135,7136,7137,7138,7139,7140,7141,7142,7143,7144,7145,7146,7147,7148,7149,7150,7151,7152,7153,7154,7155,7156,7157,7158,7159,7160,7161,7162,7163,7164,7165,7166,7167,7168,7169,7170])
        self.set_actor(trigger_id=205, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3003])
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=104, spawn_ids=[2002]):
            return 몬스터생성05(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 몬스터생성05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=206, visible=True, initial_sequence='Opened')
        self.spawn_monster(spawn_ids=[1005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1005]):
            return 몬스터생성06(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 몬스터생성06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1006]):
            return 문열림04(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 문열림04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9005])
        self.set_agent(trigger_ids=[9006])
        self.set_breakable(trigger_ids=[7201,7202,7203,7204,7205,7206,7207,7208,7209,7210,7211,7212,7213,7214,7215,7216,7217,7218,7219,7220,7221,7222,7223,7224,7225,7226,7227,7228,7229,7230,7231,7232,7233,7234,7235,7236,7237,7238,7239,7240,7241,7242,7243,7244,7245,7246,7247,7248,7249,7250,7251,7252,7253,7254,7255,7256,7257,7258,7259,7260,7261,7262,7263,7264,7265,7266,7267,7268,7269,7270])
        self.set_actor(trigger_id=207, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3004])
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=105, spawn_ids=[2002]):
            return 문열림05(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 문열림05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=208, visible=True, initial_sequence='Opened')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=106, spawn_ids=[2002]):
            return NPC교체2(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class NPC교체2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2003], auto_target=False)
        self.destroy_monster(spawn_ids=[2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[10002595], quest_states=[2]):
            return 포털생성(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=30)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            self.move_user(map_id=2000309, portal_id=2, box_id=199)
            return 종료(self.ctx)
        if not self.user_detected(box_ids=[199]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,2001,2002,2003])

    def on_tick(self) -> trigger_api.Trigger:
        return 시작(self.ctx)


initial_state = 시작
