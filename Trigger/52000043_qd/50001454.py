""" trigger/52000043_qd/50001454.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606])
        self.set_effect(trigger_ids=[607])
        self.set_effect(trigger_ids=[608])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001454], quest_states=[1]):
            self.destroy_monster(spawn_ids=[1003,2003])
            return 시작조건(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001454], quest_states=[2]):
            self.destroy_monster(spawn_ids=[1003,2003])
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001454], quest_states=[3]):
            self.destroy_monster(spawn_ids=[1003,2003])
            return 종료(self.ctx)


class 시작조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1003,2003], auto_target=False)
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017])
        self.set_interact_object(trigger_ids=[10001020], state=2)
        self.set_interact_object(trigger_ids=[10001021], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=305)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003D')
        self.move_user_path(patrol_name='MS2PatrolData_PCD')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 말퉁선대사01(self.ctx)


class 말퉁선대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1003, script='$52000043_QD__50001454__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NPC이동02(self.ctx)


class NPC이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003E')
        self.move_user_path(patrol_name='MS2PatrolData_PCE')
        self.move_npc(spawn_id=2003, patrol_name='MS2PatrolData_2003D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=105, spawn_ids=[2003]):
            return 준타대사01(self.ctx)


class 준타대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__1$', time=4)
        self.set_skip(state=준타대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 틴차이대사01(self.ctx)


class 준타대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 틴차이대사01(self.ctx)


class 틴차이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000043_QD__50001454__2$', time=4)
        self.set_skip(state=틴차이대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 준타대사02(self.ctx)


class 틴차이대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사02(self.ctx)


class 준타대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__3$', time=4)
        self.set_skip(state=준타대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 준타대사03(self.ctx)


class 준타대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사03(self.ctx)


class 준타대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__4$', time=5)
        self.set_skip(state=준타대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 틴차이대사02(self.ctx)


class 준타대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 틴차이대사02(self.ctx)


class 틴차이대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[607], visible=True)
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000043_QD__50001454__5$', time=3)
        self.set_skip(state=틴차이대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 준타대사04(self.ctx)


class 틴차이대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[607])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사04(self.ctx)


class 준타대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__6$', time=3)
        self.set_skip(state=준타대사04스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 준타대사05(self.ctx)


class 준타대사04스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사05(self.ctx)


class 준타대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__7$', time=5)
        self.set_skip(state=준타대사05스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 준타대사06(self.ctx)


class 준타대사05스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사06(self.ctx)


class 준타대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__8$', time=5)
        self.set_skip(state=준타대사06스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 준타대사07(self.ctx)


class 준타대사06스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사07(self.ctx)


class 준타대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__9$', time=6)
        self.set_skip(state=준타대사07스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 준타대사08(self.ctx)


class 준타대사07스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사08(self.ctx)


class 준타대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__10$', time=3)
        self.set_skip(state=준타대사08스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 틴차이대사03(self.ctx)


class 준타대사08스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 틴차이대사03(self.ctx)


class 틴차이대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000043_QD__50001454__26$', time=2)
        self.set_skip(state=틴차이대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 준타대사09(self.ctx)


class 틴차이대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사09(self.ctx)


class 준타대사09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__11$', time=4)
        self.set_skip(state=준타대사09스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 준타대사10(self.ctx)


class 준타대사09스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사10(self.ctx)


class 준타대사10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__12$', time=4)
        self.set_skip(state=준타대사10스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 준타대사11(self.ctx)


class 준타대사10스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사11(self.ctx)


class 준타대사11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__13$', time=4)
        self.set_skip(state=준타대사11스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 틴차이대사04(self.ctx)


class 준타대사11스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 틴차이대사04(self.ctx)


class 틴차이대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000043_QD__50001454__14$', time=2)
        self.set_skip(state=틴차이대사04스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 준타대사12(self.ctx)


class 틴차이대사04스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사12(self.ctx)


class 준타대사12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__15$', time=4)
        self.set_skip(state=준타대사12스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 준타대사13(self.ctx)


class 준타대사12스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사13(self.ctx)


class 준타대사13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__16$', time=4)
        self.set_skip(state=준타대사13스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PC이동(self.ctx)


class 준타대사13스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[608])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC이동(self.ctx)


class PC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=306)
        self.move_user_path(patrol_name='MS2PatrolData_PCG')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return 준타대사14(self.ctx)


class 준타대사14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__17$', time=4)
        self.set_skip(state=준타대사14스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 틴차이대사05(self.ctx)


class 준타대사14스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 틴차이대사05(self.ctx)


class 틴차이대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000043_QD__50001454__18$', time=2)
        self.set_skip(state=틴차이대사05스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 준타대사15(self.ctx)


class 틴차이대사05스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사15(self.ctx)


class 준타대사15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__19$', time=6)
        self.set_skip(state=준타대사15스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 준타대사16(self.ctx)


class 준타대사15스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사16(self.ctx)


class 준타대사16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__20$', time=3)
        self.set_skip(state=준타대사16스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 준타대사17(self.ctx)


class 준타대사16스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사17(self.ctx)


class 준타대사17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__21$', time=4)
        self.set_skip(state=준타대사17스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 틴차이대사06(self.ctx)


class 준타대사17스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 틴차이대사06(self.ctx)


class 틴차이대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000043_QD__50001454__22$', time=3)
        self.set_skip(state=틴차이대사06스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 준타대사18(self.ctx)


class 틴차이대사06스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사18(self.ctx)


class 준타대사18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__23$', time=5)
        self.set_skip(state=준타대사18스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 준타대사19(self.ctx)


class 준타대사18스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사19(self.ctx)


class 준타대사19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__24$', time=6)
        self.set_skip(state=준타대사19스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 준타대사20(self.ctx)


class 준타대사19스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사20(self.ctx)


class 준타대사20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000043_QD__50001454__25$', time=3)
        self.set_skip(state=준타대사20스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출종료(self.ctx)


class 준타대사20스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=199, type='trigger', achieve='gdfight')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.move_user(map_id=2000039, portal_id=10)
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
