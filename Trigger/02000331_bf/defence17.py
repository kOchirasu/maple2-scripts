""" trigger/02000331_bf/defence17.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[99993]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9030, spawn_ids=[999]):
            return 전투중(self.ctx)


class 전투중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[999]):
            return 생존체크01(self.ctx)


class 생존체크01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=99997, spawn_ids=[601]):
            return 생존체크02(self.ctx)
        if self.monster_dead(spawn_ids=[601]):
            return 종료(self.ctx)


class 생존체크02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=99997, spawn_ids=[602]):
            return 생존체크03(self.ctx)
        if self.monster_dead(spawn_ids=[602]):
            return 종료(self.ctx)


class 생존체크03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=99997, spawn_ids=[603]):
            return 생존체크04(self.ctx)
        if self.monster_dead(spawn_ids=[603]):
            return 종료(self.ctx)


class 생존체크04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=99997, spawn_ids=[604]):
            return 생존체크05(self.ctx)
        if self.monster_dead(spawn_ids=[604]):
            return 종료(self.ctx)


class 생존체크05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=99997, spawn_ids=[605]):
            return 업적발생(self.ctx)
        if self.monster_dead(spawn_ids=[605]):
            return 종료(self.ctx)


class 업적발생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값 : 꼬마 5명 모두 살아 있으면 지급하는 트로피
        self.set_achievement(trigger_id=99996, type='trigger', achieve='defence_child') # defence_child


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
