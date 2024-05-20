""" trigger/52000192_qd/52000192.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class wait_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(trigger_ids=[6001])
        self.set_effect(trigger_ids=[6002])
        self.set_effect(trigger_ids=[6003])
        self.set_effect(trigger_ids=[6004])
        self.set_interact_object(trigger_ids=[10001453], state=2)
        self.set_interact_object(trigger_ids=[10001454], state=2)
        self.set_interact_object(trigger_ids=[10001455], state=2)
        self.set_interact_object(trigger_ids=[10001456], state=2)
        self.set_portal(portal_id=5003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003423], quest_states=[1]):
            # 비밀 통로를 따라 퀘스트 수락
            return wait_01_02(self.ctx)
        if not self.quest_user_detected(box_ids=[2001], quest_ids=[10003423], quest_states=[1]):
            # 비밀 통로를 따라 퀘스트 수락 유저가 아니면
            return 이동(self.ctx)


class wait_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return wait_01_03(self.ctx)


class wait_01_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000192, portal_id=5001)
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.spawn_monster(spawn_ids=[101]) # 바론
        self.spawn_monster(spawn_ids=[102]) # 여제

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 불난통로_01(self.ctx)


class 불난통로_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 불난통로_02(self.ctx)


class 불난통로_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000192_QD__52000192__0$', align=Align.Left, illust_id='Ereb_surprise', duration=4000)
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=5000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 불난통로_03(self.ctx)


class 불난통로_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52000192_QD__52000192__1$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 불난통로_04(self.ctx)


class 불난통로_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000192_QD__52000192__2$', duration=5000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000192_QD__52000192__3$', align=Align.Left, illust_id='Baron_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 불끄기준비(self.ctx)


class 불끄기준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 불끄기준비_02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 불끄기준비_02(self.ctx)


class 불끄기준비_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103]) # 바론
        self.spawn_monster(spawn_ids=[104]) # 여제
        self.set_effect(trigger_ids=[6001], visible=True) # 여제 지킴
        self.set_interact_object(trigger_ids=[10001453], state=1)
        self.move_user(map_id=52000192, portal_id=5002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 불꺼라불꺼(self.ctx)


class 불꺼라불꺼(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.side_npc_talk(npc_id=11004787, illust='Baron_normal', script='$52000192_QD__52000192__4$', duration=3000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001453], state=0):
            return 불꺼라불꺼_02(self.ctx)


class 불꺼라불꺼_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.add_balloon_talk(spawn_id=104, msg='$52000192_QD__52000192__5$', duration=4000)
        self.set_effect(trigger_ids=[6021]) # 불끄기
        self.set_effect(trigger_ids=[6005], visible=True)
        self.set_effect(trigger_ids=[6006], visible=True)
        self.set_effect(trigger_ids=[6007], visible=True)
        self.set_effect(trigger_ids=[6008], visible=True)
        self.spawn_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[204])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 불꺼라불꺼_02_02(self.ctx)


class 불꺼라불꺼_02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000192_QD__52000192__6$', illust_id='Baron_normal', align=Align.Left, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 불꺼라불꺼_02_01(self.ctx)


class 불꺼라불꺼_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204]):
            return 불꺼라불꺼_03(self.ctx)


class 불꺼라불꺼_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=104, msg='$52000192_QD__52000192__7$', duration=4000)
        self.set_effect(trigger_ids=[6001])
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_3001')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 불꺼라불꺼_04(self.ctx)


class 불꺼라불꺼_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6002], visible=True) # 여제 지킴
        self.set_interact_object(trigger_ids=[10001454], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001454], state=0):
            return 불꺼라불꺼_05(self.ctx)


class 불꺼라불꺼_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=104, msg='$52000192_QD__52000192__8$', duration=4000)
        self.set_effect(trigger_ids=[6022]) # 불끄기
        self.set_effect(trigger_ids=[6009], visible=True)
        self.set_effect(trigger_ids=[6010], visible=True)
        self.set_effect(trigger_ids=[6011], visible=True)
        self.set_effect(trigger_ids=[6012], visible=True)
        self.spawn_monster(spawn_ids=[205])
        self.spawn_monster(spawn_ids=[206])
        self.spawn_monster(spawn_ids=[207])
        self.spawn_monster(spawn_ids=[208])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[205,206,207,208]):
            return 불꺼라불꺼_06(self.ctx)


class 불꺼라불꺼_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=104, msg='$52000192_QD__52000192__9$', duration=4000)
        self.set_effect(trigger_ids=[6002])
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_3003')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_3004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 불꺼라불꺼_07(self.ctx)


class 불꺼라불꺼_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003], visible=True) # 여제 지킴
        self.set_interact_object(trigger_ids=[10001455], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001455], state=0):
            return 불꺼라불꺼_08(self.ctx)


class 불꺼라불꺼_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=104, msg='$52000192_QD__52000192__10$', duration=4000)
        self.set_effect(trigger_ids=[6023]) # 불끄기
        self.set_effect(trigger_ids=[6013], visible=True)
        self.set_effect(trigger_ids=[6014], visible=True)
        self.set_effect(trigger_ids=[6015], visible=True)
        self.set_effect(trigger_ids=[6016], visible=True)
        self.spawn_monster(spawn_ids=[209])
        self.spawn_monster(spawn_ids=[210])
        self.spawn_monster(spawn_ids=[211])
        self.spawn_monster(spawn_ids=[212])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[209,210,211,212]):
            return 불꺼라불꺼_09(self.ctx)


class 불꺼라불꺼_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6003])
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_3005')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_3006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 불꺼라불꺼_10(self.ctx)


class 불꺼라불꺼_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6004], visible=True) # 여제 지킴
        self.set_interact_object(trigger_ids=[10001456], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001456], state=0):
            return 불꺼라불꺼_11(self.ctx)


class 불꺼라불꺼_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004787, illust='Baron_normal', script='$52000192_QD__52000192__11$', duration=3000)
        self.set_effect(trigger_ids=[6024]) # 불끄기
        self.set_effect(trigger_ids=[6017], visible=True)
        self.set_effect(trigger_ids=[6018], visible=True)
        self.set_effect(trigger_ids=[6019], visible=True)
        self.set_effect(trigger_ids=[6020], visible=True)
        self.spawn_monster(spawn_ids=[213])
        self.spawn_monster(spawn_ids=[214])
        self.spawn_monster(spawn_ids=[215])
        self.spawn_monster(spawn_ids=[216])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[213,214,215,216]):
            return 불꺼라불꺼_12(self.ctx)


class 불꺼라불꺼_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=104, msg='$52000192_QD__52000192__12$', duration=3000)
        self.set_effect(trigger_ids=[6004])
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_3007')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_3008')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 다왔다(self.ctx)


class 다왔다(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=6000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000192_QD__52000192__13$', duration=3000)
        self.add_cinematic_talk(npc_id=11004785, msg='$52000192_QD__52000192__14$', illust_id='Ereb_surprise', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 밖으로(self.ctx)


class 밖으로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=2001, achieve='EscapePrisonTower')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portal_id=5003, visible=True, enable=True)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000119, portal_id=20)


initial_state = wait_01
