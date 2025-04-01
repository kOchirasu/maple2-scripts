""" trigger/02020111_bf/main.xml """
import trigger_api
from System.Numerics import Vector3


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900012, key='SkillBreakMissionReset', value=0)
        self.set_ambient_light(primary=Vector3(183,189,201))
        self.set_directional_light(diffuse_color=Vector3(192,210,211), specular_color=Vector3(170,170,170))

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1007]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=1006, skill_id=70002151, is_player=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1001]):
            return 보스전_시작(self.ctx)


class 보스전_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900012, key='SkillBreakMissionReset', value=1) # <스킬브레이크 던전 미션 체크시작>
        self.side_npc_talk(npc_id=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__MAIN__0$', duration=5684, voice='ko/Npc/00002201')
        self.dungeon_reset_time(seconds=420)
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5684):
            return 조건추가(self.ctx)


class 조건추가(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]) and self.dungeon_play_time() < 420:
            return 보스전_성공(self.ctx)
        if self.dungeon_play_time() == 420:
            return 보스전_타임어택실패(self.ctx)
        if self.user_value(key='SkillBreakFail') == 1:
            return 보스전_스킬브레이크실패(self.ctx)


class 보스전_스킬브레이크실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_stop_timer()
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 보스전_리셋세팅(self.ctx)


class 보스전_타임어택실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스전_타임어택실패세팅(self.ctx)


class 보스전_리셋세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=900012, key='SkillBreakMissionReset', value=0) # <스킬브레이크 던전 미션 리셋>
        self.set_portal(portal_id=5)
        self.set_portal(portal_id=6)
        self.set_portal(portal_id=7)
        self.set_portal(portal_id=8)
        self.set_portal(portal_id=9)
        self.set_portal(portal_id=10)
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=12)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.destroy_monster(spawn_ids=[-1])
        self.move_user(map_id=2020111, portal_id=1, box_id=1001)
        self.remove_buff(box_id=1006, skill_id=70002151, is_player=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


class 보스전_타임어택실패세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_set_end_time()
        self.dungeon_close_timer()
        self.remove_buff(box_id=1006, skill_id=70002151, is_player=True)


class 보스전_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_mission_complete(mission_id=23039005)
        self.dungeon_set_end_time()
        # self.dungeon_close_timer()
        self.side_npc_talk(npc_id=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__MAIN__1$', duration=3176, voice='ko/Npc/00002202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3176):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.dungeon_clear()
        self.set_achievement(type='trigger', achieve='ClearBlueLapenta')
        self.remove_buff(box_id=1006, skill_id=70002151, is_player=True)
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=7, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=8, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=9, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=10, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=12, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
