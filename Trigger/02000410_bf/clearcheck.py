""" trigger/02000410_bf/clearcheck.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면, 750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_play_time() >= 420:
            # 플레이 시간이 7분 되면, 전멸체크 로직 부분으로 넘어가기
            return 지금부터파티전멸체크(self.ctx)
        if self.user_value(key='ThirdPhase') == 1:
            # 2페이즈 전투 다 끝나고 , 파괴되어진 AI_AirshipBalrogCrimsonBroken.xml 인페르녹 전함에게   ThirdPhase = 1 신호를 받을때까지 여기서 대기, 즉 AI_AirshipBalrogCrimsonBroken.xml 에서 보냄
            return 지금부터파티전멸체크(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 파티장이 던전을 포기해서 실패한 경우
            return 던전포기(self.ctx)


class 지금부터파티전멸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[700]):
            # MS2TriggerBox   TriggerObjectID = 700 , 이 트리거 박스 안에 플레이어가 한명도 없다면, 700은 전투판만 포함되는 범위, 750은 스타팅 지점 전투판 다  포함되는 범위
            # MS2TriggerBox   TriggerObjectID = 700 ,  꼭 700 번을 사용해야 함, 실수로 750 설정하면 대박 버그임
            return 전멸던전실패연출01(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 파티장이 던전을 포기해서 실패한 경우
            return 던전포기(self.ctx)
        if self.dungeon_play_time() >= 900:
            # 플레이 시간이 15분 다 됬으면 던전 클리어 처리하기
            return 분완료15(self.ctx)


class 던전포기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 던전 포기 버튼 누르면 바로 몬스터 제거하기
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전멸던전실패연출01(self.ctx)


class 전멸던전실패연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ## 실패연출 설정 작업은 여기서 정의함
        self.side_npc_talk(npc_id=11000144, illust='tristan_normal', duration=4000, script='$02000410_BF__ClearCheck__0$', voice='ko/Npc/00002171')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전멸던전실패연출02(self.ctx)


class 전멸던전실패연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ## 실패연출 설정 작업은 여기서 정의함
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=4000, script='$02000410_BF__ClearCheck__1$', voice='ko/Npc/00002156')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전멸던전실패(self.ctx)


class 전멸던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # 던전 나가기 위한 포탈 생성,   arg1="1" 은 포탈ID, 전투판에 있는 포탈
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
            # 던전 나가기 위한 포탈 생성,   arg1="2" 은 포탈ID, 안전 부활 지점에 있는 포탈
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 분완료15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ## 한국용 던전랭크 코드: 15분 경과시 던전랭크 체크하기 위한 신호
        self.dungeon_mission_complete(feature='DungeonRankBalance_01', mission_id=24090003)
        # ## 중국용 던전랭크 코드: 15분 경과시 던전랭크 체크하기 위한 신호
        self.dungeon_mission_complete(feature='DungeonRankBalance_02', mission_id=24090013)

    def on_tick(self) -> trigger_api.Trigger:
        # 인페르녹 보스 스폰ID : 102 의 몬스터가 지금까지 받은 대미지가 HP 기준 대비 100%보다 적으면 던전 실패 처리
        if self.npc_damage(spawn_id=102) >= 1.0:
            return 성공연출시작(self.ctx)
        """
        condition name="CheckNpcDamage"   파라미터 기능 설명

                    spawnPointID: 체크할 NPC스폰포인트ID 스포너 안에 여러 NPC가 있을 경우 맨 첫 NPC를 체크합니다.
                    damageRate: 누적 대미지 기준 값 1.0 일경우 해당 npc의 maxHP 0.5의 경우 50%
                    operator: 연산자 기준 입니다 생략시 해당 값 이상 (GreaterEqual 이며) 다음 옵션을 사용 가능합니다.
                    Greater, GreaterEqual, Equal, LessEqual, Less,
        """
        if self.npc_damage(spawn_id=102) < 1.0:
            # 인페르녹 보스 스폰ID : 102
            return 실패연출시작(self.ctx)


class 성공연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 여기서는 인페르녹 보스 소멸 시키지 말고, AI쪽으로 EventClear = 1 신호 보내서 던전성공 이벤트 연출용도 NPC로 교체하고 본인 자신은 퇴장하도록 설정함
        self.set_ai_extra_data(key='EventClear', value=1)
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
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=8000, script='$02000410_BF__ClearCheck__3$', voice='ko/Npc/00002177')

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


class 실패연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 여기서는 인페르녹 보스 소멸 시키지 말고, AI쪽으로 EventLeave = 1 신호 보내서 던전실패 이벤트 연출용도 NPC로 교체하고 본인 자신은 퇴장하도록 설정함
        self.set_ai_extra_data(key='EventLeave', value=1)
        # 다섯번째팝업영상출력
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=3000, script='$02000410_BF__ClearCheck__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 실패연출01(self.ctx)


class 실패연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 다섯번째팝업영상출력
        # duration="0" 은 영상 끝날때까지 계속 출력
        self.side_npc_movie(usm='Common/WorldInvasionScene5.usm', duration=0)
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=8000, script='$02000410_BF__ClearCheck__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 실패연출02(self.ctx)


class 실패연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ## 실패연출 설정 작업은 여기서 정의함
        self.side_npc_talk(npc_id=11003795, illust='infernog_nomal', duration=4000, script='$02000410_BF__ClearCheck__6$', voice='ko/Monster/60000722')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 실패연출03(self.ctx)


class 실패연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ## 실패연출 설정 작업은 여기서 정의함
        self.side_npc_talk(npc_id=11003795, illust='infernog_nomal', duration=4000, script='$02000410_BF__ClearCheck__7$', voice='ko/Monster/60000723')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 실패연출05(self.ctx)


class 실패연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ## 실패연출 설정 작업은 여기서 정의함
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=4000, script='$02000410_BF__ClearCheck__8$', voice='ko/Npc/00002165')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 실패연출06(self.ctx)


class 실패연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ## 실패연출 설정 작업은 여기서 정의함
        self.side_npc_talk(npc_id=11003533, illust='Bliche_closeEye', duration=4000, script='$02000410_BF__ClearCheck__9$', voice='ko/Npc/00002155')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 최종실패처리(self.ctx)


class 최종성공처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 던전성공처리
        # 대포하고 12시 방향의 파괴 직전의 인페르녹 전함 제거함
        self.destroy_monster(spawn_ids=[-1])
        # arg3="ClearBalrogMagicBurster" 는 achieve.xlsx 의 코드 21230095 던전 클리어 조건 트로피 설정에 넣는 데이터임
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(trigger_id=750, type='trigger', achieve='infernogout')
        # arg1="750"는 MS2TriggerBox   TriggerObjectID = 750  이것으로 02000410 맵에 트리거 박스가 2개 있는데(700, 750)  750이 안전부활 장소까지 포함되는 범위라서 이거 사용함
        self.set_achievement(trigger_id=750, type='trigger', achieve='ClearBalrogMagicBurster')
        # 던전 나가기 위한 포탈 생성,   arg1="1" 은 포탈ID, 전투판에 있는 포탈
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        # 던전 나가기 위한 포탈 생성,   arg1="2" 은 포탈ID, 안전 부활 지점에 있는 포탈
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.dungeon_clear() # 던전성공

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 최종실패처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 던전실패처리
        # 대포하고 12시 방향의 파괴 직전의 인페르녹 전함 제거함
        self.destroy_monster(spawn_ids=[-1])
        self.set_achievement(trigger_id=750, type='trigger', achieve='infernogout')
        # 던전 나가기 위한 포탈 생성,   arg1="1" 은 포탈ID, 전투판에 있는 포탈
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        # 던전 나가기 위한 포탈 생성,   arg1="2" 은 포탈ID, 안전 부활 지점에 있는 포탈
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.dungeon_fail() # 던전실패

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_enable_give_up()


initial_state = Ready
