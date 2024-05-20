""" trigger/52020028_qd/main30000328.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 아크로폴리스 수호자 처치 퀘스트를 받고 입장
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[30000328], quest_states=[1]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020028, portal_id=6002)
        self.set_onetime_effect(id=1000, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아크로폴리스내부확인(self.ctx)


class 아크로폴리스내부확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.show_caption(type='VerticalCaption', title='아크로폴리스', desc='고대 크리티아스 지식의 안식처', align=Align.Center | Align.Left, duration=4000, scale=2.0)
        self.select_camera_path(path_ids=[4002,4003,4004], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='여기가 아크로폴리스...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4012,4001], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3001')
        self.add_cinematic_talk(npc_id=0, msg='생각보다 조용하군.', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='수호자 때문에 안에 들어갈 수가 없다니, 얼마나 대단한 녀석인거지.', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='싸우지 않을 수 있었으면 좋겠는데.', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='그나저나, 정말 아무도 없는 것 같은데...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 유저자격확인하기전(self.ctx)


class 유저자격확인하기전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_effect(trigger_ids=[5003], visible=True)
        self.face_emotion(emotion_name='Trigger_panic')
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=6000.0)
        self.add_balloon_talk(msg='?!', duration=3000)
        self.add_balloon_talk(msg='이... 이건?', duration=3000, delay_tick=3000)
        self.set_scene_skip(state=경고, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 유저자격확인(self.ctx)


class 유저자격확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='침입자 발견. 자격을 확인한다.')
        self.set_scene_skip(state=아르케온등장4, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 유저자격확인2(self.ctx)


class 유저자격확인2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.face_emotion(emotion_name='Trigger_panic')
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=18000.0)
        self.set_effect(trigger_ids=[5003], visible=True)
        self.add_balloon_talk(msg='자격을 확인한다고? 잠깐!!!', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 유저자격확인2_1(self.ctx)


class 유저자격확인2_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=22000117, msg='문답무용.\\n순수한 크리티아스의 피가 흐르지 않는 자는 이곳에 발을 디딜 수 없다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 유저자격확인3(self.ctx)


class 유저자격확인3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010], return_view=False)
        self.add_balloon_talk(msg='잠시 이야기를 들어줘!', duration=3000, delay_tick=4000)
        self.add_cinematic_talk(npc_id=22000117, msg='결과를 확인한다.', duration=3000)
        self.add_cinematic_talk(npc_id=22000117, msg='결과, 부적합.\\n전투 시스템 가동.', duration=3000)
        self.set_effect(trigger_ids=[5003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 아르케온등장(self.ctx)


class 아르케온등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003])
        self.set_onetime_effect(id=1000, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npc_id=22000117, msg='자격이 없는 자, 즉시 처단한다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아르케온등장2(self.ctx)


class 아르케온등장2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.add_balloon_talk(msg='아니 대화가 전혀 안 통하잖아!', duration=2000)
        self.set_onetime_effect(id=1000, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 경고(self.ctx)


class 경고(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 등장연출(self.ctx)


class 등장연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1000, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.show_caption(type='VerticalCaption', title='아르케온', desc='아크로폴리스의 수호자', align=Align.Center | Align.Left, duration=4000, scale=2.0)
        self.set_onetime_effect(id=1001, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아르케온등장3(self.ctx)


class 아르케온등장3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, msg='역시 이렇게 되는군.', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='말이 통하지 않으니, 어쩔 수 없지.\\n여기서 시간을 낭비할 수 없어.\\n어서 처치하자.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 아르케온등장4(self.ctx)


class 아르케온등장4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1001, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='수호자 아르케온을 처치하세요.', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 다음연출시작(self.ctx)


class 다음연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다음연출시작_02(self.ctx)


class 다음연출시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020028, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 위치이동(self.ctx)


class 위치이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=0, msg='휴... 힘든 싸움이었어.', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='중요한 시설인가보군, 이런 괴물같은 녀석이 지키고 있는 것을 보니...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 진리의문확인(self.ctx)


class 진리의문확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004,4003], return_view=False)
        self.set_effect(trigger_ids=[5002])
        self.add_cinematic_talk(npc_id=0, msg='아무래도 저기가 진리의 문인가 보군.', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='아르망에게 전달해야겠어. 알케이나 고원으로 돌아가자.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 이오네독백준비(self.ctx)


class 이오네독백준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(is_visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 이오네독백준비_02(self.ctx)


class 이오네독백준비_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.select_camera(trigger_id=4011)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 이오네독백(self.ctx)


class 이오네독백(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011,4008], return_view=False)
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.show_caption(type='VerticalCaption', title='이오네', desc='크리티아스의 왕녀', align=Align.Center | Align.Left, duration=4000, scale=2.0)
        self.add_cinematic_talk(npc_id=11003760, msg='그 동안 수고 했어요. 아르케온.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 이오네독백_02(self.ctx)


class 이오네독백_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003760, msg='이 뒤는 저에게 맡기고 편히 쉬세요.', duration=3000)
        self.add_cinematic_talk(npc_id=11003760, msg='이제 이 곳의 모든 정보는 그 누구도 열어보지 못하도록...\\n이 이오네가 책임지고 막겠습니다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Warp준비(self.ctx)


class Warp준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Warp(self.ctx)


class Warp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2020016, portal_id=3)


initial_state = idle
