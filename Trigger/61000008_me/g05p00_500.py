""" trigger/61000008_me/g05p00_500.xml """
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P01Set') == 1:
            return NumberOnP01(self.ctx)
        if self.user_value(key='G05P02Set') == 1:
            return NumberOnP02(self.ctx)
        if self.user_value(key='G05P03Set') == 1:
            return NumberOnP03(self.ctx)
        if self.user_value(key='G05P04Set') == 1:
            return NumberOnP04(self.ctx)
        if self.user_value(key='G05P05Set') == 1:
            return NumberOnP05(self.ctx)
        if self.user_value(key='G05P06Set') == 1:
            return NumberOnP06(self.ctx)
        if self.user_value(key='G05P07Set') == 1:
            return NumberOnP07(self.ctx)
        if self.user_value(key='G05P08Set') == 1:
            return NumberOnP08(self.ctx)
        if self.user_value(key='G05P09Set') == 1:
            return NumberOnP09(self.ctx)
        if self.user_value(key='G05P10Set') == 1:
            return NumberOnP10(self.ctx)
        if self.user_value(key='G05P11Set') == 1:
            return NumberOnP11(self.ctx)
        if self.user_value(key='G05P12Set') == 1:
            return NumberOnP12(self.ctx)
        if self.user_value(key='G05P13Set') == 1:
            return NumberOnP13(self.ctx)
        if self.user_value(key='G05P14Set') == 1:
            return NumberOnP14(self.ctx)
        if self.user_value(key='G05P15Set') == 1:
            return NumberOnP15(self.ctx)
        if self.user_value(key='G05P16Set') == 1:
            return NumberOnP16(self.ctx)
        if self.user_value(key='G05P17Set') == 1:
            return NumberOnP17(self.ctx)
        if self.user_value(key='G05P18Set') == 1:
            return NumberOnP18(self.ctx)
        if self.user_value(key='G05P19Set') == 1:
            return NumberOnP19(self.ctx)
        if self.user_value(key='G05P20Set') == 1:
            return NumberOnP20(self.ctx)
        if self.user_value(key='G05P21Set') == 1:
            return NumberOnP21(self.ctx)
        if self.user_value(key='G05P22Set') == 1:
            return NumberOnP22(self.ctx)
        if self.user_value(key='G05P23Set') == 1:
            return NumberOnP23(self.ctx)
        if self.user_value(key='G05P24Set') == 1:
            return NumberOnP24(self.ctx)
        if self.user_value(key='G05P25Set') == 1:
            return NumberOnP25(self.ctx)
        if self.user_value(key='G05P26Set') == 1:
            return NumberOnP26(self.ctx)
        if self.user_value(key='G05P27Set') == 1:
            return NumberOnP27(self.ctx)
        if self.user_value(key='G05P28Set') == 1:
            return NumberOnP28(self.ctx)
        if self.user_value(key='G05P29Set') == 1:
            return NumberOnP29(self.ctx)
        if self.user_value(key='G05P30Set') == 1:
            return NumberOnP30(self.ctx)
        if self.user_value(key='G05P31Set') == 1:
            return NumberOnP31(self.ctx)
        if self.user_value(key='G05P32Set') == 1:
            return NumberOnP32(self.ctx)
        if self.user_value(key='G05P33Set') == 1:
            return NumberOnP33(self.ctx)
        if self.user_value(key='G05P34Set') == 1:
            return NumberOnP34(self.ctx)
        if self.user_value(key='G05P35Set') == 1:
            return NumberOnP35(self.ctx)
        if self.user_value(key='G05P36Set') == 1:
            return NumberOnP36(self.ctx)
        if self.user_value(key='G05P37Set') == 1:
            return NumberOnP37(self.ctx)
        if self.user_value(key='G05P38Set') == 1:
            return NumberOnP38(self.ctx)
        if self.user_value(key='G05P39Set') == 1:
            return NumberOnP39(self.ctx)
        if self.user_value(key='G05P40Set') == 1:
            return NumberOnP40(self.ctx)
        if self.user_value(key='G05P41Set') == 1:
            return NumberOnP41(self.ctx)
        if self.user_value(key='G05P42Set') == 1:
            return NumberOnP42(self.ctx)
        if self.user_value(key='G05P43Set') == 1:
            return NumberOnP43(self.ctx)
        if self.user_value(key='G05P44Set') == 1:
            return NumberOnP44(self.ctx)
        if self.user_value(key='G05P45Set') == 1:
            return NumberOnP45(self.ctx)
        if self.user_value(key='G05P46Set') == 1:
            return NumberOnP46(self.ctx)
        if self.user_value(key='G05P47Set') == 1:
            return NumberOnP47(self.ctx)
        if self.user_value(key='G05P48Set') == 1:
            return NumberOnP48(self.ctx)
        if self.user_value(key='G05P49Set') == 1:
            return NumberOnP49(self.ctx)
        if self.user_value(key='G05P50Set') == 1:
            return NumberOnP50(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=7110, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7120, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7130, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7140, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7210, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7220, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7230, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7240, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7310, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7320, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7330, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7340, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7410, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7420, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7430, key='ColorStart', value=1) # start
        self.set_user_value(trigger_id=7440, key='ColorStart', value=1) # start


