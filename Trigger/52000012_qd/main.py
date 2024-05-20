""" trigger/52000012_qd/main.xml """
import trigger_api


class 초기상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[6000], visible=True)
        self.set_agent(trigger_ids=[6001], visible=True)
        self.set_agent(trigger_ids=[6002], visible=True)
        self.set_agent(trigger_ids=[6003], visible=True)
        self.set_agent(trigger_ids=[6004], visible=True)
        self.set_agent(trigger_ids=[6005], visible=True)
        self.set_agent(trigger_ids=[6006], visible=True)
        self.set_agent(trigger_ids=[6007], visible=True)
        self.set_agent(trigger_ids=[6008], visible=True)
        self.set_agent(trigger_ids=[6009], visible=True)
        self.set_agent(trigger_ids=[6010], visible=True)
        self.set_agent(trigger_ids=[6011], visible=True)
        self.set_agent(trigger_ids=[6012], visible=True)
        self.set_agent(trigger_ids=[6013], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_actor(trigger_id=5001, initial_sequence='DownIdle_B')
        self.set_effect(trigger_ids=[5002])
        self.set_actor(trigger_id=10001, visible=True, initial_sequence='Closed')
        self.set_actor(trigger_id=10002, visible=True, initial_sequence='Closed')
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[5000], auto_target=False)
        self.set_agent(trigger_ids=[7000], visible=True)
        self.set_agent(trigger_ids=[7001], visible=True)
        self.set_agent(trigger_ids=[7002], visible=True)
        self.set_agent(trigger_ids=[7003], visible=True)
        self.set_agent(trigger_ids=[7004], visible=True)
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)
        self.set_agent(trigger_ids=[8009], visible=True)
        self.set_agent(trigger_ids=[8010], visible=True)
        self.set_mesh(trigger_ids=[10011], visible=True)
        self.set_mesh(trigger_ids=[10012], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002610], quest_states=[1]):
            return 레논연출1(self.ctx)


class 레논연출1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='9', seconds=2)
        self.spawn_monster(spawn_ids=[1000], auto_target=False)
        self.set_agent(trigger_ids=[7000])
        self.set_agent(trigger_ids=[7001])
        self.set_agent(trigger_ids=[7002])
        self.set_agent(trigger_ids=[7003])
        self.set_agent(trigger_ids=[7004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='9'):
            return 레논연출2(self.ctx)


class 레논연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000012_QD__MAIN__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 전투1(self.ctx)


class 전투1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103]):
            return 벨라연출시작(self.ctx)


class 벨라연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='8', seconds=3)
        self.select_camera_path(path_ids=[901,902], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='8'):
            return 벨라연출중(self.ctx)


class 벨라연출중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=7)
        self.set_dialogue(type=2, spawn_id=11000844, script='$52000012_QD__MAIN__1$', time=2)
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000012_QD__MAIN__2$', time=2)
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000012_QD__MAIN__3$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 벨라연출종료(self.ctx)


class 벨라연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='14', seconds=1)
        self.select_camera_path(path_ids=[906])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 문열림1(self.ctx)


class 문열림1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='19', seconds=1)
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.spawn_monster(spawn_ids=[203], auto_target=False)
        self.set_actor(trigger_id=10001, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[10011])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='19'):
            return 전투2(self.ctx)


class 전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1000, patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203]):
            return 문열림2(self.ctx)


class 문열림2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=2)
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.set_actor(trigger_id=10002, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[10012])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 악령연출시작(self.ctx)


class 악령연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='13', seconds=6)
        self.select_camera_path(path_ids=[904,905], return_view=False)
        self.spawn_monster(spawn_ids=[301], auto_target=False)
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='13'):
            return 화면끄기(self.ctx)


class 화면끄기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='22', seconds=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='22'):
            return 영혼연출(self.ctx)


class 영혼연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='23', seconds=2)
        self.destroy_monster(spawn_ids=[301])
        self.destroy_monster(spawn_ids=[5000])
        self.destroy_monster(spawn_ids=[301])
        self.destroy_monster(spawn_ids=[5000])
        self.set_actor(trigger_id=5001, visible=True, initial_sequence='DownIdle_B')
        self.set_effect(trigger_ids=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='23'):
            return 화면켜기(self.ctx)


class 화면켜기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='14', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 영혼연출중(self.ctx)


class 영혼연출중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=4)
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000012_QD__MAIN__4$', time=3)
        self.select_camera_path(path_ids=[905,903], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 영혼연출종료(self.ctx)


class 영혼연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1000, patrol_name='MS2PatrolData_1002')
        self.select_camera(trigger_id=903, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        return 전투3(self.ctx)


class 전투3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=5001, initial_sequence='DownIdle_B')
        self.set_effect(trigger_ids=[5002])
        self.spawn_monster(spawn_ids=[302], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[302]):
            return 레논교체(self.ctx)


class 레논교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1000])
        self.spawn_monster(spawn_ids=[2000], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[10002611], quest_states=[2]):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9001]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1000,2000,101,102,103,201,202,203,301,302])

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


initial_state = 초기상태
