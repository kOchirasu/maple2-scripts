""" trigger/52020019_qd/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_sound(trigger_id=7001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200010], quest_states=[1]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.spawn_monster(spawn_ids=[101]) # 이오네
        self.spawn_monster(spawn_ids=[102]) # 미카엘
        self.move_user(map_id=52020019, portal_id=6001)
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.set_portal(portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Camera_Work_01(self.ctx)


class Camera_Work_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.set_scene_skip(action='nextState') # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ShowCaption(self.ctx)


class ShowCaption(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='VerticalCaption', title='$map:52020019$', desc='$npcName:11003614$의 두 번째 시험장.', align=Align.Bottom | Align.Left, duration=2000, scale=1.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Camera_Work_02(self.ctx)


class Camera_Work_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_01(self.ctx)


class EventScene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003614, msg='자, 시작하세요.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_02(self.ctx)


class EventScene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_03(self.ctx)


class EventScene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_3002')
        self.add_cinematic_talk(npc_id=11003598, msg='오호.... 제법 기합을 넣을 줄 아시는군요.', duration=2500, illust_id='Michael_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_04(self.ctx)


class EventScene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003598, msg='그럼 시작하기전에....', duration=2500, illust_id='Michael_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_05(self.ctx)


class EventScene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003598, msg='정식으로 제 소개를 하죠.', duration=2500, illust_id='Michael_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_06(self.ctx)


class EventScene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003598, msg='제 이름은 $npcName:11003598$.', duration=2500, illust_id='Michael_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_07(self.ctx)


class EventScene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003598, msg='크리티아스 제 3기사. 몽환의 $npcName:11003598$입니다.', duration=3000, illust_id='Michael_normal', align=Align.Center)
        self.show_caption(type='NameCaption', title='$npcName:11003598$', desc='몽환의 기사', align=Align.Center | Align.Left, offset_rate_x=0.05, offset_rate_y=0.15, duration=3000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return EventScene_08(self.ctx)


class EventScene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_effect(trigger_ids=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return EventScene_09(self.ctx)


class EventScene_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Bore_A'])
        self.add_balloon_talk(msg='!!!', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_10(self.ctx)


class EventScene_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Emotion_B')
        self.add_cinematic_talk(npc_id=11003598, msg='자, 그럼 당신의 실력을 확인해보도록 하죠.', duration=3000, illust_id='Michael_normal', align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return White(self.ctx)


class White(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Battle_Ready(self.ctx)


class Battle_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True)
        self.destroy_monster(spawn_ids=[102]) # 미카엘
        self.spawn_monster(spawn_ids=[201]) # 미카엘 몬스터

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Battle(self.ctx)


class Battle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return Battle_Stop(self.ctx)


class Battle_Stop(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='그만!', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Battle_End(self.ctx)


class Battle_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[201]) # 미카엘

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return EventScene_11(self.ctx)


class EventScene_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003614, msg='그만 하세요.', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_12(self.ctx)


class EventScene_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003598, msg='이런, 이제 막 재미있어지려는 참이었는데 아쉽군요.', duration=2500, illust_id='Michael_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_13(self.ctx)


class EventScene_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003598, msg='뭐, 다음 기회라는 것도 있으니 이번엔 여기까지만 하겠습니다.', duration=2500, illust_id='Michael_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_14(self.ctx)


class EventScene_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003614, msg='.......', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_15(self.ctx)


class EventScene_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003614, msg='돌아가죠. $npcName:11003598$.', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EventScene_16(self.ctx)


class EventScene_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003598, msg='네. 분부대로.', duration=2500, illust_id='Michael_normal', align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return QuestComplete(self.ctx)


class QuestComplete(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(type='trigger', achieve='ForgottenrRoad')
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Warp(self.ctx)


class Warp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2020006, portal_id=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[60200010], quest_states=[1]):
            return QuestComplete(self.ctx)


initial_state = Idle