# G05 P01
class NumberOnP01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[121], visible=True, fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[221], visible=True, fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[331], visible=True, fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=1)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=1)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=1)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P01TimeLimit') == 1:
            return CheckP01(self.ctx)


class CheckP01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=1)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=1)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=1)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP01(self.ctx)


class NumberOffP01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[121], fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[221], fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[331], fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP01(self.ctx)


class ResetP01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P01End', value=1)
        self.set_user_value(key='G05P01Set', value=0)
        self.set_user_value(key='G05P01TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P02
class NumberOnP02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[131], visible=True, fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[211], visible=True, fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[341], visible=True, fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=1)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=1)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=1)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P02TimeLimit') == 1:
            return CheckP02(self.ctx)


class CheckP02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=1)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=1)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=1)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP02(self.ctx)


class NumberOffP02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[131], fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[211], fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[341], fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP02(self.ctx)


class ResetP02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P02End', value=1)
        self.set_user_value(key='G05P02Set', value=0)
        self.set_user_value(key='G05P02TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P03
class NumberOnP03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[111], visible=True, fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[211], visible=True, fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[431], visible=True, fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=1)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=1)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=1)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P03TimeLimit') == 1:
            return CheckP03(self.ctx)


class CheckP03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=1)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=1)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=1)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP03(self.ctx)


class NumberOffP03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[111], fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[211], fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[431], fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP03(self.ctx)


class ResetP03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P03End', value=1)
        self.set_user_value(key='G05P03Set', value=0)
        self.set_user_value(key='G05P03TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P04
class NumberOnP04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[111], visible=True, fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[241], visible=True, fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[342], visible=True, fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[441], visible=True, fade=2.0) # 4,4 / 1
        self.set_user_value(trigger_id=8110, key='Barrier11', value=1)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=1)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=2)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P04TimeLimit') == 1:
            return CheckP04(self.ctx)


class CheckP04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=1)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=1)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=2)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP04(self.ctx)


class NumberOffP04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[111], fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[241], fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[342], fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[441], fade=2.0) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP04(self.ctx)


class ResetP04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P04End', value=1)
        self.set_user_value(key='G05P04Set', value=0)
        self.set_user_value(key='G05P04TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P05
class NumberOnP05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[311], visible=True, fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[341], visible=True, fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=1)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=1)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P05TimeLimit') == 1:
            return CheckP05(self.ctx)


class CheckP05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=1)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=1)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP05(self.ctx)


class NumberOffP05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[311], fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[341], fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP05(self.ctx)


class ResetP05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P05End', value=1)
        self.set_user_value(key='G05P05Set', value=0)
        self.set_user_value(key='G05P05TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P06
class NumberOnP06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[131], visible=True, fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[211], visible=True, fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[341], visible=True, fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[421], visible=True, fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=1)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=1)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=1)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=1)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P06TimeLimit') == 1:
            return CheckP06(self.ctx)


class CheckP06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=1)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=1)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=1)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=1)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP06(self.ctx)


class NumberOffP06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[131], fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[211], fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[341], fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[421], fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP06(self.ctx)


class ResetP06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P06End', value=1)
        self.set_user_value(key='G05P06Set', value=0)
        self.set_user_value(key='G05P06TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P07
class NumberOnP07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[120], visible=True, fade=2.0) # 1,2 / 0
        self.set_mesh(trigger_ids=[131], visible=True, fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[221], visible=True, fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[240], visible=True, fade=2.0) # 2,4 / 0
        self.set_mesh(trigger_ids=[311], visible=True, fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[341], visible=True, fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=0)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=1)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=1)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=0)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=1)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=1)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P07TimeLimit') == 1:
            return CheckP07(self.ctx)


class CheckP07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=0)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=1)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=1)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=0)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=1)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=1)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP07(self.ctx)


class NumberOffP07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[120], fade=2.0) # 1,2 / 0
        self.set_mesh(trigger_ids=[131], fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[221], fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[240], fade=2.0) # 2,4 / 0
        self.set_mesh(trigger_ids=[311], fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[341], fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP07(self.ctx)


class ResetP07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P07End', value=1)
        self.set_user_value(key='G05P07Set', value=0)
        self.set_user_value(key='G05P07TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P08
class NumberOnP08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[231], visible=True, fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[322], visible=True, fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=1)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=2)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P08TimeLimit') == 1:
            return CheckP08(self.ctx)


class CheckP08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=1)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=2)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP08(self.ctx)


class NumberOffP08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[231], fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[322], fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP08(self.ctx)


class ResetP08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P08End', value=1)
        self.set_user_value(key='G05P08Set', value=0)
        self.set_user_value(key='G05P08TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P09
class NumberOnP09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[141], visible=True, fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[241], visible=True, fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[311], visible=True, fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=1)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=1)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=1)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P09TimeLimit') == 1:
            return CheckP09(self.ctx)


class CheckP09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=1)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=1)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=1)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP09(self.ctx)


class NumberOffP09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[141], fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[241], fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[311], fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP09(self.ctx)


