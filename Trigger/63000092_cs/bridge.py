""" trigger/63000092_cs/bridge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') in [1]:
            self.set_mesh(trigger_ids=[4023,4024])
            self.set_mesh(trigger_ids=[4021,4022,4025,4026,4027], visible=True)
            self.set_mesh(trigger_ids=[4030], visible=True)
            return 일요일(self.ctx) # 일요일이면 다리5단
        if self.day_of_week(desc='1(일)-7(토)') in [2]:
            self.set_mesh(trigger_ids=[4024])
            self.set_mesh(trigger_ids=[4021,4022,4023,4025,4026,4027], visible=True)
            self.set_mesh(trigger_ids=[4030], visible=True)
            return 월요일(self.ctx) # 월요일이면 다리6단
        if self.day_of_week(desc='화요일') in [3]:
            self.set_mesh(trigger_ids=[4021,4022,4023,4024,4025,4026,4027], visible=True)
            self.set_mesh(trigger_ids=[4030], desc='바운딩 메쉬를 끈다')
            # 화요일이면 다리7단(다 놓임. 완성. 바운딩도 꺼짐)
            return 화요일(self.ctx)
        if self.day_of_week(desc='1(일)-7(토)') in [4]:
            self.set_mesh(trigger_ids=[4021,4022,4023,4024,4026,4027])
            self.set_mesh(trigger_ids=[4025], visible=True)
            self.set_mesh(trigger_ids=[4030], visible=True)
            return 수요일(self.ctx) # 수요일이면 다리1단
        if self.day_of_week(desc='1(일)-7(토)') in [5]:
            self.set_mesh(trigger_ids=[4021,4022,4023,4024,4027])
            self.set_mesh(trigger_ids=[4025,4026], visible=True)
            self.set_mesh(trigger_ids=[4030], visible=True)
            return 목요일(self.ctx) # 목요일이면 다리2단
        if self.day_of_week(desc='1(일)-7(토)') in [6]:
            self.set_mesh(trigger_ids=[4021,4022,4023,4024,4025,4026])
            self.set_mesh(trigger_ids=[4025,4026,4027], visible=True)
            self.set_mesh(trigger_ids=[4030], visible=True)
            return 금요일(self.ctx) # 금요일이면 다리3단
        if self.day_of_week(desc='1(일)-7(토)') in [7]:
            self.set_mesh(trigger_ids=[4022,4023,4024])
            self.set_mesh(trigger_ids=[4021,4025,4026,4027], visible=True)
            self.set_mesh(trigger_ids=[4030], visible=True)
            return 토요일(self.ctx) # 토요일이면 다리4단


class 일요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') not in [1]:
            return 대기(self.ctx) # 다음날이면 다시 체크


class 월요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') not in [2]:
            return 대기(self.ctx) # 다음날이면 다시 체크


class 화요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') not in [3]:
            return 대기(self.ctx) # 다음날이면 다시 체크


class 수요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') not in [4]:
            return 대기(self.ctx) # 다음날이면 다시 체크


class 목요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') not in [5]:
            return 대기(self.ctx) # 다음날이면 다시 체크


class 금요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') not in [6]:
            return 대기(self.ctx) # 다음날이면 다시 체크


class 토요일(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.day_of_week(desc='1(일)-7(토)') not in [7]:
            return 대기(self.ctx) # 다음날이면 다시 체크


initial_state = 대기
