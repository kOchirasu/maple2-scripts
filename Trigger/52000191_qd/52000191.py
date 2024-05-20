""" trigger/52000191_qd/52000191.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6001]) # 마법진
        self.set_effect(trigger_ids=[6008]) # 마법진
        self.set_effect(trigger_ids=[6015]) # 마법진
        self.set_effect(trigger_ids=[6022]) # 마법진
        self.set_effect(trigger_ids=[6033]) # 마법진

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003412], quest_states=[1]):
            # 영웅의 그늘 퀘스트 수락
            return CameraEffect01(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000191, portal_id=5001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraEffect03_3(self.ctx)


class CameraEffect03_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3001')
        self.show_caption(type='VerticalCaption', title='$52000191_QD__52000191__0$', align=Align.Bottom | Align.Left, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 바론과첫만남_01(self.ctx)


class 바론과첫만남_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52000191_QD__52000191__1$', duration=5000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000191_QD__52000191__2$', align=Align.Left, illust_id='Baron_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 바론과첫만남_02(self.ctx)


class 바론과첫만남_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4005,4006], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=5000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000191_QD__52000191__3$', duration=5000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000191_QD__52000191__4$', align=Align.Left, illust_id='Baron_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 바론과첫만남_02_02(self.ctx)


class 바론과첫만남_02_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=5000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000191_QD__52000191__5$', duration=5000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000191_QD__52000191__6$', align=Align.Left, illust_id='Baron_normal', duration=4000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000191_QD__52000191__7$', align=Align.Left, illust_id='Baron_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=13000):
            return 바론과첫만남_03(self.ctx)


class 바론과첫만남_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Angry_A'])
        self.add_cinematic_talk(npc_id=0, msg='$52000191_QD__52000191__8$', duration=4000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000191_QD__52000191__9$', align=Align.Left, illust_id='Baron_normal', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 전투준비(self.ctx)


class 전투준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False) # 유저 투명 처리
        self.move_user(map_id=52000191, portal_id=5003)
        self.select_camera_path(path_ids=[4007,4008], return_view=False)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000191_QD__52000191__10$', duration=4000)
        self.set_effect(trigger_ids=[6029], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6030], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6031], visible=True) # 리젠 이펙트
        self.spawn_monster(spawn_ids=[101]) # 연출용 수하 생성
        self.spawn_monster(spawn_ids=[102]) # 연출용 수하 생성
        self.spawn_monster(spawn_ids=[103]) # 연출용 수하 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 전투준비_02(self.ctx)


class 전투준비_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투준비_03(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52000191, portal_id=5003)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 전투준비_03(self.ctx)


class 전투준비_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.visible_my_pc(is_visible=True) # 유저 투명 처리

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 페이즈1(self.ctx)


class 페이즈1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[6001], visible=True) # 마법진
        self.set_effect(trigger_ids=[6002], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6003], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6004], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6005], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6006], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6007], visible=True) # 리젠 이펙트
        self.spawn_monster(spawn_ids=[201]) # 수하 생성
        self.spawn_monster(spawn_ids=[202]) # 수하 생성
        self.spawn_monster(spawn_ids=[203]) # 수하 생성
        self.spawn_monster(spawn_ids=[204]) # 수하 생성
        self.spawn_monster(spawn_ids=[205]) # 수하 생성
        self.spawn_monster(spawn_ids=[206]) # 수하 생성
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203,204,205,206]):
            return 페이즈2(self.ctx)


class 페이즈2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004787, illust='Baron_normal', script='$52000191_QD__52000191__11$', duration=3000)
        self.set_effect(trigger_ids=[6001]) # 마법진
        self.set_effect(trigger_ids=[6015], visible=True) # 마법진
        self.set_effect(trigger_ids=[6016], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6017], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6018], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6019], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6020], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6021], visible=True) # 리젠 이펙트
        self.spawn_monster(spawn_ids=[213]) # 수하 생성
        self.spawn_monster(spawn_ids=[214]) # 수하 생성
        self.spawn_monster(spawn_ids=[215]) # 수하 생성
        self.spawn_monster(spawn_ids=[216]) # 수하 생성
        self.spawn_monster(spawn_ids=[217]) # 수하 생성
        self.spawn_monster(spawn_ids=[218]) # 수하 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[213,214,215,216,217,218]):
            return 페이즈3(self.ctx)


class 페이즈3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004787, illust='Baron_normal', script='$52000191_QD__52000191__12$', duration=3000)
        self.set_effect(trigger_ids=[6015]) # 마법진
        self.set_effect(trigger_ids=[6008], visible=True) # 마법진
        self.set_effect(trigger_ids=[6009], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6010], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6011], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6012], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6013], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6014], visible=True) # 리젠 이펙트
        self.spawn_monster(spawn_ids=[207]) # 수하 생성
        self.spawn_monster(spawn_ids=[208]) # 수하 생성
        self.spawn_monster(spawn_ids=[209]) # 수하 생성
        self.spawn_monster(spawn_ids=[210]) # 수하 생성
        self.spawn_monster(spawn_ids=[211]) # 수하 생성
        self.spawn_monster(spawn_ids=[212]) # 수하 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[207,208,209,210,211,212]):
            return 페이즈4(self.ctx)


class 페이즈4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004787, illust='Baron_normal', script='$52000191_QD__52000191__13$', duration=3000)
        self.set_effect(trigger_ids=[6008]) # 마법진
        self.set_effect(trigger_ids=[6022], visible=True) # 마법진
        self.set_effect(trigger_ids=[6023], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6024], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6025], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6026], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6027], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6028], visible=True) # 리젠 이펙트
        self.spawn_monster(spawn_ids=[219]) # 수하 생성
        self.spawn_monster(spawn_ids=[220]) # 수하 생성
        self.spawn_monster(spawn_ids=[221]) # 수하 생성
        self.spawn_monster(spawn_ids=[222]) # 수하 생성
        self.spawn_monster(spawn_ids=[223]) # 수하 생성
        self.spawn_monster(spawn_ids=[224]) # 수하 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[219,220,221,222,223,224]):
            return 페이즈5(self.ctx)


class 페이즈5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004787, illust='Baron_normal', script='$52000191_QD__52000191__14$', duration=3000)
        self.set_effect(trigger_ids=[6022]) # 마법진
        self.set_effect(trigger_ids=[6033], visible=True) # 마법진
        self.set_effect(trigger_ids=[6032], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6034], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6035], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6036], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6037], visible=True) # 리젠 이펙트
        self.set_effect(trigger_ids=[6038], visible=True) # 리젠 이펙트
        self.spawn_monster(spawn_ids=[225]) # 수하 생성
        self.spawn_monster(spawn_ids=[226]) # 수하 생성
        self.spawn_monster(spawn_ids=[227]) # 수하 생성
        self.spawn_monster(spawn_ids=[228]) # 수하 생성
        self.spawn_monster(spawn_ids=[229]) # 수하 생성
        self.spawn_monster(spawn_ids=[230]) # 수하 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[225,226,227,228,229,230]):
            return 고마해(self.ctx)


class 고마해(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 고마해_02(self.ctx)


class 고마해_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6033]) # 마법진
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.move_user(map_id=52000191, portal_id=5002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 고마해_03(self.ctx)


class 고마해_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 고마해_04(self.ctx)


class 고마해_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Attack_Idle_A', duration=5000.0)
        self.add_cinematic_talk(npc_id=0, msg='$52000191_QD__52000191__15$', duration=3000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000191_QD__52000191__16$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 고마해_05(self.ctx)


class 고마해_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011,4012], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='$52000191_QD__52000191__17$', duration=5000)
        self.add_cinematic_talk(npc_id=0, msg='$52000191_QD__52000191__18$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 고마해_06(self.ctx)


class 고마해_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013,4014], return_view=False)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000191_QD__52000191__19$', duration=4000)
        self.add_cinematic_talk(npc_id=11004787, msg='$52000191_QD__52000191__20$', duration=3000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 고마해_07(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 고마해_07(self.ctx)


class 고마해_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(trigger_id=2001, achieve='BattlewithBaron')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 그만싸워(self.ctx)


class 그만싸워(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = start