class ResetP09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P09End', value=1)
        self.set_user_value(key='G05P09Set', value=0)
        self.set_user_value(key='G05P09TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P10
class NumberOnP10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[111], visible=True, fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[230], visible=True, fade=2.0) # 2,3 / 0
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[321], visible=True, fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[441], visible=True, fade=2.0) # 4,4 / 1
        self.set_user_value(trigger_id=8110, key='Barrier11', value=1)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=0)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=1)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P10TimeLimit') == 1:
            return CheckP10(self.ctx)


class CheckP10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=1)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=0)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=1)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP10(self.ctx)


class NumberOffP10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[111], fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[230], fade=2.0) # 2,3 / 0
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[321], fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[441], fade=2.0) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP10(self.ctx)


class ResetP10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P10End', value=1)
        self.set_user_value(key='G05P10Set', value=0)
        self.set_user_value(key='G05P10TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P11
class NumberOnP11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[131], visible=True, fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[211], visible=True, fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[311], visible=True, fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[341], visible=True, fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[421], visible=True, fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=1)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=1)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=1)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=1)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=1)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P11TimeLimit') == 1:
            return CheckP11(self.ctx)


class CheckP11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=1)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=1)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=1)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=1)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=1)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP11(self.ctx)


class NumberOffP11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[131], fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[211], fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[311], fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[341], fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[421], fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP11(self.ctx)


class ResetP11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P11End', value=1)
        self.set_user_value(key='G05P11Set', value=0)
        self.set_user_value(key='G05P11TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P12
class NumberOnP12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[221], visible=True, fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[331], visible=True, fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=1)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=1)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P12TimeLimit') == 1:
            return CheckP12(self.ctx)


class CheckP12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=1)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=1)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP12(self.ctx)


class NumberOffP12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[221], fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[331], fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP12(self.ctx)


class ResetP12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P12End', value=1)
        self.set_user_value(key='G05P12Set', value=0)
        self.set_user_value(key='G05P12TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P13
class NumberOnP13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[121], visible=True, fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[231], visible=True, fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[332], visible=True, fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[421], visible=True, fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=1)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=1)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=2)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=1)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P13TimeLimit') == 1:
            return CheckP13(self.ctx)


class CheckP13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=1)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=1)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=2)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=1)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP13(self.ctx)


class NumberOffP13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[121], fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[231], fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[332], fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[421], fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP13(self.ctx)


class ResetP13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P13End', value=1)
        self.set_user_value(key='G05P13Set', value=0)
        self.set_user_value(key='G05P13TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P14
class NumberOnP14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[141], visible=True, fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[241], visible=True, fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[421], visible=True, fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[432], visible=True, fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=1)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=1)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=1)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=2)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P14TimeLimit') == 1:
            return CheckP14(self.ctx)


class CheckP14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=1)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=1)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=1)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=2)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP14(self.ctx)


class NumberOffP14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[141], fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[241], fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[421], fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[432], fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP14(self.ctx)


class ResetP14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P14End', value=1)
        self.set_user_value(key='G05P14Set', value=0)
        self.set_user_value(key='G05P14TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P15
class NumberOnP15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[111], visible=True, fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[331], visible=True, fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[421], visible=True, fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=1)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=1)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=1)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P15TimeLimit') == 1:
            return CheckP15(self.ctx)


class CheckP15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=1)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=1)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=1)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP15(self.ctx)


class NumberOffP15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[111], fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[331], fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[421], fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP15(self.ctx)


class ResetP15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P15End', value=1)
        self.set_user_value(key='G05P15Set', value=0)
        self.set_user_value(key='G05P15TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P16
class NumberOnP16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[131], visible=True, fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[231], visible=True, fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[321], visible=True, fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[432], visible=True, fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=1)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=1)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=1)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=2)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P16TimeLimit') == 1:
            return CheckP16(self.ctx)


class CheckP16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=1)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=1)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=1)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=2)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP16(self.ctx)


class NumberOffP16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[131], fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[231], fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[321], fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[432], fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP16(self.ctx)


class ResetP16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P16End', value=1)
        self.set_user_value(key='G05P16Set', value=0)
        self.set_user_value(key='G05P16TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P17
class NumberOnP17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[141], visible=True, fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[321], visible=True, fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[411], visible=True, fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=1)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=1)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=1)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P17TimeLimit') == 1:
            return CheckP17(self.ctx)


class CheckP17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=1)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=1)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=1)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP17(self.ctx)


class NumberOffP17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[141], fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[321], fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[411], fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP17(self.ctx)


class ResetP17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P17End', value=1)
        self.set_user_value(key='G05P17Set', value=0)
        self.set_user_value(key='G05P17TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P18
class NumberOnP18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[121], visible=True, fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[331], visible=True, fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=1)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=1)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P18TimeLimit') == 1:
            return CheckP18(self.ctx)


class CheckP18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=1)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=1)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP18(self.ctx)


class NumberOffP18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[121], fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[331], fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP18(self.ctx)


