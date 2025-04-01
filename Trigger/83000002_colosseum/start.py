""" trigger/83000002_colosseum/start.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import Align


"""
class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CameraStart') == 1:
            return 유저감지(self.ctx)
"""

class 유저감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_user_value(trigger_id=1001, key='CameraStart', value=0)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2001], job_code=0):
            return 연출준비(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.destroy_monster(spawn_ids=[202])
        self.destroy_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출_01(self.ctx)


class 연출_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출_01_01(self.ctx)


class 연출_01_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4002], return_view=False)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출_02(self.ctx)


class 연출_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003,4004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출_03(self.ctx)


class 연출_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 연출_05(self.ctx)


class 연출_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[4005,4006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출_07(self.ctx)


class 연출_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007,4008], return_view=False)
        self.show_caption(type='VerticalCaption', title='$83000002_COLOSSEUM__START__0$', align=Align.bottomLeft, duration=5000, scale=2.5)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.set_cinematic_ui(type=0)
            self.reset_camera()
            return 연출끝_01(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[4009], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_cinematic_ui(type=0)
            self.reset_camera()
            return 대화딜레이(self.ctx)


class 대화딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 연출끝_01(self.ctx)


class 연출끝_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # NPC에게 자동으로 대화걸기 NPCID: 11004288/나기
        self.talk_npc(spawn_id=203)
        # self.debug_string(value='라운드 클리어 테스트 합니다. 현재 5라운드 클리어로 설정됩니다.')
        # self.dungeon_clear_round(round=5)
        # self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[902]):
            self.move_user_to_pos(pos=Vector3(300,-225,1500), rot=Vector3(0,0,270))
            return 대화딜레이(self.ctx)
        if self.user_value(key='DungeonPlayType') == 1:
            return NewGame(self.ctx)
        if self.user_value(key='DungeonPlayType') == 2:
            return ContinueGame(self.ctx)


class NewGame(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='새로 시작하기를 설정했습니다.')
        self.set_user_value(trigger_id=900001, key='MainStart', value=1)


class ContinueGame(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='이어하기를 설정했습니다.')
        self.dungeon_disable_ranking()
        self.set_user_value(trigger_id=900001, key='MainStart', value=2)


initial_state = 유저감지
