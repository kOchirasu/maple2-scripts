""" trigger/52010061_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


"""
룬블레이더 떡밥
11003843 - 렌듀비앙(101)
11003844 - 유페리아(102)
11003845 - 이슈라(104)
11003846 - 레잔(103)
"""
class 입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[6001], quest_ids=[91000076], quest_states=[3]):
            return 칼리브해안전경(self.ctx)
        if not self.quest_user_detected(box_ids=[6001], quest_ids=[91000076], quest_states=[3]):
            return 맵이동(self.ctx)


class 칼리브해안전경(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(is_visible=False) # 유저안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 칼리브해안전경_02(self.ctx)


class 칼리브해안전경_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=종료_02, action='exit')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4001,4002], return_view=False) # 전경비추는카메라

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 칼리브해안전경_03(self.ctx)


class 칼리브해안전경_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52010061_QD__main__0$', align=Align.Center | Align.Left, duration=2800, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1800):
            return 교역선비추기(self.ctx)


class 교역선비추기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 스폰조절(self.ctx)


class 스폰조절(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 렌듀비앙
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 유페리아
        self.spawn_monster(spawn_ids=[103], auto_target=False) # 레잔

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 교역선비추기_02(self.ctx)


class 교역선비추기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4003,4005], return_view=False) # 교역선비추는카메라

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 레잔대사_01(self.ctx)


class 레잔대사_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=11003846, msg='$52010061_QD__main__1$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 레잔대사_02(self.ctx)


class 레잔대사_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.add_cinematic_talk(npc_id=11003846, msg='$52010061_QD__main__2$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 유페리아대사_01(self.ctx)


class 유페리아대사_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=6000.0)
        self.add_cinematic_talk(npc_id=11003844, illust_id='Yuperia_normal', msg='$52010061_QD__main__3$', duration=4800, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 랜듀비앙대사_01(self.ctx)


class 랜듀비앙대사_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=5000.0)
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=11001567, illust_id='Renduebian_normal', msg='$52010061_QD__main__4$', duration=4800, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 랜듀비앙대사_02(self.ctx)


class 랜듀비앙대사_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=11001567, illust_id='Renduebian_normal', msg='$52010061_QD__main__5$', duration=3800, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 유페리아대사_02(self.ctx)


class 유페리아대사_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=11003844, illust_id='Yuperia_normal', msg='$52010061_QD__main__6$', duration=3800, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 랜듀비앙대사_03(self.ctx)


class 랜듀비앙대사_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.add_cinematic_talk(npc_id=11001567, illust_id='Renduebian_normal', msg='$52010061_QD__main__7$', duration=3800, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 이슈라등장(self.ctx)


class 이슈라등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이슈라등장_02(self.ctx)


class 이슈라등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11001975, msg='$52010061_QD__main__8$', duration=4000)
        self.spawn_monster(spawn_ids=[104], auto_target=False) # 이슈라

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 이슈라등장_03(self.ctx)


class 이슈라등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4006,4007], return_view=False)
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 이슈라대사(self.ctx)


class 이슈라대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=11003845, illust_id='Ishura_normal', msg='$52010061_QD__main__9$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이슈라모션(self.ctx)


class 이슈라모션(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='RuneBlader_Bore_A') # 이 후 새로운 모션으로 수정

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=State)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료_02(self.ctx)


class 종료_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=300, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return UI초기화(self.ctx)


class UI초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])
        self.reset_camera(interpolation_time=2.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 맵이동(self.ctx)


class 맵이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000422) # 스카이 포트리스 함교로 텔레포트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return State(self.ctx)


class State(trigger_api.Trigger):
    pass


initial_state = 입장