class ResetP18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P18End', value=1)
        self.set_user_value(key='G05P18Set', value=0)
        self.set_user_value(key='G05P18TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P19
class NumberOnP19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[111], visible=True, fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[431], visible=True, fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=1)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=1)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P19TimeLimit') == 1:
            return CheckP19(self.ctx)


class CheckP19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=1)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=1)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP19(self.ctx)


class NumberOffP19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[111], fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[431], fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP19(self.ctx)


class ResetP19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P19End', value=1)
        self.set_user_value(key='G05P19Set', value=0)
        self.set_user_value(key='G05P19TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P20
class NumberOnP20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[121], visible=True, fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[241], visible=True, fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=1)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=1)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P20TimeLimit') == 1:
            return CheckP20(self.ctx)


class CheckP20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=1)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=1)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP20(self.ctx)


class NumberOffP20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[121], fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[241], fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP20(self.ctx)


class ResetP20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P20End', value=1)
        self.set_user_value(key='G05P20Set', value=0)
        self.set_user_value(key='G05P20TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P21
class NumberOnP21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[141], visible=True, fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[411], visible=True, fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[432], visible=True, fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=1)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=1)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=2)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P21TimeLimit') == 1:
            return CheckP21(self.ctx)


class CheckP21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=1)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=1)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=2)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP21(self.ctx)


class NumberOffP21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[141], fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[411], fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[432], fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP21(self.ctx)


class ResetP21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P21End', value=1)
        self.set_user_value(key='G05P21Set', value=0)
        self.set_user_value(key='G05P21TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P22
class NumberOnP22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[131], visible=True, fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[311], visible=True, fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[332], visible=True, fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=1)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=1)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=2)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P22TimeLimit') == 1:
            return CheckP22(self.ctx)


class CheckP22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=1)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=1)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=2)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP22(self.ctx)


class NumberOffP22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[131], fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[311], fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[332], fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP22(self.ctx)


class ResetP22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P22End', value=1)
        self.set_user_value(key='G05P22Set', value=0)
        self.set_user_value(key='G05P22TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P23
class NumberOnP23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[221], visible=True, fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[431], visible=True, fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=1)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=1)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P23TimeLimit') == 1:
            return CheckP23(self.ctx)


class CheckP23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=1)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=1)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP23(self.ctx)


class NumberOffP23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[221], fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[431], fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP23(self.ctx)


class ResetP23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P23End', value=1)
        self.set_user_value(key='G05P23Set', value=0)
        self.set_user_value(key='G05P23TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P24
class NumberOnP24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[141], visible=True, fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[321], visible=True, fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=1)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=1)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P24TimeLimit') == 1:
            return CheckP24(self.ctx)


class CheckP24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=1)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=1)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP24(self.ctx)


class NumberOffP24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[141], fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[321], fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP24(self.ctx)


class ResetP24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P24End', value=1)
        self.set_user_value(key='G05P24Set', value=0)
        self.set_user_value(key='G05P24TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P25
class NumberOnP25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[111], visible=True, fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[141], visible=True, fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[231], visible=True, fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[321], visible=True, fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[421], visible=True, fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[441], visible=True, fade=2.0) # 4,4 / 1
        self.set_user_value(trigger_id=8110, key='Barrier11', value=1)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=1)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=1)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=1)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=1)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P25TimeLimit') == 1:
            return CheckP25(self.ctx)


class CheckP25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=1)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=1)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=1)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=1)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=1)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP25(self.ctx)


class NumberOffP25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[111], fade=2.0) # 1,1 / 1
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[141], fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[231], fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[321], fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[421], fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[441], fade=2.0) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP25(self.ctx)


class ResetP25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P25End', value=1)
        self.set_user_value(key='G05P25Set', value=0)
        self.set_user_value(key='G05P25TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P26
class NumberOnP26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[341], visible=True, fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[431], visible=True, fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=1)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=1)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P26TimeLimit') == 1:
            return CheckP26(self.ctx)


class CheckP26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=1)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=1)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP26(self.ctx)


class NumberOffP26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[341], fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[431], fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP26(self.ctx)


class ResetP26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P26End', value=1)
        self.set_user_value(key='G05P26Set', value=0)
        self.set_user_value(key='G05P26TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P27
class NumberOnP27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[121], visible=True, fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[331], visible=True, fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=1)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=1)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P27TimeLimit') == 1:
            return CheckP27(self.ctx)


class CheckP27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=1)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=1)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP27(self.ctx)


class NumberOffP27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[121], fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[331], fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP27(self.ctx)


class ResetP27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P27End', value=1)
        self.set_user_value(key='G05P27Set', value=0)
        self.set_user_value(key='G05P27TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P28
class NumberOnP28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[131], visible=True, fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[323], visible=True, fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[421], visible=True, fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=1)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=3)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=1)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P28TimeLimit') == 1:
            return CheckP28(self.ctx)


class CheckP28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=1)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=3)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=1)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP28(self.ctx)


class NumberOffP28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[131], fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[323], fade=2.0) # 3,2 / 3
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[421], fade=2.0) # 4,2 / 1
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP28(self.ctx)


