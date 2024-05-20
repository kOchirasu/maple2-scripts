""" trigger/52000040_qd/main.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002635], quest_states=[1]):
            self.hide_guide_summary(entity_id=20020020)
            return ready_02(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002635], quest_states=[2]):
            return start_22(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001445], quest_states=[3]):
            return end_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001445], quest_states=[2]):
            return sb_ready_b_13(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001445], quest_states=[1]):
            return sb_ready_b_12(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001444], quest_states=[3]):
            return sb_ready_b_12(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001444], quest_states=[2]):
            # 소울바인더 퀘스트 진행
            self.set_portal(portal_id=1)
            self.hide_guide_summary(entity_id=20020020)
            return sb_ready_b_02(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001443], quest_states=[3]):
            # 소울바인더 퀘스트 완료
            self.add_buff(box_ids=[701], skill_id=70000096, level=1) # 현기증 없애
            self.set_portal(portal_id=1)
            self.hide_guide_summary(entity_id=20020020)
            return sb_ready_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001442], quest_states=[3]):
            # 소울바인더 퀘스트 진행
            return sb_ready_01(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001442], quest_states=[2]):
            # 소울바인더 퀘스트 진행
            return sb_ready_01(self.ctx)


class sb_ready_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[145])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001443], quest_states=[2]):
            # 소울바인더 퀘스트 진행
            self.add_buff(box_ids=[701], skill_id=70000096, level=1) # 현기증 없애
            self.set_portal(portal_id=1)
            self.hide_guide_summary(entity_id=20020020)
            return sb_ready_02(self.ctx)


class sb_ready_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Cut_BeyondLink_CCTV.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return sb_ready_03(self.ctx)


class sb_ready_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[144])
        self.spawn_monster(spawn_ids=[145])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001443], quest_states=[3]):
            # 소울바인더 퀘스트 진행
            return sb_ready_04(self.ctx)


class sb_ready_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])
        self.show_guide_summary(entity_id=40010, text_id=40010) # 모든 몬스터를  처치하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201]):
            self.add_buff(box_ids=[701], skill_id=70000094, level=1) # 현기증 버프
            self.hide_guide_summary(entity_id=40010)
            return sb_ready_05(self.ctx)


class sb_ready_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return sb_ready_06(self.ctx)


class sb_ready_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Push_A', duration=5000.0)
        self.add_buff(box_ids=[701], skill_id=70000095, level=1) # 현기증 2단계 버프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return sb_ready_07(self.ctx)


class sb_ready_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.add_buff(box_ids=[701], skill_id=70000096, level=1) # 현기증 없애
            return sb_ready_08(self.ctx)


class sb_ready_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000017, portal_id=1)


# 이도 공간에서 돌아온 소울 바인더
class sb_ready_b_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000040, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return sb_ready_b_03(self.ctx)


class sb_ready_b_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[221,222,223])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[7001,7002,7003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return sb_ready_b_04(self.ctx)


class sb_ready_b_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7100], return_view=False)
        self.move_npc(spawn_id=221, patrol_name='MS2PatrolData_2101')
        self.move_npc(spawn_id=222, patrol_name='MS2PatrolData_2102')
        self.move_npc(spawn_id=223, patrol_name='MS2PatrolData_2103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return sb_ready_b_06(self.ctx)


class sb_ready_b_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001726, script='$52000040_QD__MAIN__26$', time=4)
        self.set_skip(state=sb_ready_b_07_skip)
        self.set_npc_emotion_loop(spawn_id=221, sequence_name='Talk_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return sb_ready_b_07_skip(self.ctx)


class sb_ready_b_07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return sb_ready_b_07(self.ctx)


class sb_ready_b_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001728, script='$52000040_QD__MAIN__27$', time=4)
        self.set_skip(state=sb_ready_b_08_skip)
        self.set_npc_emotion_loop(spawn_id=222, sequence_name='Talk_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return sb_ready_b_08_skip(self.ctx)


class sb_ready_b_08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return sb_ready_b_08(self.ctx)


class sb_ready_b_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001726, script='$52000040_QD__MAIN__28$', time=4)
        self.set_skip(state=sb_ready_b_09_skip)
        self.set_npc_emotion_loop(spawn_id=221, sequence_name='Talk_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return sb_ready_b_09_skip(self.ctx)


class sb_ready_b_09_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return sb_ready_b_09(self.ctx)


class sb_ready_b_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001724, script='$52000040_QD__MAIN__29$', time=4)
        self.set_skip(state=sb_ready_b_10_skip)
        self.set_npc_emotion_loop(spawn_id=223, sequence_name='Talk_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return sb_ready_b_10_skip(self.ctx)


class sb_ready_b_10_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return sb_ready_b_10(self.ctx)


class sb_ready_b_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[145])
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.select_camera_path(path_ids=[7010])
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return sb_ready_b_11(self.ctx)


class sb_ready_b_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class sb_ready_b_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[145])
        self.spawn_monster(spawn_ids=[221,222,223])
        self.move_npc(spawn_id=221, patrol_name='MS2PatrolData_2101')
        self.move_npc(spawn_id=222, patrol_name='MS2PatrolData_2102')
        self.move_npc(spawn_id=223, patrol_name='MS2PatrolData_2103')


class sb_ready_b_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[145])


class sb_end(trigger_api.Trigger):
    pass


class ready_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2001')
        self.spawn_monster(spawn_ids=[101,102])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[7001,7002,7003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ready_03(self.ctx)


class ready_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000040_QD__MAIN__0$', time=5)
        self.set_skip(state=ready_04_skip)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Idle_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ready_04(self.ctx)


class ready_04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ready_04(self.ctx)


class ready_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000040_QD__MAIN__1$', time=5)
        self.set_skip(state=ready_05_skip)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Idle_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ready_05(self.ctx)


class ready_05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ready_05(self.ctx)


class ready_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000040_QD__MAIN__2$', time=5)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Idle_A', duration=5000.0)
        self.set_skip(state=ready_06_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ready_06(self.ctx)


class ready_06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ready_06(self.ctx)


class ready_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000040_QD__MAIN__3$', time=5)
        self.set_skip(state=ready_07_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ready_07(self.ctx)


class ready_07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ready_07(self.ctx)


class ready_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000040_QD__MAIN__4$', time=5)
        self.set_skip(state=ready_08_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ready_08(self.ctx)


class ready_08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ready_08(self.ctx)


class ready_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000040_QD__MAIN__5$', time=5)
        self.set_skip(state=ready_09_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ready_09(self.ctx)


class ready_09_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ready_09(self.ctx)


class ready_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000040_QD__MAIN__6$', time=5)
        self.set_skip(state=ready_10_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ready_10(self.ctx)


class ready_10_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ready_10(self.ctx)


class ready_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Cut_BeyondLink_CCTV.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return start_01(self.ctx)


class start_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__7$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_01_ready(self.ctx)


class start_01_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2004')
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2003')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7005], return_view=False)
        self.spawn_monster(spawn_ids=[103])
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000040_QD__MAIN__8$', time=5)
        self.set_skip(state=start_02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_03(self.ctx)


class start_02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000040_QD__MAIN__9$', time=5)
        self.set_skip(state=start_03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_04(self.ctx)


class start_03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000040_QD__MAIN__10$', time=4)
        self.set_skip(state=start_04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_05(self.ctx)


class start_04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7006,7007], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__11$', time=5)
        self.set_skip(state=start_05_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_06(self.ctx)


class start_05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__12$', time=4)
        self.set_skip(state=start_06_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_07(self.ctx)


class start_06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000040_QD__MAIN__13$', time=5)
        self.set_skip(state=start_07_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_08(self.ctx)


class start_07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_08(self.ctx)


class start_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7008], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__14$', time=5)
        self.set_skip(state=start_08_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_09(self.ctx)


class start_08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_09(self.ctx)


class start_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000040_QD__MAIN__15$', time=3)
        self.set_skip(state=start_09_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_10(self.ctx)


class start_09_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_10(self.ctx)


class start_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000040_QD__MAIN__16$', time=5)
        self.set_skip(state=start_10_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_11(self.ctx)


class start_10_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_11(self.ctx)


class start_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__17$', time=4)
        self.set_skip(state=start_11_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_12(self.ctx)


class start_11_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_12(self.ctx)


class start_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000040_QD__MAIN__18$', time=3)
        self.set_skip(state=start_12_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_13(self.ctx)


class start_12_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_13(self.ctx)


class start_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__19$', time=5)
        self.set_skip(state=start_13_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_14(self.ctx)


class start_13_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_14(self.ctx)


class start_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__20$', time=5)
        self.set_skip(state=start_14_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_15(self.ctx)


class start_14_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_15(self.ctx)


class start_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__21$', time=5)
        self.set_skip(state=start_15_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_16(self.ctx)


class start_15_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_16(self.ctx)


class start_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__22$', time=5)
        self.set_skip(state=start_16_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_17(self.ctx)


class start_16_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return start_17(self.ctx)


class start_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000040_QD__MAIN__23$', time=3)
        # Missing State: start_17_skip
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_18(self.ctx)


class start_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2005')
        self.select_camera_path(path_ids=[7009], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__24$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_19(self.ctx)


class start_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001548, script='$52000040_QD__MAIN__25$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.destroy_monster(spawn_ids=[103,102,101])
            return start_20(self.ctx)


class start_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[7010])
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_cinematic_ui(type=0)
            self.spawn_monster(spawn_ids=[104,111,112])
            self.set_cinematic_ui(type=2)
            return start_21(self.ctx)


class start_21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20020020, text_id=20020020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002635], quest_states=[2]):
            self.hide_guide_summary(entity_id=20020020)
            return end_01(self.ctx)


class start_22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104,111,112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[40002635], quest_states=[2]):
            self.hide_guide_summary(entity_id=20020020)
            return end_01(self.ctx)


class end_01(trigger_api.Trigger):
    pass


initial_state = ready
