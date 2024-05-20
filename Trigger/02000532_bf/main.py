""" trigger/02000532_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001], visible=True)
        self.set_mesh(trigger_ids=[3002,3003], visible=True)
        self.set_mesh(trigger_ids=[3004], visible=True)
        self.set_portal(portal_id=1)
        self.set_effect(trigger_ids=[7001])
        self.set_effect(trigger_ids=[7006])
        self.set_effect(trigger_ids=[7007])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip() # Missing State: State
        self.spawn_monster(spawn_ids=[216,101,102,103,104,105,106,107,108,109,111,112,113])
        self.spawn_monster(spawn_ids=[110,111])
        self.move_npc(spawn_id=110, patrol_name='MS2PatrolData_8000')
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_8001')
        self.set_portal(portal_id=1)
        self.set_mesh(trigger_ids=[3000,3001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=목표, action='nextState')
        self.select_camera_path(path_ids=[604,603])
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.show_caption(type='VerticalCaption', title='$02000532_BF__MAIN__0$', desc='$02000532_BF__MAIN__1$', align=Align.Center | Align.Right, duration=3000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 목표(self.ctx)


class 목표(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.lock_my_pc()
        self.reset_camera(interpolation_time=1.0)
        self.set_event_ui(type=1, arg2='$02000532_BF__MAIN__2$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 문들어가기(self.ctx)


class 문들어가기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=1, arg2='$02000532_BF__MAIN__3$', arg3='3000')
        self.set_effect(trigger_ids=[7006], visible=True)
        self.set_effect(trigger_ids=[7007], visible=True)
        self.spawn_monster(spawn_ids=[408])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[408], auto_target=False):
            return 문이열림(self.ctx)


class 문이열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3004])
        self.add_balloon_talk(spawn_id=112, msg='$02000532_BF__MAIN__4$', duration=3500)
        self.add_balloon_talk(spawn_id=112, msg='$02000532_BF__MAIN__5$', duration=3500, delay_tick=3500)
        self.add_balloon_talk(spawn_id=102, msg='$02000532_BF__MAIN__6$', duration=3500, delay_tick=500)
        self.add_balloon_talk(spawn_id=113, msg='$02000532_BF__MAIN__7$', duration=3500, delay_tick=900)
        self.set_npc_emotion_loop(spawn_id=102, sequence_name='Talk_A', duration=10000.0)
        self.set_npc_emotion_loop(spawn_id=113, sequence_name='Sit_Down_A', duration=10000.0)
        self.set_npc_emotion_loop(spawn_id=112, sequence_name='Talk_A', duration=10000.0)
        self.set_effect(trigger_ids=[7001], visible=True)
        self.set_mesh(trigger_ids=[3000,3001])
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702], job_code=0):
            return 경계하기(self.ctx)


class 경계하기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.lock_my_pc(is_lock=True)
        self.set_scene_skip(state=흑성회의반격, action='nextState')
        self.add_balloon_talk(spawn_id=104, msg='$02000532_BF__MAIN__8$', duration=3500)
        self.add_balloon_talk(spawn_id=105, msg='$02000532_BF__MAIN__9$', duration=3500, delay_tick=2500)
        self.add_balloon_talk(spawn_id=103, msg='$02000532_BF__MAIN__10$', duration=3500, delay_tick=2800)
        self.set_effect(trigger_ids=[7006])
        self.set_effect(trigger_ids=[7007])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 통신을받은제이부하(self.ctx)


class 통신을받은제이부하(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[602], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 통신을받은제이부하2(self.ctx)


class 통신을받은제이부하2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=205, msg='$02000532_BF__MAIN__11$', duration=3500, delay_tick=500)
        self.add_balloon_talk(spawn_id=300, msg='$02000532_BF__MAIN__12$', duration=3500, delay_tick=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 불안한제이(self.ctx)


class 불안한제이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 불안한제이2(self.ctx)


class 불안한제이2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=4000, script='$02000532_BF__MAIN__13$')
        self.add_balloon_talk(spawn_id=205, msg='$02000532_BF__MAIN__14$', duration=3500, delay_tick=4100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 흑성회의반격(self.ctx)


class 흑성회의반격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_mesh(trigger_ids=[3002,3003])
        self.lock_my_pc()
        self.reset_camera(interpolation_time=1.0)
        self.set_event_ui(type=1, arg2='$02000532_BF__MAIN__15$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 흑성회의반격2(self.ctx)


class 흑성회의반격2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,110,111,112,113])
        self.spawn_monster(spawn_ids=[401,402,403,404,412,405])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 흑성회의반격22(self.ctx)


class 흑성회의반격22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=21450001, illust='Mafia1_normal', duration=3000, script='$02000532_BF__MAIN__16$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 골목체크(self.ctx)


class 골목체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=3000, script='$02000532_BF__MAIN__17$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705], job_code=0):
            return 길목에서나오는몬스터(self.ctx)


class 길목에서나오는몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[108,109])
        self.spawn_monster(spawn_ids=[406,407,409,410,411])
        self.add_balloon_talk(spawn_id=409, msg='$02000532_BF__MAIN__18$', duration=3500, delay_tick=1500)
        self.add_balloon_talk(spawn_id=410, msg='$02000532_BF__MAIN__19$', duration=3500, delay_tick=1500)
        self.add_balloon_talk(spawn_id=407, msg='$02000532_BF__MAIN__20$', duration=3500, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[401,402,403,404,405,406,407,409,410,411,412]):
            return 차생성2(self.ctx)


class 차생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=3000, script='$02000532_BF__MAIN__21$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 엘리베이터안내(self.ctx)


class 엘리베이터안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000532_BF__MAIN__22$', arg3='3000')
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)


initial_state = idle
