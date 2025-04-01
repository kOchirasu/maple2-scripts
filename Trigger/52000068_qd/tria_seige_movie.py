""" trigger/52000068_qd/tria_seige_movie.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='tria_seige') == 1:
            return LoadingDelayB0(self.ctx)


# 챕터5 에필로그 [10002105 엇갈리는 마음]완료 시 연출맵으로 이동
class LoadingDelayB0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=NPC이동, action='nextState')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skill(trigger_ids=[701], enable=True)
        self.set_actor(trigger_id=11010, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=11010, visible=True, initial_sequence='Dead_A')
        self.set_actor(trigger_id=16000, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=16001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=16002, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16003, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16004, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16005, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16006, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16007, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=16008, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16009, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16010, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16011, visible=True, initial_sequence='Idle_A')
        self.set_actor(trigger_id=16012, visible=True, initial_sequence='Stun_A')
        self.spawn_monster(spawn_ids=[10000,10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023], auto_target=False)
        self.spawn_monster(spawn_ids=[10024,10025,10026,10027,10028,10029,10030,10031,10032,10033,10034], auto_target=False)
        self.set_visible_breakable_object(trigger_ids=[5000,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012])
        self.spawn_monster(spawn_ids=[11000,11001,11002,11003,11004,11005,11006,11007], auto_target=False)
        self.spawn_monster(spawn_ids=[11009], auto_target=False)
        self.set_sound(trigger_id=90000, enable=True) # TriaAttack

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return LoadingDelayB1(self.ctx)


class LoadingDelayB1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 원경카메라01(self.ctx)


class 원경카메라01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[12000,12001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 원경카메라02(self.ctx)


class 원경카메라02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[12002,12003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 원경카메라03(self.ctx)


class 원경카메라03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[12004,12005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 프레이대사(self.ctx)


class 프레이대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000064, illust_id='Lennon_closeEye', msg='$52000068_QD__TRIA_SEIGE_MOVIE__0$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 알론대사(self.ctx)


class 알론대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000068_QD__TRIA_SEIGE_MOVIE__1$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 근위대원등장(self.ctx)


class 근위대원등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=2.0)
        self.spawn_monster(spawn_ids=[11008], auto_target=False)
        self.move_npc(spawn_id=11008, patrol_name='MS2PatrolData_soldier') # 에레브 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 근위대대사01(self.ctx)


class 근위대대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001968, script='$52000068_QD__TRIA_SEIGE_MOVIE__2$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 근위대대사02(self.ctx)


class 근위대대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001968, script='$52000068_QD__TRIA_SEIGE_MOVIE__3$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 근위대대사03(self.ctx)


class 근위대대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000601, script='$52000068_QD__TRIA_SEIGE_MOVIE__4$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 근위대대사04(self.ctx)


class 근위대대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0.5)
        self.move_npc(spawn_id=11000, patrol_name='MS2PatrolData_GoToJody_ereb') # 에레브 이동
        self.move_npc(spawn_id=11001, patrol_name='MS2PatrolData_GoToJody_karl') # 칼 이동
        self.move_npc(spawn_id=11002, patrol_name='MS2PatrolData_GoToJody_luana') # 루아나 이동
        self.move_npc(spawn_id=11003, patrol_name='MS2PatrolData_GoToJody_BlackEye') # 블랙아이 이동
        self.move_npc(spawn_id=11004, patrol_name='MS2PatrolData_GoToJody_lennon') # 레논 이동
        self.move_npc(spawn_id=11005, patrol_name='MS2PatrolData_GoToJody_eve') # 이브 이동
        self.move_npc(spawn_id=11006, patrol_name='MS2PatrolData_GoToJody_alon') # 알론 이동
        self.move_npc(spawn_id=11007, patrol_name='MS2PatrolData_GoToJody_pray') # 프레이 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return None # Missing State: 지원군등장


initial_state = start
