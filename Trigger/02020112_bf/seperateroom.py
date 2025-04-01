""" trigger/02020112_bf/seperateroom.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727])
        self.set_mesh(trigger_ids=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827], visible=True)
        self.set_user_value(trigger_id=99990013, key='Extinction', value=0)
        self.set_user_value(trigger_id=99990014, key='Extinction', value=0)
        self.set_user_value(trigger_id=99990015, key='Extinction', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Start') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=191, is_relative=True) <= 70:
            return 격리조치_1_준비(self.ctx)


class 격리조치_1_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990013, key='Extinction', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Start') == 2:
            return 종료(self.ctx)
        if self.npc_hp(spawn_id=191, is_relative=True) <= 45:
            return 격리조치_2_준비(self.ctx)


class 격리조치_2_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990014, key='Extinction', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Start') == 2:
            return 종료(self.ctx)
        if self.npc_hp(spawn_id=191, is_relative=True) <= 20:
            return 격리조치_2_준비(self.ctx)


class 격리조치_3_준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990015, key='Extinction', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Start') == 2:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[181,182,183])
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='2')
        self.reset_timer(timer_id='3')
        self.set_mesh(trigger_ids=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727], fade=3.0)
        self.set_mesh(trigger_ids=[1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827], visible=True, fade=3.0)


initial_state = 대기
