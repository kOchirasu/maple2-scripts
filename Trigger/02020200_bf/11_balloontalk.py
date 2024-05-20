""" trigger/02020200_bf/11_balloontalk.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[905]):
            return 대사1(self.ctx)


class 대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020200_BF__11_BALLOONTALK__0$')
        self.add_balloon_talk(msg='$02020200_BF__11_BALLOONTALK__1$', duration=5000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[921]) and not self.monster_dead(spawn_ids=[205]):
            return 대사2(self.ctx)
        if self.user_detected(box_ids=[922]) and not self.monster_dead(spawn_ids=[205]):
            return 대사2(self.ctx)
        if self.user_detected(box_ids=[923]) and not self.monster_dead(spawn_ids=[205]):
            return 대사2(self.ctx)
        if self.monster_dead(spawn_ids=[205]):
            return 종료(self.ctx)


class 대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='$02020200_BF__11_BALLOONTALK__2$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=205, additional_effect_id=42030261, level=1):
            return 대사3(self.ctx)


class 대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020200_BF__11_BALLOONTALK__3$')
        self.add_balloon_talk(msg='$02020200_BF__11_BALLOONTALK__4$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
