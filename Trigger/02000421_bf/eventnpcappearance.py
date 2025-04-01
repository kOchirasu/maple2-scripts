""" trigger/02000421_bf/eventnpcappearance.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 보스등장대기(self.ctx)


class 보스등장대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 최초에는 우호적NPC 3인방이 스카이포트리스 함교 안에 있다는 설정에 맞추어, 유리로 둘러싸인 함교 안에 해당 NPC를 배치함
        self.spawn_monster(spawn_ids=[111])
        self.spawn_monster(spawn_ids=[121])
        self.spawn_monster(spawn_ids=[131])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EventNpcAppearance') == 1:
            # 필드보스가 등장하여 전투 상태가 되면 AI 에서 EventNpcAppearance = 1  신호를 트리거에게 보내서 이 신호를 트리거가 받으면 이부분 실행함
            return 우호적NPC등장(self.ctx)


class 우호적NPC등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스가 출몰해 전투가 시작되면, 함교 안에 있는 우호적 NPC 3인방 제거하고
        self.destroy_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[121])
        # 함교 안에 있었던  우호적 NPC 3인방이 전투판으로 나와 전투를 진행한다는 설정에 맞추어 전투판에 우호적 NPC 3인방을 등장시킴
        self.destroy_monster(spawn_ids=[131])
        self.spawn_monster(spawn_ids=[11])
        self.spawn_monster(spawn_ids=[21])
        # 참고로 이 우호적 NPC 3인방 제거는 보스 몬스터가 죽을 때 AI 에서 신호 보내서 제거하는 방식을 사용함
        self.spawn_monster(spawn_ids=[31])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EventNpcAppearance') == 2:
            # 필드보스가 죽거나 전투가 풀리면 AI 에서 EventNpcAppearance = 2  신호를 트리거에게 보내서 이 신호를 트리거가 받으면 이부분 실행함
            return 시작대기중(self.ctx) # 다시 처음으로 돌아감, 초기화


initial_state = 시작대기중
