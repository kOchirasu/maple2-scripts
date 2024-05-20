""" trigger/02000428_bf/airshipbalrogcrimsonflamekillplayer.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면, 750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_play_time() >= 540:
            # 아직도 인페르녹의 전함 전투 중인데 플레이 시간이 9분 되면
            # # 이 신호를 지속적으로 보내 파티원 강제로 죽이는 스킬 사용하도록 설정하기, NA 버전에서는 이 트리거 xml 사용 안함
            self.set_ai_extra_data(key='AirshipBalrogCrimsonFlameKillPlayer', value=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