class ResetP28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P28End', value=1)
        self.set_user_value(key='G05P28Set', value=0)
        self.set_user_value(key='G05P28TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P29
class NumberOnP29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[311], visible=True, fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=1)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P29TimeLimit') == 1:
            return CheckP29(self.ctx)


class CheckP29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=1)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP29(self.ctx)


class NumberOffP29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[311], fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP29(self.ctx)


class ResetP29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P29End', value=1)
        self.set_user_value(key='G05P29Set', value=0)
        self.set_user_value(key='G05P29TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P30
class NumberOnP30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[322], visible=True, fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[332], visible=True, fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[341], visible=True, fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=2)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=2)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=1)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P30TimeLimit') == 1:
            return CheckP30(self.ctx)


class CheckP30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=2)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=2)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=1)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP30(self.ctx)


class NumberOffP30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[322], fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[332], fade=2.0) # 3,3 / 2
        self.set_mesh(trigger_ids=[341], fade=2.0) # 3,4 / 1
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP30(self.ctx)


class ResetP30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P30End', value=1)
        self.set_user_value(key='G05P30Set', value=0)
        self.set_user_value(key='G05P30TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P31
class NumberOnP31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[221], visible=True, fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[342], visible=True, fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[431], visible=True, fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=1)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=2)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=1)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P31TimeLimit') == 1:
            return CheckP31(self.ctx)


class CheckP31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=1)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=2)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=1)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP31(self.ctx)


class NumberOffP31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[221], fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[342], fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[431], fade=2.0) # 4,3 / 1
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP31(self.ctx)


class ResetP31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P31End', value=1)
        self.set_user_value(key='G05P31Set', value=0)
        self.set_user_value(key='G05P31TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P32
class NumberOnP32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[221], visible=True, fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[321], visible=True, fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=1)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=1)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P32TimeLimit') == 1:
            return CheckP32(self.ctx)


class CheckP32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=1)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=1)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP32(self.ctx)


class NumberOffP32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[221], fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[321], fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP32(self.ctx)


class ResetP32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P32End', value=1)
        self.set_user_value(key='G05P32Set', value=0)
        self.set_user_value(key='G05P32TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P33
class NumberOnP33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[231], visible=True, fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[441], visible=True, fade=2.0) # 4,4 / 1
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=1)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P33TimeLimit') == 1:
            return CheckP33(self.ctx)


class CheckP33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=1)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP33(self.ctx)


class NumberOffP33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[231], fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[441], fade=2.0) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP33(self.ctx)


class ResetP33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P33End', value=1)
        self.set_user_value(key='G05P33Set', value=0)
        self.set_user_value(key='G05P33TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P34
class NumberOnP34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[241], visible=True, fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[331], visible=True, fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=1)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=1)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P34TimeLimit') == 1:
            return CheckP34(self.ctx)


class CheckP34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=1)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=1)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP34(self.ctx)


class NumberOffP34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[241], fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[331], fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP34(self.ctx)


class ResetP34(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P34End', value=1)
        self.set_user_value(key='G05P34Set', value=0)
        self.set_user_value(key='G05P34TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P35
class NumberOnP35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[231], visible=True, fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[321], visible=True, fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[342], visible=True, fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=1)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=1)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=2)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P35TimeLimit') == 1:
            return CheckP35(self.ctx)


class CheckP35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=1)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=1)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=2)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP35(self.ctx)


class NumberOffP35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[231], fade=2.0) # 2,3 / 1
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[321], fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[342], fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP35(self.ctx)


class ResetP35(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P35End', value=1)
        self.set_user_value(key='G05P35Set', value=0)
        self.set_user_value(key='G05P35TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P36
class NumberOnP36(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[131], visible=True, fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[321], visible=True, fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[441], visible=True, fade=2.0) # 4,4 / 1
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=1)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=1)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P36TimeLimit') == 1:
            return CheckP36(self.ctx)


class CheckP36(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=1)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=1)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP36(self.ctx)


class NumberOffP36(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[131], fade=2.0) # 1,3 / 1
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[321], fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[441], fade=2.0) # 4,4 / 1

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP36(self.ctx)


class ResetP36(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P36End', value=1)
        self.set_user_value(key='G05P36Set', value=0)
        self.set_user_value(key='G05P36TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P37
class NumberOnP37(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[211], visible=True, fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[241], visible=True, fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[411], visible=True, fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=1)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=1)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=1)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P37TimeLimit') == 1:
            return CheckP37(self.ctx)


class CheckP37(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=1)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=1)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=1)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP37(self.ctx)


class NumberOffP37(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[211], fade=2.0) # 2,1 / 1
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[241], fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[411], fade=2.0) # 4,1 / 1
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP37(self.ctx)


class ResetP37(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P37End', value=1)
        self.set_user_value(key='G05P37Set', value=0)
        self.set_user_value(key='G05P37TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P38
class NumberOnP38(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[241], visible=True, fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[321], visible=True, fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=1)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=1)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P38TimeLimit') == 1:
            return CheckP38(self.ctx)


class CheckP38(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=1)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=1)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP38(self.ctx)


class NumberOffP38(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[241], fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[321], fade=2.0) # 3,2 / 1
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP38(self.ctx)


