""" trigger/52000044_qd/10003040.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000390], state=0)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.spawn_monster(spawn_ids=[1001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[10003042], quest_states=[1]):
            self.destroy_monster(spawn_ids=[1001])
            self.spawn_monster(spawn_ids=[1003], auto_target=False)
            return 오브젝트반응대기(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[10003041], quest_states=[3]):
            self.destroy_monster(spawn_ids=[1001])
            self.spawn_monster(spawn_ids=[1003], auto_target=False)
            return 오브젝트반응조건(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[10003041], quest_states=[2]):
            self.destroy_monster(spawn_ids=[1001])
            self.spawn_monster(spawn_ids=[1003], auto_target=False)
            return 오브젝트반응조건(self.ctx)
        if self.quest_user_detected(box_ids=[103], quest_ids=[10003041], quest_states=[1]):
            return 연출시작02(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[10003041], quest_states=[1]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.destroy_monster(spawn_ids=[1001])
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.set_effect(trigger_ids=[602], visible=True)
        self.spawn_monster(spawn_ids=[2001,2002,2003,2004,2005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 말풍선대사01(self.ctx)


class 연출시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001])
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.set_effect(trigger_ids=[602], visible=True)
        self.spawn_monster(spawn_ids=[2001,2002,2003,2004,2005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 차전투시작1(self.ctx)


class 말풍선대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2001, script='$52000044_QD__10003040__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 말풍선대사02(self.ctx)


class 말풍선대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2001, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=2002, patrol_name='MS2PatrolData_2002')
        self.move_npc(spawn_id=2003, patrol_name='MS2PatrolData_2003')
        self.move_npc(spawn_id=2004, patrol_name='MS2PatrolData_2004')
        self.move_npc(spawn_id=2005, patrol_name='MS2PatrolData_2005')
        self.set_dialogue(type=1, spawn_id=2003, script='$52000044_QD__10003040__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 제이시대사01(self.ctx)


class 제이시대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000515, script='$52000044_QD__10003040__2$', time=2)
        self.set_skip(state=제이시대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 제이시대사02(self.ctx)


class 제이시대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 제이시대사02(self.ctx)


class 제이시대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_dialogue(type=2, spawn_id=11000515, script='$52000044_QD__10003040__3$', time=4)
        self.set_skip(state=제이시대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출종료(self.ctx)


class 제이시대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=302, enable=False)
        self.set_effect(trigger_ids=[601])
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 차전투시작1(self.ctx)


class 차전투시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25200441, text_id=25200441, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001,2002,2003,2004,2005]):
            self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002B')
            return 차전투시작2(self.ctx)


class 차전투시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2006]):
            self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002C')
            return NPC감지대기(self.ctx)


class NPC감지대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[1002]):
            self.set_achievement(trigger_id=199, type='trigger', achieve='EscapewithJacy')
            self.destroy_monster(spawn_ids=[1002])
            self.spawn_monster(spawn_ids=[1003], auto_target=False)
            return 오브젝트반응조건(self.ctx)


class 오브젝트반응조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[10003042], quest_states=[1]):
            return 오브젝트반응대기(self.ctx)


class 오브젝트반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000390], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000390], state=0):
            self.move_user(map_id=52000045, portal_id=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
