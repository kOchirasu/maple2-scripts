""" trigger/02000410_bf/resurrectionprohibition.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면          750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_timer(timer_id='1', seconds=1)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_play_time() >= 420:
            # 던전 플레이 시간이 7분 지났는데, 인페르녹의 전함을 처지하지 못하여 인페르녹 등장 조건을 만족 못했으면 부할불가 처리하기, 이 부분은 맵으로 바로 들어가지 말고 던전로직을 통해서 정식으로 입장해야 작동함
            return 지금부터부활불가처리(self.ctx)
        """
        # 인페르녹과 전투 시작할 때 인페르녹  AI에서 BalrogMagicBursterBattlePhase =  1 신호를 보낼때까지 대기
        if self.user_value(key='BalrogMagicBursterBattlePhase') == 1:
            return 지금부터부활불가처리(self.ctx)
        """
        if self.user_value(key='ThirdPhase') == 1:
            # 2페이즈 전투 다 끝나고 , 파괴되어 너덜너덜해진 인페르녹 전함에게   ThirdPhase = 1 신호를 받을때까지 여기서 대기, 즉 AI_AirshipBalrogCrimsonBroken.xml 에서 보냄
            return 지금부터부활불가처리(self.ctx)


class 지금부터부활불가처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이때 부활불가 버프 부여하기
        # 여기서 맵 안에 있는 모든 플레이어에게 부활불가 디버프 부여함
        self.add_buff(box_ids=[750], skill_id=70000073, level=1, ignore_player=False)
        # arg1 = "트리거박스ID", arg2 = "애디셔널코드", arg3 = "애디셔널레벨", arg4 = "타겟이 플레이어로 하려면 0, 타겟이 몬스터로 하려면 1설정"
        # 부활불가 되었고 이제 파티가 전멸되면 게임오버 된다는 내여을 시스템메시지를 통해서 알려줌, 참고로 파티원전멸 체크 트리거는 ClearCheck.xml 이것임
        self.show_guide_summary(entity_id=20041001, text_id=20041001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20041001)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
