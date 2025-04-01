""" trigger/02100009_bf/skill.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=100, key='Fencebreak', value=0)
        self.set_mesh(trigger_ids=[10001,10002,10003,10004,10005,10006,10007,10008], visible=True)
        self.set_skill(trigger_ids=[1000001], enable=True)
        self.set_skill(trigger_ids=[1000002], enable=True)
        self.set_skill(trigger_ids=[1000003], enable=True)
        self.set_skill(trigger_ids=[1000004], enable=True)
        self.set_skill(trigger_ids=[1000005], enable=True)
        self.set_skill(trigger_ids=[1000006], enable=True)
        self.set_skill(trigger_ids=[1000007], enable=True)
        self.set_skill(trigger_ids=[1000008], enable=True)
        self.set_skill(trigger_ids=[1000008], enable=True)
        self.set_skill(trigger_ids=[1000008], enable=True)
        self.set_skill(trigger_ids=[1000008], enable=True)
        self.set_skill(trigger_ids=[1000008], enable=True)
        self.set_skill(trigger_ids=[1000009], enable=True)
        self.set_skill(trigger_ids=[1000010], enable=True)
        self.set_skill(trigger_ids=[1000011], enable=True)
        self.set_skill(trigger_ids=[1000012], enable=True)
        self.set_skill(trigger_ids=[1000013], enable=True)
        self.set_skill(trigger_ids=[1000014], enable=True)
        self.set_skill(trigger_ids=[1000015], enable=True)
        self.set_skill(trigger_ids=[1000016], enable=True)
        self.set_skill(trigger_ids=[1000017], enable=True)
        self.set_skill(trigger_ids=[1000018], enable=True)
        self.set_skill(trigger_ids=[1000019], enable=True)
        self.set_skill(trigger_ids=[1000020], enable=True)
        self.set_skill(trigger_ids=[1000021], enable=True)
        self.set_skill(trigger_ids=[1000022], enable=True)
        self.set_skill(trigger_ids=[1000023], enable=True)
        self.set_skill(trigger_ids=[1000024], enable=True)
        self.set_skill(trigger_ids=[1000025], enable=True)
        self.set_skill(trigger_ids=[1000026], enable=True)
        self.set_skill(trigger_ids=[1000027], enable=True)
        self.set_skill(trigger_ids=[1000028], enable=True)
        self.set_skill(trigger_ids=[1000029], enable=True)
        self.set_skill(trigger_ids=[1000030], enable=True)
        self.set_skill(trigger_ids=[1000031], enable=True)
        self.set_skill(trigger_ids=[1000032], enable=True)
        self.set_skill(trigger_ids=[1000033], enable=True)
        self.set_skill(trigger_ids=[1000034], enable=True)
        self.set_skill(trigger_ids=[1000035], enable=True)
        self.set_skill(trigger_ids=[1000036], enable=True)
        self.set_skill(trigger_ids=[1000037], enable=True)
        self.set_skill(trigger_ids=[1000038], enable=True)
        self.set_skill(trigger_ids=[1000039], enable=True)
        self.set_skill(trigger_ids=[1000040], enable=True)
        self.set_skill(trigger_ids=[1000041], enable=True)
        self.set_skill(trigger_ids=[1000042], enable=True)
        self.set_skill(trigger_ids=[1000043], enable=True)
        self.set_skill(trigger_ids=[1000044], enable=True)
        self.set_skill(trigger_ids=[1000045], enable=True)
        self.set_skill(trigger_ids=[1000046], enable=True)
        self.set_skill(trigger_ids=[1000047], enable=True)
        self.set_skill(trigger_ids=[1000048], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 스킬사용(self.ctx)


class 스킬사용(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FenceBreak') == 1:
            return 길막삭제(self.ctx)


class 길막삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10001,10002,10003,10004,10005,10006,10007,10008])
        self.set_skill(trigger_ids=[1000001])
        self.set_skill(trigger_ids=[1000002])
        self.set_skill(trigger_ids=[1000003])
        self.set_skill(trigger_ids=[1000004])
        self.set_skill(trigger_ids=[1000005])
        self.set_skill(trigger_ids=[1000006])
        self.set_skill(trigger_ids=[1000007])
        self.set_skill(trigger_ids=[1000008])
        self.set_skill(trigger_ids=[1000008])
        self.set_skill(trigger_ids=[1000008])
        self.set_skill(trigger_ids=[1000008])
        self.set_skill(trigger_ids=[1000008])
        self.set_skill(trigger_ids=[1000009])
        self.set_skill(trigger_ids=[1000010])
        self.set_skill(trigger_ids=[1000011])
        self.set_skill(trigger_ids=[1000012])
        self.set_skill(trigger_ids=[1000013])
        self.set_skill(trigger_ids=[1000014])
        self.set_skill(trigger_ids=[1000015])
        self.set_skill(trigger_ids=[1000016])
        self.set_skill(trigger_ids=[1000017])
        self.set_skill(trigger_ids=[1000018])
        self.set_skill(trigger_ids=[1000019])
        self.set_skill(trigger_ids=[1000020])
        self.set_skill(trigger_ids=[1000021])
        self.set_skill(trigger_ids=[1000022])
        self.set_skill(trigger_ids=[1000023])
        self.set_skill(trigger_ids=[1000024])
        self.set_skill(trigger_ids=[1000025])
        self.set_skill(trigger_ids=[1000026])
        self.set_skill(trigger_ids=[1000027])
        self.set_skill(trigger_ids=[1000028])
        self.set_skill(trigger_ids=[1000029])
        self.set_skill(trigger_ids=[1000030])
        self.set_skill(trigger_ids=[1000031])
        self.set_skill(trigger_ids=[1000032])
        self.set_skill(trigger_ids=[1000033])
        self.set_skill(trigger_ids=[1000034])
        self.set_skill(trigger_ids=[1000035])
        self.set_skill(trigger_ids=[1000036])
        self.set_skill(trigger_ids=[1000037])
        self.set_skill(trigger_ids=[1000038])
        self.set_skill(trigger_ids=[1000039])
        self.set_skill(trigger_ids=[1000040])
        self.set_skill(trigger_ids=[1000041])
        self.set_skill(trigger_ids=[1000042])
        self.set_skill(trigger_ids=[1000043])
        self.set_skill(trigger_ids=[1000044])
        self.set_skill(trigger_ids=[1000045])
        self.set_skill(trigger_ids=[1000046])
        self.set_skill(trigger_ids=[1000047])
        self.set_skill(trigger_ids=[1000048])

    def on_tick(self) -> trigger_api.Trigger:
        return None # Missing State: 끝1


initial_state = 대기
