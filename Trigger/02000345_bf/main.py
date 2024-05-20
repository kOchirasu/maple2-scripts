""" trigger/02000345_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


"""
플레이어 감지
60002 : 모든 영역
"""
class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2001,2002], visible=True, start_delay=1, interval=1)
        self.remove_buff(box_id=60002, skill_id=99910040)
        self.remove_buff(box_id=60002, skill_id=70000106)
        self.spawn_monster(spawn_ids=[102]) # 촬영 감독
        self.set_mesh(trigger_ids=[6010], visible=True) # 벽 생성
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009]) # 길 차단

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=60001) >= 1:
            return CheckUserCount(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return start_game_01(self.ctx)


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
        self.move_random_user(map_id=2000345, portal_id=99, box_id=702, count=1)
        self.move_random_user(map_id=2000345, portal_id=98, box_id=60005, count=1)
        self.move_random_user(map_id=2000345, portal_id=97, box_id=60005, count=1)
        self.move_random_user(map_id=2000345, portal_id=96, box_id=60005, count=1)
        self.select_camera_path(path_ids=[8801,8802], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_01(self.ctx)


class start_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8802,8803], return_view=False)
        self.set_dialogue(type=1, spawn_id=102, script='$02000345_BF__MAIN__0$', time=2)
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000345_BF__MAIN__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000345_BF__MAIN__2$', time=2)
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000345_BF__MAIN__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000345_BF__MAIN__4$', time=2)
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000345_BF__MAIN__5$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000345_BF__MAIN__6$', time=2)
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000345_BF__MAIN__7$', time=3)

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
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000345_BF__MAIN__8$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001376, script='$02000345_BF__MAIN__9$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_game(self.ctx)


class start_game(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(path_ids=[8808])
        self.show_count_ui(text='$02000345_BF__MAIN__10$', count=3)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_game_01(self.ctx)


class start_game_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000345_BF__MAIN__11$', arg3='3000')
        self.spawn_monster(spawn_ids=[189])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_game_02(self.ctx)


class start_game_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8809,8810], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_game_02_b(self.ctx)


class start_game_02_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=189, script='$02000345_BF__MAIN__12$', time=2)
        self.set_dialogue(type=2, spawn_id=11001890, script='$02000345_BF__MAIN__13$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_game_03(self.ctx)


class start_game_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=189, script='$02000345_BF__MAIN__14$', time=3)
        self.set_dialogue(type=2, spawn_id=11001890, script='$02000345_BF__MAIN__15$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_game_04(self.ctx)


class start_game_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=189, script='$02000345_BF__MAIN__16$', time=3)
        self.set_dialogue(type=2, spawn_id=11001890, script='$02000345_BF__MAIN__17$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return start_game_05(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(path_ids=[8808])


class start_game_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000345_BF__MAIN__18$', arg3='3000')
        self.spawn_monster(spawn_ids=[201,202,203,204,205,206,207,208,209,210])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204,205,206,207,208,209,210]):
            return start_game_06(self.ctx)


class start_game_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306,307])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[301,302,303,304,305,306,307]):
            return start_game_07(self.ctx)


class start_game_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[401,402,403,404,405,406])


class 대기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4) # 보상으로 연결되는 포탈 제어 (끔)
        self.set_interact_object(trigger_ids=[10000791], state=0) # 보상 상태 (없음)
        self.set_mesh(trigger_ids=[6001,6010], visible=True) # 벽 생성
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009]) # 길 차단
        self.set_ladder(trigger_ids=[9001]) # 사다리 가려
        self.set_ladder(trigger_ids=[9002])
        self.set_ladder(trigger_ids=[9003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=60001) >= 1:
            return 대기_02(self.ctx)


class 대기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기_03(self.ctx)


class 대기_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=60001) >= 1:
            return 오브젝티브_01(self.ctx)


class 오브젝티브_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000345_BF__MAIN1__2$', arg3='10000')
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 오브젝티브_02(self.ctx)


class 오브젝티브_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001,8002]) # 연출 카메라
        self.spawn_monster(spawn_ids=[101]) # 보스 등장
        self.set_cinematic_ui(type=1)
        # self.move_user(map_id=2000345, portal_id=3)
        self.set_cinematic_ui(type=3, script='$02000345_BF__MAIN1__0$') # 오브젝티브
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 시작_01(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


# 플레이어 감지하면 1초 대기
class 시작_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$02000345_BF__MAIN1__3$', count=3)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 시작_02(self.ctx)


class 시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[9001], visible=True, enable=True) # 사다리 보여
        self.set_ladder(trigger_ids=[9002], visible=True, enable=True) # 사다리 보여
        self.set_ladder(trigger_ids=[9003], visible=True, enable=True) # 사다리 보여
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 클리어(self.ctx)


class 클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True) # 보상으로 연결되는 포탈 제어 (on)
        self.set_event_ui(type=7, arg2='$02000345_BF__MAIN1__1$', arg3='3000')
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009], visible=True, fade=10.0) # 길 생성
        self.set_mesh(trigger_ids=[6010]) # 벽 삭제
        self.set_interact_object(trigger_ids=[10000791], state=1) # 보상 상태 (없음)
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 클리어_02(self.ctx)


class 클리어_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=110, text_id=40009) # 포탈 이용하세요


initial_state = 대기
