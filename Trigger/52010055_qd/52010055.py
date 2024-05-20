""" trigger/52010055_qd/52010055.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[500])
        self.set_effect(trigger_ids=[501])
        self.set_effect(trigger_ids=[502])
        self.remove_buff(box_id=9002, skill_id=99910311) # 포탑으로변신
        self.destroy_monster(spawn_ids=[-1])
        self.visible_my_pc(is_visible=False) # 캐릭터 숨김

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9002]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_mesh(trigger_ids=[10000], visible=True) # 스폰 발판 생성
        self.set_mesh(trigger_ids=[10001], visible=True) # 공습용발판 생성
        self.set_mesh(trigger_ids=[30000], visible=True) # 대포1 생성
        self.set_mesh(trigger_ids=[30001], visible=True) # 대포1 생성
        self.set_mesh(trigger_ids=[30002], visible=True) # 대포1 생성
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[1], auto_target=False) # 함교 연출용 블리체
        self.spawn_monster(spawn_ids=[2], auto_target=False) # 함교 연출용 네이린
        self.spawn_monster(spawn_ids=[3], auto_target=False) # 함교 연출용 콘대르
        self.spawn_monster(spawn_ids=[4], auto_target=False) # 함교 연출용 메이슨
        self.spawn_monster(spawn_ids=[5], auto_target=False) # 함교 연출용 샤텐
        self.spawn_monster(spawn_ids=[10000], auto_target=False) # 함교 연출용 해군
        self.spawn_monster(spawn_ids=[10001], auto_target=False) # 함교 연출용 해군
        self.spawn_monster(spawn_ids=[10002], auto_target=False) # 함교 연출용 해군
        self.spawn_monster(spawn_ids=[100], auto_target=False)
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
        self.spawn_monster(spawn_ids=[114], auto_target=False)
        self.spawn_monster(spawn_ids=[115], auto_target=False)
        self.spawn_monster(spawn_ids=[116], auto_target=False)
        self.spawn_monster(spawn_ids=[117], auto_target=False)
        self.spawn_monster(spawn_ids=[118], auto_target=False)
        self.spawn_monster(spawn_ids=[119], auto_target=False)
        self.spawn_monster(spawn_ids=[120], auto_target=False)
        self.spawn_monster(spawn_ids=[121], auto_target=False)
        self.spawn_monster(spawn_ids=[122], auto_target=False)
        self.spawn_monster(spawn_ids=[123], auto_target=False)
        self.move_user(map_id=52010055, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크림슨발록비춤1(self.ctx)


class 크림슨발록비춤1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_mesh(trigger_ids=[10000]) # 스폰 발판 지움
        self.set_mesh(trigger_ids=[10001]) # 공습용발판 지움
        self.set_scene_skip(state=게임시작, action='nextState')
        self.select_camera(trigger_id=4001)
        self.add_cinematic_talk(npc_id=11003781, msg='$52010055_QD__52010055__0$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11003781, msg='$52010055_QD__52010055__1$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 크림슨이동(self.ctx)


class 크림슨이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=29000378, msg='$52010055_QD__52010055__2$', duration=3000, align=Align.Right)
        self.move_npc(spawn_id=101, patrol_name='PatrolDataBalrog_Open_101')
        self.move_npc(spawn_id=102, patrol_name='PatrolDataBalrog_Open_102')
        self.move_npc(spawn_id=103, patrol_name='PatrolDataBalrog_Open_103')
        self.move_npc(spawn_id=104, patrol_name='PatrolDataBalrog_Open_104')
        self.move_npc(spawn_id=105, patrol_name='PatrolDataBalrog_Open_105')
        self.move_npc(spawn_id=106, patrol_name='PatrolDataBalrog_Open_106')
        self.move_npc(spawn_id=107, patrol_name='PatrolDataBalrog_Open_107')
        self.move_npc(spawn_id=108, patrol_name='PatrolDataBalrog_Open_108')
        self.move_npc(spawn_id=109, patrol_name='PatrolDataBalrog_Open_109')
        self.move_npc(spawn_id=110, patrol_name='PatrolDataBalrog_Open_110')
        self.move_npc(spawn_id=111, patrol_name='PatrolDataBalrog_Open_111')
        self.move_npc(spawn_id=112, patrol_name='PatrolDataBalrog_Open_112')
        self.move_npc(spawn_id=113, patrol_name='PatrolDataBalrog_Open_113')
        self.move_npc(spawn_id=114, patrol_name='PatrolDataBalrog_Open_114')
        self.move_npc(spawn_id=115, patrol_name='PatrolDataBalrog_Open_115')
        self.move_npc(spawn_id=116, patrol_name='PatrolDataBalrog_Open_116')
        self.move_npc(spawn_id=117, patrol_name='PatrolDataBalrog_Open_117')
        self.move_npc(spawn_id=118, patrol_name='PatrolDataBalrog_Open_118')
        self.move_npc(spawn_id=119, patrol_name='PatrolDataBalrog_Open_119')
        self.move_npc(spawn_id=120, patrol_name='PatrolDataBalrog_Open_120')
        self.move_npc(spawn_id=121, patrol_name='PatrolDataBalrog_Open_121')
        self.move_npc(spawn_id=122, patrol_name='PatrolDataBalrog_Open_122')
        self.move_npc(spawn_id=123, patrol_name='PatrolDataBalrog_Open_123')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 함교비춤1(self.ctx)


class 함교비춤1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123])
        self.visible_my_pc(is_visible=True) # 캐릭터 보임
        self.move_user(map_id=52010055, portal_id=2)
        self.select_camera_path(path_ids=[4002,4003], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=2, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003536, illust_id='Neirin_surprise', msg='$52010055_QD__52010055__3$', duration=3000, align=Align.Left)
        self.add_cinematic_talk(npc_id=11003682, illust_id='Bliche_closeEye', msg='$52010055_QD__52010055__4$', duration=4000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 함교비춤2(self.ctx)


class 함교비춤2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=1, rotation=180.0)
        self.set_npc_emotion_sequence(spawn_id=1, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010055_QD__52010055__5$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 콘대르대사(self.ctx)


class 콘대르대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=3, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003776, illust_id='Conder_normal', msg='$52010055_QD__52010055__6$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 콘대르이동(self.ctx)


class 콘대르이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=3, patrol_name='PatrolDataOpenConder0')
        self.set_npc_emotion_sequence(spawn_id=5, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003584, illust_id='Schatten_normal', msg='$52010055_QD__52010055__7$', duration=2000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 샤텐이동(self.ctx)


class 샤텐이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=5, patrol_name='PatrolDataOpenSchatten0')
        self.set_npc_emotion_sequence(spawn_id=4, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003586, illust_id='Mason_closeEye', msg='$52010055_QD__52010055__8$', duration=3000, align=Align.Left)
        self.destroy_monster(spawn_ids=[3])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 메이슨이동(self.ctx)


class 메이슨이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5])
        self.move_npc(spawn_id=4, patrol_name='PatrolDataOpenMason0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 함교비춤3(self.ctx)


class 함교비춤3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=1, rotation=270.0)
        self.set_npc_emotion_sequence(spawn_id=1, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010055_QD__52010055__9$', duration=3000, align=Align.Right)
        self.destroy_monster(spawn_ids=[4])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 함교비춤4(self.ctx)


class 함교비춤4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=2, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003536, illust_id='Neirin_surprise', msg='$52010055_QD__52010055__10$', duration=2000, align=Align.Left)
        self.set_npc_emotion_sequence(spawn_id=1, sequence_name='Talk_A')
        self.set_npc_rotation(spawn_id=1, rotation=170.0)
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010055_QD__52010055__11$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 함교비춤5(self.ctx)


class 함교비춤5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Calm_A'])
        self.init_npc_rotation(spawn_ids=[1])
        self.set_npc_emotion_sequence(spawn_id=1, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010055_QD__52010055__12$', duration=3000, align=Align.Left)
        self.set_npc_emotion_sequence(spawn_id=2, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003536, illust_id='Neirin_surprise', msg='$52010055_QD__52010055__13$', duration=3000, align=Align.Right)
        self.set_npc_emotion_sequence(spawn_id=1, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010055_QD__52010055__14$', duration=2000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11003682, illust_id='Bliche_closeEye', msg='$52010055_QD__52010055__15$', duration=2000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010055_QD__52010055__16$', duration=2000, align=Align.Right)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 게임시작(self.ctx)


class 게임시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10002,10003,10004,10005], visible=True) # 1차 전투 링
        self.select_camera_path(path_ids=[4003,4019], return_view=False)
        self.visible_my_pc(is_visible=True) # 캐릭터 보임
        self.reset_camera()
        self.move_user(map_id=52010055, portal_id=3)
        self.set_local_camera(camera_id=9009, enable=True)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.side_npc_talk(npc_id=11003533, illust='Bliche_closeEye', duration=3000, script='$52010055_QD__52010055__17$', voice='ko/Npc/00002154')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차발록스피어스폰1(self.ctx)


class 차발록스피어스폰1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4019)
        self.set_mesh(trigger_ids=[10000]) # 스폰 발판 제거
        self.spawn_monster(spawn_ids=[1], auto_target=False) # 함교 연출용 블리체
        self.spawn_monster(spawn_ids=[2], auto_target=False) # 함교 연출용 네이린
        self.spawn_monster(spawn_ids=[10000], auto_target=False) # 함교 연출용 해군
        self.spawn_monster(spawn_ids=[10001], auto_target=False) # 함교 연출용 해군
        self.spawn_monster(spawn_ids=[10002], auto_target=False) # 함교 연출용 해군
        self.spawn_monster(spawn_ids=[1000], auto_target=False)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1002], auto_target=False)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1000,1001,1002,1003,1004]):
            return 차발록스피어스폰2(self.ctx)


class 차발록스피어스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)
        self.spawn_monster(spawn_ids=[1009], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1005,1006,1007,1008,1009]):
            return 차발록스피어스폰3(self.ctx)


class 차발록스피어스폰3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1010], auto_target=False)
        self.spawn_monster(spawn_ids=[1011], auto_target=False)
        self.spawn_monster(spawn_ids=[1012], auto_target=False)
        self.spawn_monster(spawn_ids=[1013], auto_target=False)
        self.spawn_monster(spawn_ids=[1014], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1010,1011,1012,1013,1014]):
            return 차크림슨스폰1(self.ctx)


class 차크림슨스폰1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200], auto_target=False)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.spawn_monster(spawn_ids=[203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[200,201,202,203]):
            return 차크림슨스폰2(self.ctx)


class 차크림슨스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[204], auto_target=False)
        self.spawn_monster(spawn_ids=[205], auto_target=False)
        self.spawn_monster(spawn_ids=[206], auto_target=False)
        self.spawn_monster(spawn_ids=[207], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[204,205,206,207]):
            return 차크림슨스폰3(self.ctx)


class 차크림슨스폰3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.spawn_monster(spawn_ids=[1006], auto_target=False)
        self.spawn_monster(spawn_ids=[1007], auto_target=False)
        self.spawn_monster(spawn_ids=[1008], auto_target=False)
        self.spawn_monster(spawn_ids=[1009], auto_target=False)
        self.spawn_monster(spawn_ids=[209], auto_target=False)
        self.spawn_monster(spawn_ids=[210], auto_target=False)
        self.spawn_monster(spawn_ids=[211], auto_target=False)
        self.spawn_monster(spawn_ids=[212], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1005,1006,1007,1008,1009,209,210,211,212]):
            return 차크림슨스폰4(self.ctx)


class 차크림슨스폰4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1010], auto_target=False)
        self.spawn_monster(spawn_ids=[1011], auto_target=False)
        self.spawn_monster(spawn_ids=[1012], auto_target=False)
        self.spawn_monster(spawn_ids=[1013], auto_target=False)
        self.spawn_monster(spawn_ids=[1014], auto_target=False)
        self.spawn_monster(spawn_ids=[213], auto_target=False)
        self.spawn_monster(spawn_ids=[214], auto_target=False)
        self.spawn_monster(spawn_ids=[215], auto_target=False)
        self.spawn_monster(spawn_ids=[216], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1010,1011,1012,1013,1014,213,214,215,216]):
            return 보스전연출준비(self.ctx)


"""
class 공습준비대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=4000, script='$52010055_QD__52010055__18$')
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=3000, script='$52010055_QD__52010055__19$')
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=3000, script='$52010055_QD__52010055__20$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 공습준비연출2(self.ctx)
"""

"""
class 공습준비연출1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.destroy_monster(spawn_ids=[-1])
        self.set_mesh(trigger_ids=[10002,10003,10004,10005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 공습준비연출2(self.ctx)
"""

"""
class 공습준비연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[999], auto_target=False)
        self.select_camera_path(path_ids=[4020,4021,4022], return_view=False)
        self.move_user(map_id=52010055, portal_id=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 공습준비연출3(self.ctx)
"""

"""
class 공습준비연출3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='PatrolDataCannon')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 공습준비연출4(self.ctx)
"""

"""
class 공습준비연출4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52010055, portal_id=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 공습준비(self.ctx)
"""

"""
class 공습준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[30000])
        self.add_buff(box_ids=[9002], skill_id=99910311, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 공습1(self.ctx)
"""

"""
class 공습1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.spawn_monster(spawn_ids=[600], auto_target=False)
        self.spawn_monster(spawn_ids=[601], auto_target=False)
        self.spawn_monster(spawn_ids=[602], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 공습1이동(self.ctx)
"""

"""
class 공습1이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=600, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=601, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=602, patrol_name='PatrolDataBridge0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 공습2(self.ctx)
"""

"""
class 공습2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[500])
        self.spawn_monster(spawn_ids=[501])
        self.spawn_monster(spawn_ids=[502])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 공습2이동(self.ctx)
"""

"""
class 공습2이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=500, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=501, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=502, patrol_name='PatrolDataBridge0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 공습3(self.ctx)
"""

"""
class 공습3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[400])
        self.spawn_monster(spawn_ids=[401])
        self.spawn_monster(spawn_ids=[402])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 공습3이동(self.ctx)
