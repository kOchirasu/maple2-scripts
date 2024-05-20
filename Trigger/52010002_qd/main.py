""" trigger/52010002_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002789], quest_states=[1]): # 유치장에 같혀있는 NPC 들
            return Event_01(self.ctx)
        if not self.quest_user_detected(box_ids=[701], quest_ids=[10002789], quest_states=[1]):
            return Event_02(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=110, text_id=40010) # 적을 모두 처치하세요
        self.set_mesh(trigger_ids=[1001,1002])
        self.set_mesh(trigger_ids=[1003,1004], visible=True)
        self.spawn_monster(spawn_ids=[101,102,103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103]):
            return Event_03(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=110)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1001,1002], visible=True)
        self.set_mesh(trigger_ids=[1003,1004])
        self.spawn_monster(spawn_ids=[111,112,113], auto_target=False)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='Clearbadman') # Clearbadman
        self.set_mesh(trigger_ids=[1001,1002], visible=True)
        self.set_mesh(trigger_ids=[1003,1004])


class End(trigger_api.Trigger):
    pass


initial_state = idle
