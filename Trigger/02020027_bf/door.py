""" trigger/02020027_bf/door.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[9001,9002,9003,9004,9005,9006,9007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=201, is_relative=True) < 50:
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.side_npc_talk(npc_id=24120006, illust='Mason_normal', duration=4000, script='장소를 옮겨볼까요?')
        self.set_mesh(trigger_ids=[9001,9002,9003,9004,9005,9006,9007], fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1002]):
            return 문닫힘(self.ctx)


class 문닫힘(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[9001,9002,9003,9004,9005,9006], visible=True, fade=10.0)
        # <두번째 방 튀어나갈 사람에 대한 예외처리로 페이드없이 바로 생기는 투명 메쉬>
        self.set_mesh(trigger_ids=[9007], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
