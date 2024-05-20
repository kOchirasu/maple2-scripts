""" trigger/52000072_qd/questnpcspawn01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002684], quest_states=[2]):
            return None # Missing State: NpcRemove01
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002684], quest_states=[1]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002683], quest_states=[3]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002683], quest_states=[2]):
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002683], quest_states=[1]): # 레논이 있던 자리
            return NpcChange01(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002682], quest_states=[3]):
            return NpcChange02(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002682], quest_states=[2]):
            return NpcChange02(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002682], quest_states=[1]):
            return NpcChange02(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002681], quest_states=[3]):
            return NpcChange02(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002681], quest_states=[2]):
            return NpcChange02(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[40002681], quest_states=[1]):
            # NPC 패트롤 연출
            return SetCamera01(self.ctx)


class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=False)


class NpcChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)


# NPC 패트롤 연출
class SetCamera01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=ActEnd01, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SetCamera02(self.ctx)


class SetCamera02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=600)
        self.spawn_monster(spawn_ids=[102,301,401], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return ActStart01(self.ctx)


class ActStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_301')
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_401')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ActStart02(self.ctx)


class ActStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ActStart03(self.ctx)


class ActStart03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ActEnd01(self.ctx)


class ActEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[301,401])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ActEnd02(self.ctx)


class ActEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return ActEnd03(self.ctx)


class ActEnd03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return QuestComplete(self.ctx)


class QuestComplete(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9900, type='trigger', achieve='triangularRelation')


initial_state = Wait
