""" trigger/52100031_qd/faction_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=199, skill_id=99910140)
        self.set_interact_object(trigger_ids=[10002060], state=2)
        self.set_interact_object(trigger_ids=[10002061], state=2)
        self.set_interact_object(trigger_ids=[10002062], state=2)
        self.set_interact_object(trigger_ids=[10002063], state=2)
        self.set_interact_object(trigger_ids=[10002068], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='faction02') >= 1:
            return 말준비(self.ctx)


class 말준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=퀘스트)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(box_ids=[199], skill_id=70000107, level=1, ignore_player=False, is_skill_set=False)
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1101,1102,1103,1104,1104], auto_target=False)
        self.set_dialogue(type=1, spawn_id=1101, script='$52100031_QD__FACTION_02__0$', time=5)
        self.set_interact_object(trigger_ids=[10002068], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 퀘스트(self.ctx)


"""
class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 던전(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트(self.ctx)
"""

"""
class 던전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=종료체크)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_interact_object(trigger_ids=[10002060], state=1)
        self.set_interact_object(trigger_ids=[10002061], state=1)
        self.set_interact_object(trigger_ids=[10002062], state=1)
        self.set_interact_object(trigger_ids=[10002063], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 종료체크(self.ctx)
"""

class 퀘스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20040102, text_id=20040102, duration=3000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.remove_buff(box_id=199, skill_id=70000107)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차안내2(self.ctx)


class 차안내2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20040105, text_id=20040105, duration=3500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.remove_buff(box_id=199, skill_id=70000107)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonClear') >= 1:
            self.destroy_monster(spawn_ids=[1101,1102,1103,1104,1104], arg2=False)
            self.set_interact_object(trigger_ids=[10002060], state=0)
            self.set_interact_object(trigger_ids=[10002061], state=0)
            self.set_interact_object(trigger_ids=[10002062], state=0)
            self.set_interact_object(trigger_ids=[10002063], state=0)
            self.set_interact_object(trigger_ids=[10002068], state=0)
            self.remove_buff(box_id=199, skill_id=99910140)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
