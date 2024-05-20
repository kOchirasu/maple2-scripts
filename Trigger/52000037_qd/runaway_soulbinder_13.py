""" trigger/52000037_qd/runaway_soulbinder_13.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9400], quest_ids=[50001411], quest_states=[2], job_code=110):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=603)
        self.move_user(map_id=52000037, portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return PC말풍선딜레이(self.ctx)


class PC말풍선딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.move_user_path(patrol_name='MS2PatrolData_PC1102A')
            return PC말풍선01(self.ctx)


class PC말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__RUNAWAY_SOULBINDER_13__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선02(self.ctx)


class PC말풍선02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__RUNAWAY_SOULBINDER_13__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return PC말풍선03(self.ctx)


class PC말풍선03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__RUNAWAY_SOULBINDER_13__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 말풍선딜레이(self.ctx)


class 말풍선딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            self.move_user_path(patrol_name='MS2PatrolData_PC1102B')
            return PC말풍선04(self.ctx)


class PC말풍선04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__RUNAWAY_SOULBINDER_13__3$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PC말풍선05(self.ctx)


class PC말풍선05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000037_QD__RUNAWAY_SOULBINDER_13__4$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NPC등장(self.ctx)


class NPC등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[211,212,213], auto_target=False)
        self.select_camera(trigger_id=604)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NPC대사01(self.ctx)


class NPC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001727, script='$52000037_QD__RUNAWAY_SOULBINDER_13__5$', time=2)
        self.set_skip(state=NPC대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NPC대사02(self.ctx)


class NPC대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return NPC대사02(self.ctx)


class NPC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001725, script='$52000037_QD__RUNAWAY_SOULBINDER_13__6$', time=2)
        self.set_skip(state=NPC대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC도주(self.ctx)


class NPC대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC도주(self.ctx)


class PC도주(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.select_camera(trigger_id=605)
        self.move_user_path(patrol_name='MS2PatrolData_PC1102C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PC말풍선06(self.ctx)


class PC말풍선06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=211, patrol_name='MS2PatrolData_NPC1102')
        self.move_npc(spawn_id=212, patrol_name='MS2PatrolData_NPC1102')
        self.move_npc(spawn_id=213, patrol_name='MS2PatrolData_NPC1102')
        self.set_dialogue(type=1, script='$52000037_QD__RUNAWAY_SOULBINDER_13__7$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000043, portal_id=5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Wait
