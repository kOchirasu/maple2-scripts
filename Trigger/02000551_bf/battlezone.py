""" trigger/02000551_bf/battlezone.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 트리거작동시작(self.ctx)


class 트리거작동시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=13, spawn_ids=[101]):
            # 중앙 전투판에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 중앙전투판신호(self.ctx)
        if self.npc_detected(box_id=12, spawn_ids=[101]):
            # 12시 전투판에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 시전투판신호12(self.ctx)
        if self.npc_detected(box_id=3, spawn_ids=[101]):
            # 3시 전투판에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 시전투판신호3(self.ctx)
        if self.npc_detected(box_id=6, spawn_ids=[101]):
            # 6시 전투판에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 시전투판신호6(self.ctx)
        if self.npc_detected(box_id=9, spawn_ids=[101]):
            # 9시 전투판에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 시전투판신호9(self.ctx)
        if self.npc_detected(box_id=122, spawn_ids=[101]):
            # 봄 컨셉 도로에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 봄컨셉도로신호(self.ctx)
        if self.npc_detected(box_id=45, spawn_ids=[101]):
            # 여름 컨셉 도로에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 여름컨셉도로신호(self.ctx)
        if self.npc_detected(box_id=78, spawn_ids=[101]):
            # 가을 컨셉 도로에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 가을컨셉도로신호(self.ctx)
        # arg2은 몬스터 스폰ID 102는 쉬운 난이도
        if self.npc_detected(box_id=1011, spawn_ids=[101]):
            # 겨울 컨셉 도로에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 겨울컨셉도로신호(self.ctx)
        if self.npc_detected(box_id=13, spawn_ids=[102]):
            # 중앙 전투판에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 중앙전투판신호(self.ctx)
        if self.npc_detected(box_id=12, spawn_ids=[102]):
            # 12시 전투판에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 시전투판신호12(self.ctx)
        if self.npc_detected(box_id=3, spawn_ids=[102]):
            # 3시 전투판에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 시전투판신호3(self.ctx)
        if self.npc_detected(box_id=6, spawn_ids=[102]):
            # 6시 전투판에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 시전투판신호6(self.ctx)
        if self.npc_detected(box_id=9, spawn_ids=[102]):
            # 9시 전투판에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 시전투판신호9(self.ctx)
        if self.npc_detected(box_id=122, spawn_ids=[102]):
            # 봄 컨셉 도로에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 봄컨셉도로신호(self.ctx)
        if self.npc_detected(box_id=45, spawn_ids=[102]):
            # 여름 컨셉 도로에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 여름컨셉도로신호(self.ctx)
        if self.npc_detected(box_id=78, spawn_ids=[102]):
            # 가을 컨셉 도로에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 가을컨셉도로신호(self.ctx)
        if self.npc_detected(box_id=1011, spawn_ids=[102]):
            # 겨울 컨셉 도로에 블랙빈이 들어셨으면, arg1 은 트리거박스 ID, arg2은 몬스터 스폰ID
            return 겨울컨셉도로신호(self.ctx)
        if self.wait_tick(wait_tick=2200):
            return 시간경과대기(self.ctx)


class 시간경과대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 트리거작동시작(self.ctx) # 1~2초 뒤에 다시 처음 단계로 돌아가기


class 중앙전투판신호(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스AI에게 이 변수 13 신호를 보내서 보스가 중앙 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄
        self.set_ai_extra_data(key='BattleZonePosition', value=13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 변수 신호 보내고 5~6초 뒤에 다시 처음 단계로 돌아가기
            return 트리거작동시작(self.ctx)


class 시전투판신호12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스AI에게 이 변수 12 신호를 보내서 보스가 12시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄
        self.set_ai_extra_data(key='BattleZonePosition', value=12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 변수 신호 보내고 5~6초 뒤에 다시 처음 단계로 돌아가기
            return 트리거작동시작(self.ctx)


class 시전투판신호3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스AI에게 이 변수 3 신호를 보내서 보스가 3시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄
        self.set_ai_extra_data(key='BattleZonePosition', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 변수 신호 보내고 5~6초 뒤에 다시 처음 단계로 돌아가기
            return 트리거작동시작(self.ctx)


class 시전투판신호6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스AI에게 이 변수 6 신호를 보내서 보스가 6시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄
        self.set_ai_extra_data(key='BattleZonePosition', value=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 변수 신호 보내고 5~6초 뒤에 다시 처음 단계로 돌아가기
            return 트리거작동시작(self.ctx)


class 시전투판신호9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스AI에게 이 변수 9 신호를 보내서 보스가 9시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄
        self.set_ai_extra_data(key='BattleZonePosition', value=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 변수 신호 보내고 5~6초 뒤에 다시 처음 단계로 돌아가기
            return 트리거작동시작(self.ctx)


class 봄컨셉도로신호(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스AI에게 이 변수 122 신호를 보내서 보스가 봄 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄
        self.set_ai_extra_data(key='BattleZonePosition', value=122)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 변수 신호 보내고 5~6초 뒤에 다시 처음 단계로 돌아가기
            return 트리거작동시작(self.ctx)


class 여름컨셉도로신호(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스AI에게 이 변수 45 신호를 보내서 보스가 여름 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄
        self.set_ai_extra_data(key='BattleZonePosition', value=45)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 변수 신호 보내고 5~6초 뒤에 다시 처음 단계로 돌아가기
            return 트리거작동시작(self.ctx)


class 가을컨셉도로신호(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스AI에게 이 변수 78 신호를 보내서 보스가 가을 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄
        self.set_ai_extra_data(key='BattleZonePosition', value=78)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 변수 신호 보내고 5~6초 뒤에 다시 처음 단계로 돌아가기
            return 트리거작동시작(self.ctx)


class 겨울컨셉도로신호(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보스AI에게 이 변수 1011 신호를 보내서 보스가 겨울 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄
        self.set_ai_extra_data(key='BattleZonePosition', value=1011)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 변수 신호 보내고 5~6초 뒤에 다시 처음 단계로 돌아가기
            return 트리거작동시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
