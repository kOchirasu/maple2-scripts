""" trigger/02000498_bf/stage_01.xml """
import trigger_api
from System.Numerics import Vector3


class 시작연출_6(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[100]):
            return 페이드아웃(self.ctx)


class 페이드아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 페이드아웃_2(self.ctx)


class 페이드아웃_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='곧 새로운 차원으로 당신을 안내 합니다.', arg3='3000')
        self.set_effect(trigger_ids=[500], visible=True)
        self.set_effect(trigger_ids=[501], visible=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작대기_1(self.ctx)


class 시작대기_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_to_pos(pos=Vector3(433,-6777,8701))

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 페이드인(self.ctx)


class 페이드인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.change_background(dds='BG_Lith_C.dds')
        self.set_ambient_light(primary=Vector3(199,207,214))
        self.set_directional_light(diffuse_color=Vector3(255,255,255), specular_color=Vector3(255,255,255))

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[100010], skill_id=70000103, level=1)
        # self.set_effect(trigger_ids=[6010], visible=True)
        # self.set_effect(trigger_ids=[6011], visible=True)
        # self.set_effect(trigger_ids=[6012], visible=True)
        # self.set_effect(trigger_ids=[6013], visible=True)
        # self.set_effect(trigger_ids=[6015], visible=True)
        # self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return None # Missing State: 안내02


"""
class 안내02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 안내03(self.ctx)
"""

"""
class 안내03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 진동대기(self.ctx)
"""

"""
class 진동대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 유저감지(self.ctx)
"""

"""
class 유저감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_start_game(round=30)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_skill(trigger_ids=[701], enable=True)
        self.set_effect(trigger_ids=[6010])
        self.set_effect(trigger_ids=[6011])
        self.set_effect(trigger_ids=[6012])
        self.set_effect(trigger_ids=[6013])
        self.set_mesh(trigger_ids=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 라운드대기1(self.ctx)
"""

"""
class 라운드대기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6110], visible=True)
        self.set_effect(trigger_ids=[6111], visible=True)
        self.set_effect(trigger_ids=[6112], visible=True)
        self.set_effect(trigger_ids=[6113], visible=True)
        self.set_timer(timer_id='3', seconds=3)
        self.dark_stream_start_round(round=1, ui_duration=3000, damage_penalty=5)
        self.set_event_ui(type=0, arg2='1,5,1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드1(self.ctx)
"""

"""
class 라운드1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[101001], score=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101001]):
            self.dark_stream_clear_round(round=1)
            self.set_achievement(trigger_id=101, type='trigger', achieve='1roundpass')
            return 라운드대기2(self.ctx)
"""

"""
class 라운드대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_start_round(round=2, ui_duration=3000, damage_penalty=5)
        self.set_timer(timer_id='3', seconds=3)
        self.set_event_ui(type=0, arg2='2,5,1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드2(self.ctx)
"""

"""
class 라운드2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[102001], score=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102001]):
            self.dark_stream_clear_round(round=2)
            self.set_achievement(trigger_id=101, type='trigger', achieve='2roundpass')
            return 라운드대기3(self.ctx)
"""

"""
class 라운드대기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='3,5,1')
        self.dark_stream_start_round(round=3, ui_duration=3000, damage_penalty=5)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드3(self.ctx)
"""

"""
class 라운드3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[103001], score=16000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103001]):
            self.dark_stream_clear_round(round=3)
            self.set_achievement(trigger_id=101, type='trigger', achieve='3roundpass')
            return 라운드대기4(self.ctx)
"""

"""
class 라운드대기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='4,5,1')
        self.set_timer(timer_id='3', seconds=3)
        self.dark_stream_start_round(round=4, ui_duration=3000, damage_penalty=5)
        self.set_event_ui(type=1, arg2='$02000350_BF__MAIN__3$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_event_ui(type=0, arg2='4,5,1')
            return 라운드4(self.ctx)
"""

"""
class 라운드4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=30, start_delay=1, interval=1, v_offset=80)
        self.spawn_monster(spawn_ids=[104099], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            self.destroy_monster(spawn_ids=[104099])
            self.reset_timer(timer_id='30')
            self.dark_stream_clear_round(round=4)
            self.set_achievement(trigger_id=101, type='trigger', achieve='4roundpass')
            return 라운드대기5(self.ctx)
"""

"""
class 라운드대기5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='5,5,1')
        self.set_effect(trigger_ids=[6101], visible=True)
        self.dark_stream_start_round(round=5, ui_duration=3000, damage_penalty=5)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 라운드5(self.ctx)
"""

"""
class 라운드5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[105001], score=135000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[105001]):
            self.dark_stream_clear_round(round=5)
            self.set_achievement(trigger_id=101, type='trigger', achieve='5roundpass')
            return 바닥부심(self.ctx)
"""

"""
class 바닥부심(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_effect(trigger_ids=[610], visible=True)
            self.set_effect(trigger_ids=[6110])
            self.set_effect(trigger_ids=[6111])
            self.set_effect(trigger_ids=[6112])
            self.set_effect(trigger_ids=[6113])
            self.set_skill(trigger_ids=[702], enable=True)
            self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146])
            self.set_event_ui(type=0, arg2='0,0')
            return 종료(self.ctx)
"""

class 종료(trigger_api.Trigger):
    pass


initial_state = 시작연출_6
