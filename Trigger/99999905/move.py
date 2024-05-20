""" trigger/99999905/move.xml """
import trigger_api


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_breakable(trigger_ids=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036])
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=102) >= 10:
            # self.set_breakable(trigger_ids=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036], enable=True)
            return 이동(self.ctx)


initial_state = 이동
