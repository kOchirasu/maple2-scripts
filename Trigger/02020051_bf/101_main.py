""" trigger/02020051_bf/101_main.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 포션사용(self.ctx)


class 포션사용(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=60001)
        self.reset_timer(timer_id='999')
        self.set_user_value(trigger_id=102, key='Timmer', value=2)
        self.set_ambient_light(primary=Vector3(198,255,205))
        self.set_directional_light(diffuse_color=Vector3(255,234,193), specular_color=Vector3(255,255,255))
        self.set_user_value(trigger_id=104, key='End', value=2)
        self.set_user_value(trigger_id=103, key='Main', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Potion') == 1:
            return 타이머(self.ctx)


class 타이머(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='999', seconds=10, auto_remove=True, display=True)
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', script='$02020051_BF__101_MAIN__0$', duration=5684, voice='ko/Npc/00002201')
        self.remove_buff(box_id=11, skill_id=90000900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 페이드아웃(self.ctx)


class 페이드아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='999')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_ambient_light(primary=Vector3(102,86,112))
            self.set_directional_light(diffuse_color=Vector3(255,234,193), specular_color=Vector3(127,91,93))
            return 페이드인(self.ctx)


class 페이드인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', script='$02020051_BF__101_MAIN__1$', duration=5684, voice='ko/Npc/00002201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 기간티카등장_렌덤조건(self.ctx)


class 기간티카등장_렌덤조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=60001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return 기간티카등장_1(self.ctx)
        if self.random_condition(weight=20.0):
            return 기간티카등장_2(self.ctx)
        if self.random_condition(weight=20.0):
            return 기간티카등장_3(self.ctx)
        if self.random_condition(weight=20.0):
            return 기간티카등장_4(self.ctx)
        if self.random_condition(weight=20.0):
            return 기간티카등장_5(self.ctx)
        if self.random_condition(weight=20.0):
            return 기간티카등장_6(self.ctx)


class 기간티카등장_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 기간티카등장_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 기간티카등장_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 기간티카등장_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 기간티카등장_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 기간티카등장_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=105, key='Summon_monster', value=1)
        self.set_user_value(trigger_id=106, key='Summon_monster_2', value=1)
        self.set_user_value(trigger_id=102, key='Timmer', value=1)
        self.set_user_value(trigger_id=104, key='End', value=1)
        self.set_event_ui_script(type=BannerType.Text, script='$02020051_BF__101_MAIN__2$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Potion') == 2:
            return 포션사용(self.ctx)


initial_state = 준비
