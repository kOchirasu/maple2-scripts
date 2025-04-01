""" trigger/02000374_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4002, initial_sequence='Closed_A')
        self.set_event_ui_round(rounds=[0,3])
        self.set_portal(portal_id=1)
        self.set_mesh(trigger_ids=[6001])
        self.set_mesh(trigger_ids=[6002], visible=True)
        self.set_effect(trigger_ids=[7999])
        self.set_effect(trigger_ids=[7001])
        self.set_effect(trigger_ids=[7002])
        self.set_effect(trigger_ids=[7003])
        self.set_effect(trigger_ids=[7999])
        self.set_effect(trigger_ids=[7998])
        self.set_effect(trigger_ids=[7801])
        self.set_effect(trigger_ids=[7802])
        self.set_effect(trigger_ids=[7803])
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=700) >= 1:
            return Ready_Idle(self.ctx)


class Ready_Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return Ready_Idle_02(self.ctx)


class Ready_Idle_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=100, text_id=40012) # 잠시 후에 시작합니다.
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return start_01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=100)


class start_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.play_system_sound_in_box(sound='System_Dark_Intro_Chord_01')
        self.set_cinematic_ui(type=3, script='$02000374_BF__MAIN__25$') # 오브젝티브
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return start_02(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_round(rounds=[1,3])
        self.set_effect(trigger_ids=[7998], visible=True)
        self.set_mesh(trigger_ids=[6002])
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Opened_A')
        self.set_portal(portal_id=1, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return Round2(self.ctx)
        if self.user_detected(box_ids=[701]):
            return Round_Talk1(self.ctx)


class Round_Talk1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__0$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return Round2(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return Round_Talk_01_1(self.ctx)


class Round_Talk_01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[110], auto_target=False) # 닥터 피피

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return Round2(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return Round_Talk_02_1(self.ctx)


class Round_Talk_02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__1$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__1$', time=3)
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return Round2(self.ctx)
        if self.wait_tick(wait_tick=4000):
            return Round_Talk_03_1(self.ctx)


class Round_Talk_03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__2$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Round_Talk_04_1(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return Round2(self.ctx)


class Round_Talk_04_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return Round2(self.ctx)


class Round2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__3$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Round_Talk_00_2(self.ctx)


class Round_Talk_00_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__26$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__27$', time=3)
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Round_Talk_01_2(self.ctx)


class Round_Talk_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_round(rounds=[2,3])
        self.select_camera(trigger_id=8001)
        self.set_effect(trigger_ids=[7801], visible=True)
        self.set_effect(trigger_ids=[7802], visible=True)
        # self.set_effect(trigger_ids=[7803], visible=True)
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__28$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__29$', time=3)
        # self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__4$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            self.set_skill(trigger_ids=[5001], enable=True)
            self.set_skill(trigger_ids=[5002], enable=True)
            self.set_skill(trigger_ids=[5003], enable=True)
            self.set_skill(trigger_ids=[5004], enable=True)
            self.set_skill(trigger_ids=[5005], enable=True)
            self.set_skill(trigger_ids=[5006], enable=True)
            self.set_skill(trigger_ids=[5007], enable=True)
            self.set_skill(trigger_ids=[5008], enable=True)
            self.set_skill(trigger_ids=[5009], enable=True)
            self.set_skill(trigger_ids=[5010], enable=True)
            self.set_skill(trigger_ids=[5011], enable=True)
            self.set_skill(trigger_ids=[5012], enable=True)
            self.set_skill(trigger_ids=[5013], enable=True)
            return Round_Talk_02_2(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(trigger_id=8001, enable=False)
        self.set_effect(trigger_ids=[7001], visible=True)
        self.set_effect(trigger_ids=[7002], visible=True)
        self.set_effect(trigger_ids=[7003], visible=True)


class Round_Talk_02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2003')
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__5$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__5$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Round_Talk_03_2(self.ctx)


class Round_Talk_03_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__6$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__6$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Round_Spawn_Random2(self.ctx)


class Round_Spawn_Random2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return Round_Spawn_A2(self.ctx)
        if self.random_condition(weight=33.0):
            return Round_Spawn_B2(self.ctx)
        if self.random_condition(weight=33.0):
            return Round_Spawn_C2(self.ctx)


class Round_Spawn_A2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__7$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__7$', time=3) # 카모칸
        self.set_user_value(trigger_id=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=85000):
            # 2라운드 1차 스폰 타이머
            return Round_Spawn_A_02_Ready2(self.ctx)
        if self.user_value(key='2Round_A') == 1:
            return Round_Spawn_A_02_Ready2(self.ctx)


class Round_Spawn_B2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2004')
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__8$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__8$', time=3)
        self.set_user_value(trigger_id=2037403, key='2Round_B', value=1) # 캡틴 아구스 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=85000):
            # 2라운드 1차 스폰 타이머
            return Round_Spawn_B_02_Ready2(self.ctx)
        if self.user_value(key='2Round_B') == 1:
            return Round_Spawn_B_02_Ready2(self.ctx)


class Round_Spawn_C2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2005')
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__9$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__9$', time=3)
        self.set_user_value(trigger_id=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=85000):
            # 2라운드 1차 스폰 타이머
            return Round_Spawn_C_02_Ready2(self.ctx)
        if self.user_value(key='2Round_C') == 1:
            return Round_Spawn_C_02_Ready2(self.ctx)


class Round_Spawn_A_02_Ready2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__10$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__10$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round_Spawn_A_02_2(self.ctx)


class Round_Spawn_B_02_Ready2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__13$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__13$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round_Spawn_B_02_2(self.ctx)


class Round_Spawn_C_02_Ready2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__16$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__16$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round_Spawn_C_02_2(self.ctx)


class Round_Spawn_A_02_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Round_Spawn_A_B_02_2(self.ctx)
        if self.random_condition(weight=50.0):
            return Round_Spawn_A_C_02_2(self.ctx)


class Round_Spawn_A_B_02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=135000):
            # 2라운드 2차 스폰 타이머
            return Round_Spawn_A_B_C2(self.ctx)
        if self.user_value(key='2Round_B') == 1:
            return Round_Spawn_A_B_C2(self.ctx)


class Round_Spawn_A_C_02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=135000):
            # 2라운드 2차 스폰 타이머
            return Round_Spawn_A_C_B2(self.ctx)
        if self.user_value(key='2Round_C') == 1:
            return Round_Spawn_A_C_B2(self.ctx)


class Round_Spawn_A_B_C2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__11$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__11$', time=3, arg5=1)
        self.set_user_value(trigger_id=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return Round_End_Condition2(self.ctx)


class Round_Spawn_A_C_B2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__12$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__12$', time=3, arg5=1)
        self.set_user_value(trigger_id=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return Round_End_Condition2(self.ctx)


class Round_Spawn_B_02_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Round_Spawn_B_A_02_2(self.ctx)
        if self.random_condition(weight=50.0):
            return Round_Spawn_B_C_02_2(self.ctx)


class Round_Spawn_B_A_02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=135000):
            # 2라운드 2차 스폰 타이머
            return Round_Spawn_B_A_C2(self.ctx)
        if self.user_value(key='2Round_A') == 1:
            return Round_Spawn_B_A_C2(self.ctx)


class Round_Spawn_B_C_02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=135000):
            # 2라운드 2차 스폰 타이머
            return Round_Spawn_B_C_A2(self.ctx)
        if self.user_value(key='2Round_C') == 1:
            return Round_Spawn_B_C_A2(self.ctx)


class Round_Spawn_B_A_C2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__14$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__14$', time=3, arg5=1)
        self.set_user_value(trigger_id=2037404, key='2Round_C', value=1) # 데블린 치프  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return Round_End_Condition2(self.ctx)


class Round_Spawn_B_C_A2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__15$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__15$', time=3, arg5=1)
        self.set_user_value(trigger_id=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return Round_End_Condition2(self.ctx)


class Round_Spawn_C_02_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return Round_Spawn_C_A_02_2(self.ctx)
        if self.random_condition(weight=50.0):
            return Round_Spawn_C_B_02_2(self.ctx)


class Round_Spawn_C_A_02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=135000):
            # 2라운드 2차 스폰 타이머
            return Round_Spawn_C_A_B2(self.ctx)
        if self.user_value(key='2Round_A') == 1:
            return Round_Spawn_C_A_B2(self.ctx)


class Round_Spawn_C_B_02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=135000):
            # 2라운드 2차 스폰 타이머
            return Round_Spawn_C_B_A2(self.ctx)
        if self.user_value(key='2Round_B') == 1:
            return Round_Spawn_C_B_A2(self.ctx)


class Round_Spawn_C_A_B2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__18$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__18$', time=3, arg5=1)
        self.set_user_value(trigger_id=2037403, key='2Round_B', value=1) # 캡틴 모크  소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return Round_End_Condition2(self.ctx)


class Round_Spawn_C_B_A2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__17$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__17$', time=3, arg5=1)
        self.set_user_value(trigger_id=2037402, key='2Round_A', value=1) # 파모칸 소환 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return Round_End_Condition2(self.ctx)


class Round_End_Condition2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102,103,104]):
            return Round_Ready3(self.ctx)


class Round_Ready3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round_Talk01_3(self.ctx)


class Round_Talk01_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__19$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__19$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round_Talk02_3(self.ctx)


class Round_Talk02_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_round(rounds=[3,3])
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__20$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__20$', time=2)
        self.set_user_value(trigger_id=2037405, key='3Round_Effect', value=1) # 3라운드 연출 장치

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round_Talk03_3(self.ctx)


class Round_Talk03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__21$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__21$', time=2)
        self.set_effect(trigger_ids=[7206], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2300):
            return Round_Talk04_3(self.ctx)


class Round_Talk04_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[199], auto_target=False) # 붉은 두꺼비
        self.set_dialogue(type=1, spawn_id=199, script='$02000374_BF__MAIN__30$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round_Talk05_3(self.ctx)


class Round_Talk05_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[199])
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__31$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__32$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round_Talk06_3(self.ctx)


class Round_Talk06_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__22$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__22$', time=2)
        self.set_effect(trigger_ids=[7205], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2300):
            # 둔둔 스폰 타이밍
            return Round_Talk07_3(self.ctx)


class Round_Talk07_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__23$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__23$', time=2)
        self.spawn_monster(spawn_ids=[105], auto_target=False) # 둔둔

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[105]):
            return Clear(self.ctx)


class Clear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000374, portal_id=6)
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Opened_A')
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2999')
        self.set_event_ui_script(type=BannerType.Success, script='$02000374_BF__MAIN__33$', duration=3000, box_ids=['0'])
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__24$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Closed_A')
        self.set_event_ui_script(type=BannerType.Text, script='$02000374_BF__MAIN__34$', duration=3000)
        self.set_dialogue(type=1, spawn_id=110, script='$02000374_BF__MAIN__35$', time=2)
        self.set_effect(trigger_ids=[4102], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return End_02(self.ctx)


class End_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4002, initial_sequence='Closed_A')
        self.destroy_monster(spawn_ids=[110])
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)


initial_state = Ready
