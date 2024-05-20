""" trigger/02000325_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_interact_object(trigger_ids=[10000739], state=2)
        self.set_interact_object(trigger_ids=[10000740], state=2)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[611])
        self.set_effect(trigger_ids=[612])
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022])
        self.set_interact_object(trigger_ids=[10000752], state=0)
        self.set_interact_object(trigger_ids=[13000009], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022], visible=True, interval=200, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__0$', arg3='4000', arg4='0')
            return 어나운스02(self.ctx)


class 어나운스02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__1$', arg3='3500', arg4='0')
            return 어나운스03(self.ctx)


class 어나운스03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__2$', arg3='3500', arg4='0')
            return 라운드반응체크1(self.ctx)


class 라운드반응체크1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000752], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000752], state=0):
            self.set_effect(trigger_ids=[601], visible=True)
            return 라운드카운트딜레이1(self.ctx)


class 라운드카운트딜레이1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 라운드카운트1(self.ctx)


class 라운드카운트1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[611], visible=True)
        self.set_effect(trigger_ids=[612], visible=True)
        self.set_interact_object(trigger_ids=[10000739], state=1)
        self.set_interact_object(trigger_ids=[10000740], state=1)
        self.set_event_ui(type=0, arg2='1,3')
        self.show_count_ui(text='$02000325_BF__MAIN__3$', stage=1, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 라운드1(self.ctx)


class 라운드1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return 소환3001(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3002(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3003(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3004(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3005(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3006(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3007(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3008(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3009(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3010(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3011(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3012(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3013(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3014(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3015(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3016(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3017(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3018(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3019(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환3020(self.ctx)


class 소환3001(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.spawn_monster(spawn_ids=[3001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3001]):
            return 라운드대기2(self.ctx)


class 소환3002(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2002], auto_target=False)
        self.spawn_monster(spawn_ids=[3002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3002]):
            return 라운드대기2(self.ctx)


class 소환3003(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2003], auto_target=False)
        self.spawn_monster(spawn_ids=[3003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3003]):
            return 라운드대기2(self.ctx)


class 소환3004(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2004], auto_target=False)
        self.spawn_monster(spawn_ids=[3004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3004]):
            return 라운드대기2(self.ctx)


class 소환3005(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2005], auto_target=False)
        self.spawn_monster(spawn_ids=[3005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3005]):
            return 라운드대기2(self.ctx)


class 소환3006(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2006], auto_target=False)
        self.spawn_monster(spawn_ids=[3006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3006]):
            return 라운드대기2(self.ctx)


class 소환3007(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2007], auto_target=False)
        self.spawn_monster(spawn_ids=[3007], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3007]):
            return 라운드대기2(self.ctx)


class 소환3008(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2008], auto_target=False)
        self.spawn_monster(spawn_ids=[3008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3008]):
            return 라운드대기2(self.ctx)


class 소환3009(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2009], auto_target=False)
        self.spawn_monster(spawn_ids=[3009], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3009]):
            return 라운드대기2(self.ctx)


class 소환3010(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2010], auto_target=False)
        self.spawn_monster(spawn_ids=[3010], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3010]):
            return 라운드대기2(self.ctx)


class 소환3011(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2011], auto_target=False)
        self.spawn_monster(spawn_ids=[3011], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3011]):
            return 라운드대기2(self.ctx)


class 소환3012(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2012], auto_target=False)
        self.spawn_monster(spawn_ids=[3012], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3012]):
            return 라운드대기2(self.ctx)


class 소환3013(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2013], auto_target=False)
        self.spawn_monster(spawn_ids=[3013], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3013]):
            return 라운드대기2(self.ctx)


class 소환3014(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2014], auto_target=False)
        self.spawn_monster(spawn_ids=[3014], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3014]):
            return 라운드대기2(self.ctx)


class 소환3015(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2015], auto_target=False)
        self.spawn_monster(spawn_ids=[3015], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3015]):
            return 라운드대기2(self.ctx)


class 소환3016(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2016], auto_target=False)
        self.spawn_monster(spawn_ids=[3016], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3016]):
            return 라운드대기2(self.ctx)


class 소환3017(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2017], auto_target=False)
        self.spawn_monster(spawn_ids=[3017], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3017]):
            return 라운드대기2(self.ctx)


class 소환3018(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2018], auto_target=False)
        self.spawn_monster(spawn_ids=[3018], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3018]):
            return 라운드대기2(self.ctx)


class 소환3019(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2019], auto_target=False)
        self.spawn_monster(spawn_ids=[3019], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3019]):
            return 라운드대기2(self.ctx)


class 소환3020(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2020], auto_target=False)
        self.spawn_monster(spawn_ids=[3020], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3020]):
            return 라운드대기2(self.ctx)


class 라운드대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000739], state=2)
        self.set_interact_object(trigger_ids=[10000740], state=2)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[611])
        self.set_effect(trigger_ids=[612])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 어나운스04(self.ctx)


class 어나운스04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__4$', arg3='3500', arg4='0')
            return 라운드반응체크2(self.ctx)


class 라운드반응체크2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000752], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000752], state=0):
            self.set_effect(trigger_ids=[601], visible=True)
            return 어나운스04_2(self.ctx)


class 어나운스04_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__5$', arg3='3500', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 라운드카운트2(self.ctx)


class 라운드카운트2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[612], visible=True)
        self.set_interact_object(trigger_ids=[10000740], state=1)
        self.set_event_ui(type=0, arg2='2,3')
        self.show_count_ui(text='$02000325_BF__MAIN__6$', stage=2, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 라운드2(self.ctx)


class 라운드2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return 소환체크3001(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3002(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3003(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3004(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3005(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3006(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3007(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3008(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3009(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3010(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3011(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3012(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3013(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3014(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3015(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3016(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3017(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3018(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3019(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크3020(self.ctx)


class 소환체크3001(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2001]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2001]):
            return 소환2_3001(self.ctx)


class 소환체크3002(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2002]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2002]):
            return 소환2_3002(self.ctx)


class 소환체크3003(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2003]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2003]):
            return 소환2_3003(self.ctx)


class 소환체크3004(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2004]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2004]):
            return 소환2_3004(self.ctx)


class 소환체크3005(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2005]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2005]):
            return 소환2_3005(self.ctx)


class 소환체크3006(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2006]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2006]):
            return 소환2_3006(self.ctx)


class 소환체크3007(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2007]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2007]):
            return 소환2_3007(self.ctx)


class 소환체크3008(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2008]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2008]):
            return 소환2_3008(self.ctx)


class 소환체크3009(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2009]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2009]):
            return 소환2_3009(self.ctx)


class 소환체크3010(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2010]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2010]):
            return 소환2_3010(self.ctx)


class 소환체크3011(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2011]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2011]):
            return 소환2_3011(self.ctx)


class 소환체크3012(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2012]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2012]):
            return 소환2_3012(self.ctx)


class 소환체크3013(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2013]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2013]):
            return 소환2_3013(self.ctx)


class 소환체크3014(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2014]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2014]):
            return 소환2_3014(self.ctx)


class 소환체크3015(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2015]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2015]):
            return 소환2_3015(self.ctx)


class 소환체크3016(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2016]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2016]):
            return 소환2_3016(self.ctx)


class 소환체크3017(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2017]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2017]):
            return 소환2_3017(self.ctx)


class 소환체크3018(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2018]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2018]):
            return 소환2_3018(self.ctx)


class 소환체크3019(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2019]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2019]):
            return 소환2_3019(self.ctx)


class 소환체크3020(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2020]):
            return 라운드2(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2020]):
            return 소환2_3020(self.ctx)


class 소환2_3001(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.spawn_monster(spawn_ids=[3001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3001]):
            return 라운드대기3(self.ctx)


class 소환2_3002(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2002], auto_target=False)
        self.spawn_monster(spawn_ids=[3002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3002]):
            return 라운드대기3(self.ctx)


class 소환2_3003(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2003], auto_target=False)
        self.spawn_monster(spawn_ids=[3003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3003]):
            return 라운드대기3(self.ctx)


class 소환2_3004(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2004], auto_target=False)
        self.spawn_monster(spawn_ids=[3004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3004]):
            return 라운드대기3(self.ctx)


class 소환2_3005(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2005], auto_target=False)
        self.spawn_monster(spawn_ids=[3005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3005]):
            return 라운드대기3(self.ctx)


class 소환2_3006(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2006], auto_target=False)
        self.spawn_monster(spawn_ids=[3006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3006]):
            return 라운드대기3(self.ctx)


class 소환2_3007(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2007], auto_target=False)
        self.spawn_monster(spawn_ids=[3007], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3007]):
            return 라운드대기3(self.ctx)


class 소환2_3008(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2008], auto_target=False)
        self.spawn_monster(spawn_ids=[3008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3008]):
            return 라운드대기3(self.ctx)


class 소환2_3009(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2009], auto_target=False)
        self.spawn_monster(spawn_ids=[3009], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3009]):
            return 라운드대기3(self.ctx)


class 소환2_3010(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2010], auto_target=False)
        self.spawn_monster(spawn_ids=[3010], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3010]):
            return 라운드대기3(self.ctx)


class 소환2_3011(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2011], auto_target=False)
        self.spawn_monster(spawn_ids=[3011], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3011]):
            return 라운드대기3(self.ctx)


class 소환2_3012(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2012], auto_target=False)
        self.spawn_monster(spawn_ids=[3012], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3012]):
            return 라운드대기3(self.ctx)


class 소환2_3013(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2013], auto_target=False)
        self.spawn_monster(spawn_ids=[3013], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3013]):
            return 라운드대기3(self.ctx)


class 소환2_3014(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2014], auto_target=False)
        self.spawn_monster(spawn_ids=[3014], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3014]):
            return 라운드대기3(self.ctx)


class 소환2_3015(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2015], auto_target=False)
        self.spawn_monster(spawn_ids=[3015], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3015]):
            return 라운드대기3(self.ctx)


class 소환2_3016(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2016], auto_target=False)
        self.spawn_monster(spawn_ids=[3016], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3016]):
            return 라운드대기3(self.ctx)


class 소환2_3017(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2017], auto_target=False)
        self.spawn_monster(spawn_ids=[3017], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3017]):
            return 라운드대기3(self.ctx)


class 소환2_3018(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2018], auto_target=False)
        self.spawn_monster(spawn_ids=[3018], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3018]):
            return 라운드대기3(self.ctx)


class 소환2_3019(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2019], auto_target=False)
        self.spawn_monster(spawn_ids=[3019], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3019]):
            return 라운드대기3(self.ctx)


class 소환2_3020(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2020], auto_target=False)
        self.spawn_monster(spawn_ids=[3020], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3020]):
            return 라운드대기3(self.ctx)


class 라운드대기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[612])
        self.set_interact_object(trigger_ids=[10000740], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 어나운스05(self.ctx)


class 어나운스05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__7$', arg3='3500', arg4='0')
            return 라운드반응체크3(self.ctx)


class 라운드반응체크3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000752], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000752], state=0):
            self.set_effect(trigger_ids=[601], visible=True)
            return 라운드카운트3(self.ctx)


"""
class 어나운스05_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=4)
        self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__8$', arg3='3500', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 라운드카운트3(self.ctx)