class ResetP38(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P38End', value=1)
        self.set_user_value(key='G05P38Set', value=0)
        self.set_user_value(key='G05P38TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P39
class NumberOnP39(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[141], visible=True, fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[311], visible=True, fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=1)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=1)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P39TimeLimit') == 1:
            return CheckP39(self.ctx)


class CheckP39(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=1)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=1)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP39(self.ctx)


class NumberOffP39(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[141], fade=2.0) # 1,4 / 1
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[311], fade=2.0) # 3,1 / 1
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP39(self.ctx)


class ResetP39(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P39End', value=1)
        self.set_user_value(key='G05P39Set', value=0)
        self.set_user_value(key='G05P39TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P40
class NumberOnP40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[121], visible=True, fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[241], visible=True, fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[432], visible=True, fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=1)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=1)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=2)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P40TimeLimit') == 1:
            return CheckP40(self.ctx)


class CheckP40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=1)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=1)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=2)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP40(self.ctx)


class NumberOffP40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[121], fade=2.0) # 1,2 / 1
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[241], fade=2.0) # 2,4 / 1
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[432], fade=2.0) # 4,3 / 2
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP40(self.ctx)


class ResetP40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P40End', value=1)
        self.set_user_value(key='G05P40Set', value=0)
        self.set_user_value(key='G05P40TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P41
class NumberOnP41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[221], visible=True, fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[322], visible=True, fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[331], visible=True, fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=1)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=2)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=1)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P41TimeLimit') == 1:
            return CheckP41(self.ctx)


class CheckP41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=1)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=2)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=1)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP41(self.ctx)


class NumberOffP41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[221], fade=2.0) # 2,2 / 1
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[322], fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[331], fade=2.0) # 3,3 / 1
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP41(self.ctx)


class ResetP41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P41End', value=1)
        self.set_user_value(key='G05P41Set', value=0)
        self.set_user_value(key='G05P41TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P42
class NumberOnP42(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], visible=True, fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[232], visible=True, fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[322], visible=True, fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=3)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=2)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=2)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P42TimeLimit') == 1:
            return CheckP42(self.ctx)


class CheckP42(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=3)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=2)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=2)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP42(self.ctx)


class NumberOffP42(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[223], fade=2.0) # 2,2 / 3
        self.set_mesh(trigger_ids=[232], fade=2.0) # 2,3 / 2
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[322], fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP42(self.ctx)


class ResetP42(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P42End', value=1)
        self.set_user_value(key='G05P42Set', value=0)
        self.set_user_value(key='G05P42TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P43
class NumberOnP43(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], visible=True, fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=3)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P43TimeLimit') == 1:
            return CheckP43(self.ctx)


class CheckP43(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=3)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP43(self.ctx)


class NumberOffP43(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[143], fade=2.0) # 1,4 / 3
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP43(self.ctx)


class ResetP43(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P43End', value=1)
        self.set_user_value(key='G05P43Set', value=0)
        self.set_user_value(key='G05P43TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P44
class NumberOnP44(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[243], visible=True, fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[322], visible=True, fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], visible=True, fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=3)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=2)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=2)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P44TimeLimit') == 1:
            return CheckP44(self.ctx)


class CheckP44(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=3)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=2)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=2)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP44(self.ctx)


class NumberOffP44(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[243], fade=2.0) # 2,4 / 3
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[322], fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[412], fade=2.0) # 4,1 / 2
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP44(self.ctx)


class ResetP44(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P44End', value=1)
        self.set_user_value(key='G05P44Set', value=0)
        self.set_user_value(key='G05P44TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P45
class NumberOnP45(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], visible=True, fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[423], visible=True, fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=5)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=3)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P45TimeLimit') == 1:
            return CheckP45(self.ctx)


class CheckP45(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=5)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=3)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP45(self.ctx)


class NumberOffP45(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[415], fade=2.0) # 4,1 / 5
        self.set_mesh(trigger_ids=[423], fade=2.0) # 4,2 / 3
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP45(self.ctx)


class ResetP45(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P45End', value=1)
        self.set_user_value(key='G05P45Set', value=0)
        self.set_user_value(key='G05P45TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P46
class NumberOnP46(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[145], visible=True, fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[313], visible=True, fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[333], visible=True, fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[433], visible=True, fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=5)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=3)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=3)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=3)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P46TimeLimit') == 1:
            return CheckP46(self.ctx)


class CheckP46(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=5)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=3)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=3)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=3)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP46(self.ctx)


class NumberOffP46(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[145], fade=2.0) # 1,4 / 5
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[313], fade=2.0) # 3,1 / 3
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[333], fade=2.0) # 3,3 / 3
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[433], fade=2.0) # 4,3 / 3
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP46(self.ctx)


class ResetP46(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P46End', value=1)
        self.set_user_value(key='G05P46Set', value=0)
        self.set_user_value(key='G05P46TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P47
class NumberOnP47(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[115], visible=True, fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[122], visible=True, fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[135], visible=True, fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[212], visible=True, fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[222], visible=True, fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[342], visible=True, fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[445], visible=True, fade=2.0) # 4,4 / 5
        self.set_user_value(trigger_id=8110, key='Barrier11', value=5)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=2)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=5)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=2)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=2)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=2)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P47TimeLimit') == 1:
            return CheckP47(self.ctx)


