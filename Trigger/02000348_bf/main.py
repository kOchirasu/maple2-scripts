""" trigger/02000348_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


"""
플레이어 감지
60002 : 모든 영역
"""
class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=34808, key='cage_01', value=0)
        self.set_user_value(trigger_id=34805, key='cage_02', value=0)
        self.set_user_value(trigger_id=34806, key='cage_03', value=0)
        self.set_user_value(trigger_id=34807, key='cage_04', value=0)
        self.set_mesh(trigger_ids=[2001,2002], visible=True, start_delay=1, interval=1)
        self.remove_buff(box_id=60002, skill_id=99910040)
        self.remove_buff(box_id=60002, skill_id=70000106)
        self.spawn_monster(spawn_ids=[102]) # 촬영 감독
        self.set_portal(portal_id=4) # 보상으로 연결되는 포탈 제어 (끔)
        self.set_interact_object(trigger_ids=[10000789], state=0) # 보상 상태 (없음)
        self.set_mesh(trigger_ids=[6010], visible=True) # 벽 생성
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009]) # 길 차단

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=60001) >= 1:
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return touchfield(self.ctx)


class touchfield(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2001,2002], interval=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_random_user(map_id=2000348, portal_id=99, box_id=702, count=1)
        self.move_random_user(map_id=2000348, portal_id=98, box_id=60005, count=1)
        self.move_random_user(map_id=2000348, portal_id=97, box_id=60005, count=1)
        self.move_random_user(map_id=2000348, portal_id=96, box_id=60005, count=1)
        self.select_camera_path(path_ids=[8801,8802], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_01(self.ctx)


class start_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8802,8803], return_view=False)
        self.set_dialogue(type=1, spawn_id=102, script='$02000348_BF__MAIN__0$', time=2)
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000348_BF__MAIN__1$', time=3)
        self.set_skip(state=start_game)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000348_BF__MAIN__2$', time=2)
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000348_BF__MAIN__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000348_BF__MAIN__4$', time=2)
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000348_BF__MAIN__5$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000348_BF__MAIN__6$', time=2)
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000348_BF__MAIN__7$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.add_buff(box_ids=[702], skill_id=99910040, level=1)
        self.add_buff(box_ids=[702], skill_id=70000106, level=1) # 카메라 스크린을 걸어준다.
        self.select_camera_path(path_ids=[8804,8805,8806,8807], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000348_BF__MAIN__8$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000348_BF__MAIN__9$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_game(self.ctx)


class start_game(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[702], skill_id=70000106, level=1) # 카메라 스크린을 걸어준다.
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(path_ids=[8808])
        self.show_count_ui(text='$02000348_BF__MAIN__10$', count=3)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_game_01(self.ctx)


class start_game_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003446, text_id=20003446, duration=5000)
        self.set_event_ui(type=1, arg2='$02000348_BF__MAIN__11$', arg3='3000')
        self.spawn_monster(spawn_ids=[201,202,203,204,211,212,213,214])
        self.set_user_value(trigger_id=34808, key='cage_01', value=1)
        self.set_user_value(trigger_id=34805, key='cage_02', value=1)
        self.set_user_value(trigger_id=34806, key='cage_03', value=1)
        self.set_user_value(trigger_id=34807, key='cage_04', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[211,212,213,214]):
            return start_game_02(self.ctx)


class start_game_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_game_03(self.ctx)


class start_game_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003442, text_id=20003442, duration=5000)
        self.spawn_monster(spawn_ids=[231,232])
        self.set_event_ui(type=1, arg2='$02000348_BF__MAIN__12$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_game_03_a(self.ctx)


class start_game_03_a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[233,234])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[231,232,233,234]):
            return start_game_03_b(self.ctx)


class start_game_03_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8811,8810])
        self.set_event_ui(type=1, arg2='$02000348_BF__MAIN__13$', arg3='3000')
        self.set_effect(trigger_ids=[7001], visible=True)
        self.set_skill(trigger_ids=[7702], enable=True)
        self.set_skill(trigger_ids=[7703], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return start_game_05(self.ctx)


class start_game_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000348_BF__MAIN__14$', arg3='3000')
        self.spawn_monster(spawn_ids=[101,205,206,207,208]) # 촬영 감독

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return start_game_06(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[205,206,207,208])


class start_game_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 클리어(self.ctx)


class 클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.remove_buff(box_id=60002, skill_id=99910040)
        self.remove_buff(box_id=60002, skill_id=70000106)
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True) # 보상으로 연결되는 포탈 제어 (on)
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=True, fade=10.0) # 길 생성
        self.set_mesh(trigger_ids=[6010]) # 벽 삭제
        self.set_interact_object(trigger_ids=[10000789], state=1) # 보상 상태 (없음)
        self.set_timer(timer_id='5', seconds=5)
        self.select_camera_path(path_ids=[8801,8803], return_view=False)
        self.set_skip(state=클리어_03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 클리어_02(self.ctx)


class 클리어_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000348_BF__MAIN__15$', time=2)
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000348_BF__MAIN__16$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 클리어_03(self.ctx)


class 클리어_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000348_BF__MAIN__17$', time=2)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 클리어_04(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[102])


class 클리어_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=1, value=1) # 1번 던전 클리어 처리
        self.show_guide_summary(entity_id=110, text_id=40009) # 포탈 이용하세요
        self.select_camera_path(path_ids=[8808])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
