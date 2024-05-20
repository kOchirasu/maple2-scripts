""" trigger/02000065_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.spawn_monster(spawn_ids=[101], auto_target=False)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001630], quest_states=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001630], quest_states=[2]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001630], quest_states=[1]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001625], quest_states=[3]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001625], quest_states=[2]):
            return 연출2준비(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001625], quest_states=[1]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001624], quest_states=[3]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001624], quest_states=[2]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001624], quest_states=[1]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001623], quest_states=[3]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001623], quest_states=[2]):
            return 앤있음(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001623], quest_states=[1]):
            return 연출1준비(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001622], quest_states=[3]):
            return 기본상태(self.ctx)


class 기본상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,111])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 퀘스트조건체크(self.ctx)


class 앤있음(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001625], quest_states=[2]):
            return 연출2준비(self.ctx)
        if self.wait_tick(wait_tick=100):
            return 종료(self.ctx)


class 연출1준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출1앤등장준비(self.ctx)


class 연출1앤등장준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 앤등장(self.ctx)


class 앤등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_ann01')
        self.add_cinematic_talk(npc_id=11003432, illust_id='Ann_normal', msg='$02000065_BF__MAIN__0$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 앤등장2(self.ctx)


class 앤등장2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)
        self.add_balloon_talk(spawn_id=101, msg='$02000065_BF__MAIN__1$', duration=3000)
        # self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_ann02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 연출종료(self.ctx)


class 연출2준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출2준비1(self.ctx)


class 연출2준비1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 앤대사01(self.ctx)


class 앤대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010,8011], return_view=False)
        self.add_cinematic_talk(npc_id=11003432, msg='$02000065_BF__MAIN__2$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Talk_A', duration=3000.0)
        self.set_scene_skip(state=칼과앤_스킵완료, action='nextState') # setsceneskip set
        self.set_skip(state=앤대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 칼대사01(self.ctx)


class 앤대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칼대사01(self.ctx)


class 칼대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000074, msg='$02000065_BF__MAIN__3$', duration=3000)
        self.set_skip(state=칼대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 앤대사02(self.ctx)


class 칼대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 앤대사02(self.ctx)


class 앤대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003432, msg='$02000065_BF__MAIN__4$', duration=4000)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Talk_A', duration=3000.0)
        self.set_skip(state=앤대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6400):
            return 칼대사02(self.ctx)


class 앤대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칼대사02(self.ctx)


class 칼대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000074, msg='$02000065_BF__MAIN__5$', duration=3000)
        self.set_skip(state=칼대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8071):
            return 앤대사03(self.ctx)


class 칼대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 앤대사03(self.ctx)


class 앤대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003432, msg='$02000065_BF__MAIN__6$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Talk_A', duration=2000.0)
        self.set_skip(state=앤대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6713):
            return 칼대사03(self.ctx)


class 앤대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칼대사03(self.ctx)


class 칼대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000074, msg='$02000065_BF__MAIN__7$', duration=4000)
        self.set_skip(state=칼대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9769):
            return 앤대사04(self.ctx)


class 칼대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 앤대사04(self.ctx)


class 앤대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003432, msg='$02000065_BF__MAIN__8$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Talk_A', duration=2000.0)
        self.set_skip(state=앤대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 칼대사04(self.ctx)


class 앤대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 칼대사04(self.ctx)


class 칼대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000074, msg='$02000065_BF__MAIN__9$', duration=3000)
        self.set_skip(state=칼대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7471):
            return 앤대사05(self.ctx)


class 칼대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 앤대사05(self.ctx)


class 앤대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_dialogue(type=2, spawn_id=11003432, script='$02000065_BF__MAIN__10$', time=3)
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Talk_A', duration=2000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3160):
            return 카메라아웃(self.ctx)


class 카메라아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000,8001], return_view=False)
        self.visible_my_pc(is_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 연출종료(self.ctx)


class 칼과앤_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.visible_my_pc(is_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='meetingAnn')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