"""

"""
class 공습3이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=400, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=401, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=402, patrol_name='PatrolDataBridge0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[999]):
            return 실패선언(self.ctx)
        if self.monster_dead(spawn_ids=[600,601,602,500,501,502,400,401,402]):
            return 공습4(self.ctx)
"""

"""
class 공습4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[400])
        self.spawn_monster(spawn_ids=[401])
        self.spawn_monster(spawn_ids=[402])
        self.spawn_monster(spawn_ids=[500])
        self.spawn_monster(spawn_ids=[501])
        self.spawn_monster(spawn_ids=[502])
        self.spawn_monster(spawn_ids=[600])
        self.spawn_monster(spawn_ids=[601])
        self.spawn_monster(spawn_ids=[602])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 공습4이동(self.ctx)
"""

"""
class 공습4이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=400, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=401, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=402, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=500, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=501, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=502, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=600, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=601, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=602, patrol_name='PatrolDataBridge0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[999]):
            return 준비(self.ctx)
        if self.monster_dead(spawn_ids=[600,601,602,500,501,502,400,401,402]):
            return 공습5(self.ctx)
"""

"""
class 공습5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[500])
        self.spawn_monster(spawn_ids=[501])
        self.spawn_monster(spawn_ids=[502])
        self.spawn_monster(spawn_ids=[600])
        self.spawn_monster(spawn_ids=[601])
        self.spawn_monster(spawn_ids=[602])
        self.spawn_monster(spawn_ids=[400])
        self.spawn_monster(spawn_ids=[401])
        self.spawn_monster(spawn_ids=[402])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 공습5이동(self.ctx)
