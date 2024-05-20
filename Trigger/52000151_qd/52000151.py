""" trigger/52000151_qd/52000151.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# ########################씬7 파토스의 등장########################
class wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001642], quest_states=[1]):
            # C퀘스트가 진행 상태 일때
            return 생명의틈으로01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001641], quest_states=[3]):
            # 퀘스트 감지 조건 추가
            return 생틈퀘수령전대기(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001641], quest_states=[2]):
            # 퀘스트 감지 조건 추가
            return 생틈퀘수령전대기(self.ctx)
        """
        if self.user_detected(box_ids=[10010]):
            return 파토스등장연출01(self.ctx)
        """
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001641], quest_states=[1]):
            # 퀘스트 감지 조건 추가
            return 파토스등장연출01(self.ctx)


class wait_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10010]):
            return 파토스등장연출01(self.ctx)


class 생틈퀘수령전대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=False) # 케이틀린
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 아노스
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 호르헤
        self.set_npc_emotion_loop(spawn_id=200, sequence_name='Event_01_A', duration=999999.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001642], quest_states=[1]):
            # C퀘스트가 진행 상태 일때
            return 생명의틈으로01(self.ctx)


class 파토스등장연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.spawn_monster(spawn_ids=[202], auto_target=False) # 케이틀린
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 아노스
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 호르헤
        self.spawn_monster(spawn_ids=[203], auto_target=False) # 파토스
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Stun_A', duration=999999.0)
        self.face_emotion(spawn_id=201, emotion_name='Concerned')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 파토스등장연출02(self.ctx)


class 파토스등장연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='exit')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 파토스등장연출02_B(self.ctx)


class 파토스등장연출02_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[3000,3001], return_view=False)
        self.set_effect(trigger_ids=[1100,1101,1102,1103,1104,1105,1106,1107], visible=True, interval=100)
        self.set_effect(trigger_ids=[1200,1201,1202,1203,1204,1205,1206], visible=True, interval=100)
        self.set_effect(trigger_ids=[1300,1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311], visible=True, interval=100)
        self.set_effect(trigger_ids=[1400,1401,1402,1403,1404,1405,1406,1407,1408,1409], visible=True, interval=100)
        self.set_effect(trigger_ids=[1500,1501,1502,1503,1504,1505,1506,1507,1508], visible=True, interval=100)
        self.set_effect(trigger_ids=[1600,1601,1602,1603,1604,1605,1606,1607,1608], visible=True, interval=100)
        self.set_effect(trigger_ids=[1700,1701,1702,1703,1704], visible=True, interval=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출03(self.ctx)


class 파토스등장연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003439, illust_id='0', msg='$52000151_QD__52000151__0$', duration=4000, align=Align.Right) # 호르헤 대사
        self.select_camera_path(path_ids=[7000,7001], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_B') # 호르헤
        # 도대체 이건…무슨 일이죠…?!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출04(self.ctx)


class 파토스등장연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003442, illust_id='0', msg='$52000151_QD__52000151__1$', duration=4000, align=Align.Right) # 케이틀린 대사
        self.select_camera_path(path_ids=[7002,7003], return_view=False) # 아노스 선생님이 두명…?!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출05(self.ctx)


class 파토스등장연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__2$', duration=4000, align=Align.Right) # 파토스 대사
        self.select_camera_path(path_ids=[7004,7005], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Bore_A') # 파토스
        # 파토스다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출06(self.ctx)


class 파토스등장연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__3$', duration=4000, align=Align.Right) # 파토스 대사
        self.select_camera_path(path_ids=[7006,7007], return_view=False)
        # 내 이름은 파토스. 빛의 이노센트 따위와 이름을 섞고 싶지 않군.
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_patos_come')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출08(self.ctx)


class 파토스등장연출08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__4$', duration=4000, align=Align.Right) # 파토스 대사
        # 난 어둠의 이노센트다. 그래, 빛의 위선을 뚫고 나온 이 세상의 진정한 힘이지…
        self.select_camera_path(path_ids=[7008,7009], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출09(self.ctx)


class 파토스등장연출09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003442, illust_id='0', msg='$52000151_QD__52000151__5$', duration=4000, align=Align.Right) # 파토스 대사
        self.select_camera_path(path_ids=[7010,7011], return_view=False) # 어둠의…이노센트?!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출10(self.ctx)


class 파토스등장연출10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003439, illust_id='0', msg='$52000151_QD__52000151__6$', duration=4000, align=Align.Right) # 호르헤 대사
        self.select_camera_path(path_ids=[7000,7001], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_A') # 호르헤
        # 가설이 맞았군…아노스 선생은 역시 고대의 이노센트였다…

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출12(self.ctx)


class 파토스등장연출12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003439, illust_id='0', msg='$52000151_QD__52000151__7$', duration=4000, align=Align.Right) # 호르헤 대사
        # 하지만 어둠의 이노센트라니…이노센트는 하나가 아니었나…?
        self.select_camera_path(path_ids=[7012,7013,7014,7015], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출13(self.ctx)


class 파토스등장연출13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__8$', duration=4000, align=Align.Right) # 파토스 대사
        self.select_camera_path(path_ids=[7016,7017], return_view=False) # 훗…하나?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 파토스등장연출14(self.ctx)


class 파토스등장연출14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__9$', duration=4000, align=Align.Right) # 파토스 대사
        # 숫자놀이를 할 만큼 여유롭지 않지만,조금은 어울려 주도록 하지.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 파토스등장연출15(self.ctx)


class 파토스등장연출15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__10$', duration=4000, align=Align.Right) # 파토스 대사
        self.select_camera_path(path_ids=[7018,7019], return_view=False) # 우린 하나가 아니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 파토스등장연출16(self.ctx)


class 파토스등장연출16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__11$', duration=4000, align=Align.Right) # 파토스 대사
        # 저 녀석은 저 녀석.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 파토스등장연출17(self.ctx)


class 파토스등장연출17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__12$', duration=4000, align=Align.Right) # 파토스 대사
        # 나 파토스는 파토스일 뿐.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 파토스등장연출18(self.ctx)


class 파토스등장연출18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__13$', duration=4000, align=Align.Right) # 파토스 대사
        # 뭐…그것도 잠시 일 테지.생명의 틈만 있다면, 빛의 이노센트도 내 몸이 될 것이다.
        self.select_camera_path(path_ids=[7020,7021], return_view=False)
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_patos_exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 파토스등장연출19(self.ctx)


class 파토스등장연출19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__14$', duration=4000, align=Align.Right) # 파토스 대사
        self.select_camera_path(path_ids=[7022,7023], return_view=False)
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_patos_turn') # 크큭…빛의 이노센트여.날 거부하지 마라.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출20(self.ctx)


class 파토스등장연출20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003441, illust_id='0', msg='$52000151_QD__52000151__15$', duration=4000, align=Align.Right) # 케이틀린 대사
        self.select_camera_path(path_ids=[7024,7025], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Attack_01_A') # 파토스
        # 네 모든 건…모두 내 것이다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출21(self.ctx)


class 파토스등장연출21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 파토스 사라지는 이펙트
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 파토스등장연출22(self.ctx)


class 파토스등장연출22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_anosTurn')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 파토스등장연출23(self.ctx)


class 파토스등장연출23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_achievement(trigger_id=10010, type='trigger', achieve='ProtectFinish') # 50001641 퀘스트 완료 업적
        self.set_npc_emotion_loop(spawn_id=200, sequence_name='Event_01_A', duration=999999.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.set_sound(trigger_id=9000, enable=True) # 전투 상황 브금
        self.destroy_monster(spawn_ids=[203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001642], quest_states=[1]):
            # C퀘스트가 진행 상태 일때
            return 생명의틈으로01(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_npc_emotion_loop(spawn_id=200, sequence_name='Event_01_A', duration=999999.0)
        self.reset_camera()
        self.set_sound(trigger_id=9000, enable=True) # 전투 상황 브금
        self.destroy_monster(spawn_ids=[203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Skip_1_1(self.ctx)


class Skip_1_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=10010, type='trigger', achieve='ProtectFinish') # 50001641 퀘스트 완료 업적

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001642], quest_states=[1]):
            # C퀘스트가 진행 상태 일때
            return 생명의틈으로01(self.ctx)


class 생명의틈으로01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000172, portal_id=21002)


initial_state = wait
