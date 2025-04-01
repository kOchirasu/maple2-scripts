""" trigger/02020141_bf/interactmesh10014110.xml """
import trigger_api


class 최초시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)
        self.set_interact_object(trigger_ids=[10003153], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 탈것_등장대기(self.ctx)


class 탈것_등장대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 탈것_등장연출(self.ctx)


class 탈것_등장연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 탑승 아르케온 등장(연출용) : 리젠 애니메이션 출력
        self.spawn_monster(spawn_ids=[914110], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 아르케온 리젠 애니메이션 길이에 맞게 WaitTick 시간 설정해야 함
            return 탈것_등장(self.ctx)


class 탈것_등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)
        self.set_interact_object(trigger_ids=[10003153], state=1)
        self.destroy_monster(spawn_ids=[914110])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003153], state=0):
            # arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 오브젝트 사라짐
            return 인터렉트_동작중(self.ctx)
        if self.user_value(key='RidingBattle') == -1:
            # 보스가 죽으면 AI_TurkaHoodForce_Phase03.xml 에서 RidingBattle = -1 신호를 보냄
            return 종료(self.ctx)


class 인터렉트_동작중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)
        self.set_interact_object(trigger_ids=[10003153], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 탈것_등장대기(self.ctx)
        if self.user_value(key='RidingBattle') == -1:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)
        self.set_interact_object(trigger_ids=[10003153], state=2)


initial_state = 최초시작
