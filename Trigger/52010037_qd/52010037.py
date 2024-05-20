""" trigger/52010037_qd/52010037.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 콘대르
        self.spawn_monster(spawn_ids=[202], auto_target=False) # 샤텐
        self.spawn_monster(spawn_ids=[203], auto_target=False) # 네이린
        self.spawn_monster(spawn_ids=[204], auto_target=False) # 메이슨
        self.spawn_monster(spawn_ids=[205], auto_target=False) # 블랙아이
        self.spawn_monster(spawn_ids=[206], auto_target=False) # 알론
        self.spawn_monster(spawn_ids=[207], auto_target=False) # 프레이
        self.spawn_monster(spawn_ids=[208], auto_target=False) # 오스칼
        self.set_actor(trigger_id=501, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=502, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=503, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=504, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=505, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=506, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=507, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=508, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=509, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=510, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=511, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=512, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=513, visible=True, initial_sequence='sf_quest_light_A01_Off')
        self.set_actor(trigger_id=514, visible=True, initial_sequence='sf_quest_light_A01_Off')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000003], quest_states=[2]):
            # [하늘의 요새] 퀘스트 완료가능 상태
            return 지하기지전경씬01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000013], quest_states=[1]):
            # [긴급 이륙] 퀘스트 시작
            self.move_user(map_id=52010038, portal_id=1)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000013], quest_states=[2]):
            # [긴급 이륙] 퀘스트 완료 가능 상태
            self.move_user(map_id=52010039, portal_id=1)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000004], quest_states=[2]):
            # [새로운 지휘관] 퀘스트 시작
            self.spawn_monster(spawn_ids=[200], auto_target=False) # 블리체
            return 블리체와대장들이동(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000010], quest_states=[3]):
            # [새로운 지휘관] 퀘스트 완료
            return 긴급상황발동01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000004], quest_states=[3]):
            # [새로운 지휘관] 퀘스트 시작
            self.spawn_monster(spawn_ids=[200], auto_target=False) # 블리체
            return 블리체와대장들이동(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000003], quest_states=[3]):
            # [하늘의 요새] 퀘스트 완료
            return 블리체함장등장(self.ctx)


# ########################지하기지 전경씬########################
class 지하기지전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 지하기지전경씬02(self.ctx)


class 지하기지전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Quit01, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[3000,3001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 지하기지전경씬02_b(self.ctx)


class 지하기지전경씬02_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3002,3003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 지하기지전경씬02_c(self.ctx)


class 지하기지전경씬02_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3004,3005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 지하기지전경씬03(self.ctx)


class 지하기지전경씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52010037_QD__52010037__0$', desc='$52010037_QD__52010037__1$', align=Align.Bottom | Align.Left, duration=7000, scale=2.5)
        self.select_camera_path(path_ids=[3006,3007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 지하기지전경씬04(self.ctx)


class 지하기지전경씬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000003], quest_states=[3]):
            # [하늘의 요새] 퀘스트 완료
            return 블리체함장등장(self.ctx)


# ########################지하기지 전경씬########################
class 블리체함장등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 블리체
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_bliche_come') # 블리체 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000004], quest_states=[2]):
            # [새로운 지휘관] 퀘스트 시작
            return 블리체와대장들이동(self.ctx)


class 블리체와대장들이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_bliche_go') # 블리체 이동
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_blackEye') # 블랙아이 이동
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_alon') # 알론 이동
        self.move_npc(spawn_id=207, patrol_name='MS2PatrolData_pray') # 프레이 이동
        self.move_npc(spawn_id=208, patrol_name='MS2PatrolData_oscal') # 오스칼 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000010], quest_states=[3]):
            # [의문의 레이더 반응] 퀘스트 완료
            return 긴급상황발동01(self.ctx)


class 긴급상황발동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=9010, enable=True) # 케이틀린 등장 브금
        self.set_ambient_light(primary=Vector3(232,92,53))
        self.set_directional_light(diffuse_color=Vector3(41,21,18), specular_color=Vector3(130,130,130))
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_actor(trigger_id=501, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=502, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=503, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=504, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=505, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=506, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=507, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=508, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=509, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=510, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=511, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=512, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=513, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.set_actor(trigger_id=514, visible=True, initial_sequence='sf_quest_light_A01_On')
        self.destroy_monster(spawn_ids=[204]) # 메이슨 삭제
        self.destroy_monster(spawn_ids=[200]) # 블리체 삭제
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_conder_come') # 콘대르 이동
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_shatten_come') # 샤텐 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 긴급상황발동02(self.ctx)


class 긴급상황발동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.spawn_monster(spawn_ids=[209], auto_target=False) # 프레이
        self.spawn_monster(spawn_ids=[210], auto_target=False) # 오스칼


initial_state = Wait