"""

"""
class 공습5이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=400, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=401, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=402, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=500, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=501, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=502, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=600, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=601, patrol_name='PatrolDataBridge0')
        self.move_npc(spawn_id=602, patrol_name='PatrolDataBridge0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[999]):
            return 실패선언(self.ctx)
        if self.monster_dead(spawn_ids=[600,601,602,500,501,502,400,401,402]):
            return 공습종료(self.ctx)
"""

"""
class 공습종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보스전연출준비(self.ctx)
"""

class 보스전연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        self.visible_my_pc(is_visible=True) # 캐릭터 보임
        self.move_user(map_id=52010055, portal_id=4)
        self.remove_buff(box_id=9002, skill_id=99910311) # 포탑으로변신
        self.reset_camera()
        self.set_mesh(trigger_ids=[10002,10003,10004,10005], visible=True) # 1차 전투 링생성
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보스전연출시작(self.ctx)


class 보스전연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        self.select_camera(trigger_id=4006)
        self.spawn_monster(spawn_ids=[1], auto_target=False) # 함교 연출용 블리체
        self.spawn_monster(spawn_ids=[2], auto_target=False) # 함교 연출용 네이린
        self.spawn_monster(spawn_ids=[2000], auto_target=False) # 연출용 보스소환

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보스전연출1(self.ctx)


class 보스전연출1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=2000, sequence_name='Attack_01_A')
        self.add_cinematic_talk(npc_id=29000382, msg='$52010055_QD__52010055__21$', duration=3000, align=Align.Right)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Suprise_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보스전시작(self.ctx)


class 보스전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4019)
        self.destroy_monster(spawn_ids=[2000])
        self.spawn_monster(spawn_ids=[2001]) # 전투용 보스 소환
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 보스사망체크(self.ctx)


class 보스사망체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True) # 캐릭터 보임
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 보스전끝크림슨발록대사1(self.ctx)


class 보스전끝크림슨발록대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        self.set_mesh(trigger_ids=[10002,10003,10004,10005]) # 1차 전투 링 해제
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[1], auto_target=False) # 함교 연출용 블리체
        self.spawn_monster(spawn_ids=[2], auto_target=False) # 함교 연출용 네이린
        self.spawn_monster(spawn_ids=[13], auto_target=False) # 엔딩 연출용 콘대르
        self.spawn_monster(spawn_ids=[14], auto_target=False) # 엔딩 연출용 메이슨
        self.spawn_monster(spawn_ids=[15], auto_target=False) # 엔딩 연출용 샤텐
        self.spawn_monster(spawn_ids=[2002], auto_target=False) # 연출용 보스소환
        self.move_user(map_id=52010055, portal_id=5) # 스카이 포트리스 작전실로 텔레포트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 엔딩연출크림슨발록보스1(self.ctx)


class 엔딩연출크림슨발록보스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=14, rotation=-10.0)
        self.set_npc_rotation(spawn_id=15, rotation=10.0)
        self.select_camera(trigger_id=4006)
        self.move_user_path(patrol_name='PatrolDataEndPC0') # 유저 보스잡고 걸어감
        self.set_npc_emotion_sequence(spawn_id=2002, sequence_name='Dead_01_A')
        self.add_cinematic_talk(npc_id=29000382, msg='$52010055_QD__52010055__22$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 엔딩연출크림슨발록보스2(self.ctx)


class 엔딩연출크림슨발록보스2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.change_monster(from_spawn_id=2002, to_spawn_id=2003) # 함교 연출용 블리체
        self.set_npc_emotion_sequence(spawn_id=2003, sequence_name='Dead_01_A')
        self.set_scene_skip(state=맵이동, action='nextState')
        self.select_camera_path(path_ids=[4007,4008], return_view=False)
        self.visible_my_pc(is_visible=False) # 캐릭터 숨김
        self.set_npc_emotion_sequence(spawn_id=13, sequence_name='Attack_Idle_A,Attack_Idle_A,Attack_Idle_A,Attack_Idle_A')
        self.set_npc_emotion_sequence(spawn_id=14, sequence_name='Attack_Idle_A,Attack_Idle_A,Attack_Idle_A,Attack_Idle_A')
        self.set_npc_emotion_sequence(spawn_id=15, sequence_name='Attack_Idle_A,Attack_Idle_A,Attack_Idle_A,Attack_Idle_A')
        self.add_cinematic_talk(npc_id=11003776, illust_id='Conder_normal', msg='$52010055_QD__52010055__23$', duration=2000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 엔딩연출샤텐1(self.ctx)


class 엔딩연출샤텐1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2002])
        self.set_npc_emotion_sequence(spawn_id=13, sequence_name='Attack_Idle_A')
        self.set_npc_emotion_sequence(spawn_id=14, sequence_name='Attack_Idle_A')
        self.set_npc_emotion_sequence(spawn_id=15, sequence_name='Attack_Idle_A')
        self.add_cinematic_talk(npc_id=11003584, illust_id='Schatten_normal', msg='$52010055_QD__52010055__24$', duration=3000, align=Align.Left)
        self.select_camera_path(path_ids=[4009,4010], return_view=False)
        self.select_camera(trigger_id=4010)
        self.set_npc_emotion_sequence(spawn_id=15, sequence_name='Attack_Idle_A,Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 엔딩연출메이슨1(self.ctx)


class 엔딩연출메이슨1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003586, illust_id='Mason_closeEye', msg='$52010055_QD__52010055__25$', duration=1500, align=Align.Left)
        self.select_camera(trigger_id=4014)
        self.select_camera_path(path_ids=[4014,4015], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=13, sequence_name='Attack_Idle_A')
        self.set_npc_emotion_sequence(spawn_id=14, sequence_name='Attack_Idle_A,Attack_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 엔딩연출콘대르1(self.ctx)


class 엔딩연출콘대르1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[500], visible=True)
        self.set_effect(trigger_ids=[501], visible=True)
        self.add_cinematic_talk(npc_id=11003776, illust_id='Conder_normal', msg='$52010055_QD__52010055__26$', duration=3000, align=Align.Left)
        self.select_camera_path(path_ids=[4016,4017], return_view=False)
        self.move_npc(spawn_id=13, patrol_name='PatrolDataCondorAttack1') # 엔딩 연출용 콘대르 돌진

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 엔딩연출콘대르2(self.ctx)


class 엔딩연출콘대르2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4006)
        self.set_effect(trigger_ids=[5000], visible=True)
        self.set_effect(trigger_ids=[5000], visible=True)
        self.set_effect(trigger_ids=[502], visible=True)
        self.set_npc_emotion_sequence(spawn_id=13, sequence_name='Attack_01_G,Attack_02_G,Attack_03_G,Attack_06_G')
        self.set_npc_emotion_sequence(spawn_id=2003, sequence_name='Stun_A,Stun_A,Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3002):
            return 엔딩연출클림슨발록사망1(self.ctx)


class 엔딩연출클림슨발록사망1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=2003, sequence_name='Dead_01_A')
        self.add_cinematic_talk(npc_id=29000382, msg='$52010055_QD__52010055__27$', duration=3000, align=Align.Right) # 크아악

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 엔딩연출준비1(self.ctx)


class 엔딩연출준비1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        self.destroy_monster(spawn_ids=[2003], arg2=False) # 엔딩연출용크림슨발록
        self.destroy_monster(spawn_ids=[13]) # 엔딩 연출용 콘대르
        self.destroy_monster(spawn_ids=[14]) # 엔딩 연출용 콘대르
        self.destroy_monster(spawn_ids=[15]) # 엔딩 연출용 콘대르
        self.move_user(map_id=52010055, portal_id=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 엔딩연출준비2(self.ctx)


class 엔딩연출준비2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 크림슨대사준비1(self.ctx)


"""
class 엔딩연출크림슨발록대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.select_camera(trigger_id=4006)
        self.add_cinematic_talk(npc_id=29000382, msg='$52010055_QD__52010055__28$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 크림슨대사준비1(self.ctx)
"""

class 크림슨대사준비1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[700], auto_target=False)
        self.spawn_monster(spawn_ids=[701], auto_target=False)
        self.spawn_monster(spawn_ids=[702], auto_target=False)
        self.spawn_monster(spawn_ids=[703], auto_target=False)
        self.spawn_monster(spawn_ids=[704], auto_target=False)
        self.spawn_monster(spawn_ids=[705], auto_target=False)
        self.spawn_monster(spawn_ids=[706], auto_target=False)
        self.spawn_monster(spawn_ids=[707], auto_target=False)
        self.visible_my_pc(is_visible=False) # 캐릭터 숨김
        self.move_user(map_id=52010055, portal_id=7) # 유저를 포탑으로 텔레포트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 엔딩연출크림슨카메라1(self.ctx)


class 엔딩연출크림슨카메라1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        self.select_camera(trigger_id=4023)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 엔딩연출크림슨대사1(self.ctx)


class 엔딩연출크림슨대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=29000378, msg='$52010055_QD__52010055__29$', duration=3000, align=Align.Right)
        self.move_npc(spawn_id=700, patrol_name='PatrolData700') # 엔딩 연출용 크림슨도망
        self.move_npc(spawn_id=701, patrol_name='PatrolData701') # 엔딩 연출용 크림슨도망
        self.move_npc(spawn_id=702, patrol_name='PatrolData702') # 엔딩 연출용 크림슨도망
        self.move_npc(spawn_id=703, patrol_name='PatrolData703') # 엔딩 연출용 크림슨도망
        self.move_npc(spawn_id=704, patrol_name='PatrolData704') # 엔딩 연출용 크림슨도망
        self.move_npc(spawn_id=705, patrol_name='PatrolData705') # 엔딩 연출용 크림슨도망
        self.move_npc(spawn_id=706, patrol_name='PatrolData706') # 엔딩 연출용 크림슨도망
        self.move_npc(spawn_id=707, patrol_name='PatrolData707') # 엔딩 연출용 크림슨도망

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 엔딩이동준비1(self.ctx)


class 엔딩이동준비1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.destroy_monster(spawn_ids=[-1])
        self.move_user(map_id=52010055, portal_id=8, box_id=9002)
        self.visible_my_pc(is_visible=True) # 캐릭터 보임

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 엔딩이동준비2(self.ctx)


class 엔딩이동준비2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4024)
        self.spawn_monster(spawn_ids=[1], auto_target=False) # 함교 연출용 블리체
        self.spawn_monster(spawn_ids=[2], auto_target=False) # 함교 연출용 네이린
        self.spawn_monster(spawn_ids=[13], auto_target=False) # 함교 연출용 콘대르
        self.spawn_monster(spawn_ids=[14], auto_target=False) # 함교 연출용 블리체
        self.spawn_monster(spawn_ids=[15], auto_target=False) # 함교 연출용 네이린
        self.spawn_monster(spawn_ids=[10001], auto_target=False) # 함교 연출용 해군
        self.spawn_monster(spawn_ids=[10002], auto_target=False) # 함교 연출용 해군

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 엔딩NPC이동1(self.ctx)


class 엔딩NPC이동1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='PatrolDataEndPC2') # 엔딩 연출용 유저 이동
        self.move_npc(spawn_id=13, patrol_name='PatrolDataEndCondor1') # 엔딩 연출용 콘대르 이동
        self.move_npc(spawn_id=14, patrol_name='PatrolDataEndMason1') # 엔딩 연출용 메이슨 이동
        self.move_npc(spawn_id=15, patrol_name='PatrolDataEndSchatten1') # 엔딩 연출용 샤텐 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 엔딩대사콘대르1(self.ctx)


class 엔딩대사콘대르1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawn_id=15, rotation=60.0)
        self.set_npc_rotation(spawn_id=14, rotation=330.0)
        self.set_npc_emotion_sequence(spawn_id=13, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003776, illust_id='Conder_normal', msg='$52010055_QD__52010055__30$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 엔딩대사샤텐1(self.ctx)


class 엔딩대사샤텐1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=15, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003584, illust_id='Schatten_normal', msg='$52010055_QD__52010055__31$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 엔딩대사메이슨1(self.ctx)


class 엔딩대사메이슨1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10000])
        self.set_mesh(trigger_ids=[10001])
        self.set_mesh(trigger_ids=[10002])
        self.set_mesh(trigger_ids=[10003])
        self.set_mesh(trigger_ids=[10004])
        self.set_npc_emotion_sequence(spawn_id=14, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003586, illust_id='Mason_closeEye', msg='$52010055_QD__52010055__32$', duration=3000, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 함교로카메라전환1(self.ctx)


class 함교로카메라전환1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4025)
        self.visible_my_pc(is_visible=False) # 캐릭터 숨김
        self.move_user(map_id=52010055, portal_id=2) # 함교 내부로 텔레포트
        self.set_onetime_effect(id=10, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return 엔딩대사네이린1(self.ctx)


class 엔딩대사네이린1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=22, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003536, illust_id='Neirin_normal', msg='$52010055_QD__52010055__33$', duration=4000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11003536, illust_id='Neirin_normal', msg='$52010055_QD__52010055__34$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 엔딩대사블리체1(self.ctx)


class 엔딩대사블리체1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=21, sequence_name='Talk_A')
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010055_QD__52010055__35$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11003533, illust_id='Bliche_normal', msg='$52010055_QD__52010055__36$', duration=5000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 엔딩연출종료1(self.ctx)


class 엔딩연출종료1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 맵이동(self.ctx)


class 맵이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.visible_my_pc(is_visible=True) # 캐릭터 보임
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=9002, type='trigger', achieve='rescueskyfortress')
        self.set_onetime_effect(id=12, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.move_user(map_id=52010052) # 스카이 포트리스 작전실로 텔레포트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return None # Missing State: State


initial_state = 준비
