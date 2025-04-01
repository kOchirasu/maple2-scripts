""" trigger/02020301_bf/300006_phase_5.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AI_Phase') == 5:
            return 패이즈_5_시작(self.ctx)


class 패이즈_5_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111])
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300006_PHASE_5__0$', duration=3176)
        self.set_effect(trigger_ids=[200021,200022,200023,200024,200025,200026,200027,200028])
        self.set_user_value(key='AI_Phase', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Portal_On_04') == 1:
            return 포탈_오픈_대기(self.ctx)


class 포탈_오픈_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 포탈_오픈(self.ctx)


class 포탈_오픈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3000051, key='Phase_4_Interect_01', value=0) # 페이즈4 장치 삭제
        self.set_user_value(trigger_id=3000052, key='Phase_4_Interect_02', value=0)
        self.set_user_value(trigger_id=3000053, key='Phase_4_Interect_03', value=0)
        self.set_user_value(trigger_id=3000054, key='Phase_4_Interect_04', value=0)
        self.set_effect(trigger_ids=[200001,200002,200003,200004,200005,200006,200007,200008])
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300006_PHASE_5__1$', duration=3176)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1002]):
            return 엘리베이터_동작_대기(self.ctx)


class 엘리베이터_동작_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='Last_Phase', value=1)
        # 초고속 플레이에 인해 트리거가 제거 되지 않는 문제를 항번더 입력
        self.set_user_value(trigger_id=3000051, key='Phase_4_Interect_01', value=0)
        self.set_user_value(trigger_id=3000052, key='Phase_4_Interect_02', value=0)
        self.set_user_value(trigger_id=3000053, key='Phase_4_Interect_03', value=0)
        self.set_user_value(trigger_id=3000054, key='Phase_4_Interect_04', value=0)
        self.set_effect(trigger_ids=[200001,200002,200003,200004,200005,200006,200007,200008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 택스트_1(self.ctx)


class 택스트_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300006_PHASE_5__2$', duration=3176)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 택스트_2(self.ctx)


class 택스트_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_normal', script='$02020301_BF__300006_PHASE_5__3$', duration=3176)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 엘리베이터_동작(self.ctx)


class 엘리베이터_동작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410], enable=True) # 5페이즈 상하 엘리베이터 동작
        self.set_breakable(trigger_ids=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420], enable=True)
        self.set_breakable(trigger_ids=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430], enable=True)
        self.set_breakable(trigger_ids=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440], enable=True)
        self.set_visible_breakable_object(trigger_ids=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410], visible=True) # 5페이즈 상하 엘리베이터 동작 보이기
        self.set_visible_breakable_object(trigger_ids=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420], visible=True)
        self.set_visible_breakable_object(trigger_ids=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430], visible=True)
        self.set_visible_breakable_object(trigger_ids=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 엘리베이터_도착(self.ctx)


class 엘리베이터_도착(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[5501,5502,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512,5513,5514,5515,5516,5517,5518,5519,5520,5521,5522,5523,5524,5525,5526,5527,5528,5529,5530,5531,5532,5533,5534,5535,5536,5537,5538,5539,5540], visible=True) # 5페이즈 상하 엘리베이터 도착 나타나기
        self.set_breakable(trigger_ids=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410]) # 5페이즈 상하 엘리베이터 멈춤
        self.set_breakable(trigger_ids=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420])
        self.set_breakable(trigger_ids=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430])
        self.set_breakable(trigger_ids=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440])
        self.set_visible_breakable_object(trigger_ids=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410]) # 5페이즈 상하 엘리베이터 동작 숨기기
        self.set_visible_breakable_object(trigger_ids=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420])
        self.set_visible_breakable_object(trigger_ids=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430])
        self.set_visible_breakable_object(trigger_ids=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아르케온_탈것_생성(self.ctx)


class 아르케온_탈것_생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020301_BF__300006_PHASE_5__4$', duration=4000)
        self.set_user_value(trigger_id=3000061, key='Phase_5_Interect_01', value=1) # 아르케온 탈것 페이즈로 이동
        self.set_user_value(trigger_id=3000062, key='Phase_5_Interect_02', value=1)
        self.set_user_value(trigger_id=3000063, key='Phase_5_Interect_03', value=1)
        self.set_user_value(trigger_id=3000064, key='Phase_5_Interect_04', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 길막열기(self.ctx)


class 길막열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5641,5642,5643,5644]) # 4페이즈 상하좌우 엘리베이터 길막 열기
        self.set_agent(trigger_ids=[1810000,1810001,1810002,1810003,1810004,1810005,1810006,1810007,1810008,1810009,1810010,1810011])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 아르케온_탈것_리셋(self.ctx)


class 아르케온_탈것_리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=3000061, key='Phase_5_Interect_01', value=0) # 아르케온 탈것 리셋
        self.set_user_value(trigger_id=3000062, key='Phase_5_Interect_02', value=0)
        self.set_user_value(trigger_id=3000063, key='Phase_5_Interect_03', value=0)
        self.set_user_value(trigger_id=3000064, key='Phase_5_Interect_04', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return None # Missing State: 게임_종료


initial_state = 대기
