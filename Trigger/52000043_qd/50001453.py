""" trigger/52000043_qd/50001453.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1003,2003])
        self.set_agent(trigger_ids=[9000])
        self.set_agent(trigger_ids=[9001])
        self.set_agent(trigger_ids=[9002])
        self.set_agent(trigger_ids=[9003])
        self.set_agent(trigger_ids=[9004])
        self.set_agent(trigger_ids=[9005])
        self.set_agent(trigger_ids=[9006])
        self.set_agent(trigger_ids=[9007])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001453], quest_states=[1]):
            self.destroy_monster(spawn_ids=[1003,2003])
            return 시작조건(self.ctx)


class 시작조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1003,2003], auto_target=False)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017])
        self.set_interact_object(trigger_ids=[10001020], state=2)
        self.set_interact_object(trigger_ids=[10001021], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001021], state=0):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[9000], visible=True)
        self.set_agent(trigger_ids=[9001], visible=True)
        self.set_agent(trigger_ids=[9002], visible=True)
        self.set_agent(trigger_ids=[9003], visible=True)
        self.set_agent(trigger_ids=[9004], visible=True)
        self.set_agent(trigger_ids=[9005], visible=True)
        self.set_agent(trigger_ids=[9006], visible=True)
        self.set_agent(trigger_ids=[9007], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[2100,2101], auto_target=False)
        self.select_camera(trigger_id=303)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1004A')
        self.move_npc(spawn_id=2003, patrol_name='MS2PatrolData_2004A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPC대사01(self.ctx)


class NPC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_dialogue(type=2, spawn_id=29000121, script='$52000043_QD__50001453__0$', time=3)
        self.set_skip(state=NPC대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 준타대사01(self.ctx)


class NPC대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사01(self.ctx)


class 준타대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001453__1$', time=3)
        self.set_skip(state=준타대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 준타대사02(self.ctx)


class 준타대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사02(self.ctx)


class 준타대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001453__2$', time=2)
        self.set_skip(state=준타대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 틴차이대사01(self.ctx)


class 준타대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 틴차이대사01(self.ctx)


class 틴차이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[605], visible=True)
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000043_QD__50001453__3$', time=4)
        self.set_skip(state=틴차이대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출종료(self.ctx)


class 틴차이대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[605])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1003,2003])
        self.spawn_monster(spawn_ids=[1004,2004], auto_target=False)
        self.set_agent(trigger_ids=[9000])
        self.set_agent(trigger_ids=[9001])
        self.set_agent(trigger_ids=[9002])
        self.set_agent(trigger_ids=[9003])
        self.set_agent(trigger_ids=[9004])
        self.set_agent(trigger_ids=[9005])
        self.set_agent(trigger_ids=[9006])
        self.set_agent(trigger_ids=[9007])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=303, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2100,2101]):
            return 연출02시작(self.ctx)


class 연출02시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_interact_object(trigger_ids=[10001021], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1002C')
        self.move_npc(spawn_id=2004, patrol_name='MS2PatrolData_2002C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[1004]):
            return NPC교체01(self.ctx)


class NPC교체01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1004])
        self.spawn_monster(spawn_ids=[1003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=103, spawn_ids=[2004]):
            return NPC교체02(self.ctx)


class NPC교체02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2004])
        self.spawn_monster(spawn_ids=[2003], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출종료2(self.ctx)


class 연출종료2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
