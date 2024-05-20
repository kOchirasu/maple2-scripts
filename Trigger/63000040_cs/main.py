""" trigger/63000040_cs/main.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,103,104], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002652], quest_states=[3]):
            return start_02(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002652], quest_states=[2]):
            return start_02_ready(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002652], quest_states=[1]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25200474, text_id=25200474)
        self.set_effect(trigger_ids=[7001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002652], quest_states=[2]):
            return start_02_ready(self.ctx)


class start_02_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25200474)
        self.set_effect(trigger_ids=[7001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002652], quest_states=[3]):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2001') # 연출용 틴차이 이동
        self.move_user_path(patrol_name='MS2PatrolData_2002') # 유저를 이동시킨다
        self.select_camera_path(path_ids=[8001,8002], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000040_CS__MAIN__0$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=3000.0)
        self.set_dialogue(type=2, spawn_id=11001708, script='$63000040_CS__MAIN__1$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2003') # 연출용 틴차이 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2003') # 연출용 틴차이 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2003') # 유저를 이동시킨다

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.select_camera_path(path_ids=[8003], return_view=False)
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = ready
