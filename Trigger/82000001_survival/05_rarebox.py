""" trigger/82000001_survival/05_rarebox.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # groupId="10000165-10000204" 황금 상자 Rare Box
        self.start_combine_spawn(group_id=[10000165,10000166,10000167,10000168,10000169,10000170,10000171,10000172,10000173,10000174,10000175,10000176,10000177,10000178,10000179,10000180,10000181,10000182,10000183,10000184,10000185,10000186,10000187,10000188,10000189,10000190,10000191,10000192,10000193,10000194,10000195,10000196,10000197,10000198,10000199,10000200,10000201,10000202,10000203,10000204])
        self.set_user_value(key='RareBoxOnCount', value=0)
        self.set_user_value(key='RareBoxOff', value=0)
        self.set_user_value(key='RareBoxStartTowerNumber', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxOnCount') == 1:
            return Delay(self.ctx)


class Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=178000):
            # test용 데이터 수정 가능 지점 / 3분 180000 / 그룹 스폰 순차적으로 하는데 걸리는 시간 2000 미리 차감 178000
            return BoxOnRandom(self.ctx)
        if self.user_value(key='RareBoxOff') == 1:
            return Quit(self.ctx)


class BoxOnRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return StartToTower01to10(self.ctx)
        if self.random_condition(weight=25.0):
            return StartToTower11to20(self.ctx)
        if self.random_condition(weight=25.0):
            return StartToTower21to30(self.ctx)
        if self.random_condition(weight=25.0):
            return StartToTower31to40(self.ctx)


class StartToTower01to10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RareBoxStartTowerNumber', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return Tower01to10(self.ctx)


class StartToTower11to20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RareBoxStartTowerNumber', value=11)

    def on_tick(self) -> trigger_api.Trigger:
        return Tower11to20(self.ctx)


class StartToTower21to30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RareBoxStartTowerNumber', value=21)

    def on_tick(self) -> trigger_api.Trigger:
        return Tower21to30(self.ctx)


class StartToTower31to40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RareBoxStartTowerNumber', value=31)

    def on_tick(self) -> trigger_api.Trigger:
        return Tower31to40(self.ctx)


class Tower01to10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 황금 상자 Rare Box Tower01to10
        self.start_combine_spawn(group_id=[10000165,10000166,10000167,10000168,10000169,10000170,10000171,10000172,10000173,10000174], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber') == 11:
            return BoxOn(self.ctx)
        if self.wait_tick(wait_tick=500):
            return Tower11to20(self.ctx)


class Tower11to20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 황금 상자 Rare Box Tower11to20
        self.start_combine_spawn(group_id=[10000175,10000176,10000177,10000178,10000179,10000180,10000181,10000182,10000183,10000184], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber') == 21:
            return BoxOn(self.ctx)
        if self.wait_tick(wait_tick=500):
            return Tower21to30(self.ctx)


class Tower21to30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 황금 상자 Rare Box Tower21to30
        self.start_combine_spawn(group_id=[10000185,10000186,10000187,10000188,10000189,10000190,10000191,10000192,10000193,10000194], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber') == 31:
            return BoxOn(self.ctx)
        if self.wait_tick(wait_tick=500):
            return Tower31to40(self.ctx)


class Tower31to40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 황금 상자 Rare Box Tower31to40
        self.start_combine_spawn(group_id=[10000195,10000196,10000197,10000198,10000199,10000200,10000201,10000202,10000203,10000204], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxStartTowerNumber') == 1:
            return BoxOn(self.ctx)
        if self.wait_tick(wait_tick=500):
            return Tower01to10(self.ctx)


class BoxOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23500110, illust='Mushking_normal', duration=5000, script='$82000000_survival__05_RAREBOX__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RareBoxOff') == 1:
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # groupId="10000165-10000204" 황금 상자 Rare Box
        self.start_combine_spawn(group_id=[10000165,10000166,10000167,10000168,10000169,10000170,10000171,10000172,10000173,10000174,10000175,10000176,10000177,10000178,10000179,10000180,10000181,10000182,10000183,10000184,10000185,10000186,10000187,10000188,10000189,10000190,10000191,10000192,10000193,10000194,10000195,10000196,10000197,10000198,10000199,10000200,10000201,10000202,10000203,10000204])


initial_state = Setting
