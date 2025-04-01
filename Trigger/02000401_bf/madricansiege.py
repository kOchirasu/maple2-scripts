""" trigger/02000401_bf/madricansiege.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8001,8002,8003,8004,8005,8006], visible=True)
        self.set_agent(trigger_ids=[8101,8102,8103,8104,8105,8106], visible=True)
        self.set_agent(trigger_ids=[8201,8202,8203,8204,8205,8206], visible=True)
        self.select_camera(trigger_id=300)
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004], visible=True)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105], visible=True)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207], visible=True)
        self.set_mesh(trigger_ids=[3801,3802,3803,3804], visible=True)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005], auto_target=False)
        self.spawn_monster(spawn_ids=[2000,2001], auto_target=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=연출종료)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_dialogue(type=2, spawn_id=11000015, script='$02000401_BF__MADRICANSIEGE__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004], fade=5.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=300, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 던전시작(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_agent(trigger_ids=[8001,8002,8003,8004,8005,8006])
        self.set_dialogue(type=1, spawn_id=1001, script='$02000401_BF__MADRICANSIEGE__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2000,2001]):
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105], fade=5.0)
            self.set_agent(trigger_ids=[8101,8102,8103,8104,8105,8106])
            self.move_npc(spawn_id=1102, patrol_name='MS2PatrolData_1001A')
            return 차지원1(self.ctx)


class 차지원1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(range_ids=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030])
        self.spawn_monster(spawn_ids=[2002,2003,2004,2005], auto_target=False)
        self.set_user_value(trigger_id=99999101, key='cannon01', value=1)
        self.set_user_value(trigger_id=99999099, key='faction01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2901]):
            self.destroy_monster(spawn_ids=[2002])
            # 좀더 빠른 타이밍에 OpenBossGauge 최초 초기화 설정 하기
            self.shadow_expedition_open_boss_gauge(max_gauge_point=1000)
            # OpenBossGauge = 1000은 100% 초기화 설정하기 전에 몬스터를 잡으면 로직이 꼬여서 몬스터를 다 죽여도 100%가 되지 못하는 버그가 발생할 수 있어, 이거 초기화 후 1.3초 대기후 진행하도록 함
            return 잠시대기(self.ctx)


class 잠시대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1300):
            # 최초 OpenBossGauge 값 초기화 설정하고 잠시 1.3초 대기 후에 이후 진행하도록 설정함
            return 다리건넘(self.ctx)


class 다리건넘(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터가 넘어오지 못하게 잠시 TOK길 막았던 벽 해제하기
        self.set_agent(trigger_ids=[8201,8202,8203,8204,8205,8206])
        # 플레이어가 넘어가지 못하게 막았던 트리거메쉬 벽 해제하기
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207], fade=5.0)
        self.set_user_value(trigger_id=99999102, key='cannon02', value=1)
        self.set_user_value(trigger_id=99999103, key='cannon03', value=1)
        self.set_user_value(trigger_id=99999104, key='cannon04', value=1)
        self.set_user_value(trigger_id=99999105, key='cannon05', value=1)
        # self.spawn_monster(spawn_ids=[2101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 300:
            return 차지원2(self.ctx)


class 차지원2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99999098, key='faction02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 600:
            return 차지원3(self.ctx)


class 차지원3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2031,2032,2033,2034,2035,2036], auto_target=False)
        self.set_user_value(trigger_id=99999097, key='faction03', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 1000:
            self.shadow_expedition_close_boss_gauge()
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2026,2027,2028,2029,2030], auto_target=False)
        self.set_user_value(trigger_id=99999096, key='faction04', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='bossSpawn') == 1:
            return 던전종료대기(self.ctx)


class 던전종료대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 던전종료딜레이(self.ctx)


class 던전종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
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
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=2000401, portal_id=3)
        self.set_user_value(trigger_id=99999099, key='DungeonClear', value=1)
        self.set_user_value(trigger_id=99999098, key='DungeonClear', value=1)
        self.set_user_value(trigger_id=99999097, key='DungeonClear', value=1)
        self.set_user_value(trigger_id=99999096, key='DungeonClear', value=1)
        self.destroy_monster(spawn_ids=[2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2099,2901,2902,2903,2904,2905], arg2=False)
        self.spawn_npc_range(range_ids=[1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919])
        self.set_portal(portal_id=2, visible=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 던전종료연출시작(self.ctx)


class 던전종료연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=305)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_dialogue(type=1, spawn_id=1901, script='$02000401_BF__MADRICANSIEGE__2$', time=3, arg5=2)
        self.set_skip(state=던전종료연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 던전종료연출01(self.ctx)

    def on_exit(self) -> None:
        self.set_mesh(trigger_ids=[3801,3802,3803,3804], fade=5.0)


class 던전종료연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=304)
        self.set_dialogue(type=1, spawn_id=1903, script='$02000401_BF__MADRICANSIEGE__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 던전종료연출02(self.ctx)


class 던전종료연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1902, script='$02000401_BF__MADRICANSIEGE__4$', time=4)
        self.set_dialogue(type=1, spawn_id=1904, script='$02000401_BF__MADRICANSIEGE__5$', time=2, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 던전종료연출종료(self.ctx)


class 던전종료연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 룸체크(self.ctx)


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 던전종료(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트던전종료(self.ctx)


class 던전종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=199, type='trigger', achieve='Madracan01')
        self.set_achievement(trigger_id=199, type='trigger', achieve='ClearMadracanSiege')
        self.set_achievement(trigger_id=199, type='trigger', achieve='Madracan_Q01')
        self.dungeon_clear()
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 퀘스트던전종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=199, type='trigger', achieve='Madracan_Q01')
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
