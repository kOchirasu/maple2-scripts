""" trigger/02000471_bf/magic_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040315, key='10002020clear', value=0)
        self.set_user_value(trigger_id=2040317, key='10002020clear', value=0)
        self.set_user_value(trigger_id=2040322, key='10002020clear', value=0)
        self.set_mesh(trigger_ids=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799], interval=200, fade=35.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002020], state=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7002])
        self.set_mesh(trigger_ids=[1102], interval=200, fade=15.0)
        self.set_mesh(trigger_ids=[1202], visible=True, interval=200, fade=15.0)
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.add_buff(box_ids=[202], skill_id=70002011, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[202]):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040315, key='10002020clear', value=1)
        self.set_user_value(trigger_id=2040317, key='10002020clear', value=1)
        self.set_user_value(trigger_id=2040322, key='10002020clear', value=1)
        self.set_achievement(trigger_id=712, type='trigger', achieve='Hauntedmansion')
        self.spawn_monster(spawn_ids=[1121,1122], auto_target=False)
        self.set_mesh(trigger_ids=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799], visible=True, interval=200, fade=35.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Event_02_b(self.ctx)


class Event_02_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1122, script='$02000471_BF__MAGIC_02__0$', time=3)
        self.set_dialogue(type=1, spawn_id=1121, script='$02000471_BF__MAGIC_02__1$', time=3, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Event_02_c(self.ctx)


class Event_02_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799], interval=200, fade=35.0)
        self.destroy_monster(spawn_ids=[1121,1122])


initial_state = idle
