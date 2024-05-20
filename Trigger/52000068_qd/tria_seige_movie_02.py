""" trigger/52000068_qd/tria_seige_movie_02.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 연출페이즈2검사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[20002264], quest_ids=[20002264], quest_states=[3]):
            # 챕터6 에필로그 [20002264 진정한 트라이아의 방패] 완료 시
            return 연출페이즈2시작(self.ctx)


# 챕터5 에필로그 [10002105 엇갈리는 마음]완료 시 연출맵으로 이동
class 연출페이즈2시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Quit, action='exit')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000068, portal_id=3)
        self.spawn_monster(spawn_ids=[10024,10025,10026,10027,10028,10029,10030,10031,10032,10033,10034], auto_target=False)
        self.spawn_monster(spawn_ids=[13000,13001,13002,13003,13004,13005,13006,13007], auto_target=False)
        self.destroy_monster(spawn_ids=[11000,11001,11002,11003,11004,11005,11006,11007], arg2=False)
        self.set_visible_breakable_object(trigger_ids=[5000,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012])
        self.set_sound(trigger_id=90001, enable=True) # TriaAttack

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 연출페이즈2대사01(self.ctx)


class 연출페이즈2대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.select_camera_path(path_ids=[15000,15001], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001966, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__0$', time=7)
        self.set_skip(state=연출페이즈2대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출페이즈2대사01스킵(self.ctx)


class 연출페이즈2대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사02(self.ctx)


class 연출페이즈2대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001966, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__1$', time=7)
        self.set_skip(state=연출페이즈2대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출페이즈2대사02스킵(self.ctx)


class 연출페이즈2대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사03(self.ctx)


class 연출페이즈2대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15002,15003], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001901, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__2$', time=7)
        self.set_skip(state=연출페이즈2대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출페이즈2대사03스킵(self.ctx)


class 연출페이즈2대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사04(self.ctx)


class 연출페이즈2대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15004], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001961, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__3$', time=7)
        self.set_skip(state=연출페이즈2대사04스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출페이즈2대사04스킵(self.ctx)


class 연출페이즈2대사04스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사04b(self.ctx)


class 연출페이즈2대사04b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15005,15006], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001972, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__4$', time=7)
        self.set_skip(state=연출페이즈2대사04b스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 연출페이즈2대사04b스킵(self.ctx)


class 연출페이즈2대사04b스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사05(self.ctx)


class 연출페이즈2대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15007], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001972, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__5$', time=7)
        self.set_skip(state=연출페이즈2대사05스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출페이즈2대사05스킵(self.ctx)


class 연출페이즈2대사05스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사05b(self.ctx)


class 연출페이즈2대사05b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15100,15101], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001970, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__17$', time=7)
        self.set_skip(state=연출페이즈2대사05b스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출페이즈2대사05b스킵(self.ctx)


class 연출페이즈2대사05b스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사06(self.ctx)


class 연출페이즈2대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15102,15103], return_view=False)
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__6$', duration=7000, align=Align.Center)
        self.set_skip(state=연출페이즈2대사06스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출페이즈2대사06스킵(self.ctx)


class 연출페이즈2대사06스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사07(self.ctx)


class 연출페이즈2대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15104,15105], return_view=False)
        self.move_npc(spawn_id=13000, patrol_name='MS2PatrolData_top_ereb_go') # 에레브 이동
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__7$', duration=7000, align=Align.Center)
        self.set_skip(state=연출페이즈2대사07스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출페이즈2대사07스킵(self.ctx)


class 연출페이즈2대사07스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사08(self.ctx)


class 연출페이즈2대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15106], return_view=False)
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_sad', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__8$', duration=7000, align=Align.Center)
        self.set_skip(state=연출페이즈2대사08스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출페이즈2대사08스킵(self.ctx)


class 연출페이즈2대사08스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사09(self.ctx)


class 연출페이즈2대사09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15107,15108], return_view=False)
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_closeEye', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__9$', duration=7000, align=Align.Center)
        self.set_skip(state=연출페이즈2대사09스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출페이즈2대사09스킵(self.ctx)


class 연출페이즈2대사09스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사10(self.ctx)


class 연출페이즈2대사10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__10$', duration=7000, align=Align.Center)
        self.set_skip(state=연출페이즈2대사10스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출페이즈2대사10스킵(self.ctx)


class 연출페이즈2대사10스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사11(self.ctx)


class 연출페이즈2대사11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15109], return_view=False)
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_closeEye', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__11$', duration=7000, align=Align.Center)
        self.set_skip(state=연출페이즈2대사11스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출페이즈2대사11스킵(self.ctx)


class 연출페이즈2대사11스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사12(self.ctx)


class 연출페이즈2대사12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15110], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001973, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__18$', time=7)
        self.set_skip(state=연출페이즈2대사12스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출페이즈2대사12스킵(self.ctx)


class 연출페이즈2대사12스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사13(self.ctx)


class 연출페이즈2대사13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15111,15112], return_view=False)
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__12$', duration=7000, align=Align.Center)
        self.set_skip(state=연출페이즈2대사13스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 연출페이즈2대사13스킵(self.ctx)


class 연출페이즈2대사13스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사14(self.ctx)


class 연출페이즈2대사14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__13$', duration=7000, align=Align.Center)
        self.set_skip(state=연출페이즈2대사14스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출페이즈2대사14스킵(self.ctx)


class 연출페이즈2대사14스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사15(self.ctx)


class 연출페이즈2대사15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15113,15114], return_view=False)
        self.move_npc(spawn_id=13000, patrol_name='MS2PatrolData_top_ereb_back') # 에레브 이동
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_closeEye', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__14$', duration=7000, align=Align.Center)
        self.set_skip(state=연출페이즈2대사15스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출페이즈2대사15스킵(self.ctx)


class 연출페이즈2대사15스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사16(self.ctx)


class 연출페이즈2대사16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_closeEye', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__15$', duration=7000, align=Align.Center)
        self.set_skip(state=연출페이즈2대사16스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출페이즈2대사16스킵(self.ctx)


class 연출페이즈2대사16스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        return 연출페이즈2대사17(self.ctx)


class 연출페이즈2대사17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[15115,15116], return_view=False)
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__16$', duration=7000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 페이드아웃(self.ctx)


class 페이드아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 페이드아웃_1(self.ctx)


class 페이드아웃_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2000001, portal_id=17)


initial_state = 연출페이즈2검사
