""" trigger/52000028_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014], auto_target=False)
        self.set_mesh(trigger_ids=[3001], visible=True)
        self.set_mesh(trigger_ids=[3002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[101], quest_ids=[20002250], quest_states=[1], job_code=90):
            return 연출시작(self.ctx)
        if self.quest_user_detected(box_ids=[101], quest_ids=[20002251], quest_states=[1], job_code=90):
            return NPC이동01(self.ctx)
        if self.quest_user_detected(box_ids=[101], quest_ids=[10002931], quest_states=[1]):
            return 연출시작(self.ctx)
        if self.quest_user_detected(box_ids=[101], quest_ids=[10002932], quest_states=[1]):
            return NPC이동01(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아시모프이동(self.ctx)


class 아시모프이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[1001]):
            return 책장변경(self.ctx)


class 책장변경(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001])
        self.set_mesh(trigger_ids=[3002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 동영상재상(self.ctx)


class 동영상재상(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Starlight_expedition.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 이슈라대사01(self.ctx)


class 이슈라대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000028_QD__MAIN__0$', time=5) # 음성 코드 00001294

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return 이슈라대사02(self.ctx)


class 이슈라대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000028_QD__MAIN__1$', time=6) # 음성 코드 00001295

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 아시모프대사01(self.ctx)


class 아시모프대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001_B')
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_dialogue(type=2, spawn_id=11000031, script='$52000028_QD__MAIN__2$', time=3) # 음성 코드 00001343

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아시모프대사02(self.ctx)


class 아시모프대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_dialogue(type=2, spawn_id=11000031, script='$52000028_QD__MAIN__3$', time=6) # 음성 코드 00001344

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 퀘스트수락대기(self.ctx)

    def on_exit(self) -> None:
        self.set_achievement(trigger_id=101, type='trigger', achieve='BackstoryOfRune')
        self.select_camera(trigger_id=301, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 퀘스트수락대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[101], quest_ids=[20002251], quest_states=[1], job_code=90):
            return NPC이동01(self.ctx)
        if self.quest_user_detected(box_ids=[101], quest_ids=[10002932], quest_states=[1]):
            return NPC이동01(self.ctx)


class NPC이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_A')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_A')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPC이동02(self.ctx)


class NPC이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1008, patrol_name='MS2PatrolData_1008_A')
        self.move_npc(spawn_id=1013, patrol_name='MS2PatrolData_1013_A')
        self.move_npc(spawn_id=1014, patrol_name='MS2PatrolData_1014_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
