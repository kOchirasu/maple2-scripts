""" trigger/02000066_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 초기화
        self.set_effect(trigger_ids=[602]) # 아노스 던전 시작01
        self.set_effect(trigger_ids=[603]) # 아노스  소환
        self.set_effect(trigger_ids=[604]) # 아노스 게이트 파괴
        self.set_effect(trigger_ids=[605]) # 아노스 경비병 사망
        self.set_effect(trigger_ids=[606]) # 파토스 성공01
        self.set_effect(trigger_ids=[607]) # 파토스 성공02
        self.set_effect(trigger_ids=[608]) # 파토스 성공03
        self.set_effect(trigger_ids=[609]) # 파토스 성공04
        self.set_effect(trigger_ids=[610]) # 파토스 성공05
        self.set_effect(trigger_ids=[611]) # 파토스 리젠
        self.set_effect(trigger_ids=[612]) # 아노스 성공
        self.set_effect(trigger_ids=[613]) # 파토스 실패01
        self.set_effect(trigger_ids=[614]) # 파토스 실패02
        self.set_effect(trigger_ids=[615]) # 파토스 실패03
        self.set_effect(trigger_ids=[616]) # 파토스 실패04
        self.set_effect(trigger_ids=[617]) # 파토스 실패05
        self.set_effect(trigger_ids=[618]) # 파토스 실패06
        self.set_effect(trigger_ids=[619]) # 파토스 실패07
        self.set_effect(trigger_ids=[620])
        self.set_effect(trigger_ids=[6003]) # 미션 성공
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.spawn_monster(spawn_ids=[99], auto_target=False)
        self.set_mesh(trigger_ids=[9001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_max_user_count() == 4:
            # 던전 최대 인원수가 4이면
            return 연출시작(self.ctx)
        if self.dungeon_max_user_count() == 3:
            # 던전 최대 인원수가 3이면
            self.set_user_value(trigger_id=9995001, key='randomTalk', value=1)
            return 연출시작(self.ctx)
        if self.dungeon_max_user_count() == 2:
            # 던전 최대 인원수가 2이면
            self.set_user_value(trigger_id=9995002, key='randomTalk', value=1)
            self.set_user_value(trigger_id=9995003, key='randomTalk', value=1)
            return 연출시작(self.ctx)
        if self.dungeon_max_user_count() == 1:
            # 던전 최대 인원수가 1이면
            self.set_user_value(trigger_id=9995001, key='randomTalk', value=1)
            self.set_user_value(trigger_id=9995002, key='randomTalk', value=1)
            self.set_user_value(trigger_id=9995003, key='randomTalk', value=1)
            return 연출시작(self.ctx)
        if self.wait_tick(wait_tick=3000):
            self.set_user_value(trigger_id=9995001, key='randomTalk', value=1)
            self.set_user_value(trigger_id=9995002, key='randomTalk', value=1)
            self.set_user_value(trigger_id=9995003, key='randomTalk', value=1)
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=300)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=차어나운스03_1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차어나운스01_1(self.ctx)


class 차어나운스01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(visible=True)
        self.add_cinematic_talk(npc_id=11000032, illust_id='Anos_serious', msg='$02000066_BF__MAIN__4$', duration=5000, align=Align.Center)
        self.set_skip(state=차어나운스03_1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 차어나운스02_1(self.ctx)


class 차어나운스02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000032, illust_id='Anos_serious', msg='$02000066_BF__MAIN__5$', duration=5000, align=Align.Center)
        self.set_skip(state=차어나운스03_1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 차어나운스03_1(self.ctx)


class 차어나운스03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.select_camera(trigger_id=300, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=0, arg2='1,3')
        self.show_count_ui(text='$02000066_BF__MAIN__6$', stage=1, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 차웨이브1(self.ctx)


class 차웨이브1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='120', seconds=120, interval=1)
        self.spawn_monster(spawn_ids=[900], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            return 차웨이브성공1(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패1(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1003])
        self.destroy_monster(spawn_ids=[1004])
        self.destroy_monster(spawn_ids=[1005])
        self.destroy_monster(spawn_ids=[1006])
        self.destroy_monster(spawn_ids=[1007])
        self.destroy_monster(spawn_ids=[1008])
        self.destroy_monster(spawn_ids=[1101])
        self.destroy_monster(spawn_ids=[1102])
        self.destroy_monster(spawn_ids=[1103])
        self.destroy_monster(spawn_ids=[1104])
        self.destroy_monster(spawn_ids=[1105])
        self.destroy_monster(spawn_ids=[1106])
        self.destroy_monster(spawn_ids=[1107])
        self.destroy_monster(spawn_ids=[1108])
        self.destroy_monster(spawn_ids=[1201])
        self.destroy_monster(spawn_ids=[1202])
        self.destroy_monster(spawn_ids=[1203])
        self.destroy_monster(spawn_ids=[1204])
        self.destroy_monster(spawn_ids=[1205])
        self.destroy_monster(spawn_ids=[1206])
        self.destroy_monster(spawn_ids=[1207])
        self.destroy_monster(spawn_ids=[1208])
        self.destroy_monster(spawn_ids=[1299])
        self.destroy_monster(spawn_ids=[1301])
        self.destroy_monster(spawn_ids=[1302])
        self.destroy_monster(spawn_ids=[1303])
        self.destroy_monster(spawn_ids=[1304])
        self.destroy_monster(spawn_ids=[1305])
        self.destroy_monster(spawn_ids=[1306])
        self.destroy_monster(spawn_ids=[1307])
        self.destroy_monster(spawn_ids=[1308])
        self.destroy_monster(spawn_ids=[1401])
        self.destroy_monster(spawn_ids=[1402])
        self.destroy_monster(spawn_ids=[1403])
        self.destroy_monster(spawn_ids=[1404])
        self.destroy_monster(spawn_ids=[1601])
        self.destroy_monster(spawn_ids=[1602])
        self.destroy_monster(spawn_ids=[1603])
        self.destroy_monster(spawn_ids=[1604])


class 차웨이브실패1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[613], visible=True)
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__7$', arg3='3000', arg4='0')
        self.destroy_monster(spawn_ids=[900])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 실패(self.ctx)


class 차웨이브성공1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20000662, text_id=20000662)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.destroy_monster(spawn_ids=[900])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 차어나운스01_2(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패1(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20000662)


class 차어나운스01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20000665, text_id=20000665, duration=7000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 차어나운스02_2(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패1(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20000665)


class 차어나운스02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='2,3')
        self.show_count_ui(text='$02000066_BF__MAIN__10$', stage=2, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 차웨이브2(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패1(self.ctx)


class 차웨이브2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='120', seconds=120, interval=1)
        self.spawn_monster(spawn_ids=[901], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            return 차웨이브성공2(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패2(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1003])
        self.destroy_monster(spawn_ids=[1004])
        self.destroy_monster(spawn_ids=[1005])
        self.destroy_monster(spawn_ids=[1006])
        self.destroy_monster(spawn_ids=[1007])
        self.destroy_monster(spawn_ids=[1008])
        self.destroy_monster(spawn_ids=[1101])
        self.destroy_monster(spawn_ids=[1102])
        self.destroy_monster(spawn_ids=[1103])
        self.destroy_monster(spawn_ids=[1104])
        self.destroy_monster(spawn_ids=[1105])
        self.destroy_monster(spawn_ids=[1106])
        self.destroy_monster(spawn_ids=[1107])
        self.destroy_monster(spawn_ids=[1108])
        self.destroy_monster(spawn_ids=[1201])
        self.destroy_monster(spawn_ids=[1202])
        self.destroy_monster(spawn_ids=[1203])
        self.destroy_monster(spawn_ids=[1204])
        self.destroy_monster(spawn_ids=[1205])
        self.destroy_monster(spawn_ids=[1206])
        self.destroy_monster(spawn_ids=[1207])
        self.destroy_monster(spawn_ids=[1208])
        self.destroy_monster(spawn_ids=[1299])
        self.destroy_monster(spawn_ids=[1301])
        self.destroy_monster(spawn_ids=[1302])
        self.destroy_monster(spawn_ids=[1303])
        self.destroy_monster(spawn_ids=[1304])
        self.destroy_monster(spawn_ids=[1305])
        self.destroy_monster(spawn_ids=[1306])
        self.destroy_monster(spawn_ids=[1307])
        self.destroy_monster(spawn_ids=[1308])
        self.destroy_monster(spawn_ids=[1401])
        self.destroy_monster(spawn_ids=[1402])
        self.destroy_monster(spawn_ids=[1403])
        self.destroy_monster(spawn_ids=[1404])
        self.destroy_monster(spawn_ids=[1601])
        self.destroy_monster(spawn_ids=[1602])
        self.destroy_monster(spawn_ids=[1603])
        self.destroy_monster(spawn_ids=[1604])


class 차웨이브실패2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__11$', arg3='3000', arg4='0')
        self.destroy_monster(spawn_ids=[901])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 실패(self.ctx)


class 차웨이브성공2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20000662, text_id=20000662)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.destroy_monster(spawn_ids=[901])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패2(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 차어나운스01_3(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20000662)


class 차어나운스01_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20000665, text_id=20000665, duration=7000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패2(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 차어나운스02_3(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20000665)


class 차어나운스02_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='3,3')
        self.show_count_ui(text='$02000066_BF__MAIN__14$', stage=3, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패2(self.ctx)
        if self.wait_tick(wait_tick=6000):
            return 차웨이브3(self.ctx)


class 차웨이브3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='120', seconds=120, interval=1)
        self.spawn_monster(spawn_ids=[902], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            return 차웨이브성공3(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패3(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1003])
        self.destroy_monster(spawn_ids=[1004])
        self.destroy_monster(spawn_ids=[1005])
        self.destroy_monster(spawn_ids=[1006])
        self.destroy_monster(spawn_ids=[1007])
        self.destroy_monster(spawn_ids=[1008])
        self.destroy_monster(spawn_ids=[1101])
        self.destroy_monster(spawn_ids=[1102])
        self.destroy_monster(spawn_ids=[1103])
        self.destroy_monster(spawn_ids=[1104])
        self.destroy_monster(spawn_ids=[1105])
        self.destroy_monster(spawn_ids=[1106])
        self.destroy_monster(spawn_ids=[1107])
        self.destroy_monster(spawn_ids=[1108])
        self.destroy_monster(spawn_ids=[1201])
        self.destroy_monster(spawn_ids=[1202])
        self.destroy_monster(spawn_ids=[1203])
        self.destroy_monster(spawn_ids=[1204])
        self.destroy_monster(spawn_ids=[1205])
        self.destroy_monster(spawn_ids=[1206])
        self.destroy_monster(spawn_ids=[1207])
        self.destroy_monster(spawn_ids=[1208])
        self.destroy_monster(spawn_ids=[1299])
        self.destroy_monster(spawn_ids=[1301])
        self.destroy_monster(spawn_ids=[1302])
        self.destroy_monster(spawn_ids=[1303])
        self.destroy_monster(spawn_ids=[1304])
        self.destroy_monster(spawn_ids=[1305])
        self.destroy_monster(spawn_ids=[1306])
        self.destroy_monster(spawn_ids=[1307])
        self.destroy_monster(spawn_ids=[1308])
        self.destroy_monster(spawn_ids=[1401])
        self.destroy_monster(spawn_ids=[1402])
        self.destroy_monster(spawn_ids=[1403])
        self.destroy_monster(spawn_ids=[1404])
        self.destroy_monster(spawn_ids=[1601])
        self.destroy_monster(spawn_ids=[1602])
        self.destroy_monster(spawn_ids=[1603])
        self.destroy_monster(spawn_ids=[1604])


class 차웨이브실패3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__15$', arg3='3000', arg4='0')
        self.destroy_monster(spawn_ids=[902])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 실패(self.ctx)


class 차웨이브성공3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=7, arg2='$02000066_BF__MAIN__33$', arg3='3000', arg4='0')
        self.set_event_ui(type=0, arg2='0,0')
        self.set_effect(trigger_ids=[6003], visible=True)
        self.show_guide_summary(entity_id=20000662, text_id=20000662)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_achievement(trigger_id=103, type='trigger', achieve='EdgeofSpirits')
        self.destroy_monster(spawn_ids=[902])
        self.set_mesh(trigger_ids=[9001])
        self.destroy_monster(spawn_ids=[99])
        self.set_npc_emotion_loop(spawn_id=99, sequence_name='Attack_Idle_A', duration=1000000000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.set_effect(trigger_ids=[6003])
            return 차승리연출랜덤3(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20000662)


class 차승리연출랜덤3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return 차승리연출01_3(self.ctx)
        if self.random_condition(weight=20.0):
            return 차승리연출02_3(self.ctx)
        if self.random_condition(weight=20.0):
            return 차승리연출03_3(self.ctx)
        if self.random_condition(weight=20.0):
            return 차승리연출04_3(self.ctx)
        if self.random_condition(weight=20.0):
            return 차승리연출05_3(self.ctx)


class 차승리연출01_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__17$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차승리연출종료3(self.ctx)


class 차승리연출02_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__18$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 차승리연출종료3(self.ctx)


class 차승리연출03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__19$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 차승리연출종료3(self.ctx)


class 차승리연출04_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__20$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 차승리연출종료3(self.ctx)


class 차승리연출05_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__21$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5982):
            return 차승리연출종료3(self.ctx)


class 차승리연출종료3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 분기점(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=103, type='trigger', achieve='ClearAnosSOS') # ClearAnosSOS 퀘스트


class 분기점(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[612], visible=True)
        self.dungeon_clear()
        self.set_achievement(trigger_id=103, type='trigger', achieve='ClearLifeForest')
        self.set_user_value(trigger_id=10003067, key='woodsoflife', value=1)
        self.spawn_monster(spawn_ids=[907], auto_target=False)
        self.move_user(map_id=2000066, portal_id=3, box_id=103)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.show_guide_summary(entity_id=20000666, text_id=20000666)
            self.set_effect(trigger_ids=[620], visible=True)
            self.destroy_monster(spawn_ids=[907])
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='woodsoflife', value=0)


"""
class 분기점01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[612], visible=True)
        self.set_event_ui(type=1, arg2='$02000066_BF__MAIN__22$', arg3='10000')
        self.spawn_monster(spawn_ids=[903], auto_target=False)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_timer(timer_id='60', seconds=60, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='60'):
            self.destroy_monster(spawn_ids=[903])
            self.set_portal(portal_id=1)
            self.set_portal(portal_id=2)
            return 차어나운스01_4(self.ctx)
