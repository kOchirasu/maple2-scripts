""" trigger/52000064_qd/90000650.xml """
import trigger_api


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True)
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.spawn_monster(spawn_ids=[1001,1002,1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1101,1102,1103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 아이템생성(self.ctx)


class 아이템생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 완료대기(self.ctx)


class 완료대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[102]):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[9011,9012,9013,9014,9015])
        self.set_event_ui(type=7, arg3='3000', arg4='0')
        self.set_achievement(trigger_id=199, type='trigger', achieve='ArrivedFlyBalloon')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000650], quest_states=[3]):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기
