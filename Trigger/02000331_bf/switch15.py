""" trigger/02000331_bf/switch15.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000801], state=2) # 외다리 재생성레버 감춤
        self.set_effect(trigger_ids=[4200]) # 아랫방향 화살표
        self.set_user_value(key='SecondBridgeOff', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[99993]):
            return 전투체크(self.ctx)


class 전투체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SecondBridgeOff') == 1:
            return 스위치준비(self.ctx)


class 스위치준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[777703]) # 길 나타남02 사운드 / 외다리
        self.set_effect(trigger_ids=[777804]) # 길 없어짐02 사운드 /  외다리

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[99995]):
            return 스위치켜기(self.ctx)


class 스위치켜기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui_script(type=BannerType.Text, script='$02000331_BF__Seeker01__810$', duration=3000, box_ids=['0'])
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_interact_object(trigger_ids=[10000801], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(trigger_ids=[10000801], state=1) # 외다리 생성하는 레버01 나타남
        self.set_effect(trigger_ids=[4200], visible=True) # 아랫방향 화살표

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000801]):
            return 외다리재생성(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[7775], visible=True) # 레버 작동 사운드


class 외다리재생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[90008]) # 9th barrier OFF
        self.set_random_mesh(trigger_ids=[10040,10041,10042,10043,10044], visible=True, start_delay=5, interval=100, fade=100)
        self.set_effect(trigger_ids=[777703], visible=True) # 길 나타남02 사운드 / 외다리
        self.set_effect(trigger_ids=[4200]) # 아랫방향 화살표

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[99992]):
            return 이동안내(self.ctx)


class 이동안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui_script(type=BannerType.Text, script='$02000331_BF__Seeker01__811$', duration=3000, box_ids=['0'])
        self.set_effect(trigger_ids=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_mesh(trigger_ids=[90008]) # 9th barrier OFF
        self.set_random_mesh(trigger_ids=[10040,10041,10042,10043,10044], visible=True, start_delay=5, interval=150, fade=150) # 3rd bridge ON

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
