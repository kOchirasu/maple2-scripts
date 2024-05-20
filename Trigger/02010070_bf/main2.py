""" trigger/02010070_bf/main2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2100,2101,2102,2103,2104,2105,2106,2107,2108])
        self.set_interact_object(trigger_ids=[10000834], state=1)
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=4)
        self.set_effect(trigger_ids=[95001])
        self.destroy_monster(spawn_ids=[22210,22211,22212,22213])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999993]):
            return 대기시간안내01(self.ctx)


class 대기시간안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2100,2101,2102,2103,2104,2105,2106,2107,2108], auto_target=False)
        self.spawn_monster(spawn_ids=[22210,22211,22212,22213], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대기시간02(self.ctx)


class 대기시간02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02010070_BF__MAIN__4$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999983]):
            return 시작1(self.ctx)


class 시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20100706, text_id=20100706, duration=7000) # 바니걸을 따라 이동하세요.
        self.move_npc(spawn_id=2108, patrol_name='MS2PatrolData0')
        self.set_dialogue(type=1, spawn_id=2108, script='$02010070_BF__MAIN__1$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[88123]):
            return 시작112(self.ctx)


class 시작112(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2108, script='$02010070_BF__MAIN__2$', time=4)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20100707, text_id=20100707) # 테이블 위에 있는 금화를 획득하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000834], state=0):
            return 시작2(self.ctx)


class 시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[95001], visible=True)
        self.hide_guide_summary(entity_id=20100707)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 욕망이 불러낸 몬스터를 모두 처치해야 합니다.
        self.show_guide_summary(entity_id=20100708, text_id=20100708)
        self.destroy_monster(spawn_ids=[2100,2101,2102,2103,2104,2105,2106,2107,2108])
        self.spawn_monster(spawn_ids=[2000,2001,2002,2003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 시작32(self.ctx)


class 시작32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2004,2005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2000,2001,2002,2003,2004,2005]):
            return 시작3(self.ctx)


class 시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20100708)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20100709, text_id=20100709) # 로비에 등장한 몬스터를 모두 처치하세요!
        self.spawn_monster(spawn_ids=[2006,2007,2008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2006,2007,2008]):
            return 시간1(self.ctx)


class 시간1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20100709)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작5(self.ctx)


class 시작5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[70002], visible=True)
        self.set_effect(trigger_ids=[70003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_effect(trigger_ids=[70001], visible=True)
            self.set_skill(trigger_ids=[70004], enable=True)
            return 시작6(self.ctx)


class 시작6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=6)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.move_user(map_id=2010070, portal_id=9)
            return 시작7(self.ctx)


class 시작7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작8(self.ctx)


class 시작8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portal_id=4, visible=True, enable=True)


initial_state = 대기
