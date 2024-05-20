""" trigger/52000062_qd/guidescene_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 유저감지(self.ctx)


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000561], quest_states=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000561], quest_states=[2]):
            return 연퀘감지2(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000560,90000561], quest_states=[1]):
            return 연퀘감지(self.ctx)
        if self.user_detected(box_ids=[199]):
            return 페르시카대사01(self.ctx)


class 페르시카대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 페르시카대사02(self.ctx)


class 페르시카대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001176, script='$52000062_QD__GUIDESCENE_01__0$', time=3)
        self.set_dialogue(type=2, spawn_id=11001176, script='$52000062_QD__GUIDESCENE_01__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 연퀘감지(self.ctx)


class 연퀘감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_Fercika')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[90000561], quest_states=[2]):
            return PC이동(self.ctx)


class 연퀘감지2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_Fercika')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PC이동(self.ctx)


class PC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.move_user_path(patrol_name='MS2PatrolData_PC')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[198]):
            return 찬양NPC이동(self.ctx)


class 찬양NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_Fercika2')
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.destroy_monster(spawn_ids=[1002], arg2=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.destroy_monster(spawn_ids=[1004], arg2=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)
        self.destroy_monster(spawn_ids=[1007], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=197, spawn_ids=[1001]):
            return 찬양연출(self.ctx)


class 찬양연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1008, script='$52000062_QD__GUIDESCENE_01__2$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=1005, script='$52000062_QD__GUIDESCENE_01__3$', time=2, arg5=3)
        self.set_dialogue(type=1, spawn_id=1006, script='$52000062_QD__GUIDESCENE_01__4$', time=2, arg5=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출종료2(self.ctx)


class 연출종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=301, enable=False)
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
