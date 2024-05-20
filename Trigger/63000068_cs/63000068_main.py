""" trigger/63000068_cs/63000068_main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000358], quest_states=[3]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000358], quest_states=[2]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000358], quest_states=[1]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000357], quest_states=[3]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000357], quest_states=[2]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000357], quest_states=[1]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000356], quest_states=[3]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000356], quest_states=[2]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000356], quest_states=[1]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000355], quest_states=[3]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000355], quest_states=[2]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000355], quest_states=[1]):
            return 몬스터등장_04(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000354], quest_states=[3]):
            return 몬스터등장_03(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000354], quest_states=[2]):
            return 몬스터등장_02(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000354], quest_states=[1]):
            return 잠시대기_01(self.ctx)
        if self.user_detected(box_ids=[701]):
            return 몬스터등장_04(self.ctx)


class 잠시대기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 잠시대기_02(self.ctx)


class 잠시대기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.spawn_monster(spawn_ids=[201], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마리엔등장_01(self.ctx)


class 마리엔등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=마리엔등장_10, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마리엔등장_02(self.ctx)


class 마리엔등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000068_CS__63000068_MAIN__0$', duration=2000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 마리엔등장_03(self.ctx)


class 마리엔등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000068_CS__63000068_MAIN__1$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마리엔등장_04(self.ctx)


class 마리엔등장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000068_CS__63000068_MAIN__2$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 마리엔등장_05(self.ctx)


class 마리엔등장_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return 마리엔등장_06(self.ctx)


class 마리엔등장_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마리엔등장_07(self.ctx)


class 마리엔등장_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000068_CS__63000068_MAIN__3$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 마리엔등장_08(self.ctx)


class 마리엔등장_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000068_CS__63000068_MAIN__4$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 마리엔등장_09(self.ctx)


class 마리엔등장_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마리엔등장_10(self.ctx)


class 마리엔등장_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.select_camera_path(path_ids=[8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 몬스터등장_01(self.ctx)


class 몬스터등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.spawn_monster(spawn_ids=[113], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마리엔퇴장_01(self.ctx)


class 몬스터등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.spawn_monster(spawn_ids=[113], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 재입장시(self.ctx)


class 몬스터등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.spawn_monster(spawn_ids=[113], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트마리엔등장(self.ctx)


class 몬스터등장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.spawn_monster(spawn_ids=[106], auto_target=False)
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.spawn_monster(spawn_ids=[108], auto_target=False)
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.spawn_monster(spawn_ids=[110], auto_target=False)
        self.spawn_monster(spawn_ids=[111], auto_target=False)
        self.spawn_monster(spawn_ids=[112], auto_target=False)
        self.spawn_monster(spawn_ids=[113], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 마리엔퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마리엔퇴장_02(self.ctx)


class 마리엔퇴장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000068_CS__63000068_MAIN__5$', duration=2000, align=Align.Right)
        self.set_effect(trigger_ids=[5003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 마리엔퇴장_03(self.ctx)


class 마리엔퇴장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마리엔퇴장_04(self.ctx)


class 마리엔퇴장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=26300681, text_id=26300681)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[705], quest_ids=[30000354], quest_states=[2]):
            return 암전_01(self.ctx)


class 재입장시(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[705], quest_ids=[30000354], quest_states=[2]):
            return 암전_01(self.ctx)


class 암전_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=26300681)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 암전_02(self.ctx)


class 암전_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마리엔재등장_01(self.ctx)


class 마리엔재등장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=재등장연출완료, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마리엔재등장_02(self.ctx)


class 마리엔재등장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마리엔재등장_03(self.ctx)


class 마리엔재등장_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 마리엔재등장_04(self.ctx)


class 마리엔재등장_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000068_CS__63000068_MAIN__6$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 마리엔재등장_05(self.ctx)


class 마리엔재등장_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000068_CS__63000068_MAIN__7$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 마리엔재등장_06(self.ctx)


class 마리엔재등장_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000068_CS__63000068_MAIN__8$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 마리엔재등장_07(self.ctx)


class 마리엔재등장_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11004294, msg='$63000068_CS__63000068_MAIN__9$', duration=2000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 재등장연출완료(self.ctx)


class 재등장연출완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트마리엔등장(self.ctx)


class 퀘스트마리엔등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[705], quest_ids=[30000355], quest_states=[1]):
            return 퀘스트마리엔퇴장_01(self.ctx)
        if self.quest_user_detected(box_ids=[705], quest_ids=[30000355], quest_states=[2]):
            return 퀘스트마리엔퇴장_01(self.ctx)


class 퀘스트마리엔퇴장_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 퀘스트마리엔퇴장_02(self.ctx)


class 퀘스트마리엔퇴장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = 준비