"""

"""
class 차어나운스01_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='4,6')
        self.set_event_ui(type=2, arg2='$02000066_BF__MAIN__23$', arg3='4,5')
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 차웨이브4(self.ctx)
"""

"""
class 차웨이브4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='120', seconds=120, interval=1)
        self.spawn_monster(spawn_ids=[99], auto_target=False)
        self.spawn_monster(spawn_ids=[904], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            return 차웨이브성공4(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패4(self.ctx)
"""

"""
class 차웨이브실패4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__24$', arg3='3000', arg4='0')
        self.set_timer(timer_id='3', seconds=3)
        self.destroy_monster(spawn_ids=[904])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 실패(self.ctx)
"""

"""
class 차웨이브성공4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20000662, text_id=20000662)
        self.set_timer(timer_id='5', seconds=5)
        self.destroy_monster(spawn_ids=[904])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패4(self.ctx)
        if self.time_expired(timer_id='5'):
            return 차어나운스01_5(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20000662)
"""

"""
class 차어나운스01_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000066_BF__MAIN__26$', arg3='7000', arg4='0')
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패4(self.ctx)
        if self.time_expired(timer_id='10'):
            return 차어나운스02_5(self.ctx)
"""

"""
class 차어나운스02_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='5,6')
        self.set_event_ui(type=2, arg2='$02000066_BF__MAIN__27$', arg3='5,5')
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 차웨이브5(self.ctx)
"""

"""
class 차웨이브5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='120', seconds=120, interval=1)
        self.spawn_monster(spawn_ids=[905], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            return 차웨이브성공5(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패5(self.ctx)
"""

"""
class 차웨이브실패5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__28$', arg3='5000', arg4='0')
        self.set_timer(timer_id='3', seconds=3)
        self.destroy_monster(spawn_ids=[905])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 실패(self.ctx)
"""

"""
class 차웨이브성공5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20000662, text_id=20000662)
        self.set_timer(timer_id='5', seconds=5)
        self.destroy_monster(spawn_ids=[905])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 차어나운스01_6(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패5(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20000662)
"""

"""
class 차어나운스01_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000066_BF__MAIN__30$', arg3='7000', arg4='0')
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 차어나운스02_6(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패5(self.ctx)
"""

"""
class 차어나운스02_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='6,6')
        self.set_event_ui(type=2, arg2='$02000066_BF__MAIN__31$', arg3='6,5')
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 차웨이브6(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패5(self.ctx)
"""

"""
class 차웨이브6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='120', seconds=120, interval=1)
        self.spawn_monster(spawn_ids=[906], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='120'):
            return 차웨이브성공6(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 차웨이브실패6(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[1001])
        self.destroy_monster(spawn_ids=[1002])
        self.destroy_monster(spawn_ids=[1003])
        self.destroy_monster(spawn_ids=[1004])
        self.destroy_monster(spawn_ids=[1005])
        self.destroy_monster(spawn_ids=[1006])
        self.destroy_monster(spawn_ids=[1007])
        self.destroy_monster(spawn_ids=[1008])
        self.destroy_monster(spawn_ids=[1101])
        self.destroy_monster(spawn_ids=[1102])
        self.destroy_monster(spawn_ids=[1103])
        self.destroy_monster(spawn_ids=[1104])
        self.destroy_monster(spawn_ids=[1105])
        self.destroy_monster(spawn_ids=[1106])
        self.destroy_monster(spawn_ids=[1107])
        self.destroy_monster(spawn_ids=[1108])
        self.destroy_monster(spawn_ids=[1201])
        self.destroy_monster(spawn_ids=[1202])
        self.destroy_monster(spawn_ids=[1203])
        self.destroy_monster(spawn_ids=[1204])
        self.destroy_monster(spawn_ids=[1205])
        self.destroy_monster(spawn_ids=[1206])
        self.destroy_monster(spawn_ids=[1207])
        self.destroy_monster(spawn_ids=[1208])
        self.destroy_monster(spawn_ids=[1299])
        self.destroy_monster(spawn_ids=[1301])
        self.destroy_monster(spawn_ids=[1302])
        self.destroy_monster(spawn_ids=[1303])
        self.destroy_monster(spawn_ids=[1304])
        self.destroy_monster(spawn_ids=[1305])
        self.destroy_monster(spawn_ids=[1306])
        self.destroy_monster(spawn_ids=[1307])
        self.destroy_monster(spawn_ids=[1308])
        self.destroy_monster(spawn_ids=[1401])
        self.destroy_monster(spawn_ids=[1402])
        self.destroy_monster(spawn_ids=[1403])
        self.destroy_monster(spawn_ids=[1404])
        self.destroy_monster(spawn_ids=[1601])
        self.destroy_monster(spawn_ids=[1602])
        self.destroy_monster(spawn_ids=[1603])
        self.destroy_monster(spawn_ids=[1604])
"""

"""
class 차웨이브실패6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02000066_BF__MAIN__32$', arg3='3000', arg4='0')
        self.set_timer(timer_id='3', seconds=3)
        self.destroy_monster(spawn_ids=[906])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 실패(self.ctx)
"""

"""
class 차웨이브성공6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003], visible=True)
        self.set_achievement(trigger_id=103, type='trigger', achieve='EdgeofSpirits')
        self.show_guide_summary(entity_id=20000662, text_id=20000662)
        self.set_timer(timer_id='5', seconds=5)
        self.destroy_monster(spawn_ids=[906])
        self.destroy_monster(spawn_ids=[99])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.set_effect(trigger_ids=[6003])
            return 차승리연출랜덤6(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20000662)
"""

"""
class 차승리연출랜덤6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip() # Missing State: 차승리연출종료6

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20.0):
            return 차승리연출01_6(self.ctx)
        if self.random_condition(weight=20.0):
            return 차승리연출02_6(self.ctx)
        if self.random_condition(weight=20.0):
            return 차승리연출03_6(self.ctx)
        if self.random_condition(weight=20.0):
            return 차승리연출04_6(self.ctx)
        if self.random_condition(weight=20.0):
            return 차승리연출05_6(self.ctx)
