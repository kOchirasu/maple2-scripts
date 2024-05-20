""" trigger/52100060_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class QuestDungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8100, enable=True) # LocalTargetCamera

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50100320], quest_states=[3]): # >
            return teleport02000487(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50100320], quest_states=[2]):
            return Ready(self.ctx)
        if self.quest_user_detected(box_ids=[1000], quest_ids=[50100320], quest_states=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=1)
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[600])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1000]):
            return narration01(self.ctx)


class narration01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$52100060_QD__MAIN__12$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Camera_Move_01(self.ctx)


class Camera_Move_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NPC_Show(self.ctx)


class NPC_Show(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=teleport02000487)
        self.spawn_monster(spawn_ids=[1,2], auto_target=False)
        self.set_npc_rotation(spawn_id=1, rotation=180.0)
        self.set_npc_rotation(spawn_id=2, rotation=180.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NPC_Change_1(self.ctx)


class NPC_Change_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1,2], arg2=False)
        self.spawn_monster(spawn_ids=[101,102], auto_target=False)
        self.select_camera_path(path_ids=[2,3])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Talk_1(self.ctx)


class Talk_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])
        self.select_camera(trigger_id=4)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Attack_01_A')
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52100060_QD__MAIN__0$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Talk_2(self.ctx)


class Talk_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=5)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11001813, illust_id='11001813', msg='$52100060_QD__MAIN__1$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11001813, illust_id='11001813', msg='$52100060_QD__MAIN__2$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Talk_3(self.ctx)


class Talk_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[10,11,12], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11001813, illust_id='11001813', msg='$52100060_QD__MAIN__3$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Talk_4(self.ctx)


class Talk_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4)
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52100060_QD__MAIN__4$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Talk_5(self.ctx)


class Talk_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[6,7], return_view=False)
        self.add_cinematic_talk(npc_id=11001813, illust_id='11001813', msg='$52100060_QD__MAIN__5$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Talk_6(self.ctx)


class Talk_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[77,78], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52100060_QD__MAIN__6$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Talk_7(self.ctx)


class Talk_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004022, illust_id='11004022', msg='$52100060_QD__MAIN__7$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Talk_8(self.ctx)


class Talk_8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=44)
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[200])
        self.add_cinematic_talk(npc_id=11001813, illust_id='11001813', msg='$52100060_QD__MAIN__8$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Talk_9(self.ctx)


class Talk_9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[13,14,15], return_view=False)
        self.set_effect(trigger_ids=[600])
        self.add_cinematic_talk(npc_id=11001813, illust_id='11001813', msg='$52100060_QD__MAIN__9$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Talk_10(self.ctx)


class Talk_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=200, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11001593, illust_id='11001593', msg='$52100060_QD__MAIN__10$', duration=4000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Talk_11(self.ctx)


class Talk_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=16)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11001813, illust_id='11001813', msg='$52100060_QD__MAIN__11$', duration=2000, align=Align.Right)
        self.select_camera(trigger_id=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NPC_Attack_Move(self.ctx)


class NPC_Attack_Move(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=0.5, end_scale=0.3, duration=3.0, interpolator=1)
        self.select_camera_path(path_ids=[8,9], return_view=False)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData3')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return teleport02000487(self.ctx)


class teleport02000487(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[-1])
        self.visible_my_pc(is_visible=True)
        # 프론티어 재단 저택 맵 3번 회의실 앞 포탈
        self.move_user(map_id=2000487, portal_id=3)


initial_state = QuestDungeonStart
