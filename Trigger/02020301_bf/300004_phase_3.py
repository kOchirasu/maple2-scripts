""" trigger/02020301_bf/300004_phase_3.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[200011,200012,200013,200014,200015,200016,200017,200018])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AI_Phase') == 3:
            return 패이즈_3_시작(self.ctx)


class 패이즈_3_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[1003], skill_id=62100168, level=1) # 포탑 기절 이뮨
        self.destroy_monster(spawn_ids=[701])
        self.destroy_monster(spawn_ids=[702])
        self.destroy_monster(spawn_ids=[703])
        self.destroy_monster(spawn_ids=[704])
        self.destroy_monster(spawn_ids=[705])
        self.destroy_monster(spawn_ids=[706])
        self.set_user_value(trigger_id=3000032, key='Phase_2_Interect_02', value=0)
        self.set_user_value(trigger_id=3000033, key='Phase_2_Interect_03', value=0)
        self.set_user_value(trigger_id=3000034, key='Phase_2_Interect_04', value=0)
        self.set_user_value(trigger_id=3000035, key='Phase_2_Interect_05', value=0)
        self.set_user_value(trigger_id=3000036, key='Phase_2_Interect_06', value=0)
        self.set_user_value(trigger_id=3000037, key='Phase_2_Interect_07', value=0)
        self.remove_buff(box_id=1001, skill_id=73000004, is_player=True)
        self.set_user_value(trigger_id=3000031, key='Phase_2_Interect_01', value=0) # 아르케온 탈것 인터렉트 제거
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300004_PHASE_3__0$', duration=3176)
        self.side_npc_talk(npc_id=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300004_PHASE_3__1$', duration=3176)
        self.set_user_value(key='AI_Phase', value=0)
        self.set_visible_breakable_object(trigger_ids=[5171,5172,5173,5174,5175,5176,5177,5178,5179,5180,5181,5182,5183,5184], visible=True)
        self.set_visible_breakable_object(trigger_ids=[5151,5152,5153,5154,5155,5156,5157,5158,5159,5160,5161,5162,5163,5164], visible=True)
        self.set_breakable(trigger_ids=[5171,5172,5173,5174,5175,5176,5177,5178,5179,5180,5181,5182,5183,5184], enable=True) # 좌우 이동 엘리베이터 동작
        self.set_breakable(trigger_ids=[5151,5152,5153,5154,5155,5156,5157,5158,5159,5160,5161,5162,5163,5164], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 엘리베이터_도착(self.ctx)


class 엘리베이터_도착(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='AI_Phase', value=0)
        self.set_visible_breakable_object(trigger_ids=[5351,5352,5353,5354,5355,5356,5357,5358,5359,5360,5361,5362,5363,5364], visible=True) # 좌우 이동 엘리베이터  도착 후 재생
        self.set_visible_breakable_object(trigger_ids=[5371,5372,5373,5374,5375,5376,5377,5378,5379,5380,5381,5382,5383,5384], visible=True)
        self.set_breakable(trigger_ids=[5171,5172,5173,5174,5175,5176,5177,5178,5179,5180,5181,5182,5183,5184]) # 좌우 이동 엘리베이터 멈춤 후, 숨기기
        self.set_breakable(trigger_ids=[5151,5152,5153,5154,5155,5156,5157,5158,5159,5160,5161,5162,5163,5164])
        self.set_visible_breakable_object(trigger_ids=[5171,5172,5173,5174,5175,5176,5177,5178,5179,5180,5181,5182,5183,5184])
        self.set_visible_breakable_object(trigger_ids=[5151,5152,5153,5154,5155,5156,5157,5158,5159,5160,5161,5162,5163,5164])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 포탑_생성(self.ctx)


class 포탑_생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[512]) # 포탑 소환
        self.spawn_monster(spawn_ids=[511])
        self.set_user_value(trigger_id=3000041, key='Phase_3_Interect_01', value=1) # 포탑 발사 트리거로 명령
        self.set_user_value(trigger_id=3000042, key='Phase_3_Interect_02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 가이드(self.ctx)


class 가이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020301_BF__300004_PHASE_3__2$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return None # Missing State: 엘리베이터_대기


initial_state = 대기