class CheckP47(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=5)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=2)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=5)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=2)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=2)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=2)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=5)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP47(self.ctx)


class NumberOffP47(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[115], fade=2.0) # 1,1 / 5
        self.set_mesh(trigger_ids=[122], fade=2.0) # 1,2 / 2
        self.set_mesh(trigger_ids=[135], fade=2.0) # 1,3 / 5
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[212], fade=2.0) # 2,1 / 2
        self.set_mesh(trigger_ids=[222], fade=2.0) # 2,2 / 2
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[342], fade=2.0) # 3,4 / 2
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[445], fade=2.0) # 4,4 / 5

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP47(self.ctx)


class ResetP47(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P47End', value=1)
        self.set_user_value(key='G05P47Set', value=0)
        self.set_user_value(key='G05P47TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P48
class NumberOnP48(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[112], visible=True, fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], visible=True, fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[133], visible=True, fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[215], visible=True, fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[225], visible=True, fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], visible=True, fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[245], visible=True, fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], visible=True, fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[325], visible=True, fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], visible=True, fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[345], visible=True, fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], visible=True, fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], visible=True, fade=2.0) # 4,4 / 3
        self.set_user_value(trigger_id=8110, key='Barrier11', value=2)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=5)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=3)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=5)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=5)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=5)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=5)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=5)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=5)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=5)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=5)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=2)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P48TimeLimit') == 1:
            return CheckP48(self.ctx)


class CheckP48(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=2)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=5)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=3)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=5)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=5)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=5)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=5)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=5)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=5)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=5)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=5)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=2)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP48(self.ctx)


class NumberOffP48(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[112], fade=2.0) # 1,1 / 2
        self.set_mesh(trigger_ids=[125], fade=2.0) # 1,2 / 5
        self.set_mesh(trigger_ids=[133], fade=2.0) # 1,3 / 3
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[215], fade=2.0) # 2,1 / 5
        self.set_mesh(trigger_ids=[225], fade=2.0) # 2,2 / 5
        self.set_mesh(trigger_ids=[235], fade=2.0) # 2,3 / 5
        self.set_mesh(trigger_ids=[245], fade=2.0) # 2,4 / 5
        self.set_mesh(trigger_ids=[315], fade=2.0) # 3,1 / 5
        self.set_mesh(trigger_ids=[325], fade=2.0) # 3,2 / 5
        self.set_mesh(trigger_ids=[335], fade=2.0) # 3,3 / 5
        self.set_mesh(trigger_ids=[345], fade=2.0) # 3,4 / 5
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[422], fade=2.0) # 4,2 / 2
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[443], fade=2.0) # 4,4 / 3

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP48(self.ctx)


class ResetP48(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P48End', value=1)
        self.set_user_value(key='G05P48Set', value=0)
        self.set_user_value(key='G05P48TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P49
class NumberOnP49(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[113], visible=True, fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[124], visible=True, fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[134], visible=True, fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[142], visible=True, fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[214], visible=True, fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[233], visible=True, fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[244], visible=True, fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], visible=True, fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[322], visible=True, fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[344], visible=True, fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], visible=True, fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[424], visible=True, fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], visible=True, fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], visible=True, fade=2.0) # 4,4 / 2
        self.set_user_value(trigger_id=8110, key='Barrier11', value=3)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=4)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=4)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=2)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=4)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=3)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=4)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=4)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=2)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=4)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=3)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=4)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=4)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P49TimeLimit') == 1:
            return CheckP49(self.ctx)


class CheckP49(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=3)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=4)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=4)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=2)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=4)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=3)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=4)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=4)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=2)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=4)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=3)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=4)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=4)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP49(self.ctx)


class NumberOffP49(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[113], fade=2.0) # 1,1 / 3
        self.set_mesh(trigger_ids=[124], fade=2.0) # 1,2 / 4
        self.set_mesh(trigger_ids=[134], fade=2.0) # 1,3 / 4
        self.set_mesh(trigger_ids=[142], fade=2.0) # 1,4 / 2
        self.set_mesh(trigger_ids=[214], fade=2.0) # 2,1 / 4
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[233], fade=2.0) # 2,3 / 3
        self.set_mesh(trigger_ids=[244], fade=2.0) # 2,4 / 4
        self.set_mesh(trigger_ids=[314], fade=2.0) # 3,1 / 4
        self.set_mesh(trigger_ids=[322], fade=2.0) # 3,2 / 2
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[344], fade=2.0) # 3,4 / 4
        self.set_mesh(trigger_ids=[413], fade=2.0) # 4,1 / 3
        self.set_mesh(trigger_ids=[424], fade=2.0) # 4,2 / 4
        self.set_mesh(trigger_ids=[434], fade=2.0) # 4,3 / 4
        self.set_mesh(trigger_ids=[442], fade=2.0) # 4,4 / 2

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP49(self.ctx)