"""

class 라운드카운트3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[612])
        # self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022], interval=200, fade=2.0)
        self.set_event_ui(type=0, arg2='3,3')
        self.show_count_ui(text='$02000325_BF__MAIN__9$', stage=3, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 라운드3(self.ctx)


class 라운드3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=5.0):
            return 소환체크2_3001(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3002(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3003(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3004(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3005(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3006(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3007(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3008(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3009(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3010(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3011(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3012(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3013(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3014(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3015(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3016(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3017(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3018(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3019(self.ctx)
        if self.random_condition(weight=5.0):
            return 소환체크2_3020(self.ctx)


class 소환체크2_3001(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2001]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2001]):
            return 소환3_3001(self.ctx)


class 소환체크2_3002(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2002]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2002]):
            return 소환3_3002(self.ctx)


class 소환체크2_3003(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2003]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2003]):
            return 소환3_3003(self.ctx)


class 소환체크2_3004(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2004]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2004]):
            return 소환3_3004(self.ctx)


class 소환체크2_3005(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2005]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2005]):
            return 소환3_3005(self.ctx)


class 소환체크2_3006(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2006]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2006]):
            return 소환3_3006(self.ctx)


class 소환체크2_3007(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2007]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2007]):
            return 소환3_3007(self.ctx)


class 소환체크2_3008(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2008]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2008]):
            return 소환3_3008(self.ctx)


class 소환체크2_3009(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2009]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2009]):
            return 소환3_3009(self.ctx)


class 소환체크2_3010(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2010]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2010]):
            return 소환3_3010(self.ctx)


class 소환체크2_3011(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2011]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2011]):
            return 소환3_3011(self.ctx)


class 소환체크2_3012(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2012]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2012]):
            return 소환3_3012(self.ctx)


class 소환체크2_3013(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2013]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2013]):
            return 소환3_3013(self.ctx)


class 소환체크2_3014(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2014]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2014]):
            return 소환3_3014(self.ctx)


class 소환체크2_3015(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2015]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2015]):
            return 소환3_3015(self.ctx)


class 소환체크2_3016(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2016]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2016]):
            return 소환3_3016(self.ctx)


class 소환체크2_3017(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2017]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2017]):
            return 소환3_3017(self.ctx)


class 소환체크2_3018(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2018]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2018]):
            return 소환3_3018(self.ctx)


class 소환체크2_3019(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2019]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2019]):
            return 소환3_3019(self.ctx)


class 소환체크2_3020(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=199, spawn_ids=[2020]):
            return 라운드3(self.ctx)
        if not self.npc_detected(box_id=199, spawn_ids=[2020]):
            return 소환3_3020(self.ctx)


class 소환3_3001(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.spawn_monster(spawn_ids=[3001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3001]):
            return 미션성공(self.ctx)


class 소환3_3002(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2002], auto_target=False)
        self.spawn_monster(spawn_ids=[3002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3002]):
            return 미션성공(self.ctx)


class 소환3_3003(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2003], auto_target=False)
        self.spawn_monster(spawn_ids=[3003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3003]):
            return 미션성공(self.ctx)


class 소환3_3004(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2004], auto_target=False)
        self.spawn_monster(spawn_ids=[3004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3004]):
            return 미션성공(self.ctx)


class 소환3_3005(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2005], auto_target=False)
        self.spawn_monster(spawn_ids=[3005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3005]):
            return 미션성공(self.ctx)


class 소환3_3006(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2006], auto_target=False)
        self.spawn_monster(spawn_ids=[3006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3006]):
            return 미션성공(self.ctx)


class 소환3_3007(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2007], auto_target=False)
        self.spawn_monster(spawn_ids=[3007], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3007]):
            return 미션성공(self.ctx)


class 소환3_3008(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2008], auto_target=False)
        self.spawn_monster(spawn_ids=[3008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3008]):
            return 미션성공(self.ctx)


class 소환3_3009(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2009], auto_target=False)
        self.spawn_monster(spawn_ids=[3009], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3009]):
            return 미션성공(self.ctx)


class 소환3_3010(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2010], auto_target=False)
        self.spawn_monster(spawn_ids=[3010], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3010]):
            return 미션성공(self.ctx)


class 소환3_3011(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2011], auto_target=False)
        self.spawn_monster(spawn_ids=[3011], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3011]):
            return 미션성공(self.ctx)


class 소환3_3012(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2012], auto_target=False)
        self.spawn_monster(spawn_ids=[3012], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3012]):
            return 미션성공(self.ctx)


class 소환3_3013(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2013], auto_target=False)
        self.spawn_monster(spawn_ids=[3013], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3013]):
            return 미션성공(self.ctx)


class 소환3_3014(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2014], auto_target=False)
        self.spawn_monster(spawn_ids=[3014], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3014]):
            return 미션성공(self.ctx)


class 소환3_3015(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2015], auto_target=False)
        self.spawn_monster(spawn_ids=[3015], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3015]):
            return 미션성공(self.ctx)


class 소환3_3016(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2016], auto_target=False)
        self.spawn_monster(spawn_ids=[3016], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3016]):
            return 미션성공(self.ctx)


class 소환3_3017(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2017], auto_target=False)
        self.spawn_monster(spawn_ids=[3017], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3017]):
            return 미션성공(self.ctx)


class 소환3_3018(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2018], auto_target=False)
        self.spawn_monster(spawn_ids=[3018], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3018]):
            return 미션성공(self.ctx)


class 소환3_3019(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2019], auto_target=False)
        self.spawn_monster(spawn_ids=[3019], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3019]):
            return 미션성공(self.ctx)


class 소환3_3020(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2020], auto_target=False)
        self.spawn_monster(spawn_ids=[3020], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[3020]):
            return 미션성공(self.ctx)


class 미션성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=102, type='trigger', achieve='BraveRace')
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022], visible=True, interval=200, fade=2.0)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[612])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 라운드보상3(self.ctx)


class 라운드보상3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # self.set_interact_object(trigger_ids=[13000009], state=1)
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
            self.set_event_ui(type=0, arg2='0,0')
            self.dungeon_clear()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
