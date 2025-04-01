""" trigger/02000376_bf/01_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3500,3501], visible=True) # Invisible_IronDoor
        self.set_mesh(trigger_ids=[3010,3011,3012,3013], visible=True) # Barrier
        self.set_mesh(trigger_ids=[3030], visible=True) # GatePortal
        self.set_mesh(trigger_ids=[3506,3507], visible=True) # EnterInvisibleBarrier
        self.set_mesh(trigger_ids=[3502,3503,3504,3505], visible=True) # EnterPillarBarrier
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Closed') # IronDoor
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Closed') # IronDoor
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='or_fi_struc_stonegate_A01_off') # StoneGate
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Closed') # EnterIronDoor
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[5000]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5001]) # StoneGate 사운드 이펙트
        self.set_effect(trigger_ids=[5004]) # MetalDoorOpen 사운드 이펙트
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_user_value(key='PuzzleSolved', value=0)
        self.set_user_value(key='PatrolEnd', value=0)
        self.spawn_monster(spawn_ids=[900], auto_target=False) # 어둠의 토템

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[100,200], auto_target=False)
        self.spawn_monster(spawn_ids=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826], auto_target=False) # 연출용 검은 그림자
        self.spawn_monster(spawn_ids=[950,951,952,953,954,955,956,958,959,961,963,964,965,966,969,970,973,974,976,977,978,979,981], auto_target=False) # 미혹의 령

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcMonologue01(self.ctx)


class NpcMonologue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=11, key='DungeonStart', value=1)
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Opened') # EnterIronDoor
        self.set_mesh(trigger_ids=[3506,3507]) # EnterInvisibleBarrier
        self.set_dialogue(type=1, spawn_id=100, script='$02000376_BF__01_MAIN__0$', time=3) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NpcMonologue02(self.ctx)


class NpcMonologue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4003, initial_sequence='Opened') # EnterIronDoor
        self.set_mesh(trigger_ids=[3502,3503,3504,3505], interval=100, fade=5.0) # EnterPillarBarrier
        self.move_npc(spawn_id=100, patrol_name='MS2PatrolData_100')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_200')
        self.set_dialogue(type=1, spawn_id=200, script='$02000376_BF__01_MAIN__1$', time=4) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return NpcPatrol01(self.ctx)


class NpcPatrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=10, key='PatrolStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NpcPatrol02(self.ctx)


class NpcPatrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02000376_BF__01_MAIN__2$', duration=5000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PatrolEnd') == 1:
            return NpcPatrol03(self.ctx)
        if self.monster_dead(spawn_ids=[900]):
            # 토템 제거
            return NpcChange01(self.ctx)


class NpcPatrol03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9400, spawn_ids=[202]):
            return NpcPatrol04(self.ctx)
        if self.monster_dead(spawn_ids=[900]):
            # 토템 제거
            return NpcChange01(self.ctx)


class NpcPatrol04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9400) >= 1:
            return FoundTotem01(self.ctx)
        if self.monster_dead(spawn_ids=[900]):
            # 토템 제거
            return NpcChange01(self.ctx)


# 20170223 업데이트 던전 개편 단축
class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,201])
        self.destroy_monster(spawn_ids=[102,202])
        self.spawn_monster(spawn_ids=[105,205], auto_target=False) # 연출용

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return RemoveTotem02(self.ctx)


class NpcChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,201])
        self.destroy_monster(spawn_ids=[102,202])
        self.destroy_monster(spawn_ids=[103,203]) # 전투
        self.spawn_monster(spawn_ids=[105,205], auto_target=False) # 연출용
        self.remove_balloon_talk(spawn_id=203)
        self.remove_balloon_talk(spawn_id=103)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return RemoveTotem02(self.ctx)


class FoundTotem01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,201])
        self.destroy_monster(spawn_ids=[102,202])
        self.spawn_monster(spawn_ids=[103,203], auto_target=False) # 전투
        self.set_dialogue(type=1, spawn_id=203, script='$02000376_BF__01_MAIN__3$', time=3) # 준타
        self.set_dialogue(type=1, spawn_id=103, script='$02000376_BF__01_MAIN__4$', time=3, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return RemoveTotem01(self.ctx)
        if self.monster_dead(spawn_ids=[900]):
            # 토템 제거
            return NpcChange02(self.ctx)


class RemoveTotem01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[900]):
            # 토템 제거
            return RemoveTotem02(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[101,201])
        self.destroy_monster(spawn_ids=[102,202])
        self.destroy_monster(spawn_ids=[103,203]) # 전투
        self.spawn_monster(spawn_ids=[105,205], auto_target=False)
        self.remove_balloon_talk(spawn_id=203)
        self.remove_balloon_talk(spawn_id=103)


class RemoveTotem02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,201])
        self.destroy_monster(spawn_ids=[102,202])
        self.move_npc(spawn_id=950, patrol_name='MS2PatrolData_850')
        self.move_npc(spawn_id=951, patrol_name='MS2PatrolData_851')
        self.move_npc(spawn_id=952, patrol_name='MS2PatrolData_852')
        self.move_npc(spawn_id=953, patrol_name='MS2PatrolData_853')
        self.move_npc(spawn_id=954, patrol_name='MS2PatrolData_854')
        self.move_npc(spawn_id=955, patrol_name='MS2PatrolData_855')
        self.move_npc(spawn_id=956, patrol_name='MS2PatrolData_856')
        self.move_npc(spawn_id=958, patrol_name='MS2PatrolData_858')
        self.move_npc(spawn_id=959, patrol_name='MS2PatrolData_859')
        self.move_npc(spawn_id=961, patrol_name='MS2PatrolData_861')
        self.move_npc(spawn_id=963, patrol_name='MS2PatrolData_863')
        self.move_npc(spawn_id=964, patrol_name='MS2PatrolData_864')
        self.move_npc(spawn_id=965, patrol_name='MS2PatrolData_865')
        self.move_npc(spawn_id=966, patrol_name='MS2PatrolData_866')
        self.move_npc(spawn_id=969, patrol_name='MS2PatrolData_869')
        self.move_npc(spawn_id=970, patrol_name='MS2PatrolData_870')
        self.move_npc(spawn_id=973, patrol_name='MS2PatrolData_873')
        self.move_npc(spawn_id=974, patrol_name='MS2PatrolData_874')
        self.move_npc(spawn_id=976, patrol_name='MS2PatrolData_876')
        self.move_npc(spawn_id=977, patrol_name='MS2PatrolData_877')
        self.move_npc(spawn_id=978, patrol_name='MS2PatrolData_878')
        self.move_npc(spawn_id=979, patrol_name='MS2PatrolData_879')
        self.move_npc(spawn_id=981, patrol_name='MS2PatrolData_881')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return RemoveTotem03(self.ctx)


# NPC 말풍선 어둠이 걷혔어
class RemoveTotem03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102,202])
        self.change_monster(from_spawn_id=950, to_spawn_id=850)
        self.change_monster(from_spawn_id=951, to_spawn_id=851)
        self.change_monster(from_spawn_id=952, to_spawn_id=852)
        self.change_monster(from_spawn_id=953, to_spawn_id=853)
        self.change_monster(from_spawn_id=954, to_spawn_id=854)
        self.change_monster(from_spawn_id=955, to_spawn_id=855)
        self.change_monster(from_spawn_id=956, to_spawn_id=856)
        self.change_monster(from_spawn_id=958, to_spawn_id=858)
        self.change_monster(from_spawn_id=959, to_spawn_id=859)
        self.change_monster(from_spawn_id=961, to_spawn_id=861)
        self.change_monster(from_spawn_id=963, to_spawn_id=863)
        self.change_monster(from_spawn_id=964, to_spawn_id=864)
        self.change_monster(from_spawn_id=965, to_spawn_id=865)
        self.change_monster(from_spawn_id=966, to_spawn_id=866)
        self.change_monster(from_spawn_id=968, to_spawn_id=868)
        self.change_monster(from_spawn_id=969, to_spawn_id=869)
        self.change_monster(from_spawn_id=970, to_spawn_id=870)
        self.change_monster(from_spawn_id=973, to_spawn_id=873)
        self.change_monster(from_spawn_id=974, to_spawn_id=874)
        self.change_monster(from_spawn_id=976, to_spawn_id=876)
        self.change_monster(from_spawn_id=977, to_spawn_id=877)
        self.change_monster(from_spawn_id=978, to_spawn_id=878)
        self.change_monster(from_spawn_id=979, to_spawn_id=879)
        self.change_monster(from_spawn_id=981, to_spawn_id=881)
        self.set_dialogue(type=1, spawn_id=105, script='$02000376_BF__01_MAIN__5$', time=3, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return RemoveTotem04(self.ctx)


class RemoveTotem04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102,202])
        self.set_dialogue(type=1, spawn_id=205, script='$02000376_BF__01_MAIN__6$', time=3, arg5=2) # 준타
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_106')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_206')
        self.set_mesh(trigger_ids=[3500,3501]) # Invisible_IronDoor
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Opened') # IronDoor
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Opened') # IronDoor
        self.set_effect(trigger_ids=[5004], visible=True) # MetalDoorOpen 사운드 이펙트
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FoundGate01(self.ctx)


class FoundGate01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102,202])
        self.set_dialogue(type=1, spawn_id=205, script='$02000376_BF__01_MAIN__7$', time=2) # 준타
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_107')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_207')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9500, spawn_ids=[105]):
            return FoundGate02(self.ctx)


class FoundGate02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=105, script='$02000376_BF__01_MAIN__8$', time=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9501, spawn_ids=[105]):
            return ShadowApp01(self.ctx)


class ShadowApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=205, script='$02000376_BF__01_MAIN__9$', time=2) # 준타
        self.spawn_monster(spawn_ids=[901,902,903,904,905,906,907,908], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return ShadowApp02(self.ctx)


class ShadowApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[105,205]) # 전투
        self.spawn_monster(spawn_ids=[106,206], auto_target=False)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui_script(type=BannerType.Text, script='$02000376_BF__01_MAIN__10$', duration=3000, box_ids=['0'])
        self.spawn_monster(spawn_ids=[911,912,913,914,915,916,917,918], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return ShadowApp03(self.ctx)


class ShadowApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[921,922,923,924,925,926,927,928], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ShadowApp04(self.ctx)


class ShadowApp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[931,932,933,934,935,936,937,938], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903,904,905,906,907,908,911,912,913,914,915,916,917,918,921,922,923,924,925,926,927,928,931,932,933,934,935,936,937,938]):
            return StartPuzzle01(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[106,206])
        self.spawn_monster(spawn_ids=[104,204], auto_target=False) # 연출용 NPC


class StartPuzzle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='PuzzleStart', value=1)
        self.set_dialogue(type=1, spawn_id=104, script='$02000376_BF__01_MAIN__11$', time=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return StartPuzzle02(self.ctx)


class StartPuzzle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui_script(type=BannerType.Text, script='$02000376_BF__01_MAIN__12$', duration=5000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return EndPuzzle01(self.ctx)


# NPC 말풍선 퍼즐에 대한 멘트 스크립트 모노로그
class EndPuzzle01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PuzzleSolved') == 1:
            return GateOpen01(self.ctx)


class GateOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True) # StoneGate 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return GateOpen02(self.ctx)


class GateOpen02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_108')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_208')
        self.set_dialogue(type=1, spawn_id=104, script='$02000376_BF__01_MAIN__13$', time=2) # 틴차이
        self.set_dialogue(type=1, spawn_id=204, script='$02000376_BF__01_MAIN__14$', time=2, arg5=2) # 준타
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='or_fi_struc_stonegate_A01_on') # StoneGate
        self.set_mesh(trigger_ids=[3030]) # GatePortal
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return GateOpen03(self.ctx)


class GateOpen03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_109')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_209')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104,204])


initial_state = Wait
