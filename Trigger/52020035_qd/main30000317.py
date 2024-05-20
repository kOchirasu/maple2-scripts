""" trigger/52020035_qd/main30000317.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 퀘스트 수락 후 연출 시작
class idle2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[30000317], quest_states=[1]):
            return 연출시작2(self.ctx)
        if self.quest_user_detected(box_ids=[702], quest_ids=[30000317], quest_states=[2]):
            return Skip_1(self.ctx)


# 라딘과 대화 시작
class 연출시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작3(self.ctx)


class 연출시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52020035, portal_id=6001)
        self.spawn_monster(spawn_ids=[110], auto_target=False) # 연출라딘
        self.select_camera_path(path_ids=[4007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 라딘과대화시작(self.ctx)


class 라딘과대화시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Skip_1, action='exit')
        self.add_cinematic_talk(npc_id=11003753, msg='자네도 알겠지만 수호군이 크리티아스에 쉽게 오지는 못할걸세.', duration=3000)
        self.add_cinematic_talk(npc_id=11003753, msg='지원군을 소집하는데도 시간이 걸리겠지만\\n우리가 포털 수리 및 방어 시스템을 무력화시키지 않는다면\\n결국 또 다른 많은 희생을 치루게 되겠지.', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7500):
            return 라딘과대화시작_02(self.ctx)


class 라딘과대화시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4027], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='그렇다면 저희가 나서서 수호군이 안전하게 올 수 있도록 조치를 취해야겠군요.', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 라딘과대화시작_03(self.ctx)


class 라딘과대화시작_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4028], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='그렇지. 게다가 자네가 얘기해준 티어스 코어라는 물건에 대해서도 빨리 정보를 찾아\\n왜 어둠의 세력이 그것을 노리고 있는지도 알아내야 하고 말이야.', duration=4500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 라딘과대화시작_04(self.ctx)


class 라딘과대화시작_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4027], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='해야할 일이 많네요… 이럴 때 수호군의 동료들이 있었다면…', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 라딘과대화시작_05(self.ctx)


class 라딘과대화시작_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4028], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='그래서 우리를 도와줄만한 사람들에게 연락을 취해두었네.\\n곧 도착할 시간인데…', duration=4000)
        self.move_user(map_id=52020035, portal_id=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 흑성회다같이입장1(self.ctx)


# 들어오는 흑성회
class 흑성회다같이입장1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.set_npc_rotation(spawn_id=110, rotation=-45.0)
        self.add_cinematic_talk(npc_id=11003753, msg='아. 마침 저기 들어오는군.', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='<font size=\'40\'>!!! 저 녀석들은?</font>', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.spawn_monster(spawn_ids=[111], auto_target=False) # 연출웨이홍
        self.spawn_monster(spawn_ids=[115], auto_target=False) # 연출브리드민
        self.spawn_monster(spawn_ids=[112], auto_target=False) # 연출바사라첸
        self.spawn_monster(spawn_ids=[113], auto_target=False) # 연출하렌
        self.spawn_monster(spawn_ids=[114], auto_target=False) # 연출카일

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 간부얼굴준비(self.ctx)


# 각 간부들의 얼굴을 비추자 1
class 간부얼굴준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4010,4011], return_view=False)
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_3007')
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_3006')
        self.move_npc(spawn_id=113, patrol_name='MS2PatrolData_3003')
        self.move_npc(spawn_id=114, patrol_name='MS2PatrolData_3004')
        self.move_npc(spawn_id=115, patrol_name='MS2PatrolData_3005')
        self.set_onetime_effect(id=9, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=0, msg='<font size=\'40\'>흑성회?!</font>', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 하렌(self.ctx)


# 각 간부들의 얼굴을 비추자 2
class 하렌(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4012], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=113, sequence_name='Bore_A')
        self.show_caption(type='VerticalCaption', title='하렌', desc='흑성회 제 3 간부', align=Align.Center | Align.Left, duration=3000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 카일(self.ctx)


class 카일(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4024], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=114, sequence_name='Bore_B')
        self.show_caption(type='VerticalCaption', title='카일', desc='흑성회 제 4 간부', align=Align.Center | Align.Right, duration=3000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 브리드민(self.ctx)


class 브리드민(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=115, sequence_name='Bore_B')
        self.show_caption(type='VerticalCaption', title='브리드 민', desc='흑성회 제 5 간부', align=Align.Center | Align.Left, duration=3000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 바사라첸(self.ctx)


class 바사라첸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4025], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=112, sequence_name='Bore_A')
        self.show_caption(type='VerticalCaption', title='바사라첸', desc='흑성회 제 2 간부', align=Align.Center | Align.Right, duration=3000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 웨이홍(self.ctx)


class 웨이홍(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4026], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=111, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003754, msg='여어~ $MyPCName$, 용케도 살아있었군.\\n정말 그 끈질긴 생명력은 칭찬하지 않을 수 없군 그래.', duration=4000)
        self.show_caption(type='VerticalCaption', title='웨이홍', desc='흑성회 보스', align=Align.Center | Align.Left, duration=3000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 흑성회와의동맹에대하여(self.ctx)


# 흑성회와 힘을 합치자고 말하는 라딘
class 흑성회와의동맹에대하여(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4029], return_view=False)
        self.face_emotion(emotion_name='defaultBattle')
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=0, msg='흑성회 놈들! 이번에야말로…!', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 흑성회와의동맹에대하여1_2(self.ctx)


class 흑성회와의동맹에대하여1_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4028], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='진정하게. 저들이 바로 내가 도움을 요청했다는 자들일세.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 흑성회와의동맹에대하여1_3(self.ctx)


class 흑성회와의동맹에대하여1_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4029], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Suprise_A'])
        self.add_cinematic_talk(npc_id=0, msg='<font size=\'40\'>!!! 뭐라고요?</font>', duration=2000)
        self.add_cinematic_talk(npc_id=0, msg='저들에게 도움을 요청하다니, 도대체 무슨 생각이신거죠!', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return 흑성회와의동맹에대하여2(self.ctx)


# 그래 그럽시다
class 흑성회와의동맹에대하여2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4026], return_view=False)
        self.add_cinematic_talk(npc_id=11003754, msg='제법 똑똑한 녀석인줄 알았는데 이제보니 영 머리가 안굴러 가는 녀석이군.\\n세상물정 모르는 꼬맹이같으니라고.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 흑성회와의동맹에대하여3(self.ctx)


class 흑성회와의동맹에대하여3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4028)
        self.add_cinematic_talk(npc_id=11003753, msg='$MyPCName$, 자네의 마음은 이해하네.\\n자네 말대로 흑성회는 신뢰할 수없는, 적이나 다름없는 이들이지.', duration=4000)
        self.add_cinematic_talk(npc_id=11003753, msg='그러나 지금은 냉정하게 판단할 때일세.\\n지금 우리는 자원도 부족하고 아무런 지원도 받을 수 없는 상황이네.', duration=4000)
        self.add_cinematic_talk(npc_id=11003753, msg='누군가의 힘을 빌려 수호군이 안전하게 크리티아스에 도착하고\\n어둠의 세력으로부터 이곳을 지켜낼 수만 있다면…', duration=4000)
        self.add_cinematic_talk(npc_id=11003753, msg='설령 그것이 흑성회라 할지라도 지금은 손을 잡아야 하지 않겠나?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return 흑성회와의동맹에대하여4(self.ctx)


class 흑성회와의동맹에대하여4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4029)
        self.add_cinematic_talk(npc_id=0, msg='……네, 알겠습니다.', duration=2000)
        self.add_cinematic_talk(npc_id=0, msg='하지만 언제 우리를 배신할지 모르는 자들이에요.\\n절대 경계를 늦춰서는 안될 겁니다.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 흑성회와의동맹에대하여5(self.ctx)


class 흑성회와의동맹에대하여5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4028)
        self.add_cinematic_talk(npc_id=11003753, msg='이해해줘서 고맙군.\\n그럼 웨이 홍, 약속한 정보는 가져왔나?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 정보전달하기(self.ctx)


# 웨이 홍의 정보 전달
class 정보전달하기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4026], return_view=False)
        self.add_cinematic_talk(npc_id=11003754, msg='뭐, 징징거리는 어린아이는 다 달랜 것 같으니…\\n본격적으로 거래를 시작해보자구.', duration=4000)
        self.add_cinematic_talk(npc_id=11003754, msg='선불을 하는 취미는 없지만 호의를 베풀어 먼저 알려주도록 하지.\\n의심많은 녀석의 입도 다물게 할겸. 후후.', duration=4000)
        self.add_cinematic_talk(npc_id=11003754, msg='일단 우리 쪽에서 입수한 정보에 따르면 크리티아스의 방어 시스템은\\n티아만 에너지 포트라는 곳에서 제어되고 있다고 한다.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 정보전달하기_02(self.ctx)


class 정보전달하기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4028], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='티아만 에너지 포트라…\\n내 기억이 맞다면 최신식 장비들을 연구, 생산해내는\\n크리티아스의 첨단 개발지역이었던 것으로 기억하네.', duration=5000)
        self.add_cinematic_talk(npc_id=11003753, msg='유학시절 방문해보고 싶었지만 크리티아스의 기술력이 집약된 장소라\\n외부인에게는 접근 자체가 불가능한 지역이었지.', duration=4000)
        self.add_cinematic_talk(npc_id=11003754, msg='왕족 나으리의 호사스런 유학 생활 이야기는 관심없고,\\n그곳을 장악하지 못하면 수호군 녀석들의 크리티아스 소풍은 포기해야할거야.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            return 정보전달하기_03(self.ctx)


class 정보전달하기_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4029], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='더 들을 필요도 없는 것 같군요.\\n서둘러 티아만 에너지 포트로 가서 방어 시스템을 무력화시키죠.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 정보전달하기_04(self.ctx)


class 정보전달하기_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4026], return_view=False)
        self.add_cinematic_talk(npc_id=11003754, msg='어이어이, 애송이. 서두르지 말라고?\\n아직 중요한 얘기가 하나 더 있으니깐 말이야.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 정보전달하기_05(self.ctx)


class 정보전달하기_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4028], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='티어스 코어에 대한건가?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 정보전달하기_06(self.ctx)


class 정보전달하기_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4026], return_view=False)
        self.add_cinematic_talk(npc_id=11003754, msg='크리티아스의 방어 시스템, 그리고 티어스 코어라는 물건에 대한 정보.\\n그게 거래조건이었으니 당연히 알아봤지.', duration=4000)
        self.add_cinematic_talk(npc_id=11003754, msg='그런데 그 티어스 코어라는 물건말이야…\\n정확하게 어디에 쓰는 것인지는 몰라도 보통 물건은 아닌 것 같더군.', duration=4000)
        self.add_cinematic_talk(npc_id=11003754, msg='헤카톤 왕이 직접 개발한 장치라는데 티마이온?\\n아무튼 무슨 거대 장치의 동력원으로 사용되었다고 하더군.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 정보전달하기2(self.ctx)


# 아르망을 찾아가보렴
class 정보전달하기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.add_balloon_talk(msg='!!!', duration=2000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=110, msg='!!!', duration=2000, delay_tick=1000)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Suprise_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 정보전달하기3(self.ctx)


class 정보전달하기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003753, msg='$MyPCName$… 생각보다 상황이 좋지 않을지도 모르겠군…', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='예… 녀석들이 티어스 코어를 노리는 것이 티마이온 때문이라면…', duration=3000)
        self.add_cinematic_talk(npc_id=11003753, msg='혹시 티어스 코어에 대한 정보는 그게 다인가? 어디에 있다던지 하는건…', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 정보전달하기3_1(self.ctx)


class 정보전달하기3_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4026], return_view=False)
        self.add_cinematic_talk(npc_id=11003754, msg='이봐 라딘 사장, 이것도 정말 어렵게 얻은 정보라고.\\n이 정도면 충분히 거래조건을 지킨 것 같은데?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 정보전달하기3_2(self.ctx)


class 정보전달하기3_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4007], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='알겠네. 잠시 $MyPCName$와 얘기 좀 할테니 기다려주게나.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 정보전달하기4(self.ctx)


class 정보전달하기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(trigger_id=702, type='trigger', achieve='MeetRadin')
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[112])
        self.destroy_monster(spawn_ids=[113])
        self.destroy_monster(spawn_ids=[114])
        self.destroy_monster(spawn_ids=[115])
        self.spawn_monster(spawn_ids=[117], auto_target=False) # 연출웨이홍
        self.spawn_monster(spawn_ids=[118], auto_target=False) # 연출브리드민
        self.spawn_monster(spawn_ids=[119], auto_target=False) # 연출바사라첸
        self.spawn_monster(spawn_ids=[120], auto_target=False) # 연출하렌
        self.spawn_monster(spawn_ids=[121], auto_target=False) # 연출카일

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111])
        self.destroy_monster(spawn_ids=[112])
        self.destroy_monster(spawn_ids=[113])
        self.destroy_monster(spawn_ids=[114])
        self.destroy_monster(spawn_ids=[115])
        self.spawn_monster(spawn_ids=[117], auto_target=False) # 연출웨이홍
        self.spawn_monster(spawn_ids=[118], auto_target=False) # 연출브리드민
        self.spawn_monster(spawn_ids=[119], auto_target=False) # 연출바사라첸
        self.spawn_monster(spawn_ids=[120], auto_target=False) # 연출하렌
        self.spawn_monster(spawn_ids=[121], auto_target=False) # 연출카일
        self.set_cinematic_ui(type=4)
        self.reset_camera()
        self.set_achievement(trigger_id=702, type='trigger', achieve='MeetRadin')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=7, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[110])


initial_state = idle2
