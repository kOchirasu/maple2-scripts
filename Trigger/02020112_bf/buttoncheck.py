""" trigger/02020112_bf/buttoncheck.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=9901, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9902, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9903, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9904, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_mesh(trigger_ids=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621], interval=20, fade=3.0)
        self.set_mesh(trigger_ids=[1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640], interval=20, fade=3.0)
        self.set_mesh(trigger_ids=[1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660], interval=20, fade=3.0)
        self.set_user_value(trigger_id=99990016, key='respawn', value=0)
        self.set_user_value(trigger_id=99990003, key='Timer', value=0)
        self.set_user_value(trigger_id=99990021, key='Reconnect', value=0)
        self.add_buff(box_ids=[916], skill_id=70002104, level=1, is_skill_set=False)
        self.set_effect(trigger_ids=[8001], visible=True)
        self.set_effect(trigger_ids=[8002,8003,8004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GravityRoom') == 1:
            return 작동(self.ctx)


class 작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[916], skill_id=70002104, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[911], job_code=0):
            return 감지_1층(self.ctx)


class 감지_1층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8001])
        self.set_effect(trigger_ids=[8002], visible=True)
        self.set_effect(trigger_ids=[8003], visible=True)
        self.set_effect(trigger_ids=[8004], visible=True)
        self.set_user_value(trigger_id=99990003, key='Timer', value=1)
        self.set_mesh(trigger_ids=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621], visible=True, interval=20, fade=3.0)
        self.set_mesh(trigger_ids=[1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640], visible=True, interval=20, fade=3.0)
        self.set_mesh(trigger_ids=[1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660], visible=True, interval=20, fade=3.0)
        self.set_actor(trigger_id=9901, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_On')
        self.set_actor(trigger_id=9902, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9903, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9904, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.add_buff(box_ids=[916], skill_id=70002103, level=1, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerReset') == 1:
            return 대기(self.ctx)
        if self.user_detected(box_ids=[912], job_code=0):
            return 감지_2층(self.ctx)


class 감지_2층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8002])
        self.set_user_value(trigger_id=99990016, key='respawn', value=1)
        self.add_buff(box_ids=[916], skill_id=70002103, level=1, is_skill_set=False)
        self.set_actor(trigger_id=9902, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerReset') == 1:
            return 대기(self.ctx)
        if self.user_detected(box_ids=[913], job_code=0):
            return 감지_3층(self.ctx)


class 감지_3층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8003])
        self.add_buff(box_ids=[916], skill_id=70002103, level=1, is_skill_set=False)
        self.set_actor(trigger_id=9903, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerReset') == 1:
            return 대기(self.ctx)
        if self.user_detected(box_ids=[914], job_code=0):
            return 감지_4층(self.ctx)


class 감지_4층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8004])
        self.set_actor(trigger_id=9904, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_On')
        self.add_buff(box_ids=[916], skill_id=70002105, level=1, is_skill_set=False)
        self.set_gravity(gravity=-32.0)
        self.set_event_ui_script(type=BannerType.Text, script='$02020112_BF__BUTTONCHECK__0$', duration=5000)
        self.set_user_value(trigger_id=99990016, key='respawn', value=2) # <1층 스폰 중지>
        self.set_user_value(trigger_id=99990003, key='Timer', value=2)
        self.set_user_value(trigger_id=99990001, key='GravityRoom', value=2)
        # <재접속 유저를 위해 버프 지속적으로 쏴주기>
        self.set_user_value(trigger_id=99990021, key='Reconnect', value=1)
        self.set_actor(trigger_id=9901, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9902, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9903, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9904, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_mesh(trigger_ids=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621], interval=20, fade=3.0)
        self.set_mesh(trigger_ids=[1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640], interval=20, fade=3.0)
        self.set_mesh(trigger_ids=[1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660], interval=20, fade=3.0)


initial_state = 대기
