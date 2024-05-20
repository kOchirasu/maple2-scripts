""" trigger/52100301_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=300002, key='Phase_1', value=0) # 페이즈별 트리거 실행 대기
        self.set_user_value(trigger_id=300003, key='Phase_2', value=0)
        self.set_user_value(trigger_id=300004, key='Phase_3', value=0)
        self.set_user_value(trigger_id=300005, key='Phase_4', value=0)
        self.set_user_value(trigger_id=300006, key='Phase_5', value=0)
        self.set_mesh(trigger_ids=[5241,5242,5243,5244], visible=True) # 4페이즈 상하좌우 엘리베이터 길막 닫음
        self.set_mesh(trigger_ids=[5641,5642,5643,5644], visible=True) # 5페이즈 상하좌우 엘리베이터 길막 닫음
        self.set_breakable(trigger_ids=[5171,5172,5173,5174,5175,5176,5177,5178,5179,5180,5181,5182,5183,5184]) # 좌우 이동 엘리베이터 동작 대기
        self.set_breakable(trigger_ids=[5151,5152,5153,5154,5155,5156,5157,5158,5159,5160,5161,5162,5163,5164])
        self.set_breakable(trigger_ids=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110]) # 4페이즈 상하 엘리베이터 동작 대기
        self.set_breakable(trigger_ids=[5111,5112,5113,5114,5115,5116,5117,5118,5119,5120])
        self.set_breakable(trigger_ids=[5121,5122,5123,5124,5125,5126,5127,5128,5129,5130])
        self.set_breakable(trigger_ids=[5131,5132,5133,5134,5135,5136,5137,5138,5139,5140])
        self.set_breakable(trigger_ids=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410]) # 5페이즈 상하 엘리베이터 동작 대기
        self.set_breakable(trigger_ids=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420])
        self.set_breakable(trigger_ids=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430])
        self.set_breakable(trigger_ids=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440])
        self.set_visible_breakable_object(trigger_ids=[5351,5352,5353,5354,5355,5356,5357,5358,5359,5360,5361,5362,5363,5364]) # 좌우 이동 엘리베이터 숨기기
        self.set_visible_breakable_object(trigger_ids=[5371,5372,5373,5374,5375,5376,5377,5378,5379,5380,5381,5382,5383,5384])
        self.set_visible_breakable_object(trigger_ids=[5351,5352,5353,5354,5355,5356,5357,5358,5359,5360,5361,5362,5363,5364,5371,5372,5373,5374,5375,5376,5377,5378,5379,5380,5381,5382,5383,5384]) # 3페이즈 좌우 엘리베이터 숨기기
        self.set_visible_breakable_object(trigger_ids=[5301,5302,5303,5304,5305,5306,5307,5308,5309,5310,5311,5312,5313,5314,5315,5316,5317,5318,5319,5320,5321,5322,5323,5324,5325,5326,5327,5328,5329,5330,5331,5332,5333,5334,5335,5336,5337,5338,5339,5340]) # 4페이즈 상하 엘리베이터(정지) 숨기기
        self.set_visible_breakable_object(trigger_ids=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110]) # 4페이즈 상하 엘리베이터 숨기기
        self.set_visible_breakable_object(trigger_ids=[5111,5112,5113,5114,5115,5116,5117,5118,5119,5120])
        self.set_visible_breakable_object(trigger_ids=[5121,5122,5123,5124,5125,5126,5127,5128,5129,5130])
        self.set_visible_breakable_object(trigger_ids=[5131,5132,5133,5134,5135,5136,5137,5138,5139,5140])
        self.set_visible_breakable_object(trigger_ids=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410]) # 5페이즈 상하 엘리베이터 동작 숨기기
        self.set_visible_breakable_object(trigger_ids=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420])
        self.set_visible_breakable_object(trigger_ids=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430])
        self.set_visible_breakable_object(trigger_ids=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440])
        self.set_visible_breakable_object(trigger_ids=[5501,5502,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512,5513,5514,5515,5516,5517,5518,5519,5520,5521,5522,5523,5524,5525,5526,5527,5528,5529,5530,5531,5532,5533,5534,5535,5536,5537,5538,5539,5540]) # 5페이즈 상하 엘리베이터 숨기기
        self.set_interact_object(trigger_ids=[10003126], state=2) # 2페이즈 인터렉트 오브젝트 대기
        self.set_interact_object(trigger_ids=[10003121], state=2) # 3페이즈 인터렉트 오브젝트 대기
        self.set_interact_object(trigger_ids=[10003122], state=2)
        self.set_interact_object(trigger_ids=[10003111], state=2) # 4페이즈 인터렉트 오브젝트 대기
        self.set_interact_object(trigger_ids=[10003112], state=2)
        self.set_interact_object(trigger_ids=[10003113], state=2)
        self.set_interact_object(trigger_ids=[10003114], state=2)
        self.set_interact_object(trigger_ids=[10003101], state=2) # 5페이즈 인터렉트 오브젝트 대기
        self.set_interact_object(trigger_ids=[10003102], state=2)
        self.set_interact_object(trigger_ids=[10003103], state=2)
        self.set_interact_object(trigger_ids=[10003104], state=2)
        self.set_agent(trigger_ids=[1800000,1800001,1800002,1800003,1800004,1800005,1800006,1800007,1800008,1800009,1800010,1800011], visible=True)
        self.set_agent(trigger_ids=[1810000,1810001,1810002,1810003,1810004,1810005,1810006,1810007,1810008,1810009,1810010,1810011], visible=True)
        self.add_buff(box_ids=[1003], skill_id=62100168, level=1) # 포탑 기절 이뮨
        self.set_portal(portal_id=7)
        # 페이즈 시작전에 올라오지 엘리베이터에 플레이어가 도달할 경우, 전투 지역으로 돌려보냄
        self.set_portal(portal_id=13)
        self.set_portal(portal_id=14)
        self.set_portal(portal_id=15)
        self.set_portal(portal_id=16)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1001]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.dungeon_reset_time(seconds=420)
        self.set_mesh(trigger_ids=[5241,5242,5243,5244], visible=True)
        self.side_npc_talk(npc_id=29500101, illust='ArcheonBlack_Normal', script='$52100301_QD__MAIN__0$', duration=5684)
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 아르케온 등장
        self.spawn_monster(spawn_ids=[111]) # 아르케온 한방기 폭발 ai
        self.spawn_monster(spawn_ids=[112]) # 아르케온 한방기 폭발 ai 엘리베이터
        self.spawn_monster(spawn_ids=[113])
        self.spawn_monster(spawn_ids=[114])
        self.spawn_monster(spawn_ids=[115])
        self.spawn_monster(spawn_ids=[121]) # 아르케온 페이즈4 일직선 폭발 ai
        self.spawn_monster(spawn_ids=[122])
        self.spawn_monster(spawn_ids=[123])
        self.spawn_monster(spawn_ids=[124])
        self.set_portal(portal_id=13, enable=True)
        self.set_portal(portal_id=14, enable=True)
        self.set_portal(portal_id=15, enable=True)
        self.set_portal(portal_id=16, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 조건추가(self.ctx)


class 조건추가(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.dungeon_play_time() == 420:
            return 보스전_타임어택실패(self.ctx)
        """
        if self.monster_dead(spawn_ids=[101]):
            return 보스전_성공(self.ctx)


"""
class 보스전_타임어택실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[1003], skill_id=62100169, level=1)
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스전_타임어택실패세팅(self.ctx)
"""

"""
class 보스전_타임어택실패세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
"""

class 보스전_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10003126], state=2) # 2페이즈 인터렉트 오브젝트 대기
        self.set_user_value(trigger_id=3000061, key='Phase_5_Interect_01', value=0)
        self.add_buff(box_ids=[1003], skill_id=62100169, level=1)
        self.dungeon_mission_complete(mission_id=23039005) # 포탑 기절 이뮨 제거
        self.dungeon_set_end_time()
        self.side_npc_talk(npc_id=29500101, illust='ArcheonBlack_Die', script='$52100301_QD__MAIN__1$', duration=3176)
        self.set_achievement(type='trigger', achieve='KillArcheon')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 추가대화(self.ctx)


class 추가대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_normal', script='$52100301_QD__MAIN__2$', duration=3176)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.dungeon_clear()
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
