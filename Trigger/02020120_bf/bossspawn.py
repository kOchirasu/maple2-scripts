""" trigger/02020120_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(trigger_ids=[1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937])
        self.set_portal(portal_id=2)
        # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        self.set_user_value(key='DungeonReset', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            # MS2TriggerBox   TriggerObjectID = 199, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        199은 스타팅 포인트 지점만 커버하는 비교적 좁은 범위
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 던전 시간 12분 설정 초기화 하기 , 이 던전의 시간 설정은 DoungeonRoom.xml 이 아닌 여기서 진행함
        self.dungeon_reset_time(seconds=720)
        self.side_npc_talk(npc_id=23000113, illust='Ishura_Dark_Idle', script='$02020120_BF__BOSSSPAWN__0$', duration=4000, voice='ko/Npc/00002192')
        self.spawn_monster(spawn_ids=[99], auto_target=False) # 이슈라 등장
        # 버그 때문에 이거 사용 안함, 그렇다고 이거 지우면 대박 버그 생기니 조심 그냥 내버려 두자, 다시 처음으로 되돌리는 순간이동 포탈 Off 처리 하는거 여기서 하기, 스킬브레이크 막기 실패하여 던전 초기화 될 경우를 대비해 여기서 초기화 처리 하는 것이 좋음, 보스 메인 전투판 주변 범위의 포발
        self.set_portal(portal_id=9901)
        # 버그 때문에 이거 사용 안함, 그렇다고 이거 지우면 대박 버그 생기니 조심 그냥 내버려 두자, 다시 처음으로 되돌리는 순간이동 포탈 Off 처리 하는거 여기서 하기, 스킬브레이크 막기 실패하여 던전 초기화 될 경우를 대비해 여기서 초기화 처리 하는 것이 좋음, 스타팅 포인트 근처 주변 범위의 포발
        self.set_portal(portal_id=9902)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonReset') == 1:
            return 던전초기화진행(self.ctx) # @####@##
        if self.monster_dead(spawn_ids=[99]):
            return 종료딜레이(self.ctx)
        if self.dungeon_timeout():
            return 던전실패(self.ctx)
        if self.dungeon_state() == 'Fail':
            # 던전을 포기해서 실패한 경우
            return 던전실패(self.ctx)


class 던전초기화진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 맵 안에 있는 모든 플레이어를 스타팅 지점에 있는 포탈로 이동시킴, arg1 은 이동시킬 맵 코드, arg2 은 도착 장소 포탈ID 임
        self.move_user(map_id=2020120, portal_id=9903)
        # 던전 초기화 되면 노말 BGM으로 교체함, 보스 BGM 교체 설정은 BgmChangeSkillBreakReset.xml 트리거에 설정 되어있음
        self.set_sound(trigger_id=19601, enable=True)
        self.side_npc_talk(npc_id=23000113, illust='Ishura_Dark_smile', script='$02020120_BF__BOSSSPAWN__1$', duration=7000, voice='ko/Npc/00002193')
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            # 위 던전 초기화 연출에 나오는 텍스트 문구 충분히 읽는 시간 확보를 위해 9초 정도 waitTick 설정하였음
            return 던전초기화시간등각종설정(self.ctx)


class 던전초기화시간등각종설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 스킬 브레이크 막기 실패로 던전 초기화 되면, 기존 흐르던 시간 정지 셋팅 종료 하고, 다시 시간 셋팅 해야 함,   이거 안하면 던전미션랭크에서 정밀한 시간 측정이 안될 수 있음
        self.dungeon_stop_timer()
        # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수 0 초기화 하기
        self.set_user_value(key='DungeonReset', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            # MS2TriggerBox   TriggerObjectID = 199, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        199은 스타팅 포인트 지점만 커버하는 비교적 좁은 범위
            return 보스등장(self.ctx) # 여기서 12분 시간 설정 다시 함


class 종료딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23000113, illust='Ishura_Dark_Idle', script='$02020120_BF__BOSSSPAWN__2$', duration=6576, voice='ko/Npc/00002194')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            # 맵 스킬 다 끄기, 이 맵은 낮으로 시작하기 때문에
            self.set_skill(trigger_ids=[2222])
            # 맵 스킬 다 끄기, 달빛의 저주 디버프 스킬 Off으로 초기 셋팅하기
            self.set_skill(trigger_ids=[1212])
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            # 던전 클리어 성공하면, 맵 트리거에 설정된 트리거 기능 정지 셋팅 종료 시킴, 이거 안하면 던전미션랭크에서 정밀한 시간 측정이 안될 수 있음
            self.dungeon_clear()
            self.dungeon_set_end_time()
            # arg1 = "특정트리거 박스 안에 있는 유저만 체크하고자 할때"   arg2 = "trigger"    즉 trigger 이거만 쓸수 있음  특정 트리거 박스 안의 유저만 체크 방식을 사용하고자 할때 이 2개 넣어야 함
            self.set_achievement(achieve='IshuraDungeonClear')
            # arg1 , arg2  넣지 않으면 맵 안에 있는 모든 유저에게 이 업적이 반영됨
            return 종료(self.ctx)


class 던전실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            # 맵 스킬 다 끄기, 이 맵은 낮으로 시작하기 때문에
            self.set_skill(trigger_ids=[2222])
            # 맵 스킬 다 끄기, 달빛의 저주 디버프 스킬 Off으로 초기 셋팅하기
            self.set_skill(trigger_ids=[1212])
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 순간이동 포탈 전부 꺼내기, 최종 보스방 가기 전에 전투가 끝날 수 있어서 종료 되었으면 모든 포탈 등장시킴
        self.set_portal(portal_id=2101, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2201, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2301, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3101, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3102, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3103, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3104, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3201, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3202, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3203, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3301, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3302, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3303, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3304, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3305, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3306, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4101, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4102, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4201, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4202, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4301, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=4302, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5101, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5102, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5201, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5202, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5203, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5204, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5205, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5206, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5301, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5302, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5303, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5304, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5401, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6101, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6201, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6301, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6302, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6303, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=6304, visible=True, enable=True, minimap_visible=True)
        self.dungeon_enable_give_up()


initial_state = 시작대기중
