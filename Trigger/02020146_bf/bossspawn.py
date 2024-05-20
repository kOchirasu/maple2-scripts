""" trigger/02020146_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1) # 맵 나가기 포탈, 시작 지점에
        self.set_portal(portal_id=2) # 맵 나가기 포탈, 전투판 지점에
        # 맵 나가기 포탈, 전투판으로 가기 위한 맵 내부 포탈
        self.set_portal(portal_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            # MS2TriggerBox   TriggerObjectID = 199, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면        199은 스타팅 포인트 지점만 커버하는 비교적 좁은 범위
            return 보스등장이벤트대기(self.ctx)


class 보스등장이벤트대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[99], auto_target=False) # 이슈라 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출대기(self.ctx)


class 연출대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23000113, illust='Ishura_Dark_Idle', script='$02020120_BF__BOSSSPAWN__0$', duration=4000, voice='ko/Npc/00002192')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투진행(self.ctx)


class 전투진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 맵 나가기 포탈, 전투판으로 가기 위한 맵 내부 포탈
        self.set_portal(portal_id=601, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[99]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg1 = "특정트리거 박스 안에 있는 유저만 체크하고자 할때"   arg2 = "trigger"    즉 trigger 이거만 쓸수 있음  특정 트리거 박스 안의 유저만 체크 방식을 사용하고자 할때 이 2개 넣어야 함
        self.set_achievement(achieve='IshuraDungeonClear_Quest')
        # arg1 , arg2  넣지 않으면 맵 안에 있는 모든 유저에게 이 업적이 반영됨

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 마무리연출(self.ctx)


class 마무리연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23000113, illust='Ishura_Dark_Idle', script='$02020120_BF__BOSSSPAWN__2$', duration=6576, voice='ko/Npc/00002194')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True) # 맵 나가기 포탈, 시작 지점에
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True) # 맵 나가기 포탈, 전투판 지점에
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
