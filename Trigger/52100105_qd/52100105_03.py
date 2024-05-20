""" trigger/52100105_qd/52100105_03.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[601])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1000]):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50101030], quest_states=[3]):
            return 시작암전1(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50101030], quest_states=[2]):
            return 연출끝(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50101030], quest_states=[1]):
            return 연출끝(self.ctx)


class 시작암전1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])
        self.set_effect(trigger_ids=[601])
        self.visible_my_pc(is_visible=False)
        self.set_onetime_effect(id=200, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 컷신1_1(self.ctx)


class 컷신1_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Kritias_EpicCutScene07_01.swf')

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 0:
            return None # Missing State: 컷신1_2
        if self.wait_tick(wait_tick=3000):
            return 몹소환1(self.ctx)


class 몹소환1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[500], auto_target=False) # 클라디아
        self.spawn_monster(spawn_ids=[1], auto_target=False) # 의자
        self.spawn_monster(spawn_ids=[400], auto_target=False)
        self.spawn_monster(spawn_ids=[401], auto_target=False)
        self.spawn_monster(spawn_ids=[402], auto_target=False)
        self.spawn_monster(spawn_ids=[403], auto_target=False)
        self.spawn_monster(spawn_ids=[404], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 인게임준비0(self.ctx)


class 인게임준비0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=200, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카대사1(self.ctx)


class 투르카대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[500], arg2=False)
        self.set_scene_skip(state=컷신3_1, action='nextState')
        self.select_camera_path(path_ids=[700,701], return_view=False)
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_normal', msg='$52100105_QD__52100105_03__0$', duration=6000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_normal', msg='$52100105_QD__52100105_03__1$', duration=6000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 클라디아생성1(self.ctx)


class 클라디아생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[500], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 클라디아이동1(self.ctx)


class 클라디아이동1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=500, patrol_name='PatrolData_500_1')
        self.select_camera_path(path_ids=[703,704], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 클라디아대사1(self.ctx)


class 클라디아대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=500, sequence_name='Talk_A', duration=8666.0)
        self.add_cinematic_talk(npc_id=11004392, illust_id='cladia_normal', msg='$52100105_QD__52100105_03__2$', duration=5000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11004392, illust_id='cladia_angry', msg='$52100105_QD__52100105_03__3$', duration=5000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카공격지시1(self.ctx)


class 투르카공격지시1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=705)
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_normal', msg='$52100105_QD__52100105_03__4$', duration=3000, align=Align.Right)
        self.set_npc_emotion_loop(spawn_id=400, sequence_name='Bore_A', duration=1333.0)
        self.set_npc_emotion_loop(spawn_id=500, sequence_name='Attack_Idle_A', duration=5333.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 암전1(self.ctx)


class 암전1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.move_npc(spawn_id=401, patrol_name='PatrolData_401_1')
        self.move_npc(spawn_id=402, patrol_name='PatrolData_402_1')
        self.move_npc(spawn_id=403, patrol_name='PatrolData_403_1')
        self.move_npc(spawn_id=404, patrol_name='PatrolData_404_1')
        self.set_onetime_effect(id=100, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 컷신3_1(self.ctx)


class 컷신3_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[401], arg2=False)
        self.destroy_monster(spawn_ids=[402], arg2=False)
        self.destroy_monster(spawn_ids=[403], arg2=False)
        self.destroy_monster(spawn_ids=[404], arg2=False)
        self.destroy_monster(spawn_ids=[500], arg2=False)
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='Kritias_EpicCutScene07_02.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 클라디아생성2(self.ctx)
        if self.wait_tick(wait_tick=12000):
            return 클라디아생성2(self.ctx)


class 클라디아생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[500], auto_target=False)
        self.move_npc(spawn_id=500, patrol_name='PatrolData_500_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카도망1(self.ctx)


class 투르카도망1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=연출끝, action='nextState')
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=100, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawn_id=500, sequence_name='Attack_Idle_A', duration=5333.0)
        self.set_npc_emotion_loop(spawn_id=400, sequence_name='Damg_A', duration=5333.0)
        self.select_camera(trigger_id=706)
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_Broken_Hood', msg='$52100105_QD__52100105_03__5$', duration=4000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카도망2(self.ctx)


class 투르카도망2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카도망3(self.ctx)


class 투르카도망3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=400, patrol_name='PatrolData_400_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 투르카도망4(self.ctx)


class 투르카도망4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=707)
        self.destroy_monster(spawn_ids=[500], arg2=False)
        self.add_cinematic_talk(npc_id=11004430, illust_id='Turka_Broken_Hood', msg='$52100105_QD__52100105_03__6$', duration=5000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 투르카도망5(self.ctx)


class 투르카도망5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[-1], arg2=False)
        self.set_effect(trigger_ids=[600])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.visible_my_pc(is_visible=True)
        self.set_onetime_effect(id=101, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52100110, portal_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: State


initial_state = Ready
