""" trigger/02020310_bf/field_5.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000322], state=2)
        self.set_interact_object(trigger_ids=[12000400], state=0)
        self.set_interact_object(trigger_ids=[12000401], state=0)
        self.set_interact_object(trigger_ids=[12000402], state=0)
        self.set_interact_object(trigger_ids=[12000403], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block') == 1:
            self.set_user_value(trigger_id=900006, key='Block', value=0)
            return Archeon_Ready(self.ctx)


class Archeon_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1117,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,1512,1513]):
            self.side_npc_talk(npc_id=11004607, illust='Neirin_normal', script='$02020310_BF__FIELD_5__0$', duration=5000)
            self.set_interact_object(trigger_ids=[12000400], state=1)
            self.set_interact_object(trigger_ids=[12000401], state=1)
            self.set_interact_object(trigger_ids=[12000402], state=1)
            self.set_interact_object(trigger_ids=[12000403], state=1)
            self.enable_spawn_point_pc(spawn_id=113)
            self.enable_spawn_point_pc(spawn_id=114)
            self.enable_spawn_point_pc(spawn_id=115)
            self.enable_spawn_point_pc(spawn_id=116, is_enable=True)
            return Archeon_On(self.ctx)


class Archeon_On(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000400,12000401,12000402,12000403], state=0):
            return Archeon_Move1_0(self.ctx)


class Archeon_Move1_0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # self.move_user_path(patrol_name='MS2PatrolData_01')
            self.set_portal(portal_id=10001, visible=True, enable=True, minimap_visible=True)
            self.set_portal(portal_id=10002, visible=True, enable=True, minimap_visible=True)
            self.set_portal(portal_id=10003, enable=True)
            self.set_portal(portal_id=10004, enable=True)
            self.patrol_condition_user(patrol_name='MS2PatrolData_01', patrol_index=1, additional_effect_id=73000005)
            self.patrol_condition_user(patrol_name='MS2PatrolData_02', patrol_index=2, additional_effect_id=73000006)
            self.patrol_condition_user(patrol_name='MS2PatrolData_03', patrol_index=3, additional_effect_id=73000007)
            self.patrol_condition_user(patrol_name='MS2PatrolData_04', patrol_index=4, additional_effect_id=73000008)
            self.spawn_monster(spawn_ids=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010], auto_target=False)
            self.spawn_monster(spawn_ids=[10011,10012,10013,10014,10015,10016,10017,10018,10019,10020], auto_target=False)
            self.spawn_monster(spawn_ids=[10021,10022,10023,10024,10025,10026,10027,10028,10029], auto_target=False)
            self.spawn_monster(spawn_ids=[11001,11002,11003,11004,11005,11006,11007,11008,11009,11010], auto_target=False)
            self.spawn_monster(spawn_ids=[11011,11012,11013,11014,11015,11016,11017,11018,11019,11020], auto_target=False)
            self.spawn_monster(spawn_ids=[11021,11022,11023,11024,11025,11026,11027,11028,11029], auto_target=False)
            return Archeon_Arrive(self.ctx)


class Archeon_Arrive(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,
        self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$02020310_BF__FIELD_5__1$', duration=6500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014,11015,11016,11017,11018,11019,11020,11021,11022,11023,11024,11025,11026,11027,11028,11029]):
            self.side_npc_talk(npc_id=11004582, illust='Eone_serious', script='$02020310_BF__FIELD_5__2$', duration=5000)
            self.patrol_condition_user(patrol_name='MS2PatrolData_05', patrol_index=5, additional_effect_id=73000005)
            self.patrol_condition_user(patrol_name='MS2PatrolData_06', patrol_index=6, additional_effect_id=73000006)
            self.patrol_condition_user(patrol_name='MS2PatrolData_07', patrol_index=7, additional_effect_id=73000007)
            self.patrol_condition_user(patrol_name='MS2PatrolData_08', patrol_index=8, additional_effect_id=73000008)
            self.enable_spawn_point_pc(spawn_id=116)
            self.enable_spawn_point_pc(spawn_id=117, is_enable=True)
            self.set_portal(portal_id=10000, visible=True, enable=True, minimap_visible=True)
            return Archeon_Move2_1(self.ctx)


class Archeon_Move2_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.set_portal(portal_id=10005, visible=True, enable=True, minimap_visible=True)
            self.set_portal(portal_id=10006, visible=True, enable=True, minimap_visible=True)
            self.set_portal(portal_id=10007, enable=True)
            self.set_portal(portal_id=10008, enable=True)
            return Archeon_Leave(self.ctx)


class Archeon_Leave(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9100]):
            return Archeon_OffDelay(self.ctx)


class Archeon_OffDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Archeon_Off(self.ctx)


class Archeon_Off(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9100], skill_id=73000009, level=1, ignore_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Archeon_OffDelay(self.ctx)


initial_state = 대기
