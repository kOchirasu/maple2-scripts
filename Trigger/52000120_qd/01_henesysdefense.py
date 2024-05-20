""" trigger/52000120_qd/01_henesysdefense.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.destroy_monster(spawn_ids=[101,102,201,202,203,204,290,210,211,212,213,214,215,220,221,222,223,224,225,240,241,242,243,244,245]) # NPC
        self.destroy_monster(spawn_ids=[300,301,302,303,304,305,306,307,308,309,310,401,402,403,404,405,406,407,408,409,410,500,501,502,503,504,505,506,507,508,509,510,601,602,603,604]) # Archer
        self.destroy_monster(spawn_ids=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,921,922,923,924,925,926,927,928]) # Battle_Mob
        self.destroy_monster(spawn_ids=[605,606,607,608,801,802,803,804,805,806,807,808,809,810,811,812,813,814]) # Actor
        self.destroy_monster(spawn_ids=[701,702,703,704]) # Cannon
        self.destroy_monster(spawn_ids=[710,711,712,713]) # CannonForPC
        self.spawn_monster(spawn_ids=[110,111,112,120,121,122,123,124,125,126,130,131,132,133,134,135,136,140,141,142,143,144,145,146,147,150,151,152,153,154,155,156,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,185,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,113,114,115,116,117,118], auto_target=False) # MobActor
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105], visible=True) # GratingDown
        # self.set_mesh(trigger_ids=[3110,3111,3112]) # GratingUp 사용 안함
        self.set_mesh(trigger_ids=[3000], visible=True) # BridgeMesh_forTOK
        self.set_mesh(trigger_ids=[3001], visible=True) # BridgeBarrier_Invisible
        self.set_actor(trigger_id=4500, visible=True, initial_sequence='Interaction_bridge_A01_on') # Bridge
        self.set_breakable(trigger_ids=[4000,4001,4002,4003,4004,4005])
        self.set_visible_breakable_object(trigger_ids=[4000,4001,4002,4003,4004,4005])
        self.set_cube(trigger_ids=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010]) # LiftUp_Bomb
        self.set_local_camera(camera_id=10000)
        self.set_local_camera(camera_id=10001)
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])
        self.set_effect(trigger_ids=[5000]) # DarkCloud
        self.set_effect(trigger_ids=[5001]) # DarkCloud

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[1]):
            return LoadingDelay01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001551], quest_states=[2]):
            # 맵 튕기고 완료가능 상태일 때 대비 위한 스테이트
            return Quit(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.spawn_monster(spawn_ids=[605,606,607,608], auto_target=False) # Actor_Training
        self.spawn_monster(spawn_ids=[801,802,803,804,805,806], auto_target=False) # Actor_Patrol
        self.spawn_monster(spawn_ids=[807,808,809,810,811,812,813,814], auto_target=False) # Actor_Standing
        self.spawn_monster(spawn_ids=[101,201], auto_target=False) # Actor_Unique
        self.spawn_monster(spawn_ids=[501,502,507,508], auto_target=False) # Archer_3rd
        self.spawn_monster(spawn_ids=[401,402,403,404,405,406,407,408,409,410], auto_target=False) # Archer_2nd
        self.spawn_monster(spawn_ids=[710,711,712,713], auto_target=False) # CannonForPC
        self.select_camera(trigger_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            # LoadingDelay02
            # 테스트용 임시
            return LoadingDelay02(self.ctx) # CameraChange12


class LoadingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LeadersTalk_Manovich01(self.ctx)


class LeadersTalk_Manovich01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__0$', duration=5000, align=Align.Center, illust_id='Manovich_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        # 씬스킵으로 바로 전투 시작
        # self.set_scene_skip(state=OskhalTalk04Skip, action='exit')
        self.set_scene_skip(state=SetLocalTargetCamera01cskip, action='nextState')
        # self.set_skip(state=LeadersTalk_Manovich01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return LeadersTalk_Manovich01Skip(self.ctx)


class LeadersTalk_Manovich01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return LeadersTalk_Osckal01(self.ctx)


class LeadersTalk_Osckal01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1000')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__1$', duration=4000, align=Align.Center, illust_id='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return LeadersTalk_Osckal01Skip(self.ctx)


class LeadersTalk_Osckal01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.select_camera(trigger_id=11)
        self.add_balloon_talk(msg='$52000120_QD__01_HENESYSDEFENSE__2$', duration=2000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return LeadersLookAtPC01(self.ctx)


class LeadersLookAtPC01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return LeadersLookAtPC02(self.ctx)


class LeadersLookAtPC02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraChange01(self.ctx)


class CameraChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraChange02(self.ctx)


class CameraChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=12) # PC 등뒤에서

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraChange03(self.ctx)


class CameraChange03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return PCTalk01(self.ctx)


class PCTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='$52000120_QD__01_HENESYSDEFENSE__3$', duration=4000, align=Align.Center, illust_id='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PCTalk01Skip(self.ctx)


class PCTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return ManovichTalk01(self.ctx)


class ManovichTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Talk_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__4$', duration=5000, align=Align.Center, illust_id='Manovich_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ManovichTalk01Skip(self.ctx)


class ManovichTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Idle_A')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCTalk02(self.ctx)


class PCTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000120_QD__01_HENESYSDEFENSE__5$', duration=4000, align=Align.Center, illust_id='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PCTalk02Skip(self.ctx)


class PCTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Idle_A'])
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return ManovichTalk02(self.ctx)


class ManovichTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__6$', duration=4000, align=Align.Center, illust_id='Manovich_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ManovichTalk02Skip(self.ctx)


class ManovichTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return OskhalTalk02(self.ctx)


class OskhalTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Talk_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__7$', duration=5000, align=Align.Center, illust_id='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return OskhalTalk02Skip(self.ctx)


class OskhalTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Idle_A')
        self.remove_cinematic_talk()
        self.set_effect(trigger_ids=[5000], visible=True) # DarkCloud
        self.set_effect(trigger_ids=[5001], visible=True) # DarkCloud

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraChange05(self.ctx)


class CameraChange05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=13) # PC 등뒤에서

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraChange06(self.ctx)


class CameraChange06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=14) # PC 등뒤에서

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return OskhalTalk03(self.ctx)


class OskhalTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__8$', duration=4000, align=Align.Center, illust_id='Oskhal_serious')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return OskhalTalk03Skip(self.ctx)


class OskhalTalk03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return OskhalTalk04(self.ctx)


class OskhalTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__9$', duration=5000, align=Align.Center, illust_id='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return OskhalTalk04Skip(self.ctx)


class OskhalTalk04Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return CameraChange11(self.ctx)


class CameraChange11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraChange12(self.ctx)


class CameraChange12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.move_user(map_id=52000120, portal_id=10, box_id=9900)
        self.select_camera(trigger_id=15)
        self.destroy_monster(spawn_ids=[101,201]) # Actor_Unique
        self.spawn_monster(spawn_ids=[102,202,210,211,212,213,214,215], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraChange13(self.ctx)


class CameraChange13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105], start_delay=500, fade=2.0) # GratingDown
        self.set_breakable(trigger_ids=[4000,4001,4002,4003,4004,4005], enable=True)
        self.set_visible_breakable_object(trigger_ids=[4000,4001,4002,4003,4004,4005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraChange14(self.ctx)


class CameraChange14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4500, visible=True, initial_sequence='Interaction_bridge_A01_off') # Bridge
        self.select_camera(trigger_id=16)
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_102')
        self.move_npc(spawn_id=210, patrol_name='MS2PatrolData_210')
        self.move_npc(spawn_id=211, patrol_name='MS2PatrolData_211')
        self.move_npc(spawn_id=212, patrol_name='MS2PatrolData_212')
        self.move_npc(spawn_id=213, patrol_name='MS2PatrolData_213')
        self.move_npc(spawn_id=214, patrol_name='MS2PatrolData_214')
        self.move_npc(spawn_id=215, patrol_name='MS2PatrolData_215')
        self.set_user_value(trigger_id=10, key='DefencePhase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraChange15(self.ctx)


class CameraChange15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return SetLocalTargetCamera01(self.ctx)


class SetLocalTargetCamera01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000,4001,4002,4003,4004,4005])
        self.set_visible_breakable_object(trigger_ids=[4000,4001,4002,4003,4004,4005])
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105], visible=True, start_delay=500, fade=2.0) # GratingDown
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SetLocalTargetCamera02(self.ctx)


class SetLocalTargetCamera01cskip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=10, key='DefencePhase', value=1)
        self.move_user(map_id=52000120, portal_id=10, box_id=9900)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_breakable(trigger_ids=[4000,4001,4002,4003,4004,4005])
        self.set_visible_breakable_object(trigger_ids=[4000,4001,4002,4003,4004,4005])
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105], visible=True, start_delay=500, fade=2.0) # GratingDown
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SetLocalTargetCamera02(self.ctx)


class SetLocalTargetCamera02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return SetLocalTargetCamera03(self.ctx)


class SetLocalTargetCamera03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=10000, enable=True)
        self.set_cube(trigger_ids=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010], is_visible=True) # LiftUp_Bomb

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SetLocalTargetCamera04(self.ctx)


class SetLocalTargetCamera04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.spawn_monster(spawn_ids=[901,902], auto_target=False) # Battle_Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BattleOnTheWallGuide01(self.ctx)


class BattleOnTheWallGuide01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202,210,211,212,213,214,215])
        self.spawn_monster(spawn_ids=[203,220,221,222,223,224,225], auto_target=False)
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__10$', duration=5000, align=Align.Center, illust_id='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        self.set_scene_skip(state=BattleOnTheWallGuide01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return BattleOnTheWallGuide01Skip(self.ctx)


class BattleOnTheWallGuide01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return BattleOnTheWallGuide02(self.ctx)


class BattleOnTheWallGuide02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_effect(trigger_ids=[5000]) # DarkCloud
        self.set_effect(trigger_ids=[5001]) # DarkCloud
        self.spawn_monster(spawn_ids=[903,904], auto_target=False) # Battle_Mob
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__11$', duration=4000, align=Align.Center, illust_id='Manovich_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        self.set_scene_skip(state=BattleOnTheWallGuide02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return BattleOnTheWallGuide02Skip(self.ctx)


class BattleOnTheWallGuide02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BattleOnTheWallGuide03(self.ctx)


class BattleOnTheWallGuide03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=25101201, text_id=25101201) # 가이드 : 자경단의 전투를 지원해주세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return BattleOnTheWallEnd01(self.ctx)


class BattleOnTheWallEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25101201)
        self.set_user_value(trigger_id=4, key='NpcDown', value=1)
        self.set_user_value(trigger_id=5, key='NpcDown', value=1)
        self.set_user_value(trigger_id=6, key='NpcDown', value=1)
        self.set_user_value(trigger_id=7, key='NpcDown', value=1)
        self.set_user_value(trigger_id=8, key='NpcDown', value=1)
        self.set_user_value(trigger_id=9, key='NpcDown', value=1)
        self.spawn_monster(spawn_ids=[905,906], auto_target=False) # Battle_Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return BattleOnTheWallEnd02(self.ctx)


class BattleOnTheWallEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[907,908], auto_target=False) # Battle_Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return BattleOnTheWallEnd03(self.ctx)


class BattleOnTheWallEnd03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[909,910], auto_target=False) # Battle_Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return CallingBackUp01(self.ctx)


class CallingBackUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__12$', duration=5000, align=Align.Center, illust_id='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        # 씬스킵으로 바로 전투 시작
        self.set_scene_skip(state=PCVolunteer05CSkip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return CallingBackUp01Skip(self.ctx)


class CallingBackUp01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCVolunteer01(self.ctx)


class PCVolunteer01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_local_camera(camera_id=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCVolunteer02(self.ctx)


class PCVolunteer02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000120, portal_id=20, box_id=9900)
        self.select_camera(trigger_id=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PCVolunteer03(self.ctx)


class PCVolunteer03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return PCVolunteer04(self.ctx)


class PCVolunteer04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return PCVolunteer05(self.ctx)


class PCVolunteer05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000120_QD__01_HENESYSDEFENSE__13$', duration=4000, align=Align.Center, illust_id='0')
        # self.set_scene_skip(state=Battle01End01Skip, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return PCVolunteer05Skip(self.ctx)


class PCVolunteer05Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Idle_A'])
        self.remove_cinematic_talk()
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return Battle01Start01(self.ctx)


class PCVolunteer05CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000120, portal_id=20, box_id=9900)
        self.set_user_value(trigger_id=10, key='DefencePhase', value=2)
        self.set_pc_emotion_sequence(sequence_names=['Idle_A'])
        self.remove_cinematic_talk()
        self.destroy_monster(spawn_ids=[901,902,903,904,905,906,907,908,909,910]) # Battle01_Mob
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        return Battle01Start01(self.ctx)


class Battle01Start01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_actor(trigger_id=4500, visible=True, initial_sequence='Interaction_bridge_A01_on') # Bridge

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Battle01Start02(self.ctx)


class Battle01Start02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(trigger_ids=[6000,6001,6002,6003,6004,6005,6006,6007,6008,6009,6010]) # LiftUp_Bomb
        self.destroy_monster(spawn_ids=[701,702,703,704]) # Cannon
        self.destroy_monster(spawn_ids=[710,711,712,713]) # CannonForPC
        self.spawn_monster(spawn_ids=[300,301,302,303,304,305,306,307,308,309,310], auto_target=False) # Archer_1st
        self.spawn_monster(spawn_ids=[500,503,504,505,506,509,510], auto_target=False) # Archer_4rd
        self.spawn_monster(spawn_ids=[601,602,603,604], auto_target=False) # Actor_Artillery
        self.spawn_monster(spawn_ids=[701,702,703,704], auto_target=False) # Cannon
        self.move_user(map_id=52000120, portal_id=30, box_id=9900)
        self.spawn_monster(spawn_ids=[240,241,242,243,244,245], auto_target=False)
        self.select_camera(trigger_id=30)
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Battle01Start03(self.ctx)


class Battle01Start03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_mesh(trigger_ids=[3001]) # BridgeBarrier_Invisible
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105], start_delay=500, fade=2.0) # GratingDown
        self.set_breakable(trigger_ids=[4000,4001,4002,4003,4004,4005], enable=True)
        self.set_visible_breakable_object(trigger_ids=[4000,4001,4002,4003,4004,4005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Battle01Start04(self.ctx)


class Battle01Start04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4500, visible=True, initial_sequence='Interaction_bridge_A01_off') # Bridge
        self.move_user_path(patrol_name='MS2PatrolData_1002')
        self.move_npc(spawn_id=240, patrol_name='MS2PatrolData_240')
        self.move_npc(spawn_id=241, patrol_name='MS2PatrolData_241')
        self.move_npc(spawn_id=242, patrol_name='MS2PatrolData_242')
        self.move_npc(spawn_id=243, patrol_name='MS2PatrolData_243')
        self.move_npc(spawn_id=244, patrol_name='MS2PatrolData_244')
        self.move_npc(spawn_id=245, patrol_name='MS2PatrolData_245')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Battle01Start05(self.ctx)


class Battle01Start05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=31)
        self.set_user_value(trigger_id=10, key='DefencePhase', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Battle01Start06(self.ctx)


class Battle01Start06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000,4001,4002,4003,4004,4005])
        self.set_visible_breakable_object(trigger_ids=[4000,4001,4002,4003,4004,4005])
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105], visible=True, start_delay=500, fade=2.0) # GratingDown
        self.set_actor(trigger_id=4500, visible=True, initial_sequence='Interaction_bridge_A01_on') # Bridge
        self.set_mesh(trigger_ids=[3001], visible=True) # BridgeBarrier_Invisible

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Battle01Start07(self.ctx)


class Battle01Start07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.change_monster(from_spawn_id=203, to_spawn_id=204)
        self.change_monster(from_spawn_id=240, to_spawn_id=250)
        self.change_monster(from_spawn_id=241, to_spawn_id=251)
        self.change_monster(from_spawn_id=242, to_spawn_id=252)
        self.change_monster(from_spawn_id=243, to_spawn_id=253)
        self.change_monster(from_spawn_id=244, to_spawn_id=254)
        self.change_monster(from_spawn_id=245, to_spawn_id=255)
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=25101202, text_id=25101202) # 가이드 : 남아있는 적군을 소탕하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[901,902,903,904,905,906,907,908,909,910]):
            return Battle01End01(self.ctx)


class Battle01End01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=25101202)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__14$', duration=5000, align=Align.Center, illust_id='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        self.set_scene_skip(state=Battle01End01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Battle01End01Skip(self.ctx)


class Battle01End01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()
        self.destroy_monster(spawn_ids=[901,902,903,904,905,906,907,908,909,910]) # Battle01_Mob
        self.move_npc(spawn_id=230, patrol_name='MS2PatrolData_230')
        self.move_npc(spawn_id=231, patrol_name='MS2PatrolData_231')
        self.move_npc(spawn_id=232, patrol_name='MS2PatrolData_232')
        self.move_npc(spawn_id=233, patrol_name='MS2PatrolData_233')
        self.move_npc(spawn_id=234, patrol_name='MS2PatrolData_234')
        self.move_npc(spawn_id=235, patrol_name='MS2PatrolData_235')
        self.move_npc(spawn_id=250, patrol_name='MS2PatrolData_250')
        self.move_npc(spawn_id=251, patrol_name='MS2PatrolData_251')
        self.move_npc(spawn_id=252, patrol_name='MS2PatrolData_252')
        self.move_npc(spawn_id=253, patrol_name='MS2PatrolData_253')
        self.move_npc(spawn_id=254, patrol_name='MS2PatrolData_254')
        self.move_npc(spawn_id=255, patrol_name='MS2PatrolData_255')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Battle01End02(self.ctx)


class Battle01End02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        # 가이드 : 서둘러 부상당한 자경단원들을 치료해주세요!
        self.show_guide_summary(entity_id=25101203, text_id=25101203, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Battle02Start01(self.ctx)


class Battle02Start01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[911,912], auto_target=False) # Battle02Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Battle02Start02(self.ctx)


class Battle02Start02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[102], sound='System_ShowGuideSummary_01')
        # 가이드 : 자경단원들과 함께 적군을 모두 물리치세요!
        self.show_guide_summary(entity_id=25101204, text_id=25101204, duration=5000)
        self.spawn_monster(spawn_ids=[913,914], auto_target=False) # Battle02Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[911,912,913,914]):
            return Battle02End01(self.ctx)


class Battle02End01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003319, msg='$52000120_QD__01_HENESYSDEFENSE__15$', duration=5000, align=Align.Center, illust_id='Oskhal_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        self.set_scene_skip(state=Battle02End01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Battle02End01Skip(self.ctx)


class Battle02End01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()
        self.destroy_monster(spawn_ids=[911,912,913,914]) # Battle02_Mob
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_203')
        self.move_npc(spawn_id=250, patrol_name='MS2PatrolData_250')
        self.move_npc(spawn_id=251, patrol_name='MS2PatrolData_251')
        self.move_npc(spawn_id=252, patrol_name='MS2PatrolData_252')
        self.move_npc(spawn_id=253, patrol_name='MS2PatrolData_253')
        self.move_npc(spawn_id=254, patrol_name='MS2PatrolData_254')
        self.move_npc(spawn_id=255, patrol_name='MS2PatrolData_255')
        self.move_npc(spawn_id=230, patrol_name='MS2PatrolData_230')
        self.move_npc(spawn_id=231, patrol_name='MS2PatrolData_231')
        self.move_npc(spawn_id=232, patrol_name='MS2PatrolData_232')
        self.move_npc(spawn_id=233, patrol_name='MS2PatrolData_233')
        self.move_npc(spawn_id=234, patrol_name='MS2PatrolData_234')
        self.move_npc(spawn_id=235, patrol_name='MS2PatrolData_235')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Battle03Start01(self.ctx)


class Battle03Start01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[921,922], auto_target=False) # Battle03Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Battle03Start02(self.ctx)


class Battle03Start02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[923,924], auto_target=False) # Battle03Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return Battle03Start03(self.ctx)


class Battle03Start03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[925,926], auto_target=False) # Battle03Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Battle03Start04(self.ctx)


class Battle03Start04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[927,928], auto_target=False) # Battle03Wave

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[921,922,923,924,925,926,927,928]):
            return Battle03End01(self.ctx)


class Battle03End01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[290], auto_target=False) # Turka
        self.destroy_monster(spawn_ids=[921,922,923,924,925,926,927,928]) # Battle03_Mob
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=40)
        self.move_user_path(patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return TurkaWalkIn01(self.ctx)


class TurkaWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=230, patrol_name='MS2PatrolData_230')
        self.move_npc(spawn_id=231, patrol_name='MS2PatrolData_231')
        self.move_npc(spawn_id=232, patrol_name='MS2PatrolData_232')
        self.move_npc(spawn_id=233, patrol_name='MS2PatrolData_233')
        self.move_npc(spawn_id=234, patrol_name='MS2PatrolData_234')
        self.move_npc(spawn_id=235, patrol_name='MS2PatrolData_235')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_203')
        self.move_npc(spawn_id=250, patrol_name='MS2PatrolData_250')
        self.move_npc(spawn_id=251, patrol_name='MS2PatrolData_251')
        self.move_npc(spawn_id=252, patrol_name='MS2PatrolData_252')
        self.move_npc(spawn_id=253, patrol_name='MS2PatrolData_253')
        self.move_npc(spawn_id=254, patrol_name='MS2PatrolData_254')
        self.move_npc(spawn_id=255, patrol_name='MS2PatrolData_255')
        self.set_user_value(trigger_id=4, key='BattleEnd', value=1)
        self.set_user_value(trigger_id=5, key='BattleEnd', value=1)
        self.set_user_value(trigger_id=6, key='BattleEnd', value=1)
        self.set_user_value(trigger_id=7, key='BattleEnd', value=1)
        self.set_user_value(trigger_id=8, key='BattleEnd', value=1)
        self.set_user_value(trigger_id=9, key='BattleEnd', value=1)
        self.move_npc(spawn_id=290, patrol_name='MS2PatrolData_301')
        self.destroy_monster(spawn_ids=[204])
        self.spawn_monster(spawn_ids=[205])
        self.move_user_path(patrol_name='MS2PatrolData_1004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return TurkaWalkIn02(self.ctx)


class TurkaWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_205')
        self.move_user_path(patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return TurkaTalk01(self.ctx)


class TurkaTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[5000], visible=True) # DarkCloud
        self.set_effect(trigger_ids=[5001], visible=True) # DarkCloud
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003226, msg='$52000120_QD__01_HENESYSDEFENSE__16$', duration=5000, align=Align.Center, illust_id='0')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입
        self.set_scene_skip(state=ManovichTalk03_CSkip, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return TurkaTalk01Skip(self.ctx)


class TurkaTalk01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return ChangeView01(self.ctx)


class ChangeView01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ChangeView02(self.ctx)


class ChangeView02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=42)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ChangeView03(self.ctx)


class ChangeView03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return TurkaTalk02(self.ctx)


class TurkaTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003226, msg='$52000120_QD__01_HENESYSDEFENSE__17$', duration=4000, align=Align.Center, illust_id='Turka_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return TurkaTalk02Skip(self.ctx)


class TurkaTalk02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.move_npc(spawn_id=290, patrol_name='MS2PatrolData_302')
        self.destroy_monster(spawn_ids=[980,981,982,983,984,985,990,991,992,993,994,995])
        self.spawn_monster(spawn_ids=[960,961,962,963,964,965,970,971,972,973,974,975], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EnemyRetreat01(self.ctx)


class EnemyRetreat01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=43) # 퇴각 연출

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EnemyRetreat02(self.ctx)


class EnemyRetreat02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=144, patrol_name='MS2PatrolData_2001') # DevilWitch
        # Right Group1
        self.move_npc(spawn_id=145, patrol_name='MS2PatrolData_2105') # DevilWitch
        self.move_npc(spawn_id=146, patrol_name='MS2PatrolData_2101') # DevilWitch
        self.move_npc(spawn_id=147, patrol_name='MS2PatrolData_2003') # DevilWitch
        self.move_npc(spawn_id=170, patrol_name='MS2PatrolData_2104') # DevilJunior
        self.move_npc(spawn_id=172, patrol_name='MS2PatrolData_2102') # DevilJunior
        self.move_npc(spawn_id=178, patrol_name='MS2PatrolData_2002') # DevilJunior
        self.move_npc(spawn_id=179, patrol_name='MS2PatrolData_2104') # DevilJunior
        self.move_npc(spawn_id=180, patrol_name='MS2PatrolData_2101') # DevilJunior
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_2103') # DevilHuge
        self.move_npc(spawn_id=160, patrol_name='MS2PatrolData_2206') # DevilJunior
        # Left Group1
        self.move_npc(spawn_id=161, patrol_name='MS2PatrolData_2203') # DevilJunior
        self.move_npc(spawn_id=162, patrol_name='MS2PatrolData_2203') # DevilJunior
        self.move_npc(spawn_id=163, patrol_name='MS2PatrolData_2202') # DevilJunior
        self.move_npc(spawn_id=164, patrol_name='MS2PatrolData_2201') # DevilJunior
        self.move_npc(spawn_id=165, patrol_name='MS2PatrolData_2205') # DevilJunior
        self.move_npc(spawn_id=166, patrol_name='MS2PatrolData_2204') # DevilJunior

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return EnemyRetreat03(self.ctx)


class EnemyRetreat03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=171, patrol_name='MS2PatrolData_2101') # DevilJunior
        # Right Group2
        self.move_npc(spawn_id=174, patrol_name='MS2PatrolData_2103') # DevilJunior
        self.move_npc(spawn_id=175, patrol_name='MS2PatrolData_2101') # DevilJunior
        self.move_npc(spawn_id=176, patrol_name='MS2PatrolData_2105') # DevilJunior
        self.move_npc(spawn_id=177, patrol_name='MS2PatrolData_2003') # DevilJunior
        self.move_npc(spawn_id=150, patrol_name='MS2PatrolData_2104') # DevilHornSpear
        self.move_npc(spawn_id=151, patrol_name='MS2PatrolData_2101') # DevilHornSpear
        self.move_npc(spawn_id=152, patrol_name='MS2PatrolData_2103') # DevilHornSpear
        self.move_npc(spawn_id=153, patrol_name='MS2PatrolData_2104') # DevilHornSpear
        self.move_npc(spawn_id=154, patrol_name='MS2PatrolData_2102') # DevilHornSpear
        self.move_npc(spawn_id=155, patrol_name='MS2PatrolData_2105') # DevilHornSpear
        self.move_npc(spawn_id=156, patrol_name='MS2PatrolData_2101') # DevilHornSpear
        self.move_npc(spawn_id=140, patrol_name='MS2PatrolData_2206') # DevilWitch
        # Left Group2
        self.move_npc(spawn_id=141, patrol_name='MS2PatrolData_2203') # DevilWitch
        self.move_npc(spawn_id=142, patrol_name='MS2PatrolData_2205') # DevilWitch
        self.move_npc(spawn_id=143, patrol_name='MS2PatrolData_2201') # DevilWitch
        self.move_npc(spawn_id=167, patrol_name='MS2PatrolData_2202') # DevilJunior
        self.move_npc(spawn_id=168, patrol_name='MS2PatrolData_2203') # DevilJunior
        self.move_npc(spawn_id=169, patrol_name='MS2PatrolData_2206') # DevilJunior

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return EnemyRetreat04(self.ctx)


class EnemyRetreat04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=191, patrol_name='MS2PatrolData_2101') # DevilHornIronMace
        # Right Group3
        self.move_npc(spawn_id=192, patrol_name='MS2PatrolData_2103') # DevilHornIronMace
        self.move_npc(spawn_id=193, patrol_name='MS2PatrolData_2101') # DevilHornIronMace
        self.move_npc(spawn_id=194, patrol_name='MS2PatrolData_2105') # DevilHornIronMace
        self.move_npc(spawn_id=195, patrol_name='MS2PatrolData_2003') # DevilHornIronMace
        self.move_npc(spawn_id=114, patrol_name='MS2PatrolData_2204') # DevilHornIronMace
        # Left Group3
        self.move_npc(spawn_id=115, patrol_name='MS2PatrolData_2205') # DevilHornIronMace
        self.move_npc(spawn_id=116, patrol_name='MS2PatrolData_2201') # DevilHornIronMace
        self.move_npc(spawn_id=117, patrol_name='MS2PatrolData_2202') # DevilHornIronMace
        self.move_npc(spawn_id=118, patrol_name='MS2PatrolData_2206') # DevilHornIronMace
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_2203') # DevilHuge

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return EnemyRetreat05(self.ctx)


class EnemyRetreat05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_2002') # DevilHuge
        # Right Group4
        self.move_npc(spawn_id=187, patrol_name='MS2PatrolData_2001') # DevilHornIronMace
        self.move_npc(spawn_id=188, patrol_name='MS2PatrolData_2003') # DevilHornIronMace
        self.move_npc(spawn_id=189, patrol_name='MS2PatrolData_2101') # DevilHornIronMace
        self.move_npc(spawn_id=190, patrol_name='MS2PatrolData_2001') # DevilHornIronMace
        self.move_npc(spawn_id=120, patrol_name='MS2PatrolData_2202') # DevilHornSpear
        # Left Group4
        self.move_npc(spawn_id=121, patrol_name='MS2PatrolData_2201') # DevilHornSpear
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_2203') # DevilHornSpear
        self.move_npc(spawn_id=123, patrol_name='MS2PatrolData_2203') # DevilHornSpear
        self.move_npc(spawn_id=124, patrol_name='MS2PatrolData_2202') # DevilHornSpear
        self.move_npc(spawn_id=125, patrol_name='MS2PatrolData_2201') # DevilHornSpear
        self.move_npc(spawn_id=126, patrol_name='MS2PatrolData_2206') # DevilHornSpear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return EnemyRetreat06(self.ctx)


class EnemyRetreat06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[112,144,145,146,147,170,172,178,179,180]) # Right Group1
        self.destroy_monster(spawn_ids=[160,161,162,163,164,165,166]) # Left Group1
        self.move_npc(spawn_id=130, patrol_name='MS2PatrolData_2101') # DevilHornSpear
        # Right Group5
        self.move_npc(spawn_id=131, patrol_name='MS2PatrolData_2003') # DevilHornSpear
        self.move_npc(spawn_id=132, patrol_name='MS2PatrolData_2002') # DevilHornSpear
        self.move_npc(spawn_id=133, patrol_name='MS2PatrolData_2001') # DevilHornSpear
        self.move_npc(spawn_id=134, patrol_name='MS2PatrolData_2001') # DevilHornSpear
        self.move_npc(spawn_id=135, patrol_name='MS2PatrolData_2002') # DevilHornSpear
        self.move_npc(spawn_id=136, patrol_name='MS2PatrolData_2003') # DevilHornSpear
        self.move_npc(spawn_id=184, patrol_name='MS2PatrolData_2102') # DevilHornIronMace
        self.move_npc(spawn_id=113, patrol_name='MS2PatrolData_2201') # DevilHornIronMace
        # Left Group5
        self.move_npc(spawn_id=196, patrol_name='MS2PatrolData_2201') # DevilHornIronMace
        self.move_npc(spawn_id=197, patrol_name='MS2PatrolData_2203') # DevilHornIronMace
        self.move_npc(spawn_id=198, patrol_name='MS2PatrolData_2206') # DevilHornIronMace
        self.move_npc(spawn_id=199, patrol_name='MS2PatrolData_2205') # DevilHornIronMace

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EnemyRetreat07(self.ctx)


class EnemyRetreat07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[171,174,175,176,177,150,151,152,153,154,155,156]) # Right Group2
        self.destroy_monster(spawn_ids=[140,141,142,143,167,168,169]) # Left Group2
        self.move_npc(spawn_id=181, patrol_name='MS2PatrolData_2001') # DevilHornIronMace
        # Right Group6
        self.move_npc(spawn_id=182, patrol_name='MS2PatrolData_2002') # DevilHornIronMace
        self.move_npc(spawn_id=183, patrol_name='MS2PatrolData_2003') # DevilHornIronMace
        self.move_npc(spawn_id=185, patrol_name='MS2PatrolData_2002') # DevilHornIronMace
        self.move_npc(spawn_id=186, patrol_name='MS2PatrolData_2001') # DevilHornIronMace
        self.move_npc(spawn_id=960, patrol_name='MS2PatrolData_2201') # ShieldBarrierLeft
        # Left Group6
        self.move_npc(spawn_id=961, patrol_name='MS2PatrolData_2202') # ShieldBarrierLeft
        self.move_npc(spawn_id=962, patrol_name='MS2PatrolData_2203') # ShieldBarrierLeft
        self.move_npc(spawn_id=963, patrol_name='MS2PatrolData_2203') # ShieldBarrierLeft
        self.move_npc(spawn_id=964, patrol_name='MS2PatrolData_2201') # ShieldBarrierLeft
        self.move_npc(spawn_id=965, patrol_name='MS2PatrolData_2202') # ShieldBarrierLeft
        self.move_npc(spawn_id=970, patrol_name='MS2PatrolData_2002') # ShieldBarrierRight
        # Right Group7
        self.move_npc(spawn_id=971, patrol_name='MS2PatrolData_2003') # ShieldBarrierRight
        self.move_npc(spawn_id=972, patrol_name='MS2PatrolData_2003') # ShieldBarrierRight
        self.move_npc(spawn_id=973, patrol_name='MS2PatrolData_2002') # ShieldBarrierRight
        self.move_npc(spawn_id=974, patrol_name='MS2PatrolData_2001') # ShieldBarrierRight
        self.move_npc(spawn_id=975, patrol_name='MS2PatrolData_2001') # ShieldBarrierRight

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EnemyRetreat08(self.ctx)


class EnemyRetreat08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[191,192,193,194,195]) # Right Group3
        self.destroy_monster(spawn_ids=[114,115,116,117,118,110]) # Left Group3

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return EnemyRetreat09(self.ctx)


class EnemyRetreat09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111,187,188,189,190]) # Right Group4
        self.destroy_monster(spawn_ids=[120,121,122,123,124,125,126]) # Left Group4

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EnemyRetreat10(self.ctx)


class EnemyRetreat10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[130,131,132,133,134,135,136,184]) # Right Group5
        self.destroy_monster(spawn_ids=[113,196,197,198,199]) # Left Group5

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EnemyRetreat11(self.ctx)


class EnemyRetreat11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[181,182,183,184,185,186]) # Right Group6
        self.destroy_monster(spawn_ids=[990,991,992,993,994,995]) # Left Group6
        self.destroy_monster(spawn_ids=[980,981,982,983,984,985]) # Right Group7
        self.destroy_monster(spawn_ids=[290]) # Turka
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Ending01(self.ctx)


class Ending01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=44)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Ending02(self.ctx)


class Ending02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ManovichTalk03(self.ctx)


class ManovichTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')
        # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.add_cinematic_talk(npc_id=11003221, msg='$52000120_QD__01_HENESYSDEFENSE__18$', duration=4000, align=Align.Center, illust_id='Manovich_normal')
        # illustID = 표시할 일러스트의 npc id, 일러스트를 표시하기 싫으면 0으로 기입

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ManovichTalk03Skip(self.ctx)


class ManovichTalk03_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1]) # Turka
        self.select_camera(trigger_id=44)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ManovichTalk03Skip(self.ctx)


class ManovichTalk03Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_achievement(trigger_id=9900, type='trigger', achieve='henesysinvasion')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2000072, portal_id=1)
        self.set_user_value(trigger_id=10, key='DefencePhase', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 스테이트
            return Leave(self.ctx)


class Leave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 맵 튕기고 이동 명령 못 받을 상태를 대비한 스테이트
        self.move_user(map_id=2000072, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Leave(self.ctx)


initial_state = Wait
