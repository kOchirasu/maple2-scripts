""" trigger/52010040_qd/52010040.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000013], quest_states=[2]):
            # [함선 강탈] 퀘스트 완료가능 상태
            return 도입부연출01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[91000015], quest_states=[3]):
            # [스카이 포트리스, 임무개시] 퀘스트 완료
            return 엔딩연출01(self.ctx)


class 도입부연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 블리체
        self.spawn_monster(spawn_ids=[300], auto_target=False) # 블랙아이
        self.spawn_monster(spawn_ids=[301], auto_target=False) # 알론
        self.spawn_monster(spawn_ids=[302], auto_target=False) # 프레이
        self.spawn_monster(spawn_ids=[303], auto_target=False) # 오스칼
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 도입부연출02(self.ctx)


class 도입부연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$52010040_QD__52010040__0$', desc='$52010040_QD__52010040__1$', align=Align.Bottom | Align.Left, duration=7000, scale=2.5)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[2000,2001,2002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 도입부연출03_b(self.ctx)


class 도입부연출03_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_blicheCome') # 블리체 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 도입부연출03(self.ctx)


class 도입부연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 도입부연출04(self.ctx)


class 도입부연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


# ########################튜토리얼 종료씬########################
class 엔딩연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 블리체
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 엔딩연출02(self.ctx)


class 엔딩연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=quit, action='nextState')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npc_id=11003536, illust_id='Neirin_normal', msg='$52010040_QD__52010040__2$', duration=6200, align=Align.Right)
        self.select_camera_path(path_ids=[2012,2013], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_blicheCome')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_bliche_front') # 블리체 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 엔딩연출03(self.ctx)


class 엔딩연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010040_QD__52010040__3$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 엔딩연출04(self.ctx)


class 엔딩연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010040_QD__52010040__4$', duration=5400, align=Align.Right)
        self.select_camera_path(path_ids=[2010,2011,2014], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 엔딩연출05(self.ctx)


class 엔딩연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010040_QD__52010040__5$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4100):
            return 엔딩연출06_b(self.ctx)


class 엔딩연출06_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010040_QD__52010040__6$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 엔딩연출06(self.ctx)


class 엔딩연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 엔딩연출07(self.ctx)


class 엔딩연출07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return quit(self.ctx)


class quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000422, portal_id=3)


initial_state = Wait
