""" trigger/63000067_cs/63000067_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[103])
        self.spawn_monster(spawn_ids=[104])
        self.spawn_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[107])
        self.spawn_monster(spawn_ids=[108])
        self.spawn_monster(spawn_ids=[109])
        self.spawn_monster(spawn_ids=[110])
        self.spawn_monster(spawn_ids=[111])
        self.spawn_monster(spawn_ids=[112])
        self.spawn_monster(spawn_ids=[113])
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000352], quest_states=[1]):
            return 인형찾기(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000352], quest_states=[2]):
            return 마리엔의방(self.ctx)
        if self.user_detected(box_ids=[701]):
            return 종료_일반(self.ctx)


class 인형찾기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=26300671, text_id=26300671)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[30000352], quest_states=[2]):
            return 암전_01(self.ctx)


class 마리엔의방(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[30000352], quest_states=[2]):
            return 암전_01(self.ctx)


class 암전_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=26300671)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 암전_02(self.ctx)


class 암전_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마리엔등장_01(self.ctx)


class 마리엔등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=스킵종료, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마리엔등장_02(self.ctx)


class 마리엔등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마리엔등장_03(self.ctx)

    def on_exit(self) -> None:
        self.select_camera_path(path_ids=[8002], return_view=False)


class 마리엔등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 마리엔등장_04(self.ctx)


class 마리엔등장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000067_CS__63000067_MAIN__0$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 마리엔등장_05(self.ctx)


class 마리엔등장_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000067_CS__63000067_MAIN__1$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 마리엔등장_06(self.ctx)


class 마리엔등장_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 마리엔등장_07(self.ctx)


class 마리엔등장_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000067_CS__63000067_MAIN__2$', duration=3500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 마리엔등장_08(self.ctx)


class 마리엔등장_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 마리엔등장_09(self.ctx)


class 마리엔등장_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000067_CS__63000067_MAIN__3$', duration=2000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 마리엔등장_10(self.ctx)


class 마리엔등장_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000067_CS__63000067_MAIN__4$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 마리엔퇴장_01(self.ctx)


class 마리엔퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.destroy_monster(spawn_ids=[201])
        self.set_effect(trigger_ids=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 마리엔퇴장_02(self.ctx)


class 마리엔퇴장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        return 종료_퀘스트(self.ctx)


class 스킵종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.destroy_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        return 종료_퀘스트(self.ctx)


class 종료_퀘스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_effect(trigger_ids=[5002])
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


class 종료_일반(trigger_api.Trigger):
    pass


initial_state = 준비
