""" trigger/52000041_qd/main.xml """
import trigger_api


class 완료조건체크50001392(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[606])

    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[199], quest_ids=[50001392], quest_states=[3]):
            return 상태01(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001392], quest_states=[3]):
            return 상태02조건(self.ctx)


class 진행조건체크50001402(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001402], quest_states=[1]):
            return 연출시작(self.ctx)
        if not self.quest_user_detected(box_ids=[199], quest_ids=[50001402], quest_states=[1]):
            return 진행조건체크50001400(self.ctx)


class 진행조건체크50001400(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001400], quest_states=[1]):
            return 상태02(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001400], quest_states=[2]):
            return 상태02(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001400], quest_states=[3]):
            return 상태02(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 상태01(self.ctx)


class 상태02조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[199], quest_ids=[50001421], quest_states=[3]):
            return 진행조건체크50001402(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001421], quest_states=[3]):
            return 상태03조건(self.ctx)


class 상태03조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[199], quest_ids=[50001431], quest_states=[3]):
            return 상태03(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001431], quest_states=[3]):
            return 상태03_2조건(self.ctx)


class 상태03_2조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[199], quest_ids=[50001432], quest_states=[3]):
            return 상태03(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001432], quest_states=[3]):
            return 상태04조건(self.ctx)


class 상태04조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[199], quest_ids=[50001433], quest_states=[3]):
            return 상태04(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001432], quest_states=[2]):
            return 상태07(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001433], quest_states=[3]):
            return 상태05조건(self.ctx)


class 상태05조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[199], quest_ids=[50001444], quest_states=[3]):
            return 상태05(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001444], quest_states=[3]):
            return 상태06조건(self.ctx)


class 상태06조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[199], quest_ids=[50001450], quest_states=[3]):
            return 상태06(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001450], quest_states=[3]):
            return 상태06_2조건(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 상태06_2조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[199], quest_ids=[50001451], quest_states=[3]):
            return 상태06(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001451], quest_states=[3]):
            return 상태07조건(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 상태07조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001451], quest_states=[1]):
            return 상태06(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001451], quest_states=[2]):
            return 상태07(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001453], quest_states=[3]):
            return 상태08조건(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 상태08조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.quest_user_detected(box_ids=[199], quest_ids=[50001454], quest_states=[3]):
            return 상태08(self.ctx)
        if self.quest_user_detected(box_ids=[199], quest_ids=[50001454], quest_states=[3]):
            return 종료(self.ctx)


class 상태01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,2001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 상태02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1002,2002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 상태03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 상태04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 상태05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 상태06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1006,2006], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 상태07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 상태08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1008], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1000,2000,3000], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=2000, sequence_name='DownIdle_A', duration=2000.0)
        self.set_npc_emotion_loop(spawn_id=3000, sequence_name='Talk_A', duration=30000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NPC이동01(self.ctx)


class NPC이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.move_npc(spawn_id=2000, patrol_name='MS2PatrolData_2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return NPC이동02(self.ctx)


class NPC이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1000, patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PC이동(self.ctx)


class PC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_9000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 어흥이대사01(self.ctx)


class 어흥이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_dialogue(type=2, spawn_id=11001729, script='$52000041_QD__MAIN__0$', time=3)
        self.set_skip(state=어흥이대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 틴차이대사01(self.ctx)


class 어흥이대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 틴차이대사01(self.ctx)


class 틴차이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000041_QD__MAIN__1$', time=3)
        self.set_skip(state=틴차이대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 준타대사01(self.ctx)


class 틴차이대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[602])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사01(self.ctx)


class 준타대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000041_QD__MAIN__2$', time=6)
        self.set_skip(state=준타대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 어흥이대사02(self.ctx)


class 준타대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 어흥이대사02(self.ctx)


class 어흥이대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001729, script='$52000041_QD__MAIN__3$', time=4)
        self.set_skip(state=어흥이대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 준타대사02(self.ctx)


class 어흥이대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사02(self.ctx)


class 준타대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000041_QD__MAIN__4$', time=5)
        self.set_skip(state=준타대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 준타대사02_2(self.ctx)


class 준타대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 준타대사02_2(self.ctx)


class 준타대사02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000041_QD__MAIN__5$', time=3)
        self.set_skip(state=준타대사02_2스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 어흥이대사03(self.ctx)


class 준타대사02_2스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 어흥이대사03(self.ctx)


class 어흥이대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_dialogue(type=2, spawn_id=11001729, script='$52000041_QD__MAIN__6$', time=3)
        self.set_skip(state=어흥이대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NPC이동03(self.ctx)


class 어흥이대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[604])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return NPC이동03(self.ctx)


class NPC이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)
        self.move_npc(spawn_id=1000, patrol_name='MS2PatrolData_1000B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 틴차이대사02(self.ctx)


class 틴차이대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000041_QD__MAIN__7$', time=3)
        self.set_skip(state=틴차이대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 틴차이대사03(self.ctx)


class 틴차이대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 틴차이대사03(self.ctx)


class 틴차이대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000041_QD__MAIN__8$', time=3)
        self.set_skip(state=틴차이대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 틴차이대사04(self.ctx)


class 틴차이대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 틴차이대사04(self.ctx)


class 틴차이대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000041_QD__MAIN__9$', time=3)
        self.set_skip(state=틴차이대사04스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 말풍선대사01(self.ctx)


class 틴차이대사04스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 말풍선대사01(self.ctx)


class 말풍선대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1000, script='$52000041_QD__MAIN__10$', time=3)
        self.set_dialogue(type=1, spawn_id=3000, script='$52000041_QD__MAIN__11$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 말풍선대사02(self.ctx)


class 말풍선대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=2000, script='$52000041_QD__MAIN__15$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 말풍선대사03(self.ctx)


class 말풍선대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=3000, script='$52000041_QD__MAIN__16$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 말풍선대사04(self.ctx)


class 말풍선대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1000, script='$52000041_QD__MAIN__17$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 말풍선대사05(self.ctx)


class 말풍선대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000041_QD__MAIN__18$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 준타대사03(self.ctx)


class 준타대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[605], visible=True)
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000041_QD__MAIN__12$', time=5)
        self.set_skip(state=준타대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 어흥이대사05(self.ctx)


class 준타대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[605])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 어흥이대사05(self.ctx)


class 어흥이대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606], visible=True)
        self.set_dialogue(type=2, spawn_id=11001729, script='$52000041_QD__MAIN__13$', time=4)
        self.set_skip(state=어흥이대사05스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 어흥이대사06(self.ctx)


class 어흥이대사05스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[606])
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 어흥이대사06(self.ctx)


class 어흥이대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001729, script='$52000041_QD__MAIN__14$', time=1)
        self.set_skip(state=어흥이대사06스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return NPC이동04(self.ctx)


class 어흥이대사06스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return NPC이동04(self.ctx)


class NPC이동04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302)
        self.move_npc(spawn_id=3000, patrol_name='MS2PatrolData_3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=101, spawn_ids=[3000]):
            self.destroy_monster(spawn_ids=[3000])
            return NPC이동05(self.ctx)


class NPC이동05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=302, enable=False)
        self.move_npc(spawn_id=1000, patrol_name='MS2PatrolData_1000C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.destroy_monster(spawn_ids=[1000,2000])
            self.spawn_monster(spawn_ids=[1010,2010], auto_target=False)
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=199, type='trigger', achieve='gdreunion')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 완료조건체크50001392
