""" trigger/02000334_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


# 플레이어 감지
class main(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=12)
        self.set_interact_object(trigger_ids=[13000012], state=2) # 보상 상태 (없음)
        self.set_effect(trigger_ids=[98001])
        self.set_effect(trigger_ids=[98002])
        self.set_effect(trigger_ids=[98003])
        self.set_effect(trigger_ids=[98004])
        self.set_effect(trigger_ids=[98005])
        self.set_effect(trigger_ids=[98006])
        self.set_effect(trigger_ids=[90021])
        self.set_effect(trigger_ids=[90022])
        self.set_effect(trigger_ids=[98031], visible=True)
        self.select_camera(trigger_id=8000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=90001) >= 1:
            return CheckUserCount(self.ctx)


# 플레이어 감지하면 1초 대기
class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10) # 보상으로 연결되는 포탈 제어 (끔)
        self.spawn_monster(spawn_ids=[199]) # 퀘스트 주는 NPC가 앞으로 걸어나옴
        self.select_camera(trigger_id=8001) # 연출 카메라
        self.set_timer(timer_id='1', seconds=1)
        self.spawn_monster(spawn_ids=[401,402,403,404,405,406]) # 성벽 지키는 NPC 소환
        self.spawn_monster(spawn_ids=[801,802,803,804,805,806,807,808,809]) # 성벽 지키는 NPC 소환
        self.set_mesh(trigger_ids=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015,6016], visible=True) # 가림막

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작_02(self.ctx)


class 시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1초 대기 경과하면 UI연출 출력
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='5', seconds=5)
        self.set_skip(state=시작_03)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 시작_03(self.ctx)


class 시작_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=2, spawn_id=11000015, script='$02000334_BF__MAIN__1$', time=3) # 오스칼 대사
        self.spawn_monster(spawn_ids=[190], auto_target=False) # 보스 등장
        self.set_skip(state=단계_시작1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 단계_시작1(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.set_cinematic_ui(type=4)


"""
해당 단계에서 플레이어의 위치를 조명해줌
1 단계 시작 카운트
"""
class 단계_시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8013,8015], return_view=False) # 사이드뷰 카메라
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 단계_시작02_1(self.ctx)


class 단계_시작02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=24001205, script='$02000334_BF__MAIN__6$', time=3) # 보스 대사 : 성벽따위 금방 부숴주지
        self.set_timer(timer_id='3', seconds=3)
        self.set_skip(state=단계_시작03_1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 단계_시작03_1(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 단계_시작03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='1,4')
        self.show_count_ui(text='$02000334_BF__MAIN__2$', stage=1, count=5)
        self.set_timer(timer_id='4', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 단계_시작04_1(self.ctx)


class 단계_시작04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=199, script='$02000334_BF__MAIN__3$', time=3) # 오스칼 말풍선 대사
        self.spawn_monster(spawn_ids=[201,203]) # 성벽 지키는 NPC 리필
        self.set_dialogue(type=1, spawn_id=203, script='$02000334_BF__MAIN__4$', time=3) # 병사 말풍선 대사
        self.set_dialogue(type=1, spawn_id=201, script='$02000334_BF__MAIN__5$', time=3) # 병사 말풍선 대사
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 단계_타이머1(self.ctx)
        if self.monster_dead(spawn_ids=[999]):
            return 게임오버(self.ctx)


# 1 단계 시작
class 단계_타이머1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[90022], visible=True) # 점프 뛰는 소리 ON
        self.spawn_monster(spawn_ids=[160], auto_target=False) # 웨이브 가이드
        self.spawn_monster(spawn_ids=[150], auto_target=False)
        self.set_timer(timer_id='60', seconds=60, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='60'):
            return 단계_준비2(self.ctx)
        if self.monster_dead(spawn_ids=[999]):
            return 게임오버(self.ctx)
        if self.user_detected(box_ids=[99999]):
            # 임시로 다음 트리거로 보내기
            return 클리어(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[90022]) # 점프 뛰는 소리 OFF


class 단계_준비2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,991,992,993,994,995,996,997,998])
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=2, spawn_id=11000015, script='$02000334_BF__MAIN__7$', time=3) # 오스칼 대사
        self.set_skip(state=단계_시작2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 단계_시작2(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


# 2 단계 시작 카운트
class 단계_시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[204,205]) # 성벽 지키는 NPC 리필
        self.set_dialogue(type=1, spawn_id=199, script='$02000334_BF__MAIN__8$', time=3) # 오스칼 대사
        self.set_mesh(trigger_ids=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015,6016], interval=250, fade=1.0) # 가림막 해제
        self.set_event_ui(type=0, arg2='2,4')
        self.show_count_ui(text='$02000334_BF__MAIN__2$', stage=2, count=5)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 단계_타이머2(self.ctx)
        if self.monster_dead(spawn_ids=[999]):
            return 게임오버(self.ctx)


# 2 단계 시작
class 단계_타이머2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[90022], visible=True) # 점프 뛰는 소리 ON
        self.select_camera(trigger_id=8000) # 사이드뷰 카메라
        self.spawn_monster(spawn_ids=[150,151], auto_target=False) # 1,2 차 웨이브 몬스터 작동 장치
        self.set_timer(timer_id='60', seconds=60, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='60'):
            return 단계_준비3(self.ctx)
        if self.monster_dead(spawn_ids=[999]):
            return 게임오버(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[90022]) # 점프 뛰는 소리 OFF


class 단계_준비3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,991,992,993,994,995,996,997,998])
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=2, spawn_id=11000015, script='$02000334_BF__MAIN__9$', time=3) # 오스칼 대사
        self.set_skip(state=단계_시작3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 단계_시작3(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


# 3 단계 시작 카운트
class 단계_시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[206,207]) # 성벽 지키는 NPC 리필
        self.set_event_ui(type=0, arg2='3,4')
        self.show_count_ui(text='$02000334_BF__MAIN__2$', stage=3, count=5)
        self.set_timer(timer_id='6', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 단계_타이머3(self.ctx)
        if self.monster_dead(spawn_ids=[999]):
            return 게임오버(self.ctx)


# 3 단계 시작
class 단계_타이머3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[90022], visible=True) # 점프 뛰는 소리 ON
        self.spawn_monster(spawn_ids=[150,151,152], auto_target=False) # 1,2,3차 웨이브 몬스터 작동 장치
        self.set_timer(timer_id='60', seconds=60, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='60'):
            return 단계_준비_01_4(self.ctx)
        if self.monster_dead(spawn_ids=[999]):
            return 게임오버(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[90022]) # 점프 뛰는 소리 OFF


class 단계_준비_01_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,991,992,993,994,995,996,997,998])
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=2, spawn_id=11000015, script='$02000334_BF__MAIN__10$', time=3) # 오스칼 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 단계_준비_02_4(self.ctx)


class 단계_준비_02_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=2, spawn_id=24001205, script='$02000334_BF__MAIN__11$', time=3) # 보스 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 단계_시작4(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


# 4 단계 시작 카운트
class 단계_시작4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,991,992,993,994,995,996,997,998])
        self.move_npc(spawn_id=190, patrol_name='MS2PatrolData_2999') # 보스 등장
        self.set_event_ui(type=0, arg2='4,4')
        self.show_count_ui(text='$02000334_BF__MAIN__2$', stage=4, count=5)
        self.set_timer(timer_id='6', seconds=6)
        self.set_dialogue(type=1, spawn_id=190, script='$02000334_BF__WAVE__2$', time=3) # 보스 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 단계_타이머4(self.ctx)
        if self.monster_dead(spawn_ids=[999]):
            return 게임오버(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[150,151], auto_target=False) # 1,2차 웨이브 몬스터 작동 장치


# 4 단계 시작
class 단계_타이머4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[90022], visible=True) # 점프 뛰는 소리 ON
        self.set_timer(timer_id='150', seconds=150, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[999]):
            return 게임오버(self.ctx)
        if self.time_expired(timer_id='150'):
            return 게임오버(self.ctx)
        if self.monster_dead(spawn_ids=[190]):
            return 클리어(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[90022]) # 점프 뛰는 소리 OFF


# 게임 오버 스테이트
class 게임오버(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,190,991,992,993,994,995,996,997,998])
        self.set_event_ui(type=5, arg3='3000')
        self.set_event_ui(type=0, arg2='0,0')
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[98031])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 게임오버_이벤트(self.ctx)


class 게임오버_이벤트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,190,991,992,993,994,995,996,997,998])
        self.set_timer(timer_id='3', seconds=3)
        self.set_dialogue(type=2, spawn_id=24001205, script='$02000334_BF__MAIN__13$', time=3) # 보스 대사
        self.set_skip(state=게임오버_강퇴)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 게임오버_강퇴(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 게임오버_강퇴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=5, interval=1)
        self.set_event_ui(type=1, arg2='$02000334_BF__MAIN__14$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 강퇴(self.ctx)


class 강퇴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(box_id=90001)


# 클리어
class 클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=90001, type='trigger', achieve='TaboKill') # 돼지왕 타보 죽임 처리
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,991,992,993,994,995,996,997,998]) # 폭죽 터뜨림
        self.set_effect(trigger_ids=[98002], visible=True)
        self.set_effect(trigger_ids=[98003], visible=True)
        self.set_effect(trigger_ids=[98004], visible=True)
        self.set_effect(trigger_ids=[98005], visible=True)
        self.set_timer(timer_id='3', seconds=3)
        self.set_effect(trigger_ids=[98031])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 클리어_이벤트(self.ctx)

    def on_exit(self) -> None:
        # 폭죽 정지
        self.set_effect(trigger_ids=[98002])
        self.set_effect(trigger_ids=[98003])
        self.set_effect(trigger_ids=[98004])
        self.set_effect(trigger_ids=[98005])


class 클리어_이벤트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,131,132,133,134,135,150,151,152,991,992,993,994,995,996,997,998]) # 몬스터 정리
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000015, script='$02000334_BF__MAIN__16$', time=3) # 오스칼 대사
        self.set_mesh(trigger_ids=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015,6016], interval=250, fade=1.0) # 가림막 해제
        self.set_skip(state=클리어_보상)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 클리어_보상(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 클리어_보상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=10, visible=True, enable=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=103, text_id=40009) # 포탈로 이동하세요
        # self.set_event_ui(type=1, arg2='$02000334_BF__MAIN__17$', arg3='10000')
        self.move_npc(spawn_id=199, patrol_name='MS2PatrolData_2015') # 오스칼 장소 이동
        self.set_timer(timer_id='10', seconds=10, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[90099]):
            return 클리어_보상_02(self.ctx)
        if self.time_expired(timer_id='10'):
            return 클리어_보상_02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=103)


class 클리어_보상_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8003) # 연출 카메라
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000015, script='$02000334_BF__MAIN__18$', time=3) # 오스칼 대사
        self.set_timer(timer_id='3', seconds=3)
        # self.set_interact_object(trigger_ids=[13000012], state=1) # 보상 상태 개방

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 클리어_보상_03(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 클리어_보상_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=199, script='$02000334_BF__MAIN__19$', time=5) # 오스칼 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.dungeon_clear()
            self.set_portal(portal_id=12, visible=True, enable=True, minimap_visible=True)
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=103)


class 종료(trigger_api.Trigger):
    pass


initial_state = main
