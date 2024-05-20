""" trigger/02010054_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=10)
        self.set_gravity(gravity=-9.8)
        self.set_interact_object(trigger_ids=[10000856], state=2)
        self.set_interact_object(trigger_ids=[10000857], state=2)
        self.set_interact_object(trigger_ids=[10000858], state=2)
        self.set_interact_object(trigger_ids=[10000859], state=2)
        self.set_mesh(trigger_ids=[3000], visible=True)
        self.set_mesh(trigger_ids=[3001], visible=True)
        self.set_mesh(trigger_ids=[3002], visible=True)
        self.set_mesh(trigger_ids=[3003], visible=True)
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123])
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222])
        self.set_mesh(trigger_ids=[3315,3316,3317,3318,3319,3320,3321])
        self.set_mesh(trigger_ids=[3130,3131,3132,3133,3134,3135,3136])
        self.set_mesh(trigger_ids=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615,3616,3617,3618,3619,3620])
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520])
        self.set_mesh(trigger_ids=[3330])
        self.set_effect(trigger_ids=[600], visible=True)
        self.set_effect(trigger_ids=[6000])
        self.set_effect(trigger_ids=[6001])
        self.set_effect(trigger_ids=[6002])
        self.set_effect(trigger_ids=[6003])
        self.set_effect(trigger_ids=[6004])
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_effect(trigger_ids=[609], visible=True)
        self.set_effect(trigger_ids=[612], visible=True)
        self.set_effect(trigger_ids=[613], visible=True)
        self.set_effect(trigger_ids=[614], visible=True)
        self.set_effect(trigger_ids=[615], visible=True)
        self.set_effect(trigger_ids=[616], visible=True)
        self.set_effect(trigger_ids=[620])
        self.set_effect(trigger_ids=[621])
        self.set_effect(trigger_ids=[622])
        self.set_effect(trigger_ids=[625], visible=True)
        self.set_effect(trigger_ids=[626], visible=True)
        self.set_effect(trigger_ids=[627], visible=True)
        self.set_effect(trigger_ids=[628], visible=True)
        self.set_effect(trigger_ids=[629], visible=True)
        self.spawn_monster(spawn_ids=[2099], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(box_ids=[199], skill_id=70000107, level=1, is_player=False, is_skill_set=False)
        self.select_camera(trigger_id=301)
        self.set_skip(state=인트로연출스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출해제(self.ctx)


class 연출해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return 시작(self.ctx)


class 인트로연출스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            self.remove_buff(box_id=199, skill_id=70000107)
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.remove_buff(box_id=199, skill_id=70000107)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20105407, text_id=20105407, duration=3500)
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[6000])
        self.set_mesh(trigger_ids=[3000])
        self.spawn_monster(spawn_ids=[2001,2002,2003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 반응대기01(self.ctx)


class 반응대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20105401, text_id=20105401)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(trigger_ids=[10000856], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000856], state=0):
            self.hide_guide_summary(entity_id=20105401)
            self.set_gravity(gravity=-39.0)
            return 반응대기02(self.ctx)


class 반응대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000860,10000861], state=0):
            self.set_event_ui(type=1, arg2='$02010054_BF__MAIN__1$', arg3='5000', arg4='0')
            self.set_interact_object(trigger_ids=[10000858], state=1)
            return 반응대기03(self.ctx)


class 반응대기03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000858], state=0):
            self.set_effect(trigger_ids=[607])
            self.set_effect(trigger_ids=[608])
            self.set_effect(trigger_ids=[609])
            self.set_effect(trigger_ids=[6001])
            self.set_effect(trigger_ids=[6002], visible=True)
            self.set_mesh(trigger_ids=[3001])
            self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222], visible=True, interval=50, fade=1.0)
            self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123], visible=True, interval=50, fade=1.0)
            self.set_mesh(trigger_ids=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615,3616,3617,3618,3619,3620], visible=True, interval=50, fade=1.0)
            self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520], visible=True, interval=50, fade=1.0)
            self.spawn_monster(spawn_ids=[2011,2014,2015,2020,2021], auto_target=False)
            self.set_gravity(gravity=-9.8)
            return 인원체크(self.ctx)


class 인원체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_max_user_count() == 1:
            # 던전 최대 인원수가 1이면
            return 반응둘중하나만(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 반응둘다01(self.ctx)


class 반응둘다01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000884,10000885], state=0):
            return 반응대기05(self.ctx)


class 반응둘중하나만(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000884], state=0):
            return 반응대기05(self.ctx)
        if self.object_interacted(interact_ids=[10000885], state=0):
            return 반응대기05(self.ctx)


class 반응대기05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000857], state=1)
        self.set_interact_object(trigger_ids=[10000859], state=1)
        self.show_guide_summary(entity_id=20105401, text_id=20105401)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000857], state=0):
            self.hide_guide_summary(entity_id=20105401)
            self.set_gravity(gravity=-39.0)
            return 별생성(self.ctx)


class 별생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3315,3316,3317,3318,3319,3320,3321], visible=True, interval=500, fade=3.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3315,3316,3317,3318,3319,3320,3321], interval=900, fade=2.0)
            return 반응대기06(self.ctx)


class 반응대기06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000859], state=0):
            self.set_mesh(trigger_ids=[3330], visible=True, fade=3.0)
            self.set_portal(portal_id=10, enable=True)
            self.set_gravity(gravity=-9.8)
            return 중간보스소환(self.ctx)


class 중간보스소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2098], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2098]):
            self.set_effect(trigger_ids=[6003])
            return 골렘소환대기(self.ctx)


class 골렘소환대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[612])
        self.set_effect(trigger_ids=[613])
        self.set_effect(trigger_ids=[614])
        self.set_effect(trigger_ids=[615])
        self.set_effect(trigger_ids=[616])
        self.set_mesh(trigger_ids=[3002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[107]):
            return 골렘소환(self.ctx)


class 골렘소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[620], visible=True)
        self.spawn_monster(spawn_ids=[2024], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 골렘소환2(self.ctx)


class 골렘소환2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[621], visible=True)
        self.spawn_monster(spawn_ids=[2025], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 골렘소환3(self.ctx)


class 골렘소환3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[622], visible=True)
        self.spawn_monster(spawn_ids=[2026], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2024,2025,2026]):
            return 그라즈나전투(self.ctx)


class 그라즈나전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[625])
        self.set_effect(trigger_ids=[626])
        self.set_effect(trigger_ids=[627])
        self.set_effect(trigger_ids=[628])
        self.set_effect(trigger_ids=[629])
        self.set_effect(trigger_ids=[6004])
        self.set_mesh(trigger_ids=[3003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3130,3131,3132,3133,3134,3135,3136], visible=True)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_timer(timer_id='4', seconds=4)
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
