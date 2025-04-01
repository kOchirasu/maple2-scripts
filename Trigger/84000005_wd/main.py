""" trigger/84000005_wd/main.xml """
import trigger_api


class 시작_타이머설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 5분 타이머. 기념촬영장은 맥시멈 5분만 돌아가도록 한다. 포털을 사용할 수 없기 때문에 시간에 제한을 둔다.
        self.set_timer(timer_id='4000', seconds=300, auto_remove=True)
        self.set_portal(portal_id=10001)

    def on_tick(self) -> trigger_api.Trigger:
        return 카메라세팅(self.ctx)


class 카메라세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_photo_studio(is_enable=True) # 자유각도변환 UI ON
        self.set_portal(portal_id=10001, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 강제퇴장대기(self.ctx)


class 강제퇴장대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='exitstudio') == 1:
            # 관리인에게 말 걸어 나가겠다고 할 때 npcscriptfunction에서 triggervalue 컬럼에 입력된 값을 쏨(setuservalue와 같은 역할). 이 값을 받은 경우 다음 state로 넘긴다.
            return 강제퇴장준비(self.ctx)
        if self.time_expired(timer_id='4000'):
            return 강퇴안내(self.ctx)


class 강퇴안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 메시지 : 잠시 후, 기념 촬영장이 폐쇄됩니다. 모두 퇴장해 주세요.
        self.show_guide_summary(entity_id=28400138)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            # 대기시간 5초
            return 강제퇴장준비(self.ctx)


class 강제퇴장준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 메시지 : 잠시 후, 기념 촬영장이 폐쇄됩니다. 모두 퇴장해 주세요.
        self.hide_guide_summary(entity_id=28400138)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 대기시간 5초
            return 강제퇴장(self.ctx)


class 강제퇴장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 방을 완전 폐쇄해버리는 명령어. 룸스테이지에서 제한시간이 다 되었을때의 처리와 같은 로직
        self.room_expire()


initial_state = 시작_타이머설정
