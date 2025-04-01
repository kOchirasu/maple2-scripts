""" trigger/02020061_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=3)
        self.enable_spawn_point_pc(spawn_id=1) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawn_id=2)
        self.enable_spawn_point_pc(spawn_id=3)
        self.enable_spawn_point_pc(spawn_id=4)
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='2')
        self.reset_timer(timer_id='3')
        self.set_actor(trigger_id=1901, visible=True, initial_sequence='Idle_A') # <연출용 액터>
        self.set_effect(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=True)
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048], visible=True) # <가두기 트리거 메쉬>
        self.shadow_expedition_close_boss_gauge()
        self.set_user_value(trigger_id=99990002, key='SpawnStart', value=0)
        self.set_user_value(trigger_id=99990003, key='ObjectPhase', value=0)
        self.set_user_value(trigger_id=99990008, key='BossPhase', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 유저카운트(self.ctx)


class 유저카운트(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FieldGameStart') == 1:
            # <게임 시작 결정>
            return 딜레이(self.ctx)
        if self.user_value(key='FieldGameStart') == 2:
            # <방폭 결정>
            return 방폭(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9002, type='trigger', achieve='corps_battle')
        self.set_event_ui_script(type=BannerType.Text, script='$02020061_BF__MAIN__0$', duration=5000)
        self.select_camera(trigger_id=999)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작(self.ctx)


class 방폭(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020061_BF__MAIN__1$', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 내보내기(self.ctx)


class 내보내기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=1, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=2, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=3, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=4, is_enable=True)
        self.reset_camera(interpolation_time=1.0)
        self.set_effect(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016])
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048])
        self.set_event_ui_round(rounds=[1,3])
        self.set_event_ui_script(type=BannerType.Text, script='$02020061_BF__MAIN__2$', duration=5000)
        self.set_timer(timer_id='1', seconds=180, auto_remove=True, display=True, v_offset=60) # <1라운드 게임 플레이 타임 설정>
        self.shadow_expedition_open_boss_gauge(max_gauge_point=800)
        self.set_user_value(trigger_id=99990002, key='SpawnStart', value=1)
        self.set_actor(trigger_id=1901, initial_sequence='Idle_A') # <연출용 액터>
        self.spawn_monster(spawn_ids=[701], auto_target=False) # <무적 오브젝트 생성>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GaugeClear') == 1:
            # <게이지를 다 채울 경우 다음 라운드>
            return 오브젝트페이즈(self.ctx)
        if self.time_expired(timer_id='1'):
            # <시간 내에 클리어하지 못할 경우 실패>
            return 실패_세팅(self.ctx)


class 오브젝트페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.give_reward_content(reward_id=31000001)
        self.set_event_ui_script(type=BannerType.Text, script='$02020061_BF__MAIN__3$', duration=5000)
        self.shadow_expedition_close_boss_gauge()
        self.set_event_ui_round(rounds=[2,3])
        self.reset_timer(timer_id='1')
        self.set_user_value(trigger_id=99990003, key='ObjectPhase', value=1)
        self.set_timer(timer_id='2', seconds=180, auto_remove=True, display=True, v_offset=60) # <2라운드 게임 플레이 타임 설정>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectClear') == 1:
            # <오브젝트를 파괴했을 경우 다음 라운드>
            return 보스페이즈(self.ctx)
        if self.time_expired(timer_id='2'):
            # <시간 내에 클리어하지 못할 경우 실패>
            return 실패_세팅(self.ctx)


class 보스페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.give_reward_content(reward_id=31000002)
        self.destroy_monster(spawn_ids=[-1])
        self.set_event_ui_script(type=BannerType.Text, script='$02020061_BF__MAIN__4$', duration=5000)
        self.reset_timer(timer_id='2')
        self.set_event_ui_round(rounds=[3,3])
        self.set_user_value(trigger_id=99990008, key='BossPhase', value=1)
        self.set_timer(timer_id='3', seconds=180, auto_remove=True, display=True, v_offset=60) # <3라운드 게임 플레이 타임 설정>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossClear') == 1:
            # <보스를 처치했을 경우 성공>
            return 성공_세팅(self.ctx)
        if self.time_expired(timer_id='3'):
            # <시간 내에 클리어하지 못할 경우 실패>
            return 실패_세팅(self.ctx)


class 성공_세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020061_BF__MAIN__5$')
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='2')
        self.reset_timer(timer_id='3')
        self.set_user_value(trigger_id=99990002, key='SpawnStart', value=2)
        self.set_user_value(trigger_id=99990003, key='ObjectPhase', value=2)
        self.set_user_value(trigger_id=99990004, key='BossPhase', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 성공_대사용(self.ctx)


class 성공_대사용(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_smile', duration=5000, script='$02020061_BF__MAIN__6$')
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 성공(self.ctx)


class 실패_세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020061_BF__MAIN__7$')
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='2')
        self.reset_timer(timer_id='3')
        self.set_user_value(trigger_id=99990002, key='SpawnStart', value=2)
        self.set_user_value(trigger_id=99990003, key='ObjectPhase', value=2)
        self.set_user_value(trigger_id=99990004, key='BossPhase', value=2)
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 실패_대사용(self.ctx)


class 실패_대사용(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_normal', duration=5000, script='$02020061_BF__MAIN__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 실패(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.field_war_end(is_clear=True)
        self.set_achievement(type='trigger', achieve='FieldwarAchieve_1')

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.field_war_end()

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