"""

"""
class 차승리연출01_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__34$', time=3)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 차승리연출종료6(self.ctx)
"""

"""
class 차승리연출02_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__35$', time=3)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 차승리연출종료6(self.ctx)
"""

"""
class 차승리연출03_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__36$', time=3)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 차승리연출종료6(self.ctx)
"""

"""
class 차승리연출04_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(visible=True)
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__37$', time=5)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 차승리연출종료6(self.ctx)
"""

"""
class 차승리연출05_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[610], visible=True)
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__38$', time=3)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 차승리연출종료6(self.ctx)
"""

"""
class 차승리연출종료6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 분기점03(self.ctx)
"""

"""
class 분기점03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[612], visible=True)
        self.set_event_ui(type=1, arg2='$02000066_BF__MAIN__39$', arg3='10000')
        self.spawn_monster(spawn_ids=[907], auto_target=False)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_timer(timer_id='60', seconds=60, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='60'):
            self.destroy_monster(spawn_ids=[907])
            return 완료(self.ctx)
"""

class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # self.set_skip(state=실패연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=15.0):
            return 실패연출01(self.ctx)
        if self.random_condition(weight=15.0):
            return 실패연출02(self.ctx)
        if self.random_condition(weight=14.0):
            return 실패연출03(self.ctx)
        if self.random_condition(weight=14.0):
            return 실패연출04(self.ctx)
        if self.random_condition(weight=14.0):
            return 실패연출05(self.ctx)
        if self.random_condition(weight=14.0):
            return 실패연출06(self.ctx)
        if self.random_condition(weight=14.0):
            return 실패연출07(self.ctx)


class 실패연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__40$', time=3)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 실패연출종료(self.ctx)


class 실패연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__41$', time=3)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 실패연출종료(self.ctx)


class 실패연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__42$', time=5)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 실패연출종료(self.ctx)


class 실패연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__43$', time=5)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 실패연출종료(self.ctx)


class 실패연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__44$', time=5)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 실패연출종료(self.ctx)


class 실패연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__45$', time=6)
        self.set_timer(timer_id='7', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='7'):
            return 실패연출종료(self.ctx)


class 실패연출07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000068, script='$02000066_BF__MAIN__46$', time=4)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 실패연출종료(self.ctx)


class 실패연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 실패강제이동(self.ctx)


class 실패강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5)
        self.move_user()

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            self.move_user()
            return 대기(self.ctx)


initial_state = 대기
