""" trigger/02020145_bf/main.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_user_value(trigger_id=900012, key='SkillBreakMissionReset', value=0)
        self.set_ambient_light(primary=Vector3(183,189,201))
        self.set_directional_light(diffuse_color=Vector3(192,210,211), specular_color=Vector3(170,170,170))
        # triggerbox 1002 풀밭 안내 화살표 끄기
        self.set_effect(trigger_ids=[200031,200032,200033,200034,200035])
        # triggerbox 1003 라펜턴드 안내 화살표 끄기
        self.set_effect(trigger_ids=[200001,200002,200003,200004,200005])
        # triggerbox 1004 화염 안내 화살표 끄기
        self.set_effect(trigger_ids=[200021,200022,200023,200024,200025])
        # triggerbox 1005 얼음 안내 화살표 끄기
        self.set_effect(trigger_ids=[200011,200012,200013,200014,200015])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1007]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=1006, skill_id=70002151, is_player=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1007]):
            return 보스전_시작(self.ctx)


class 보스전_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__MAIN__0$', duration=5684, voice='ko/Npc/00002201')
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5684):
            return 조명변경(self.ctx)


class 조명변경(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_ambient_light(primary=Vector3(52,48,38))
        self.set_directional_light(diffuse_color=Vector3(0,0,0), specular_color=Vector3(206,174,84))
        self.add_buff(box_ids=[101], skill_id=62100014, level=1)
        self.add_buff(box_ids=[1001], skill_id=75000001, level=1) # 캐릭터 밝히기
        self.spawn_monster(spawn_ids=[121,123,125,131,132,133])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 보스전_성공(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return 페이드인(self.ctx)


class 페이드인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # 위에 걸린 62100014 : 렌듀비앙 어둠의 기운 삭제
        self.npc_remove_additional_effect(spawn_id=101, additional_effect_id=62100014)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 조명리셋(self.ctx)


class 조명리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 하하핫, 제법이군... 끝까지 한번 버텨봐라!!
        self.set_dialogue(type=1, spawn_id=101, script='$02020111_BF__MOVEMENT_01__1$', time=3)
        self.destroy_monster(spawn_ids=[121,122,123,124,125,131,132,133,134])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_ambient_light(primary=Vector3(183,189,201))
        self.set_directional_light(diffuse_color=Vector3(192,210,211), specular_color=Vector3(170,170,170))
        self.add_buff(box_ids=[1001], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1002], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1003], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1004], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1005], skill_id=75000002, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 보스전_성공(self.ctx)
        if self.wait_tick(wait_tick=15000):
            return 조건확인(self.ctx)


class 조건확인(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 보스전_성공(self.ctx)
        if self.npc_hp(spawn_id=101, is_relative=True) >= 50:
            # 렌듀비앙 HP 50% 이상이면 불 끄고 싸우는 패턴 한번 더
            return 조명변경(self.ctx)
        if self.npc_hp(spawn_id=101, is_relative=True) <= 50:
            # 렌듀비앙 HP 50% 이하면 일반 싸우는 패턴으로 유지
            return 조건추가(self.ctx)


class 조건추가(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 보스전_성공(self.ctx)


class 보스전_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(type='trigger', achieve='ClearBlueLapenta_Quest')
        self.side_npc_talk(npc_id=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__MAIN__1$', duration=3176, voice='ko/Npc/00002202') # 크윽.....네놈들.... 두고보자!!
        self.destroy_monster(spawn_ids=[121,122,123,124,125,131,132,133,134])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3176):
            return 조명리셋2(self.ctx)


class 조명리셋2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=Vector3(183,189,201))
        self.set_directional_light(diffuse_color=Vector3(192,210,211), specular_color=Vector3(170,170,170))
        self.add_buff(box_ids=[1001], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1002], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1003], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1004], skill_id=75000002, level=1)
        self.add_buff(box_ids=[1005], skill_id=75000002, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_achievement(type='trigger', achieve='ClearBlueLapenta_Quest')
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
