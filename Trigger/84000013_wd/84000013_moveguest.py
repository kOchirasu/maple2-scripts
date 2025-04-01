""" trigger/84000013_wd/84000013_moveguest.xml """
import trigger_api


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Weddingceremonystartsready', value=0) # 초기화
        self.set_user_value(key='Weddingceremonyfail', value=0) # 초기화

    def on_tick(self) -> trigger_api.Trigger:
        return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wedding_hall_state() == 'weddingComplete':
            # 결혼 연출 끝나서 보상받고 결혼상태로 변경되는 시점부터는 자리옮김 멈춤
            return 종료(self.ctx)
        if self.user_value(key='Weddingceremonystartsready') == 1:
            # 결혼하시겠습니까 입력창 띄우자마자 쏘는 신호 받으면 하객옮기기 트리거 시작되도록
            self.set_user_value(key='Weddingceremonystartsready', value=0) # 초기화
            return 새로운하객있는지감지(self.ctx)


class 새로운하객있는지감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wedding_hall_state() == 'weddingComplete':
            # 결혼 연출 끝나서 보상받고 결혼상태로 변경되는 시점부터는 자리옮김 멈춤
            return 종료(self.ctx)
        if self.user_value(key='Weddingceremonyfail') == 1:
            # 결혼 실패
            self.set_user_value(key='Weddingceremonyfail', value=0) # 초기화
            return 시작(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 방금입장한하객은하객석으로위치이동(self.ctx)


class 방금입장한하객은하객석으로위치이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 799번 박스(입장구역)에 있는 하객들은 22,23번으로 랜덤이동
        self.wedding_move_user(entry_type='Guest', map_id=84000013, portal_ids=[22,23], box_id=701)

    def on_tick(self) -> trigger_api.Trigger:
        return 새로운하객있는지감지(self.ctx)


class 하객은버진로드밖으로위치이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 701번 박스(버진로드)에 있는 하객들은 22,23번으로 랜덤이동
        self.wedding_move_user(entry_type='Guest', map_id=84000013, portal_ids=[22,23], box_id=701)

    def on_tick(self) -> trigger_api.Trigger:
        return 새로운하객있는지감지(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 초기화