class ResetP49(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P49End', value=1)
        self.set_user_value(key='G05P49Set', value=0)
        self.set_user_value(key='G05P49TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


# G05 P50
class NumberOnP50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='DDStop_Stage_Number_01') # 사운드 / 맵 전체 / 숫자 나타날 때
        self.set_mesh(trigger_ids=[114], visible=True, fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[123], visible=True, fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[132], visible=True, fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[144], visible=True, fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[213], visible=True, fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[224], visible=True, fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[234], visible=True, fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[242], visible=True, fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], visible=True, fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[324], visible=True, fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[334], visible=True, fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[343], visible=True, fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], visible=True, fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[425], visible=True, fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], visible=True, fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[444], visible=True, fade=2.0) # 4,4 / 4
        self.set_user_value(trigger_id=8110, key='Barrier11', value=4)
        self.set_user_value(trigger_id=8120, key='Barrier12', value=3)
        self.set_user_value(trigger_id=8130, key='Barrier13', value=2)
        self.set_user_value(trigger_id=8140, key='Barrier14', value=4)
        self.set_user_value(trigger_id=8210, key='Barrier21', value=3)
        self.set_user_value(trigger_id=8220, key='Barrier22', value=4)
        self.set_user_value(trigger_id=8230, key='Barrier23', value=4)
        self.set_user_value(trigger_id=8240, key='Barrier24', value=2)
        self.set_user_value(trigger_id=8310, key='Barrier31', value=2)
        self.set_user_value(trigger_id=8320, key='Barrier32', value=4)
        self.set_user_value(trigger_id=8330, key='Barrier33', value=4)
        self.set_user_value(trigger_id=8340, key='Barrier34', value=3)
        self.set_user_value(trigger_id=8410, key='Barrier41', value=4)
        self.set_user_value(trigger_id=8420, key='Barrier42', value=5)
        self.set_user_value(trigger_id=8430, key='Barrier43', value=5)
        self.set_user_value(trigger_id=8440, key='Barrier44', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='G05P50TimeLimit') == 1:
            return CheckP50(self.ctx)


class CheckP50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=9110, key='Box11Check', value=4)
        self.set_user_value(trigger_id=9120, key='Box12Check', value=3)
        self.set_user_value(trigger_id=9130, key='Box13Check', value=2)
        self.set_user_value(trigger_id=9140, key='Box14Check', value=4)
        self.set_user_value(trigger_id=9210, key='Box21Check', value=3)
        self.set_user_value(trigger_id=9220, key='Box22Check', value=4)
        self.set_user_value(trigger_id=9230, key='Box23Check', value=4)
        self.set_user_value(trigger_id=9240, key='Box24Check', value=2)
        self.set_user_value(trigger_id=9310, key='Box31Check', value=2)
        self.set_user_value(trigger_id=9320, key='Box32Check', value=4)
        self.set_user_value(trigger_id=9330, key='Box33Check', value=4)
        self.set_user_value(trigger_id=9340, key='Box34Check', value=3)
        self.set_user_value(trigger_id=9410, key='Box41Check', value=4)
        self.set_user_value(trigger_id=9420, key='Box42Check', value=5)
        self.set_user_value(trigger_id=9430, key='Box43Check', value=5)
        self.set_user_value(trigger_id=9440, key='Box44Check', value=4)

    def on_tick(self) -> trigger_api.Trigger:
        return NumberOffP50(self.ctx)


class NumberOffP50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[114], fade=2.0) # 1,1 / 4
        self.set_mesh(trigger_ids=[123], fade=2.0) # 1,2 / 3
        self.set_mesh(trigger_ids=[132], fade=2.0) # 1,3 / 2
        self.set_mesh(trigger_ids=[144], fade=2.0) # 1,4 / 4
        self.set_mesh(trigger_ids=[213], fade=2.0) # 2,1 / 3
        self.set_mesh(trigger_ids=[224], fade=2.0) # 2,2 / 4
        self.set_mesh(trigger_ids=[234], fade=2.0) # 2,3 / 4
        self.set_mesh(trigger_ids=[242], fade=2.0) # 2,4 / 2
        self.set_mesh(trigger_ids=[312], fade=2.0) # 3,1 / 2
        self.set_mesh(trigger_ids=[324], fade=2.0) # 3,2 / 4
        self.set_mesh(trigger_ids=[334], fade=2.0) # 3,3 / 4
        self.set_mesh(trigger_ids=[343], fade=2.0) # 3,4 / 3
        self.set_mesh(trigger_ids=[414], fade=2.0) # 4,1 / 4
        self.set_mesh(trigger_ids=[425], fade=2.0) # 4,2 / 5
        self.set_mesh(trigger_ids=[435], fade=2.0) # 4,3 / 5
        self.set_mesh(trigger_ids=[444], fade=2.0) # 4,4 / 4

    def on_tick(self) -> trigger_api.Trigger:
        return ResetP50(self.ctx)


class ResetP50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1, key='G05P50End', value=1)
        self.set_user_value(key='G05P50Set', value=0)
        self.set_user_value(key='G05P50TimeLimit', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Wait(self.ctx)


initial_state = Wait
