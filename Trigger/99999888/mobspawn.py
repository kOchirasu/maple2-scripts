""" trigger/99999888/mobspawn.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=911) >= 1:
            self.spawn_monster(spawn_ids=[101])
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_additional_effect(spawn_id=101, additional_effect_id=50000900, level=1):
            self.debug_string(value='버프가감지되었습니다. 20초 후 삭제합니다')
            return 버프삭제(self.ctx)


class 버프삭제(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            self.debug_string(value='버프가 삭제되었습니다.')
            self.npc_remove_additional_effect(spawn_id=101, additional_effect_id=50000900)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
