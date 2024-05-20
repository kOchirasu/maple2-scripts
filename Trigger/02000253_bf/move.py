""" trigger/02000253_bf/move.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2901,2902,2903,2904,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916])
        self.set_effect(trigger_ids=[8041])
        self.set_effect(trigger_ids=[8042])
        self.set_effect(trigger_ids=[8043])
        self.set_effect(trigger_ids=[8044])
        self.set_interact_object(trigger_ids=[10001050], state=2)
        self.set_interact_object(trigger_ids=[10001051], state=2)
        self.set_interact_object(trigger_ids=[10001052], state=2)
        self.set_interact_object(trigger_ids=[10001053], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=906) >= 1:
            return 벨라소환(self.ctx)


class 벨라소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라이동(self.ctx)


class 벨라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=10)


class 랜덤선택1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return 번1(self.ctx)
        if self.random_condition(weight=33.0):
            return 번2(self.ctx)
        if self.random_condition(weight=34.0):
            return 번3(self.ctx)
        if self.random_condition(weight=34.0):
            return 번4(self.ctx)


class 랜덤선택1To1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return 번2(self.ctx)
        if self.random_condition(weight=34.0):
            return 번3(self.ctx)
        if self.random_condition(weight=34.0):
            return 번4(self.ctx)


class 랜덤선택1To2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return 번1(self.ctx)
        if self.random_condition(weight=34.0):
            return 번3(self.ctx)
        if self.random_condition(weight=34.0):
            return 번4(self.ctx)


class 랜덤선택1To3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return 번1(self.ctx)
        if self.random_condition(weight=34.0):
            return 번2(self.ctx)
        if self.random_condition(weight=34.0):
            return 번4(self.ctx)


class 랜덤선택1To4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=33.0):
            return 번1(self.ctx)
        if self.random_condition(weight=34.0):
            return 번2(self.ctx)
        if self.random_condition(weight=34.0):
            return 번3(self.ctx)


class 번1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=10)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002523, text_id=20002523)
        # self.set_mesh(trigger_ids=[265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296], interval=200)
        self.set_effect(trigger_ids=[8041], visible=True)
        self.set_breakable(trigger_ids=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904], enable=True)
        self.set_breakable(trigger_ids=[905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.hide_guide_summary(entity_id=20002523)
            return To1번1(self.ctx)


class To1번1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8041])
        self.set_timer(timer_id='1', seconds=30)
        self.spawn_monster(spawn_ids=[3001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.destroy_monster(spawn_ids=[3001])
            self.set_interact_object(trigger_ids=[10001050], state=2)
            self.set_interact_object(trigger_ids=[10001051], state=2)
            self.set_interact_object(trigger_ids=[10001052], state=2)
            self.set_interact_object(trigger_ids=[10001053], state=2)
            return 랜덤선택1To1(self.ctx)
        if self.monster_dead(spawn_ids=[3001]):
            return To2번1(self.ctx)


class To2번1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)
        self.set_interact_object(trigger_ids=[10001052], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.destroy_monster(spawn_ids=[3001])
            self.set_interact_object(trigger_ids=[10001050], state=2)
            self.set_interact_object(trigger_ids=[10001051], state=2)
            self.set_interact_object(trigger_ids=[10001052], state=2)
            self.set_interact_object(trigger_ids=[10001053], state=2)
            return 랜덤선택1To1(self.ctx)
        if self.object_interacted(interact_ids=[10001052], state=0):
            return 끝1(self.ctx)


class 번2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8042], visible=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002523, text_id=20002523)
        self.set_timer(timer_id='1', seconds=10)
        # self.set_mesh(trigger_ids=[297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328], interval=200)
        self.set_breakable(trigger_ids=[905,906,907,908,1905,1906,1907,1908,2905,2906,2907,2908,3905,3906,3907,3908], enable=True)
        self.set_breakable(trigger_ids=[901,902,903,904,909,910,911,912,913,914,915,916,1901,1902,1903,1904,1909,1910,1911,1912,1913,1914,1915,1916,2901,2902,2903,2904,2909,2910,2911,2912,2913,2914,2915,2916,3901,3902,3903,3904,3909,3910,3911,3912,3913,3914,3915,3916])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.hide_guide_summary(entity_id=20002523)
            return To1번2(self.ctx)


class To1번2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8042])
        self.set_timer(timer_id='1', seconds=30)
        self.spawn_monster(spawn_ids=[3002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.destroy_monster(spawn_ids=[3002])
            self.set_interact_object(trigger_ids=[10001050], state=2)
            self.set_interact_object(trigger_ids=[10001051], state=2)
            self.set_interact_object(trigger_ids=[10001052], state=2)
            self.set_interact_object(trigger_ids=[10001053], state=2)
            return 랜덤선택1To2(self.ctx)
        if self.monster_dead(spawn_ids=[3002]):
            return To2번2(self.ctx)


class To2번2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)
        self.set_interact_object(trigger_ids=[10001051], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.destroy_monster(spawn_ids=[3004])
            self.set_interact_object(trigger_ids=[10001050], state=2)
            self.set_interact_object(trigger_ids=[10001051], state=2)
            self.set_interact_object(trigger_ids=[10001052], state=2)
            self.set_interact_object(trigger_ids=[10001053], state=2)
            return 랜덤선택1To2(self.ctx)
        if self.object_interacted(interact_ids=[10001051], state=0):
            return 끝2(self.ctx)


class 번3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8044], visible=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002523, text_id=20002523)
        self.set_timer(timer_id='1', seconds=10)
        # self.set_mesh(trigger_ids=[233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264], interval=200)
        self.set_breakable(trigger_ids=[909,910,911,912,1909,1910,1911,1912,2909,2910,2911,2912,3909,3910,3911,3912], enable=True)
        self.set_breakable(trigger_ids=[901,902,903,904,905,906,907,908,913,914,915,916,1901,1902,1903,1904,1905,1906,1907,1908,1913,1914,1915,1916,2901,2902,2903,2904,2905,2906,2907,2908,2913,2914,2915,2916,3901,3902,3903,3904,3905,3906,3907,3908,3913,3914,3915,3916])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.hide_guide_summary(entity_id=20002523)
            return To1번3(self.ctx)


class To1번3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8044])
        self.set_timer(timer_id='1', seconds=30)
        self.spawn_monster(spawn_ids=[3003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.destroy_monster(spawn_ids=[3003])
            self.set_interact_object(trigger_ids=[10001050], state=2)
            self.set_interact_object(trigger_ids=[10001051], state=2)
            self.set_interact_object(trigger_ids=[10001052], state=2)
            self.set_interact_object(trigger_ids=[10001053], state=2)
            return 랜덤선택1To3(self.ctx)
        if self.monster_dead(spawn_ids=[3003]):
            return To2번3(self.ctx)


class To2번3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)
        self.set_interact_object(trigger_ids=[10001050], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.destroy_monster(spawn_ids=[3004])
            self.set_interact_object(trigger_ids=[10001050], state=2)
            self.set_interact_object(trigger_ids=[10001051], state=2)
            self.set_interact_object(trigger_ids=[10001052], state=2)
            self.set_interact_object(trigger_ids=[10001053], state=2)
            return 랜덤선택1To3(self.ctx)
        if self.object_interacted(interact_ids=[10001050], state=0):
            return 끝3(self.ctx)


class 번4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8043], visible=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002523, text_id=20002523)
        self.set_timer(timer_id='1', seconds=10)
        # self.set_mesh(trigger_ids=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232], interval=200)
        self.set_breakable(trigger_ids=[913,914,915,916,1913,1914,1915,1916,2913,2914,2915,2916,3913,3914,3915,3916], enable=True)
        self.set_breakable(trigger_ids=[901,902,903,904,905,906,907,908,909,910,911,912,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,2901,2902,2903,2904,2905,2906,2907,2908,2909,2910,2911,2912,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.hide_guide_summary(entity_id=20002523)
            return To1번4(self.ctx)


class To1번4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8043])
        self.set_timer(timer_id='1', seconds=30)
        self.spawn_monster(spawn_ids=[3004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.destroy_monster(spawn_ids=[3004])
            self.set_interact_object(trigger_ids=[10001050], state=2)
            self.set_interact_object(trigger_ids=[10001051], state=2)
            self.set_interact_object(trigger_ids=[10001052], state=2)
            self.set_interact_object(trigger_ids=[10001053], state=2)
            return 랜덤선택1To4(self.ctx)
        if self.monster_dead(spawn_ids=[3004]):
            return To2번4(self.ctx)


class To2번4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)
        self.set_interact_object(trigger_ids=[10001053], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            self.destroy_monster(spawn_ids=[3004])
            self.set_interact_object(trigger_ids=[10001050], state=2)
            self.set_interact_object(trigger_ids=[10001051], state=2)
            self.set_interact_object(trigger_ids=[10001052], state=2)
            self.set_interact_object(trigger_ids=[10001053], state=2)
            return 랜덤선택1To4(self.ctx)
        if self.object_interacted(interact_ids=[10001053], state=0):
            return 끝4(self.ctx)


class 끝1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)
        self.set_interact_object(trigger_ids=[10001050], state=2)
        self.set_interact_object(trigger_ids=[10001051], state=2)
        self.set_interact_object(trigger_ids=[10001052], state=2)
        self.set_interact_object(trigger_ids=[10001053], state=2)
        self.set_breakable(trigger_ids=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 랜덤선택1To1(self.ctx)


class 끝2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)
        self.set_interact_object(trigger_ids=[10001050], state=2)
        self.set_interact_object(trigger_ids=[10001051], state=2)
        self.set_interact_object(trigger_ids=[10001052], state=2)
        self.set_interact_object(trigger_ids=[10001053], state=2)
        self.set_breakable(trigger_ids=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 랜덤선택1To2(self.ctx)


class 끝3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)
        self.set_interact_object(trigger_ids=[10001050], state=2)
        self.set_interact_object(trigger_ids=[10001051], state=2)
        self.set_interact_object(trigger_ids=[10001052], state=2)
        self.set_interact_object(trigger_ids=[10001053], state=2)
        self.set_breakable(trigger_ids=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 랜덤선택1To3(self.ctx)


class 끝4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=30)
        self.set_interact_object(trigger_ids=[10001050], state=2)
        self.set_interact_object(trigger_ids=[10001051], state=2)
        self.set_interact_object(trigger_ids=[10001052], state=2)
        self.set_interact_object(trigger_ids=[10001053], state=2)
        self.set_breakable(trigger_ids=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 랜덤선택1To4(self.ctx)


initial_state = 대기
