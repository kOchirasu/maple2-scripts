""" trigger/52000037_qd/lookinto_beginner_02.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, initial_sequence='Dead_A') # NelfActor
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=13)
        self.set_mesh(trigger_ids=[3000,3001], visible=True)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, path='BG/Common/Sound/Eff_System_Dark_Ending_Chord_01.xml')
        self.set_onetime_effect(id=3, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_onetime_effect(id=4, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_onetime_effect(id=5, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100070], quest_states=[3], job_code=1):
            # 초보자 넬프의 죽음 퀘스트 완료
            return Quit(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[60100070], quest_states=[2], job_code=1):
            # 초보자 넬프의 죽음 퀘스트 완료 가능
            return Quit(self.ctx)
        if self.quest_user_detected(box_ids=[9900], quest_ids=[60100070], quest_states=[1], job_code=1):
            # 초보자 넬프의 죽음 퀘스트 진행중
            return LoadingDelay02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100065], quest_states=[3], job_code=1):
            # 초보자 랄프의 정보 퀘스트 완료
            return DefaultSetting02(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100065], quest_states=[2], job_code=1):
            # 초보자 랄프의 정보 퀘스트 완료 가능
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Dead_A') # NelfActor

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera(trigger_id=800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraWalk02(self.ctx)


class CameraWalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraWalk03(self.ctx)


class CameraWalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=801)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraWalk04(self.ctx)


class CameraWalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/Sound/Eff_System_Dark_Ending_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraShot01(self.ctx)


class CameraShot01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=802)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return CameraShot02(self.ctx)


class CameraShot02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=803)
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            return CameraShot03(self.ctx)


class CameraShot03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=804)
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraFadeIn01(self.ctx)


class CameraFadeIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraFadeOut01(self.ctx)


class CameraFadeOut01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera(trigger_id=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return DefaultSetting02(self.ctx)


class DefaultSetting02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Dead_A') # NelfActor
        self.spawn_monster(spawn_ids=[101], auto_target=False) # NelfDummyNPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9900], quest_ids=[60100070], quest_states=[1]):
            # 초보자 넬프의 죽음 퀘스트 수락
            return LoadingDelay02(self.ctx)


class LoadingDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_actor(trigger_id=4000, visible=True, initial_sequence='Dead_A') # NelfActor
        self.spawn_monster(spawn_ids=[501], auto_target=False) # 의문의남자

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return LoadingDelay03(self.ctx)


class LoadingDelay03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000037, portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FindDoor01(self.ctx)


class FindDoor01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrol_name='MS2PatrolData_1200')
        self.select_camera(trigger_id=810)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FindDoor02(self.ctx)


class FindDoor02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=13, visible=True, enable=True, minimap_visible=True)
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_500') # 의문의남자

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FindDoor03(self.ctx)


class FindDoor03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=811)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Chase01(self.ctx)


class Chase01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001], start_delay=100, interval=200, fade=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Chase02(self.ctx)


class Chase02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_501') # 의문의남자

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9500, spawn_ids=[501]):
            return Chase03(self.ctx)


class Chase03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[501])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=811, enable=False)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000037_QD__LOOKINTO_BEGINNER_02__0$', arg3='3000', arg4='0')


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = Wait
