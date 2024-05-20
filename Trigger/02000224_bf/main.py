""" trigger/02000224_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[2]):
            return 다음맵으로(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[1]):
            return 연출준비00(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001561], quest_states=[3]):
            return 아르마노있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001561], quest_states=[2]):
            return 아르마노있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001561], quest_states=[1]):
            return 아르마노있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001560], quest_states=[3]):
            return 아르마노있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001560], quest_states=[2]):
            return 아르마노있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001560], quest_states=[1]):
            return 기본상태(self.ctx)


class 기본상태(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 아르마노있음(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[1]):
            return 연출준비(self.ctx)
        if not self.quest_user_detected(box_ids=[9000], quest_ids=[50001562], quest_states=[1]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 다음맵으로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[104], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 연출종료(self.ctx)


class 연출준비00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=아르마노말썽_스킵완료, action='exit') # setsceneskip 정의
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출준비(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.move_user(map_id=2000224, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 티니에등장(self.ctx)


class 티니에등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__18$', time=3)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Bore_C', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 티니에이동01(self.ctx)


class 티니에이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_girl01')
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아르마노대사01(self.ctx)


class 아르마노대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003242, script='$02000224_BF__MAIN__1$', time=4)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=아르마노대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 티니에대사01(self.ctx)


class 아르마노대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 티니에대사01(self.ctx)


class 티니에대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__2$', time=4)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=티니에대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6765):
            return 아르마노대사02(self.ctx)


class 티니에대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사02(self.ctx)


class 아르마노대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_girl02')
        self.set_dialogue(type=2, spawn_id=11003242, script='$02000224_BF__MAIN__3$', time=4)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=아르마노대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4597):
            return 티니에대사02(self.ctx)


class 아르마노대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 티니에대사02(self.ctx)


class 티니에대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__4$', time=4)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=티니에대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7471):
            return 티니에이동02(self.ctx)


class 티니에대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 티니에이동02(self.ctx)


class 티니에이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_girl02')
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__5$', time=4)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=4000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10109):
            return 티니에대사03(self.ctx)


class 티니에대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__6$', time=4)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=티니에대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9090):
            return 아르마노대사03(self.ctx)


class 티니에대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사03(self.ctx)


class 아르마노대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003242, script='$02000224_BF__MAIN__7$', time=4)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=아르마노대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5146):
            return 티니에대사04(self.ctx)


class 아르마노대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 티니에대사04(self.ctx)


class 티니에대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__8$', time=4)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=티니에대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7418):
            return 아르마노대사04(self.ctx)


class 티니에대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사04(self.ctx)


class 아르마노대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003242, script='$02000224_BF__MAIN__9$', time=4)
        self.set_skip(state=아르마노대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아르마노대사05(self.ctx)


class 아르마노대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노대사05(self.ctx)


class 아르마노대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.set_dialogue(type=2, spawn_id=11003242, script='$02000224_BF__MAIN__10$', time=3)
        self.set_skip(state=아르마노대사05_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3030):
            return 아르마노탈주(self.ctx)


class 아르마노대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 아르마노탈주(self.ctx)


class 아르마노탈주(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_boy01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 티니에대사05(self.ctx)


class 티니에대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_girl03')
        self.destroy_monster(spawn_ids=[101])
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__11$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 티니에대사06(self.ctx)


class 티니에대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_PC01')
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__12$', time=4)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Bore_C', duration=4000.0)
        self.set_skip(state=티니에대사06_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11023):
            return PC대사01(self.ctx)


class 티니에대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return PC대사01(self.ctx)


class PC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$02000224_BF__MAIN__13$', time=3)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 티니에대사07(self.ctx)


class 티니에대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__14$', time=4)
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='ChatUp_A')
        self.set_skip(state=티니에대사07_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7810):
            return PC대사02(self.ctx)


class 티니에대사07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 티니에대사08(self.ctx)


class PC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$02000224_BF__MAIN__15$', time=3)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 티니에대사08(self.ctx)


class 티니에대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__16$', time=4)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=4000.0)
        self.set_skip(state=티니에대사08_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7497):
            return 티니에대사09(self.ctx)


class 티니에대사08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 티니에대사09(self.ctx)


class 티니에대사09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11003243, script='$02000224_BF__MAIN__17$', time=4)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=4000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7157):
            return 연출종료(self.ctx)


class 아르마노말썽_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,103])
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='foolishson')
        self.move_user(map_id=2000054, portal_id=10)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
