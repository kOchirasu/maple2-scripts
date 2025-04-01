""" trigger/02020141_bf/interactmesh10014100.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 최초시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)
        self.set_interact_object(trigger_ids=[10003154], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 탈것_등장대기(self.ctx)


class 탈것_등장대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=3.0):
            return WaitTick후에결정01(self.ctx)
        if self.random_condition(weight=3.0):
            return WaitTick후에결정02(self.ctx)
        if self.random_condition(weight=3.0):
            return WaitTick후에결정03(self.ctx)


class WaitTick후에결정01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RidingBattle') == -1:
            # 보스가 죽으면 AI_TurkaHoodForce_Phase03.xml 에서 RidingBattle = -1 신호를 보냄
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=110000):
            return 탈것_확률결정(self.ctx)


class WaitTick후에결정02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RidingBattle') == -1:
            # 보스가 죽으면 AI_TurkaHoodForce_Phase03.xml 에서 RidingBattle = -1 신호를 보냄
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=135000):
            return 탈것_확률결정(self.ctx)


class WaitTick후에결정03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RidingBattle') == -1:
            # 보스가 죽으면 AI_TurkaHoodForce_Phase03.xml 에서 RidingBattle = -1 신호를 보냄
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=150000):
            return 탈것_확률결정(self.ctx)


class 탈것_확률결정(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=85.0):
            return 탈것등장_실패(self.ctx)
        if self.random_condition(weight=15.0):
            # 15% 확률로 거대 로봇탈것이 등장함
            return 탈것등장_성공(self.ctx)


class 탈것등장_성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 탑승 거대 아르케온 등장(연출용) : 리젠 애니메이션 출력
        self.spawn_monster(spawn_ids=[914100], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            # 아르케온 리젠 애니메이션 길이에 맞게 WaitTick 시간 설정해야 함
            return 탈것_등장(self.ctx)


class 탈것_등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020141_BF__INTERACTMESH_PHASE_3_INTERECT_01__0$', duration=5000) # 거대 로봇탈것 등장을 알리는 메시지 출력
        # arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)
        self.set_interact_object(trigger_ids=[10003154], state=1)
        # 탑승 거대 아르케온 등장(연출용) : 리젠 애니메이션 출력용 몬스터 리젠 애니만 나오고 바로 제거하기
        self.destroy_monster(spawn_ids=[914100])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003154], state=0):
            # arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 오브젝트 사라짐
            return 종료(self.ctx)
        if self.user_value(key='RidingBattle') == -1:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)
        self.set_interact_object(trigger_ids=[10003154], state=2)


class 탈것등장_실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 탑승 거대 아르케온 등장(연출용) : 리젠 애니메이션 출력, 그리고 가만히 내버려 두면 AI에서 스스로 자살하면서 사라짐(AI_ArcheonMaceRegenEvent_TypeB.xml)
        self.spawn_monster(spawn_ids=[914100], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return 탈것등장_실패_최종종료처리(self.ctx)


class 탈것등장_실패_최종종료처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 혹시 <action name="몬스터를생성한다" arg1="914100" arg2="0" /> 로 인해 생성한 몬스터가 주변에 적대적 몬스터가 없어서 스스로 자살 스킬 사용하지 않을 경우를 대비해, WaitTick = 13초 후에 스스로 사라지도록 설정함
        self.destroy_monster(spawn_ids=[914100])


initial_state = 최초시작
