""" trigger/84000007_wd/g07p00_700.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[110,111,112,113,114,115]) # 1,1 / Number 0 to 5
        self.set_mesh(trigger_ids=[120,121,122,123,124,125]) # 1,2 / Number 0 to 5
        self.set_mesh(trigger_ids=[130,131,132,133,134,135]) # 1,3 / Number 0 to 5
        self.set_mesh(trigger_ids=[140,141,142,143,144,145]) # 1,4 / Number 0 to 5
        self.set_mesh(trigger_ids=[210,211,212,213,214,215]) # 2,1 / Number 0 to 5
        self.set_mesh(trigger_ids=[220,221,222,223,224,225]) # 2,2 / Number 0 to 5
        self.set_mesh(trigger_ids=[230,231,232,233,234,235]) # 2,3 / Number 0 to 5
        self.set_mesh(trigger_ids=[240,241,242,243,244,245]) # 2,4 / Number 0 to 5
        self.set_mesh(trigger_ids=[310,311,312,313,314,315]) # 3,1 / Number 0 to 5
        self.set_mesh(trigger_ids=[320,321,322,323,324,325]) # 3,2 / Number 0 to 5
        self.set_mesh(trigger_ids=[330,331,332,333,334,335]) # 3,3 / Number 0 to 5
        self.set_mesh(trigger_ids=[340,341,342,343,344,345]) # 3,4 / Number 0 to 5
        self.set_mesh(trigger_ids=[410,411,412,413,414,415]) # 4,1 / Number 0 to 5
        self.set_mesh(trigger_ids=[420,421,422,423,424,425]) # 4,2 / Number 0 to 5
        self.set_mesh(trigger_ids=[430,431,432,433,434,435]) # 4,3 / Number 0 to 5
        self.set_mesh(trigger_ids=[440,441,442,443,444,445]) # 4,4 / Number 0 to 5
        self.set_mesh(trigger_ids=[2207,2208,2209,22000,22005,22010,22020,22030]) # 2,2 / Large Number
        self.set_mesh(trigger_ids=[2307,2308,2309,23000,23005,23010,23020,23030]) # 2,3 / Large Number
        self.set_mesh(trigger_ids=[3207,3208,3209,32000,32005,32010,32020,32030]) # 3,2 / Large Number
        self.set_mesh(trigger_ids=[3307,3308,3309,33000,33005,33010,33020,33030]) # 3,3 / Large Number

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P201Set') == 1:
            return NumberOnP201(self.ctx)
        if self.user_value(key='G07P202Set') == 1:
            return NumberOnP202(self.ctx)
        if self.user_value(key='G07P203Set') == 1:
            return NumberOnP203(self.ctx)
        if self.user_value(key='G07P204Set') == 1:
            return NumberOnP204(self.ctx)
        if self.user_value(key='G07P205Set') == 1:
            return NumberOnP205(self.ctx)
        if self.user_value(key='G07P206Set') == 1:
            return NumberOnP206(self.ctx)
        if self.user_value(key='G07P207Set') == 1:
            return NumberOnP207(self.ctx)
        if self.user_value(key='G07P208Set') == 1:
            return NumberOnP208(self.ctx)
        if self.user_value(key='G07P209Set') == 1:
            return NumberOnP209(self.ctx)
        if self.user_value(key='G07P210Set') == 1:
            return NumberOnP210(self.ctx)
        if self.user_value(key='G07P301Set') == 1:
            return NumberOnP301(self.ctx)
        if self.user_value(key='G07P302Set') == 1:
            return NumberOnP302(self.ctx)
        if self.user_value(key='G07P303Set') == 1:
            return NumberOnP303(self.ctx)
        if self.user_value(key='G07P304Set') == 1:
            return NumberOnP304(self.ctx)
        if self.user_value(key='G07P305Set') == 1:
            return NumberOnP305(self.ctx)
        if self.user_value(key='G07P306Set') == 1:
            return NumberOnP306(self.ctx)
        if self.user_value(key='G07P307Set') == 1:
            return NumberOnP307(self.ctx)
        if self.user_value(key='G07P308Set') == 1:
            return NumberOnP308(self.ctx)
        if self.user_value(key='G07P309Set') == 1:
            return NumberOnP309(self.ctx)
        if self.user_value(key='G07P310Set') == 1:
            return NumberOnP310(self.ctx)
        if self.user_value(key='G07P401Set') == 1:
            return NumberOnP401(self.ctx)
        if self.user_value(key='G07P402Set') == 1:
            return NumberOnP402(self.ctx)
        if self.user_value(key='G07P403Set') == 1:
            return NumberOnP403(self.ctx)
        if self.user_value(key='G07P404Set') == 1:
            return NumberOnP404(self.ctx)
        if self.user_value(key='G07P405Set') == 1:
            return NumberOnP405(self.ctx)
        if self.user_value(key='G07P406Set') == 1:
            return NumberOnP406(self.ctx)
        if self.user_value(key='G07P407Set') == 1:
            return NumberOnP407(self.ctx)


# G07 P201
class NumberOnP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[110], visible=True, fade=2.0) # 1,1 / 0
        self.set_mesh(trigger_ids=[120], visible=True, fade=2.0) # 1,2 / 0
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[22010], visible=True, fade=2.0) # 2,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[22005], visible=True, fade=2.0) # 2,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[322], visible=True, fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[430], visible=True, fade=2.0) # 4,3 / 0
        self.set_mesh(trigger_ids=[440], visible=True, fade=2.0) # 4,4 / 0
        self.set_user_value(trigger_id=8110, key='Barrier11', value=0)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=0)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=2)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=0)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P201TimeLimit') == 1:
            return CheckP201(self.ctx)


class CheckP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=0)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=0)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=2)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=0)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP201(self.ctx)


class NumberOffP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[110], fade=2.0) # 1,1 / 0
        self.set_mesh(trigger_ids=[120], fade=2.0) # 1,2 / 0
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[22010], fade=2.0) # 2,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[22005], fade=2.0) # 2,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[322], fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[430], fade=2.0) # 4,3 / 0
        self.set_mesh(trigger_ids=[440], fade=2.0) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP201(self.ctx)


class ResetP201(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P201End', value=1)
        self.set_user_value(key='G07P201Set', value=0)
        self.set_user_value(key='G07P201TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P202
class NumberOnP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[210], visible=True, fade=2.0) # 2,1 / 0
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[23010], visible=True, fade=2.0) # 2,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[23005], visible=True, fade=2.0) # 2,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[322], visible=True, fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[332], visible=True, fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[410], visible=True, fade=2.0) # 4,1 / 0
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[432], visible=True, fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=0)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=2)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=2)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=0)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=2)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P202TimeLimit') == 1:
            return CheckP202(self.ctx)


class CheckP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=0)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=2)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=2)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=0)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=2)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP202(self.ctx)


class NumberOffP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[210], fade=2.0) # 2,1 / 0
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[23010], fade=2.0) # 2,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[23005], fade=2.0) # 2,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[322], fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[332], fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[410], fade=2.0) # 4,1 / 0
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[432], fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP202(self.ctx)


class ResetP202(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P202End', value=1)
        self.set_user_value(key='G07P202Set', value=0)
        self.set_user_value(key='G07P202TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P203
class NumberOnP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[130], visible=True, fade=2.0) # 1,3 / 0
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[210], visible=True, fade=2.0) # 2,1 / 0
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[240], visible=True, fade=2.0) # 2,4 / 0
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[32010], visible=True, fade=2.0) # 3,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[32005], visible=True, fade=2.0) # 3,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[332], visible=True, fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[430], visible=True, fade=2.0) # 4,3 / 0
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=0)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=0)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=0)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=8330, key='Barrier33', value=2)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=0)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P203TimeLimit') == 1:
            return CheckP203(self.ctx)


class CheckP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=0)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=0)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=0)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=9330, key='Box33Check', value=2)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=0)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP203(self.ctx)


class NumberOffP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[130], fade=2.0) # 1,3 / 0
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[210], fade=2.0) # 2,1 / 0
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[240], fade=2.0) # 2,4 / 0
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[32010], fade=2.0) # 3,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[32005], fade=2.0) # 3,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[332], fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[430], fade=2.0) # 4,3 / 0
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP203(self.ctx)


class ResetP203(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P203End', value=1)
        self.set_user_value(key='G07P203Set', value=0)
        self.set_user_value(key='G07P203TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P204
class NumberOnP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[120], visible=True, fade=2.0) # 1,2 / 0
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[140], visible=True, fade=2.0) # 1,4 / 0
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[240], visible=True, fade=2.0) # 2,4 / 0
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[33010], visible=True, fade=2.0) # 3,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[33005], visible=True, fade=2.0) # 3,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[342], visible=True, fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[430], visible=True, fade=2.0) # 4,3 / 0
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=0)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=0)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=0)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=8340, key='Barrier34', value=2)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=0)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P204TimeLimit') == 1:
            return CheckP204(self.ctx)


class CheckP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=0)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=0)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=0)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=9340, key='Box34Check', value=2)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=0)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP204(self.ctx)


class NumberOffP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[120], fade=2.0) # 1,2 / 0
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[140], fade=2.0) # 1,4 / 0
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[240], fade=2.0) # 2,4 / 0
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[33010], fade=2.0) # 3,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[33005], fade=2.0) # 3,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[342], fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[430], fade=2.0) # 4,3 / 0
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP204(self.ctx)


class ResetP204(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P204End', value=1)
        self.set_user_value(key='G07P204Set', value=0)
        self.set_user_value(key='G07P204TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P205
class NumberOnP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[120], visible=True, fade=2.0) # 1,2 / 0
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[22020], visible=True, fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[22000], visible=True, fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[330], visible=True, fade=2.0) # 3,3 / 0
        self.set_mesh(trigger_ids=[342], visible=True, fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[420], visible=True, fade=2.0) # 4,2 / 0
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=0)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=0)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=2)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=0)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P205TimeLimit') == 1:
            return CheckP205(self.ctx)


class CheckP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=0)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=0)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=2)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=0)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP205(self.ctx)


class NumberOffP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[120], fade=2.0) # 1,2 / 0
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[22020], fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[22000], fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[330], fade=2.0) # 3,3 / 0
        self.set_mesh(trigger_ids=[342], fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[420], fade=2.0) # 4,2 / 0
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP205(self.ctx)


class ResetP205(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P205End', value=1)
        self.set_user_value(key='G07P205Set', value=0)
        self.set_user_value(key='G07P205TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P206
class NumberOnP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[111], visible=True, fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[141], visible=True, fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[23020], visible=True, fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[23000], visible=True, fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[310], visible=True, fade=2.0) # 3,1 / 0
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[340], visible=True, fade=2.0) # 3,4 / 0
        self.set_mesh(trigger_ids=[411], visible=True, fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=1)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=1)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=0)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=0)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=1)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P206TimeLimit') == 1:
            return CheckP206(self.ctx)


class CheckP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=1)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=1)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=0)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=0)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=1)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP206(self.ctx)


class NumberOffP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[111], fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[141], fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[23020], fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[23000], fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[310], fade=2.0) # 3,1 / 0
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[340], fade=2.0) # 3,4 / 0
        self.set_mesh(trigger_ids=[411], fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP206(self.ctx)


class ResetP206(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P206End', value=1)
        self.set_user_value(key='G07P206Set', value=0)
        self.set_user_value(key='G07P206TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P207
class NumberOnP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[110], visible=True, fade=2.0) # 1,1 / 0
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[131], visible=True, fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[210], visible=True, fade=2.0) # 2,1 / 0
        self.set_mesh(trigger_ids=[221], visible=True, fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[32020], visible=True, fade=2.0) # 3,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[32000], visible=True, fade=2.0) # 3,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[431], visible=True, fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[440], visible=True, fade=2.0) # 4,4 / 0
        self.set_user_value(trigger_id=8110, key='Barrier11', value=0)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=1)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=0)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=1)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=1)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P207TimeLimit') == 1:
            return CheckP207(self.ctx)


class CheckP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=0)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=1)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=0)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=1)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=1)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP207(self.ctx)


class NumberOffP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[110], fade=2.0) # 1,1 / 0
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[131], fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[210], fade=2.0) # 2,1 / 0
        self.set_mesh(trigger_ids=[221], fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[32020], fade=2.0) # 3,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[32000], fade=2.0) # 3,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[431], fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[440], fade=2.0) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP207(self.ctx)


class ResetP207(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P207End', value=1)
        self.set_user_value(key='G07P207Set', value=0)
        self.set_user_value(key='G07P207TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P208
class NumberOnP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[121], visible=True, fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[231], visible=True, fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[33020], visible=True, fade=2.0) # 3,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[33000], visible=True, fade=2.0) # 3,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[341], visible=True, fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[441], visible=True, fade=2.0) # 4,4 / 1
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=1)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=1)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8340, key='Barrier34', value=1)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P208TimeLimit') == 1:
            return CheckP208(self.ctx)


class CheckP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=1)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=1)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9340, key='Box34Check', value=1)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP208(self.ctx)


class NumberOffP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[121], fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[231], fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[33020], fade=2.0) # 3,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[33000], fade=2.0) # 3,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[341], fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[441], fade=2.0) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP208(self.ctx)


class ResetP208(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P208End', value=1)
        self.set_user_value(key='G07P208Set', value=0)
        self.set_user_value(key='G07P208TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P209
class NumberOnP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[22020], visible=True, fade=2.0) # 2,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[22005], visible=True, fade=2.0) # 2,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[342], visible=True, fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[432], visible=True, fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=2)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=2)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P209TimeLimit') == 1:
            return CheckP209(self.ctx)


class CheckP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=2)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=2)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP209(self.ctx)


class NumberOffP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[22020], fade=2.0) # 2,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[22005], fade=2.0) # 2,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[342], fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[432], fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP209(self.ctx)


class ResetP209(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P209End', value=1)
        self.set_user_value(key='G07P209Set', value=0)
        self.set_user_value(key='G07P209TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P210
class NumberOnP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[110], visible=True, fade=2.0) # 1,1 / 0
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[140], visible=True, fade=2.0) # 1,4 / 0
        self.set_mesh(trigger_ids=[210], visible=True, fade=2.0) # 2,1 / 0
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[320], visible=True, fade=2.0) # 3,2 / 0
        self.set_mesh(trigger_ids=[33020], visible=True, fade=2.0) # 3,3 /25 Jackpot
        self.set_mesh(trigger_ids=[33005], visible=True, fade=2.0) # 3,3 /25 Jackpot
        self.set_mesh(trigger_ids=[342], visible=True, fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[440], visible=True, fade=2.0) # 4,4 / 0
        self.set_user_value(trigger_id=8110, key='Barrier11', value=0)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=0)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=0)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=0)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=8340, key='Barrier34', value=2)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P210TimeLimit') == 1:
            return CheckP210(self.ctx)


class CheckP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=0)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=0)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=0)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=0)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=9340, key='Box34Check', value=2)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP210(self.ctx)


class NumberOffP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[110], fade=2.0) # 1,1 / 0
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[140], fade=2.0) # 1,4 / 0
        self.set_mesh(trigger_ids=[210], fade=2.0) # 2,1 / 0
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[320], fade=2.0) # 3,2 / 0
        self.set_mesh(trigger_ids=[33020], fade=2.0) # 3,3 /25 Jackpot
        self.set_mesh(trigger_ids=[33005], fade=2.0) # 3,3 /25 Jackpot
        self.set_mesh(trigger_ids=[342], fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[440], fade=2.0) # 4,4 / 0

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP210(self.ctx)


class ResetP210(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P210End', value=1)
        self.set_user_value(key='G07P210Set', value=0)
        self.set_user_value(key='G07P210TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P301
class NumberOnP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[33020], visible=True, fade=2.0) # 3,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[33005], visible=True, fade=2.0) # 3,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[432], visible=True, fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=2)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P301TimeLimit') == 1:
            return CheckP301(self.ctx)


class CheckP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=2)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP301(self.ctx)


class NumberOffP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[33020], fade=2.0) # 3,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[33005], fade=2.0) # 3,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[432], fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP301(self.ctx)


class ResetP301(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P301End', value=1)
        self.set_user_value(key='G07P301Set', value=0)
        self.set_user_value(key='G07P301TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P302
class NumberOnP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[23020], visible=True, fade=2.0) # 2,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[23005], visible=True, fade=2.0) # 2,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P302TimeLimit') == 1:
            return CheckP302(self.ctx)


class CheckP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP302(self.ctx)


class NumberOffP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[23020], fade=2.0) # 2,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[23005], fade=2.0) # 2,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP302(self.ctx)


class ResetP302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P302End', value=1)
        self.set_user_value(key='G07P302Set', value=0)
        self.set_user_value(key='G07P302TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P303
class NumberOnP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[32020], visible=True, fade=2.0) # 3,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[32005], visible=True, fade=2.0) # 3,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[332], visible=True, fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=8330, key='Barrier33', value=2)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P303TimeLimit') == 1:
            return CheckP303(self.ctx)


class CheckP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=9330, key='Box33Check', value=2)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP303(self.ctx)


class NumberOffP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[32020], fade=2.0) # 3,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[32005], fade=2.0) # 3,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[332], fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP303(self.ctx)


class ResetP303(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P303End', value=1)
        self.set_user_value(key='G07P303Set', value=0)
        self.set_user_value(key='G07P303TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P304
class NumberOnP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[22020], visible=True, fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[22000], visible=True, fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[322], visible=True, fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=2)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P304TimeLimit') == 1:
            return CheckP304(self.ctx)


class CheckP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=2)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP304(self.ctx)


class NumberOffP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[22020], fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[22000], fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[322], fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP304(self.ctx)


class ResetP304(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P304End', value=1)
        self.set_user_value(key='G07P304Set', value=0)
        self.set_user_value(key='G07P304TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P305
class NumberOnP305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[211], visible=True, fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[23020], visible=True, fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[23000], visible=True, fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[411], visible=True, fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[431], visible=True, fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=1)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=1)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=1)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P305TimeLimit') == 1:
            return CheckP305(self.ctx)


class CheckP305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=1)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=1)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=1)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP305(self.ctx)


class NumberOffP305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[211], fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[23020], fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[23000], fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[411], fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[431], fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP305(self.ctx)


class ResetP305(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P305End', value=1)
        self.set_user_value(key='G07P305Set', value=0)
        self.set_user_value(key='G07P305TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P306
class NumberOnP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[141], visible=True, fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[33020], visible=True, fade=2.0) # 3,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[33000], visible=True, fade=2.0) # 3,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[411], visible=True, fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[441], visible=True, fade=2.0) # 4,4 / 1
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=1)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=1)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P306TimeLimit') == 1:
            return CheckP306(self.ctx)


class CheckP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=1)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=1)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP306(self.ctx)


class NumberOffP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[141], fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[33020], fade=2.0) # 3,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[33000], fade=2.0) # 3,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[411], fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[441], fade=2.0) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP306(self.ctx)


class ResetP306(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P306End', value=1)
        self.set_user_value(key='G07P306Set', value=0)
        self.set_user_value(key='G07P306TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P307
class NumberOnP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[32030], visible=True, fade=2.0) # 3,2 / 30 Jackpot
        self.set_mesh(trigger_ids=[32000], visible=True, fade=2.0) # 3,2 / 30 Jackpot
        self.set_mesh(trigger_ids=[332], visible=True, fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=30) # 30 Jackpot
        self.set_user_value(trigger_id=8330, key='Barrier33', value=2)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P307TimeLimit') == 1:
            return CheckP307(self.ctx)


class CheckP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=30) # 30 Jackpot
        self.set_user_value(trigger_id=9330, key='Box33Check', value=2)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP307(self.ctx)


class NumberOffP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[32030], fade=2.0) # 3,2 / 30 Jackpot
        self.set_mesh(trigger_ids=[32000], fade=2.0) # 3,2 / 30 Jackpot
        self.set_mesh(trigger_ids=[332], fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP307(self.ctx)


class ResetP307(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P307End', value=1)
        self.set_user_value(key='G07P307Set', value=0)
        self.set_user_value(key='G07P307TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P308
class NumberOnP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[131], visible=True, fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[23030], visible=True, fade=2.0) # 2,3 / 30 Jackpot
        self.set_mesh(trigger_ids=[23000], visible=True, fade=2.0) # 2,3 / 30 Jackpot
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[311], visible=True, fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[332], visible=True, fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[342], visible=True, fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[431], visible=True, fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=1)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=30) # 30 Jackpot
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=1)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=2)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=2)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=1)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P308TimeLimit') == 1:
            return CheckP308(self.ctx)


class CheckP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=1)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=30) # 30 Jackpot
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=1)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=2)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=2)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=1)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP308(self.ctx)


class NumberOffP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[131], fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[23030], fade=2.0) # 2,3 / 30 Jackpot
        self.set_mesh(trigger_ids=[23000], fade=2.0) # 2,3 / 30 Jackpot
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[311], fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[332], fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[342], fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[431], fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP308(self.ctx)


class ResetP308(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P308End', value=1)
        self.set_user_value(key='G07P308Set', value=0)
        self.set_user_value(key='G07P308TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P309
class NumberOnP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[22010], visible=True, fade=2.0) # 2,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[22005], visible=True, fade=2.0) # 2,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[33020], visible=True, fade=2.0) # 3,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[33005], visible=True, fade=2.0) # 3,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P309TimeLimit') == 1:
            return CheckP309(self.ctx)


class CheckP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP309(self.ctx)


class NumberOffP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[22010], fade=2.0) # 2,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[22005], fade=2.0) # 2,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[33020], fade=2.0) # 3,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[33005], fade=2.0) # 3,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP309(self.ctx)


class ResetP309(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P309End', value=1)
        self.set_user_value(key='G07P309Set', value=0)
        self.set_user_value(key='G07P309TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P310
class NumberOnP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[23020], visible=True, fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[23000], visible=True, fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[32020], visible=True, fade=2.0) # 3,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[32000], visible=True, fade=2.0) # 3,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P310TimeLimit') == 1:
            return CheckP310(self.ctx)


class CheckP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP310(self.ctx)


class NumberOffP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[23020], fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[23000], fade=2.0) # 2,3 / 20 Jackpot
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[32020], fade=2.0) # 3,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[32000], fade=2.0) # 3,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP310(self.ctx)


class ResetP310(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P310End', value=1)
        self.set_user_value(key='G07P310Set', value=0)
        self.set_user_value(key='G07P310TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P401
class NumberOnP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=6) # 22 start jackpot
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[22030], visible=True, fade=2.0) # 2,2 / 30 Jackpot
        self.set_mesh(trigger_ids=[22000], visible=True, fade=2.0) # 2,2 / 30 Jackpot
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[432], visible=True, fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=30) # 30 Jackpot
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=2)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P401TimeLimit') == 1:
            return CheckP401(self.ctx)


class CheckP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=30) # 30 Jackpot
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=2)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP401(self.ctx)


class NumberOffP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[22030], fade=2.0) # 2,2 / 30 Jackpot
        self.set_mesh(trigger_ids=[22000], fade=2.0) # 2,2 / 30 Jackpot
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[432], fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP401(self.ctx)


class ResetP401(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P401End', value=1)
        self.set_user_value(key='G07P401Set', value=0)
        self.set_user_value(key='G07P401TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P402
class NumberOnP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[33030], visible=True, fade=2.0) # 3,3 / 30 Jackpot
        self.set_mesh(trigger_ids=[33000], visible=True, fade=2.0) # 3,3 / 30 Jackpot
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=30) # 30 Jackpot
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P402TimeLimit') == 1:
            return CheckP402(self.ctx)


class CheckP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=30) # 30 Jackpot
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP402(self.ctx)


class NumberOffP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[33030], fade=2.0) # 3,3 / 30 Jackpot
        self.set_mesh(trigger_ids=[33000], fade=2.0) # 3,3 / 30 Jackpot
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP402(self.ctx)


class ResetP402(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P402End', value=1)
        self.set_user_value(key='G07P402Set', value=0)
        self.set_user_value(key='G07P402TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P403
class NumberOnP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[23020], visible=True, fade=2.0) # 2,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[23005], visible=True, fade=2.0) # 2,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P403TimeLimit') == 1:
            return CheckP403(self.ctx)


class CheckP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP403(self.ctx)


class NumberOffP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[23020], fade=2.0) # 2,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[23005], fade=2.0) # 2,3 / 25 Jackpot
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP403(self.ctx)


class ResetP403(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P403End', value=1)
        self.set_user_value(key='G07P403Set', value=0)
        self.set_user_value(key='G07P403TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P404
class NumberOnP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[32020], visible=True, fade=2.0) # 3,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[32005], visible=True, fade=2.0) # 3,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P404TimeLimit') == 1:
            return CheckP404(self.ctx)


class CheckP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=25) # 25 Jackpot
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP404(self.ctx)


class NumberOffP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[32020], fade=2.0) # 3,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[32005], fade=2.0) # 3,2 / 25 Jackpot
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP404(self.ctx)


class ResetP404(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P404End', value=1)
        self.set_user_value(key='G07P404Set', value=0)
        self.set_user_value(key='G07P404TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P405
class NumberOnP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(trigger_id=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[32010], visible=True, fade=2.0) # 3,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[32005], visible=True, fade=2.0) # 3,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[33010], visible=True, fade=2.0) # 3,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[33005], visible=True, fade=2.0) # 3,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=8330, key='Barrier33', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P405TimeLimit') == 1:
            return CheckP405(self.ctx)


class CheckP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=9330, key='Box33Check', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP405(self.ctx)


class NumberOffP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[32010], fade=2.0) # 3,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[32005], fade=2.0) # 3,2 / 15 Jackpot
        self.set_mesh(trigger_ids=[33010], fade=2.0) # 3,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[33005], fade=2.0) # 3,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP405(self.ctx)


class ResetP405(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P405End', value=1)
        self.set_user_value(key='G07P405Set', value=0)
        self.set_user_value(key='G07P405TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P406
class NumberOnP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7230, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=6) # 32 start jackpot
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[23010], visible=True, fade=2.0) # 2,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[23005], visible=True, fade=2.0) # 2,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[32010], visible=True, fade=2.0) # 3,2 / 	15 Jackpot
        self.set_mesh(trigger_ids=[32005], visible=True, fade=2.0) # 3,2 / 	15 Jackpot
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P406TimeLimit') == 1:
            return CheckP406(self.ctx)


class CheckP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=15) # 15 Jackpot
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP406(self.ctx)


class NumberOffP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[23010], fade=2.0) # 2,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[23005], fade=2.0) # 2,3 / 15 Jackpot
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[32010], fade=2.0) # 3,2 / 	15 Jackpot
        self.set_mesh(trigger_ids=[32005], fade=2.0) # 3,2 / 	15 Jackpot
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP406(self.ctx)


class ResetP406(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P406End', value=1)
        self.set_user_value(key='G07P406Set', value=0)
        self.set_user_value(key='G07P406TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G07 P407
class NumberOnP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7220, key='ColorStart', value=6) # 23 start jackpot
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7330, key='ColorStart', value=6) # 33 start jackpot
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # yellow
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # yellow
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[22020], visible=True, fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[22000], visible=True, fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[33020], visible=True, fade=2.0) # 3,3 / 	20 Jackpot
        self.set_mesh(trigger_ids=[33000], visible=True, fade=2.0) # 3,3 / 	20 Jackpot
        self.set_mesh(trigger_ids=[342], visible=True, fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=8340, key='Barrier34', value=2)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G07P407TimeLimit') == 1:
            return CheckP407(self.ctx)


class CheckP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=20) # 20 Jackpot
        self.set_user_value(trigger_id=9340, key='Box34Check', value=2)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP407(self.ctx)


class NumberOffP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[22020], fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[22000], fade=2.0) # 2,2 / 20 Jackpot
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[33020], fade=2.0) # 3,3 / 	20 Jackpot
        self.set_mesh(trigger_ids=[33000], fade=2.0) # 3,3 / 	20 Jackpot
        self.set_mesh(trigger_ids=[342], fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP407(self.ctx)


class ResetP407(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G07P407End', value=1)
        self.set_user_value(key='G07P407Set', value=0)
        self.set_user_value(key='G07P407TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


initial_state = Wait
