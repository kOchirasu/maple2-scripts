""" trigger/02000429_bf/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 맨 오른쪽 지점에서 대포 배치하기 위한 오프젝트 생성하기 , TriggerObjectID: 6010, 6011
        self.set_mesh(trigger_ids=[6010,6011], visible=True, start_delay=1, interval=1)
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(trigger_ids=[6000,6001,6002,6003])
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(trigger_ids=[6004,6005])
        # 던전 나가기 위한 포탈 초기화 설정,   arg1="1" 은 포탈ID, 메인 전투판에 있는 포탈, 참고로 스타팅 포인트에 있는 나가가 포탈인 arg1="1" 은 활성화 상태로 배치함
        self.set_portal(portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면,          750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 전투시작_인페르녹전함(self.ctx)


class 전투시작_인페르녹전함(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 인페르녹 전함 스폰하기, 스폰ID : 101
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 첫번째페이즈_인페르녹전함(self.ctx)


class 첫번째페이즈_인페르녹전함(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SecondPhase') == 1:
            # 1페이즈 전투 진행하면서  SecondPhase = 1 신호를 받을때까지 여기서 대기
            return 두번째페이즈_인페르녹전함(self.ctx)
        if self.dungeon_timeout():
            # 시간이 다 되어서 실패한 경우
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 파티장이 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 두번째페이즈_인페르녹전함(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 맨 오른쪽 건너편 막힌 벽 제거하기 ,    오른쪽 지점 대포 배치하기 위한 오프젝트는 TriggerObjectID: 6010, 6011  이거 제거해야 전투가 쾌적함
        self.set_mesh(trigger_ids=[6010,6011,6012,6013,6014,6015,6016], fade=0.5)
        # <action feature="DungeonRankBalance_01" name="DungeonMissionComplete" missionID="24090007"/> ## 한국용 던전랭크 코드: 인페르녹의 전함 측면파괴 던전랭크 달성을 위한 신호
        # <action feature="DungeonRankBalance_02" name="DungeonMissionComplete" missionID="24090017"/> ## 중국용 던전랭크 코드: 인페르녹의 전함 측면파괴 던전랭크 달성을 위한 신호

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ThirdPhase') == 1:
            # 2페이즈 전투 진행하면서, 인페르녹 전함에게   ThirdPhase = 1 신호를 받을때까지 여기서 대기
            return 세번째페이즈_인페르녹등장(self.ctx)
        if self.dungeon_timeout():
            # 시간이 다 되어서 실패한 경우
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 파티장이 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 세번째페이즈_인페르녹등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 인페르녹 보스 스폰하기, 스폰ID : 102
        self.spawn_monster(spawn_ids=[102])
        self.set_sound(trigger_id=8410, enable=True) # 보스 등장하면 보스용 BGM으로 교체하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인페르녹전투시작(self.ctx)
        if self.dungeon_timeout():
            # 시간이 다 되어서 실패한 경우
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 파티장이 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 인페르녹전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[102]):
            # 인페르녹 보스 죽이면, 스폰ID : 102
            return 인페르녹처치성공(self.ctx)
        if self.dungeon_timeout():
            # 시간이 다 되어서 실패한 경우
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 파티장이 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


# 던전 포기 버튼 눌렸을 때 혹은 시간이 다 되었을때에 실패 일러스트 연출 처리하기 위한 장치 넣기, 그런데 이것은 1인 퀘스트용 던전이기 때문에 던전 포기나 시간 다 되는 경우 없어서 이 부분 실행 안할 것임
class 던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 던전 포기 버튼 누르면 바로 몬스터 제거하기
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전멸던전실패연출01(self.ctx)


class 전멸던전실패연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ## 실패연출 설정 작업은 여기서 정의함
        # 트리스탄의 "이런 시간이 부족한 건가?! 이대로면 버틸 수 없어!" 대사로, NA는 인페르녹 던전이 시간 버티기가 아닌 제한 시간까지 인페르녹 HP 다 까는 것이 목적이기 때문에 여기서의 트리스탄 대사는 NA만 다름
        self.side_npc_talk(npc_id=11003536, illust='tristan_normal', duration=4000, script='$02000410_BF__ClearCheck__10$')
        # 원래 여기에 ko/Npc/00002171 설정이 있었는데, 대사가 달라져서 음성 설정 빼기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전멸던전실패연출02(self.ctx)


class 전멸던전실패연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ## 실패연출 설정 작업은 여기서 정의함
        self.side_npc_talk(npc_id=11003536, illust='Bliche_nomal', duration=6200, script='$02000410_BF__ClearCheck__1$', voice='ko/Npc/00002156')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6200):
            return 전멸던전실패(self.ctx)


class 전멸던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # 던전 나가기 위한 포탈 생성,   arg1="1" 은 포탈ID, 메인 전투판에 있는 포탈
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 인페르녹처치성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg3="infernogout" 는 퀘스트 완료 조건 처리 키값임
        self.set_achievement(trigger_id=750, type='trigger', achieve='infernogout')
        # arg1="750"는 MS2TriggerBox   TriggerObjectID = 750  이것으로 02000410 맵에 트리거 박스가 2개 있는데(700, 750)  750이 안전부활 장소까지 포함되는 범위라서 이거 사용함
        # # DungeonMission.xml 에 등록된 숫자 코드 미션 완료 처리하기, 던전 클리어 미션 달성임
        self.dungeon_mission_complete(mission_id=23040000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 성공연출시작(self.ctx)


class 성공연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 다섯번째팝업영상출력
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=3000, script='$02000410_BF__ClearCheck__2$', voice='ko/Npc/00002182')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 성공연출01(self.ctx)


class 성공연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 다섯번째팝업영상출력
        # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_movie(usm='Common/WorldInvasionScene5.usm', duration=0)
        self.side_npc_talk(npc_id=11003536, illust='Bliche_nomal', duration=8000, script='$02000410_BF__ClearCheck__3$', voice='ko/Npc/00002177')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 성공연출02_pre(self.ctx)


class 성공연출02_pre(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 성공연출02(self.ctx)


class 성공연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='common\\WorldInvasionScene6.usm', movie_id=1, skip_type='needAll')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 최종성공처리(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 최종성공처리(self.ctx)


class 최종성공처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 던전성공처리
        # 대포하고 12시 방향의 파괴 직전의 인페르녹 전함 제거함
        self.destroy_monster(spawn_ids=[-1])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.show_guide_summary(entity_id=20041012, text_id=20041012) # 인페르녹 몰아내기 성공 알림 메시지
        # 던전 나가기 위한 포탈 생성,   arg1="1" 은 포탈ID, 전투판에 있는 포탈
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.dungeon_clear() # 던전성공

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20041012) # 인페르녹 몰아내기 성공 알림 메시지


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_enable_give_up()


initial_state = Ready
