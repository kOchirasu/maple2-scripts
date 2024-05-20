""" trigger/52020035_qd/main30000316.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 퀘스트 이후 라딘의 막사로 PC이동
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[30000315,30000316], quest_states=[2]):
            return 연출시작(self.ctx)


# PC를 숨기고 라딘 독백
class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4001], return_view=False) # 라딘

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작_02(self.ctx)


class 연출시작_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(is_visible=False)
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 연출라딘
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 연출연구원

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라딘이야기01(self.ctx)


# 라딘 이야기
class 라딘이야기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Skip01, action='exit')
        self.show_caption(type='VerticalCaption', title='라딘의 막사', desc='$MyPCName$$pp:가,이$ 떠난 직후', align=Align.Center | Align.Left, duration=4000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 라딘이야기01_01(self.ctx)


class 라딘이야기01_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Bore_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=11003750, msg='…이런 일이 있었다고 합니다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 라딘이야기01_02(self.ctx)


class 라딘이야기01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='흠… 크리티아스가 다시 나타난 것은 어둠의 세력과 관련이 있을지도 모르겠군…', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 라딘이야기01_03(self.ctx)


class 라딘이야기01_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003753, msg='그렇다는 것은 확실히 이곳에 중요한 무언가가 있다는 얘기겠지.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 라딘이야기01_04(self.ctx)


class 라딘이야기01_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False) # 라딘
        self.add_cinematic_talk(npc_id=11003753, msg='수고했네. 덕분에 중요한 정보를 얻게 되었군.', duration=4000)
        self.add_cinematic_talk(npc_id=11003750, msg='이런 상황을 예측하신 라딘님께서 미리 지시해주신 덕분입니다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 라딘이야기02(self.ctx)


class 라딘이야기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=4000.0)
        self.add_cinematic_talk(npc_id=11003753, msg='가질, 아무래도 그 자들과 다시 한번 거래를 해야할 것 같으니 연락 좀 해주게.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 라딘이야기02_01(self.ctx)


class 라딘이야기02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4015], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='ChatUP_A')
        self.add_cinematic_talk(npc_id=11003750, msg='그 자들이라면… 설마 흑성회 녀석들과 다시 거래하실 생각이신겁니까?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 라딘이야기02_02(self.ctx)


class 라딘이야기02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='분명 신뢰할 수 없는 자들이지만 아직은 이용할 가치가 있어.\\n원하는 것을 손에 넣을때까지는 장단을 맞춰줘야지.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 라딘이야기02_03(self.ctx)


class 라딘이야기02_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4016], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='짓밟아버리는 것은 그 이후에 해도 늦지 않아.', duration=3000)
        self.set_npc_emotion_sequence(spawn_id=102, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003750, msg='넵, 분부대로 하겠습니다.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 화면암전(self.ctx)


# 장면 전환
class 화면암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 흑성회입장전(self.ctx)


class 흑성회입장전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 흑성회등장직전(self.ctx)


class 흑성회등장직전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='잠시 후, 라딘의 막사')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 흑성회입장(self.ctx)


class 흑성회입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[116], auto_target=False) # 바사라첸
        self.spawn_monster(spawn_ids=[109], auto_target=False) # 브리드민
        self.spawn_monster(spawn_ids=[104], auto_target=False) # 웨이홍
        self.spawn_monster(spawn_ids=[103], auto_target=False) # 연출라딘
        self.spawn_monster(spawn_ids=[122], auto_target=False) # 흑성회 대원1
        self.spawn_monster(spawn_ids=[123], auto_target=False) # 흑성회 대원2

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 흑성회입장_02(self.ctx)


class 흑성회입장_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4032], return_view=False) # 흑성회 브리드민, 바라세첸 쪽
        self.add_cinematic_talk(npc_id=11003754, msg='이런곳까지 불러내다니... 다시봤구만, 나으리.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 손님맞이(self.ctx)


"""
흑성회와 대화
앞으로의 계획 이야기
"""
class 손님맞이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=109, patrol_name='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 손님맞이_01(self.ctx)


class 손님맞이_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.add_cinematic_talk(npc_id=11003758, msg='이곳이 바로 역사에서 사라졌던 크리티아스…\\n빨리 구경해보고 싶어요!', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 손님맞이_01_01(self.ctx)


class 손님맞이_01_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=116, patrol_name='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 손님맞이_02(self.ctx)


class 손님맞이_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4033], return_view=False)
        self.add_cinematic_talk(npc_id=11003757, msg='우린 여기 놀러온게 아니야.\\n흑성회의 간부답게 행동해라.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 손님맞이_03(self.ctx)


class 손님맞이_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4017], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 손님맞이_03_01(self.ctx)


class 손님맞이_03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=109, rotation=90.0)
        self.set_npc_emotion_sequence(spawn_id=109, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003758, msg='형… 알았어요.\\n대신 일이 끝나면 꼭 같이…', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 흑성회와이야기시작01_1(self.ctx)


class 흑성회와이야기시작01_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4020], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='하하, 흑성회가 자랑하는 천재 전략가가 이런 어린 소년일줄이야.\\n과연 웨이 홍이 자랑할만하군.', duration=3000)
        self.set_npc_rotation(spawn_id=109, rotation=-360.0) # 브리드민 원래대로

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 흑성회와이야기시작02(self.ctx)


class 흑성회와이야기시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4018], return_view=False) # 흑성회 브리드민 쪽
        self.set_npc_emotion_sequence(spawn_id=109, sequence_name='Bore_B')
        self.add_cinematic_talk(npc_id=11003758, msg='칭찬해주셔서 감사합니다. 당신이 바로 라딘님이시군요.\\n과거 트라이아의 검은 사자라고 불리웠던 제1왕위계승자…', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 흑성회와이야기시작02_01(self.ctx)


class 흑성회와이야기시작02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=116, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003757, msg='민, 상대의 도발에 일일이 반응하지마라.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 흑성회와이야기시작02_02(self.ctx)


class 흑성회와이야기시작02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4020], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='이런, 거기에 루델리 아레나 최강의 챔피언 바사라 첸이라니.\\n이런 귀빈들이 올 줄 알았다면 좀 더 손님맞이를 잘 준비했을텐데.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 흑성회와이야기시작03(self.ctx)


class 흑성회와이야기시작03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False) # 흑성회 웨이홍 쪽으로 돌진
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003754, msg='능구렁이 같은 모습은 여전하시군. 그 덕에 이번에 뒷통수를 거하게 맞았지.', duration=4000)
        self.add_cinematic_talk(npc_id=11003754, msg='거기에 황송하게도 갑작스러운 초대라니…\\n이번엔 또 어떤 기가막힌 선물을 주실지 몰라 흑성회의 간부들을 모두 소집했지.', duration=5000)
        self.add_cinematic_talk(npc_id=11003754, msg='그나저나 내가 당신을 너무 높게 평가했던 것 같군.\\n천하의 라딘 비드블라임님께서 먼저 꼬리를 말고 기어올 줄이야.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=14000):
            return 흑성회와이야기시작03_01(self.ctx)


class 흑성회와이야기시작03_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4023], return_view=False)
        self.add_cinematic_talk(npc_id=11003754, msg='도대체 무슨 꿍꿍이 속인거지?', duration=3000)
        self.destroy_monster(spawn_ids=[109])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 흑성회와이야기시작04(self.ctx)


class 흑성회와이야기시작04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False) # 라딘과 웨이홍
        self.add_cinematic_talk(npc_id=11003753, msg='자네의 그 경박한 언사는 도저히 고칠 수가 없나 보군.', duration=3000)
        self.add_cinematic_talk(npc_id=11003753, msg='아무튼 더 큰 일을 위해서라면 사소한 오해 정도는 아량을 베풀 수 있는 법이니…\\n지난 일은 조용히 넘어가주도록 하겠네.', duration=5000)
        self.add_cinematic_talk(npc_id=11003753, msg='이제라도 제대로 손을 잡고 일 해보는 게 어떤가?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return 흑성회와이야기시작04_라딘과웨이홍(self.ctx)


class 흑성회와이야기시작04_라딘과웨이홍(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4021], return_view=False)
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Talk_A', duration=5000.0)
        self.add_cinematic_talk(npc_id=11003754, msg='장사 한 두 번 하는 것도 아니고, 그런 말에 내가 속아 넘어갈 것으로 보이시나 보지?\\n두 번이나 당할 정도로 이 웨이 홍이 어리석진 않은데 말이야.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 흑성회와이야기시작04_라딘과웨이홍_02(self.ctx)


class 흑성회와이야기시작04_라딘과웨이홍_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4020], return_view=False)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=18000.0)
        self.add_cinematic_talk(npc_id=11003753, msg='자네의 리소스를 활용하여 우리 연구원들의 안전한 자료 수집 및 조사를 지원한다.', duration=4000)
        self.add_cinematic_talk(npc_id=11003753, msg='그리고 이를 통해 나는 사라졌던 크리티아스의 기술력을 손에 넣고\\n자네는 우리가 개발할 최첨단 장비들을 제공받는다.', duration=5000)
        self.add_cinematic_talk(npc_id=11003753, msg='난 이게 우리의 계약이었던 것으로 기억하네만…\\n계약을 어기고 멋대로 이오네 왕녀를 추적한 것은 자네가 먼저였던 것 같은데?', duration=5000)
        self.add_cinematic_talk(npc_id=11003753, msg='그 덕에 $MyPCName$ 녀석이 일을 이 모양으로 망쳐놓았고 말이야.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=17000):
            return 흑성회와이야기시작04_라딘과웨이홍_03(self.ctx)


class 흑성회와이야기시작04_라딘과웨이홍_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4021], return_view=False)
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Talk_A', duration=10000.0)
        self.add_balloon_talk(spawn_id=123, msg='건방진..', duration=3000)
        self.add_balloon_talk(spawn_id=122, msg='감히!', duration=3000)
        self.add_cinematic_talk(npc_id=11003754, msg='흥, 기술력을 손에 넣고나면 순순히 약속을 지킬 정도로\\n당신이 믿음직한 사람인줄 아나?', duration=4000)
        self.add_cinematic_talk(npc_id=11003754, msg='우리 입장에서도 보험 하나 정도는 있어야 하는게 당연하지 않나?\\n게다가 그 여자가 당신의 말대로 정말 크리티아스의 왕녀라는 보장도 없고 말이야.', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 흑성회와이야기시작04_라딘과웨이홍_04(self.ctx)


class 흑성회와이야기시작04_라딘과웨이홍_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4020], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003753, msg='훗, 이거이거 내가 이 정도로 신용도가 없는 사람인가 보군.', duration=3000)
        self.add_cinematic_talk(npc_id=11003753, msg='그녀가 이오네 왕녀라는 중요한 정보를 자네에게 공유해줄만큼\\n난 우리 사이에 어느 정도 신뢰가 있다고 생각했는데 말이야.', duration=5000)
        self.add_cinematic_talk(npc_id=11003753, msg='게다가 내가 손을 쓰지 않았다면 벌써 이곳은 이미 수호군의 손아귀에 넘어갔을 걸세.\\n이 정도면 나를 믿어줄 이유는 충분하다고 보는데, 어떤가?', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return 흑성회와이야기시작04_라딘과웨이홍_05(self.ctx)


class 흑성회와이야기시작04_라딘과웨이홍_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4021], return_view=False)
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Talk_A', duration=7000.0)
        self.add_cinematic_talk(npc_id=11003754, msg='오호~ 그러신가?', duration=2000)
        self.add_cinematic_talk(npc_id=11003754, msg='$MyPCName$ 녀석 하나 제대로 못 막아준 덕분에\\n공들여 키운 장기말을 써먹을 수가 없는 상황이 되었는데?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 흑성회와이야기시작04_라딘과웨이홍_06(self.ctx)


class 흑성회와이야기시작04_라딘과웨이홍_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4020], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='진정하고 크게 생각하세나.\\n이렇게 서로 싸우기만 하다간 우리 모두 아무런 이득을 보지 못할걸세.', duration=4000)
        self.add_cinematic_talk(npc_id=11003753, msg='난 지금 무조건적으로 나를 믿어달라는게 아니야.\\n그저 원하는 것을 손에 넣기 위해 서로 돕자는 것이지.', duration=4000)
        self.add_cinematic_talk(npc_id=11003753, msg='애당초 자네나 나나 이곳에 원하는 것이 있어서 함께 손을 잡았던 것 아닌가?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 흑성회와이야기시작04_라딘과웨이홍_07(self.ctx)


class 흑성회와이야기시작04_라딘과웨이홍_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4021], return_view=False)
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Talk_A', duration=8000.0)
        self.add_cinematic_talk(npc_id=11003754, msg='서로 언제 뒤통수를 칠 지 모르는데도 어쩔 수 없는 동맹이라…\\n크큭. 왕족 나리께서 제법 모험도 하시는군.', duration=4000)
        self.add_cinematic_talk(npc_id=11003754, msg='좋소. 어디 원하는 바를 말해보시지 그래.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 흑성회와이야기시작04_라딘과웨이홍_08(self.ctx)


class 흑성회와이야기시작04_라딘과웨이홍_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4022], return_view=False)
        self.add_cinematic_talk(npc_id=11003753, msg='훗, 이제서야 말이 통하는군.', duration=2000)
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003753, msg='그럼, 계획에 대해서 이야기해 보도록 하지…', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 흑성회와이야기시작04_1(self.ctx)


class 흑성회와이야기시작04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 장면전환(self.ctx)


# 장면 전환
class 장면전환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 장면전환_02(self.ctx)


class 장면전환_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='MeetRadin')
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])
        self.destroy_monster(spawn_ids=[109])
        self.destroy_monster(spawn_ids=[122])
        self.destroy_monster(spawn_ids=[123])
        self.destroy_monster(spawn_ids=[116])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마을로이동(self.ctx)


class Skip01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_achievement(trigger_id=701, type='trigger', achieve='MeetRadin')
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])
        self.destroy_monster(spawn_ids=[109])
        self.destroy_monster(spawn_ids=[122])
        self.destroy_monster(spawn_ids=[123])
        self.destroy_monster(spawn_ids=[116])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 마을로이동(self.ctx)


# 티마이오스로 내보내기
class 마을로이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.reset_camera()
        self.visible_my_pc(is_visible=True)
        self.move_user(map_id=2020014, portal_id=4)


initial_state = idle
