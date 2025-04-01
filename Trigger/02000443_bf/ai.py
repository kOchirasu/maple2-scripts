""" trigger/02000443_bf/ai.xml """
import trigger_api


"""
플레이어 감지
슈팅전 체크 에디셔널 이펙트를 계속 걸어줌
"""
class IsDungeonRoomReady(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return idle(self.ctx)


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Ending') == 1:
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[210]) # 메비딕 제거
        self.destroy_monster(spawn_ids=[101,102]) # 초반 등장 npc 제거

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Ending(self.ctx)


class Ending(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=49200003, level=1, ignore_player=False, is_skill_set=False)
        self.remove_buff(box_id=701, skill_id=99910120)
        self.set_effect(trigger_ids=[7001], visible=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[202,103,104])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ending_02(self.ctx)


class Ending_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=Ending_04)
        self.select_camera_path(path_ids=[8101,8102,8103], return_view=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Stun_A', duration=9000000.0)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2008')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_2007')
        self.set_dialogue(type=1, spawn_id=103, script='$02000443_BF__AI__0$', time=2)
        self.set_dialogue(type=1, spawn_id=104, script='$02000443_BF__AI__1$', time=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Ending_03(self.ctx)


class Ending_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=202, script='$02000443_BF__AI__2$', time=2)
        self.set_dialogue(type=1, spawn_id=104, script='$02000443_BF__AI__3$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=103, script='$02000443_BF__AI__4$', time=2, arg5=3)
        self.set_dialogue(type=1, spawn_id=202, script='$02000443_BF__AI__5$', time=2, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Ending_04(self.ctx)


class Ending_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Ending_04_b(self.ctx)


class Ending_04_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ending_05(self.ctx)


class Ending_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_local_camera(camera_id=8001) # LocalTargetCamera
        self.set_local_camera(camera_id=8002) # LocalTargetCamera
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return IsDungeonRoom(self.ctx)


class IsDungeonRoom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return dungeonEnd(self.ctx)


class dungeonEnd(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001])
        self.set_mesh(trigger_ids=[1001,1002])
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_achievement(trigger_id=701, type='trigger', achieve='clearalbanos')
        self.set_achievement(trigger_id=701, type='trigger', achieve='ClearOceanKing')
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[50001518], quest_states=[1]):
            return None # Missing State: QuestEnd_warp


initial_state = IsDungeonRoomReady
