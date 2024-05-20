""" trigger/02000461_bf/madricansiege.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99999102, key='cannon02', value=0)
        self.set_user_value(trigger_id=99999103, key='cannon03', value=0)
        self.set_user_value(trigger_id=99999104, key='cannon04', value=0)
        self.set_user_value(trigger_id=99999105, key='cannon05', value=0)
        self.set_user_value(trigger_id=99999102, key='Bosscannon02', value=0)
        self.set_user_value(trigger_id=99999103, key='Bosscannon03', value=0)
        self.set_user_value(trigger_id=99999104, key='Bosscannon04', value=0)
        self.set_user_value(trigger_id=99999105, key='Bosscannon05', value=0)
        self.set_agent(trigger_ids=[8001,8002,8003,8004,8005,8006], visible=True)
        self.set_agent(trigger_ids=[8101,8102,8103,8104,8105,8106], visible=True)
        self.set_agent(trigger_ids=[8201,8202,8203,8204,8205,8206], visible=True)
        self.select_camera(trigger_id=300)
        self.set_portal(portal_id=1)
        self.spawn_monster(spawn_ids=[2000,2001], auto_target=False)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004], visible=True)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207], visible=True)
        self.set_mesh(trigger_ids=[3801,3802,3803,3804], visible=True)
        self.set_actor(trigger_id=201, initial_sequence='Dead_A')
        self.set_actor(trigger_id=202, initial_sequence='Dead_A')
        self.set_actor(trigger_id=203, initial_sequence='Dead_A')
        self.set_actor(trigger_id=204, initial_sequence='Dead_A')
        self.set_actor(trigger_id=205, initial_sequence='Dead_A')
        self.set_actor(trigger_id=206, initial_sequence='Dead_A')
        self.set_actor(trigger_id=207, initial_sequence='Dead_A')
        self.set_actor(trigger_id=208, initial_sequence='Dead_A')
        self.set_actor(trigger_id=209, initial_sequence='Dead_A')
        self.set_actor(trigger_id=210, initial_sequence='Dead_A')
        self.remove_buff(box_id=199, skill_id=99910150)
        self.set_interact_object(trigger_ids=[12000045], state=2)
        self.set_interact_object(trigger_ids=[12000046], state=2)
        self.set_interact_object(trigger_ids=[12000054], state=2)
        self.remove_buff(box_id=199, skill_id=99910140)
        self.set_interact_object(trigger_ids=[12000047], state=2)
        self.set_interact_object(trigger_ids=[12000048], state=2)
        self.set_interact_object(trigger_ids=[12000049], state=2)
        self.set_interact_object(trigger_ids=[12000050], state=2)
        self.set_interact_object(trigger_ids=[12000055], state=2)
        self.remove_buff(box_id=199, skill_id=99910130)
        self.set_interact_object(trigger_ids=[12000051], state=2)
        self.set_interact_object(trigger_ids=[12000052], state=2)
        self.set_interact_object(trigger_ids=[12000056], state=2)
        self.set_effect(trigger_ids=[601])
        self.remove_buff(box_id=199, skill_id=99910160)
        self.set_interact_object(trigger_ids=[12000053], state=2)
        self.set_interact_object(trigger_ids=[12000057], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004], fade=5.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 던전시작(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_agent(trigger_ids=[8001,8002,8003,8004,8005,8006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2000,2001]):
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105], fade=5.0)
            self.set_agent(trigger_ids=[8101,8102,8103,8104,8105,8106])
            return 차지원1(self.ctx)


class 차지원1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])
        self.spawn_monster(spawn_ids=[2002,2003,2004,2005], auto_target=False)
        self.set_user_value(trigger_id=99999101, key='cannon01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2901]):
            self.destroy_monster(spawn_ids=[2002])
            self.set_agent(trigger_ids=[8201,8202,8203,8204,8205,8206])
            self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207], fade=5.0)
            return 다리건넘(self.ctx)


class 다리건넘(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition_open_boss_gauge(max_gauge_point=1400)
        self.set_user_value(trigger_id=99999102, key='cannon02', value=1)
        self.set_user_value(trigger_id=99999103, key='cannon03', value=1)
        self.set_user_value(trigger_id=99999104, key='cannon04', value=1)
        self.set_user_value(trigger_id=99999105, key='cannon05', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 450:
            return 차지원2(self.ctx)


class 차지원2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[2021,2022,2023,2024,2025,2026,2027,2028,2029,2030])

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 700:
            return 차지원3(self.ctx)


class 차지원3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2031,2032,2033,2034,2035,2036], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 1400:
            self.shadow_expedition_close_boss_gauge()
            return 보스등장_딜레이(self.ctx)


class 보스등장_딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2901,2902,2903,2904,2905], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2099])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=2099, is_relative=True) <= 50:
            return 보스_버프패턴(self.ctx)


class 보스_버프패턴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000461_BF__MADRICANSIEGE__0$', arg3='5000')
        self.set_user_value(trigger_id=99999102, key='Bosscannon02', value=1)
        self.set_user_value(trigger_id=99999103, key='Bosscannon03', value=1)
        self.set_user_value(trigger_id=99999104, key='Bosscannon04', value=1)
        self.set_user_value(trigger_id=99999105, key='Bosscannon05', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 던전종료(self.ctx)


class 던전종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=199, type='trigger', achieve='Madracan01')
        self.set_achievement(trigger_id=199, type='trigger', achieve='ClearMadracanSiege')
        self.dungeon_clear()
        self.set_actor(trigger_id=201, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=202, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=203, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=204, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=205, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=206, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=207, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=208, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=209, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=210, visible=True, initial_sequence='Dead_A')
        self.set_user_value(trigger_id=99999099, key='DungeonClear', value=1)
        self.set_user_value(trigger_id=99999098, key='DungeonClear', value=1)
        self.set_user_value(trigger_id=99999097, key='DungeonClear', value=1)
        self.set_user_value(trigger_id=99999096, key='DungeonClear', value=1)
        self.set_user_value(trigger_id=99999102, key='DungeonClear', value=1)
        self.set_user_value(trigger_id=99999103, key='DungeonClear', value=1)
        self.set_user_value(trigger_id=99999104, key='DungeonClear', value=1)
        self.set_user_value(trigger_id=99999105, key='DungeonClear', value=1)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
